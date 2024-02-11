title: 记录和读取数据文件
hash: 404c31c1711c098c3d658e7de50a871eaeae4a66cfa946a5405071f57239ea81
locale: zh
language: Chinese

在进行实验之前，始终要三重检查数据是否已正确记录！
{: .page-notification}

[TOC]


## 使用日志记录器（LOGGER）项目

OpenSesame 不会自动记录你的数据。相反，你需要在试验序列的末尾插入一个 LOGGER 项目。

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  LOGGER 项目。
--%

使用 LOGGER 的最简单方式是启用“自动记录所有变量”选项。这样，OpenSesame 所知道的所有变量都会被写入日志文件，除了那些明确排除的变量（见下文）。

你可以明确*包括*你想记录的变量。这样做的主要原因是，因为 OpenSesame 没有自动检测到某些变量，导致这些变量丢失，或者你已经禁用了“自动记录所有变量”的选项。

你也可以明确排除某些变量，不在日志文件中记录。这样做的主要原因是通过排除通常无用的变量，保持日志文件的清洁。

通常情况下，你应该只创建一个 LOGGER 项目，并在实验的不同位置根据需要重复使用该 LOGGER（即使用同一个 LOGGER 项目的链接副本）。如果你创建了多个 LOGGER（而不是多次使用单一的 LOGGER），它们都将写入同一个日志文件，结果会是一团糟！

## 使用 Python 内联脚本

你可以使用 `log` 对象来写入日志：

~~~ .python
log.write('这将被写到日志文件中！')
~~~

更多信息，请参见：

- %link:log%

你通常不应该直接写入日志文件，并同时使用 LOGGER 项目；这样会导致日志文件混乱。

## 数据文件的格式

如果你使用了标准的 LOGGER 项目，则数据文件的格式如下（只是标准的 csv 格式）：

- 纯文本
- 逗号分隔
- 双引号包围（字面上的双引号用反斜杠转义）
- Unix 风格的行尾
- UTF-8 编码
- 第一行为列名

## 记录哪些变量？

默认情况下，用户界面中定义的变量，如 `loop` 表中的列或响应变量总是会被记录。

默认情况下，`inline_script` 或 `inline_javascript` 中定义的变量如果是数字（`int` 和 `float`）、字符串（`str` 和 `bytes`）或 `None` 值时，会被记录。这是为了避免因记录长列表和其他大值而导致日志文件过于庞大。 （截至 OpenSesame 4.0 版本，不再需要使用 `var`（Python）或 `vars`（JavaScript）对象。）

如果你想明确记录某个默认不会被记录的变量，可以在 LOGGER 项目中使用“包括”字段。

## 读取和处理数据文件

### 在 Python 中使用 pandas 或 DataMatrix

在 Python 中，你可以使用 [pandas](http://pandas.pydata.org/) 来读取 csv 文件。

```python
import pandas
df = pandas.read_csv('subject-1.csv')
print(df)
```

或者使用 [DataMatrix](https://datamatrix.cogsci.nl/)：

```python
from datamatrix import io
dm = io.readtxt('subject-1.csv')
print(dm)
```

### 在 R 中

在 R 中，你可以简单地使用 `read.csv()` 函数来读取单个数据文件。

~~~ .R
df = read.csv('subject-1.csv', encoding = 'UTF-8')
head(df)
~~~

此外，你可以使用来自 [readbulk](https://github.com/pascalkieslich/readbulk) 包的 `read_opensesame()` 函数，以方便地读取多个数据文件，并将它们合并成一个大的数据框。该包可在 CRAN 上安装，通过 `install.packages('readbulk')` 进行安装。

~~~ .R
# 读取并合并存储在文件夹 'raw_data' 中的所有数据文件
library(readbulk)
df = read_opensesame('raw_data')
~~~

### 在 JASP 中

[JASP](http://jasp-stats.org/)，一款开源统计软件包，可以直接打开 csv 文件。

### 在 LibreOffice Calc 中

如果您在LibreOffice Calc中打开一个csv文件，您需要指明确切的数据格式，如%FigLibreOffice所示。（默认设置通常是正确的。）

%--
figure:
 source: libreoffice.png
 id: FigLibreOffice
--%

### 在Microsoft Excel中

在Microsoft Excel中，您需要使用文本导入向导。

### 将多个数据文件合并成一个大文件

出于某些目的，例如使用数据透视表，将所有数据文件合并成一个大文件可能会比较方便。使用Python DataMatrix，您可以使用以下脚本来实现：

```python
import os
from datamatrix import DataMatrix, io, operations as ops

# 将此处更改为包含.csv文件的文件夹
SRC_FOLDER = 'student_data'
# 更改为您想要保留的列名列表
COLUMNS_TO_KEEP = [
    'RT_search',
    'load',
    'memory_resp'
]

dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('读取 {}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'merged-data.csv')
```

## 在OSWeb中记录

当您在浏览器中用OSWeb运行实验时，记录的方式与在桌面上运行实验时不同。

具体来说，当您直接从OpenSesame中启动OSWeb实验时，日志文件会在实验结束时下载。这个日志文件是`.json`格式的。当您通过JATOS启动OSWeb实验时，没有实际的日志文件，而是所有数据都发送到JATOS，从那里可以下载。

另见：

- %link:manual/osweb/workflow%

[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/
[log-func]: /python/inline-script/#inline_script.log
[codecs]: http://docs.python.org/2/library/codecs.html
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl/