---
layout: osdoc
title: SR Box
group: Devices
permalink: /srbox/
parser: academicmarkdown
---

[TOC]

## About the srbox plug-in

The serial response (SR) box is a button box, specifically designed for response collection in psychological experiments. The original version, developed by Psychology Software Tools, has 5 buttons, 5 lights, and is connected to the PC trough the serial port. There are also SR Box compatible devices by other manufacturers, which may differ in the number of buttons and lights and often use a USB connection, which emulates a serial port.

The srbox plug-in for OpenSesame allows you to use the SR Box or compatible device in your OpenSesame experiments.

## Screenshot

%--
figure:
  source: srbox.png
  id: FigSrbox
  caption: The srbox plug-in in OpenSesame.
--%

## Setting the device name

By default, the plug-in tries to autodetect your SR Box. If this works, you don't have to change it. If your experiment freezes, OpenSesame has chosen the wrong serial port and you must enter the device name manually. Under Windows, the device is probably called something like

	COM4

Under Linux the device is probably called something like

	/dev/tty0

## Requirements

An SR Box or compatible button box. Not all button boxes are compatible, see:

- [/devices/button-box](/devices/button-box)

## Using the SR Box from Python inline code

%-- include: include/api/srbox.md --%
