---
layout: osdoc
title: Eyelink
group: Devices
permalink: /eyelink/
level: 1
sortkey: 009.002
---

The Eyelink series of eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for the Eyelink, which are used by the OpenSesame Eyelink plug-ins. The license of the Eyelink Python bindings is incompatible with the license used by OpenSesame. For that reason, the Eyelink does not work out of the box with the official distribution of OpenSesame.

To use OpenSesame with the Eyelink, there are two options:

- *Easy:* Use the Python portable-based OpenSesame package ([link][python-portable]), which runs OpenSesame with Eyelink support out of the box.
- *Advanced:* Install all dependencies per the instructions below.

Overview
--------

- [Running in dummy mode](#dummy)
- [SR Research forum](#forum)
- [System requirements](#system-requirements)
- [Step 1: Installing OpenSesame from source](#step-1)
- [Step 2: Installing Eyelink display software](#step-2)
- [Step 3: Installing the Python Imaging Library](#step-3)
- [Step 4: Installing PyLink](#step-4)
- [Step 5: Installing the OpenSesame Eyelink plug-ins](#step-5)
- [Step 6: Running OpenSesame with Eyelink support!](#step-6)
- [Tutorial, documentation, examples and function overview](#documentation)

Running in dummy mode {#dummy}
---------------------

You need to walk through the steps below only for the computer to which the Eyelink is actually attached. You can easily install the OpenSesame eyelink plug-ins on your own computer, as per [step 5](#step-5), without having to install anything or having to run OpenSesame from source. Obviously, you can only run the plug-in in 'dummy mode' in this case, but this is very convenient while developing and testing your experiment.

SR Research forum {#forum}
-----------------

You will need to download some software from the SR Research forum. This is a closed forum, but you can register free of charge.

- <https://www.sr-support.com/forums/>

System requirements {#system-requirements}
-------------------

This tutorial has been written primarily for Windows XP 32-bit, for the simple reason that our own Eyelink PC uses this OS. Instructions for Ubuntu are also provided, but have not been tested extensively. You may still find this tutorial a useful resource when trying to install the OpenSesame Eyelink plug-ins on a different OS, but things will obviously work a little differently.

Step 1: Installing OpenSesame from source {#step-1}
-----------------------------------------

### Windows XP

The Windows binary of OpenSesame comes with its own Python environment and can only make use of the modules that have been included (PyGame, NumPy, etc.). Since PyLink is not included, and due to licensing restrictions probably never will be included, with OpenSesame, you will have to run OpenSesame from source. The following tutorial describes how to set-up the environment necessary for running OpenSesame from source:

- <http://osdoc.cogsci.nl/getting-started/running-from-source>

### Ubuntu

Under Linux, you can simply install OpenSesame as described [here](/getting-started/getting-opensesame/).

Step 2: Installing the Python Imaging Library {#step-2}
---------------------------------------------

### Windows XP

The Python Imaging Library is used to do some juggling between various image formats. You can download it here (make sure you download the most recent version for Python 2.6):

- <http://www.pythonware.com/products/pil/>

### Ubuntu

The Python imaging library is probably installed already. If not, run the following command in a terminal:

	sudo apt-get install python-imaging

Step 3: Installing Eyelink display software {#step-3}
-------------------------------------------

### Windows XP

The Eyelink display software provides the libraries that are required to communicate with the Eyelink PC. You can find it here:

- <https://www.sr-support.com/forums/showthread.php?t=6>

Add the following directory to the Path (this may have been added to the path automatically, but check to make sure):

	C:\Program Files\SR Research\EyeLink\libs

You can do this by opeing “My Computer”, clicking on “View system information”, opening the “Advanced” tab, clicking on “Environment Variables” and appending `;C:\Program Files\SR Research\EyeLink\libs` to the Path variable (under System variables).

### Ubuntu

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
	
Step 4: Installing PyLink {#step-4}
-------------------------

PyLink is a Python wrapper around the display software. 

### Windows XP

There are two versions of PyLink: one with custom SDL and one without custom SDL. The reason that SR Research has changed some functionality in SDL (the Simple DirectMedia Layer, which is a set of libraries used to control the display etc.) is to improve timing accuracy. This is nice, but in the case of OpenSesame it is only relevant if you use the legacy (pygame) back-end: xpyriment and psycho have excellent timing regardless of which pylink version is used. The downside of pylink's custom SDL is that you may encounter compatibility issues.

The bottom line: Initially, you may want to use the with SDL version of pylink, because this is the default version. However, if you encounter weird issues (such as sound not working), you may want to try the without SDL version of pylink.

#### Pylink with custom SDL

You can find it here:

- <https://www.sr-support.com/forums/showthread.php?t=14>

Download the `pylink_win32.zip` package and (assuming that you have installed Python to `c:\Python26`) copy the `pylink26` folder in its entirety to

	c:\Python26\Lib\site-packages

and rename the folder to `pylink`.

#### Pylink without custom SDL

You can find it here:

- <https://www.sr-support.com/showthread.php?1971-quot-pylink-import-quot-after-quot-pygame-import-quot-causes-quot-DLL-load-failed-quot-error&p=6897#post6897>

Copy the `pylink` folder in its entirety to

	c:\Python26\Lib\site-packages
	
### Ubuntu

Download the correct PyLink for your distribution from here (make sure that you have the correct Python version, usually 2.7, and chipset, x64 for 64 bit and x32 for 32 bit):

- <https://www.sr-support.com/forums/showthread.php?t=14>

Extract it to a location of your choice and rename the `pylink27` folder to `pylink`.

Step 5: Installing the OpenSesame Eyelink plug-ins {#step-5}
--------------------------------------------------

### All platforms

You can download the latest Eyelink plug-ins from GitHub:

- <https://github.com/smathot/opensesame_eyelink_plugins/tags>

Extract the archive and put all the folders (eyelink_calibrate, etc.) directly into the plugins folder of OpenSesame, as per these instructions:

- <http://osdoc.cogsci.nl/plug-ins/plug-in-installation>

Step 6: Running OpenSesame with Eyelink support! {#step-6}
------------------------------------------------

### Windows XP

You're done! If you have installed the with SDL version of PyLink, you need to start OpenSesame with the `--pylink` command line argument (again, assuming that Python is installed in `c:\Python26`):

	c:\Python26\python.exe opensesame --pylink

If you start OpenSesame now, you should see the Eyelink plug-ins appear as additional items in the item toolbar (as in the screenshot below). You can drag and drop these items into your experiment!

![](/img/fig/fig7.6.1.png)

### Ubuntu

You can start OpenSesame in the usual way from the applications menu, or by running the following command in a terminal:

	opensesame

Documentation, examples and function overview {#documentation}
---------------------------------------------

You can find a tutorial for using the OpenSesame Eyelink plug-ins here [(PDF)][tutorial].

The following experiment, kindly provided by Daniel Schreij, shows how to use the OpenSesame Eyelink plug-ins from the graphical interface:

- [schreij_owens_theeuwes_2008_eyelink.opensesame][example-schreij]

###### Schreij, D., Owens, C., & Theeuwes, J. (2008). Abrupt onsets capture attention independent of top-down control settings. Perception & Psychophysics, 70(2), 208-218.

The example below shows how to display the trajectory of an eye movement immediately after every trial, using Python inline code. I created this as a demonstration of saccadic curvature for a class of students.

- [curvature_demo.opensesame.tar.gz][example-curvature]

You can also access the Eyelink using python in an inline_script item. The eyelink class is a property of the experiment class, which (in an inline_script item) you can access like this:

{% highlight python %}
exp.eyelink
{% endhighlight %}

So, for example, you can do the following:

{% highlight python %}
exp.eyelink.log("Message for the EDF")
time, start_pos = exp.eyelink.wait_for_saccade_start()
time, start_pos, end_pos = exp.eyelink.wait_for_saccade_end()
x, y = exp.eyelink.sample()
{% endhighlight %}

Below is the full list of available functions. It is also possible to use the PyLink API directly, but I recommend using the libeyelink functions, which are considerably easier to use.

{% include doc/libeyelink %}

[python-portable]: /getting-started/running-with-python-portable/
[tutorial]: http://files.cogsci.nl/software/opensesame/plugins/eyelink/tutorial/Schreij_Mathot_OpenSesame_Eyelink_Tutorial.pdf
[example-schreij]: http://files.cogsci.nl/software/opensesame/plugins/eyelink/examples/schreij_owens_theeuwes_2008_eyelink.opensesame
[example-curvature]: https://github.com/smathot/OpenSesame/raw/master/examples/curvature_demo.opensesame.tar.gz