---
layout: osdoc
title: Canvas functions
group: Python inline code
permalink: /canvas/
---

The `canvas` class is used for display presentation. For example, the following script creates a canvas, draws a fixation dot and shows the canvas:

{% highlight python %}
from openexp.canvas import canvas
my_canvas = canvas(exp)
my_canvas.fixdot()
my_canvas.show()
{% endhighlight %}

*Important note:* When using a `canvas` all coordinates are specified relative to the top-left of the display, and not, as in `sketchpad`s, relative to the display center. For example, the following script will draw an arrow from the top-left to the display center.

{% highlight python %}
from openexp.canvas import canvas
my_canvas = canvas(exp)
# Top left
fromX = 0
fromY = 0
# Center
toX = my_canvas.xcenter()
toY = my_canvas.ycenter()
# Draw arrow from top-left to center
my_canvas.arrow(fromX, fromY, toX, toY)
my_canvas.show()
{% endhighlight %}

{% include doc/canvas %}
