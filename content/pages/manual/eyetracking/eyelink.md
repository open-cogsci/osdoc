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

`pylink` is the Python library for EyeLink support. Currently, `pylink` only supports Python 3.12 and earlier, whereas the standard packages of OpenSesame are built with Python 3.13. Therefore, you must use the Python 3.12 (or earlier) package of OpenSesame from [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases).

Next, `pylink` can be installed from the SR Research PyPi repository through `pip install`:

```
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
```

Important: do *not* try to install `pylink` by running `pip install pylink`. Doing so will install a completely different package!

You can find more information about `pylink` on the SR Research forum (free registration required):

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

The EyeLink display software can be installed directly from a repository. This also installs PyLink and various convenient tools, such ast the `edf2asc` converter.

```bash
sudo add-apt-repository 'deb [arch=amd64] https://apt.sr-research.com SRResearch main'
sudo apt-key adv --fetch-keys https://apt.sr-research.com/SRResearch_key
sudo apt-get update
sudo apt-get install eyelink-display-software
```

For more information, please visit:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

After you have install the EyeLink display software and PyLink per the instructions above, you can use the EyeLink with PyGaze! See:

- %link:pygaze%


## SR Research eyelink plugin

SR Research also provides their own EyeLink plug-ins for OpenSesame. These are somewhat similar to (and originally based on) the PyGaze plugins, but offer some functionality that is not available through PyGaze. To install these plugins, run:

```
pip install opensesame-plugin-eyelink
```

For more information, please visit:

- <https://www.sr-research.com/support/thread-52.html>
