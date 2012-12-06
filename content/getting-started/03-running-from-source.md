---
layout: osdoc
title: Running from source
group: Getting started
permalink: /running-from-source/
level: 1
sortkey: 003.003
---

This post describes how to set up a complete Python environment on your computer, so you can run OpenSesame directly from the source code. Depending on your needs, you could also consider using Python portable, as described [here][python-portable].

Overview
--------

- [Description of required packages](#description)
- [Isn't Python always run from source?](#always)
- [Reasons to run from source](#reasons)
- [Instructions for Linux](#linux)
- [Instructions for Windows](#windows)
- [Instructions for Mac OS](#macos)

Description of required packages {#description}
--------------------------------

OpenSesame depends on a number of other packages (dependencies), all of which are freely available. If you run OpenSesame from source you will need to manually install these packages. The minimum packages are:

- Python is the programming language in which OpenSesame is created.
- PyGame is a library that is used for graphics and sound. It is essentially a wrapper around the Simple DirectMedia Layer.
- (Py)Qt4 is the graphics toolkit that is used to construct the graphical user interface.
- NumPy is an advanced mathematical library, which is used for various things.

Isn't Python always run from source? {#always}
------------------------------------

Being clever, huh? But yes, actually you're right. However, the packages come with their own Python environment or, in the case of the Debian/ Ubuntu packages, all dependencies are installed automatically. If you run straight from the source code, you have to set up your own Python environment, which is a little extra work. But you don't need to compile anything, as, for example, you would need to do with a program written in C.

Reasons to run from source {#reasons}
--------------------------

The most obvious reason to run from source is that there may not be a package available for your platform (if you run, say, Solaris). Another reason, which applies only to the Windows and Mac packages, is that these packages come with their own Python environment, which doesn't allow you to install additional modules. If you want to use specific modules, which are not included with the packages, you will have to run from source.

Instructions for Linux {#linux}
----------------------

### Install dependencies

On most modern Linux distributions Python is installed by default and you can simply install python-pygame, python-qt4, python-numpy and python-serial using your package manager. Under Ubuntu, you can do this with the following command:

	sudo apt-get install python-pygame python-numpy python-serial python-qt4 python-tk

If you want to use the PsychoPy-based psycho back-end, you will also need to install PsychoPy. Under Ubuntu, you can do this with the following command: (If you are on a Debian/ Ubuntu system I would recommend adding the NeuroDebian repository to your software sources. NeuroDebian provides up to date packages of many neuroscience-related software. See these instructions.)

	sudo apt-get install psychopy

If you want to use the OpenGL back-end, you will need to install python-opengl. Under Ubuntu you can do this with the following command:

	sudo apt-get install python-opengl

### Run OpenSesame

Download the source code of the latest OpenSesame release here. Extract the .tar.gz to your home folder (any other location works analogously). Open a terminal and switch to the location of OpenSesame (this example assumes that the version is 0.21):

	cd ~/opensesame-0.21

Run OpenSesame using one of the following commands:

	python opensesame
	python opensesame --debug

Instructions for Windows {#windows}
------------------------

The links provided below are current as of Jan 20, 2011. Check the websites of the respective packages to check for more recent versions. Running OpenSesame from source has been tested on Windows XP.

### Selecting the best version of Python

There are multiple versions of Python available. OpenSesame has been tested extensively with Python 2.6 and 2.7. As of OpenSesame 0.27, Python 2.7 is the default version. Because 64-bit versions are not available for some of the required packages, it is recommended to stick to 32-bit versions of everything. Python 3.X will not work at all.

You need to install at least the following packages:

- Python <http://www.python.org/>
- PyGame <http://www.pygame.org/>
- PyQt4 <http://www.riverbankcomputing.co.uk/software/pyqt/intro>
- NumPy <http://numpy.scipy.org/>

The following packages are optional, but there's a good chance you will want to install at least one of them:

- PySerial <http://pyserial.sourceforge.net/>: Required for SR box and other serial port communications
- PsychoPy <http://www.psychopy.org/>: Required for psycho back-end
- Expyriment <http://www.expyriment.org>: Required for the xpyriment back-end
- PyOpenGL <http://pyopengl.sourceforge.net/>: Required for psycho and xpyriment back-ends

Please note that the packages listed above may, in turn, have dependencies that need to be installed. This is especially true for PsychoPy. For instructions, please refer to the respective homepages.

Run OpenSesame
--------------

Download the source code for the latest OpenSesame release [here][src_stable] or from [GitHub][src_unstable]. Extract the .tar.gz to `C:\` (any other location works analogously). You can extract .tar.gz files with WinRar. Open a command prompt (run command `cmd`) and switch to the location of OpenSesame (this example assumes that the version is 0.21):

	c:
	cd c:\opensesame-0.21

Run OpenSesame using one of the following commands (this example assumes that you have installed Python in `c:\Python27`):

	c:\Python27\python.exe opensesame
	c:\Python27\python.exe opensesame --debug

It's convenient to create a batch file for running OpenSesame from source. You can do this simply by creating a file called `opensesame.bat` containing one of the commands above. You will then be able to run OpenSesame by executing the batch file.

Instructions for Mac OS {#macos}
-----------------------

There are two ways to prepare the software environment for running OpenSesame from source on Mac OS X. One is by downloading and installing all the packages manually. The other is to use MacPorts, which compiles all required packages from source. Basically MacPorts is a large repository containing the source code of programs that have been ported from Linux to Mac OS X (which are very related as Mac OS X is also a Unix based system, as you might know). Installing all the packages manually seems pretty labour-intensive, but will be the fastest way nevertheless as Macports takes an astoundingly long time to compile all dependencies (with a quad core cpu it can already take up to a full day). On the other hand, MacPorts does not have the dependecy hassle if you ever want to install additional packages, which require other packages again, etc. Macports sorts out and installs these depencies itself. You have to decide for yourself which method of composing the source environment you like best. Both will work fine for running OpenSesame from source.

### Installing with MacPorts

The easiest way to install the necessary packages on Mac OS is probably using MacPorts, a large repository of packages. It takes a long time (and by this I mean many hours!) to install all the packages that are required for running OpenSesame, because MacPorts works by compiling from source. But on the bright side, it's a pretty straightforward process.

#### Download Xcode

The first thing that you need is Xcode, the Apple developer toolkit. Apple really wants you to buy the latest Xcode 4, which is not free, but apparently you can get Xcode 3 for free from their website. If you can't find it, might I suggest that you search your favorite pirate hangout for a copy. I tested this process with Xcode 3.2.5, but you can check the MacPorts website to see which versions of Xcode are supported.

Website: <http://developer.apple.com/technologies/tools/whats-new.html>

#### Download MacPorts

I used MacPorts 1.9.2, but again, any reasonably recent version should be fine.

Website: <http://www.macports.org/install.php>

#### Install dependencies

Essentially, you can now install all required packages by running a single command in a terminal:

	sudo port install py26-game py26-pyqt4 py26-serial py26-pil

This takes forever and, in my case, crashed a few times with a checksum error. You can simply recover from such errors by executing the following command:

	sudo port clean --all [package_that_caused_the_error]

Then you repeat the first command and MacPorts should be on its way again.

#### Make the MacPorts Python the default Python

Mac OS comes with a custom version of Python but, for our purpose (and many purposes), you need the official Python. This has already been installed by MacPorts, but you still need to make it the default. You can do this with the following command:

	sudo port select --set python python26

### Installing packages manually

If you want to install all Opensesame dependecies yourself you need to download and install the following package distributions:

#### Install Python

The python installation that comes with OS X by default is usually of a very old version (and nowadays is only 64-bit). Therefore it is better to install the newest version:

Website: <http://www.python.org/>

Direct download: http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg

#### Install PyGame

Website: <http://www.pygame.org/>

Direct download (Snow Leopard): <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.6-macosx10.6.mpkg.zip>
Direct download ((Mountain) Lion): <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.7-macosx10.7.mpkg.zip>

#### Install PyQt4

There is no official distribution (from Riverbank) available of PyQt4 for Mac OS X. However there are some well maintained unofficial distributions, but these miss the QScintilla module, which is required for the code editting window in OpenSesame. You need to download this file manually from the link provided below and move it in PyQt4 folder after installing it first.

Official website: <http://www.riverbankcomputing.co.uk/software/pyqt/intro>

Mac OS X distribution (PyQtX) website: <http://sourceforge.net/projects/pyqtx/>

Direct download: <http://sourceforge.net/projects/pyqtx/files/latest/download>

After PyQt4 is installed, download the QScintilla module (QSci.so) to the site-packages/PyQt4 folder (see section "Some final clean up" below, if you have trouble finding this folder).

#### Install NumPy and SciPy

Getting the latest version of NumPy or SciPy that works with the newer versions of the OS X (Lion/Mountain Lion) is a bit trickier, as the current official distributions of these packages are not supported yet by the newest OS X versions, due to the shift from 32-bit to 64-bit architecture. There is however a third-party installation script that takes care of this problem and gets numpy and scipy installed on your system, by compiling the latest versions of these packages from source.

Official website: <http://numpy.scipy.org/>

The installation script can be found at <http://fonnesbeck.github.com/ScipySuperpack/>  (Direct download: <https://raw.github.com/fonnesbeck/ScipySuperpack/master/install_superpack.sh>)
along with the instructions of how to use it. Basically you just have to run

	sudo sh ./install_superpack.sh

in the console in the folder which you downloaded the script.

Alternatively, you can also download the packages and install them yourself from <https://github.com/fonnesbeck/ScipySuperpack/zipball/master> if the script doesn't work for you, or you'd like to keep matters in your own hand. Using the script however is recommended, as it gets the job done without problems and is way easier.

#### Install PsychoPy (optional, required for psycho back-end)

PsychoPy requires the installation of a number of dependencies. Most of these can be installed fairly easily using setuptools.

Website: <http://pypi.python.org/pypi/setuptools>

Direct download: <http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea>

As described on the website, installation should proceed through the following steps:

Download the appropriate egg for your version of Python (e.g. setuptools-0.6c9-py2.7.egg). Do NOT rename it.

Run it as if it were a shell script, e.g. `sh setuptools-0.6c9-py2.7.egg`. Setuptools will install itself using the matching version of Python (e.g. python2.7), and will place the easy_install executable in the default location for installing Python scripts (as determined by the standard distutils configuration files, or by the Python installation).
Afterwards, install most dependencies with the command:

	sudo easy_install psychopy pyglet pyopengl pil

You may need to manually install Matplotlib, wxPython because (at the time of testing) these didn't install using easy_install. Make sure you install the versions that match your Python version.

*NOTE:* The psychopy backend does not seem to work yet and crashes with a message "No default config present". This problem is caused by the underlying package pyglet of which, again, there is no suitable version for the newer 64-bit or cocoa versions of Mac OS X yet. We are working on this problem and hope to have it solved soon.

#### Install wxPython (Optional, required for the PsychoPy back-end)

You can download wxPython yourself or install it using easy_install (see "install PsychoPy").

Website: <http://wxpython.org/>

Direct download: <http://downloads.sourceforge.net/wxpython/wxPython2.9-osx-docs-demos-2.9.4.0-cocoa-py2.7.dmg>

### Install PyOpenGL (Optional, required for opengl back-end)

You can download PyOpenGL yourself or install it using easy_install (see "install PsychoPy").

Website: <http://pyopengl.sourceforge.net/>

Direct download: <http://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.0.2a5.zip#md5=18cd8e5f8b57fa2d091ac07b0de35dfd>

*NOTE:* PyOpenGL does not work correctly yet under Mac Os X. When running your experiment, it will break off with the error message "Invalid foreground or background color". We are working on this problem.

#### Some final clean-up

Someone closely monitoring the installation process might have noticed that not all of the installed packages have ended up at the same place. This is because some have been copied to the site-packages folder of the Python installation that came with Mac OS X and others to the site-packages folder of the Python installation you performed at step 1 of these instructions. This is not a bad thing at all. Both site-packages folders are part of the path, so any import statement in Python will look and find the modules placed in either folder. Nevertheless, for numerous reasons it's better to have all the modules at the same place, so copy the contents of

	(/System)/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/

To

	/Library/Python/2.7/site-packages

If it asks if you want to overwrite any files choose No. Probably these are .pth files of which the correct ones are already placed in the destination folder. After you have completed this step, all modules are located in a single site-packages and shoulde be findable by Python when using the import statement.

#### Run OpenSesame

Download the source code of the latest OpenSesame release here. Extract the .tar.gz to your home folder (any other location works analogously). Open a terminal and switch to the location of OpenSesame (this example assumes that the version is 0.26):

	cd /Users/[your username]/opensesame-0.26

Run OpenSesame using one of the following commands:

	python opensesame
	python opensesame --debug

[python-portable]: /getting-started/running-with-python-portable
[src_stable]: http://files.cogsci.nl/software/opensesame/
[src_unstable]: https://github.com/smathot/OpenSesame