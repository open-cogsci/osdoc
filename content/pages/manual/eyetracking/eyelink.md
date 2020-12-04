title: Eyelink

[TOC]

## About EyeLink

The Eyelink series of eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for the Eyelink (called PyLink), which are used by PyGaze. The license of PyLink is incompatible with the license used by OpenSesame. For that reason, PyLink is not included in the default distribution of OpenSesame, and needs to be installed separately.


## SR Research forum

You will need to download some software from the SR Research forum. This is a closed forum, but you can register free of charge.

- <https://www.sr-support.com/>


## Windows

### Installing the EyeLink Developers Kit

The Eyelink Developers Kit (sometimes called Display Software) provides the libraries that are required to communicate with the Eyelink PC. You can find it here:

- <https://www.sr-support.com/thread-13.html>

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

Alternatively, you can download Pylink from here:

- <https://www.sr-support.com/thread-13.html>

To install PyLink in OpenSesame, simply copy the folder with the PyLink the OpenSesame program folder, or the `Lib\site-packages` subfolder. In some cases, the `pylink` folder has a name such as `pylink27-amd64`, in which case you have to rename it to just `pylink`.

__Important:__ The Python version of PyLink needs to match the Python version of your OpenSesame installation. In most cases, this means that you need PyLink for Python 3.7.


## Ubuntu

The EyeLink display software can be installed directly from a repository. This also installs PyLink and various convenient tools, such ast the `edf2asc` converter.

```
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

For more information, please visit:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

After you have install the EyeLink display software and PyLink per the instructions above, you can use the EyeLink with PyGaze! See:

- %link:pygaze%
