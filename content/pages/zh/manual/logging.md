title: 记录和读取数据文件
hash: 6c081bb9571ecf270fcbd02104d88319bf6044245745b621d549cbc38c34e370
locale: zh
language: Chinese

始终三次检查您的数据在运行实验之前是否正确记录！
{：.page-notification}

[TOC]


## 使用 logger item

OpenSesame 不会自动记录您的数据。相反，您需要插入一个 LOGGER 项目，通常位于试验序列的末尾。

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  LOGGER 项目。
--%

使用 LOGGER 的最简单方法是启用 “自动记录所有变量” 选项。这样，除了下面明确排除的变量之外，OpenSesame已知的所有变量都会写入日志文件。

您可以明确地*包含*要记录的变量。这样做的主要原因是当您发现某些变量丢失(因为OpenSesame没有自动检测到它们)或者当您禁用了“自动记录所有变量”选项，

您还可以明确地从日志文件中排除某些变量。这样做的主要原因是通过排除通常没有用处的变量来保持日志文件的整洁。

一般来说，您应该只创建一个 logger 项目，并在需要的时候在实验中的不同位置重复使用该 LOGGER（即使用相同 LOGGER 项目的链接副本）。如果您创建多个 LOGGER（而不是多次使用单个 LOGGER），它们都将写入相同的日志文件，结果将是混乱的！

## 使用 Python 内联脚本

您可以使用 `log` 对象将数据写入日志文件：

~~~ .python
log.write('这将写入日志文件！')
~~~

有关详细信息，请参阅：

- %link:log%

通常情况下，您不应直接将数据写入日志文件，同时使用 LOGGER 项目。这样做会导致混乱的日志文件。

## 数据文件格式

如果您使用了标准的 LOGGER 项，数据文件采用以下格式（简单的标准 csv）：

- 纯文本
- 逗号分隔
- 双引号（文字双引号带反斜杠转义）
- 类 Unix 行结束符
- UTF-8 编码
- 第一行上的列名

## 读取和处理数据文件

### 用 Python pandas 或 DataMatrix

在 Python 中，您可以使用 [pandas](http://pandas.pydata.org/) 读取 csv 文件。

```python
import pandas
df = pandas.read_csv('subject-1.csv')
print(df)
```

或 [DataMatrix](https://datamatrix.cogsci.nl/):

```python
from datamatrix import io
dm = io.readtxt('subject-1.csv')
print(dm)
```

### 在 R 中

在 R 中，您可以简单地使用 `read.csv()` 函数读取单个数据文件。

~~~ .R
df = read.csv('subject-1.csv', encoding = 'UTF-8')
head(df)
~~~

此外，您可以使用 [readbulk](https://github.com/pascalkieslich/readbulk) 包中的 `read_opensesame()` 函数轻松读取和合并多个数据文件到一个大的数据框架中。该包可在 CRAN 上获得，可以通过 `install.packages('readbulk')` 来安装。

~~~ .R
# 读取并合并存储在'raw_data'文件夹中的所有数据文件
library(readbulk)
df = read_opensesame('raw_data')
~~~

### 在 JASP 中

[JASP](http://jasp-stats.org/)，一个开源统计软件包，可以直接打开 csv 文件。

### 在 LibreOffice Calc 中

如果在 LibreOffice Calc 中打开 csv 文件，您需要指定准确的数据格式，如 %FigLibreOffice 所示。（默认设置通常是正确的。）

%--
figure:
 source: libreoffice.png
 id: FigLibreOffice
--%

### 在 Microsoft Excel 中

在 Microsoft Excel 中，您需要使用“文本导入向导”。

### 将多个数据文件合并到一个大文件中

对于某些用途，例如使用数据透视表，将所有数据文件合并到一个大文件中可能会很方便。使用 Python DataMatrix，您可以使用以下脚本执行此操作：

```python
import os
from datamatrix import DataMatrix, io, operations as ops

# 将此更改为包含.csv文件的文件夹
SRC_FOLDER = 'student_data'
# 将此更改为您要保留的列名列表
COLUMNS_TO_KEEP = [
    'RT_search',
    'load',
    'memory_resp'
]


dm = DataMatrix()
for basename in os.listdir(SRC_FOLDER):
    path = os.path.join(SRC_FOLDER, basename)
    print('正在读取{}'.format(path))
    dm <<= ops.keep_only(io.readtxt(path), *COLUMNS_TO_KEEP)
io.writetxt(dm, 'merged-data.csv')
```


## 在OSWeb中记录日志

当您使用OSWeb在浏览器中运行实验时，日志记录方式与在桌面上运行实验时不同。

具体来说，当您直接从 OpenSesame 启动 OSWeb 实验时，实验结束时会下载日志文件。这个日志文件是`.json`格式。当您从 JATOS 启动 OSWeb 实验时，没有日志文件，而是将所有数据发送到 JATOS，然后从那里下载。

参考：

- %link:manual/osweb/workflow%



[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/
[log-func]: /python/inline-script/#inline_script.log
[codecs]: http://docs.python.org/2/library/codecs.html
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl/