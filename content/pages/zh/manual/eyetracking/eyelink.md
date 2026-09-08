title: EyeLink
hash: 37419c41f2ba79dc8903d36fe35edc800de2791247978b58d7a4c3ee07121ff1
locale: zh
language: Chinese

[TOC]

## 关于 EyeLink

由 SR Research 生产的 EyeLink 眼动仪是心理学研究中最常用的眼动仪之一。SR Research 提供了用于与 EyeLink 通信的 Python 绑定（称为 PyLink），PyGaze 和他们自己的 EyeLink Plugin 都使用这些绑定。 


## 安装 PyLink

用于集成 EyeLink 的 Python 库以 `sr-research-pylink` 的名称发布在 PyPI 上。它在 Python 2.7 至 3.14 中全面支持 Windows、macOS 和 Linux，因此可以安装在最新版本的 OpenSesame 中。

您可以直接在终端中安装：

```
pip install sr-research-pylink
```

**重要提示：** 请*不要*通过运行 `pip install pylink` 来尝试安装 `pylink`。这样做会安装一个完全不同且无关的软件包！

您可以在 SR Research 论坛上找到有关 `sr-research-pylink` 的更多信息（需要免费注册）：

- <https://www.sr-research.com/support/> 
- <https://www.sr-research.com/support/thread-48.html>
	
## PyGaze

按照上述说明安装 PyLink 后，您就可以将 EyeLink 与 PyGaze 一起使用！请参阅：

- %link:pygaze%

## SR Research EyeLink Plugin

SR Research 还为 OpenSesame 提供了他们自己的 EyeLink plugin 集。该 plugin 提供了 PyGaze 中不可用的额外 EyeLink 集成功能，例如 gaze trigger、任务中止时的 EDF 传输，以及对较新 EyeLink 型号在摄像头传输期间的全面支持。要安装该 plugin，请运行：

```
pip install opensesame-plugin-eyelink
```

如需更多信息，请访问：

- <https://www.sr-research.com/support/thread-52.html>

## 可选：EyeLink Developers Kit

虽然在 OpenSesame 中运行 PyLink 已不再需要 EyeLink Developers Kit（有时称为 EyeLink Display Software），但它提供了其他有用工具，例如 `edf2asc` 转换器、文档和离线 `sr-research-pylink` 安装文件（.whl）。

如果您需要这些工具，可以在 SR Research Support 网站上找到 Windows、macOS 和 Ubuntu repositories 的安装程序：

- <https://www.sr-research.com/support/forum-9.html>