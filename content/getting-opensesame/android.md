---
layout: osdoc
title: Runtime for Android
group: Getting OpenSesame
permalink: /android/
--- 

[Help us](http://forum.cogsci.nl/index.php?p=/discussion/439/opensesame-mobile-call-for-testers) test the OpenSesame runtime for Android!
{: .page-notification}

:--
cmd: overview
--:

## OpenSesame runtime for Android

### Download

You can download the OpenSesame runtime for Android through the Android market / Google Play Store:

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Get it on Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

Alternatively, you can download the latest OpenSesame runtime for Android package in `.apk` format from here:

- <http://files.cogsci.nl/software/opensesame/>

Once you have installed this package (please refer to Google for tips on installing `.apk` packages on your device) the OpenSesame runtime will simply appear as an app.

### Usage

When you start the OpenSesame runtime, you will be asked where your experiments are located. By default, OpenSesame assumes that they are in the `/sdcard/` folder, or (if it exists) in the `/sdcard/Experiments/` folder. If you have no experiments on your device, pressing `enter` will show the example experiments that are bundled with the `.apk`.

The `Back` button serves the same purpose as the `Escape` key on regular systems, and will exit OpenSesame.

### Debugging

Debug output is written to `/sdcard/opensesame-debug.txt`.

### Limitations

- The *synth* item and `openexp.synth` module are not functional.
- The *sampler* item and `openexp.sampler` module will ignore panning and pitching.
- Participants may be eaten by dragons.
- The `fixation_dot`, `touch_response`, and `notepad` plug-ins don't work.

### Supported devices

If you have tested the OpenSesame runtime for Android on a device, please [share your experiences][forum].

*The OpenSesame runtime for Android requires Android 2.2 'Froyo' or later.*

|**Device**				|**Android**				|**Status**		|
|Asus Transformer TF101	|4.0.3						|Works			|
|EEE PC 701 			|Android x86 4.0-r1			|Works			|
|Eken M009S				|2.2						|Works			|
|Samsung Galaxy S3 Mini	|4.1.2						|Works			|
|Samsung Galaxy S3		|4.0.4						|Works			|
|Mpman MP434			|2.2.1						|Works			|
|Nexus 4				|4.2.2						|Works			|
|Nexus 7				|4.2.1						|Works			|
|Sony Xperia SP			|4.1.2						|Works			|
|ZTE V970				|4.1.1						|Works			|

### Disabling automatic updates

If you are using the OpenSesame runtime for Android in a production environment (e.g., while you are running an experiment), it is recommended to disable the Auto-update feature of the Google Play Store, at least for OpenSesame. This will prevent the app from being updated and potentially changing its behavior.

## Developing experiments for Android

The OpenSesame runtime for Android requires the `droid` back-end, which is available as of OpenSesame 0.27.2.

A few design tips:

- Implement most user interactions through the `mouse_response` item or `touch_response` plug-in. In general, screen touches are registered as mouse clicks.
- The resolution for the `droid` backend is fixed at 1280x800. On Android, your experiment will be automatically scaled up or down depending on the resolution of the device, but the resolution that you design with is always 1280x800.

## Forum topics

A general forum topic on the OpenSesame runtime for Android:
	
- <http://forum.cogsci.nl/index.php?p=/discussion/333/opensesame-runtime-for-android>

Eoin Traver's project to test the OpenSesame runtime for Android (call for testers):
	
- <http://forum.cogsci.nl/index.php?p=/discussion/439/opensesame-mobile-call-for-testers>

[google-play]: https://play.google.com/store/apps/details?id=nl.cogsci.opensesame
[forum]: http://forum.cogsci.nl/index.php?p=/discussion/333/a-video-of-opensesame-running-natively-on-android