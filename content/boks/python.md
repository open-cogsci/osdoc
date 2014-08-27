---
layout: osdoc
title: Python library
group: Boks
permalink: /python/
show: True
---

The Boks and documentation below is under development.
{: .page-notification}

If there is a Boks plug-in in your OpenSesame experiment, the `boks` can be accessed as `exp.boks` or `self.experiment.boks`:

{% highlight python %}
# Collect a response time with a 2000ms timeout
exp.boks.set_timeout(2000)
t1 = self.time()
button, t2 = exp.boks.get_button_press()
exp.set('response', button)
exp.set('response_time', t2-t1)
{% endhighlight %}

{% include doc/libboks %}
