---
layout: osdoc
title: Collecting responses
group: Usage
permalink: /collecting-responses/
---

Response items
--------------

The two primary response items are:

- *keyboard_response* (to collect key presses)
- *mouse_response* (to collect mouse clicks)

In addition, all items that have a duration can be used as simplified response items. By setting duration to 'keypress' an item functions as a basic keyboard_response item. By setting duration to 'mouseclick' an item functions as a basic mouse_response item. The following items have a duration (the list of plug-ins may be incomplete):

- *sketchpad*
- *feedback*
- *sampler*
- *synth*
- *text_display* (plug-in)
- *fixation_dot* (plug-in)

Finally, certain plug-ins, such as the 'srbox', can also be used to collect responses. In general, these plug-ins should behave as described above, but for detailed information, see the documentation of the specific plug-in.

Response variables
------------------

All response items store responses in more-or-less the same way. The following variables are set by response items:

|`response`					|contains the actual response. The type of response depends on the response item: It may be the name of a key, the number of a mouse button, a string of text, etc.|
|`response_time`				|contains the response time. The meaning of `response time` depends on the response item, but it is typically the interval between the start of the response interval and the first response that is received. If the start of the response interval has not been set explicitly, the onset of the response item is used.|
|`correct`					|indicates whether the response was correct. Specifically, `correct` is set to 1 if `response` matches `correct_response` and to 0 if it does not. `correct` is set to undefined if the `correct_response` variable has not been set.|

In addition, each of the variables above also exists with the suffix `_[item_name]` so that you can refer specifically to the response collected by a specific item. For example, the variable `response_second_item` is the response collected by the item called 'second_item'.

Another important variable is `correct_response`. This indicates the expected response, and is used to evaluate `correct` (as described above). Typically, you define `correct_response` along with the independent variables in your block loop.

Finding out key names
---------------------

Many keys have obvious names. For example, the 'a' key is called 'a'. But sometimes the name is ambiguous. There are a few ways to find out what a key is called. First, for keyboard_response items, you can click on the 'List available keys' button to find out which key names are available. This is a best guess of OpenSesame, which is usually accurate, but not guaranteed to be perfect. A foolproof way to find out what a key is called is to append a feedback item after your keyboard_response item, and print out the response (i.e. the key name) by adding something like the text: "You just pressed [response]"

Finally, key names may differ slightly between  back-ends. For example, the xpyriment backend uses the name "left shift", whereas the psycho back-end uses "lshift" to refer to the left shift button.

Collecting responses using Python inline code
---------------------------------------------

Responses can also be collected using Python inline code in inline_script items. This (usually) handled by the `openexp.keyboard` and `openexp.mouse` modules. For documentation and examples, see the respective documentation pages:

- [openexp.keyboard](/python-inline-code/keyboard-functions)
- [openexp.mouse](/python-inline-code/mouse-functions)
