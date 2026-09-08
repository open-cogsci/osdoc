title: Download

<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('download-started').style.display = 'block'
	document.getElementById('download-started').scrollIntoView()
}
</script>

<div class="info-box" id="download-started" markdown="1" style="display:none;">

<h3>Your download should start shortly!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Subscribe to SigmundAI.eu
</a>

Your AI-copilot for OpenSesame. Your €9/month subscription supports OpenSesame.

Click <a id="click-here">here</a> if your download doesn't start.
</div>


## Overview

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standard installation options

The latest $status$ version is $version$ *$codename$* ([release notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows no installation required (.zip)
</a>

Most people download the `.exe` installer package. If you do not have admin privileges, or if you need to run multiple versions of OpenSesame side by side, download the `.zip` package instead.

Based on Python 3.13 for 64 bit systems. Tested on Windows 11.

Some external devices, such as [Tobii](%url:tobii%) eye trackers, require a different version of Python. Visit the respective documentation pages for more information.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS package (.dmg)
</a>

When you start OpenSesame for the first time, it is blocked by the operating system because the app is not from a trusted developer. You will find an 'Open anyway' option under Settings > Privacy & Security. This option appears after the app is blocked.

Based on Python 3.13 for 64 bit intel systems. Tested on Mac OS X Sequoia.

Some external devices, such as [Tobii](%url:tobii%) eye trackers, require a different version of Python. Visit the respective documentation pages for more information.


### Linux / Ubuntu

Copy-paste the lines below into a terminal. This will download and run an installation script.

```bash
# These packages need to be installed on Ubuntu 24.04.
# Equivalent packages need to be installed on other
# Linux distributions.
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# Download and run the OpenSesame installation script.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/nightingale/linux-installer.sh) --install
```

Tested on Ubuntu 24.04 (Python 3.12).


## Advanced installation options


### PyPi (crossplatform)

All packages can be pip-installed. Note that OpenSesame is called `opensesame-core` on PyPi.

OpenSesame core dependencies:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy for the (default) psycho backend. Depending on your operating system and version of Python, PsychoPy may not install properly. If this happens, seek help on the support forum or use one of the premade packages/ installers.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze for eye tracking:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment for the xpyriment backend

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Once you have installed all packages, you can simply run OpenSesame by running:

```bash
opensesame
```

Or for Sigmund Analyst (code editor):

```bash
sigmund-analyst
```


### Anaconda (cross-platform)

First, create a new Python environment for OpenSesame (optional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Next, follow the PyPi installation instructions above. Dedicated Anaconda packages are no longer provided.


### Older versions of OpenSesame and other Python versions

Older versions of OpenSesame as well as packages built with different versions of Python (3.10, 3.11, and 3.12) are available on GitHub releases:

- <https://github.com/open-cogsci/OpenSesame/releases>



### Source code

The source code of OpenSesame is available on [GitHub](https://github.com/open-cogsci/OpenSesame).


## Tips


### Which version of Python to use?

OpenSesame is currently built and tested with Python 3.13. Others versions of Python >=3.10 work but are not extensively tested. Python 2 is no longer supported. The last release that included a Python 2 package was 3.3.12, which can still be downloaded from the [release archive](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### When (not) to update?

- Update while developing and testing your experiment; it is always best to use the latest version of OpenSesame.
- Do not update while running an experiment; that is, do not update while you are collecting data.
- Run an experiment with the same version of OpenSesame that you used for developing and testing.


### Manually upgrading packages

OpenSesame is a regular Python environment, and you can run `pip install` commands in the Jupyter console.


### Tips for system administrators

- When a new major version of OpenSesame is released (with a version ending in 0, e.g. 3.1.0), it is generally followed quickly by one or two maintenance releases (e.g. 3.1.1 and 3.1.2) that address major bugs. Therefore, if you are installing OpenSesame on systems that you do not update often, it is best to wait until the second or third maintenance release (e.g. 3.0.2, 3.1.3, etc.). That way you minimize the risk of rolling out a version of OpenSesame that contains major bugs.
- The Windows installer allows you to silently install OpenSesame using the `/S` flag.
