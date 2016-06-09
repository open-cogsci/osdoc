title: Creating custom forms

If forms are slow, see [this page](%link:manual/forms/performance%).
{: .page-notification}

[TOC]

## About forms, geometries, and widgets

A form is a set of widgets (buttons, labels, text-input fields, etc.) arranged into a grid with a particular geometry. In the image below you see an example of a 2 (columns) × 3 (rows) form. A form geometry is simple, and consists of the following properties:

- *margins* ensure that the widgets do not touch the edge of the display. You can have different margins for the top, right, bottom, and left.
- *spacing* ensure that the widgets do not touch each other. The horizontal and vertical spacing is the same.
- There are one or more *rows*, possibly of different sizes.
- There are one or more *columns*, possibly of different sizes.

%--
figure:
 id: FigGeometry
 source: geometry.png
 caption: A schematic of FORM geometries.
--%

Of course, an empty form is no fun. So let's add the following widgets to create a simple question form:

- A `label` that spans the two columns of the top row. We use this label to give a title to the form.
- Another `label` that spans the two columns of the middle row. This label contains the actual question.
- A `button` in the bottom right widget area. This button allows the user to give the $0.05 response.
- Another `button` in the bottom left widget area. This button allows the user to give the $0.10 response.

%--
figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: A schematic example FORM.
--%

The images above are schematic examples. How this form actually looks in OpenSesame depends on your settings (notably your font and colors), but it may look something like this:

%--
figure:
 id: FigExample1
 source: example1.png
 caption: A example FORM.
--%

## Creating custom forms

There are two ways to create custom forms. You can:

- Use the FORM_BASE plugin, and specify your form using OpenSesame script.
- Use the `libopensesame.widgets` package and create your form using Python code. The Python way is slightly more flexible, but for most purposes both ways can be used.

### Creating forms using OpenSesame script

We will create the form described above using OpenSesame script. First, drag the FORM_BASE plugin into your experiment. Click on the newly created item to open its tab. Next, click on the 'Edit script' button (with the terminal icon), in the top-right of the tab area. This will open the script editor. Enter the following script to generate the form described above (see the comments for explanations).

~~~
# Margins are defined as "top;right;bottom;left". Each value corresponds to a
# margin in pixels.
set margins "50;100;50;100"

# The spacing is simply a value in pixels.
set spacing "25"

# The sizes of the rows are relative. "1;2;1" means that there are three rows,
# where the middle one is twice as large as the bottom and top ones. So "1;2;1"
# means exactly the same thing as "3;6;3". Please note that "3" does not mean
# that there are three equally-sized rows (but "1;1;1" does).
set rows "1;2;1"

# Columns are defined in the same way. "1;1" simply means that there
# are two columns of the same size.
set cols "1;1"

# Widgets are defined as follows:
# widget [column] [row] [column span] [row span] [widget type] [keywords]
#
# The columns and rows start counting at 0. If you do not want to have your widget
# span multiple columns and rows, you simply set the column and row span to 1.
widget 0 0 2 1 label text="Question"
widget 0 1 2 1 label center="no" text="A bat and a baseball together cost $1.10. The bat costs one dollar more than the ball. How much does the ball cost?"
widget 0 2 1 1 button text="$0.10"
widget 1 2 1 1 button text="$0.05"
~~~

### Creating forms using Python inline script

The exact same form can be created using an INLINE_SCRIPT and a bit of Python code. You will notice that the Python code somewhat resembles the OpenSesame script shown above. This is no wonder: The FORM_BASE plugin essentially translates the OpenSesame script into Python code.

First, drag an INLINE_SCRIPT into your experiment. Select the newly created item to open its tab, and add the following script into the Run phase of the INLINE_SCRIPT item (see the comments for explanations).

~~~ .python
# Import the widgets library
from libopensesame import widgets

# Create a form
form = widgets.form(exp, cols=[1,1], rows=[1,2,1],
	margins=(50,100,50,100), spacing=25)

# Create four widgets
labelTitle = widgets.label(form, text='Question')
labelQuestion = widgets.label(form,
	text='A bat and a baseball together cost $1.10. The bat costs one dollar more than the ball. How much does the ball cost?',
	center=False)
button5cts = widgets.button(form, text='$0.05')
button10cts = widgets.button(form, text='$0.10')

# Add the widgets to the form. The position in the form is indicated as a
# (column, row) tuple.
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))

# Execute the form! In this case, the form will return the text of the button that
# was clicked. This is one way to get a return value out of the form. Another way
# is to use the 'var' keyword, supported some of the widgets.
button_clicked = form._exec()
~~~

