title: Form widgets and keywords


[TOC]


## Screenshot

%--
figure:
 id: FigWidgets
 source: widgets.png
 caption: A list of available FORM widgets.
--%


## Widgets and keywords

All keywords are optional, instead otherwise indicated.

### Form

The `cols` and `rows` keywords can either be single `int` values, in which case they specify the number of equally sized columns and rows, or lists of `int`, in which case they specify the relative sizes of each column and row. For more information about form geometry, see:

- %link:manual/forms/custom%

The `validator` keyword can be used to validate form input. For more information, see:

- %link:manual/forms/validation%

(In OpenSesame script, you do not need to explicitly create a form.)

Python script:

~~~ .python
form = Form(
	cols=2, rows=2, spacing=10, margins=(100, 100, 100, 100), theme=u'gray',
	timeout=None, clicks=False, validator=None
)
button = Button(text=u'Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### button / Button

OpenSesame script:

~~~
widget 0 0 1 1 button text="Click me!" center=yes frame=yes var=response
~~~

Python script:

~~~ .python
form = Form()
button = Button(text=u'Click me!', frame=True, center=True, var=u'response')
form.set_widget(button, (0, 0))
form._exec()
~~~


### checkbox / Checkbox

If a group is specified, checking one checkbox from that group will uncheck all other checkboxes from that group. Checkboxes that are part of a group cannot be unchecked, except by clicking on another checkbox in that group.

The `group` keyword also affects how variables are stored, as described here:

- %link:manual/forms/variables%

OpenSesame script:

~~~
widget 0 0 1 1 checkbox group=group text="Option 1"
widget 0 1 1 1 checkbox group=group text="Option 2"
~~~

Python script:

~~~ .python
form = Form()
checkbox1 = Checkbox(text=u'Option 1', group=u'group')
checkbox2 = Checkbox(text=u'Option 2', group=u'group')
form.set_widget(checkbox1, (0, 0))
form.set_widget(checkbox2, (0, 1))
form._exec()
~~~


### image / ImageWidget

The Python object is called `ImageWidget` to distinguish it from the `Image` canvas element.

OpenSesame script:

~~~
# Only path is a required keyword
widget 0 0 1 1 image path="my_image.png" adjust=yes frame=no
~~~

Python script:

~~~ .python
# Only path is a required keyword
form = Form()
image = ImageWidget(path=pool[u'my_image.png'], adjust=True, frame=False)
form.set_widget(image, (0, 0))
form._exec()
~~~


### image_button / ImageButton

The `image_id` keyword is used to identify the image button when it is clicked. If no `image_id` is provided, the path to the image is used as id.

OpenSesame script:

~~~
# Only path is a required keyword
widget 0 0 1 1 image_button path="my_image.png" adjust=yes frame=no image_id=my_image var=response
~~~

Python script:

~~~ .python
# Only path is a required keyword
form = Form()
image_button = ImageButton(
	path=pool[u'my_image.png'], adjust=True, frame=False,
	image_id=u'my_image', var=u'response'
)
form.set_widget(image_button, (0, 0))
form._exec()
~~~


### label / Label

OpenSesame script:

~~~
widget 0 0 1 1 label text="My text" frame=no center=yes
~~~

Python script:

~~~ .python
form = Form()
label = Label(text=u'My text', frame=False, center=True)
form.set_widget(label, (0,0))
form._exec()
~~~


### rating_scale / RatingScale

The `nodes` keyword can be an `int` or a semicolon-separated list of labels. If `nodes` is an `int`, it specified the number of (unlabeled) nodes.

The `default` keyword indicates which node number is selected by default, where the first node is 0.

OpenSesame script:

~~~
widget 0 1 1 1 rating_scale var=response nodes="Agree;Don't know;Disagree" click_accepts=no orientation=horizontal var=response default=0
~~~

Python script:

~~~ .python
form = Form()
rating_scale = RatingScale(
	nodes=[u'Agree', u"Don't know", u'Disagree'], click_accepts=False,
	orientation=u'horizontal', var='response', default=0
)
form.set_widget(rating_scale, (0, 0))
form._exec()
~~~


### text_input / TextInput

The `stub` keyword indicates placeholder text that is shown when no text has been entered. The `key_filter` keyword, available only in Python, specifies a function to filter key presses. This is described in more detail under:

- %link:manual/forms/validation%

OpenSesame script:

~~~
widget 0 0 1 1 text_input text="Initial text" frame=yes center=no stub="Type here …" return_accepts=yes var=response
~~~

Python script:

~~~ .python
form = Form()
text_input = TextInput(
		text=u'Initial text', frame=True, center=False, stub=u'Type here …',
		return_accepts=True, var=u'response', key_filter=my_filter_function
)
form.set_widget(text_input, (0, 0))
form._exec()
~~~
