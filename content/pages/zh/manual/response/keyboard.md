title: 键盘响应
hash: 23ed6413bd7bc9180b1e3a384c25c3f89c817414a4460a00260be06f5698474a
locale: zh
language: Chinese

使用 KEYBOARD_RESPONSE 项目收集键盘响应。

[TOC]

## 响应变量

KEYBOARD_RESPONSE 设置标准响应变量，如下所述：

- %link:manual/variables%

## 按键名称

按键通常由其字符和/或其描述（取决于哪个适用）来识别。例如：

- `/`键名为'slash'和'/'。您可以使用这两个名称中的任何一个。
- `a`键名为'a'。
- 左箭头键名为'left'。

如果您不知道某个特定键的名称，您可以：

- 点击“列出可用按键”按钮；或者
- 创建一个简单的实验，其中 KEYBOARD_RESPONSE 紧跟着具有文本'{response}'的 FEEDBACK 项目。这将显示先前收集的响应的名称。

## 正确响应

*正确响应* 字段表示哪个响应被认为是正确的。在正确响应之后，`correct` 变量自动设置为 1；在错误响应（即其他所有响应）之后，`correct` 设置为 0；如果没有指定正确响应，`correct` 设置为“未定义”。

您可以通过以下三种主要方式指示正确响应：

- *保留该字段为空。*如果您将*正确响应*字段保留为空，OpenSesame 将自动检查是否已定义名为 `correct_response` 的变量，如果有，则将此变量用于正确响应。
- *输入字面值。*您可以显式输入响应，例如在 KEYBOARD_RESPONSE 项目的情况下为'left'。只有在正确响应是固定的情况下，这才有用。
- *输入变量名。*您可以输入一个变量，例如'{cr}'。在这种情况下，将使用此变量作为正确响应。

## 允许的响应

*允许的响应* 字段表示允许的响应列表。所有其他响应将被忽略，但“Escape”将暂停实验。允许的响应应该是一个分号分隔的响应列表，例如对于 KEYBOARD_RESPONSE，可以是'a;left;/'。要接受所有响应，请将*允许的响应*字段保留为空。

%--include: include/timeout.md--%

## 在 Python 中收集键盘响应

您可以使用 `keyboard` 对象在 Python 中收集键盘响应：

- %link:manual/python/keyboard%