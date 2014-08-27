---
layout: osdoc
title: Drivers
group: Boks
permalink: /drivers/
show: True
---

The Boks and documentation below is under development.
{: .page-notification}

At the heart of the Boks is an [Arduino][] board. To use the Boks, you therefore need to install Arduino drivers, which are available for all platforms.

Overview
--------

- [Windows](#windows)
- [Linux](#linux)
- [Mac OS](#macos)

Windows driver installation {#windows}
---------------------------

First, download the Arduino software for Windows from [here][arduino-download]. Next, install the Arduino UNO drivers as explained [here][windows-instructions]. (The Arduino software includes a lot more than just the drivers. Unless you want to [update the firmware][firmware], you can ignore everything except for the drivers.)

For more information, please refer to the Arduino site:

- <http://arduino.cc/en/Guide/Windows>

Linux driver installation {#linux}
-------------------------

The Boks works almost straight-away on most modern Linux distributions. The only thing that you may need to do is add your user to the `dialout` group. Under recent distributions of Ubuntu you can do this with the following command (you need to log out/in for the group change to take effect):

	sudo usermod -aG dialout <myuser>

Usually, this will be sufficient, but [it has been reported](http://blog.markloiseau.com/2012/05/install-arduino-ubuntu/) that in some cases you need to explicitly modify the permission for the Arduino port:

	sudo chmod a+rw /dev/ttyACM0

For more information, please refer to the Arduino site:

- <http://playground.arduino.cc/Learning/Linux>

Mac OS driver installation {#macos}
---------------------------

The Boks has not been tested on Mac OS, but Arduino drivers are available. 

For more information, please refer to the Arduino site:

- <http://arduino.cc/en/Guide/MacOSX>

[arduino]: http://arduino.cc/
[arduino-download]: http://arduino.cc/en/Main/Software)
[windows-instructions]: http://arduino.cc/en/Guide/Windows#toc4
[firmware]: /boks/source
