---
layout: osdoc
title: Plug-in installation
group: Plug-ins
permalink: /installation/
---

Installation simply consists of copying the plug-in folder into one of the folders that OpenSesame searches for plug-ins. Note that you need to unpack the .zip files first! A number of plug-ins are included by default with OpenSesame, so if you're unsure you can see how these plug-ins are organized and organize the new plug-in in the same way.

Under Windows, you can place plug-ins in the following folders:

	[opensesame folder]\plugins
	[drive]:\Documents and Settings\[user name]\.opensesame\plugins

Under Linux you can place plug-ins in the following folders:

	/home/[user name]/.opensesame/plugins
	/usr/share/opensesame/plugins

So let's assume that you are running Windows, that the OpenSesame folder is `c:\Program Files\opensesame`, and that you want to install the SRBox plugin. In this case, you simply copy the `srbox` folder to the `plugins` directory of OpenSesame, so you get the following folder structure:

	c:\Program Files\opensesame\plugins\srbox