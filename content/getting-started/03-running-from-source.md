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

The first thing that you need is Xcode, the Apple developer toolkit. You can get the latest version of Xcode for free from their website (you do need to login with an apple account though).

Website: <http://developer.apple.com/technologies/tools/whats-new.html>

#### Download MacPorts

You can download macports from its website on which you can also find the necessary documentation and a catalogue of all available packages.

Website: <http://www.macports.org/install.php>

#### Configuring MacPorts for psychopy support

Before you start building your Python environment, it is best to decide if want to be able to use OpenSesame's PsychoPy backend. On newer OS X verions (>10.6) macports builds everything with the 64-bit architecture by default, but Psychopy is unable to run in a 64-bit environment (yet, as of version 1.76.00) and will show unpredictable behaviour and crashes when it has to do so. If you would like to be able to use the psychopy backend, you will need to configure macports to compile everything with 32-bit architecture by changing

	build_arch=x86_64

to

	build_arch=i386

in /opt/local/etc/macports.conf

You don't need the PsychoPy backend to be able to run OpenSesame, as it has other quality backends like expyriment or legacy (pygame), so feel free to skip this step if you never plan on using PsychoPy.

#### Install dependencies

Essentially, you can now install all required packages by running a single command in a terminal:

	sudo port install py27-game py27-pyqt4 py27-scintilla py27-serial py27-pil py27-opengl py27-pyaudio opencv +python27

This takes forever and, in my case, crashed a few times with a checksum error. You can simply recover from such errors by executing the following command:

	sudo port clean --all [package_that_caused_the_error]

Then you repeat the first command and MacPorts should be on its way again.

#### Expyriment and Psychopy backends
Next to the legacy backend, which is based on pygame, OpenSesame also offers you the option of using expyriment or psychopy. In contrast to the legacy backend, both of these backends are hardware accelerated (OpenGL) and should have increased timing precision. You can use the python package manager 'pip' to install the other two backends. If you don't have pip installed, you can do so by executing the following command:

	sudo port install py27-pip

After the installation of pip is completed, you can easily install expyriment with:

	sudo pip install expyriment

If you plan on using the PsychoPy backend, make sure your Python environment is running in 32-bit mode. You can install psychopy and its dependency pyglet with the commands:

	sudo pip install pyglet 
	sudo pip install psychopy
	
