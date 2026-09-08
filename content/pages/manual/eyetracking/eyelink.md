title: EyeLink

[TOC]

## About EyeLink

The EyeLink eye trackers, produced by SR Research, are one of the most commonly used eye trackers in psychological research. SR Research provides Python bindings for communicating with the EyeLink (called PyLink), which are used by PyGaze and their own EyeLink Plugin. 


## Installing PyLink

The Python library for EyeLink integration is available on PyPI as `sr-research-pylink`. It has full support for Windows, macOS, and Linux across Python 2.7 to 3.14, so it can be installed in the latest OpenSesame installations.

You can install it directly from the terminal:

```
pip install sr-research-pylink
```

**Important:** Do *not* try to install `pylink` by running `pip install pylink`. Doing so will install a completely different, unrelated package!

You can find more information about `sr-research-pylink` on the SR Research forum (free registration required):

- <https://www.sr-research.com/support/> 
- <https://www.sr-research.com/support/thread-48.html>
	
## PyGaze

After you have installed PyLink using the instructions above, you can use the EyeLink with PyGaze! See:

- %link:pygaze%

## SR Research EyeLink Plugin

SR Research also provides their own EyeLink plugin set for OpenSesame. This plugin offers additional EyeLink integration not available through PyGaze, such as a gaze trigger, EDF transfer when a task is aborted, and full support during camera transfer for recent EyeLink models. To install their plugin, run:

```
pip install opensesame-plugin-eyelink
```

For more information, please visit:

- <https://www.sr-research.com/support/thread-52.html>

## Optional: EyeLink Developers Kit

While no longer required to run PyLink in OpenSesame, the EyeLink Developers Kit (sometimes called EyeLink Display Software) provides additional useful tools, such as the `edf2asc` converter, documentation, and offline `sr-research-pylink` installation files (.whl).

If you need these utilities, you can find the installers for Windows, macOS, and Ubuntu repositories on the SR Research Support site:

- <https://www.sr-research.com/support/forum-9.html>