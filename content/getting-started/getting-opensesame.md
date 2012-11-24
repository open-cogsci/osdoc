---
layout: osdoc
title: Getting OpenSesame
group: Getting started
permalink: /getting-opensesame/
level: 1
sortkey: 003.002
---

The latest stable version is 0.26 "Earnest Einstein". The development version is 0.27 "Frisky Freud". Older versions can be found [here][archive].

Installation instructions and more download options can be found below the download buttons.

{% include downloads %}

Windows XP / Vista / 7
----------------------

The easiest way to install OpenSesame under Windows is using the automated installer (see link above). After installation, you can run OpenSesame from the start menu.

Alternatively, you can download the Windows portable .zip file (see link above) and extract it to a location of your choice. After extraction, you can start OpenSesame by running.

	opensesame.exe

Ubuntu/ Debian/ Linux Mint
--------------------------

The recommended way to install OpenSesame under Ubuntu/ Debian/ Linux Mint is through the NeuroDebian repository (see their instructions on how to add NeuroDebian to your list of repositories). After you have added NeuroDebian to your software sources, you can install it using your package manager (Synaptic/ Add remove programs/ Ubuntu software center) or by typing the following lines in a terminal:

	sudo apt-get update
	sudo apt-get install opensesame
	
If you encounter problems or if your distribution is not supported by NeuroDebian, you can also install OpenSesame via the [ppa:smathot/cogscinl][ppa_cogscinl] Ubuntu repository. If you experience missing icons, please install the package gnome-icon-theme-full or see this post.

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install opensesame

After you have installed OpenSesame, you can start OpenSesame from the menu (Accessories => OpenSesame) or by opening a terminal and running:

	opensesame

Mac OS
------

Support for Mac OS is experimental. Instructions for running OpenSesame from source on Mac OS can be found here.

Are you a Mac OS user and want to help out? We are looking for someone to maintain Mac OS packages for OpenSesame!

[opensesame_0.26-macos-2.zip (latest)](http://files.cogsci.nl/software/opensesame/opensesame_0.26-macos-2.zip)

[opensesame_0.25-macos-3.zip](http://files.cogsci.nl/software/opensesame/opensesame_0.25-macos-3.zip)

Other platforms
---------------

If there are no packages provided for your platform, you will need to run OpenSesame from source, as per these instructions.

[ppa_cogscinl]: https://launchpad.net/~smathot/+archive/cogscinl