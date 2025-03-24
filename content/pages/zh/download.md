title: 下载
hash: 48b36f28d46849599cac6b02aa148d9b70d6476758c8b21e016736aed881ea59
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

<h3>您的下载将很快开始！</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; 订阅 SigmundAI.eu
</a>

比 ChatGPT 更适合 OpenSesame 问题。您的 €9/月订阅支持 OpenSesame。

如果下载没有开始，请点击<a id="click-here">这里</a>。
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

Windows 软件包基于适用于 64 位系统的 Python 3.11。安装程序和 `.zip` 软件包是相同的，只是安装方式不同。大多数人会下载安装程序包（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> 无需安装的 Windows 压缩包 (.zip)
</a>


### Mac OS

[这篇文章](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) 在 Mac OS 支持网站上解释了如何覆盖 Mac OS 的安全设置，Mac OS 默认会阻止 OpenSesame 启动。第一次启动 OpenSesame 需要很长时间，随后的启动会快很多。

下面的包是为 Intel 处理器构建的，但也可以在 ARM (M1) 处理器上运行。

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Intel x64 的 Python 3</b> Mac OS 软件包 (.dmg)
</a>

要使用 [Homebrew](https://brew.sh/) 安装 OpenSesame，请在终端中运行以下命令：

```bash
brew install --cask opensesame
```


### Ubuntu

软件包是在 Ubuntu 24.04 Jammy Jellyfish 上开发和测试的。在其他版本的 Ubuntu 上可能会有所不同。

如果您已安装 OpenSesame 3.X，请首先卸载所有软件包。这是为了避免由于 OpenSesame 4.0 中某些软件包的轻微重命名而导致的软件包冲突。

```bash
# 如有必要：卸载 OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

接下来，添加所需的存储库到您的软件源并安装 OpenSesame（和 Rapunzel），在终端中运行以下命令：

```bash
# 添加稳定软件包的存储库
sudo add-apt-repository ppa:smathot/cogscinl
# 添加开发软件包的存储库
sudo add-apt-repository ppa:smathot/milgram
# 安装 OpenSesame 4.X 软件包及有用的扩展
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

有些常用的软件包无法通过 PPA 获得。您可以通过 `pip` 安装它们：

```bash
# 安装通过 pip 提供的可选软件包
pip install --break-system-packages --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy 最好通过 pip 安装，因为 Ubuntu 软件包当前已损坏。

```bash
# 首先安装自定义版本的 wxPython，这是 PsychoPy 所需的
pip install --break-system-packages https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04/wxPython-4.2.2-cp312-cp312-linux_x86_64.whl
# 然后安装 psychopy，并忽略对 Python <=3.11 的要求，因为 Ubuntu 24.04 使用的是 Python 3.12
pip install --break-system-packages --ignore-requires-python psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (跨平台)

所有软件包都可以通过 pip 安装。请注意，OpenSesame 在 PyPi 上被称为 `opensesame-core`。

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

您可能还需要安装 PyQt5 和 QtWebEngine，它们提供 GUI 工具包：

```bash
pip install pyqt5 pyqtwebengine
```


安装完所有软件包后，只需运行 OpenSesame 即可（激活正确的环境后）：

```bash
opensesame
```

或者对于 Rapunzel 代码编辑器：

```bash
rapunzel
```


### Anaconda (跨平台)

首先，为 OpenSesame 创建一个新的 Python 环境（可选）：

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

接下来，添加相关的频道 (`cogsci`) 和 (`conda-forge`)，并安装所有相关软件包。确保 `pyqode.core` 和 `pyqode.python` 是来自 `cogsci` 频道的 >= 3.2，而不是来自 `conda-forge` 频道的旧版本。

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

有些软件包不能通过 conda 获得。您可以使用 `pip install` 来安装这些软件包。（PsychoPy 在某些系统上安装失败，因此在此处单独安装。）

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

安装完所有软件包后，只需运行 OpenSesame 即可（激活正确的环境后）：

```bash
opensesame
```

或者对于 Rapunzel 代码编辑器：

```bash
rapunzel
```


### 较旧版本

较旧版本可以从 GitHub releases 下载：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 上获得。


## 提示


### 使用哪个版本的 Python？

OpenSesame 当前使用 Python 3.11 构建和测试。其他版本的 Python >=3.7 可以使用，但未经全面测试。Python 2 不再被支持。包含 Python 2 包的最后一个版本是 3.3.12，仍可从 [release archive](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。


### 什么时候（不）更新？

- 在开发和测试实验时更新；最好使用最新版的 OpenSesame。
- 在运行实验时不要更新；也就是说，在收集数据时不要更新。
- 使用与开发和测试时相同版本的 OpenSesame 来运行实验。


### 手动升级软件包

OpenSesame 是一个常规的 Python 环境，您可以按以下描述使用 `pip` 或 `conda` 升级软件包：

- <https://rapunzel.cogsci.nl/manual/environment/>


### 系统管理员提示

- 当 OpenSesame 的一个新的主要版本发布时（版本号以 0 结尾，例如 3.1.0），通常会紧随其后发布一两个维护版本（例如 3.1.1 和 3.1.2），以解决主要的漏洞。因此，如果您在不经常更新的系统上安装 OpenSesame，最好等到第二或第三个维护版本（例如 3.0.2、3.1.3 等）。这样可以最大限度地减少推出包含重大漏洞的 OpenSesame 版本的风险。
- Windows 安装程序允许您使用 `/S` 标志静默安装 OpenSesame。