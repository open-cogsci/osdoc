title: 创建扩展
hash: 91a79a763c57d0445f9ee814ec6e513ab04f651b716fdd1fe99937052b85df97
locale: zh
language: Chinese

[TOC]


## 什么是 OpenSesame 扩展？

*扩展*向 OpenSesame 用户界面添加任意功能。例如，扩展可以在主工具栏或菜单栏中添加一个新条目。(要添加可用于实验的功能，请使用 [插件](%url:plugin%)。)


## 相关文件

一个或多个扩展被放置在扩展包中，它总是`opensesame_extensions`（这本身是一个所谓的隐含的命名空间包，但这是一个技术细节）的子包。假设你的扩展包叫做`example`，并且它包含一个叫做`example_extension`的单一扩展（可以有更多）。这将对应以下文件和文件夹结构：

```
opensesame_extensions/
    example/
        __init__.py               #可以为空，但必须存在
        example_extension/
            __init__.py           #包含扩展信息
            example_extension.py  #包含扩展类
```


## 扩展信息

扩展信息定义在扩展模块的`__init__.py`中，因此在我们的示例中，这是 `opensesesame_extensions/example/example_extension/__init__.py`。

```python
"""包含扩展描述的 docstring"""

# 标准图标名称
# - <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>
icon = 'applications-accessories'
# 标签和工具提示用户创建默认操作时使用，即将其插入到菜单和/或工具栏(或两者皆非)
label = "示例扩展"
tooltip = "示例工具提示"
menu = {
    "index": -1,
    "separator_before": True,
    "separator_after": True,
    "submenu": "示例"
}
toolbar = {
    "index": -1,
    "separator_before": True,
    "separator_after": True
}
# 设置会在 cfg 对象中持续存储
settings = {
    "example_setting": "示例值"
}
```

扩展可以出现在 OpenSesame 的菜单或主工具栏中。这需要您像上面所示在`__init__.py`中定义几个字段：

- `label` 是将出现在菜单中的文本。
- `icon` 是一个遵循 [freedesktop-compliant 图标名称][icon-spec] 的规格，用于指定将出现在菜单和/或工具栏中的图标。
- `index` 给出扩展在菜单/工具栏中的位置，并像 `list` 索引一样工作。也就是说，负数值相对于最后一个条目，-1 将扩展放在最后。

要让您的扩展响应菜单/工具栏的激活，请像下面的扩展代码中所示实现`activate()`方法。


## 编写扩展代码

主扩展代码放在 `[extension_name].py`中。这个文件通常只包含一个名为 `［ExtensionName］.py`的类，即类名的驼峰形式等于插件名称，继承自 `libqtopensesame.extensions.BaseExtension`。 所以一个基本的（非功能性的）扩展类应该是这样的：

~~~ .python
from libopensesame.py3compat import *
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class ExampleExtension(BaseExtension):
    """一个列出若干常见事件的示例扩展。类名应为
    folder_name 和 file_name 的 CamelCase 版本。所以在
    这种情况下，扩展文件夹（即 Python 包)和
    .py 文件（即 Python 模块）都叫做 example_extension，而
    类名则叫做 ExampleExtension
    """

    def activate(self):
        oslogger.debug('example_extension 扩展激活')

    def event_save_experiment(self, path):
        oslogger.debug(f'Event fired: save_experiment(path={path})')

    # 更多事件监听器，请参阅示例扩展源代码
~~~


## 监听事件

OpenSesame在发生重要事情时会触发事件。例如，当实验被保存时，“save_experiment”事件会被触发。要让您的扩展监听某个事件，只需实现一个名为`event_[event name]`的方法，如上所示。

请注意，某些事件需要关键字参数，例如`save_experiment`的`path`。您的函数的关键字签名必须符合预期的关键字签名。请参阅下面的事件概览以获取所有事件和预期关键字的完整列表。


## 构建软件包并上传至 pypi

构建扩展包并将其上传至`pypi`的方法与插件相同：

- %link:plugin%
- <https://github.com/open-cogsci/opensesame-extension-example>

## 例子

具体示例可见：

- <https://github.com/open-cogsci/opensesame-extension-example>

其他示例可以在OpenSesame源代码的`opensesame_extensions`文件夹中找到：

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_extensions/core>

[example]: https://github.com/open-cogsci/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html

## 事件概览

本概览列出了代码中触发的所有事件，因此，您的扩展可以通过实现相应的`event_[eventname]()`函数来监听它们。

%-- include: include/events.md --%