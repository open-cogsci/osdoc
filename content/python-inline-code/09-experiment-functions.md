---
layout: osdoc
title: Experiment functions
group: Python inline code
permalink: /experiment-functions/
level: 1
sortkey: 005.009
---

The `experiment` object controls the flow of the experiment. If you are writing Python inline code,  there are a few functions in the experiment object that may be useful, mostly to `get` and `set` variables, and to retrieve files from the file pool. The `experiment` object is a property of the `inline_script` object, so you can access it as `self.experiment` in an inline_script. For convenience, you can also refer to it simply as `exp`. For example, the following script retrieves the full path to a file from the pool, shows it using a canvas, and stores the timestamp of the display presentation as `canvas_timestamp`, so it can be logged.

{% highlight python %}
from openexp.canvas import canvas
my_canvas = canvas(exp)
my_canvas.image(exp.get_file('my_image.png'))
timestamp = my_canvas.show()
exp.set('canvas_timestamp', timestamp)
{% endhighlight %}

{% include doc/experiment %}