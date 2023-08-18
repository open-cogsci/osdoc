title: 视觉刺激
hash: 88ce873464207508e0ba22cecad7bdf4c51299ae1bf089ba96618c35389e13c2
locale: zh
language: Chinese

使用SKETCHPAD项目或者对于非时间关键性刺激的FEEDBACK项目是呈现视觉刺激的最常见方式。

[TOC]


## 使用sketchpad和feedback项

SKETCHPAD 和 FEEDBACK 项提供了基础的所见即所得的绘图工具(%FigSketchpad)。

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: SKETCHPAD提供了内置的绘图工具。
--%


## 使用show-if表达式

您可以使用show-if表达式来确定是否应显示特定元素。例如，如果你有一个快乐脸的图片，只有在变量`valence`的值为'positive'时才显示，那么你可以将对应图片元素的show-if表达式设置为：

```python
valence == 'positive'
```

如果你留下一个空的show-if表达式或输入‘True'，元素将始终被显示。show-if表达式使用与其他条件表达式相同的语法。有关更多信息，请参阅：

- %link:manual/variables%

在准备显示的时候，会评估show-if表达式。这意味着，对于SKETCHPAD项目，它们在准备阶段进行评估，而对于FEEDBACK项目，它们在运行阶段进行评估（请参阅下面的部分）。

## sketchpad和feedback项之间的不同

SKETCHPAD和FEEDBACK项在大多数情况下是相同的，除了两个重要的区别。


### Sketchpad项提前准备，反馈项则不然

SKETCHPAD的内容是在其所属SEQUENCE的准备阶段准备的。这是为了确保准确的计时：它允许SKETCHPAD在运行阶段立即显示，没有任何由于刺激准备引起的延迟。然而，这一点的弊端是SKETCHPAD的内容不能依赖于其所属SEQUENCE的过程。例如，你不能使用SKETCHPAD来提供由KEYBOARD_RESPONSE项目收集的响应时间的直接反馈（假设SKETCHPAD和KEYBOARD_RESPONSE是同一序列的一部分）。

相比之下，FEEDBACK项目的内容只有在实际显示时才准备，也就是在其所属SEQUENCE的运行阶段。这使得可以提供关于刚刚发生的事情的反馈，因此得名。然而，FEEDBACK项不应用于呈现时间关键性的刺激，因为它会因刺激准备而受到延迟。

有关准备-运行策略的更多信息，请参阅：

- %link:prepare-run%

### 反馈变量（默认情况下）由反馈项重置

FEEDBACK项目有一个选项'重置反馈变量'。当此选项启用（默认启用）时，显示FEEDBACK项目时将重置反馈变量。

有关反馈变量的更多信息，请参阅：

- %link:manual/variables%


## 在Python内联脚本中显示视觉刺激

### 在Python中访问SKETCHPAD

您可以访问SKETCHPAD的`Canvas`对象作为项目的`canvas`属性。例如，假设你的SKETCHPAD名为*my_sketchpad*，并且包含一个名为'my_image'的图片元素。然后，你可以使用以下脚本使这个图片旋转：

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~


### 在Python中创建一个Canvas

您可以使用`Canvas`对象在Python中呈现视觉刺激：

- %link:manual/python/canvas%