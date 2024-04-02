title: 下载
hash: fd00279bec39b52c5cf277e973c6f314758b571714fbc3b1fb8730ac172aa061
locale: zh
language: Chinese

<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('download-started').style.display = 'block'
	document.getElementById('download-started').scrollIntoView()
}
</script>

<div class="info-box" id="download-started" markdown="1" style="display:none;">

<h3>您的下载将很快开始!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; 订阅 SigmundAI.eu
</a>

针对 OpenSesame 问题比 ChatGPT 更好。您每月9欧元的订阅支持 OpenSesame。

使用优惠码 NHVB3IXD 免费试用1个月。&#128293;

如果您的下载没有开始，请点击 <a id="click-here">这里</a>。
</div>


## 概览

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 所有下载选项

最新的 $status$ 版本是 $version$ *$codename$* ([发布说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。


### Windows

Windows 包基于 64 位系统的 Python 3.11。安装包和 `.zip` 包是一样的，除了安装方式。大多数人下载安装包（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 无需安装 (.zip)
</a>


### Mac OS

[这篇文章](https://support.apple.com/zh-cn/guide/mac-help/mh40616/mac) 在 Mac OS 支持网站上解释了如何覆盖 Mac OS 的安全设置，默认情况下它会阻止启动 OpenSesame。您第一次启动 OpenSesame 时，应用程序启动之前需要很长时间；后续启动会快得多。

下面的包是为 Intel 处理器构建的，但也可以在 ARM (M1) 处理器上运行。

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 for Intel x64</b> Mac OS 包 (.dmg)
</a>

要通过 [Homebrew](https://brew.sh/) 安装 OpenSesame，请在终端运行以下命令：

```bash
brew install --cask opensesame
```


### Ubuntu

包是在 Ubuntu 22.04 Jammy Jellyfish 上开发和测试的。仅为 22.04 和 22.10 提供包。

如果您安装了 OpenSesame 3.X，请首先卸载所有包。由于 OpenSesame 4.0 中一些包稍有重命名，必须这样做以避免包冲突。

```bash
# 如果需要：卸载 OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

接下来，要将所需的库添加到您的软件源并安装 OpenSesame（和 Rapunzel），请在终端运行以下命令：

```bash
# 添加稳定包的仓库
sudo add-apt-repository ppa:smathot/cogscinl
# 添加开发包的仓库
sudo add-apt-repository ppa:smathot/milgram
# 安装 OpenSesame 4.X 包和有用的扩展
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

一些常用的包不通过 PPA 提供。你可以通过 `pip` 安装它们：

```bash
# 通过 pip 安装只能通过 pip 获得的可选包
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

因为 Ubuntu 的包目前存在问题，所以通过 pip 安装 PsychoPy 是最佳选择。

```bash
# 安装 psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (跨平台)

所有的包可以通过pip安装。请注意，在PyPi上，OpenSesame被称为`opensesame-core`。

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

一旦你安装了所有的包，你可以（在激活了正确的环境之后）通过运行以下命令简单地运行OpenSesame：

```bash
opensesame
```

或者是Rapunzel代码编辑器：

```bash
rapunzel
```


### Anaconda（跨平台）

首先，为OpenSesame创建一个新的Python环境（可选）：

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

接下来，添加相关频道（`cogsci`）和（`conda-forge`），并安装所有相关的包。确保`pyqode.core` 和 `pyqode.python` 是来自`cogsci`频道的>= 3.2版本，而不是来自`conda-forge`频道的旧版本。

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

有些包在conda中不可用。你可以使用`pip install`来安装这些包。（PsychoPy在一些系统上安装失败，这就是为什么它在下面单独安装。）

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

一旦你安装了所有的包，你可以（在激活了正确的环境之后）通过运行以下命令简单地运行OpenSesame：

```bash
opensesame
```

或者是Rapunzel代码编辑器：

```bash
rapunzel
```


### 旧版本

旧版本可以在GitHub的发布页面下载：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame的源代码可以在[GitHub](https://github.com/open-cogsci/OpenSesame)上获得。


## 小贴士


### 使用哪个版本的Python？

OpenSesame目前是用Python 3.11构建和测试的。其他>=3.7的Python版本也可以工作，但没有进行广泛的测试。Python 2不再受支持。最后一个包含Python 2包的发布版本是3.3.12，仍然可以从[发布档案](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12)下载。


### 什么时候（不）更新？

- 在开发和测试你的实验时更新；最好使用OpenSesame的最新版本。
- 在运行实验时不要更新；也就是说，在你收集数据的时候不要更新。
- 用你用于开发和测试的相同版本的OpenSesame来运行实验。


### 手动升级包

OpenSesame是一个常规的Python环境，你可以使用`pip`或`conda`来升级包，如下所述：

- <https://rapunzel.cogsci.nl/manual/environment/>


### 系统管理员的小贴士

- 当OpenSesame发布一个新的主要版本（版本号以0结尾，例如3.1.0）时，通常会很快有一到两个维护版本（例如3.1.1和3.1.2）跟上，以处理主要的错误。因此，如果你在不经常更新的系统上安装OpenSesame，最好等到第二个或第三个维护版本（例如3.0.2，3.1.3等）。这样你就可以最大限度地降低推出包含主要错误的OpenSesame版本的风险。
- Windows安装程序允许你使用`/S`标志进行无提示安装OpenSesame。