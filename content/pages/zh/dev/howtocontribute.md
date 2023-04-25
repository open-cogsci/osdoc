title: 如何贡献
uptodate: false
hash: cdf0ef5efe4027ec45865c8235a04695c3ed9e91a1c8db4ffab4c5351d8c05d5
locale: zh
language: Chinese

[TOC]

## 获取最新的源代码

OpenSesame 的源代码托管在 GitHub 上：

- <https://github.com/smathot/OpenSesame>。

GitHub 为项目合作提供了直接的方法。如果您不熟悉 GitHub，您可能需要查看它们的帮助站点：<http://help.github.com/>。

贡献代码的最佳（也是最简单）方式如下：

1. 创建一个 GitHub 账户。
2. 创建一个 OpenSesame 的 fork <https://github.com/smathot/OpenSesame>。
3. 修改您的 fork。
4. 发送一个“拉取请求”，要求将您的更改合并回主仓库。

每个 OpenSesame 主要版本都有自己的分支。例如，`ising` 分支包含 3.0 *Interactive Ising* 的代码。`master` 分支包含最新稳定版的代码。

## 开发插件或扩展

有关插件或扩展开发，请参阅：

- %link:dev/plugin%
- %link:dev/extension%

## 翻译用户界面

有关如何翻译用户界面的说明，请参阅：

- %link:dev/translate%

## 编码风格指南

目标是保持易读且一致的代码库。因此，在贡献代码时，请考虑以下风格指南：

### 异常处理

异常应通过 `libopensesame.exceptions.osexception` 类处理。例如：

~~~ .python
from libopensesame.exceptions import osexception
raise osexception(u'发生错误')
~~~

### 打印调试输出

调试输出应通过 `libopensesame.debug.msg()` 处理，仅在使用 `--debug` 命令行参数启动 OpenSesame 时显示。例如：

~~~ .python
from libopensesame import debug
debug.msg(u'这将仅在调试模式下显示')
~~~

### 缩进

缩进应基于制表符。*这是所有风格指南中最重要的一条*，因为混合缩进会导致问题，并且更正起来耗时。

### 名称、文档字符串和行换行

- 名称应为小写，单词之间用下划线分隔。
- 每个函数应附有一个信息性文档字符串，格式如下所示。如果文档字符串是多余的，例如，因为一个函数重写了另一个具有文档字符串的函数，请指明可以找到完整文档字符串的位置。
- 请不要让代码行超过79个字符（其中一个制表符计为4个字符），除非是长字符串难以分割的情况。

~~~ .python
def a_function(argument, keyword=None):

	"""
	desc:
		这是一个 YAMLDoc 风格的文档字符串，允许完全指定参数。另请参见<https://github.com/smathot/python-yamldoc>。

	arguments:
		argument:   这是一个参数。

	keywords:
		keyword:    这是一个关键字。

	returns:
		此函数返回一些值。
	"""

	pass

def a_simple_function():

	"""这是一个简单的文档字符串"""

	pass

~~~

### 编写 Python 2 和 3 兼容代码

代码应与 Python 2.7 和 3.4 以及更新版本兼容。为了更容易编写 Python 2 和 3 兼容代码，`py3compat` 模块中包含了一些技巧，您应该*始终*在脚本中导入它，如下所示：

~~~ .python
from libopensesame.py3compat import *
~~~

此模块：

- 将 Python-2 的 `str` 和 `unicode` 类型重映射为（大致）相当于 Python-3 的 `bytes` 和 `str` 类型。因此，在大多数情况下，您应该使用 `str` 对象，在特殊情况下使用 `bytes` 对象。
- 添加以下功能：
  - `safe_decode(s, enc='utf-8', errors='strict')` 将任何对象转换为 `str` 对象
  - `safe_encode(s, enc='utf-8', errors='strict')` 将任何对象转换为 `bytes` 对象
- 添加一个`py3`变量，在 Python 3 上运行时为`True`，在 Python 2 上运行时为`False`。
- 在 Python 3 上运行时，添加一个`basestr`对象。

### Unicode 和字符串

确保所有功能都是 Unicode 安全的。对于新代码，内部*仅*使用 Unicode 字符串。

~~~ .python
my_value = 'a string' # 不推荐
my_value = u'a string' # 推荐
~~~

有关更多信息，请参阅：

- <http://docs.python.org/2/howto/unicode.html>

### 其他

除了上面显示的指南之外，请遵循以下标准：

- <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>