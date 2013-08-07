---
permalink: /textinput-functions/
group: Forms
level: 1
layout: osdoc
title: Text_input functions
sortkey: 006.013
---

The text_input widget allows the participant to enter multi-character responses. (This widget has no relation to the text_input plug-in, which was created before forms where added to OpenSesame.)

Defining a text_input widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 text_input var='response' return_accepts='yes'

Defining a text_input widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
text_input = widgets.text_input(form, var='response', return_accepts=True)
form.set_widget(text_input, (0,0))
form._exec()
{% endhighlight %}

{% include doc/text_input %}