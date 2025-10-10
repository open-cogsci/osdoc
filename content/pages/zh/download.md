title: 下载
hash: 0057d1f73dae2a2590e1f0e03dfe7d984bdf6d67622188a9eb35e2cb08646b28
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

您的 OpenSesame AI 协作助手。每月 9 欧元的订阅支持 OpenSesame 项目。

如果下载没有开始，请点击 <a id="click-here">此处</a>。
</div>


## 概述

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## 标准安装选项

最新的 $status$ 版本是 $version$ *$codename$* ([发布说明](http://osdoc.cogsci.nl/$branch$/notes/$notes$))。


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>标准</b> Windows 安装包 (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>标准</b> Windows 免安装包 (.zip)
</a>

大多数用户下载 `.exe` 安装包。如果您没有管理员权限，或者需要同时运行多个版本的 OpenSesame，请下载 `.zip` 包。

基于适用于 64 位系统的 Python 3.13。在 Windows 11 上进行过测试。

某些外部设备，如 [EyeLink](%url:eyelink%) 和 [Tobii](%url:tobii%) 眼动仪，需要不同版本的 Python。请访问相关设备的文档页面获取更多信息。


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS 安装包 (.dmg)
</a>

首次启动 OpenSesame 时，操作系统会因应用非受信开发者而阻止运行。您将在“设置 > 隐私与安全性”下找到“仍要打开”选项。该选项会在应用被阻止后出现。

基于适用于 64 位 Intel 系统的 Python 3.13。在 Mac OS X Sequoia 上经过测试。

某些外部设备，如 [EyeLink](%url:eyelink%) 和 [Tobii](%url:tobii%) 眼动仪，需要不同版本的 Python。请访问相关设备的文档页面获取更多信息。


### Linux / Ubuntu

将以下命令复制粘贴到终端。这将下载并运行安装脚本。

```bash
# 下面这些软件包需要在 Ubuntu 24.04 上安装。
# 其他 Linux 发行版需要安装对应的软件包。
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# 下载并运行 OpenSesame 安装脚本。
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

在 Ubuntu 24.04（Python 3.12）上测试通过。


## 高级安装选项


### PyPi（跨平台）

所有软件包都支持 pip 安装。请注意，OpenSesame 在 PyPi 上叫做 `opensesame-core`。

OpenSesame 核心依赖项：

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

用于（默认）psycho 后端的 PsychoPy。根据您的操作系统和 Python 版本，PsychoPy 可能无法正确安装。如遇此问题，请在支持论坛寻求帮助，或使用官方预制安装包。

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

用于眼动仪的 PyGaze：

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

用于 xpyriment 后端的 Expyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

安装所有软件包后，您只需运行以下命令即可启动 OpenSesame：

```bash
opensesame
```

或者对于 Sigmund Analyst（代码编辑器）：

```bash
sigmund-analyst
```


### Anaconda（跨平台）

首先，为 OpenSesame 创建一个新的 Python 环境（可选）

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

接下来，按照上面的 PyPi 安装说明操作。不再提供专门的 Anaconda 安装包。


### 旧版本 OpenSesame 及其它 Python 版本

旧版本的 OpenSesame 以及基于不同 Python 版本（3.10、3.11 和 3.12）构建的软件包都可以在 GitHub releases 页面获取：

- <https://github.com/open-cogsci/OpenSesame/releases>



### 源代码

OpenSesame 的源代码可在 [GitHub](https://github.com/open-cogsci/OpenSesame) 获取。


## 提示


### 应该使用哪个版本的 Python？

OpenSesame 当前基于并经测试的 Python 版本是 3.13。其它 >=3.10 的 Python 版本也可以使用，但没有经过充分测试。Python 2 不再支持。最后一个包含 Python 2 软件包的版本为 3.3.12，可以在 [release archive](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) 下载。


### 什么时候（不）应该更新？

- 在开发和测试实验时请更新；使用 OpenSesame 的最新版本永远是最佳选择。
- 在运行实验时请勿更新，也就是说，在收集数据时不要更新。
- 运行实验时请使用与开发和测试时相同版本的 OpenSesame。


### 手动升级包

OpenSesame 是一个常规的 Python 环境，你可以在 Jupyter 控制台中运行 `pip install` 命令。


### 系统管理员提示

- 当 OpenSesame 发布新的主版本（版本号以 0 结尾，例如 3.1.0）时，通常很快会跟进一两个维护版本（例如 3.1.1 和 3.1.2），这些版本主要修复重大漏洞。因此，如果你需要在不经常更新的系统上安装 OpenSesame，建议等待第二或第三个维护版本（例如 3.0.2、3.1.3 等）再进行安装。这样可以最小化部署包含重大漏洞版本的风险。
- Windows 安装程序支持使用 `/S` 参数静默安装 OpenSesame。