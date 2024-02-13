title: 创建自定义表单
hash: a7ba48cceefdfccdc42df16e4cfeb5980dcbd13a9a5b8516a328456704b5b400
locale: zh
language: Chinese

## 关于表单、布局和小部件

表单是一系列小部件（按钮、标签、文本输入字段等）按照特定的布局排列成一个网格。下图显示了一个2（列）×3（行）表单的示例。一个表单的布局很简单，包括以下属性：

- *边距* 确保小部件不会触碰到显示边缘。你可以对顶部、右侧、底部和左侧设置不同的边距。
- *间距* 确保小部件之间不会相互接触。水平和垂直间距是相同的。
- 有一个或多个可能大小不同的 *行*。
- 有一个或多个可能大小不同的 *列*。

%--
图：
 id: FigGeometry
 source: geometry.png
 caption: FORM布局示意图。
--%

当然，一个空白的表单并没有什么乐趣。所以，让我们添加以下小部件来创建一个简单的问答表单：

- 一个跨越顶行两列的 `label`。我们使用这个标签来为表单提供标题。
- 另一个跨越中间行两列的 `label`。这个标签包含了实际的问题。
- 一个位于底部右侧小部件区域的 `button`。这个按钮允许用户给出 $0.05 的回答。
- 另一个位于底部左侧小部件区域的 `button`。这个按钮允许用户给出 $0.10 的回答。

%--
图：
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: 一个示意性的FORM示例。
--%

上面的图片是示意性的例子。这个表单在OpenSesame中实际的样子取决于你的设置（特别是你的字体和颜色），但它可能看起来像这样：

%--
图：
 id: FigExample1
 source: example1.png
 caption: 一个FORM实例。
--%

## 创建自定义表单

有两种方法可以创建自定义表单。你可以：

- 使用FORM_BASE项目，并使用OpenSesame脚本指定你的表单。
- 在INLINE_SCRIPT项目中使用Python。使用Python的方式略微灵活些，但对于大多数目的来说，两种方式都可行。

### 使用OpenSesame脚本创建表单

我们将使用OpenSesame脚本创建上面描述的表单。首先，将FORM_BASE插件拖动到你的实验中。点击新创建的项目以打开其标签页。接下来，点击位于标签页右上角的“编辑脚本”按钮（带终端图标的），这将打开脚本编辑器。输入以下脚本以生成上述描述的表单（参看注释以获得解释）。

~~~
# 边距定义为“上;右;下;左”。每个值对应像素上的一个边距。
set margins "50;100;50;100"
# 间距只是一个像素值。
set spacing "25"
# 行的大小是相对的。“1;2;1”意味着有三行，
# 其中中间一行的大小是底部和顶部的两倍。所以“1;2;1”
# 和“3;6;3”是完全相同的意思。请注意，“3”并不意味着
# 有三个大小相同的行（但“1;1;1”确实意味着这一点）。
set rows "1;2;1"
# 列的定义方式相同。“1;1”简单意味着有两个大小相同的列。
set cols "1;1"
# 小部件的定义如下：
# widget [列] [行] [列跨度] [行跨度] [小部件类型] [关键字]
#
# 列和行的计数从0开始。如果你不想让你的小部件跨越多个列和行，
# 你只需将列跨度和行跨度设置为1。
widget 0 0 2 1 label text="问题"
widget 0 1 2 1 label center="no" text="一棒球和一个棒球拍总共花费$1.10。棒球拍比棒球贵一美元。棒球花了多少钱？"
widget 0 2 1 1 button text="$0.10"
widget 1 2 1 1 button text="$0.05"
~~~

如果你想在执行表单时让特定小部件获得焦点，可以向其中一个小部件应用`focus=yes`关键字：

```
widget 0 0 1 1 text_input text="初始文本" frame=yes center=no stub="在这里输入 …" return_accepts=yes var=response focus=yes
```


### 使用Python内联脚本创建表单

使用 INLINE_SCRIPT 配合一些 Python 代码也可以创建完全相同的表单。你会注意到，Python 代码与上面显示的 OpenSesame 脚本有些相似。这并不奇怪：FORM_BASE 插件基本上把 OpenSesame 脚本翻译成了 Python 代码。

