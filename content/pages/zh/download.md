title: 下载
hash: bb4581487a399790e873f0a07ab48b9c8592ed4061874de0b12d80d523c84678
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

<h3>您的下载应该会很快开始！</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://www.buymeacoffee.com/cogsci">
<span class="glyphicon glyphicon-heart" aria-hidden="true"></span>
请帮我们保持专注并给我们买一杯咖啡！
</a>

咖啡使我们保持清醒，以便我们可以开发免费软件，并在支持论坛上回答您的问题！

点击<a id="click-here">这里</a>，如果您的下载没有开始。
</div>


## 概述

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 所有下载选项

最新的 $status$ 版本是 $version$ *$codename$*, 发布于 $release-date$（[发行说明](http://osdoc.cogsci.nl/$branch$/zh/notes/$notes$)）。

### Windows

Windows 软件包基于 Python 3.11，面向 64 位系统。安装程序和 `.zip` 软件包相同，只是安装方式不同。大多数人下载安装程序软件包（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序（.exe）
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> 不需要安装的 Windows（.zip）
</a>


### Mac OS

目前还没有 OpenSesame 4.0 的 Mac OS 预发布软件包。请使用 conda 或 pip。
{: .page-notification}

[Mac OS 支持网站上的这篇文章](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) 解释了如何覆盖 Mac OS 的安全设置，以防止 OpenSesame 默认启动。

下面的软件包是为 Intel 处理器构建的，但也可以在 ARM (M1) 处理器上运行。

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 for Intel x64</b> Mac OS 软件包（.dmg）
</a>

要使用 [Homebrew](https://brew.sh/) 安装 OpenSesame，在终端中运行以下命令：

```bash
brew install --cask opensesame
```


### Ubuntu

软件包是在 Ubuntu 22.04 Jammy Jellyfish 上开发和测试的。软件包仅适用于 22.04 和 22.10。

如果您已安装 OpenSesame 3.X，首先卸载所有软件包。这是为了避免由于 OpenSesame 4.0 中部分软件包重命名而导致的软件包冲突。

```bash
# 如果需要：卸载 OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

接下来，要将所需的存储库添加到您的软件源并安装 OpenSesame（和 Rapunzel），请在终端中运行以下命令：

```bash
# 添加稳定包存储库
sudo add-apt-repository ppa:smathot/cogscinl
# 添加开发包存储库
sudo add-apt-repository ppa:smathot/milgram
# 安装 OpenSesame 4.X 软件包及有用的扩展
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

一些常用软件包无法通过 PPA 获取。您可以通过 `pip` 安装它们：

```bash
# 安装仅通过 pip 提供的可选软件包
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

最好通过 pip 安装 PsychoPy，因为 Ubuntu 软件包当前已损坏。

```bash
# 安装 psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi（跨平台）

所有软件包均可通过pip安装。请注意，在PyPi上，OpenSesame被称为`opensesame-core`。

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

安装了所有软件包后，只需运行一下命令（激活正确的环境后）来启动OpenSesame：

```bash
opensesame
```

或者启动Rapunzel代码编辑器：

```bash
rapunzel
```


### Anaconda（跨平台）

首先，为OpenSesame创建一个新的Python环境（可选）：

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

接下来，添加相关通道（`cogsci`和`conda-forge`），并安装所有相关软件包。确保`pyqode.core`和`pyqode.python`版本>= 3.2 来自`cogsci`通道，而不是来自`conda-forge`通道的旧版本。

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

有些软件包无法通过conda安装。您可以使用`pip install`安装这些软件包。

```bash
pip install soundfile pygame psychopy psychopy-sounddevice http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

安装了所有软件包后，只需运行一下命令（激活正确的环境后）来启动OpenSesame：

```bash
opensesame
```

或者启动Rapunzel代码编辑器：

```bash
rapunzel
```


### 旧版本

可以从GitHub发布版本中下载旧版本：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 上找到。


## 建议


### 使用哪个版本的Python？

目前，OpenSesame与Python 3.11.0进行构建和测试。Python >=3.7的其他版本可用，但未经过广泛测试。Python 2已不再支持。最后一个包含Python 2软件包的版本是3.3.12，仍可从 [发行版本归档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。


### 何时（不）更新？

- 在开发和测试实验时更新；使用OpenSesame的最新版本总是最好的。
- 在运行实验时不要更新；也就是说，收集数据时不要更新。
- 使用用于开发和测试的相同版本的OpenSesame运行实验。


### 手动升级软件包

OpenSesame是一个常规的Python环境，您可以按照以下方法使用`pip`或`conda`升级软件包：

- <https://rapunzel.cogsci.nl/manual/environment/>


### 系统管理员的提示

- 当OpenSesame发布一个新的主要版本（版本号以0结尾，例如3.1.0），它通常会很快跟随一两个维护版本（例如3.1.1和3.1.2），以解决主要错误。因此，如果您在不经常更新的系统上安装OpenSesame，最好等到第二个或第三个维护版本（例如3.0.2，3.1.3等）。这样，您可以将推出包含主要错误的OpenSesame版本的风险降到最低。
- 使用 `/S`参数 ，Windows安装程序允许您静默安装OpenSesame。
