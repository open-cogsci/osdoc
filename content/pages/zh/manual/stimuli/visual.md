title: 视觉刺激
hash: 4ead1768298a015dc8af358675db670a71ea61876c2803a8998223c3509860c5
locale: zh
language: Chinese

使用 SKETCHPAD 项目是呈现视觉刺激的最常见方法，或对于非时间关键刺激，则使用 FEEDBACK 项目。

[TOC]

## 使用涂鸦板和反馈项目

SKETCHPAD 和 FEEDBACK 项目提供了基本的所见即所得绘图工具（%FigSketchpad）。

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: SKETCHPAD 提供了内置的绘图工具。
--%

## 涂鸦板和反馈项目之间的区别

SKETCHPAD 和 FEEDBACK 项目在大多数方面是相同的，除了两个重要的区别。

### 涂鸦板项目提前准备，反馈项目不是

SEQUENCE 部分的准备阶段会提前准备 SKETCHPAD 的内容。为了确保准确的计时，这是必要的：这允许在运行阶段立即显示 SKETCHPAD，而不会因为刺激物准备导致的延迟。然而，这种方法的缺点是 SKETCHPAD 的内容不能取决于它所属的 SEQUENCE 发生的事情。例如，您不能使用 SKETCHPAD 提供有关同一序列中的 SKETCHPAD 和 KEYBOARD_RESPONSE 项目收集的响应时间的即时反馈。

相比之下，只有在实际显示时，才会准备 FEEDBACK 项目的内容，即在其所属的 SEQUENCE 的运行阶段。这使得可以提供刚刚发生的事情的反馈 - 因此得名。然而，FEEDBACK 项目不应用于呈现时间关键刺激，因为它可能受到刺激准备导致的延迟影响。

有关准备运行策略的更多信息，请参阅：

- %link:prepare-run%

### 反馈变量（默认情况下）由反馈项目重置

FEEDBACK 项目有一个 “重置反馈变量” 选项。启用此选项后（默认情况下是启用的），显示 FEEDBACK 项目时会重置反馈变量。

有关反馈变量的更多信息，请参阅：

- %link:manual/variables%

## 在 Python 内联脚本中呈现视觉刺激

### 在Python中访问 SKETCHPAD

您可以将 SKETCHPAD 的 `Canvas` 对象作为项目的 `canvas` 属性进行访问。例如， 假设您的 SKETCHPAD 名为 *my_sketchpad*，并包含名为“my_image”的图像元素。然后，您可以使用以下脚本使此图像旋转：

```python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
    my_canvas['my_image'].rotation = angle
    my_canvas.show()
```

### 在 Python 中创建画布

您可以使用 `Canvas` 对象在 Python 中呈现视觉刺激：

- %link:manual/python/canvas%
