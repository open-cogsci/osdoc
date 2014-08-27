---
layout: osdoc
title: Legacy
group: Back-ends
permalink: /legacy/
---

The legacy back-end is built on top of [PyGame][] in non-OpenGL mode. The downside of this is that there is no hardware acceleration, and the timing properties are not as good as that of the psycho or xpyriment back-ends. The upside is that PyGame is very easy to use, very reliable, and well supported on a wide range of platforms.

Using PyGame directly
---------------------

PyGame is well documented and you can find everything you need to know about using PyGame on <http://www.pygame.org/docs/>. Specific to OpenSesame is the fact that the display surface is stored as `self.experiment.window` or simply `win`. So the following code snippet, which you could paste into an inline_script item, draws a red rectangle to the display:

{% highlight python %}
import pygame # Import the PyGame module
pygame.draw.rect(self.experiment.window, pygame.Color("red"),
	[20, 20, 100, 100]) # Draw a red rectangle. Not shown yet...
pygame.display.flip() # Update the display to show the red rectangle.
{% endhighlight %}

[pygame]: http://www.pygame.org/
