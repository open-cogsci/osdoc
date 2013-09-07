---
layout: osdoc
title: Mouse functions
group: Python inline code
permalink: /mouse-functions/
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

{% include doc/mouse %}