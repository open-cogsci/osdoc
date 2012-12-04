---
layout: osdoc
title: Development snapshots and pre-release packages
group: Getting started
permalink: /getting-the-latest-development-snapshot/
level: 1
sortkey: 003.006
---

If you want to have the latest features and don't mind potential instability, you can grab the latest experimental source code.

Pre-release packages
--------------------

Pre-release packages are created occasionally, especially as an official release draws near. Windows packages and source archives can be found [here][pre-release]

Ubuntu users can obtain the latest pre-release through the [opensesame-next PPA][ppa].

The latest source code
----------------------

### Using the GitHub website

The easiest way to obtain the latest snapshot, is by going to <https://github.com/smathot/OpenSesame> and clicking on the "Downloads" button (make sure you select one of the links at the top, not the previous releases that are listed below).

### Using git

Alternatively, you can use git to grab the latest source with the following command:

	git clone git://github.com/smathot/OpenSesame.git

By default, you will be in the `master` branch, which contains semi-stable code. For even more experimental code, you can switch to the `playground` branch, with the following command:

	git checkout playground

### Running the snapshot

Once you have obtained the source code, you can run it as described [here][run-source].

[pre-release]: http://files.cogsci.nl/software/opensesame/pre-releases/
[run-source]: /getting-started/running-from-source
[ppa]: https://launchpad.net/~smathot/+archive/opensesame-next