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

If you extract the .zip, and then run the .exe installer, the EyeLink display will be installed in one of the following folders (depending on your version of Windows:

	C:\Program Files\SR Research\EyeLink\
	C:\Program Files (x86)\SR Research\EyeLink

In this folder, there is a `libs` subfolder, which you need to add to the system Path (this may have been added to the path automatically, but check to make sure). You can do this by opening "My Computer", clicking on "View system information", opening the "Advanced" tab, clicking on "Environment Variables" and appending `;C:\Program Files\SR Research\EyeLink\libs` or (depending on your system) `;C:\Program Files (x86)\SR Research\EyeLink\libs` to the Path variable (under System variables).

### Installing PyLink

PyLink is the Python library for EyeLink support. PyLink is included with recent versions of the EyeLink display software (described above), and you can find it in one of the following folders (depending on your version of Windows):

	C:\Program Files\SR Research\EyeLink\SampleExperiments\Python
	C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python

Alternatively, you can download older versions of Pylink from here:

- <https://www.sr-support.com/showthread.php?14-Pylink>

To install PyLink in OpenSesame, simply copy the folder with the correct PyLink version to the OpenSesame program folder (i.e. `pylink27` for Python 2.7) and rename the folder to `pylink` (i.e. strip the Python version number from the folder name).

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

Don't fortget the trailing "/" character! Save the file (Control+O, Enter) and exit (Control+X). Now reload the software sources, and install the Eyelink display software (the version number might vary, at the time of writing it is 1.9):

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

- <http://osdoc.cogsci.nl/2.8/devices/eyelink>
