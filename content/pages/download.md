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

<a role="button" class="btn btn-success btn-align-left" href="https://www.buymeacoffee.com/cogsci">
<span class="glyphicon glyphicon-heart" aria-hidden="true"></span>
Help us stay focused and buy us a coffee!
</a>

Coffee keeps us awake so that we can develop free software and answer your questions on the support forum!

Click <a id="click-here">here</a> if your download doesn't start.
</div>


## Overview

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## All download options

The latest $status$ version is $version$ *$codename$*, released on $release-date$ ([release notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

The Windows package is based on Python 3.11 for 64 bit systems. The installer and `.zip` packages are identical, except for the installation. Most people download the installer package (green button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows no installation required (.zip)
</a>


### Mac OS

There are currently no prerelease packages of OpenSesame 4.0 for Mac OS. Please use conda or pip.
{: .page-notification}

[This article](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) on the Mac OS support site explains how to override the security settings of Mac OS that will by default prevent OpenSesame from launching.

The package below is built for Intel processors but also runs on ARM (M1) processors.

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 for Intel x64</b> Mac OS package (.dmg)
</a>

To install OpenSesame with [Homebrew](https://brew.sh/), run the following command in a terminal:

```bash
brew install --cask opensesame
```


### Ubuntu

Packages are developed and tested on Ubuntu 22.04 Jammy Jellyfish. Packages are only available for 22.04 and 22.10.

If you have OpenSesame 3.X installed, first deinstall all packages . This is required to avoid package conflicts due to slight renaming of some packages in OpenSesame 4.0.

```bash
# If necessary: uninstall OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Next, to add the required repositories to your software sources and install OpenSesame (and Rapunzel), run the following commands in a terminal:

```bash
# Add repository for stable packages
sudo add-apt-repository ppa:smathot/cogscinl
# Add repository for development packages
sudo add-apt-repository ppa:smathot/milgram
# Install OpenSesame 4.X packages plus useful extensions
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Some commonly used packages are not available through the PPA. You can install them through `pip`:

```bash
# Install optional packages that are only available through pip
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy is best installed through pip, because the Ubuntu package is currently broken. 

```bash
# Install psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (crossplatform)

All packages can be pip-installed. Note that OpenSesame is called `opensesame-core` on PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Once you have installed all packages, you can simply run OpenSesame by (after having activated the correct environment) running:

```bash
opensesame
```

Or for the Rapunzel code editor:

```bash
rapunzel
```


### Anaconda (cross-platform)

First, create a new Python environment for OpenSesame (optional):

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Next, add the relevant channels (`cogsci`) and (`conda-forge`) and install all relevant packages. Make sure that `pyqode.core` and `pyqode.python` are >= 3.2 from the `cogsci` channel, and not the older versions from the `conda-forge` channel.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Some packages are not available through conda. You can use `pip install` for these. (PsychoPy is known to fail to install on some systems, which is why it is installed separately below.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Once you have installed all packages, you can simply run OpenSesame by (after having activated the correct environment) running:

```bash
opensesame
```

Or for the Rapunzel code editor:

```bash
rapunzel
```


### Older versions

Older versions can be downloaded from GitHub releases:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Source code

The source code of OpenSesame is available on [GitHub](https://github.com/open-cogsci/OpenSesame).


## Tips


### Which version of Python to use?

OpenSesame is currently built and tested with Python 3.11 Others versions of Python >=3.7 work but are not extensively tested. Python 2 is no longer supported. The last release that included a Python 2 package was 3.3.12, which can still be downloaded from the [release archive](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### When (not) to update?

- Update while developing and testing your experiment; it is always best to use the latest version of OpenSesame.
- Do not update while running an experiment; that is, do not update while you are collecting data.
- Run an experiment with the same version of OpenSesame that you used for developing and testing.


### Manually upgrading packages

OpenSesame is a regular Python environment, and you can upgrade packages with `pip` or `conda` as described here:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Tips for system administrators

- When a new major version of OpenSesame is released (with a version ending in 0, e.g. 3.1.0), it is generally followed quickly by one or two maintenance releases (e.g. 3.1.1 and 3.1.2) that address major bugs. Therefore, if you are installing OpenSesame on systems that you do not update often, it is best to wait until the second or third maintenance release (e.g. 3.0.2, 3.1.3, etc.). That way you minimize the risk of rolling out a version of OpenSesame that contains major bugs.
- The Windows installer allows you to silently install OpenSesame using the `/S` flag.
