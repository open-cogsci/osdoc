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
Buy us a coffee!
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

The standard download is based on Python 3.7 for 64 bit systems. The installer and `.zip` packages are identical, except for the installation. Most people download the installer package (green button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows no installation required (.zip)
</a>

The Megapack is identical to the standard Python 3.7 download above, except that it comes with a large number of libraries for scientific computing pre-installed. The Megapack also includes advanced support for JavaScript (code completion, syntax checking, etc.).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-exe-py3-megapack$')">
	<b>Megapack</b> Windows installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3-megapack$')">
	<b>Megapack</b> Windows no installation required (.zip)
</a>

Some Python packages are not compatible with Python 3. If you want to use those, please download the Python 2.7 (64 bit) package below. Note: As of January 1, 2020, Python 2.7 is no longer maintained.

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-exe-py2$')">
	<b>Python 2</b> Windows installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py2$')">
	<b>Python 2</b> Windows no installation required (.zip)
</a>


### Mac OS

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

OpenSesame 3.3 is available through the [Cogscinl PPA](https://launchpad.net/~smathot/+archive/cogscinl). Packages are developed and tested on Ubuntu 20.04 Focal Fossa. To add this repository to your software sources and install OpenSesame, run the following commands in a terminal:

```bash
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt update
sudo apt install python3-opensesame
```

Some commonly used packages are not available through the PPA. You can install them through `pip`:

```bash
pip install psychopy expyriment pyspellchecker fastnumbers js2py
```


### Anaconda (cross-platform)

First, create a new Python environment for OpenSesame (optional):

```bash
conda create -n opensesame-py3 python=3.7  # For Python 2: python=2.7.15
conda activate opensesame-py3
```

Next, add the relevant channels (`cogsci`) and (`conda-forge`) and install all relevant packages. Make sure that `pyqode.core` and `pyqode.python` are >= 3.2 from the `cogsci` channel, and not the older versions from the `conda-forge` channel.

```bash
conda config --add channels cogsci --add channels conda-forge
conda install python-opensesame opensesame-extension-osweb opensesame-plugin-psychopy psychopy rapunzel python-pygaze
```

Some packages are not available through conda. You can use `pip install` for these.

```bash
pip install soundfile pygame yolk3k opensesame-extension-osf python-qtpip http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
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

- <https://github.com/smathot/OpenSesame/releases>


### Source code

The source code of OpenSesame is available on [GitHub](https://github.com/smathot/OpenSesame).


## Tips


### Which version of Python to use?

OpenSesame is currently built with Python 3.7.6 (standard package) and Python 2.7.15.

### When (not) to update?

- Update while developing and testing your experiment; it is always best to use the latest version of OpenSesame.
- Do not update while running an experiment; that is, do not update while you are collecting data.
- Run an experiment with the same version of OpenSesame that you used for developing and testing.


### Manually upgrading packages

- OpenSesame is a regular Python environment, and you can upgrade packages with `pip` or `conda` as described here:
	- <https://rapunzel.cogsci.nl/manual/environment/>


### Tips for system administrators

- When a new major version of OpenSesame is released (with a version ending in 0, e.g. 3.1.0), it is generally followed quickly by one or two maintenance releases (e.g. 3.1.1 and 3.1.2) that address major bugs. Therefore, if you are installing OpenSesame on systems that you do not update often, it is best to wait until the second or third maintenance release (e.g. 3.0.2, 3.1.3, etc.). That way you minimize the risk of rolling out a version of OpenSesame that contains major bugs.
- The Windows installer allows you to silently install OpenSesame using the `/S` flag.
