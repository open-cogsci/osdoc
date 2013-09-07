---
permalink: /form-functions/
group: Forms
layout: osdoc
title: Form functions
---

The form is a container for widgets, such as labels, etc. If you use the form_base plug-in in combination with OpenSesame script, you do not need to explicitly create a form. However, if you use Python inline code, you do.

Defining a form with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
label = widgets.label(form, text='label)
form.set_widget(label, (0,0))
form._exec()
{% endhighlight %}

{% include doc/form %}