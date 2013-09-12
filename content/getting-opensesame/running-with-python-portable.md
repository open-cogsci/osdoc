---
layout: osdoc
title: Running with Python portable
group: Getting OpenSesame
permalink: /running-with-python-portable/
---

:--
cmd: overview
--:

## About

[Edwin Dalmaijer][edwin] (Utrecht University) has bundled OpenSesame with [Portable Python][portable-python] (Windows only). As of OpenSesame 0.27.2, [WinPython][winpython] (another portable distribution of Python) is used in favor of Portable Python. The advantage of using WinPython is that it is tailord to scientific use, as is reflected in the fact that it contains Spyder (a code editor) and a number of analysis tools (e.g. NumPy and Matplotlib). For a full overview, please refer to the WinPython website.

Basically, this means that you run OpenSesame from source using a portable, but full Python environment. This is different from the regular Windows packages, because the OpenSesame source is not compiled into a .exe file. This doesn't mean that it's slower, though. It's simply a different way of packaging, with a number of benefits:

- PyLink and the [eyelink plug-ins][eyelink] are included, so it works out of the box with the Eyelink series of eye trackers
- You get a portable Python environment that you can use for other purposes as well (e.g., for doing analyses)
- You can directly edit the OpenSesame source code
- You can easily download and run [the latest code snapshots][latest-code] from GitHub

A note of thanks goes out to Bob Rosbag (Utrecht University), who pointed us towards WinPython and helped modifying the package to suit our needs.

## Download and usage

If you have any questions, please post them on the forum.

- Forum topic about OpenSesame portable: <http://forum.cogsci.nl/index.php?p=/discussion/69/opensesame-0-25-portable>
- Download (select the latest release): <http://www.cogsci.nl/esdalmaijer/>

Once the download is complete, extract the .zip file to a location of your choice and double-click on 'opensesame.bat' to start OpenSesame.

[edwin]: http://staff.fss.uu.nl/esdalmaijer
[portable-python]: http://www.portablepython.com/
[winpython]: http://code.google.com/p/winpython/
[eyelink]: /devices/eyelink
[questionnaire]: /plug-ins/questionnaire-plug-ins
[latest-code]: /getting-opensesame/development-snapshots