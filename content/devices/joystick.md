---
layout: osdoc
title: Joystick
group: Devices
permalink: /joystick/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About

Joysticks and gamepads are supported through the `joystick` plug-in.

## Using a joystick through Python inline code

If you insert the `joystick` plugin at the start of your experiment, a `joystick` object automatically becomes part of the experiment object and can be accessed from within an inline_script item as `exp.joystick`. Below is a list of available functions.

{% include doc/libjoystick %}
