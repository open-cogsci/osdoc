---
layout: osdoc
title: Synth functions
group: Python inline code
permalink: /synth-functions/
---

The `synth` class provides basic sound synthesis functionality. For example, the following script generates a simple sound and plays it:

{% highlight python %}
from openexp.synth import synth
my_synth = synth(exp, osc='saw', freq='b2', attack=250, length='500')
my_synth.play()
{% endhighlight %}

{% include doc/synth %}