PsychoPy refuses to run without the wxPython library installed (which is weird, because OpenSesame doesn't use any of the wx GUI components of psychopy), so as a final step install wxPython with:

	sudo port install py27-wxpython-dev

#### Make the MacPorts Python the default Python

Mac OS comes with a custom version of Python but, for our purpose (and many purposes), you need the official Python. This has already been installed by MacPorts, but you still need to make it the default. You can do this with the following command:

	sudo port select --set python python27

### Installing packages manually

If you want to install all Opensesame dependecies yourself you need to download and install the following package distributions:

#### Install Python

The python installation that comes with OS X is usually of an older version. Therefore it is better to install the newest version from python.org:

Website: <http://www.python.org/>

Direct download: http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg

Another option is to install the [Enthought Python Distribution (EPD)][EPD_Download] instead. This distribution includes Python and many of the modules OpenSesame depends on ([view][EPD_Packages] a complete list). 

#### Install PyGame

Website: <http://www.pygame.org/>

Direct download (Snow Leopard): <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.6-macosx10.6.mpkg.zip><br/>
Direct download ((Mountain) Lion): <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.7-macosx10.7.mpkg.zip>

#### Install PyQt4

There is no official distribution (from Riverbank) available of PyQt4 for Mac OS X. However there are some well maintained unofficial distributions:

Official website: <http://www.riverbankcomputing.co.uk/software/pyqt/intro>

Mac OS X distribution (PyQtX) website: <http://sourceforge.net/projects/pyqtx/> (Direct download: <http://sourceforge.net/projects/pyqtx/files/latest/download>)


After PyQt4 is installed, download and install the QScintilla module, which is used for the inline script editor in OpenSesame:

PyQScintillaX: <http://sourceforge.net/projects/pyqtx/files/PyQScintillaX/>

#### Install NumPy and SciPy

Getting the latest versions of NumPy or SciPy can be done in two ways:

You can use the installation script which can be found at <http://fonnesbeck.github.com/ScipySuperpack/>  (Direct download: <https://raw.github.com/fonnesbeck/ScipySuperpack/master/install_superpack.sh>)
along with the instructions of how to use it. This script will automatically find the latest versions of numpy and scipy and install them for you. Basically you just have to run

	sudo sh ./install_superpack.sh

in the console in the folder which you downloaded the script.

Alternatively, you can download and install the packages from the projects' own websites:

Numpy: <http://sourceforge.net/projects/numpy/files/NumPy/> (Direct download version 1.7.0: <http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/numpy-1.7.0-py2.7-python.org-macosx10.6.dmg/download>)
Scipy: <http://sourceforge.net/projects/scipy/files/scipy/> (Direct download version 0.11.0: <http://sourceforge.net/projects/scipy/files/scipy/0.11.0/scipy-0.11.0-py2.7-python.org-macosx10.6.dmg/download>)

#### Install PsychoPy and Expyriment(optional)

PsychoPy requires the installation of a number of dependencies. Most of these can be installed fairly easily using setuptools.

Website: <http://pypi.python.org/pypi/setuptools>

Direct download: <http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea>

As described on the website, installation should proceed through the following steps:

Download the appropriate egg for your version of Python (e.g. setuptools-0.6c9-py2.7.egg). Do NOT rename it.

Run it as if it were a shell script, e.g. 

	sh setuptools-0.6c9-py2.7.egg

Setuptools will install itself using the matching version of Python (e.g. python2.7), and will place the easy_install executable in the default location for installing Python scripts (as determined by the standard distutils configuration files, or by the Python installation).
Afterwards, install most dependencies with the command:

	sudo easy_install psychopy pyglet pyopengl pil expyriment

You may need to manually install Matplotlib, wxPython because (at the time of testing) these didn't install using easy_install. Make sure you install the versions that match your Python version.

*NOTE:* The psychopy backend does not seem to work yet and crashes. The reason is that PsychoPy (or rather its underlying library pyglet) can't cope with the 64-bit cocoa environment of the newer Mac OS X versions yet. In newer versions of psychopy this problem is hopefully solved.

#### Install wxPython (Optional, required for the PsychoPy back-end)

You can download wxPython yourself or install it using easy_install (see "install PsychoPy").

Website: <http://wxpython.org/>

Direct download: <http://downloads.sourceforge.net/wxpython/wxPython2.9-osx-2.9.4.0-cocoa-py2.7.dmg>

#### Install PyOpenGL (Optional, required for opengl or expyriment back-end)

You can download PyOpenGL yourself or install it using easy_install (see "install PsychoPy").

Website: <http://pyopengl.sourceforge.net/>

Direct download: <https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.0.2.tar.gz#md5=77becc24ffc0a6b28030aa109ad7ff8b>

### Run OpenSesame

Download the source code of the latest OpenSesame release here. Extract the .tar.gz to your home folder (any other location works analogously). Open a terminal and switch to the location of OpenSesame (this example assumes that the version is 0.26):

	cd /Users/[your username]/opensesame-0.26

Run OpenSesame using one of the following commands:

	python opensesame
	python opensesame --debug

[python-portable]: /getting-started/running-with-python-portable
[src_stable]: http://files.cogsci.nl/software/opensesame/
[src_unstable]: https://github.com/smathot/OpenSesame
[EPD_Download]: http://www.enthought.com/products/epd.php
[EPD_Packages]: http://www.enthought.com/products/epdlibraries.php
