title: 鼠标反应
hash: 9e348c65c44cf1d0e1e152976c013b0a235f432d16ceeb3fff09001f8c9d0e7b
locale: zh
language: Chinese

鼠标响应通过 MOUSE_RESPONSE 项目进行收集。MOUSE_RESPONSE 主要用于收集单个鼠标点击。如果您想要收集鼠标光标轨迹，请查看 MOUSETRAP 插件：

- %link:mousetracking%

[TOC]


## 响应变量

MOUSE_RESPONSE 设置标准响应变量，如下所述：

- %link:manual/variables%


## 鼠标按钮名称

鼠标按钮有一个编号（`1` 等）以及一个名称（`left_button` 等）。两者都可以用来指定正确的和允许的响应，但 `response` 变量将被设置为一个数字。

- `left_button` 对应于 `1`
- `middle_button` 对应于 `2`
- `right_button` 对应于 `3`
- `scroll_up` 对应于 `4`
- `scroll_down` 对应于 `5`


## 正确响应

*正确响应* 字段表示哪个响应被认为是正确的。在正确响应之后，`correct` 变量自动设置为 1；在不正确的响应或超时（即其他所有情况）之后，`correct`设置为 0; 如果没有指定正确的响应，`correct`设置为'未定义'。

您可以通过以下三种主要方式指示正确的响应：

- *将字段保留为空。* 如果您将 *正确响应* 字段留空，OpenSesame 将自动检查是否已定义一个名为 `correct_response` 的变量，并在有的情况下使用此变量进行正确响应。
- *输入文字。* 您可以明确输入响应，例如 1。这仅在正确响应是固定的情况下有用。
- *输入变量名。* 您可以输入一个变量，例如 '{cr}'。在这种情况下，这个变量将用于正确响应。


## 允许的响应

*允许的响应* 字段 表示允许响应的列表。所有其他响应都将被忽略，除了 'Escape'，它将暂停实验。允许的响应应该是一个分号分隔的响应列表，例如'1;3' 允许左键和右键。要接受所有响应，请将 *允许的响应* 字段设置为空。


%--include: include/timeout.md--%

## 坐标和感兴趣区域（ROIs）

`cursor_x` 和 `cursor_y` 变量保存鼠标点击的位置。

如果您指示一个关联的 SKETCHPAD，变量 `cursor_roi` 将包含一个以逗号分隔的包含被点击坐标的元素名称列表。换句话说，SKETCHPAD 上的元素自动用作鼠标点击的感兴趣区域。

%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  收集鼠标点击并使用感兴趣区域。
--%

## 用 Python 收集鼠标响应

您可以使用 `mouse` 对象在 Python 中收集鼠标响应：

- %link:manual/python/mouse%