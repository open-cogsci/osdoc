---
layout: osdoc
title: Grip devices (U Plymouth)
group: Devices
permalink: /grip-devices/
level: 1
sortkey: 009.008
---

The grip devices are a pair of custom input devices that are used (primarily at the University of Plymouth) to collect responses made using a power and a precision grip. Essentially, the grip-devices are like a button box, except you need to squeeze either a big cylinder (power grip) or a small button (precision grip) to give a response.

port_reader plug-in
-------------------

The easiest way to use the grip devices in OpenSesame is through the port_reader plug-in. This plug-in is also used in some of the examples (see below). The port_reader is Windows only, because it relies on `inpout32.dll`. The port_reader is a generic input plug-in and requires specific settings in order to work with the grip devices. The default settings appear to be as follows:

{% highlight python %}
port number = 889
resting state value = 127
power response value = 63
precision response value = 11
{% endhighlight %}

However, these values depend on how the grip devices are connected. In order to find out the proper values, you can use the grip_test experiment (see below).

Using inpout32.dll directly
---------------------------

You can also control the grip devices directly using Python inline script. For an example script, see [Using the serial/ parallel port][serial-parallel].

Example experiments
-------------------

- [grip_test][grip-test] is a test experiment that displays the values that it reads from the parallel port. So you can squeeze the devices and determine the resting state value (no device pressed), the precision response value and the power response value. Uses the port_reader plug-in.

The following experiments provide complete examples of using the grip devices, using the keyboard to emulate the grip devices (for testing the experiment) and counterbalancing the response rule based on subject nr.

- [grip_devices_image_example][grip-image] is a basic affordances experiment using the Rossion & Pourtois line drawings. Uses the port_reader plug-in.
- [grip_devices_photo_example][grip-photo] is a basic affordances experiment using the BOSS stimuli. Uses the port_reader plug-in.
- [grip_devices_video_example][grip-video] is a more complicated affordances experiment using videos. This example shows how to poll the grip devices during video playback using Python scripting. (Note that the videos are not included, but you can easily change the experiment to use your own videos.)

[serial-parallel]: /devices/serial-parallel-port/
[grip-test]: http://files.cogsci.nl/software/opensesame/examples/plymouth/grip_test.opensesame.tar.gz
[grip-image]: http://files.cogsci.nl/software/opensesame/examples/plymouth/grip_devices_image_example.opensesame.tar.gz
[grip-photo]: http://files.cogsci.nl/software/opensesame/examples/plymouth/grip_devices_photo_example.opensesame.tar.gz
[grip-video]: http://files.cogsci.nl/software/opensesame/examples/plymouth/grip_devices_video_example.opensesame.tar.gz