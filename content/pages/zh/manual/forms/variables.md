title: 表单变量
hash: 5699e805a79ad2de0de21343a912e41c96c96935e89844f6af55864fcb4864cc
locale: zh
language: Chinese

[TOC]

## 关于表单变量

当你使用多个`checkbox`呈现一个表单时，你通常想知道用户勾选了哪个`checkbox`。同样，当你在一个表单中有两个`button`时，你想知道用户点击了哪个`button`。这些信息可以通过用户与表单互动时自动设置的变量获得。你可以自己指定应使用哪些响应变量。如何操作取决于你创建表单的方式。

### 在预制的表单插件中

当你使用预制的表单插件，如 FORM_TEXT_INPUT，可以直接在插件控件中指定响应变量名。

### 在自定义表单中

你可以使用`var`关键字来指示应使用哪个变量。例如，以下 OpenSesame 脚本（可以输入到 FORM_BASE 插件中）表示来自`text_input`窗口部件的响应应存储在名为`my_response_var`的变量中：

```python
widget 0 0 1 1 text_input var=my_response_var
```

等效的 Python 代码是：

~~~ .python
my_widget = TextInput(var='my_response_var')
~~~

另请参阅：

- %link:manual/forms/widgets%

## 窗口部件特定信息

每个窗口部件都以略有不同的方式使用其响应变量。

### button

如果点击了`button`窗口部件，它会将响应变量设置为'yes'；如果没有点击，则设置为'no'。

### checkbox

`checkbox`窗口部件会将响应变量设置为一个分号分隔的列表，列表内为所有已勾选的复选框的文本（对应该变量），如果没有勾选（对应该变量）`checkbox`，则设置为'no'。这听起来有点复杂，让我们来看一些例子。

```python
widget 0 0 1 1 checkbox group="1" text="A" var="my_response_var"
widget 1 0 1 1 checkbox group="1" text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
```

这里有两个带有文本“A”和“B”的`checkbox`，它们都属于同一个组，名为“1”，它们使用相同的响应变量，名为`my_response_var`。如果选中了“A”，`my_response_var`将是'A'。如果选中了“B”，`my_response_var`将是'B'。如果两者都没有被选中，`my_response_var`将是'no'。请注意，在本示例中，同一组中的`checkbox`只能选中一个，因此`my_response_var`将*永远不会*是'A;B'。

现在让我们考虑相同的脚本，唯一不同的是这两个`checkbox`不属于一个组：

```python
widget 0 0 1 1 checkbox text="A" var="my_response_var"
widget 1 0 1 1 checkbox text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
```

在这种情况下，情况就像上面描述的那样，但是两个`checkbox`可以同时被选中，在这种情况下,`my_response_var`将被设置为'A;B'。

你不能对不同组中的`checkbox`使用相同的响应变量。

### image

变量不适用于`image`窗口部件。

### image_button

如果点击了`image_button`窗口部件，它会将响应变量设置为'yes'；如果没有点击，则设置为'no'。

### label

变量不适用于`label`窗口部件。

### rating_scale

`rating_scale`窗口部件会将响应变量设置为已点击选项的编号，其中第一个选项为'0'（从零开始索引）。如果没有选择任何选项，响应变量设为'None'。

### text_input

`text_input`窗口部件会将响应变量设置为输入的文本。