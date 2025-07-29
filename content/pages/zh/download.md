title: 下载
hash: 70d7d3aa0db9c3d49b6e9a94cd6d92a1dd50ec0dc94bc9bfc9e076703ab3dd3a
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

对 OpenSesame 问题来说，比 ChatGPT 更好。您的每月€9订阅将支持 OpenSesame。

如果您的下载没有开始，请点击<a id="click-here">这里</a>。
</div>


## 概览

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 所有下载选项

最新的 $status$ 版本为 $version$ *$codename$* ([发布说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。


### Windows

Windows 安装包基于 64 位系统的 Python 3.13。安装版和 `.zip` 压缩包除了安装方式不同以外功能一致。大多数用户建议下载安装版（绿色按钮）。

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b>Windows 安装包 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b>Windows 免安装版 (.zip)
</a>


### Mac OS

Mac OS 的 OpenSesame 4.1 安装包尚未发布。如下方下载链接仍指向 4.0 版本。
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 安装包 (.dmg)
</a>


### Linux / Ubuntu

复制并粘贴下面的命令到终端中。这将下载并运行一个安装脚本。安装脚本需要 virtualenv，在 Ubuntu 上可以用 `sudo apt install python3-venv` 安装。

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame 在 Ubuntu 24.04 上进行开发和测试，在其它 Linux 发行版和不同 Ubuntu 版本上的兼容性可能有所不同。


### PyPi（跨平台）

所有安装包都可以通过 pip 安装。请注意 OpenSesame 在 PyPi 上叫做 `opensesame-core`。

OpenSesame 核心依赖：

```bash
# OpenSesame 核心依赖
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

用于（默认）psycho 后端的 PsychoPy，注意根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。如果遇到问题，请到支持论坛求助或使用预制安装包。

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

安装好所有包后，您可以通过以下命令直接运行 OpenSesame：

```bash
opensesame
```

对于 Sigmund Analyst（代码编辑器），请执行：

```bash
sigmund-analyst
```


### Anaconda（跨平台）

首先为 OpenSesame 创建新的 Python 环境（可选）

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

接下来，按照上面的 PyPi 安装说明操作。不再单独提供 Anaconda 安装包。


### 旧版本

旧版本可在 GitHub Releases 页面下载：

- <https://github.com/open-cogsci/OpenSesame/releases>


### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 获取。


## 提示


### 应该使用哪个版本的 Python？

OpenSesame 目前是基于并在 Python 3.13 进行构建和测试的。其他 Python >=3.10 的版本也可用，但未经过充分测试。不再支持 Python 2。最后一个包含 Python 2 安装包的版本是 3.3.12，仍可从[版本归档](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12)下载。


### 何时（不）需要更新？

- 在开发和测试实验时进行更新；始终建议使用 OpenSesame 的最新版本。
- 在运行实验时请勿更新；也就是说，在收集数据时不要更新。
- 使用与开发和测试时相同版本的 OpenSesame 来运行实验。


### 手动升级软件包

OpenSesame 是一个常规的 Python 环境，你可以在 Jupyter 控制台中运行 `pip install` 命令。


### 给系统管理员的提示

- 当 OpenSesame 发布新主版本（版本号末尾为 0，如 3.1.0）时，通常很快会有一到两个维护版本（如 3.1.1 和 3.1.2）用于修复主要漏洞。因此，如果你要在不经常更新的系统上安装 OpenSesame，建议等到第二或第三个维护版本发布后再安装（例如 3.0.2、3.1.3 等）。这样可以最大限度地减少部署含有严重漏洞版本的风险。
- Windows 安装程序允许你使用 `/S` 参数静默安装 OpenSesame。