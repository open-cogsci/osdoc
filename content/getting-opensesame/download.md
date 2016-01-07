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

## Install on Mac OS {#macos}

We are looking for someone to improve and maintain the Mac OS packages for OpenSesame!
{: .page-notification}

Support for Mac OS is experimental. Instructions for running OpenSesame from source on Mac OS can be found [here][macos-running-from-source].

The latest version of the OpenSesame app has been composed on OS X Yosemite (10.10). Initial tests have shown that the app also appears to run well on Mavericks (10.9). If you experience problems starting or using the app when you have an OS X version older than Mavericks, we recommend you to upgrade to a newer version of OS X (after all, Mavericks and Yosemite are both free) or use one of the older releases of OpenSesame for Mac.

A caveat of the OpenSesame app is that the multiprocess implementation is not yet working (this does work well if you run OpenSesame from source). We hope to have this fixed in one of the next releases, but for now you will have to stick to the inprocess runner (go to <http://osdoc.cogsci.nl/miscellaneous/runners/> to see what this means).

- [OpenSesame 2.9.6 (.dmg)][macos-package-2.9.6]
- [OpenSesame 2.9.7 (.dmg)][macos-package-2.9.7]

Older versions can be found here:

- [OpenSesame 0.27.4 64bit][macos-package-0.27.4-64bit] (without Psychopy backend)
- [OpenSesame 0.27.4 32bit][macos-package-0.27.4-32bit] (including PsychoPy backend)
- [OpenSesame 0.26][macos-package-0.26] (should run on OS X versions (< 10.8))

For other OS X versions of OpenSesame refer to <http://www.cogsci.nl/dschreij/opensesame-mac/>.

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
