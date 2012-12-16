---
layout: osdoc
title: Choosing and configuring a system
group: Getting started
permalink: /choosing-and-configuring-a-system/
level: 1
sortkey: 003.007
---

When you are setting up a computer to run experiments, there are lots of choices to make. There is not a single "best" way, but here are a few pointers to get you started. Mostly derived from my personal experience, so feel free to correct and/ or complement this section.

Choosing software
-----------------

Since you're reading this there's a fair chance that you're considering OpenSesame for running your experiments. Good! But, of course, there are other options that you could consider. Hans Stransburger maintains [a very nice overview][strasburger] of available software.

Choosing a computer
-------------------

In my experience, any reasonably modern computer will do. A common misconception is that an expensive graphics card will improve the accuracy of your timing. It doesn't. An expensive graphics card is only useful if you plan on generating stimuli on the fly, and even then only if the software makes use of hardware acceleration. In the case of OpenSesame, hardware acceleration is used by the psycho and xpyriment back-ends, but not by the default legacy back-end. For most purposes, the built-in graphics card of your computer or laptop will do just fine.

Regarding the selection of a monitor: A common belief of questionably veracity is that TFT (flat-screen) monitors are not suitable for running experiments. It used to be that TFT displays had a slow response time and a long decay time, but that's not the case anymore, at least not always. There is a notable difference between TFT and CRT displays in the way that the display is refreshed, though, as can be seen in the video below (CRT in the middle):

<iframe src="http://player.vimeo.com/video/24216910?badge=0" width="640" height="160" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe> <p><a href="http://vimeo.com/24216910">High speed display refresh demonstration</a> from <a href="http://vimeo.com/smathot">Sebastiaan Mathot</a> on <a href="http://vimeo.com">Vimeo</a>.</p>

Choosing an operating system
----------------------------

This is very much a matter of preference. Right now, Windows 7 is [the most widely used operating system for running experiments][most-used] and it works pretty well. In our tests, Linux offers marginally better performance than Windows. A popular and free Linux distribution is [Ubuntu][], which is supported by OpenSesame and [NeuroDebian][].

OpenSesame is developed primarily on [Kubuntu][] 12.04.1 LTS.

Choosing an OpenSesame back-end
-------------------------------

In OpenSesame you can select the library that is used to handle display, sound and input operations. This is called the back-end. Back-ends are transparent, in the sense that you can run most experiments unchanged using any back-end. However, back-ends differ in their timing properties, and the functionality they offer in inline scripting.

For more information about the various back-ends, see [here][backends].

[strasburger]: http://www.hans.strasburger.de/psy_soft.html
[most-used]: http://www.cogsci.nl/blog/miscellaneous/205-what-operating-systems-do-experimental-psychologists-use
[ubuntu]: http://www.ubuntu.com/
[neurodebian]: http://neuro.debian.net/
[backends]: /back-ends
[kubuntu]: http://www.kubuntu.org/