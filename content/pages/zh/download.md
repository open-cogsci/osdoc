title: 下载
hash: 9beb2ebf584b530f7411227d288486a4076872b885ede71e4a690dd50ad929c9
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

<h3>您的下载很快就会开始！</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; 订阅 SigmundAI.eu
</a>

您的 OpenSesame AI助理伙伴。每月 9 欧元的订阅费用支持 OpenSesame 的发展。

如果您的下载没有自动开始，请点击<a id="click-here">这里</a>。
</div>


## 概述

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 标准安装选项

最新版 $status$ 版本为 $version$ *$codename$* ([更新日志](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 免安装版 (.zip)
</a>

大多数用户会下载 `.exe` 安装包。如果您没有管理员权限，或者需要同时运行多个版本的 OpenSesame，请下载 `.zip` 包。

基于 Python 3.13，适用于 64 位系统。在 Windows 11 上测试通过。


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 安装包 (.dmg)
</a>

首次启动 OpenSesame 时，操作系统会因应用程序非受信开发者而阻止该程序。您可以在“设置” > “隐私与安全性”中找到“始终允许打开”选项。该选项会在应用被拦截后出现。

基于 Python 3.13，适用于 64 位 intel 系统。在 Mac OS X Sequoia 上测试通过。


### Linux / Ubuntu

将以下命令复制粘贴到终端中。这将下载并运行安装脚本。

```bash
# 这些包需要在 Ubuntu 24.04 上安装。
# 其他 Linux 发行版请安装相应的软件包。
sudo apt install curl python3-venv libxcb-cursor0
# 下载并运行 OpenSesame 安装脚本。
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

已在 Ubuntu 24.04（Python 3.12）上测试通过。


## 高级安装选项


### PyPi（跨平台）

所有包都可以通过 pip 安装。注意 OpenSesame 在 PyPi 上称为 `opensesame-core`。

OpenSesame 核心依赖项：

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy 用于（默认）psycho 后端。根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。如果发生这种情况，请在技术支持论坛寻求帮助，或使用预制包/安装程序。

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze 用于眼动追踪：

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment 用于 xpyriment 后端

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

安装完所有包后，您只需运行：

```bash
opensesame
```

或运行 Sigmund Analyst（代码编辑器）：

```bash
sigmund-analyst
```


### Anaconda（跨平台）

首先，为 OpenSesame 创建一个新的 Python 环境（可选）

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

接下来，按照上述 PyPi 安装说明操作。不再单独提供 Anaconda 包。


### 老版本

旧版本可从 GitHub 发布页面下载：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 获取。


## 提示


### 应该使用哪个版本的 Python？

OpenSesame 目前基于 Python 3.13 构建并测试。其他版本的 Python（>=3.10）也可以使用，但没有经过全面测试。Python 2 已不再支持。最后一个包含 Python 2 安装包的版本是 3.3.12，可以从 [发布归档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。


### 何时（不）更新？

- 在开发和测试实验时应更新；使用最新版 OpenSesame 总是最佳选择。
- 正在运行实验时请勿更新；也就是说，在数据采集期间不要更新。
- 用于开发和测试的 OpenSesame 版本也应用于正式实验。


### 手动升级软件包

OpenSesame 是一个常规的 Python 环境，可以在 Jupyter 控制台中运行 `pip install` 命令。


### 给系统管理员的提示

- 当 OpenSesame 发布新主版本（版本号以 0 结尾，例如 3.1.0）时，通常很快会有一到两个维护发布（如 3.1.1 和 3.1.2）用于修复重大漏洞。因此，如果你是在不经常更新的软件系统上安装 OpenSesame，最好等待第二或第三个维护发布（如 3.0.2、3.1.3 等）。这样可以最大限度地减少推出包含重大漏洞版本的风险。
- Windows 安装程序支持使用 `/S` 标志静默安装 OpenSesame。