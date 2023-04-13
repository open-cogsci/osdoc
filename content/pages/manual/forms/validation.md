title: Validating form input


To validate a form, pass a function with the `validator` keyword to `Form()`. In the example below, `my_form_validator()` is used in this way. A validator function should not expect any arguments, and should return a `bool` to indicate whether or not the form validates. If the form does not validate, no error message is shown, but the form simply stays open.

In addition, you can validate (or filter) input to a `TextInput` widget to exclude certain characters as input. To do so, pass a function with the `key_filter` keyword to `TextInput()`. In the example below, `filter_digits()` is used in this way. A key-filter function should accept a single argument, which corresponds to a single key press, and should return a `bool` to indicate whether or not the key is accepted as input.

~~~ .python
def my_form_validator():
    """Checks whether both the gender and age fields have been filled out"""
    return gender != 'no' and age != ''


def filter_digits(ch):
    """Allows only digit characters as input"""
    return ch in '0123456789'


# Define all widgets
button_ok = Button(text='Ok')
label_gender= Label('Your gender')
checkbox_male = Checkbox(text='Male', group='gender', var='gender')
checkbox_female = Checkbox(text='Female', group='gender', var='gender')
label_age = Label('Your age')
# Specify a key filter so that only digits are accepted as text input
input_age = TextInput(stub='Age here …', var='age', key_filter=filter_digits)
# Build the form. Specify a validator function to make sure that the form is
# completed.
my_form = Form(validator=my_form_validator, rows=[1,1,1], cols=[1,1,1])
my_form.set_widget(label_gender, (0, 0))
my_form.set_widget(checkbox_male, (1, 0))
my_form.set_widget(checkbox_female, (2, 0))
my_form.set_widget(label_age, (0, 1))
my_form.set_widget(input_age, (1, 1), colspan=2)
my_form.set_widget(button_ok, (1, 2))
my_form._exec()
~~~
