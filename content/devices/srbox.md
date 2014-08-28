---
layout: osdoc
title: SR Box
group: Devices
permalink: /srbox/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About the srbox plug-in

The serial response (SR) box is a button box, specifically designed for response collection in psychological experiments. The original version, developed by Psychology Software Tools, has 5 buttons, 5 lights, and is connected to the PC trough the serial port. There are also SR Box compatible devices by other manufacturers, which may differ in the number of buttons and lights and often use a USB connection, which emulates a serial port. The advantage of using an SR Box is that response times can be measured more accurately than using a garden variety keyboard. Of course, it also looks much more sciency. The SR Box plug-in for OpenSesame allows you to use the SR Box or compatible device in your OpenSesame experiments. The plug-in appears as an item in the item toolbar and you can simply drag it into your experiment.

## Screenshot

![](/img/fig/fig7.7.1.png)

## Setting the device name

By default, the plug-in tries to autodetect your SR Box. If this works, you don't have to change it. If your experiment freezes, OpenSesame has chosen the wrong serial port and you must enter the device name manually. Under Windows, the device is probably called something like

	COM4

Under Linux the device is probably called something like

	/dev/tty0

## Requirements

An SR Box or compatible device and OpenSesame 0.22 or higher.

## Download and installation

As of 0.25, the srbox plugin is included with OpenSesame by default, so no installation is required.

## Using the SR Box from Python inline code

{% include doc/libsrbox %}
