---
layout: osdoc
title: Triggers for EEG/ ERP
group: Devices
permalink: /triggers/
level: 1
sortkey: 009.005
---

In EEG/ ERP studies it is common to send triggers to mark the time of significant events (e.g., the onset of a trial, presentation of a particular stimulus, etc.). Triggers are typically bytes that are sent via the parallel port to the EEG apparatus. This post shows how to send triggers using `DLPortIO.dll`. Because this uses a .dll, it is (unfortunately) a Windows only solution.

Step 1: Put dlportio.dll in the right place
-------------------------------------------

If you use a 32 bit system (typical for Windows XP), you can download a copy [here][win32-dll]. The .dll is located in the folder `DriverLINX/drivers` inside the .zip archive. If you use a 64 bit system (typical for Windows 7), you can download a copy [here][win64-dll].

You need to copy `dlportio.dll` to the OpenSesame folder (that is, the same folder that contains `opensesame.exe`).

Step 2: Install dlportio drivers on your system
-----------------------------------------------

In order for dlportio.dll to work, a driver has to be installed on your system. An installer (`install.exe`) is included in the .zip archive (see step 1), in the folder `install`. For some reason, you need to copy `dlportio.dll` and `dlportio.sys` to the install folder before the running the installer. Depending on your version of Windows, you may or may not have to deal with security issues (see troubleshooting below).

Step 3: Add an initialization inline_script item
------------------------------------------------

Add an inline_script to the start of the experiment with the following code in the prepare phase:

{% highlight python %}
try:
	from ctypes import windll
	global io
	io = windll.dlportio # requires dlportio.dll !!!
except:
	print 'The parallel port couldnt be opened'
{% endhighlight %}

This will load `dlportio.dll` as a global object called `io`. Please note that failure will not crash the experiment, so make sure to check the debug window for error messages!

Step 4: Send a trigger
----------------------

You can now use the following code in an inline_script anywhere in the experiment to send a trigger:

{% highlight python %}
global io
trigger = 1
port = 0x378
try:
	io.DlPortWritePortUchar(port, trigger)
except:
	print 'Failed to send trigger!'
{% endhighlight %}

Note that this send the trigger 1 to port 0x378 (=888). Change these values according to your set-up.

Troubleshooting
---------------

There are a number of relevant forum topics in which trigger-related problems are discussed (and, for the most, solved!).

- A post with elaborate installation instructions for DLPortIO on Windows 7: [link][post-1]
- A post about ghost triggers, i.e. unwanted triggers that are mysteriously registered by the EEG apparatus: [link][post-2]

Please don't hesitate to post questions on the forum, or to let us know of your experiences (good or bad).

[win32-dll]: http://files.cogsci.nl/misc/dlportio.zip
[win64-dll]: http://real.kiev.ua/avreal/download/#DLPORTIO_TABLE
[post-1]: http://forum.cogsci.nl/index.php?p=/discussion/comment/745#Comment_745
[post-2]: http://forum.cogsci.nl/index.php?p=/discussion/comment/780#Comment_780