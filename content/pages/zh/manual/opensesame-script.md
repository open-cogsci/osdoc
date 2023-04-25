title: OpenSesame 脚本
reviewed: false
hash: 73e219615747fe9d3e0d6444db9859ce306004221b08c7ff0f63e555f160cfa2
locale: zh
language: Chinese

[TOC]

## 关于 OpenSesame 脚本

OpenSesame 脚本是一种简单的定义实验的语言。它不是一种完整的编程语言，不包括诸如 `for` 循环等功能。OpenSesame 脚本由 OpenSesame 运行时环境解释。

OpenSesame 脚本与用于 inline_script 项目中的 Python 脚本不同。Python 是一种真正的编程语言，具有所有相关的灵活性和复杂性。相反，OpenSesame 脚本用于以简单、易于理解的方式定义实验。

## 一般备注

### 关键词

一些项目（如 form_base 和 sketchpad）接受关键词。关键词的格式为 `keyword=value`。关键词是可选的，应默认为默认值。

### 注释

以散列开头的字符串应解释为注释。

*示例*

	# 这是一个注释

### 引用

除非字符串中包含空格或其他标点符号，否则不需要引用。因此，以下行应解释为相同：

	set my_var 'my_value'
	set my_var "my_value"
	set my_var my_value

然而，以下行并不相同。事实上，第一行是无效的，因为它有一个意外的第三个参数。

	set my_var my value
	set my_var "my value"

### 类型

没有类型。字符串、整数等之间没有区别。

### 特定项目的语法

一些项目有特定的语法。在下面讨论的每个关键词的“应用于”部分中指示此。

### 路径名解析

TODO

## *define* 语句

开始定义一个项目。在一个 define 语句之后，所有行都有一个制表符缩进。项定义的末尾是第一个不再缩进的字符串。不允许嵌套 define 语句。

*应用于*

所有项目

*格式*

	define [item name] [item type]
		[item definition]

*参数*

|`item name`	|项目的名称	|
|`item type`	|项目的类型	|

*示例*

	define get_key keyboard_response
		set allowed_responses "a;x"
		set description "收集键盘响应"
		set timeout "infinite"
		set flush "yes"

## *draw* 语句

定义 sketchpad 或 feedback 项目的视觉元素。

*应用于*

sketchpad, feedback

*格式*

格式取决于元素。

	draw ellipse [left] [top] [width] [height] [keywords]
	draw circle [x] [y] [radius] [keywords]
	draw line [left] [right] [top] [bottom] [keywords]
	draw arrow [left] [right] [top] [bottom] [keywords]
	draw textline [x] [y] [text]
	draw image [x] [y] [path]
	draw gabor [x] [y]
	draw noise [x] [y]
	draw fixdot [x] [y]

*参数*

|`left` 		|最左边的 x 坐标		|
|`right`		|最右边的 x 坐标	|
|`top`			|顶部的 y 坐标			|
|`bottom`		|底部的 y 坐标		|
|`x` 			|x坐标				|
|`y`			|y坐标				|
|`text` 		|文本字符串				|
|`path` 		|图像文件的路径		|

*关键词*

TODO

*示例*

	draw fixdot 0 0

## *log* 语句

表示变量应写入日志文件。

*应用于*

logger

*格式*

	log [variable name]

*参数*

|`variable name`		|变量的名称	|

*示例*

	log response_time

## *run* 语句

表示应运行一个项目。在序列的情况下，运行语句的顺序决定了项目调用的顺序。在 coroutines 插件的情况下，所有项目同时调用。

*应用于*

sequence

*格式*

	run [item name] [optional: condition] [optional: disabled]

*参数*

|`item name`			|要运行的项目的名称	|
|`condition` (optional)	|条件语句，决定实际调用项目。如果没有提供条件，项目始终被调用。|

*示例*

	run correct_feedback '[correct] = 1'

## *set* 语句

定义单行变量。

*应用于*

所有项目

*格式*

	set [variable name] [value]

*参数*

|`variable name`	|变量名	|
|`value`			|变量值	|

*示例*

	set timeout 1000

*注意事项*

多行变量使用`__[variable name]__`符号定义。这主要适用于需要大量文本的项目。在项目定义中，每行前都有一个制表符，不应将其解释为文本的一部分。`__end__`表示变量的结束。

*例如：*

	__my_variable__
	这是第一行。
	这是第二行。
	__end__

## *setcycle* 语句

类似于常规的“set”语句，但仅在循环的特定周期内设置变量。这是循环表的脚本等效项。

*适用于*

循环

*格式*

	setcycle [cycle #] [variable name] [variable value]

*参数*

|`Cycle #`			|循环次数，其中0为第一个	|
|`variable name` 	|变量名						|
|`value`			|变量值						|

*示例*

	setcycle 0 cue valid

## *widget* 语句

将一个小部件（按钮、标签等）添加到表单中。有效关键词取决于小部件的类型。widget语句并非严格属于OpenSesame核心语法的一部分，而是由form_base插件使用。

*适用于*

form_base (插件)

*格式*

	widget [column] [row] [column span] [row span] [widget type] [keywords]

*参数*

|`column`		|窗口部件在表单中的列位置，其中0为最左边							|
|`row`			|窗口部件在表单中的行位置，其中0为顶部								|
|`column span`	|窗口部件占用的列数													|
|`row span`		|窗口部件占用的行数												|
|`widget type`	|'button', 'checkbox', 'image', 'image_button', 'label', 'rating_scale', 或 'text_input'	|

*关键词*

待定

*示例*

	widget 0 0 1 1 label text='这是一个标签'