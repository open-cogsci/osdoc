title: Installing plugins and extensions

To install a plug-in or extension, simply copy the plug-in/ extension folder to one of the folders that OpenSesame scans for plug-ins and extensions.

Under Windows, you can place plug-ins in the following folders:

	[opensesame folder]\opensesame_plugins
	[drive]:\Documents and Settings\[user name]\.opensesame\opensesame_plugins

Under Windows, you can place extensions in the following folders:

	[opensesame folder]\opensesame_extensions
	[drive]:\Documents and Settings\[user name]\.opensesame\opensesame_extensions

Under Linux you can place plug-ins in the following folders:

	/home/[user name]/.opensesame/opensesame_plugins
	/usr/share/opensesame/opensesame_plugins

Under Linux you can place extensions in the following folders:

	/home/[user name]/.opensesame/opensesame_extensions
	/usr/share/opensesame/opensesame_extensions

So let's assume that you are running Windows, that the OpenSesame folder is `c:\Program Files\opensesame`, and that you want to install the SRBox plugin. In this case, you simply copy the `srbox` folder to the `plugins` directory of OpenSesame, so you get the following folder structure:

	c:\Program Files\opensesame\opensesame_plugins\srbox