首先，将一个 INLINE_SCRIPT 拖到你的实验中。选择新创建的项目以打开它的标签页，并将以下脚本添加到 INLINE_SCRIPT 项目的运行阶段（查看注释了解解释）。

~~~ .python
# 创建一个表单
form = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# 创建四个部件
labelTitle = Label(text='问题')
labelQuestion = Label(
    text='一支棒球和一个棒球队一共花费 $1.10 美元。棒球比棒球队多花费 $1 美元。小球要花费多少钱？',
    center=False
)
button5cts = Button(text='$0.05')
button10cts = Button(text='$0.10')
# 添加部件到表单中。表单中的位置以
# (列, 行) 元组的形式指出。
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))
# 执行表单！在这个例子中，表单将返回被点击按钮的文本。
# 这是从表单中获取返回值的一种方式。另一种方法
# 是使用一些部件支持的 'var' 关键词。
button_clicked = form._exec()
~~~

如果你想让表单执行时某个特定的部件获得焦点，你可以使用 `focus_wiget` 关键词：

~~~ .python
button_clicked = form._exec(focus_widget=button5cts)
~~~

### 非交互式表单

通常，一个表单会有一个输入字段、按钮或其他某种交互元素。然而，你也可以在不带任何交互元素的情况下使用表单。在 OpenSesame 脚本中，你设置 `only_render` 为 "yes" 来实现这一点：

```python
set only_render yes
```

在 Python 的 INLINE_SCRIPT 中，你则调用 `form.render()` 来代替 `form._exec()`。

### 主题

表单支持主题设置。目前有两种可用的主题："gray" 和 "plain"。"gray" 是默认主题。尽管 "gray" 主题已经非常简洁了，"plain" 主题还要基础得多。你可以在 OpenSesame 脚本中这样选择一个主题：

```python
set theme plain
```

或者在 Python 内联脚本中使用 `theme` 关键词：

~~~ .python
form = Form(theme='plain')
~~~

### 可用的部件和关键词

查看可用部件和关键词的列表，请访问：

- %link:manual/forms/widgets%

### 验证输入

要查看如何验证表单输入，请访问：

- %link:manual/forms/validation%

## 另一个例子

下面的 OpenSesame 脚本（在 FORM_BASE 插件中）将生成一个包含三个评级量表加上一个下一步按钮的问卷：

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="指出你对以下陈述的赞同程度"
widget 0 1 1 1 label center="no" text="表单很简单"
widget 1 1 1 1 rating_scale var="question1" nodes="赞同;不确定;反对"
widget 0 2 1 1 label center="no" text="我喜欢数据"
widget 1 2 1 1 rating_scale var="question2" nodes="赞同;不确定;反对"
widget 0 3 1 1 label center="no" text="我喜欢问卷"
widget 1 3 1 1 rating_scale var="question3" nodes="赞同;不确定;反对"
widget 0 4 2 1 button text="下一步"
```

下面的 Python 内联脚本将生成相同的问卷。

``` .python
form = Form(cols=[1,1], rows=[1,1,1,1,1])
title = Label(
    text='请指明你对以下陈述的同意程度'
)
question1 = Label(text='表格很容易', center=False)
question2 = Label(text='我喜欢数据', center=False)
question3 = Label(text='我喜欢问卷', center=False)
ratingScale1 = RatingScale(
    var='question1',
    nodes=['同意', u"不知道", '不同意']
)
ratingScale2 = RatingScale(
    var='question2',
    nodes=['同意', u"不知道", '不同意']
)
ratingScale3 = RatingScale(var='question3',
    nodes=['同意', u"不知道", '不同意'])
nextButton = Button(text='下一步')
form.set_widget(title, (0, 0), colspan=2)
form.set_widget(question1, (0, 1))
form.set_widget(question2, (0, 2))
form.set_widget(question3, (0, 3))
form.set_widget(ratingScale1, (1, 1))
form.set_widget(ratingScale2, (1, 2))
form.set_widget(ratingScale3, (1, 3))
form.set_widget(nextButton, (0, 4), colspan=2)
form._exec()
```

生成的表单大致如下所示。（具体外观取决于您的字体、颜色等。）

%--
figure:
 id: FigExample2
 source: example2.png
 caption: 另一个示例表单。
--%