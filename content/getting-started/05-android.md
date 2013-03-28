---
layout: osdoc
title: Runtime for Android
group: Getting started
permalink: /android/
level: 1
sortkey: 003.004
--- 

##### The OpenSesame runtime for Android is experimental.

Overview
--------

- [OpenSesame runtime for Android](#runtime)
	- [Download](#download)
	- [Usage](#usage)
	- [Debugging](#debugging)
	- [Limitations](#limitations)
	- [Supported devices](#devices)
- [Developing experiments for Android](#development)

OpenSesame runtime for Android {#runtime}
------------------------------

### Download {#download}

You can download the OpenSesame runtime for Android through the Android market / Google Play Store:

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Get it on Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

Alternatively, you can download the latest OpenSesame runtime for Android package in `.apk` format from the list of pre-release packages:

- <http://files.cogsci.nl/software/opensesame/pre-releases/>

Once you have installed this package (please refer to Google for tips on installing `.apk` packages on your device) the OpenSesame runtime will simply appear as an app.

### Usage {#usage}

When you start the OpenSesame runtime, you will be asked where your experiments are located. By default, OpenSesame assumes that they are in the `/sdcard/` folder, or (if it exists) in the `/sdcard/Experiments/` folder. If you have no experiments on your device, pressing `enter` will show the example experiments that are bundled with the `.apk`.

The `Back` button serves the same purpose as the `Escape` key on regular systems, and will exit OpenSesame.

### Debugging {#debugging}

Debug output is written to `/sdcard/opensesame-debug.txt`.

### Limitations {#limitations}

- The *synth* item and `openexp.synth` module are not functional.
- The *sampler* item and `openexp.sampler` module will ignore panning and pitching.
- Participants may be eaten by dragons.

### Supported devices {#devices}

If you have tested the OpenSesame runtime for Android on a device, please [share your experiences][forum].

*The OpenSesame runtime for Android requires Android 2.2 'Froyo' or later.*

|**Device**				|**Android**		|**Status**		|
|Asus Transformer TF101	|4.0.3				|Works			|
|Eken M009S				|2.2				|Works			|
|Mpman MP434			|2.2.1				|Works			|
|Nexus 7				|4.2.1				|Works			|
|ZTE V970				|4.1.1				|Works			|

Developing experiments for Android {#development}
----------------------------------

The OpenSesame runtime for Android requires the `droid` back-end, which is available as of OpenSesame 0.27.2, currently in pre-release. You can get the latest pre-release from here:

- <http://files.cogsci.nl/software/opensesame/pre-releases/>

A few design tips:

- Implement most user interactions through the *mouse_response* item. Screen touches are registered as mouse clicks.
- The resolution for the `droid` backend is fixed at 1280x800. On Android, your experiment will be automatically scaled up or down depending on the resolution of the device, but the resolution that you design with is always 1280x800.

[google-play]: https://play.google.com/store/apps/details?id=nl.cogsci.opensesame
[forum]: http://forum.cogsci.nl/index.php?p=/discussion/333/a-video-of-opensesame-running-natively-on-android