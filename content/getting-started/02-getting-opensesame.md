---
layout: osdoc
title: Getting OpenSesame
group: Getting started
permalink: /getting-opensesame/
level: 1
sortkey: 003.002
---

The latest stable version of OpenSesame is 0.27.1 *Frisky Freud* ([release notes][]), the first maintenance release in the 0.27 series. If you are upgrading from 0.26, please read the [0.27 release notes][]. Older versions can be found [here][archive].

Installation instructions and more download options can be found below the download buttons.

{% include downloads %}

Windows XP / Vista / 7 {#windows}
----------------------

There are a number of ways to run OpenSesame under Windows:

- Use the automated installer (see link above). After installation, you can run OpenSesame from the start menu.
- Download the Windows portable .zip file (see link above) and extract it to a location of your choice.
- Download the package based on Python portable, which comes with a slightly different set of modules. For more information, see [this article][python-portable].

Ubuntu/ Debian/ Linux Mint {#ubuntu}
--------------------------

The recommended way to install OpenSesame under Ubuntu/ Debian/ Linux Mint is through the [NeuroDebian][] repository (see their instructions on how to add NeuroDebian to your list of repositories). After you have added NeuroDebian to your software sources, you can install it using your package manager (Synaptic/ Add remove programs/ Ubuntu software center) or by typing the following lines in a terminal:

	sudo apt-get update
	sudo apt-get install opensesame

If you encounter problems or if your distribution is not supported by NeuroDebian, you can also install OpenSesame via the [ppa:smathot/cogscinl][ppa-cogscinl] Ubuntu repository. If you experience missing icons, please install the package `gnome-icon-theme-full`.

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install opensesame

After you have installed OpenSesame, you can start OpenSesame from the menu or by opening a terminal and running:

	opensesame

Mac OS {#macos}
------

Support for Mac OS is experimental. Instructions for running OpenSesame from source on Mac OS can be found [here][macos-running-from-source].
The newest version of OpenSesame (0.27.1) comes in two *flavors*. One runs on 64-bit Python (from python.org) and of all its underlying packages were obtained by using the official distributables that are available from the developers' websites. Because psychopy is not able to run in a 64-bit Python environment (yet), this backend is not available in this version. The other version is completely built from the ground up with macports and is compiled in 32-bit. This version does contain the psychopy backend. Concerning their usage, there are no real noticable differences between these versions (except for the lack of the psychopy backend in one) and experiments created in one version should work perfectly in the other, so the decision of which one to use is completely up to you (upon initial testing, the 64-bit version seemed a bit more stable, but these tests were not really in-depth)

Both versions have been built on *Mountain Lion* and, after initial tests on our systems, sadly did not seem to be backward compatible with older OS X versions. If they do work for you on pre-Mountain Lion macs, please let us know on [the forum](http://forum.cogsci.nl).

- [opensesame 0.27.1 64bit][macos-package-0.27.1-64bit]
- [opensesame 0.27.1 32bit][macos-package-0.27.1-32bit]

An older version of OpenSesame which should run on all OS X versions (>10.6) can be found here:

- [opensesame_0.26-macos-2.zip][macos-package-0.26]

##### We are looking for someone to improve and maintain the Mac OS packages for OpenSesame!

Other platforms {#other}
---------------

If there are no packages provided for your platform, you will need to run OpenSesame from source, as [per these instructions][running-from-source].

[archive]: http://files.cogsci.nl/software/opensesame/
[macos-package-0.26]: http://files.cogsci.nl/software/opensesame/opensesame_0.26-macos-2.zip
[macos-package-0.27.1-64bit]: http://www.cogsci.nl/dschreij/opensesame-mac/Opensesame-0.27.1-wo_psychopy-macos-x86_64-1.dmg
[macos-package-0.27.1-32bit]: http://www.cogsci.nl/dschreij/opensesame-mac/Opensesame-0.27.1-macos-i386-1.dmg
[macos-running-from-source]: /getting-started/running-from-source#macos
[ppa-cogscinl]: https://launchpad.net/~smathot/+archive/cogscinl
[running-from-source]: /getting-started/running-from-source
[neurodebian]: http://neuro.debian.net/
[python-portable]: /getting-started/running-with-python-portable/
[0.27 release notes]: /notes/0.27
[release notes]: /notes/0.27.1
