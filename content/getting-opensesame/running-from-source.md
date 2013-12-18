---
layout: osdoc
title: Running from source
group: Getting started
permalink: /running-from-source/
parser: academicmarkdown
---

This post describes how to set up a complete Python environment on your computer, so you can run OpenSesame directly from the source code. Depending on your needs, you could also consider using the [winpython-based package].

%--
toc:
 mindepth: 2
--%

## Download source code

Download the source code of the latest stable release from GitHub:
	
- <https://github.com/smathot/OpenSesame/releases>

You can also download a development snapshot of the code. To obtain a reasonable stable snapshot, download from the `master` branch. To get the latest, greatest, and potentially very unstable snapshot, download from the `playground` branch.

- <https://github.com/smathot/OpenSesame/>

## Dependencies

### Required

The following packages are required to run a minimal version of the OpenSesame GUI, with only support for the [legacy] back-end and no sound support.

- [Python](http://www.python.org) is the programming language in which OpenSesame is created.
- [PyGame](http://www.pygame.org) is a library that is used for graphics and sound.
- [PyQt4](http://www.riverbankcomputing.com/software/pyqt/download) is the graphics toolkit that is used to for the user interface.
- [QScintilla2](http://www.riverbankcomputing.com/software/pyqt/download) is a basic text-editor component. In some cases, it is bundled with `PyQt4`.
- [QProgEdit](https://github.com/smathot/QProgEdit) is an advanced text-editor component built on top of `QScintilla2`.

### Optional

The following packages are not required, but some functionality will be missing if they are not installed.

- [Expyriment](http://www.expyriment.org/) is required for the [xpyriment] back-end.
- [NumPy](http://www.numpy.org/) is an advanced mathematical library that is used for various things, such as sound support.
- [PIL](http://www.pythonware.com/products/pil/) is an imaging library that is used for various things.
- [PsychoPy](http://www.psychopy.org/) is required for the [psycho] back-end.
- [pyflakes](https://pypi.python.org/pypi/pyflakes) is required for automatic validation of your Python scripts.
- [Pyglet](http://www.pyglet.org/) is required by PsychoPy.
- [PyOpenGL]() is required by PsychoPy and Expyriment.
- [pySerial](http://pyserial.sourceforge.net/) is required for serial-port communication.
- [python-bidi](https://pypi.python.org/pypi/python-bidi) is required for bi-directional-text support.
- [python-markdown](https://pypi.python.org/pypi/Markdown) is required for viewing in-program help files.

### Extra

The following packages are not used directly by OpenSesame, but may come in handy while developing your experiments, and are included with the official Windows distribution of OpenSesame.

- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) is an alternative library for sound recording and playback.
- [Matplotlib](http://matplotlib.org/) is a library for plotting graphs.
- [Scipy](http://www.scipy.org/) is a set of miscellaneous scientific routines.
- [pyCairo](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo) is a library for vector graphics.
- [pyParallel](http://pyserial.sourceforge.net/pyparallel.html) allows communication via the parallel port.
- [OpenCV](http://opencv.org/) (Python bindings) is an extensive computer-vision library.

## Reasons to run from source

The most obvious reason to run from source is that there may not be a package available for your platform (if you run, say, Solaris). Another reason, which applies only to the Windows and Mac packages, is that these packages come with their own Python environment, which doesn't allow you to install additional modules. If you want to use specific modules, which are not included with the packages, you will have to run from source.

## Instructions for Linux

Under Ubuntu, all dependencies are available via the official repositories or the [Cogsci.nl PPA]. Therefore, the easiest way to install all dependencies is by first adding the Cogsci.nl PPA, and then installing all dependencies in one go.

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install python-pygame python-numpy python-qt4 \
		python-qscintilla2 psychopy expyriment python-qprogedit \
		python-serial
		
See [Dependencies](#dependencies) for a list of additional packages that you may want to install.

To start OpenSesame, open a terminal in the folder where OpenSesame has been extracted and run OpenSesame using one of the following commands:

	python opensesame
	python opensesame --debug

## Instructions for Windows

There are multiple versions of Python available. OpenSesame has been tested extensively with Python 2.6 and 2.7. As of OpenSesame 0.27, Python 2.7 is the default version. Because 64-bit versions are not available for some of the required packages, it is recommended to stick to 32-bit versions of everything. Python 3.X will not work at all.

To start OpenSesame, open a command prompt in the folder where OpenSesame has been extracted and run OpenSesame using one of the following commands (this example assumes that you have installed Python in `c:\Python27`):

	c:\Python27\python.exe opensesame
	c:\Python27\python.exe opensesame --debug

It's convenient to create a batch file for running OpenSesame from source. You can do this simply by creating a file called `opensesame.bat` containing one of the commands above. You will then be able to run OpenSesame by executing the batch file.

## Instructions for Mac OS

There are three ways to prepare the software environment for running OpenSesame from source on Mac OS X. One is by downloading and installing all the packages manually. The other is to use MacPorts, which compiles all required packages from source. Basically MacPorts is a large repository containing the source code of programs that have been ported from Linux to Mac OS X (which are very related as Mac OS X is also a Unix based system, as you might know). Installing all the packages manually seems pretty labour-intensive, but will be the fastest way nevertheless as Macports takes an astoundingly long time to compile all dependencies (with a quad core cpu it can already take up to a full day). On the other hand, MacPorts does not have the dependecy hassle if you ever want to install additional packages, which require other packages again, etc. Macports sorts out and installs these depencies itself. The final option is by using homebrew. This works on the same principle as macports, but if there are binary packages available for your system, hmoebrew will find these and install them instead. Therefore, it works much faster. The downside is that homebrew is 'less complete' than macports and you have to manually install most python packages (using easy_install and pip). You have to decide for yourself which method of composing the source environment you like best. All will work fine for running OpenSesame from source.

### Download Xcode

If you like to install using Homebrew or Macports, the first thing that you need to do is install Xcode, the Apple developer toolkit. You can get the latest version of Xcode for free from the App Store or from their website (you do need to login with an apple account though).

Website: <https://developer.apple.com/xcode/>

Using the App Store is preferable, as it will keep your version of X Code automatically up to date. You do need to also manually install the Command Line tools for X Code.


### Installing with MacPorts

Another way to install the necessary packages on Mac OS is by using MacPorts, a large repository of packages. It takes a long time (and by this I mean many hours!) to install all the packages that are required for running OpenSesame, because MacPorts works by compiling from source. But on the bright side, it's a pretty straightforward process.

#### Download MacPorts

You can download macports from its website on which you can also find the necessary documentation and a catalogue of all available packages.

Website: <http://www.macports.org/install.php>

You can add +universal to your /opt/local/etc/macports/variants.conf to ask MacPorts to build all ports you install with that variant (thus 32-bit and 64-bit versions packed in the same module), without having to remember to type it at every install command. However, some ports have not yet been tested as universal binaries and may not build properly.

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

### Installing using homebrew

Homebrew is a newer and easier way to build a source tree on your mac. It has many benefits on top of macports, such as speed, and nowadays seems to have less trouble compiling and updating packages than macports does. 
You can install homebrew as instructed on <http://http://brew.sh/>. Then issue the following command to get started:

    brew update
    brew doctor
		
Solve any problem that this indicates, and then continue on to the real work by issuing:

    brew install python qt pyqt qscintilla2 freetype portaudio

Now for pygame:

    brew tap homebrew/headonly
	brew install --HEAD smpeg
	brew install sdl sdl_image sdl_mixer sdl_ttf portmidi hg
	pip install hg+http://bitbucket.org/pygame/pygame
	
Install the necessary python packages

    sudo pip install pygopengl numpy pillow pyglet psychopy pyflakes markdown python-bidi pyserial
	
Install QProgEdit (from OpenSesame 2.8 on)

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	sudo python setup.py install
	cd ..
	rm -R QProgEdit

Install expyriment (from OpenSesame 0.27 on)

    hg clone https://code.google.com/p/expyriment/
	cd expyriment
	sudo python setup.py install
	cd ..
	rm -R expyriment
	
You should now be able to run OpenSesame, but you'll notice you're missing some icons! You need to download the Faenza icon theme from <http://tiheum.deviantart.com/art/Faenza-Icons-173323228> and place it under resources/theme/default
	
The following packages are optional, but might be useful to install nevertheless:

	sudo pip install matplotlib scipy pycairo pyparallel
	
For OpenCV (as it depends on numpy, do this *after* you issued the above pip commands)

	brew tap homebrew/science
	brew install opencv
	
you can find more detailed instructions on installing OpenCV at <http://www.jeffreythompson.org/blog/2013/08/22/update-installing-opencv-on-mac-mountain-lion/>
	
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

[winpython-based package]: /getting-opensesame/running-with-python-portable/
[EPD_Download]: http://www.enthought.com/products/epd.php
[EPD_Packages]: http://www.enthought.com/products/epdlibraries.php
[xpyriment]: /back-ends/xpyriment
[legacy]: /back-ends/legacy
[psycho]: /back-ends/psycho
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl