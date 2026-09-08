title: 下载
hash: 43af7638374babac965b68a0a316b0487bd9a9f780ffb4e0674e0c7e015f026e
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

您在 OpenSesame 中的 AI 副驾驶。您每月 €9 的订阅支持 OpenSesame。

如果下载未开始，请点击<a id="click-here">这里</a>。
</div>


## 概览

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 标准安装选项

最新的 $status$ 版本为 $version$ *$codename$*（[发行说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$)）。


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 无需安装版本 (.zip)
</a>

大多数人会下载安装程序 `.exe`。如果您没有管理员权限，或者需要并行运行多个版本的 OpenSesame，请改为下载 `.zip` 包。

基于适用于 64 位系统的 Python 3.13。在 Windows 11 上测试。

某些外部设备，例如 [Tobii](%url:tobii%) 眼动仪，需要不同版本的 Python。请访问相应的文档页面以获取更多信息。


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 软件包 (.dmg)
</a>

首次启动 OpenSesame 时，操作系统会阻止它，因为该应用并非来自受信任的开发者。您可以在“设置”>“隐私与安全性”中找到“仍要打开”选项。该选项会在应用被阻止后出现。

基于适用于 64 位 intel 系统的 Python 3.13。在 Mac OS X Sequoia 上测试。

某些外部设备，例如 [Tobii](%url:tobii%) 眼动仪，需要不同版本的 Python。请访问相应的文档页面以获取更多信息。


### Linux / Ubuntu

将以下内容复制并粘贴到终端中。这将下载并运行安装脚本。

```bash
# These packages need to be installed on Ubuntu 24.04.
# Equivalent packages need to be installed on other
# Linux distributions.
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# Download and run the OpenSesame installation script.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/nightingale/linux-installer.sh) --install
```

在 Ubuntu 24.04（Python 3.12）上测试。


## 高级安装选项


### PyPi（跨平台）

所有软件包都可以通过 pip 安装。请注意，OpenSesame 在 PyPi 上名为 `opensesame-core`。

OpenSesame 核心依赖项：

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

用于（默认）psycho backend 的 PsychoPy。根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。如果发生这种情况，请在支持论坛寻求帮助，或使用预构建的软件包/安装程序。

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

用于眼动追踪的 PyGaze：

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

用于 xpyriment backend 的 Expyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

安装完所有软件包后，您只需运行以下命令即可启动 OpenSesame：

```bash
opensesame
```

或者用于 Sigmund Analyst（代码编辑器）：

```bash
sigmund-analyst
```


### Anaconda（跨平台）

首先，为 OpenSesame 创建一个新的 Python 环境（可选）

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

接下来，请按照上述 PyPi 安装说明操作。不再提供专用的 Anaconda 软件包。


### 旧版 OpenSesame 和其他 Python 版本

旧版 OpenSesame，以及使用不同 Python 版本（3.10、3.11 和 3.12）构建的软件包，可在 GitHub releases 中获取：

- <https://github.com/open-cogsci/OpenSesame/releases>



### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 上获取。


## 提示


### 应使用哪个版本的 Python？

OpenSesame 目前使用 Python 3.13 构建和测试。其他 Python >=3.10 版本也可运行，但尚未经过广泛测试。Python 2 已不再受支持。最后一个包含 Python 2 软件包的版本是 3.3.12，仍可从[发布存档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12)下载。


### 何时（不）更新？

- 在开发和测试实验时进行更新；始终最好使用最新版本的 OpenSesame。
- 在运行实验期间不要更新；也就是说，不要在收集数据时更新。
- 使用与开发和测试时相同版本的 OpenSesame 运行实验。


### 手动升级软件包

OpenSesame 是一个常规 Python 环境，您可以在 Jupyter 控制台中运行 `pip install` 命令。


### 面向系统管理员的提示

- 发布新的 OpenSesame 主要版本时（版本号以 0 结尾，例如 3.1.0），通常会很快发布一到两个维护版本（例如 3.1.1 和 3.1.2）来修复重大错误。因此，如果您要在不经常更新的系统上安装 OpenSesame，最好等到第二个或第三个维护版本（例如 3.0.2、3.1.3 等）。这样可以最大限度地降低部署包含重大错误的 OpenSesame 版本的风险。
- Windows 安装程序允许您使用 `/S` 标志静默安装 OpenSesame。