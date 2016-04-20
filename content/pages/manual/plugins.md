title: Installing plugins and extensions
uptodate: false

Installation simply consists of copying the plug-in/ extensions folder into one of the folders that OpenSesame searches for plug-ins and extensions. Note that you need to unpack the .zip files first! A number of plug-ins and extensions are included by default with OpenSesame, so if you're unsure you can see how they are organized and organize the new plug-in/ extension in the same way.

Under Windows, you can place plug-ins in the following folders:

	[opensesame folder]\plugins
	[drive]:\Documents and Settings\[user name]\.opensesame\plugins

Under Windows, you can place extensions in the following folders:

	[opensesame folder]\extensions
	[drive]:\Documents and Settings\[user name]\.opensesame\extensions

Under Linux you can place plug-ins in the following folders:

	/home/[user name]/.opensesame/plugins
	/usr/share/opensesame/plugins

Under Linux you can place extensions in the following folders:

	/home/[user name]/.opensesame/extensions
	/usr/share/opensesame/extensions

So let's assume that you are running Windows, that the OpenSesame folder is `c:\Program Files\opensesame`, and that you want to install the SRBox plugin. In this case, you simply copy the `srbox` folder to the `plugins` directory of OpenSesame, so you get the following folder structure:

	c:\Program Files\opensesame\plugins\srbox
