title: Eyelink
hash: c9635275665d7dc2d7c42f6f480e386381284e31750ff4cd7cbaab5fb4522ee5
locale: zh
language: Chinese

[TOC]

## 关于 EyeLink

由 SR Research 生产的 EyeLink 系列眼动仪是心理学研究中最常用的眼动仪之一。SR Research 为 Eyelink 提供了 Python 绑定（称为 PyLink），由 PyGaze 使用。PyLink 的许可与 OpenSesame 使用的许可不兼容。因此，PyLink 没有包含在 OpenSesame 的默认发行版中，需要单独安装。


## SR Research 论坛

您需要从 SR Research 论坛上下载一些软件。这是一个封闭的论坛，但您可以免费注册。

- <https://www.sr-support.com/>


## Windows

### 安装 EyeLink 开发者套件

Eyelink 开发者套件（有时称为显示软件）提供了与 Eyelink PC 通信所需的库。可以在这里找到它：

- <https://www.sr-support.com/thread-13.html>

如果您解压缩 .zip 文件，然后运行 .exe 安装程序，EyeLink 显示器将安装在以下文件夹之一（取决于您的 Windows 版本：

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

在此文件夹中，有一个 `libs` 子文件夹，您需要将其添加到系统路径（这可能已自动添加到路径中，但请检查以确保您没有）。您可以通过打开“我的电脑”，单击“查看系统信息”，打开“高级”选项卡，单击“环境变量”并将 `;C:\Program Files\SR Research\EyeLink\libs` 或（取决于您的系统） `;C:\Program Files (x86)\SR Research\EyeLink\libs` 添加到 Path 变量（在系统变量下）实现这一点。


### 安装 PyLink

PyLink 是支持 EyeLink 的 Python 库。PyLink 与近期的 EyeLink 显示软件（如上述）一起提供，您可以在以下文件夹之一找到它（取决于您的 Windows 版本）：

```
C:\Program Files\SR Research\EyeLink\SampleExperiments\Python
C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python
```

或者，您可以从这里下载 Pylink ：

- <https://www.sr-support.com/thread-13.html>

要在 OpenSesame 中安装 PyLink，请将带有 PyLink 的文件夹复制到 OpenSesame 程序文件夹，或者复制到 `Lib\site-packages` 子文件夹。在某些情况下，`pylink` 文件夹可能有一个名为 `pylink27-amd64` 的名字，在这种情况下，你必须将其重命名为 `pylink`。

__重要：__ PyLink 的 Python 版本需要与您的 OpenSesame 安装的 Python 版本相匹配。在大多数情况下，这意味着您需要适用于 Python 3.7 的 PyLink 。

## Ubuntu

EyeLink 显示软件可以直接从存储库安装。这也会安装 PyLink 和各种便捷工具，如 `edf2asc` 转换器。

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

有关更多信息，请访问：

- <https://www.sr-support.com/thread-13.html>


## PyGaze

在您按照上述说明安装了 EyeLink 显示软件和 PyLink 之后，您可以使用 PyGaze 上的 EyeLink！请参阅：

- %链接：pygaze%