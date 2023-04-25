title: 创建插件
hash: d1fa28a6fa30fd06e613cb36e47efbafb5f2b52b7276950343c65e3556ff3f8c
locale: zh
language: Chinese

[TOC]

## 什么是OpenSesame插件？

*插件* 是出现在OpenSesame项目工具栏中的额外项目。插件为你的实验增加功能。（要向OpenSesame用户界面添加功能，你需要[*extension*](%url:extension%)。）

## 相关文件

一个或多个插件组合成一个插件包，它始终是 `opensesame_plugins` 的一个子包（它本身是所谓的隐式命名空间包，但这是一个不太重要的技术细节）。 假设你的插件包叫 `example`，包含一个名为 `example_plugin` 的单个插件（可以有更多）。这将对应于以下文件和文件夹结构：

```
opensesame_plugins/
    example/
        __init__.py                  # 可以为空但必须存在
        example_plugin/
            __init__.py              # 包含插件信息
            example_plugin.py        # 包含插件类
            example_plugin.png       # 16 x 16 图标（可选）
            example_plugin_large.png # 32 x 32 图标（可选）
            example_plugin.md        # 以Markdown格式的帮助文件（可选）
```

## 图标

每个插件都需要一个图标，你可以通过以下两种方式之一指定：

- 在插件文件夹中包含两个图标文件，如上所示：
    - 一个16x16像素的png文件，名为 `[plugin_name].png`；和
    - 一个32x32像素的png文件，名为 `[plugin_name]_large.png`。
- 或者在插件信息（`__init__.py`）中指定一个 `icon` 名称。 如果这样做，插件图标将从图标主题中获取。


## 帮助文件

您可以提供Markdown或HTML格式的帮助文件。要添加Markdown帮助文件，只需在插件文件夹中创建一个名为 `[plugin_name].md` 的文件。 对于HTML帮助文件，创建一个名为 `[plugin_name].html` 的文件。首选Markdown格式，因为它更易于阅读。 严格来说，帮助文件是选项，而且您的插件将没有它工作。 不过，详细的帮助文件是一个好插件的基本部分。


## 定义GUI

插件信息（`__init__.py`）定义了一个（至少）docstring，一个 `category` 变量和一个`controls`变量。

`controls` 变量是定义GUI控件的 `dict` 元素列表。最重要的字段是：

- `type` 指定控件类型。可能的值：
	- `checkbox` 是一个可选框 (`QtGui.QCheckBox`)
	- `color_edit` 是一个颜色选择小部件 (`libqtopensesame.widgets.color_edit.ColorEdit`)
	- `combobox` 是带有多个选项的下拉框 (`QtGui.QComboBox`)
	- `editor` 是一个多行文本编辑器 (使用 PyQode)
	- `filepool` 是一个文件选择部件（`QtGui.QLineEdit`）
	- `line_edit` 是一个单行文本输入 (`QtGui.QLineEdit`)
	- `spinbox` 是一个基于文本的数字值选择器 (`QtGui.QSpinBox`)
	- `slider` 是一个滑动数字值选择器 (`QtGui.QSlider`)
	- `text` 是一个非交互式文本字符串 (`QtGui.QLabel`)
- `var` 指定应使用控件设置的变量名（如果 `type` 是 `text`，则不适用）。
- `label` 指定控件的文本标签。
- `name` (可选) 指定应将部件添加到插件对象的名称，以便将它称为 `self.[name]`。
- `tooltip` (可选) 提示信息提示。

```python
"""一个含有插件描述的docstring"""

# 具体类别决定了插件在项目工具栏中的分组
category = "视觉刺激"
# 定义GUI控件
controls = [
    {
        "type": "checkbox",
        "var": "checkbox",
        "label": "示例复选框",
        "name": "checkbox_widget",
        "tooltip": "一个示例复选框"
    }, {
        "type": "color_edit",
        "var": "color",
        "label": "颜色",
        "name": "color_widget",
        "tooltip": "一个示例颜色编辑器"
    }
]
```

请参见[示例](#examples) 插件以获取所有控件和选项的列表。

## 编写插件代码

主要的插件代码位于 `[plugin_name].py` 中。这个文件通常只包含一个名为 `[PluginName].py` 的类，也就是一个插件名的驼峰式等价类，它继承自 `libopensesame.item.Item`。一个基本的插件类看起来像这样：


```python
from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from openexp.canvas import Canvas


class ExamplePlugin(Item):
    """一个示例插件，显示一个简单的画布。类名应该是文件夹名和文件名的驼峰式版本。因此，在这种情况下，插件文件夹（它是一个Python包）和.py文件（它是一个Python模块）都称为example_plugin，而类名为ExamplePlugin。
    """
    def reset(self):
        """将插件重置为初始值。"""
        # 在这里，我们为 __init__.py 文件中指定的变量提供默认值。如果您不提供默认值，插件将工作，但当它们没有在GUI中明确设置时，变量将是未定义的。
        self.var.checkbox = 'yes'  # yes = checked, no = unchecked
        self.var.color = 'white'
        self.var.option = 'Option 1'
        self.var.file = ''
        self.var.text = 'Default text'
        self.var.spinbox_value = 1
        self.var.slider_value = 1
        self.var.script = 'print(10)'

    def prepare(self):
        """插件的准备阶段在这里。"""
        # 调用父构造函数。
        super().prepare()
        # 在这里简单地准备一个带有修正点的画布。
        self.c = Canvas(self.experiment)
        self.c.fixdot()

    def run(self):
        """插件的运行阶段在这里。"""
        # self.set_item_onset() 设置 time_[item name] 变量。 可选参数，您可以传递一个时间戳，例如通过canvas.show()返回的值。
        self.set_item_onset(self.c.show())
```


如果您想为插件实现自定义GUI控件，您还需要在同一个文件中实现一个 `Qt[PluginName]` 类。这在[示例](#examples)插件中有说明。如果您没有实现这个类，将根据在 `__init__.py` 中定义的控件自动创建一个默认的GUI。


## 实验变量

实验变量是 `var` 对象的属性。一个示例是上面示例中的 `self.var.my_line_edit_var`。这些变量可定义插件，并可解析为OpenSesame脚本。另请参阅：

- %link:manual/variables%


## 构建一个包并上传到pypi

构建插件包的最简单方法是定义一个 `pyproject.toml` 文件，并使用 `poetry` 来构建包并将其上传到 `pypi`。

- <https://python-poetry.org/>

一个示例的 `pyproject.toml` 文件如下：

```toml
[tool.poetry]
name = "opensesame-plugin-example"
version = "0.0.1"
description = "An example plugin for OpenSesame"
authors = ["Sebastiaan Mathôt <s.mathot@cogsci.nl>"]
readme = "readme.md"
packages = [
    {include = "opensesame_plugins"},
]

[tool.poetry.dependencies]
python = ">= 3.7"
opensesame-core = ">= 4.0.0a0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

将此文件添加到插件代码的根文件夹后，可以通过运行以下命令构建一个 `.whl` 包：

```bash
poetry build
```

成功地构建了一个包后，在 <https://pypi.org/> 上创建一个账户，为您的账户创建一个API令牌，并像这样验证 `poetry`：

```bash
poetry config pypi-token.pypi [api_token]
```

完成此操作后，您可以运行以下命令将您的包发布到PyPi：

```bash
poetry publish
```


这样您的用户就可以通过pip安装您的插件了！

```bash
pip install opensesame-plugin-example
```


## 示例

有关工作示例，请参阅：

- <https://github.com/open-cogsci/opensesame-plugin-example>

其他示例可以在OpenSesame源代码的`opensesame_plugins`文件夹中找到：

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_plugins/core>