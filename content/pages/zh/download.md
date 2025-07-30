title: 下载
hash: b38f65619e4c2d6695dd956ab06de9e176c145e37d2819dbaac4a0bc70eb23a5
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

对于 OpenSesame 问题，比 ChatGPT 更好。您每月 €9 的订阅支持 OpenSesame。

如果您的下载没有自动开始，请点击<a id="click-here">这里</a>。
</div>


## 概览

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 标准安装选项

最新的 $status$ 版本为 $version$ *$codename$* ([发行说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。


### Windows

Windows 包基于 Python 3.13，适用于 64 位系统。安装程序和 `.zip` 包功能相同，仅安装方式不同。大多数用户会下载安装程序包（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装程序 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 免安装版 (.zip)
</a>

OpenSesame 在 Windows 11 上开发和测试。在其他版本的 Windows 上效果可能有所不同。


### Mac OS

Mac OS 包尚未适配 OpenSesame 4.1。下面的下载链接仍指向 4.0。
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 软件包 (.dmg)
</a>


### Linux / Ubuntu

将下方命令复制粘贴到终端。这将下载并运行安装脚本。安装脚本需要 curl 和 virtualenv。在 Ubuntu 上可以通过 `sudo apt install curl python3-venv` 安装它们。

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame 在 Ubuntu 24.04 上开发和测试。在其他 Linux 发行版及其他版本的 Ubuntu 上效果可能有所不同。


## 高级安装选项


### PyPi（跨平台）

所有软件包均可通过 pip 安装。注意 OpenSesame 在 PyPi 上名为 `opensesame-core`。

OpenSesame 核心依赖：

```bash
# OpenSesame 核心依赖
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy 用于（默认的）psycho 后端。根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。若有问题，可以到支持论坛寻求帮助，或使用现成的安装包。

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

安装所有软件包后，您可以通过以下命令直接运行 OpenSesame：

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


### 旧版本

旧版本可从 GitHub releases 下载：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 获取。

## 提示

### 应该使用哪个版本的 Python？

OpenSesame 目前基于 Python 3.13 构建和测试。其他 >=3.10 的 Python 版本可以工作，但没有经过广泛测试。Python 2 已不再支持。最后一个包含 Python 2 安装包的版本是 3.3.12，仍可从 [release archive](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。

### 何时（不）应更新？

- 在开发和测试实验时请更新；始终使用 OpenSesame 的最新版本是最佳做法。
- 在运行实验过程中不要更新；也就是说，在收集数据时请勿更新。
- 运行实验时应使用你开发与测试时用的同一版本的 OpenSesame。

### 手动升级软件包

OpenSesame 是一个常规的 Python 环境，你可以在 Jupyter 控制台运行 `pip install` 命令。

### 系统管理员提示

- 当 OpenSesame 发布新主版本（版本号以 0 结尾，例如 3.1.0）时，通常会很快发布一到两个维护版本（如 3.1.1 和 3.1.2）以修复主要 bug。因此，如果你是在不经常更新的软件环境中安装 OpenSesame，最好等到第二或第三个维护版本（例如 3.0.2、3.1.3 等）再安装。这样可以最大程度降低部署含有严重 bug 的 OpenSesame 版本的风险。
- Windows 安装程序支持使用 `/S` 标志进行静默安装。