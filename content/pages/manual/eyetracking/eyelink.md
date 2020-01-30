title: Eyelink

[TOC]

## About EyeLink

The Eyelink series of eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for the Eyelink (called PyLink), which are used by PyGaze. The license of PyLink is incompatible with the license used by OpenSesame. For that reason, PyLink is not included in the default distribution of OpenSesame, and needs to be installed separately.


## Which Python version to use?

PyLink (see below) is not available for all versions of Python. At the time of writing, no PyLink version is available for Python 3.7, which is the default Python version used by OpenSesame. This means that you cannot use the default OpenSesame package for use with the EyeLink. You have two options:

- Use the Python 2.7-based package of OpenSesame. This is assumed for the explanation below.
- Install OpenSesame in your own Python 3.6, for example using Anaconda. You can then use the Python 3.6 version of PyLink, which you can download from the SR Support forum. (It is not included with the EyeLink display software.)


## SR Research forum

You will need to download some software from the SR Research forum. This is a closed forum, but you can register free of charge.

- <https://www.sr-support.com/forums/>


## Windows

### Installing the EyeLink display software

The Eyelink display software provides the libraries that are required to communicate with the Eyelink PC. You can find it here:

- <https://www.sr-support.com/forums/showthread.php?t=6>

If you extract the .zip, and then run the .exe installer, the EyeLink display will be installed in one of the following folders (depending on your version of Windows:

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

In this folder, there is a `libs` subfolder, which you need to add to the system Path (this may have been added to the path automatically, but check to make sure). You can do this by opening "My Computer", clicking on "View system information", opening the "Advanced" tab, clicking on "Environment Variables" and appending `;C:\Program Files\SR Research\EyeLink\libs` or (depending on your system) `;C:\Program Files (x86)\SR Research\EyeLink\libs` to the Path variable (under System variables).

### Installing PyLink

PyLink is the Python library for EyeLink support. PyLink is included with recent versions of the EyeLink display software (described above), and you can find it in one of the following folders (depending on your version of Windows):

```
C:\Program Files\SR Research\EyeLink\SampleExperiments\Python
C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python
```

Alternatively, you can download older versions of Pylink from here:

- <https://www.sr-support.com/showthread.php?14-Pylink>

To install PyLink in OpenSesame, simply copy the folder with the correct PyLink version to the OpenSesame program folder (i.e. `pylink27-amd64` for Python 2.7) and rename the folder to `pylink` (i.e. strip the Python version number from the folder name).


## Ubuntu

The EyeLink display software can be installed directly from a repository. This also installs PyLink and various convenient tools, such ast the `edf2asc` converter.

```
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

For more information, please visit:

- <https://www.sr-support.com/forum/downloads/eyelink-display-software/46-eyelink-developers-kit-for-linux-linux-display-software?16-EyeLink-Developers-Kit-for-Linux-(Linux-Display-Software)=>


## PyGaze

After you have install the EyeLink display software and PyLink per the instructions above, you can use the EyeLink with PyGaze! See:

- %link:pygaze%
