---
layout: osdoc
title: Download
group: Getting OpenSesame
permalink: /download/
---

## Recommended downloads

{% include recommended-downloads %}

## Other download options

The latest $status$ version of OpenSesame is $version$ *$codename$*, released on $release-date$ ([release notes]).

{% include downloads %}

## Install on Ubuntu/ Linux Mint {#ubuntu}

OpenSesame is available through the [Cogsci.nl PPA]. To add this repository to your software sources and install OpenSesame, run the following commands in a terminal:

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install opensesame

If you experience missing icons, please install the package `gnome-icon-theme-full`.

	sudo apt-get install gnome-icon-theme-full

## Install on other platforms

If there are no packages provided for your platform, you will need to run OpenSesame from source, as [per these instructions][running-from-source].

[archive]: http://files.cogsci.nl/software/opensesame/
[macos-package-0.26]: http://files.cogsci.nl/software/opensesame/opensesame_0.26-macos-2.zip
[macos-package-0.27.4-64bit]: http://www.cogsci.nl/dschreij/opensesame-mac/opensesame-0.27.4-macos-x86_64-1.dmg
[macos-package-0.27.4-32bit]: http://www.cogsci.nl/dschreij/opensesame-mac/opensesame-0.27.4-macos-i386-1.dmg
[macos-package-2.9.6]: http://asteria.psy.vu.nl/dbbschreij/opensesame/OpenSesame-2.9.6-osx.dmg
[macos-package-2.9.7]: http://asteria.psy.vu.nl/dbbschreij/opensesame/OpenSesame-2.9.7-osx-3.dmg
[macos-running-from-source]: /getting-opensesame/running-from-source#macos
[ppa-cogscinl]: https://launchpad.net/~smathot/+archive/cogscinl
[running-from-source]: /getting-opensesame/running-from-source
[neurodebian]: http://neuro.debian.net/
[python-portable]: /getting-opensesame/running-with-python-portable/
[release notes]: /notes/$version$
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl
[neurodebian]: http://neuro.debian.net/
