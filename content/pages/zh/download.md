title: 下载
hash: 02c996f07585f459badd7fcb648bad241d5c8415f54a7ceb58cd0b3f4dc465a5
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

<h3>您的下载应该很快就会开始！</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; 订阅 SigmundAI.eu
</a>

比 ChatGPT 更适合 OpenSesame 问题。您的 9 欧元/月订阅将支持 OpenSesame。

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

最新 $status$ 版本是 $version$ *$codename$* ([发行说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。

### Windows

Windows 安装包基于 64 位系统的 Python 3.13。安装程序和 `.zip` 包除安装方式外完全相同。大多数人选择下载安装程序包（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 免安装包 (.zip)
</a>

OpenSesame 在 Windows 11 下开发和测试。在其他版本的 Windows 上的使用体验可能有所不同。

### Mac OS

当第一次启动 OpenSesame 时，操作系统会因为该应用程序不是来自可信开发者而进行阻止。您可在“设置 > 隐私与安全性”中找到“仍然打开”选项。该选项会在应用被阻止后出现。

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 软件包 (.dmg)
</a>

OpenSesame 在 Mac OS X Sequoia 上进行开发和测试。在其他版本的 Mac OS X 上的使用体验可能有所不同。

### Linux / Ubuntu

将下面的命令复制并粘贴到终端中。这将下载并运行一个安装脚本。安装脚本需要 curl 和 virtualenv。在 Ubuntu 系统中可以用 `sudo apt install curl python3-venv` 安装它们。

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame 在 Ubuntu 24.04 上开发和测试。在其他 Linux 发行版及 Ubuntu 其他版本中的使用体验可能会有所不同。

## 高级安装选项

### PyPi（跨平台）

所有软件包均可通过 pip 安装。请注意，OpenSesame 在 PyPi 上叫做 `opensesame-core`。

OpenSesame 核心依赖项：

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy 作为（默认）psycho 后端。根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。如果遇到这种情况，请到支持论坛寻求帮助或使用预制包/安装程序。

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze 用于眼动仪追踪：

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment 用于 xpyriment 后端

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

安装好所有软件包后，只需运行：

```bash
opensesame
```

或 Sigmund 分析器（代码编辑器）：

```bash
sigmund-analyst
```

### Anaconda（跨平台）

首先，为 OpenSesame 创建一个新的 Python 环境（可选）

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

接下来，请按照上面的 PyPi 安装说明进行操作。不再提供专门的 Anaconda 软件包。

### 旧版本

旧版本可从 GitHub 的发布页面下载：

- <https://github.com/open-cogsci/OpenSesame/releases>

### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 获取。

## 提示

### 应该使用哪个版本的 Python？

OpenSesame 目前基于 Python 3.13 构建和测试。其他 Python >=3.10 的版本也能运行，但未经过广泛测试。不再支持 Python 2。最后一个包含 Python 2 包的版本是 3.3.12，仍可从 [发布存档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。

### 什么时候（不）该更新？

- 在开发和测试实验时请更新；建议始终使用最新版本的 OpenSesame。
- 在运行实验过程中请勿更新；也就是说，在收集数据时请勿更新。
- 请使用开发和测试所用的同一版本 OpenSesame 运行实验。

### 手动升级软件包

OpenSesame 是常规的 Python 环境，您可以在 Jupyter 控制台中运行 `pip install` 命令。

### 系统管理员提示

- 当 OpenSesame 发布新主版本（版本号以 0 结尾，例如 3.1.0）时，通常会很快跟进一到两个维护版本（如 3.1.1 和 3.1.2），以解决主要错误。因此，如果您在安装 OpenSesame 至不经常更新的系统时，最好等到第二或第三个维护版（如 3.0.2、3.1.3 等）发布后再安装，这样可以最大程度降低安装到包含重大错误版本的风险。
- Windows 安装程序允许您使用 `/S` 标志进行静默安装。