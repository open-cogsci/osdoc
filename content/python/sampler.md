---
layout: osdoc
title: Sampler functions
group: Python inline code
permalink: /sampler/
---

The `sampler` module provides functionality to play sound samples in .ogg and .wav format (Audacity is an excellent free tool to convert samples from other formats). For example, the following script plays the sample 'bark.ogg', which it retrieves from the file pool using `exp.get_file()`:

{% highlight python %}
from openexp.sampler import sampler
my_sampler = sampler(exp, exp.get_file('bark.ogg'))
my_sampler.play()
{% endhighlight %}

{% include doc/sampler %}