---
permalink: /checkbox-functions/
group: Forms
level: 1
layout: osdoc
title: Checkbox functions
sortkey: 006.008
---

The checkbox widget is a checkable box accompanied by a string of text.

Defining a checkbox widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 checkbox group="group" text="Option 1"
	widget 0 1 1 1 checkbox group="group" text="Option 2"

Defining a checkbox widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
checkbox1 = widgets.checkbox(form, text='Option 1', group='group')
checkbox2 = widgets.checkbox(form, text='Option 2', group='group')
form.set_widget(checkbox1, (0,0))
form.set_widget(checkbox2, (0,1))
{% endhighlight %}

{% include doc/checkbox %}