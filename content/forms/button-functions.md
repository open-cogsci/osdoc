---
permalink: /button-functions/
group: Forms
layout: osdoc
title: Button functions
---

The button widget is a clickable text string, by default surrounded by a button-like frame.

Defining a button widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 button text='Click me!' center='yes' frame='yes' var='response'

Defining a button widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
button = widgets.button(form, text='Click me!', frame=True, center=True, var='response')
form.set_widget(button, (0,0))
form._exec()
{% endhighlight %}

{% include doc/button %}