---
layout: osdoc
title: Running on a Raspberry Pi
group: Devices
permalink: /raspberry-pi/
level: 1
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About the Raspberry Pi

The Raspberry Pi is a computer the size of a credit card. By default, the Pi runs a customized version of Debian Linux called Raspbian.

%--
figure:
 id: BoksOfPi
 source: boksofpi.png
 caption: "The Raspberry Pi is nothing more than a print board with some connections. Yet it may be (almost) all you need to run psychological experiments!"
--%

See also:

- <http://www.raspberrypi.org/>
- <http://www.raspbian.org/>

## Installing OpenSesame

You can install OpenSesame in Raspbian with the script shown in %InstallScript. Change `$OSVER` to match the latest version of OpenSesame.

%--
code:
 id: InstallScript
 source: install-opensesame-rpi.sh
 syntax: bash
 caption: "Script for installing OpenSesame onto Raspbian."
--%

## Running OpenSesame

To start OpenSesame, navigate to the folder where OpenSesame has been installed and execute `opensesame` or `opensesamerun`:
	
{% highlight bash %}
cd OpenSesame-release-0.27.4
./opensesame
{% endhighlight %}

## Limitations

At the time of testing, the Raspberry Pi does not support hardware-accelerated graphics. This means that only the [legacy] back-end works.

## More information

Some tests and impressions are available here:

- <http://www.cogsci.nl/blog/miscellaneous/216-running-psychological-experiments-on-a-raspberry-pi-with-opensesame>

[legacy]: /back-ends/legacy