---
layout: osdoc
title: Button box
group: Devices
permalink: /button-box/
---

There are many different types of button boxes, and they all work in different ways. Therefore, there is no single OpenSesame item that works with all button boxes. (This is different from keyboards, which are standard devices that all work with the `keyboard_response` item.)

Common types of button boxes:

- Some button boxes *emulate keypresses*. This is easy, because you can use the normal `keyboard_response` item.
- Some button boxes *emulate a joystick*. This is also easy, because you can use the [joystick](/devives/joystick/) plug-in.
- Some button boxes are compatible with the *Serial Response Box* that is developed by Psychology Software Tools. These button boxes are supported by the [srbox](/devices/srbox/) plug-in.
- Some button boxes have their own Python libaries. In this case, you should be able to find example scripts of how to use the button box in Python, that is, in an OpenSesame `inline_script` item.
