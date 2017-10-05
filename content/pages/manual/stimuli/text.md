title: Text

[TOC]

## How can I present text?

The most common way to show text is using a SKETCHPAD or FEEDBACK item. These allow you to enter text and other visual stimuli. For a questionnaire-like way to show text, you can use [forms](%link:manual/forms/about%).

__Note:__ The TEXT_DISPLAY plugin has been removed as of OpenSesame 3.0.0, because it was outdated and did not provide any functionality that is not offered by FORMs and SKETCHPAD items.
{: .page-notification}

## HTML formatting

You can use a HTML tags, which you can simply insert into your text. You can use these tags everywhere: In SKETCHPAD items, in INLINE_SCRIPTs (provided you use the `Canvas` class), in forms, etc.

__Note:__ Using `color`, `size`, and `style` directly as keywords in a `<span>` tag no longer works. This was invalid HTML, and has been deprecated as of OpenSesame 3.2. The example below shows the correct way to change the family (style), size, and color of text.
{: .page-notification}

Example:

~~~ .html
OpenSesame supports a sub-set of HTML tags:
- <b>Bold face</b>
- <i>Italic</i>
- <u>Underline</u>

In addition, you can pass 'color', 'size', and 'style' as keywords to a 'span' tag:
- <span style='color:red;'>Color</span>
- <span style='font-size:32;'>Font size</span>
- <span style='font-family:serif;'>Font style</span>

Finally, you can force newlines with the 'br' tag:
Line 1<br>Line 2
~~~


## Variables and inline Python

You can embed variables in text using the `[...]` syntax. For example, the following:

~~~ .python
The subject number is [subject_nr]
~~~

... might evaluate to (for subject 1):

~~~ .python
The subject number is 1
~~~

You can embed Python code using the `[=...]` syntax. For example, the following:

~~~ .python
The subject number modulo five is [=var.subject_nr % 5]
~~~

... might evaluate to (for subject 7)

~~~ .python
The subject number modulo five is 2
~~~

## Fonts

### Default fonts

You can select one of the default fonts from the font-selection dialogs (%FigFontSelect). These fonts are included with OpenSesame and your experiment will therefore be fully portable when you use them.

%--
figure:
 id: FigFontSelect
 source: font-selection-dialog.png
 caption: "A number of default fonts, which are bundled with OpenSesame, can be selected through the font-selection dialogs."
--%

The fonts have been renamed for clarity, but correspond to the following open-source fonts:

|__Name in OpenSesame__		|__Actual font__		|
|---------------------------|-----------------------|
|`sans`						|Droid Sans				|
|`serif`					|Droid Serif			|
|`mono`						|Droid Sans Mono		|
|`chinese-japanese-korean`	|WenQuanYi Micro Hei	|
|`arabic`					|Droid Arabic Naskh		|
|`hebrew`					|Droid Sans Hebrew		|
|`hindi`					|Lohit Hindi			|

### Selecting a custom font through the font-selection dialog

If you select 'other ...' in the font selection dialog, you can select any font that is available on your operating system. If you do this, your experiment is no longer fully portable, and will require that the selected font is installed on the system that you run your experiment on.

### Placing a custom font in the file pool

Another way to use a custom font is to put a font file in the file pool. For example, if you place the font file `inconsolata.ttf` in the file pool, you can use this font in a SKETCHPAD item, like so:

	draw textline 0.0 0.0 "This will be inconsolata" font_family="inconsolata"

Note that the font file must be a truetype `.ttf` file.
