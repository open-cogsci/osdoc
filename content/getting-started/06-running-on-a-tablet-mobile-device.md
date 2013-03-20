---
layout: osdoc
title: Running on a tablet/ mobile device
group: Getting started
permalink: /running-on-a-tablet-mobile-device/
level: 1
sortkey: 003.006
---

A frequently asked question is whether it is possible to run OpenSesame on a tablet device.  Below is a short description of the current options:

- [Using an Android tablet](#android)
- [Using a Windows XP/Vista/ 7 tablet](#windows)
- [Using a Ubuntu on a Google Nexus 7](#nexus7)
- [Using an iPad](#ipad)

Using an Android tablet {#android}
-----------------------

For information about the OpenSesame runtime for Android, see [this page][android]

Using a Windows XP/ Vista/ 7 tablet {#windows}
-----------------------------------

There are a number of tablets available that run a regular installation of Windows XP/ Vista/ 7, rather than a mobile operating system. These tablets are essentially just laptops sans keyboard, and thus allow you to run OpenSesame in the same way that you would on a regular computer. Unfortunately, such tablets are rare and relatively expensive.

Using a Google Nexus 7
----------------------

The [Google Nexus 7][nexus7] manufactured by ASUS is a relatively cheap Android tablet. At the time of writing, you can pick one up for around €250/  $260 / £200 for the [16Gb][nexus16] version, and around €200/ $230/ £190 for [8Gb][nexus8] version. This tablet is unique in the sense that the developers of [Ubuntu Linux][ubuntu] provide an installer that allows you to easily install Ubuntu onto this device (you can recover Android afterwards). Since OpenSesame runs on Ubuntu, this is a straightforward and affordable way to run your experiments on a tablet. A short demonstration is provided in the video below:

<iframe width="640" height="480" src="http://www.youtube.com/embed/6kvEu_wkY08" frameborder="0" allowfullscreen></iframe>

### Installation

A step-by-step walk-through for installing Ubuntu onto the Nexus 7 is provided here:

- <https://wiki.ubuntu.com/Nexus7/Installation>

After you have installed the Ubuntu operating system, you can install OpenSesame from the [Cogsci.nl PPA][ppa] with the following commands:

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install opensesame

### Tips for creating experiments

If you run your experiment in fullscreen mode, the device will get confused because it does not know which display rotation to select. But you can run your experiment in an undecorated window that covers the entire display, which comes down to the same thing for most purposes.

- Change the back-end to legacy
- In the back-end settings, set
	- Window position to '0,0' (under Canvas)
	- Draw window frame to 'no' (under Canvas)
	- Enable escape to 'yes' (under Mouse)
- Next, run your experiment in Window mode (Control + W)

### Usability

After you have installed Ubuntu onto your tablet, you will likely find that the default "Unity" desktop environment is quite slow (although it does work). To increase the usability of your tablet, you can install [LXDE][], a light-weight desktop environment:

	sudo apt-get install lxde

In order to use LXDE, you need to log out, select LXDE, and log back in.

Furthermore, you will notice that Ubuntu is not very touch-friendly, and that typing commands using the default 'OnBoard' virtual keyboard is painstaking. [Quicksynergy][] allows you to share the keyboard and mouse with your regular computer (Windows, Mac, or Linux). This improves things a lot, especially when configuring the device, etc.

	sudo apt-get install quicksynergy

Using an iPad {#ipad}
-------------

It is not possible to run OpenSesame on the iPad. The iPad does not appear to be very Python-friendly, and it will therefore not be easy to port OpenSesame to the iPad.

[lxde]: http://lxde.org/
[nexus7]: http://www.amazon.com/gp/product/B008M04V1E/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B008M04V1E&linkCode=as2&tag=cogscinl-20
[nexus8]: http://www.amazon.com/gp/product/B008J6VYUC/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B008J6VYUC&linkCode=as2&tag=cogscinl-20
[nexus16]: http://www.amazon.com/gp/product/B008M04V1E/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B008M04V1E&linkCode=as2&tag=cogscinl-20
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl
[quicksynergy]: http://code.google.com/p/quicksynergy/
[ubuntu]: http://www.ubuntu.com/
[android]: /getting-started/android/