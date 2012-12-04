---
layout: osdoc
title: Keyboard functions
group: Python inline code
permalink: /keyboard-functions/
level: 1
sortkey: 005.004
---

The `keyboard` class is used to collect keyboard responses. For example, the following script waits for a 'z' or 'x' key with a timeout of 3000ms:

{% highlight python %}
from openexp.keyboard import keyboard
my_keyboard = keyboard(exp, keylist=['z', 'x'], timeout=3000)
start_time = self.time()
key, end_time = my_keyboard.get_key()
self.experiment.set('response', key)
self.experiment.set('response_time', end_time - start_time)
{% endhighlight %}

{% include doc/keyboard %}