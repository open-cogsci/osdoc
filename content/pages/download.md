title: Download

%-- include: "include/recommended-download.md" --%

%-- include: include/ads-inpage.md --%

## Overview

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%

## All download options

### Windows

<a role="button" class="btn btn-default btn-align-left" href="$url-windows-exe-py2$">
	Windows installer (.exe)
	<br /><span class='cogsci-btn-info'>
		Based on Python 2.7 for 32 and 64 bit systems
	</span>
</a>

<a role="button" class="btn btn-default btn-align-left" href="$url-windows-zip-py2$">
	Windows no installation required (.zip)
	<br /><span class='cogsci-btn-info'>
		Unzip and run! Based on Python 2.7 for 32 and 64 bit systems
	</span>
</a>

Support for Python 3.5 is experimental:

<a role="button" class="btn btn-default btn-align-left" href="$url-windows-exe-py3$">
	Windows installer (.exe)
	<br /><span class='cogsci-btn-info'>
		Based on Python 3.5 for 64 bit systems
	</span>
</a>

<a role="button" class="btn btn-default btn-align-left" href="$url-windows-zip-py3$">
	Windows no installation required (.zip)
	<br /><span class='cogsci-btn-info'>
		Unzip and run! Based on Python 3.5 for 64 bit systems
	</span>
</a>

### Mac OS

The Mac OS package doesn't work smoothly on some systems. We are aware of this, and are working to improve it. Please let us know of any issues on the forum!

<a role="button" class="btn btn-default btn-align-left" href="$url-osx-dmg-py2$">
	Mac OS package (.dmg)
	<br /><span class='cogsci-btn-info'>
		Based on Python 2.7 for 64 bit systems
	</span>
</a>

### Android

For more information about the OpenSesame runtime for Android, see:

- %link:android%

### Ubuntu

OpenSesame is available through the [Cogsci.nl PPA](https://launchpad.net/~smathot/+archive/cogscinl). To add this repository to your software sources and install OpenSesame, run the following commands in a terminal:

~~~ .bash
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install opensesame
~~~

If you experience missing icons, install `gnome-icon-theme-full`.

~~~ .bash
sudo apt-get install gnome-icon-theme-full
~~~

### Arch Linux

Arch Linux packages are available in the [Arch Linux user repository](https://aur.archlinux.org/packages/opensesame/).

### All platforms (pip)

To install OpenSesame from PyPi (Python package index), type:

~~~ .bash
pip install python-opensesame
~~~

### Anaconda

You can install OpenSesame in Anaconda through the CogSci channel:

~~~ .bash
conda install -c cogsci python-opensesame
~~~

### Older versions

Older versions can be downloaded from GitHub releases:

- <https://github.com/smathot/OpenSesame/releases>

### Source code

The source code of OpenSesame is available on [GitHub](https://github.com/smathot/OpenSesame).


## Tips

### When (not) to update?

- Update while developing and testing your experiment; it is always best to use the latest version of OpenSesame.
- Do not update while running an experiment; that is, do not update while you are collecting data.
- Run an experiment with the same version of OpenSesame that you used for developing and testing.


### Manually upgrading packages

- OpenSesame is a regular Python environment, and you can upgrade packages with `pip` as described here:
	- %link:environment%


### Tips for system administrators

- When a new major version of OpenSesame is released (with a version ending in 0, e.g. 3.1.0), it is generally followed quickly by one or two maintenance releases (e.g. 3.1.1 and 3.1.2) that address major bugs. Therefore, if you are installing OpenSesame on systems that you do not update often, it is best to wait until the second or third maintenance release (e.g. 3.0.2, 3.1.3, etc.). That way you minimize the risk of rolling out a version of OpenSesame that contains major bugs.
- The Windows installer allows you to silently install OpenSesame using the `/S` flag.
