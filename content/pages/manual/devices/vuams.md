---
layout: osdoc
title: Ambulatory Monitoring System (VU-AMS)
group: Devices
permalink: /vu-ams/
---

The VU University Ambulatory Monitoring System (VU-AMS) is a device that can be used to measure a variety of factors related to heart rate, respiration, and body movement. The developers made an OpenSesame [plugin](https://github.com/JdenHartog/vu_ams).

- <http://www.vu-ams.nl/>

%--
figure:
 id: FigVuamsDevice
 source: VU-AMS.png
 caption: |
  The VU-AMS device.
--%

[TOC]

## Using the `vu-ams` plugin

vu-ams is a third-party plugin.
{: .page-notification}

Markers can be sent with the `vu-ams` plugin which currently works under **Windows only**.

The plugin has three input boxes:

- The *Device name* can be autodetect or can be specified manually.
- The *Send marker* value ranges between 0-65535 and specifies the marker number to send.
- The *Use number from title* checkbox allows you to use a number from the item title to send.
- The *Use without VU-AMS device* checkbox allows you to run your experiment without a VU-AMS connected and recording.

You can download the plugin from here:

- <https://github.com/JdenHartog/vu_ams/releases>

%--
figure:
 id: FigScreenshot
 source: plugin-screenshot.png
 caption: |
  A screenshot of the `vu-ams` plugin.
--%

## Setting the device name

By default, the plugin tries to autodetect the VU-AMS. If this works, you don't have to change it. If your experiment stops, OpenSesame can't automatically detect the port and you must enter the device name manually. Under Windows, the device is called something like

	COM3

Note that entering a device name manually makes your experiment start a bit faster because than the plugin doesn't have to sequentially  try all ports.

## Requirements

A VU-AMS device see:

- <http://www.vu-ams.nl/>

## Using the vu-ams from Python inline code

## class __AMS__

If you insert the vu-ams plugin at the start of your experiment, an
instance of `AMS` automatically becomes part of the `var`
object and can be accessed within an inline_script item as `var.AMS`
Technically you will be calling *AmsSerial.dll* functions directly.

__Function list:__

- [function __AMS\.SendCodedMarker__\(int\)](#function-__AMSSendCodedMarker__int)

__Example:__

~~~ .python
try:
	var.AMS.SendCodedMarker(555)
except:
	print 'Failed sending marker!'
~~~

### [function __AMS\.SendCodedMarker__\(int\)](#function-__AMSSendCodedMarker__int) {#function-__AMSSendCodedMarker__int}

Sends a coded marker to the VU-AMS device.

__Arguments:__

- `int` -- The integer to send.
	- Type: int


[function __AMS\.SendCodedMarker__\(int\)]: #function-__AMSSendCodedMarker__int


## Troubleshooting

Make sure to close the VU-DAMS suite *device configuration window* as the VU-AMS device can 'talk' to one application at a time.

Please don't hesitate to post questions on the forum, or to let us know of your experiences (good or bad).

