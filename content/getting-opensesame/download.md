---
layout: osdoc
title: Download
group: Getting OpenSesame
permalink: /download/
---

<div class="recommended" markdown="1">

<script type="text/javascript">

var OSName="unknown OS";
if (navigator.appVersion.indexOf("Win") != -1) OSName="Windows";
if (navigator.appVersion.indexOf("Mac") != -1) OSName="MacOS";
if (navigator.appVersion.indexOf("Linux") != -1) OSName="Linux";
if (navigator.userAgent.toLowerCase().indexOf("android") != -1) OSName="Android";

var msg = "Unknown"

if (OSName == "Linux") {
	msg = "<p>You appear to be running Linux. The following download options are available for Linux:</p>"
		+ "<p class=\"button-debian\"><a href=\"#ubuntu\">Ubuntu/ Debian package</a></p>"
		+ "<p class=\"button-arch\"><a target=\"_blank\" href=\"https://aur.archlinux.org/packages/opensesame/\" >Arch Linux package</a></p>";
} else if (OSName == "Windows") {
	msg = "<p>You appear to be running Windows. The following download option is recommended:</p>"
		+ "<p class=\"button-winexe\"><a target=\"_blank\" href=\"$url-windows-exe$\" >Windows XP/Vista/7 installer (.exe)</a></p>";
} else if (OSName == "MacOS") {
	msg = "<p>You appear to be running Mac OS. Installation instructions can be found here:</p>"
		+ "<p class=\"button-macos\"><a href=\"#macos\">Mac OS package (.zip)</a></p>";
} else if (OSName == "Android") {
	msg = "<p>You appear to be running Android. Installation instructions can be found here:</p>"
		+ "<p class=\"button-android\"><a href=\"/getting-opensesame/android\">OpenSesame runtime for Android</a></p>";
} else {
	msg = "<p>No recommended download is available, because your operating system could not be recognized.</p>";
}

document.write(msg);

</script>

</div>

The latest $status$ version of OpenSesame is $version$ *$codename$*, released on $release-date$ ([release notes]). Older versions can be found [here][archive].

Installation instructions and more download options can be found below the download buttons.

{% include downloads %}

## Windows XP / Vista / 7

There are a number of ways to run OpenSesame under Windows:

- Use the automated installer (see link above). After installation, you can run OpenSesame from the start menu.
- Download the Windows portable .zip file (see link above) and extract it to a location of your choice.
- Download the WinPython-based package, which comes with a slightly different set of modules and offers more flexibility for advanced users. For more information, see [this article][python-portable].

## Ubuntu/ Debian/ Linux Mint {#ubuntu}

OpenSesame is available through [NeuroDebian] (for Debian, Ubuntu, Linux Mint, and other derivatives) and the [Cogsci.nl PPA] (Ubuntu only). The [Cogsci.nl PPA] generally has the most up-to-date version.

### Cogsci.nl PPA

To add the [Cogsci.nl PPA] to your software sources and install OpenSesame, run the following commands in a terminal:

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install opensesame

If you experience missing icons, please install the package `gnome-icon-theme-full`.

	sudo apt-get install gnome-icon-theme-full

### NeuroDebian

Instructions for adding [NeuroDebian] to your software sources can be found on the [NeuroDebian] website. Once you have done this, you can install OpenSesame by running the following commands in a terminal:

	sudo apt-get update
	sudo apt-get install opensesame

## Mac OS {#macos}

We are looking for someone to improve and maintain the Mac OS packages for OpenSesame!
{: .page-notification}

Support for Mac OS is experimental. Instructions for running OpenSesame from source on Mac OS can be found [here][macos-running-from-source].

The latest versions of OpenSesame (> 0.27.1) come in two *flavors*. One runs on 64-bit Python (from python.org) and of all its underlying packages were obtained by using the official distributables that are available from the developers' websites. Because psychopy is not able to run in a 64-bit Python environment (yet), this backend is not available in this version. The other version is completely built from the ground up with macports and is compiled in 32-bit. This version does contain the psychopy backend. Concerning their usage, there are no real noticable differences between these versions (except for the lack of the psychopy backend in one) and experiments created in one version should work perfectly in the other, so the decision of which one to use is completely up to you. (Upon initial testing, the 64-bit version seemed a bit more stable, but these tests were not really in-depth.)

Both versions have been built on *Mountain Lion* and, after initial tests on our systems, sadly did not seem to be backward compatible with older OS X versions. If they do work for you on pre-Mountain Lion macs, please let us know on [the forum](http://forum.cogsci.nl).

- [opensesame 0.27.4 64bit][macos-package-0.27.4-64bit] (without Psychopy backend)
- [opensesame 0.27.4 32bit][macos-package-0.27.4-32bit] (including PsychoPy backend)

An older version of OpenSesame which should run on all OS X versions (>10.6) can be found here:

- [opensesame_0.26-macos-2.zip][macos-package-0.26]

For other OS X versions of OpenSesame refer to <http://www.cogsci.nl/dschreij/opensesame-mac/>.

## Other platforms

If there are no packages provided for your platform, you will need to run OpenSesame from source, as [per these instructions][running-from-source].

[archive]: http://files.cogsci.nl/software/opensesame/
[macos-package-0.26]: http://files.cogsci.nl/software/opensesame/opensesame_0.26-macos-2.zip
[macos-package-0.27.4-64bit]: http://www.cogsci.nl/dschreij/opensesame-mac/opensesame-0.27.4-macos-x86_64-1.dmg
[macos-package-0.27.4-32bit]: http://www.cogsci.nl/dschreij/opensesame-mac/opensesame-0.27.4-macos-i386-1.dmg
[macos-running-from-source]: /getting-opensesame/running-from-source#macos
[ppa-cogscinl]: https://launchpad.net/~smathot/+archive/cogscinl
[running-from-source]: /getting-opensesame/running-from-source
[neurodebian]: http://neuro.debian.net/
[python-portable]: /getting-opensesame/running-with-python-portable/
[release notes]: /notes/$version$
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl
[neurodebian]: http://neuro.debian.net/
