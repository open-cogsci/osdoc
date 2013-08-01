---
layout: osdoc
title: Triggers for EEG/ ERP
group: Devices
permalink: /triggers/
level: 1
sortkey: 009.005
---

In EEG/ ERP studies it is common to send triggers to mark the time of significant events (e.g., the onset of a trial, presentation of a particular stimulus, etc.). Triggers are typically bytes that are sent via the parallel port to the EEG apparatus. This post shows how to send triggers using the parallel port trigger plugin.
This plugin works in both linux and windows. In Windows `DLPortIO.dll` is used to access the parallel port. You can download the plugin from:

Linux:

In linux we have to use parport_pc. We can accomplish this by exectuting the following cmds:

$ sudo rmmod lp
$ sudo rmmod parport_pc
$ sudo modprobe parport_pc
$ sudo adduser user lp


Windows:

If you use a 32 bit system (typical for Windows XP), you can download a copy [here][win32-dll]. The .dll is located in the folder `DriverLINX/drivers` inside the .zip archive. If you use a 64 bit system (typical for Windows 7), you can download a copy [here][win64-dll].

For Windows XP x86




For Windows 7 x64:

1) Download the DLPortIO x64 driver from http://real.kiev.ua/avreal/download/#DLPORTIO_TABLE and uncompress the zip archive.

2) As Windows 7 has a strengthened security system (at least compared to XP) one cannot simply install the DLPortIO x64 driver. This won't work as Windows 7 will block all attempts of installing a not officially signed (by Microsoft) driver. Good for the security of an average user -- bad for us.

To bypass this restriction one has to use a little helper program called "Digital Signature Enforcement Overrider" (DSEO) which can be downloaded here: http://www.ngohq.com/home.php?page=dseo (of course there are other possible ways to do this but this program is mentioned in the DLPortIO-64-readme.txt and one does not have to dive deeper into MS Windows 7 architecture specialities).

3) Start DSEO with administrator privileges (right click on dseo13b.exe, select "run as administrator"). Now the DSEO window pops up. It just presents a list of options which operation to run next.

4) Choose the option "sign driver/sys-file" and press ok. Now another window appears where you have to type in the absolute path to the DLPortIO.sys file (only this one, not the dll!). Remember to escape spaces in the path if you have any (don't ask how long that took me) otherwise your files will not be found. Pressing ok will sign the sys-file.

5) Back in the DSEO list choose "enable test mode" and press ok. Then choose "exit" and restart your PC. (Windows 7 wrongly complains that DSEO might not be installed correctly -- just click on "yes, the software is installed correctly").

6) After boot up is completed you'll see that something like "Windows 7 test mode built #number#" is written on the desktop just above the clock in the starter-bar. That's necessary. You have to be in test mode to run this unofficially signed driver.

7) Now run DLPortIO_install.bat with administrator privileges (in Windows Explorer, right click the file, ...). Answer "yes" if Windows warns you about registry changes.

8) Reboot

9) Copy the DLPortIO.dll file to the folder containing opensesame.exe.



You need to copy `dlportio.dll` to the OpenSesame folder (that is, the same folder that contains `opensesame.exe`).

Step 2: Install dlportio drivers on your system
-----------------------------------------------

In order for dlportio.dll to work, a driver has to be installed on your system. An installer (`install.exe`) is included in the .zip archive (see step 1), in the folder `install`. For some reason, you need to copy `dlportio.dll` and `dlportio.sys` to the install folder before the running the installer. Depending on your version of Windows, you may or may not have to deal with security issues (see troubleshooting below).



Note that this send the trigger 1 to port 0x378 (=888). Change these values according to your set-up.

Recommendations:

Start your experiment with a zero trigger to reset the port. 


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
