---
layout: osdoc
title: Eyelink
group: Devices
permalink: /eyelink/
level: 1
sortkey: 009.002
---

##### The Python portable-based OpenSesame package ([link][python-portable]) comes with a full Python environment that works out of the box with the Eyelink.

The Eyelink series of eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for the Eyelink, which are used by the OpenSesame Eyelink plug-ins. Unfortunately, SR Research does not allow redistribution of their Python bindings, which means that you have to install them yourself and run OpenSesame from source. But don't worry, this is not as hard as it sounds! This tutorial will guide you through the process.

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

Running in dummy mode <a id='dummy'></a>
---------------------

You need to walk through the steps below only for the computer to which the Eyelink is actually attached. You can easily install the OpenSesame eyelink plug-ins on your own computer, as per [step 5](#step-5), without having to install anything or having to run OpenSesame from source. Obviously, you can only run the plug-in in 'dummy mode' in this case, but this is very convenient while developing and testing your experiment.

SR Research forum <a id='forum'></a>
-----------------

You will need to download some software from the SR Research forum. This is a closed forum, but you can register free of charge.

- <https://www.sr-support.com/forums/>

System requirements <a id='system-requirements'></a>
-------------------

This tutorial has been written for Windows XP 32-bit, for the simple reason that our own Eyelink PC uses this OS. You may still find this tutorial a useful resource when trying to install the OpenSesame Eyelink plug-ins on a different OS, but things will obviously work a little differently.

Step 1: Installing OpenSesame from source <a id='step-1'></a>
-----------------------------------------

The Windows binary of OpenSesame comes with its own Python environment and can only make use of the modules that have been included (PyGame, NumPy, etc.). Since PyLink is not included, and due to licensing restrictions probably never will be included, with OpenSesame, you will have to run OpenSesame from source. The following tutorial describes how to set-up the environment necessary for running OpenSesame from source:

- <http://osdoc.cogsci.nl/getting-started/running-from-source>

Step 2: Installing the Python Imaging Library <a id='step-2'></a>
---------------------------------------------

The Python Imaging Library is used to do some juggling between various image formats. You can download it here (make sure you download the most recent version for Python 2.6):

- <http://www.pythonware.com/products/pil/>

Step 3: Installing Eyelink display software <a id='step-3'></a>
-------------------------------------------

The Eyelink display software provides the libraries that are required to communicate with the Eyelink PC. You can find it here:

- <https://www.sr-support.com/forums/showthread.php?t=6>

Add the following directory to the Path (this may have been added to the path automatically, but check to make sure):

	C:\Program Files\SR Research\EyeLink\libs

You can do this by opeing “My Computer”, clicking on “View system information”, opening the “Advanced” tab, clicking on “Environment Variables” and appending `;C:\Program Files\SR Research\EyeLink\libs` to the Path variable (under System variables).

Step 4: Installing PyLink <a id='step-4'></a>
-------------------------

PyLink is a Python wrapper around the display software. There are two versions of PyLink: one with custom SDL and one without custom SDL. The reason that SR Research has changed some functionality in SDL (the Simple DirectMedia Layer, which is a set of libraries used to control the display etc.) is to improve timing accuracy. This is nice, but in the case of OpenSesame it is only relevant if you use the legacy (pygame) back-end: xpyriment and psycho have excellent timing regardless of which pylink version is used. The downside of pylink's custom SDL is that you may encounter compatibility issues.

The bottom line: Initially, you may want to use the with SDL version of pylink, because this is the default version. However, if you encounter weird issues (such as sound not working), you may want to try the without SDL version of pylink.

### Pylink with custom SDL

You can find it here:

- <https://www.sr-support.com/forums/showthread.php?t=14>

Download the `pylink_win32.zip` package and (assuming that you have installed Python to `c:\Python26`) copy the `pylink26` folder in its entirety to

	c:\Python26\Lib\site-packages

and rename the folder to `pylink`.

### Pylink without custom SDL

You can find it here:

- <https://www.sr-support.com/showthread.php?1971-quot-pylink-import-quot-after-quot-pygame-import-quot-causes-quot-DLL-load-failed-quot-error&p=6897#post6897>

Copy the `pylink` folder in its entirety to

	c:\Python26\Lib\site-packages

Step 5: Installing the OpenSesame Eyelink plug-ins <a id='step-5'></a>
--------------------------------------------------

You can download the latest Eyelink plug-ins from GitHub:

- <https://github.com/smathot/opensesame_eyelink_plugins/tags>

Extract the archive and put all the folders (eyelink_calibrate, etc.) directly into the plugins folder of OpenSesame, as per these instructions:

- <http://osdoc.cogsci.nl/plug-ins/plug-in-installation>

Step 6: Running OpenSesame with Eyelink support! <a id='step-6'></a>
------------------------------------------------

You're done! If you have installed the with SDL version of PyLink, you need to start OpenSesame with the `--pylink` command line argument (again, assuming that Python is installed in `c:\Python26`):

	c:\Python26\python.exe opensesame --pylink

If you start OpenSesame now, you should see the Eyelink plug-ins appear as additional items in the item toolbar (as in the screenshot below). You can drag and drop these items into your experiment!

![](/img/fig/fig7.6.1.png)

Documentation, examples and function overview <a id='documentation'></a>
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