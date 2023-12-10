title: 鼠标反应
hash: 047288a3fddc3e00aa932fe2d7d9f62628bd9d8e5e6d54ceac2b7b5a836e6f0f
locale: zh
language: Chinese

鼠标反应是通过MOUSE_RESPONSE项目来收集的。MOUSE_RESPONSE主要用来收集个别鼠标点击。如果您想要收集鼠标轨迹，请查看MOUSETRAP插件：

- %link:mousetracking%

[TOC]


## 响应变量

MOUSE_RESPONSE设置了标准的响应变量，如下所述：

- %link:manual/variables%


## 鼠标按钮名称

鼠标按钮有一个数字（`1`等）以及一个名称（`left_button`等）。两者都可以用来指定正确和允许的响应，但`response`变量将被设置为一个数字。

- `left_button` 对应 `1`
- `middle_button` 对应 `2`
- `right_button` 对应 `3`
- `scroll_up` 对应 `4`
- `scroll_down` 对应 `5`


## 正确反应

*正确反应* 字段指出了哪个反应被视为正确的。正确反应后，`correct`变量自动设置为1；错误反应或超时（即其他一切）后，`correct` 设置为0；如果没有指定正确的反应，`correct` 设置为'undefined'。

您可以通过三种主要方式指定正确的反应：

- *将字段留空。* 如果您将*正确反应* 字段留空，OpenSesame将自动检查是否定义了一个名为`correct_response`的变量，如果有，则使用这个变量作为正确反应。
- *输入一个字面值。* 您可以明确输入一个响应，如1。这只在正确响应是固定的情况下有用。
- *输入一个变量名。* 您可以输入一个变量，例如`{cr}`。在这种情况下，这个变量将用于正确响应。

请注意，正确响应指的是哪个鼠标按钮被点击，而不是哪个感兴趣区域被点击（ROI），有关ROI的更多信息，请看下面的部分。

## 允许的响应

*允许的响应* 字段指出了一系列允许的响应。除了'Escape'之外，所有其他响应都将被忽略，这将暂停实验。允许的响应应该是一个用分号分隔的响应列表，例如'1;3'来允许左键和右键。若接受所有响应，请将*允许的响应* 字段留空。

请注意，允许的响应指的是可以点击哪个鼠标按钮，而不是可以点击哪个感兴趣区域（ROI），有关ROI的更多信息，请看下面的部分。


include: include/timeout.md--%

## 坐标和感兴趣区域 (ROIs)

`cursor_x` 和 `cursor_y` 变量持有鼠标点击的位置。

如果您指明了一个链接的SKETCHPAD，变量`cursor_roi`将持有一个包含点击坐标的元素名称的逗号分隔列表。换句话说，SKETCHPAD上的元素自动作为鼠标点击的感兴趣区域。

如果响应的正确性取决于点击了哪个ROI，您不能使用`correct_response`变量，因为它目前仅指的是哪个鼠标按钮被点击。相反，您需要使用一个简单的脚本。

在Python INLINE_SCRIPT中，您可以如下操作：

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

在OSWeb中使用INLINE_JAVASCRIPT，您可以这样做：

```js
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


video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  收集鼠标点击和使用感兴趣区域。
--%

## 在Python中收集鼠标响应

您可以在Python中使用`mouse`对象来收集鼠标响应：

- %link:manual/python/mouse%