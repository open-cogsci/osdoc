title: 下载
hash: c3287b768243f4d57f2068746ebea3538a3441372f6a29ed902c5fe1429fa59e
locale: zh
language: Chinese

```javascript
<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('download-started').style.display = 'block'
	document.getElementById('download-started').scrollIntoView()
}
</script>

<div class="info-box" id="download-started" markdown="1" style="display:none;">

<h3>您的下载应会很快开始！</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; 订阅 SigmundAI.eu
</a>

适用于OpenSesame问题的服务优于ChatGPT。您每月9欧元的订阅费将支持OpenSesame。

如果您的下载没有开始，请点击<a id="click-here">这里</a>。
</div>

## 概览

## 所有下载选项

最新的$status$版本是$version$ *$codename$*（[发布说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$)）。

### Windows

Windows包基于64位系统的Python 3.11。安装程序和`.zip`包的内容是相同的，除了安装方式不同。大多数人下载安装程序包（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows安装程序（.exe）
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> 无需安装的Windows程序（.zip）
</a>

### Mac OS

[这篇文章](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) 在Mac OS支持网站上解释了如何覆盖Mac OS的安全设置，这些设置默认会阻止启动OpenSesame。您第一次启动OpenSesame时，应用程序开启需要很长时间；之后的启动会快很多。

下面的包适用于Intel处理器，但也可以在ARM（M1）处理器上运行。

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>针对Intel x64的Python 3</b> Mac OS包（.dmg）
</a>

要通过[Homebrew](https://brew.sh/)安装OpenSesame，请在终端运行以下命令：

```bash
brew install --cask opensesame
```

### Ubuntu

软件包在Ubuntu 22.04 Jammy Jellyfish上开发和测试。软件包仅适用于22.04和22.10版本。

如果您已经安装了OpenSesame 3.X，请首先卸载所有包。这是必须的，以避免由于OpenSesame 4.0中某些包的轻微重命名而造成的包冲突。

```bash
# 如果必要：卸载OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

接下来，要将所需的存储库添加到您的软件源并安装OpenSesame（及Rapunzel），在终端运行以下命令：

```bash
# 添加稳定包的存储库
sudo add-apt-repository ppa:smathot/cogscinl
# 添加开发包的存储库
sudo add-apt-repository ppa:smathot/milgram
# 安装OpenSesame 4.X包加上有用的扩展
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

有些常用的包不通过PPA提供。您可以通过`pip`安装：

```bash
# 安装只通过pip提供的可选包
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

通过pip安装PsychoPy是最好的，因为Ubuntu的包目前已损坏。

```bash
# 安装psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```

### PyPi（跨平台）

所有的包可以通过pip安装。请注意，在PyPi上OpenSesame被称为`opensesame-core`。

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

安装完所有包之后，只需在激活了正确环境后运行以下命令即可启动 OpenSesame：

```bash
opensesame
```

或者启动 Rapunzel 代码编辑器：

```bash
rapunzel
```


### Anaconda（跨平台）

首先，为 OpenSesame 创建一个新的 Python 环境（可选）：

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

接下来，添加相关频道（`cogsci`）和（`conda-forge`），并安装所有相关的包。确保从 `cogsci` 频道获取的 `pyqode.core` 和 `pyqode.python` 版本 >= 3.2，而不是 `conda-forge` 频道的较旧版本。

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

有些包在 conda 中不可用。您可以使用 `pip install` 来安装这些包。（PsychoPy 在某些系统上安装可能会失败，因此它会在下面单独安装。）

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

安装完所有包之后，只需在激活了正确环境后运行以下命令即可启动 OpenSesame：

```bash
opensesame
```

或者启动 Rapunzel 代码编辑器：

```bash
rapunzel
```


### 旧版本

可以从 GitHub 发布页下载旧版本：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame 的源代码可以在 [GitHub](https://github.com/open-cogsci/OpenSesame) 上找到。


## 小贴士


### 应该使用哪个版本的 Python？

OpenSesame 目前是使用 Python 3.11 构建和测试的。其他 Python 版本 >=3.7 也可以工作，但没有经过广泛测试。Python 2 不再受支持。最后一个包含 Python 2 包的版本是 3.3.12，仍然可以从 [发布存档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 中下载。


### 什么时候（不）更新？

- 开发和测试实验时更新；最好总是使用 OpenSesame 的最新版本。
- 在进行实验时不要更新；即在收集数据时不要更新。
- 使用您开发和测试时所用的同一版本的 OpenSesame 来运行实验。


### 手动升级包

OpenSesame 是一个常规的 Python 环境，您可以如下使用 `pip` 或 `conda` 来升级包：

- <https://rapunzel.cogsci.nl/manual/environment/>


### 给系统管理员的小贴士

- 当发布新的 OpenSesame 主要版本时（版本号以 0 结尾，例如 3.1.0），通常会很快接着发布一两个维护版本（例如 3.1.1 和 3.1.2），以解决主要的错误。因此，如果您要在不经常更新的系统上安装 OpenSesame，最好等到第二个或第三个维护版本发布（例如 3.0.2、3.1.3 等）。这样您可以将推出包含主要错误的 OpenSesame 版本的风险降到最低。
- Windows 安装程序允许您使用 `/S` 标志来无声安装 OpenSesame。