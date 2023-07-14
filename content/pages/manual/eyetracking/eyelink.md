title: Eyelink

[TOC]

## About EyeLink

The Eyelink series of eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for the Eyelink (called PyLink), which are used by PyGaze. The license of PyLink is incompatible with the license used by OpenSesame. For that reason, PyLink is not included in the default distribution of OpenSesame, and needs to be installed separately.


## Windows

### Installing the EyeLink Developers Kit

The Eyelink Developers Kit (sometimes called Display Software) provides the libraries that are required to communicate with the Eyelink PC. You can find it here (free registration required):

- <https://www.sr-research.com/support/thread-13.html>

If you extract the `.zip`, and then run the `.exe` installer, the EyeLink display will be installed in one of the following folders (depending on your version of Windows:

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

In this folder, there is a `libs` subfolder, which you need to add to the system Path (this may have been added to the path automatically, but check to make sure). You can do this by opening "My Computer", clicking on "View system information", opening the "Advanced" tab, clicking on "Environment Variables" and appending `;C:\Program Files\SR Research\EyeLink\libs` or (depending on your system) `;C:\Program Files (x86)\SR Research\EyeLink\libs` to the Path variable (under System variables).


### Installing OpenSesame with PyLink

PyLink is the Python library for EyeLink support. As of July 2023, PyLink supports Python versions up to 3.10, whereas OpenSesame by default uses Python 3.11. Therefore, until Pylink is updated for Python 3.11, the easiest way to install OpenSesame with Pylink is by building a Python 3.10 environment through Anaconda.

This sounds complicated, but it is really not. To do so, first read the general procedure for installing OpenSesame through Anaconda as described on the Downloads page:

- %link:download%

Next, once you understand the general procedure, start by creating a Python 3.10 environment, continue with the instructions from the Downloads page, and then install PyLink:

```
# Start by creating a Python 3.10 environment
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Now follow the instructions from the downloads page
# ...
# Then install PyLink from the SR Research PyPi repository
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
# And now launch OpenSesame!
opensesame
```

You can find more information about PyLink on the SR Research forum (free registration required):

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

The EyeLink display software can be installed directly from a repository. This also installs PyLink and various convenient tools, such ast the `edf2asc` converter.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

For more information, please visit:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

After you have install the EyeLink display software and PyLink per the instructions above, you can use the EyeLink with PyGaze! See:

- %link:pygaze%