### Non-interactive forms

Usually, a form will have an input field, a button, or some other interactive element. However, you can also use forms without having any interactive element. To do this in OpenSesame script, you set `only_render` to "yes":

	set only_render "yes"

To this in a Python INLINE_SCRIPT, you call `form.render()`, instead of `form._exec()`.

### Themes

Forms support theming. Currently, two themes are available: 'gray' and 'plain'. The 'gray' theme is the default. Although the 'gray' theme is already quite plain, the 'plain' theme is even more basic. You can choose a theme like this in OpenSesame script:

	set theme plain

And by using the `theme` keyword in Python inline script:

~~~ .python
form = widgets.form(exp, theme='plain')
~~~

### Available widgets and keywords

The following widgets are available:

%--
figure:
 id: FigWidgets
 source: widgets.png
 caption: A list of available FORM widgets.
--%

You can define a widget using keywords. In Python inline code, you pass these keywords to the constructor of the widget class, like so:

~~~ .python
# text, frame, and var are keywords
button = widgets.button(form, text='Click me!', frame=True, var='response_variable')
~~~

In OpenSesame script, you list the keyword options after the widget type, like so:

	widget 0 0 1 1 button text='Click me!' frame='yes' var='response_variable

The keywords that are used when defining widgets in OpenSesame script are the same as those used in Python inline script, so you can rely on the Python documentation to see which keywords are available (see links below). However, there are a few things to keep in mind.

- If a keyword should be boolean (`True` or `False`) in Python, it should be 'yes' or 'no' in OpenSesame script.
- If a keyword requires a path name, you can directly enter the name of a file in the file pool. (Whereas in Python inline script you would have to use the `pool` object to accomplish this.)
- The keywords in OpenSesame script are the arguments to the `__init__()` function (the constructor) of the corresponding Python class. Only the arguments that are listed as 'Keyword arguments' are valid keywords.

Click on the links below to see a full description of keywords and functions (Python API):

- [Button](%link:manual/forms/widgets/button%)
- [Checkbox](%link:manual/forms/widgets/checkbox%)
- [Image](%link:manual/forms/widgets/image%)
- [Image_button](%link:manual/forms/widgets/image_button%)
- [Label](%link:manual/forms/widgets/label%)
- [Rating_scale](%link:manual/forms/widgets/rating_scale%)
- [Text_input](%link:manual/forms/widgets/text_input%)
- [Form](%link:manual/forms/widgets/form%)

## Another example

The following OpenSesame script (in a form_base plugin) will produce a questionnaire of three rating scales plus a next button:

~~~
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="Indicate how much you agree with the following statements"
widget 0 1 1 1 label center="no" text="Forms are easy"
widget 1 1 1 1 rating_scale var="question1" nodes="Agree;Don't know;Disagree"
widget 0 2 1 1 label center="no" text="I like data"
widget 1 2 1 1 rating_scale var="question2" nodes="Agree;Don't know;Disagree"
widget 0 3 1 1 label center="no" text="I like questionnaires"
widget 1 3 1 1 rating_scale var="question3" nodes="Agree;Don't know;Disagree"
widget 0 4 2 1 button text="Next"
~~~

The following Python inline_script will produce the same questionnaire.

~~~ .python
from libopensesame import widgets
form = widgets.form(exp, cols=[1,1], rows=[1,1,1,1,1])
title = widgets.label(form,
	text='Indicate how much you agree with the following statement')
question1 = widgets.label(form, text='Forms are easy', center=False)
question2 = widgets.label(form, text='I like data', center=False)
question3 = widgets.label(form, text='I like questionnaires', center=False)
ratingScale1 = widgets.rating_scale(form, var='question1',
	nodes=['Agree', "Don't know", 'Disagree'])
ratingScale2 = widgets.rating_scale(form, var='question2',
	nodes=['Agree', "Don't know", 'Disagree'])
ratingScale3 = widgets.rating_scale(form, var='question3',
	nodes=['Agree', "Don't know", 'Disagree'])
nextButton = widgets.button(form, text='Next')
form.set_widget(title, (0,0), colspan=2)
form.set_widget(question1, (0,1))
form.set_widget(question2, (0,2))
form.set_widget(question3, (0,3))
form.set_widget(ratingScale1, (1,1))
form.set_widget(ratingScale2, (1,2))
form.set_widget(ratingScale3, (1,3))
form.set_widget(nextButton, (0,4), colspan=2)
form._exec()
~~~

The resulting form looks something like this. (The exact appearance depends on your font, colors, etc.)

%--
figure:
 id: FigExample2
 source: example2.png
 caption: Another example FORM.
--%
