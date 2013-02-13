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

[opensesame_0.26-macos-2.zip][macos-package]

##### We are looking for someone to improve and maintain the Mac OS packages for OpenSesame!

Other platforms {#other}
---------------

If there are no packages provided for your platform, you will need to run OpenSesame from source, as [per these instructions][running-from-source].

[archive]: http://files.cogsci.nl/software/opensesame/
[macos-package]: http://files.cogsci.nl/software/opensesame/opensesame_0.26-macos-2.zip
[macos-running-from-source]: /getting-started/running-from-source#macos
[ppa-cogscinl]: https://launchpad.net/~smathot/+archive/cogscinl
[running-from-source]: /getting-started/running-from-source
[neurodebian]: http://neuro.debian.net/
[python-portable]: /getting-started/running-with-python-portable/
[0.27 release notes]: /notes/0.27
[release notes]: /notes/0.27.1