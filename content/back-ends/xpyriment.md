---
layout: osdoc
title: Xpyriment
group: Back-ends
permalink: /xpyriment/
---

The xpyriment back-end is built on top of [Expyriment][], a library that has been designed specifically for creating cognitive and neuroscientific experiments. It is a light-weight hardware-accelerated back-end with excellent timing properties. If you care about temporal precision, but do not plan on generating complex stimuli (i.e. Gabor patches, random-dot gratings, etc.) xpyriment is a good choice.

Using Expyriment directly
-------------------------

You can find extensive documentation on Expyriment at <http://www.expyriment.org/doc>. The following code snippet shows a line of text:

~~~ .python
from expyriment import stimuli
text = stimuli.TextLine('This is expyriment!')
text.present()
~~~

Installing Expyriment on Ubuntu
-------------------------------

Ubuntu users can install Expyriment from the Cogsci.nl PPA:

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install expyriment

Citation
--------

Although Expyriment is bundled with the binary distributions of OpenSesame, it is a separate project. When appropriate, please provide the following citation in addition to citing OpenSesame:

Krause, F., & Lindemann, O. (in press). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*.
{: .reference}

[expyriment]: http://www.expyriment.org
