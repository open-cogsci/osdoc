title: 鼠标和触摸响应
hash: d6f7dcf58a399be886fd23f0ed29e9898c1beae44c3c8f6d076e26f96471d4f0
locale: zh
language: Chinese

鼠标响应通过 MOUSE_RESPONSE item 收集。MOUSE_RESPONSE 主要用于收集单次鼠标点击。在支持触摸的设备上，触摸响应（TOUCH_RESPONSE item）通常会以与触摸坐标处的鼠标按钮 1 点击相同的方式注册，因此同一个 item 和逻辑通常可以同时用于鼠标和触摸输入。如果你想收集鼠标光标轨迹，可以查看 MOUSETRAP plugins：

- %link:mousetracking%

[TOC]


## 响应变量

MOUSE_RESPONSE 会设置此处所述的标准响应变量：

- %link:manual/variables%

此外，以下变量与鼠标和触摸响应相关：

| Variable | Description |
|---|---|
| `response` | 被点击的鼠标按钮。该值存储为数字（`1` = 左键，`2` = 中键，`3` = 右键，`4` = 向上滚动，`5` = 向下滚动）。发生超时时，`response` 会被设为 `None`。 |
| `response_time` | 以毫秒为单位的响应时间；如果未作出响应，则为已注册的超时时间。 |
| `correct` | 根据按钮正确性自动设置：正确的鼠标按钮响应为 `1`，错误的鼠标按钮响应或超时为 `0`，如果未指定正确响应则为 `undefined`。 |
| `cursor_x` | 点击或触摸的 x 坐标。 |
| `cursor_y` | 点击或触摸的 y 坐标。 |
| `cursor_roi` | 包含被点击坐标的 sketchpad 元素名称列表，以分号分隔。如果元素重叠，可以列出多个名称。该变量报告点击发生的位置；它不会自动判断 `correct`。 |


## 鼠标按钮名称

鼠标按钮既有数字（`1` 等），也有名称（`left_button` 等）。两者都可用于指定正确响应和允许响应，但 `response` 变量将被设为数字。

- `left_button` 对应 `1`
- `middle_button` 对应 `2`
- `right_button` 对应 `3`
- `scroll_up` 对应 `4`
- `scroll_down` 对应 `5`


## 正确响应

*Correct response* 字段用于指示哪个响应被视为正确。作出正确响应后，`correct` 变量会自动设为 1；作出错误响应或发生超时后（即其他所有情况），`correct` 会被设为 0；如果未指定正确响应，`correct` 会被设为 'undefined'。

你可以通过三种主要方式指示正确响应：

- *将字段留空。* 如果你将 *Correct response* 字段留空，OpenSesame 会自动检查是否定义了名为 `correct_response` 的变量，如果有，则将该变量用作正确响应。
- *输入一个字面值。* 你可以显式输入一个响应，例如 1。只有在正确响应固定时，这样做才有用。
- *输入一个变量名。* 你可以输入一个变量，例如 '{cr}'。在这种情况下，该变量将被用作正确响应。

请注意，正确响应指的是点击了哪个鼠标按钮，而不是点击了哪个感兴趣区域（ROI）。如果正确性取决于点击位置而不是鼠标按钮，你需要根据 `cursor_roi` 自行判断正确性；有关 ROI 的更多信息，请参见下文。


## 允许响应

*Allowed responses* 字段表示允许响应的列表。所有其他响应都会被忽略，只有 'Escape' 例外，它会暂停实验。允许响应应为以分号分隔的响应列表，例如用 '1;3' 来允许鼠标左键和右键。要接受所有响应，请将 *Allowed responses* 字段留空。

请注意，允许响应指的是允许点击哪个鼠标按钮，而不是允许点击哪个感兴趣区域（ROI）；有关 ROI 的更多信息，请参见下文。


%--include: include/timeout.md--%

## Coordinates and regions of interest (ROIs)</notranslate>

`cursor_x` 和 `cursor_y` 变量保存鼠标点击的位置。

如果你指定了一个关联的 SKETCHPAD，变量 `cursor_roi` 将保存一个以分号分隔的名称列表，这些名称对应包含被点击坐标的元素。换句话说，SKETCHPAD 上的元素会自动作为鼠标点击的兴趣区。

