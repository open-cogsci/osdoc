---
layout: osdoc
title: Xpyriment
group: Back-ends
permalink: /xpyriment/
level: 1
sortkey: 008.003
---

The xpyriment back-end is built on top of [Expyriment][], a library that has been designed specifically for creating psychological experiments. It is a light-weight hardware-accelerated back-end with excellent timing properties. If you care about temporal precision, but do not plan on generating complex stimuli (i.e. Gabor patches, random-dot gratings, etc.) xpyriment is a good choice.

Using Expyriment directly
-------------------------

You can find extensive documentation on Expyriment at <http://code.google.com/p/expyriment/>. The following code snippet shows a line of text:

{% highlight python %}
from expyriment import stimuli
text = stimuli.TextLine('This is expyriment!')
text.present()
{% endhighlight %}

Citation
--------

Although Expyriment is bundled with the binary distributions of OpenSesame, it is a separate project. When appropriate, please provide the following citation in addition to citing OpenSesame:

###### Krause, F., & Lindemann, O. (2012). Expyriment (Version 0.5.2) [Software]. Available from <http://code.google.com/p/expyriment/>

[expyriment]: http://code.google.com/p/expyriment/