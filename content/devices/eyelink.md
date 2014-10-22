---
layout: osdoc
title: Eyelink
group: Devices
permalink: /eyelink/
---

The Eyelink series of eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for the Eyelink (called PyLink), which are used by PyGaze. The license of PyLink is incompatible with the license used by OpenSesame. For that reason, PyLink is not included in the default distribution of OpenSesame, and needs to be installed separately.

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## SR Research forum

You will need to download some software from the SR Research forum. This is a closed forum, but you can register free of charge.

- <https://www.sr-support.com/forums/>

## Windows

### Installing the EyeLink display software

The Eyelink display software provides the libraries that are required to communicate with the Eyelink PC. You can find it here:

- <https://www.sr-support.com/forums/showthread.php?t=6>

Add the following directory to the Path (this may have been added to the path automatically, but check to make sure):

	C:\Program Files\SR Research\EyeLink\libs

You can do this by opening "My Computer", clicking on "View system information", opening the "Advanced" tab, clicking on "Environment Variables" and appending `;C:\Program Files\SR Research\EyeLink\libs` to the Path variable (under System variables).

### Installing PyLink

PyLink is the Python library for EyeLink support. You can download Pylink from here:

- <https://www.sr-support.com/showthread.php?14-Pylink>

You should grab `pylink_win32.zip`. In this archive, you will find several folders, each corresponding to a specific Python version. Currently, OpenSesame uses Python 2.7, so you need to get `pylink27`. Copy this folder to the OpenSesame program folder, and rename it to `pylink`.

### Alternative: WinPython

If you have trouble getting PyLink to work in OpenSesame, or if you experience random crashes, you can use the WinPython-based package of OpenSesame. This package comes with EyeLink support out of the box. See:

- [/getting-opensesame/running-with-python-portable/](/getting-opensesame/running-with-python-portable/)

## Ubuntu

### Installing the EyeLink display software

There is a repository with the Eyelink display software available for Ubuntu Linux. To add this repository to your software sources, type the following in a terminal:

	sudo nano /etc/apt/sources.list

This will open the software sources in a simple text editor. At the bottom of the file, add the following lines for 32 bit systems:

	# Eyelink repository (32bit)
	deb http://download.sr-support.com /

For 64 bit, add the following lines:

	# Eyelink repository (64bit)
	deb http://download.sr-support.com/x64 /

Save the file (Control+O, Enter) and exit (Control+X). Now reload the software sources, and install the Eyelink display software (the version number might vary, at the time of writing it is 1.9):

	sudo apt-get update
	sudo apt-get install eyelink-display-software1.9

For more information, please visit:

- <https://www.sr-support.com/showthread.php?16-Linux-Display-Software-Package>

### Installing PyLink

Download the correct PyLink for your distribution from here (make sure that you have the correct Python version, usually 2.7, and chipset, x64 for 64 bit and x32 for 32 bit):

- <https://www.sr-support.com/forums/showthread.php?t=14>

Extract it to a location of your choice and rename the `pylink27` folder to `pylink`.

## PyGaze

After you have install the EyeLink display software and PyLink per the instructions above, you can use the EyeLink with PyGaze! See:

- [/devices/pygaze](/devices/pygaze)

## What happened to the EyeLink plug-ins?

The OpenSesame EyeLink plug-ins have been deprecated in favor of PyGaze. However, even though the EyeLink plug-ins are no longer maintained, they still work. For more information, visit the older version of this documentation page:

- <http://osdoc.cogsci.nl/2.8.3/devices/eyelink>
