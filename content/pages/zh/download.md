title: 下载
hash: 4c609d80d00e5704f1e59d0daf4820641810168b01ec87f556a20c226969d520
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

<h3>您的下载即将开始！</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; 订阅 SigmundAI.eu
</a>

在 OpenSesame 问题方面比 ChatGPT 更出色。您的 €9/月 订阅费用将支持 OpenSesame。

如果您的下载没有开始，请点击<a id="click-here">这里</a>。
</div>


## 概述

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
	<b>标准</b> Windows 安装程序（.exe）
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 免安装包（.zip）
</a>

大多数人会下载 `.exe` 安装程序包。如果您没有管理员权限，或需要同时运行多个 OpenSesame 版本，请下载 `.zip` 包。

基于 64 位系统的 Python 3.13。已在 Windows 11 上测试。


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 安装包（.dmg）
</a>

当您首次启动 OpenSesame 时，操作系统会因应用非来自信任开发者而阻止其运行。您可以在 设置 > 隐私与安全 中找到“仍要打开”选项。该选项会在应用被阻止后出现。

基于适用于英特尔 64 位系统的 Python 3.13。已在 Mac OS X Sequoia 上测试。


### Linux / Ubuntu

将以下命令复制粘贴到终端。这将下载并运行安装脚本。该安装脚本需要 curl 和 virtualenv。在 Ubuntu 上可通过 `sudo apt install curl python3-venv` 进行安装。

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

已在 Ubuntu 24.04（Python 3.12）上测试。


## 高级安装选项


### PyPi（跨平台）

所有软件包都可以使用 pip 安装。请注意，OpenSesame 在 PyPi 上的名称为 `opensesame-core`。

OpenSesame 核心依赖：

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

用于（默认）psycho 后端的 PsychoPy。根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。如果遇到此问题，请前往支持论坛寻求帮助，或使用预制软件包/安装程序。

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

用于眼动追踪的 PyGaze：

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

用于 xpyriment 后端的 Expyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

安装全部软件包后，您可以通过运行：

```bash
opensesame
```

来启动 OpenSesame。

或者启动 Sigmund Analyst（代码编辑器）：

```bash
sigmund-analyst
```


### Anaconda（跨平台）

首先，为 OpenSesame 创建新的 Python 环境（可选）

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

接下来，请参照上方的 PyPi 安装说明。已不再提供专用 Anaconda 软件包。


### 旧版本

旧版本可从 GitHub releases 页面下载：

- <https://github.com/open-cogsci/OpenSesame/releases>

### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 获取。

## 提示

### 应该使用哪个版本的 Python？

OpenSesame 目前是基于 Python 3.13 构建和测试的。其他版本的 Python（>=3.10）也可以使用，但未经过充分测试。不再支持 Python 2。最后一个包含 Python 2 安装包的版本为 3.3.12，仍可在 [发布归档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。

### 什么时候（不）应该更新？

- 在进行实验开发和测试时更新；始终建议使用最新版本的 OpenSesame。
- 在运行实验时不要更新；也就是说，在收集数据时不要更新。
- 运行实验时应使用与开发和测试所用一致的 OpenSesame 版本。

### 手动升级软件包

OpenSesame 是一个常规的 Python 环境，你可以在 Jupyter 控制台中运行 `pip install` 命令。

### 系统管理员提示

- 当发布 OpenSesame 的新主版本（以 0 结尾的版本号，例如 3.1.0）时，通常会很快跟进一到两个维护版本（例如 3.1.1 和 3.1.2），以修复主要的漏洞。因此，如果你是在不经常更新的系统上安装 OpenSesame，最好等到第二或第三个维护版本发布后再进行安装（如 3.0.2、3.1.3 等）。这样可以最大程度减少部署含有重大缺陷版本的风险。
- Windows 安装程序允许你使用 `/S` 参数进行静默安装。