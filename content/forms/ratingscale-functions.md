---
permalink: /ratingscale-functions/
group: Forms
layout: osdoc
title: Rating_scale functions
---

The rating_scale widget is a horizontally aligned series of checkable boxes (nodes), optionally with a label attached to each node.

Defining a rating_scale widget in OpenSesame script using the form_base plug-in:

	widget 0 0 1 1 label text="I like fluffy kittens"
	widget 0 1 1 1 rating_scale var="response" nodes="Agree;Don't know;Disagree"

Defining a rating_scale widget with Python inline code:

{% highlight python %}
from libopensesame import widgets
form = widgets.form(self.experiment)
label = widgets.label(form, text='I like fluffy kittens')
rating_scale = widgets.rating_scale(form, nodes=['Agree', "Don't know", 'Disagree'], var='response')
form.set_widget(label, (0,0))
form.set_widget(rating_scale, (0,1))
form._exec()
{% endhighlight %}

{% include doc/rating_scale %}