title: 创建自定义表单
hash: a87d6a87fa567e6e8d52bfd533cc60fb77b7e646afa3b49d05009bbe198d852f
locale: zh
language: Chinese

[TOC]


## 关于表单、几何形状和小部件

表单是一组按特定几何形状排列的小部件（按钮、标签、文本输入字段等）。在下面的图片中，您可以看到一个 2（列）× 3（行）表单的示例。表单几何形状很简单，包括以下属性：

- *边缘* 确保部件不接触显示器的边缘。您可以为顶部、右侧、底部和左侧设置不同的边距。
- *间距* 确保部件彼此不接触。水平和垂直间距相同。
- 可能有一个或多个大小不同的 *行*。
- 可能有一个或多个大小不同的 *列*。

%--
figure:
 id: FigGeometry
 source: geometry.png
 caption: FORM 几何形状示意图。
--%

当然，空表单没什么意思。因此，让我们添加以下部件以创建一个简单的问题表单：

- 跨越顶部行的两列的`标签`。我们使用此标签为表单添加标题。
- 跨越中间行的两列的另一个`标签`。此标签包含实际问题。
- 位于底部右侧部件区域的`按钮`。此按钮允许用户给出 $0.05 的回答。
- 位于底部左侧部件区域的另一个`按钮`。此按钮允许用户给出 $0.10 的回答。

%--
figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: FORM 示意图示例。
--%

上面的图片是示意性的示例。该表单在 OpenSesame 中的实际外观取决于您的设置（尤其是您的字体和颜色），但它可能如下所示：

%--
figure:
 id: FigExample1
 source: example1.png
 caption: FORM 示例。
--%

## 创建自定义表单

有两种方法可以创建自定义表单。您可以：

- 使用 FORM_BASE 项，使用 OpenSesame 脚本指定表单。
- 在 INLINE_SCRIPT 项中使用 Python。Python 方法略微灵活一点，但对于大多数目的来说，这两种方法都可以使用。

### 使用 OpenSesame 脚本创建表单

我们将使用 OpenSesame 脚本创建上述表单。首先，将 FORM_BASE 插件拖动到您的实验中。单击新创建的项目以打开其标签页。接下来，在标签页区域的右上角，单击"编辑脚本"按钮（带终端图标）。这将打开脚本编辑器。输入以下脚本以生成上述表单（参见注释以获取解释）。

~~~
# 边缘定义为"上;右;下;左"。每个值对应一个像素的边缘。
set margins "50;100;50;100"
# 间距只是一个以像素为单位的值。
set spacing "25"
# 行的大小相对而言。"1;2;1"表示有三行，其中中间一行的大小是底部和顶部的两倍。因此，“1;2;1”
# 的意思与“3;6;3”完全相同。请注意，“3”并不意味着有三个同样大的行（但“1;1;1”确实如此）。
set rows "1;2;1"
# 以同样的方式定义列。"1;1"只是表示有两个相同大小的列。
set cols "1;1"
# 部件定义如下：
# widget [column] [row] [column span] [row span] [widget type] [keywords]
#
# 列和行从 0 开始计数。如果您不希望部件跨越多个列和行，只需将列和行跨度设置为1。
widget 0 0 2 1 label text="问题"
widget 0 1 2 1 label center="no" text="一只蝙蝠和一个棒球一起花费 $1.10。蝙蝠比球贵一美元。球多少钱？"
widget 0 2 1 1 button text="$0.10"
widget 1 2 1 1 button text="$0.05"
~~~

### 使用 Python 内联脚本创建表单

可以使用 INLINE_SCRIPT 和一些 Python 代码创建完全相同的表单。您会注意到 Python 代码在某种程度上类似于上面显示的 OpenSesame 脚本。这并不奇怪：FORM_BASE 插件基本上将 OpenSesame 脚本转换为 Python 代码。

首先，将一个 INLINE_SCRIPT 拖入你的实验中。选中新建的项目以打开其选项卡，并将以下脚本添加到 INLINE_SCRIPT 项目的运行阶段（查看注释以获得解释）。

~~~ .python
# 创建一个表单
form = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# 创建四个部件
labelTitle = Label(text='问题')
labelQuestion = Label(
    text='一只蝙蝠和一只棒球在一起花费 $1.10。棒子比球贵一美元。球花了多少钱？',
    center=False
)
button5cts = Button(text='$0.05')
button10cts = Button(text='$0.10')
# 将部件添加到表单中。表单中的位置以
# 表示为（列，行）元组。
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))
# 执行表单！在这种情况下，表单将返回被点击的按钮的文本内容。这是从表单中获取返回值的一种方法。另一种方法
# 是使用一些部件支持的 'var' 关键字。
button_clicked = form._exec()
~~~

如果你想在执行表单时让特定的部件获得焦点，你可以使用 `focus_wiget` 关键字：

~~~ .python
button_clicked = form._exec(focus_widget=button5cts)
~~~

### 非交互式表单

通常，一个表单会有一个输入字段、一个按钮或其他交互元素。但是，你也可以在没有任何交互元素的情况下使用表单。在OpenSesame脚本中，将`only_render` 设置为 "yes"：

```python
set only_render yes
```

在Python INLINE_SCRIPT中，调用`form.render()`，而不是`form._exec()`。

### 主题

表单支持主题。目前有两个主题可用：'gray' 和 'plain'。'gray' 主题是默认的。虽然 'gray' 主题已经相当简单，但 'plain' 主题更基本。在OpenSesame脚本中这样选择主题：

```python
set theme plain
```

在Python内联脚本中使用 `theme` 关键字：

~~~ .python
form = Form(theme='plain')
~~~

### 可用部件和关键字

有关可用部件和关键字的列表，请参阅：

- %link:manual/forms/widgets%

### 验证输入

要查看如何验证表单输入，请参阅：

- %link:manual/forms/validation%

## 另一个示例

以下OpenSesame脚本（在FORM_BASE插件中）将生成一个包含三个评分量表以及一个下一个按钮的问卷：

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="表明你对以下陈述的赞同程度"
widget 0 1 1 1 label center="no" text="表单很简单"
widget 1 1 1 1 rating_scale var="question1" nodes="同意;不知道;反对"
widget 0 2 1 1 label center="no" text="我喜欢数据"
widget 1 2 1 1 rating_scale var="question2" nodes="同意;不知道;反对"
widget 0 3 1 1 label center="no" text="我喜欢问卷"
widget 1 3 1 1 rating_scale var="question3" nodes="同意;不知道;反对"
widget 0 4 2 1 button text="下一步"
```

以下Python内联脚本将生成相同的问卷。

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