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

The latest $status$ version is $version$ *$codename$*, released on $release-date$ ([release notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).

### Windows

Installers are not yet available. You can use the `.zip` files instead.
{: .page-notification}

The recommended download is based on Python 3.7. The installer and `.zip` packages are identical, except for the installation.

<a role="button" class="btn btn-default btn-align-left" href="$url-windows-exe-py3$">
	Windows installer (.exe)
	<br /><span class='cogsci-btn-info'>
		Based on Python 3.7 for 64 bit systems
	</span>
</a>

<a role="button" class="btn btn-default btn-align-left" href="$url-windows-zip-py3$">
	Windows no installation required (.zip)
	<br /><span class='cogsci-btn-info'>
		Unzip and run! Based on Python 3.7 for 64 bit systems
	</span>
</a>

Some Python packages, notably PyGaze, are not compatible with Python 3. If you want to use those, please download the Python 2 package below.

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

### Mac OS

Mac OS packages are not yet available. For now, you can install OpenSesame 3.3 on Mac OS through Anaconda (see below).
{: .page-notification}

<a role="button" class="btn btn-default btn-align-left" href="$url-osx-dmg-py2$">
	Mac OS package (.dmg)
	<br /><span class='cogsci-btn-info'>
		Based on Python X.X for 64 bit systems
	</span>
</a>


### Ubuntu

OpenSesame 3.3 is available through the [Rapunzel PPA](https://launchpad.net/~smathot/+archive/rapunzel). To add this repository to your software sources and install OpenSesame, run the following commands in a terminal:

~~~ .bash
sudo add-apt-repository ppa:smathot/rapunzel
sudo apt-get update
sudo apt-get install python3-opensesame opensesame-extension-osf opensesame-extension-osweb opensesame-plugin-psychopy
# To install also rapunzel, the OpenSesame-based code editor
sudo apt-get install python3-rapunzel
~~~

Some commonly used packages are not available through the PPA. You can install them through `pip`:

~~~ .bash
pip install psychopy expyriment
~~~


### Arch Linux

Arch Linux packages are available in the [Arch Linux user repository](https://aur.archlinux.org/packages/opensesame/).


### Pip / PyPi (cross-playform)

To install OpenSesame from PyPi (Python package index), type:

~~~ .bash
pip install python-opensesame
~~~


### Anaconda (cross-platform)

First, create a new Python environment for OpenSesame (optional):

```bash
conda create -n opensesame-py3 python=3.7.3  # For Python 2: ptyhon=2.7.15
conda activate opensesame-py3
```

Next, add the relevant channels (`cogsci`) and (`conda-forge`) and install all relevant packages:

```bash
conda config --add channels cogsci --add channels conda-forge
conda install python-opensesame opensesame-extension-osf opensesame-extension-osweb opensesame-plugin-psychopy psychopy rapunzel
```

[PyGaze](%url:pygaze%), a Python eye-tracking library, is only available on Python 2.

```bash
conda install python-pygaze
```


### Older versions

Older versions can be downloaded from GitHub releases:

- <https://github.com/smathot/OpenSesame/releases>


### Source code

The source code of OpenSesame is available on [GitHub](https://github.com/smathot/OpenSesame).


## Tips


### Which version of Python to use?

OpenSesame is currently built with Python 3.7.3 (standard package) and Python 2.7.15.

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
