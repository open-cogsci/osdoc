---
layout: osdoc
title: Canvas functions
group: Python inline code
permalink: /python-inline-code/canvas-functions/
level: 1
sortkey: 004.003
---

The `canvas` class is used for display presentation. For example, the following script creates a canvas, draws a fixation dot and shows the canvas:

{% highlight python %}
from openexp.canvas import canvas
my_canvas = canvas(self.experiment)
my_canvas.fixdot()
my_canvas.show()
{% endhighlight %}

{% include doc/canvas %}