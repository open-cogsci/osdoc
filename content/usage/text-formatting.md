---
layout: osdoc
title: Text formatting (HTML subset)
group: Usage
permalink: /text-formatting/
---

The easiest way to specify the appearance of your text is with the font-selection boxes in the graphical interface:

:--
cmd: figure
src: font-selection-box.png
caption: The font-selection box.
--:

However, if you need more flexibility you can use a subset of HTML tags, which you can simply insert into your text. You can use these tags everywhere: In sketchpad items, in inline_scripts (provided you use the openexp.canvas class), in forms, etc.

Example:

{% highlight html %}
OpenSesame supports a sub-set of HTML tags:
- <b>Bold face</b>
- <i>Italic</i>
- <u>Underline</u>

In addition, you can pass 'color', 'size', and 'style' as keywords to a 'span' tag:
- <span color="red">Color</span>
- <span size="32">Font size</span>
- <span style="serif">Font style</span>

Finally, you can force newlines with the 'br' tag:
Line 1<br>Line 2
{% endhighlight %}

The text above will be rendered as shown below: (The exact appearance depends on your default colors, font, etc.)

:--
cmd: figure
src: form-example.png
caption: Using (a subset of) HTML, you can define the appearance of your text.
--: