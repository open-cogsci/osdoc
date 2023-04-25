title: 验证表单输入
hash: 8f257c66947b338bded5e3096f9fd8535d30a638ed3dda7124df22044e543a9d
locale: zh
language: Chinese

要验证表单，请将带有 `validator` 关键字的函数传递给 `Form()`。在下面的示例中，以这种方式使用了 `my_form_validator()`。验证器函数不应期望任何参数，并应返回一个 `bool` 以指示表单是否验证。如果表单未验证，将不显示错误消息，但表单仍会保持打开状态。

此外，您可以验证（或筛选）`TextInput` 小部件的输入，以排除某些字符作为输入。要这样做，请使用 `key_filter` 关键字将函数传递给 `TextInput()`。在下面的示例中，以这种方式使用了 `filter_digits()`。键筛选器函数应接受一个参数，该参数对应于单个按键，应返回一个 `bool` 以表示键是否被接受为输入。

~~~ .python
def my_form_validator():
    """检查性别和年龄字段是否都已填写"""
    return gender != 'no' and age != ''


def filter_digits(ch):
    """仅允许数字字符作为输入"""
    return ch in '0123456789'


# 定义所有小部件
button_ok = Button(text='Ok')
label_gender= Label('您的性别')
checkbox_male = Checkbox(text='男', group='gender', var='gender')
checkbox_female = Checkbox(text='女', group='gender', var='gender')
label_age = Label('您的年龄')
# 指定一个键筛选器，以便只接受数字作为文本输入
input_age = TextInput(stub='此处输入年龄 ...', var='age', key_filter=filter_digits)
# 构建表单。指定一个验证器函数以确保表单完成。
my_form = Form(validator=my_form_validator, rows=[1,1,1], cols=[1,1,1])
my_form.set_widget(label_gender, (0, 0))
my_form.set_widget(checkbox_male, (1, 0))
my_form.set_widget(checkbox_female, (2, 0))
my_form.set_widget(label_age, (0, 1))
my_form.set_widget(input_age, (1, 1), colspan=2)
my_form.set_widget(button_ok, (1, 2))
my_form._exec()
~~~