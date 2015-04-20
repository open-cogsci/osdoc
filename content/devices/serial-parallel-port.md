---
layout: osdoc
title: Serial and parallel port
group: Devices
permalink: /serial-parallel-port/
---

Some external devices are connected to the computer through the serial or parallel port or, as is increasingly common, through a USB connection that simulates a serial port.

%--
toc:
 mindepth: 2
--%

## Triggers

For sending triggers for ERP/EEG studies, see:
	
- [devices/triggers]

## Port_reader plug-in and inpout32.dll (Windows only)

If you are using a different type of input device, you can try using the port_reader plug-in, which is bundled with the Windows release. It simply reads from a port (serial or parallel) and waits for input. Depending on how your device works, port_reader may provide the required functionality. Unfortunately it is Windows only, because it depends on `inpout32.dll`.

In inline_script items, you can interface with `inpout32.dll` as well. This does not appear to be very well documented (please refer to Google), but here's an example script:

~~~ .python
from ctypes import windll
port = 889 # Port nr to read from. Names like COM1 etc do not appear to work
dev = windll.inpout32 # Init the device
val = dev.Inp32(port) # Read a value
print "Read %d from port %d" % (val, port)
~~~

## python-serial / python-parallel

PySerial is an easy to use Python library for serial port communications, which is bundled with all OpenSesame packages. PyParallel is a subproject of pySerial, but unfortunately it's not as straight-forward to use as its big brother. You can use pySerial/ pyParallel in inline_script items.

- For more information, see <http://pyserial.sourceforge.net/>

[devices/triggers]: /devices/triggers
