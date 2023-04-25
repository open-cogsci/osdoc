title: 从源代码运行
reviewed: false
hash: 97b9ccebc7a5b8f621d7724e6cf0a8a423800dd3861b85aaa93ff679ac90ded5
locale: zh
language: Chinese

此页面描述了如何在您的计算机上设置完整的Python环境，以便可以直接从源代码运行OpenSesame。

[TOC]

## 下载源代码

从GitHub上下载最新稳定版本的源代码：

- <https://github.com/smathot/OpenSesame/releases>

您还可以下载代码的开发快照。要获得相对稳定的快照，请从`master`分支下载。要获取最新，最好，可能非常不稳定的快照，请从与OpenSesane的主要版本相对应的分支下载（例如，`heisenberg`用于2.9，`ising`用于3.0）。

- <https://github.com/smathot/OpenSesame/>

## 依赖关系

### 图标主题

如果您直接从源代码运行OpenSesame，则不包含图标主题。OpenSesame使用两个图标主题：[MokaSesame](https://github.com/smathot/moka-icon-theme/tree/MokaSesame)，Moka的fork，以及[Faba](https://github.com/snwh/faba-icon-theme)。

可以自己编译这些图标主题，也可以从此处下载预编译的主题：

- http://forum.cogsci.nl/uploads/editor/we/p1y3i4qm70ch.zip

将`Faba`和`MokaSesame`文件夹作为`opensesame_resources/theme/default/`的子文件夹放置。

### 必需的

以下软件包需要运行OpenSesame GUI的最小版本，仅支持[旧版]后端，不支持声音，且无插件支持。

- [Python](http://www.python.org)是创建OpenSesame的编程语言。支持以下版本的Python：
	- Python 2.7（默认）
	- OpenSesame >= 3.0.0支持Python >= 3.4
- [PyGame](http://www.pygame.org)是用于图形和声音的库。
- [qtpy](https://github.com/goanpeca/qtpy)是在PyQt4或PyQt5上面的抽象层。
	- [PyQt4](http://www.riverbankcomputing.com/software/pyqt/download)是用于用户界面的图形工具包；或
	- [PyQt5](http://www.riverbankcomputing.com/software/pyqt/download)是用于用户界面的图形工具包。
- [QScintilla2](http://www.riverbankcomputing.com/software/pyqt/download)是一个基本的文本编辑器组件。在某些情况下，它包含在`PyQt4`中。
- [QProgEdit](https://github.com/smathot/QProgEdit))是基于`QScintilla2`构建的高级文本编辑器组件。
	- OpenSesame >= 3.1.0需要QProgEdit >= 4.0.0
- [PyYAML](http://pyyaml.org/)是用于加载`yaml`文件的库。
- [WebColors](https://pypi.python.org/pypi/webcolors)是用于解释颜色描述的库。
- [python-datamatrix](https://github.com/smathot/python-datamatrix)由循环项使用。
- [python-qdatamatrix](https://github.com/smathot/python-qdatamatrix)由循环项使用。
- [python-pseudorandom](https://github.com/smathot/python-pseudorandom)由循环项使用。
- [QNotifications](https://github.com/dschreij/QNotifications)由通知扩展使用。

### 可选

以下软件包不是必需的，但如果未安装，某些功能可能会缺失。

- [Expyriment](http://www.expyriment.org/) 对于 [xpyriment] 后端是必需的。
    - OpenSesame >= 3.0.0 需要 Expyriment >= 0.8.0。
- [NumPy](http://www.numpy.org/) 是一个高级数学库，用于支持诸如声音等多种功能。
- [PIL](http://www.pythonware.com/products/pil/) 是一个图像库，用于支持多种功能。
    - 您也可以使用 `pillow`，这是原始库 `PIL` 的活跃维护分支（原始库不再维护）。
- [PsychoPy](http://www.psychopy.org/) 对于 [psycho] 后端是必需的。
- [pyflakes](https://pypi.python.org/pypi/pyflakes) 用于自动验证您的 Python 脚本。
- [Pyglet](http://www.pyglet.org/) 由 PsychoPy 所需。
- [PyOpenGL](http://pyopengl.sourceforge.net/) 由 PsychoPy 和 Expyriment 所需。
- [pySerial](http://pyserial.sourceforge.net/) 用于串口通信。
- [python-markdown](https://pypi.python.org/pypi/Markdown) 用于查看程序内帮助文件。
- [IPython](http://ipython.org/)（如果可用）用于调试窗口。
- [python-fileinspector](https://github.com/dschreij/fileinspector) 用于生成文件类型特定的图标。
- [shapely](https://pypi.org/project/Shapely/) 用于检查 `Canvas` 元素的边界

### 额外

以下软件包不直接由 OpenSesame 使用，但在开发实验时可能会派上用场，并且包含在 OpenSesame 官方 Windows 版本中。

- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) 是一个用于录音和播放的替代声音库。
- [Matplotlib](http://matplotlib.org/) 是一个绘制图表的库。
- [Scipy](http://www.scipy.org/) 是一套杂项科学程序。
- [pyCairo](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo) 是一个矢量图形库。
- [pyParallel](http://sourceforge.net/projects/pyserial/files/pyparallel) 允许通过并行端口进行通信。
- [OpenCV](http://opencv.org/)（Python 绑定）是一个广泛的计算机视觉库。
- [PyGaze](http://www.pygaze.org/) 是一个用于眼动追踪的 Python 库。
    - OpenSesame >= 3.0.0 需要 PyGaze >= 0.6.0。

## Mac OS 的说明

有三种方法可以为 Mac OS X 上的 OpenSesame 源代码准备软件环境。您可以分别下载并安装所有所需的包，或者使用基于存储库的包管理器 MacPorts 或 Homebrew 来组合所需的源代码环境。如今最简单且首选的方法是使用 Homebrew。这个包管理器运行非常快，能很好地处理依赖关系要求，并且维护得很好。另一个包管理器，MacPorts，基本上是一个包含从 Linux 移植到 Mac OS X（您可能已经知道，它们之间有很大关系，因为 Mac OS X 也是一个基于 Unix 的系统）的程序源代码的大型存储库。与 Homebrew 相比，Macports 需要花费惊人的长时间来编译所有依赖项。此外，尽管 Macports 以前的效果很好，但现在由于依赖问题经常出现“中断”。Homebrew 的缺点在于它不像 Macports 那样“完整”，您必须手动安装许多 Python 包（使用 easy_install 或 pip）。

### 下载 Xcode

如果您想使用 Homebrew 或 Macports 进行安装，首先需要做的是安装 Xcode，这是 Apple 的开发者工具包。您可以免费从 App Store 或他们的网站上获得最新版的 Xcode（不过您需要使用一个 Apple 帐户登录）。

网站： <https://developer.apple.com/xcode/>

使用 App Store 更为理想，因为它会使您的 Xcode 版本保持自动更新。但是，您还需要手动安装 Xcode 的命令行工具（每次更新后都需要这样做）。

### 使用 Homebrew 安装

Homebrew是在Mac上构建源代码树的更新和更简便的方法。它在macports之上具有许多优点，例如速度，而且现在似乎在编译和更新程序包方面比macports更少的遇到问题。
您可以按照<http://brew.sh/>上的说明安装homebrew。然后输入以下命令以开始：

    brew update
    brew doctor

解决“doctor”命令提出的任何问题。这应该很简单，解决方案（以简单命令的形式）通常已经与问题陈述一起给出。

接下来，使用homebrew的“tap”命令添加一些其他所需的存储库：

	brew tap homebrew/python
	brew tap homebrew/headonly
	brew tap homebrew/science

现在是时候开始安装homebrew自己的python环境了。其实没有必要在系统的python旁边安装另一个Python环境，但Homebrew版本通常更新且维护得更好，因此我们强烈推荐这样做。

    brew install python

安装Python后，您必须使其成为OS X使用的“默认”python。这意味着每当您在终端中输入“python”的命令时，将使用home-brewed python解释器，而不是默认的系统python。要做到这一点，请输入命令

    echo export PATH="/usr/local/bin:$PATH" >> ~/.bash_profile

这将把对所有homebrew材料位于的文件夹（/usr/local/bin）的引用放在PATH变量的其余部分的前面。从现在开始，每当您在终端中发出命令时，OS X将首先查找该文件夹中要执行的脚本或程序，如果在那里找不到，它将继续查找PATH变量中的其他文件夹。关闭并重新打开您的终端，或输入命令

	source ~/.bash_profile

以重新运行在您的.bash_profile中写的命令。如果您运行命令

    which python

它应该输出类似于“/usr/local/bin/python”的内容。如果它仍然输出“/usr/bin/python”，OSX仍在使用默认的系统Python，这并不是您想要的。您现在可以继续通过执行以下操作来安装其余的所需程序包

	brew install qt pyqt qscintilla2 freetype portaudio numpy scipy portmidi hg pillow

对于pygame来说，首先安装SDL库和smpeg更佳（这些都比OS X自带的版本好，仿佛缺少了一些重要功能）：

	brew install --HEAD smpeg
	brew install sdl sdl_image sdl_mixer sdl_ttf pygame

安装必要的python软件包

    pip install pyopengl pyflakes markdown python-bidi pyserial billiard

安装QProgEdit(从OpenSesame 2.8开始)

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	python setup.py install
	cd ..
	rm -R QProgEdit

安装expyriment (从OpenSesame 0.27开始)

    git clone https://github.com/expyriment/expyriment.git
	cd expyriment
	python setup.py install
	cd ..
	rm -R expyriment

安装psychopy及其依赖项pyglet。为了使psychopy正常工作，您（当前）需要从pyglet和psychopy的最新存储库版本中安装。

首先安装pyglet：

    hg clone https://code.google.com/p/pyglet/
	cd pyglet
	python setup.py install
	cd ..
	rm -R pyglet

然后安装psychopy。安装它并进行一些清理：

	git clone https://github.com/psychopy/psychopy.git
	cd psychopy
	python setup.py install
	cd ..
	rm -R psychopy

在安装过程中，您可能会收到一条带有“未知语言环境UTF8”的错误消息。您可以通过在~/.bash_profile中放置“LC_ALL=en_US.UTF8”这一行，然后重新打开终端来轻松解决此问题。

您现在应该能够运行 OpenSesame，但您会发现缺少一些图标！您需要从 <http://tiheum.deviantart.com/art/Faenza-Icons-173323228> 下载 Faenza 图标主题，并将其放置在 resources/theme/default/ 下。此外，还有一个小问题，即当主文件未作为 .py 文件存在时，多进程将无法工作，这是 opensesame 的情况。要启用多进程支持，您需要将 opensesame 文件重命名为 opensesame.py，然后如果您现在运行一次实验，您会看到已创建 opensesame.pyc。从该文件出现的那一刻起，Python 将在生成新进程时使用 .pyc，现在您可以将 opensesame.py 改回 opensesame。这是让多进程工作的奇怪解决方案，但目前我们只知道这一个。

以下软件包是可选的，但仍有可能是有用的，因此安装起来也不错：

	brew install matplotlib opencv
	pip install pycairo pyparallel scikit-image

### 使用 MacPorts 安装

在 Mac OS 上安装必要的软件包的另一种方法是使用 MacPorts，一个庞大的软件包仓库。安装运行 OpenSesame 所需的所有软件包需要很长时间（我是指许多小时！），因为 MacPorts 是通过源码编译来工作的。但从好的方面来看，这是一个相当简单的过程。

#### 下载 MacPorts

您可以从其网站上下载 macports，您还可以在网站上找到所需的文档和所有可用软件包的目录。

网站：<http://www.macports.org/install.php>

您可以将 +universal 添加到 /opt/local/etc/macports/variants.conf 中，以便向 MacPorts 请求使用该变体构建您安装的所有端口（即 32 位和 64 位），而无需记住在每个安装命令中键入它。然而，有些端口尚未作为通用二进制文件进行测试，可能无法正常构建。

#### 安装依赖项

基本上，您现在可以通过在终端中运行单个命令来安装所有所需的软件包：

	sudo port install py27-game py27-pyqt4 py27-scintilla py27-serial py27-pil py27-opengl py27-pyaudio opencv +python27 py27-pip

这需要很长时间，而且在我的例子中，由于校验和错误，它崩溃了几次。您可以通过执行以下命令简单地从这类错误中恢复：

	sudo port clean --all [package_that_caused_the_error]

然后重复第一个命令，MacPorts 应该会继续运行。

使用 pip 安装剩余的必要 python 软件包

    sudo pip install pyflakes markdown python-bidi pyserial billiard

安装 QProgEdit（从 OpenSesame 2.8 开始的默认代码编辑器）

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	sudo python setup.py install
	cd ..
	rm -R QProgEdit

#### Expyriment 和 Psychopy 后端

OpenSesame 除了基于 pygame 的传统后端外，还提供了使用 expyriment 或 psychopy 的选项。与传统后端相反，这两个后端都是硬件加速（OpenGL）的，并且应该具有更高的定时精度。

安装 expyriment（从 OpenSesame 0.27 开始）

    git clone https://github.com/expyriment/expyriment.git
    cd expyriment
    sudo python setup.py install
    cd ..
    rm -R expyriment

安装 psychopy 及其依赖项 pyglet：

首先安装 pyglet：

    hg clone https://code.google.com/p/pyglet/
    cd pyglet
    sudo python setup.py install
    cd ..
    rm -R pyglet

然后安装 psychopy：

    git clone https://github.com/psychopy/psychopy.git
    cd psychopy
    python setup.py install
    cd ..
    rm -R psychopy

PsychoPy 在没有安装 wxPython 库的情况下拒绝运行（这很奇怪，因为 OpenSesame 不使用 psychopy 的任何 wx GUI 组件），所以作为最后一步，请使用以下命令安装 wxPython ：

	sudo port install py27-wxpython-dev

#### 将 MacPorts Python 设为默认 Python

Mac OS带有一个定制版本的Python，但是为了我们（以及许多）的目的，您需要官方的Python。MacPorts已经安装了它，但是您仍然需要将其设置为默认。您可以使用以下命令执行此操作：

	sudo port select --set python python27

### 手动安装软件包

如果您想自己安装所有Opensesame依赖项，您需要下载并安装以下软件包分发：

#### 安装Python

OS X附带的Python安装通常是较旧的版本。因此，最好从python.org安装最新版本：

网站： <http://www.python.org/>

直接下载：http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg

另一个选择是安装 [Enthought Python Distribution (EPD)][EPD_Download]。此发行版包括Python和OpenSesame所依赖的许多模块（[查看][EPD_Packages] 完整列表）。

#### 安装PyGame

网站： <http://www.pygame.org/>

直接下载（Snow Leopard）：<http://www.pygame.org/ftp/pygame-1.9.2pre-py2.6-macosx10.6.mpkg.zip><br/>
直接下载（（Mountain）Lion）：<http://www.pygame.org/ftp/pygame-1.9.2pre-py2.7-macosx10.7.mpkg.zip>

#### 安装PyQt4

Riverbank没有为Mac OS X提供PyQt4的官方分发。但是有一些维护良好的非官方分发版：

官方网站： <http://www.riverbankcomputing.co.uk/software/pyqt/intro>

Mac OS X发行版（PyQtX）网站： <http://sourceforge.net/projects/pyqtx/> (直接下载：<http://sourceforge.net/projects/pyqtx/files/latest/download>)

安装了PyQt4之后，请下载并安装与OpenSesame内联脚本编辑器一起使用的QScintilla模块：

PyQScintillaX： <http://sourceforge.net/projects/pyqtx/files/PyQScintillaX/>

#### 安装NumPy和SciPy

可以通过两种方式获取NumPy或SciPy的最新版本：

您可以使用位于<http://fonnesbeck.github.com/ScipySuperpack/>的安装脚本（直接下载：<https://raw.github.com/fonnesbeck/ScipySuperpack/master/install_superpack.sh>）以及如何使用它的说明。这个脚本将自动查找numpy和scipy的最新版本并为您安装它们。基本上，您只需在下载脚本的文件夹中的控制台中运行

	sudo sh ./install_superpack.sh

或者，您可以从项目自己的网站上下载并安装软件包：

Numpy：<http://sourceforge.net/projects/numpy/files/NumPy/> (直接下载版本1.7.0：<http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/numpy-1.7.0-py2.7-python.org-macosx10.6.dmg/download>)
Scipy：<http://sourceforge.net/projects/scipy/files/scipy/> (直接下载版本0.11.0：<http://sourceforge.net/projects/scipy/files/scipy/0.11.0/scipy-0.11.0-py2.7-python.org-macosx10.6.dmg/download>)

#### 安装PsychoPy和Expyriment（可选）

PsychoPy需要安装许多依赖项。大多数这些依赖项可以通过使用setuptools轻松安装。

网站： <http://pypi.python.org/pypi/setuptools>

直接下载：<http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea>

如网站所述，安装应通过以下步骤进行：

下载与您的Python版本相匹配的适当蛋（例如setuptools-0.6c9-py2.7.egg）。不要重命名它。

将其运行为shell脚本，例如

	sh setuptools-0.6c9-py2.7.egg

setuptools将使用匹配的Python版本（例如python2.7）安装自己，并将easy_install可执行文件放置在安装Python脚本的默认位置 （根据标准distutils配置文件或Python安装程序确定）。
之后，使用以下命令安装大多数依赖项：

	sudo easy_install psychopy pyglet pyopengl pil expyriment

您可能需要手动安装Matplotlib, wxPython，因为（在测试时）这些易安装程序未能安装。确保您安装与您的Python版本匹配的版本。

*注意：* psychopy后端似乎还无法正常工作且会崩溃。原因是PsychoPy（或者说其底层库pyglet）尚无法应对新版Mac OS X中的64位cocoa环境。在众多软件新版本中极有可能已经解决这个问题。

#### 安装wxPython（可选，PsychoPy后端所需）

您可以自行下载wxPython或使用easy_install进行安装（参见"安装PsychoPy"）。

网站：<http://wxpython.org/>

直接下载：<http://downloads.sourceforge.net/wxpython/wxPython2.9-osx-2.9.4.0-cocoa-py2.7.dmg>

#### 安装PyOpenGL（可选，适用于opengl或expyriment后端）

您可以自行下载PyOpenGL或者使用easy_install进行安装（请参阅“安装PsychoPy”）。

网站：<http://pyopengl.sourceforge.net/>

直接下载：<https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.0.2.tar.gz#md5=77becc24ffc0a6b28030aa109ad7ff8b>

### 运行OpenSesame

在此处下载最新的OpenSesame版本源代码。将.tar.gz解压缩到您的主文件夹（其他位置按类似方式操作）。打开一个终端，切换到OpenSesame的位置（此示例假定版本为0.26）：

	cd /Users/[your username]/opensesame-0.26

使用以下命令之一运行OpenSesame：

	python opensesame
	python opensesame --debug

[winpython-based package]: /getting-opensesame/running-with-python-portable/
[EPD_Download]: http://www.enthought.com/products/epd.php
[EPD_Packages]: http://www.enthought.com/products/epdlibraries.php
[xpyriment]: /backends/xpyriment
[legacy]: /backends/legacy
[psycho]: /backends/psycho
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl