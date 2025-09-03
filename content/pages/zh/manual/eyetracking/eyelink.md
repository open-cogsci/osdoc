title: Eyelink
hash: 446281a464dd40eabe3f55f650572a8894359598a77c99f0c8eb20fe31cad1fc
locale: zh
language: Chinese

[TOC]

## 关于 EyeLink

Eyelink 系列眼动仪由 SR Research 生产，是心理学研究中最常用的眼动仪之一。SR Research 提供了 Eyelink 的 Python 绑定（称为 PyLink），该绑定被 PyGaze 使用。PyLink 的许可证与 OpenSesame 使用的许可证不兼容。因此，PyLink 没有包含在 OpenSesame 的默认发行版中，需要单独安装。

## Windows

### 安装 EyeLink Developers Kit

Eyelink Developers Kit（有时也叫 Display Software）提供了与 Eyelink PC 通信所需的库。你可以在这里找到（需要免费注册）：

- <https://www.sr-research.com/support/thread-13.html>

如果你解压 `.zip` 文件，然后运行 `.exe` 安装程序，EyeLink 显示软件将安装在以下文件夹之一（取决于你的 Windows 版本）：

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

在该文件夹下有一个 `libs` 子文件夹，你需要将其添加至系统 Path（该路径有时会自动添加，但请务必检查确认）。你可以通过打开“我的电脑”，点击“查看系统信息”，打开“高级”标签，点击“环境变量”，并在 Path 变量（系统变量下）后面添加 `;C:\Program Files\SR Research\EyeLink\libs` 或（根据你的系统）`;C:\Program Files (x86)\SR Research\EyeLink\libs` 完成。

### 安装带有 PyLink 的 OpenSesame

`pylink` 是支持 EyeLink 的 Python 库。目前，`pylink` 只支持 Python 3.12 及更早版本，而 OpenSesame 的标准软件包是基于 Python 3.13 构建的。因此，你必须从 [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases) 使用 Python 3.12（或更早）版本的软件包。

之后，可以通过 SR Research 的 PyPi 仓库使用 `pip install` 安装 `pylink`：

```
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
```

重要提示：*不要* 通过运行 `pip install pylink` 来安装 `pylink`。这样安装的是完全不同的软件包！

你可以在 SR Research 论坛上找到更多关于 `pylink` 的信息（需要免费注册）：

- <https://www.sr-research.com/support/thread-8291.html>

## Ubuntu

Eyelink 显示软件可以直接通过仓库安装。这同时也会安装 PyLink 以及一些便利工具，比如 `edf2asc` 转换器。

```bash
sudo add-apt-repository 'deb [arch=amd64] https://apt.sr-research.com SRResearch main'
sudo apt-key adv --fetch-keys https://apt.sr-research.com/SRResearch_key
sudo apt-get update
sudo apt-get install eyelink-display-software
```

欲了解更多信息，请访问：

- <https://www.sr-support.com/thread-13.html>

## PyGaze

按照上述说明安装 EyeLink 显示软件和 PyLink 后，您就可以在 PyGaze 中使用 EyeLink 了！参见：

- %link:pygaze%

## SR Research eyelink 插件

SR Research 也为 OpenSesame 提供了自己的 EyeLink 插件。这些插件与（并最初基于）PyGaze 插件类似，但提供了一些 PyGaze 所不具备的功能。要安装这些插件，请运行：

```
pip install opensesame-plugin-eyelink
```

欲了解更多信息，请访问：

- <https://www.sr-research.com/support/thread-52.html>