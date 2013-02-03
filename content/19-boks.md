---
layout: osdoc
title: Boks
group: General
permalink: /boks/
level: 0
sortkey: 0019.001
menuclass: external
ext_url: /boks
show: False
---

Overview
--------

- [About](#about)
- [Get a Boks](#getit)
- Driver installation
	- [Windows](#install-windows)
	- [Linux](#install-linux)
	- [Mac OS](#install-macos)
- Usage
	- [OpenSesame plug-in](#opensesame)
	- [Python module](#python)
	- [Serial port communication](#serial)
- Advanced
	- [Source code](#source)
	- [Timing](#timing)
	- [Test your own system](#test)
	- [Updating firmware](#firmware)

About Boks {#about}
----------

The Boks is an open-source response box for use in psychological and neuroscientific experiments. The hardware has been developed by [Beter Elektro](http://www.beterelektro.nl/), a Dutch electronics company. The software is developed by the OpenSesame community.

Features:

- The most affordable response box on the market
- [Seamless integration](#openesame) with OpenSesame
- Comfortable and durable
- Sub-millisecond temporal precision [timing](#timing)
- [open source](#source)
- Intregrated photodiode to test your own system
- USB connected

In addition, part of the price is a direct donation to the OpenSesame project. So your purchase of the Boks helps to maintain OpenSesame!

![](/img/fig/fig19.1.1.png)

Get a Boks {#getit}
----------

Currently, the Boks is under development and used by a limited number of bèta testers. Details on prices and availablity will be provided at a later date.

Windows driver installation {#install-windows}
---------------------------

First, download the Arduino software for Windows from [here](http://arduino.cc/en/Main/Software). Next, install the Arduino UNO drivers as explained [here](http://arduino.cc/en/Guide/Windows#toc4). (The Arduino software includes a lot more than just the drivers. Unless you want to [update the firmware](#firmware), you can ignore everything except for the drivers.)

For more information, please refer to the Arduino site:

- <http://arduino.cc/en/Guide/Windows>

Linux driver installation {#install-linux}
-------------------------

The Boks works almost straight-away on most modern Linux distributions. The only thing that you may need to do is add your user to the `dialout` group. Under recent distributions of Ubuntu you can do this with the following command (you need to log out/in for the group change to take effect):

	sudo usermod -aG dialout <myuser>

For more information, please refer to the Arduino site:

- <http://playground.arduino.cc/Learning/Linux>

Mac OS driver installation {#install-macos}
---------------------------

The Boks has not been tested on Mac OS, but Arduino drivers are available. 

For more information, please refer to the Arduino site:

- <http://arduino.cc/en/Guide/MacOSX>

OpenSesame plug-in {#opensesame}
------------------

You can download the Boks software from here (select the latest release):

- <https://github.com/smathot/boks/tags>

If you download and extract the software, the OpenSesame plug-in is located in the folder:

	opensesame/boks

To install the plug-in, copy the plug-in folder to the OpenSesame plug-in folder, as described [here](plug-in installation). After you have installed the plug-in and restarted OpenSesame, you should see the Boks plug-in icon appear in the item toolbar:

![](/img/fig/fig19.1.2.png)

After you have dragged a Boks item into your experiment, you see the following controls:

![](/img/fig/fig19.1.3.png)

The Boks model and the firmware version will be detected by the plug-in. In addition, you can test whether the Boks functions properly by clicking on the *Start test* button.

Python module {#python}
-------------

If there is a Boks plug-in in your OpenSesame experiment, the `boks` can be accessed as `exp.boks`:

{% highlight python %}
# Collect a response time with a 2000ms timeout
exp.boks.set_timeout(2000)
t1 = self.time()
button, t2 = exp.boks.get_button_press()
exp.set('response', button)
exp.set('response_time', t2-t1)
{% endhighlight %}

{% include doc/libboks %}

Serial port communication {#serial}
-------------------------

If you are using software that cannot make use the Boks Python module, you can interact directly with the Boks through via the serial port. Communication occurs by sending a single command byte to the Boks. Depending on the command, the command byte should be followed by one or more bytes that serve as parameters. Depending on the command, the Boks responds by sending zero or more bytes in response. The command bytes are indicated in decimal notation in the square brackets.

#### Timestamps

All timestamps are in microseconds. Only the `CMD_WAIT_SLEEP` command will fall back to millisecond precision when the timeout has been set to more than 16 milliseconds.

#### Serial port settings

The Boks is connected via USB as a virtual serial port device. The baudrate is `115200`.

#### `CMD_RESET` [001]

Resets the Boks to the initial state.

#### `CMD_IDENTIFY` [002]

Returns a sequence of 21 bytes, which should be interpreted as two ASCII strings. The first string is 5 bytes and contains the firmware version of the Boks. The second string is 16 bytes and contains the model description, optionally right-padded with whitespace.

Return example:

	'0.1.0dev.boks        '

#### `CMD_WAIT_PRESS` [003]

A single byte that corresponds to the button that is pressed, i.e. `1`, `2`, `3`, or `4`. If a timeout occurs (see `CMD_SET_TIMEOUT`), `255` is returned. Depending on whether the device is in continuous or discontinuous mode (see `CMD_SET_CONTINUOUS`), pressed buttons are returned immediate (continuous) or only buttons that are pressed after the command has been sent are returned (discontinuous)

#### `CMD_WAIT_RELEASE` [004]

Returns a single byte that corresponds to the button that is released. For more information, see `CMD_WAIT_PRESS`.

#### `CMD_WAIT_SLEEP` [005]

Waits for the interval specified by `CMD_SET_TIMEOUT`.

#### `CMD_BUTTON_STATE` [006]

Returns a single byte that contains the state for each of the buttons. The first bit (rightmost) indicates the state of the first button, the second bit indicates the state of the second button, etc.

Return example (binary):

	00001111 # All buttons pressed
	00000010 # Button 2 pressed

#### `CMD_SET_T1` [007]

Sets the `T1` (Timestamp 1) of the Boks to the current time in microseconds, as measured by the Boks' internal clock. Does not return a value.

#### `CMD_SET_T2` [008]

Sets the `T2`. For more information, see `CMD_SET_T1`.

#### `CMD_SET_TIMEOUT` [009]

Sets the timeout value, which is used by `CMD_WAIT_PRESS`, `CMD_WAIT_RELEASE`, and `CMD_SLEEP`. The command byte should be followed by an unsigned long (4 bytes) that indicates the timeout in microseconds. The value `0` disables the timeout.

#### `CMD_SET_BUTTONS` [010]

Sets the buttons that should be polled by `CMD_WAIT_PRESS` and `CMD_WAIT_RELEASE`. The command byte should be followed by a single byte that indicates which buttons should be pressed. The first (rightmost) bit corresponds to the first button, etc. To prevent deadlocks, you cannot turn off all buttons. If you try do this, by sending a 0-byte, all buttons will be switched on instead.

Parameter example (binary):

	00001111 # Poll all buttons
	00000011 # Only poll buttons one and two
	00000000 # Turn on all buttons (special case!)

#### `CMD_GET_T1` [011]

Returns `T1` as an unsigned long (4 bytes).

#### `CMD_GET_T2` [012]

Returns `T2` as an unsigned long (4 bytes)

#### `CMD_GET_TD` [013]

Returns the difference between `T2` and `T1` (`T2` – `T1`) as an unsigned long (4 bytes).

#### `CMD_GET_TIME` [014]

Returns the current time according to the Boks' internal clock as an unsigned long (4 bytes).

#### `CMD_GET_TIMEOUT` [015]

Returns the timeout value as set by `CMD_SET_TIMEOUT` as an unsigned long (4 bytes).

#### `CMD_GET_BUTTONS` [0016]

Returns the active buttons as set by `CMD_SET_BUTTONS` as a single byte. For more information, see `CMD_SET_BUTTONS`.

#### `CMD_LED_ON` [18]

Turns the led on.

#### `CMD_LED_OFF` [19]

Turns the led off.

Source code {#source}
-----------

The source code of the Boks firmware, Python module, and OpenSesame plug-in can be found at:

- <https://github.com/smathot/boks>

Timing {#timing}
------

##### More detailed benchmarks will be made available at a later date.

The Boks is able to record responses with sub-millisecond precision. The graph below shows the response time to a continuously pressed button, which indicates the minimum response latency. The average response latency when measured like this is, on this particular system, around 90 microseconds. There are some outliers, but even these are well in the sub-millisecond range.

![](/img/fig/fig19.1.4.png)

Test your own system {#test}
--------------------

##### More detailed test instructions will be made available at a later date.

You can perform the test shown above using the `unittest` script included with the Boks source code and running the `latency` test:

	./unittest latency
	
You can run the full test suite with the following command:

	./unittest led buttons photodiode latency commspeed
	
Furthermore, you can test your Boks in OpenSesame using the `boks_test.opensesame` file included with the Boks source code.

Update firmware {#firmware}
---------------

To update the firmware, load the `boks.ino` sketch, which is included with the Boks source code, and upload it to the Boks using the Arduino IDE.

For more information, please refer to the Arduino site:

- <http://arduino.cc/en/Guide/Environment>

[arduino]: http://arduino.cc/
