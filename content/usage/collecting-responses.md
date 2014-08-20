---
layout: osdoc
title: Collecting responses
group: Usage
permalink: /collecting-responses/
---

%--
toc:
 mindepth: 2
--%

## Response items

The two primary response items are:

- `keyboard_response` (to collect key presses)
- `mouse_response` (to collect mouse clicks)

In addition, all items that have a duration can be used as simplified response items. By setting duration to 'keypress' an item functions as a basic `keyboard_response` item. By setting duration to 'mouseclick' an item functions as a basic `mouse_response` item.

Finally, certain plug-ins, such as the `srbox`, can also be used to collect responses. In general, these plug-ins should behave as described above, but for detailed information see the documentation of the specific plug-in.

## Response variables

All response items store responses in more-or-less the same way. A description of response-related variables can be found here:
	
- [usage/variables-and-conditional-statements]
	
## Finding out key names

Many keys have obvious names. For example, the 'a' key is called 'a'. But sometimes the name is ambiguous, such as in the case of the Control key, which may be called `control` or `ctrl`. There are a few ways to find out what a key is called. First, for `keyboard_response` items, you can click on the 'List available keys' button to find out which key names are available. This is a best guess of OpenSesame, which is usually accurate, but not guaranteed to be perfect. A foolproof way to find out what a key is called is to append a `feedback` item after your `keyboard_response` item, and print out the response (i.e. the key name) by adding something like the text: "You just pressed [response]"

Finally, key names may differ slightly between  back-ends. For example, the [xpyriment] backend uses the name "left shift", whereas the [psycho] back-end uses "lshift" to refer to the left shift button.

## Collecting responses using Python inline code

Responses can also be collected using Python inline code in `inline_script` items. This (usually) handled by the `openexp.keyboard` and `openexp.mouse` modules. For documentation and examples, see the respective documentation pages:

- [python/keyboard]
- [python/mouse]

[usage/variables-and-conditional-statements]: /usage/variables-and-conditional-statements
[python/keyboard]: /python/keyboard
[python/mouse]: /python/mouse
[xpyriment]: /back-ends/xpyriment
[psycho]: /back-ends/psycho
