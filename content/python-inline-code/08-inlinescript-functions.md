---
layout: osdoc
title: Inline_script functions
group: Python inline code
permalink: /inlinescript-functions/
level: 1
sortkey: 005.008
---

When you are using the inline_script item, you are essentially writing the body of two functions (`prepare` and `run`) of an `inline_script` object. The `inline_script` object has many more functions which you can use, and these are listed below. To use these functions, you use the `self.[function_name]` notation. For example:

{% highlight python %}
subject_nr = self.get("subject_nr")
{% endhighlight %}

or

{% highlight python %}
self.sleep(1000)
{% endhighlight %}

{% include doc/inline_script %}