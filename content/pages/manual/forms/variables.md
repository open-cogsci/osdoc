---
layout: osdoc
title: Form variables
group: Forms
permalink: /form-variables/
---

If you experience performance issues when using forms, see [this post](/forms/performance-issues-and-troubleshooting/).
{: .page-notification}

%--
toc:
 mindepth: 2
--%

## About form variables

When you present a form with multiple `checkbox`es, you generally want to know which `checkbox` the user has checked. Similarly, when you present a form with two `button`s, you want to know which `button` the user has clicked. This information is available through variables that are automatically set when the user interacts with a form. You can specify yourself which response variables should be used. How this is done depends on how you have created your form:

### In ready-made `form_*` plug-ins

When you use one of the ready-made form plug-ins, such as `form_text_input`, you can specify the name of the response variable directly in the plug-in controls.

### In custom forms

You can use the `var` keyword to indicate which variable should be used. For example, the following OpenSesame script, which you can enter into a `form_base` plug-in, indicates that the response from a `text_input` widget should be stored in a variable called `my_response_var`:
	
~~~
widget 0 0 1 1 text_input var="my_response_var"
~~~

The equivalent Python code is:
	
~~~ .python
my_widget = widgets.text_input(form, var='my_response_var')
~~~

## Widget-specific notes

Each widget uses its response variable in a slightly different way.

### button

The `button` widget sets the response variable to 'yes' if it has been clicked and to 'no' if it has not.

### checkbox

The `checkbox` widget sets the response variable to a semicolon-separated list of the text on all checkboxes in the same group that have been checked, or 'no' if no `checkbox` has been checked. This sounds a bit complicated, so let's see a few examples.

~~~
widget 0 0 1 1 checkbox group="1" text="A" var="my_response_var"
widget 1 0 1 1 checkbox group="1" text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
~~~

Here there are two `checkbox`es with the text 'A' and 'B'. Both part of the same group, called '1'. Both have the same response variable, called `my_response_var`. If 'A' is checked, `my_response_var` will be 'A'. If 'B' is checked, `my_response_var` will be 'B'. If neither is checked, `my_response_var` will be 'no'. Note that only one `checkbox` in the same group can be checked, so `my_response_var` will *never* be 'A;B' in this example.

~~~
widget 0 0 1 1 checkbox text="A" var="my_response_var"
widget 1 0 1 1 checkbox text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
~~~

Now let's consider the same script, with the sole difference that the two `checkbox`es are not part of a group. In this case, the situation is much like described above, with the exception that both `checkbox`es can be checked at the same time, in which case `my_response_var` will be set to 'A;B'.

### image

Variables are not applicable to the `image` widget.

### image_button

The `image_button` widget sets the response variable to 'yes' if it has been clicked and to 'no' if it has not.

### label

Variables are not applicable to the `label` widget.

### rating_scale

The `rating_scale` widget sets the response variable to the number of the option that has been clicked, where '0' is the first option (zero-based indexing). If no option has been selected, the response variable is set to 'None'.

### text_input

The `text_input` widget sets the response variable to the entered text.
