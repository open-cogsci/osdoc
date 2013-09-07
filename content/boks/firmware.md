---
layout: osdoc
title: Source code and firmware
group: Boks
permalink: /source/
level: 1
sortkey: 0019.008
show: True
---

The Boks and documentation below is under development.
{: .page-notification}

Source code
-----------

The source code for the Boks is hosted on GitHub:

- <https://github.com/smathot/boks/tags>

Firmware
--------

To update the firmware on the Boks, first download the source code from GitHub. You will find the firmware in the `arduino/boks` folder. To upload the firmware to the Boks, you can follow one of the following procedures:

### Using the `flash` script

On Linux, you can use the `flash` script to upload the latest firmware to the Boks. This script will automatically download the latest (stable) firmware from GitHub, insert the correct model and button layout, compile it, and upload it to the Boks.

For example, to upload the latest firmware for a 2 button 'dev.boks' model, run the following command:

	./flash	--model=dev.boks --buttons=2 --upload

### Using the Arduino IDE

- First, rename `boks.ino.dist` to `boks.ino`
- Open `boks.ino` in the Arduino IDE.
- Change the line `#define MODEL 				"dev.boks        "` to include your model name. Make sure that the string is exactly 16 characters!
- Change the lines like `#define BUTTON_PIN_3 		9` to `#define BUTTON_PIN_3 		0` for all buttons that are not present on your Boks.
- Click on the upload button.
- Done!

For more information about the Arduino IDE, please refer to the Arduino site:

- <http://arduino.cc/en/Guide/Environment>