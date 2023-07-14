title: Eyelink
hash: 795cf5b31d90084e4fe773cb7002ad511f76aa023cfef172927e5544fd44ed44
locale: zh
language: Chinese

[TOC]

## 关于EyeLink

EyeLink系列眼动跟踪器由SR Research生产，是心理学研究中最常用的眼动跟踪器之一。SR Research为EyeLink提供了Python绑定（名为PyLink），被PyGaze所使用。PyLink的许可证与OpenSesame所使用的许可证不兼容。出于这个原因，PyLink并未包含在OpenSesame的默认分发中，需要单独安装。

## Windows

### 安装EyeLink开发者工具包

EyeLink开发者工具包（有时被称为显示软件）提供了与EyeLink PC交流所需的库。你可以在这里找到它（需要免费注册）：

- <https://www.sr-research.com/support/thread-13.html>

如果你解压了`.zip`文件，然后运行`.exe`安装器，EyeLink显示器将会被安装在以下文件夹中的一个（取决于你的Windows版本）：

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

在这个文件夹中，有一个名为`libs`的子文件夹，你需要将其添加到系统路径（这可能已经自动添加到路径中，但最好确认一下）。你可以通过打开"我的计算机"，点击"查看系统信息"，打开"高级"标签，点击"环境变量"并添加`；C:\Program Files\SR Research\EyeLink\libs`或（取决于你的系统）`；C:\Program Files (x86)\SR Research\EyeLink\libs`到系统变量中的Path变量。


### 使用PyLink安装OpenSesame

PyLink是支持EyeLink的Python库。截至2023年7月，PyLink支持最高到Python 3.10版本，而OpenSesame默认使用Python 3.11。因此，直到Pylink更新支持Python 3.11，安装带有Pylink的OpenSesame的最简单方法是通过Anaconda构建一个Python 3.10环境。

这听起来很复杂，但其实并不复杂。首先，阅读一下通过Anaconda安装OpenSesame的通用步骤，这在下载页面有描述：

- %link:download%

接下来，一旦你理解了通用步骤，首先创建一个Python 3.10环境，继续按照下载页面的指示操作，然后安装PyLink：

```
# 首先创建一个Python 3.10环境
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# 现在按照下载页面的指示操作
# ...
# 然后从SR Research PyPi仓库安装PyLink
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
# 现在启动OpenSesame！
opensesame
```

你可以在SR Research的论坛上找到更多关于PyLink的信息（需要免费注册）：

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

EyeLink显示软件可以直接从仓库安装。这也会安装PyLink和一些便利工具，比如`edf2asc`转换器。

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

更多信息，请访问：

- <https://www.sr-support.com/thread-13.html>


## PyGaze

在你按照以上指示安装EyeLink显示软件和PyLink后，你就可以使用PyGaze和EyeLink了！参见：

- %link:pygaze%