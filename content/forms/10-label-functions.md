---
layout: osdoc
title: Label functions
group: Forms
permalink: /label-functions/
level: 1
sortkey: 006.010
---

The label widget is a non-interactive string of text.

Defining a label widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 label text='My text'

Defining a label widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
label = widgets.label(form, text='My text')
form.set_widget(label, (0,0))
form._exec()
{% endhighlight %}

{% include doc/label %}