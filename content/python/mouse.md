---
layout: osdoc
title: Mouse functions
group: Python inline code
permalink: /mouse/
---

The `mouse` class is used to collect mouse input. For example, the following script lets you move around a fixation dot with the mouse until a button is clicked:

{% highlight python %}
from openexp.mouse import mouse
from openexp.canvas import canvas
my_mouse = mouse(exp)
my_canvas = canvas(exp)
while True:
	button, position, timestamp = my_mouse.get_click(timeout=20)
	if button != None:
		break
	pos, time = my_mouse.get_pos()
	my_canvas.clear()
	my_canvas.fixdot(pos[0], pos[1])
	my_canvas.show()
{% endhighlight %}

*Important note:* When using a `mouse` all coordinates are specified relative to the top-left of the display, and not, as in `sketchpad`s, relative to the display center. For example, the following script will determine the deviation of a mouse click relative to the display center.

{% highlight python %}
from openexp.mouse import mouse
from math import sqrt
# Determine coordinates of display center
xc = self.get('width')/2
yc = self.get('height')/2
# Create a mouse object and collect a click
my_mouse = mouse(exp, visible=True)
button, position, timestamp = my_mouse.get_click()
# Unpack the position tuple into x and y coordinates
x, y = position
# Use Pythagoras to determine the distance to the display center
click_err = sqrt( (x-xc)**2 + (y-yc)**2 )
exp.set('click_err', click_err)
{% endhighlight %}

{% include doc/mouse %}
