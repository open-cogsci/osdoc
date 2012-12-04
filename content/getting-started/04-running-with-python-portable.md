---
layout: osdoc
title: Running with Python portable
group: Getting started
permalink: /running-with-python-portable/
level: 1
sortkey: 003.004
---

About
-----

[Edwin Dalmaijer][edwin] (Universiteit Utrecht) has bundled OpenSesame with [portable Python][portable-python] (Windows only). Basically, this means that you run OpenSesame from source using a portable, but full Python environment. This is different from the regular Windows packages, because the OpenSesame source is not compiled into a .exe file. This doesn't mean that it's slower, though. It's simply a different way of packaging, with a number of benefits:

- PyLink and the [eyelink plug-ins][eyelink] are included, so it works out of the box with the Eyelink series of eye trackers
- A few other non-default plug-ins, such as the [questionnaire plug-ins][questionnaire], are included
- You get a portable Python environment that you can use for other purposes as well (e.g., for doing analyses)
- You can directly edit the OpenSesame source code
- You can easily download and run [the latest code snapshots][latest-code] from GitHub

Download and usage
------------------

If you have any questions, please post them on the forum.

- Forum topic about OpenSesame portable: <http://forum.cogsci.nl/index.php?p=/discussion/69/opensesame-0-25-portable>
- Download (select the latest release): <http://www.cogsci.nl/esdalmaijer/>

Once the download is complete, extract the .zip file to a location of your choice and double-click on `run_opensesame.bat` to start OpenSesame.

[edwin]: http://staff.fss.uu.nl/esdalmaijer
[portable-python]: http://www.portablepython.com/
[eyelink]: /plug-ins/eyelink-plug-ins
[questionnaire]: /plug-ins/questionnaire-plug-ins
[latest-code]: /getting-started/getting-the-latest-development-snapshot