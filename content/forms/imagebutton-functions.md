---
permalink: /imagebutton-functions/
group: Forms
layout: osdoc
title: Image_button functions
---

The image_button widget is a clickable image.

Defining an image_button widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 image_button path='5.png' var='response'

Defining an image_button widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
# The full path to the image needs to be provided.
# self.experiment.get_file() can be used to retrieve the full path
# to an image in the file pool.
image_button = widgets.image_button(form, path=self.experiment.get_file('5.png'), var='response')
form.set_widget(image_button, (0,0))
form._exec()
{% endhighlight %}

{% include doc/image_button %}