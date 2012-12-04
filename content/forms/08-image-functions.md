---
layout: osdoc
title: Image functions
group: Forms
permalink: /image-functions/
level: 1
sortkey: 006.008
---

The image widget is used to display a non-interactive image.

Defining an image widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 image path='5.png'

Defining an image widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
# The full path to the image needs to be provided.
# self.experiment.get_file() can be used to retrieve the full path
# to an image in the file pool.
image = widgets.image(form, path=self.experiment.get_file('5.png'))
form.set_widget(image, (0,0))
form._exec()
{% endhighlight %}

{% include doc/image %}