`cursor_roi` 变量表示点击发生在何处，而 `response` 表示点击了哪个鼠标按钮。如果多个已命名元素在点击位置发生重叠，`cursor_roi` 可以包含多个元素名称。

如果响应的正确性取决于点击了哪个 ROI，那么你不能为此使用 `correct_response` 变量，因为它只涉及点击了哪个鼠标按钮。你需要改为使用一个简单的脚本，根据 `cursor_roi` 判断正确性，并在必要时覆盖 `correct`。

在 Python INLINE_SCRIPT 中，你可以这样做：

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('correct!')
    correct = 1
else:
    print('incorrect!')
    correct = 0
```

在使用 INLINE_JAVASCRIPT 的 OSWeb 中，你可以这样做：

```javascript
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('correct!')
    correct = 1
} else {
    console.log('incorrect!')
    correct = 0
}
```

这里，`'my_roi'` 只是一个 sketchpad 元素名称的示例。在真实实验中，请将它替换为应被视为正确的 ROI 名称。为避免歧义，已命名元素在一个 sketchpad 中应当保持唯一。


## 触摸响应

在支持触摸的设备上，每次轻触通常都会在被触碰的坐标处注册为一次鼠标按钮 1 响应。这意味着，MOUSE_RESPONSE item 通常可以同时用于鼠标点击和触摸轻触，而无需进一步修改。

在实践中，这意味着触摸响应的行为如下：

- 按钮通常会被注册为 `1`
- 触摸位置会存储在 `cursor_x` 和 `cursor_y` 中
- 如果关联了一个 sketchpad，则可以通过 `cursor_roi` 识别被触碰的元素

这对于需要同时在桌面设备和触摸屏设备上运行的实验会很有帮助。

### 示例：使用 MOUSE_RESPONSE 的触摸响应

例如，考虑一个简单的选择任务，其中屏幕左侧和右侧显示两个较大的 sketchpad 元素。如果参与者在触摸屏上轻触左侧元素：

- `response` 通常会被设为 `1`
- `cursor_x` 和 `cursor_y` 将包含触摸坐标
- `cursor_roi` 可能包含被触碰元素的名称，例如 `left_option`

这意味着，触摸输入可以与鼠标输入以相同方式处理。如果正确性取决于被触碰的元素而不是按钮，你可以使用上文描述的相同 `cursor_roi` 逻辑。

### 示例：使用 `touch_response` plug-in

对于你想将屏幕划分为离散响应区域的实验（例如按钮网格），`touch_response` plug-in 提供了一种比处理原始坐标更简单、更方便的方法。它将显示区域划分为由行和列组成的网格，并将每次响应编码为一个单独的数字，按从左到右、从上到下的顺序计数。

例如，使用 2 列和 3 行时，显示区域划分如下：

| | 第 1 列 | 第 2 列 |
|---|---|---|
| **第 1 行** | 1 | 2 |
| **第 2 行** | 3 | 4 |
| **第 3 行** | 5 | 6 |

因此，如果你指定 2 列和 1 行，显示区域将被划分为两个响应区域：

| 左半边 | 右半边 |
|---|---|
| `1` | `2` |

在一个简单的是/否任务中，你可以指定：

- `1` = 是
- `2` = 否

如果正确答案是“是”，请将 *Correct response* 字段设置为 `1`。这样当参与者轻触屏幕左半边时，OpenSesame 就会自动将 `correct` 设为 1。

> [!NOTE]
> `touch_response` 插件不使用具名 sketchpad 元素或 `cursor_roi`。响应仅编码为网格位置。

> [!NOTE]
> 触摸输入的确切行为可能取决于用于运行实验的平台和 backend。

> [!NOTE]
> MOUSE_RESPONSE 项目只捕获单次触摸响应。如果多根手指同时触摸屏幕，则只会注册一个响应。


%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Collecting mouse clicks and using regions of interest.
--%

## 在 Python 中收集鼠标响应

你可以使用 `mouse` 对象在 Python 中收集鼠标响应：

- %link:manual/python/mouse%