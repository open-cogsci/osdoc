title: 并行处理事务
hash: 355690924feb930d7fef825b28269bb20c28adb8e20b8c2a86de761222d40d95
locale: zh
language: Chinese

协同程序并行运行多个项目——或者更准确地说，它们以一种看起来像是并行的方式快速交替运行项目。并非所有项目都支持协同程序。

[TOC]

## 使用协同程序

您可以通过COROUTINES插件使用协同程序（请参见%FigCoroutinesInterface）。

%--
figure:
 source: FigCoroutinesInterface.png
 caption: coroutines插件的界面。
 id: FigCoroutinesInterface
--%

如您所见，COROUTINES插件看起来类似于SEQUENCE项目，但有一些额外的选项：

- *持续时间* 表示协同程序的总持续时间。
- *在项目结束后结束（可选）* 表示当特定项目结束时，协同程序应该终止。这允许您，例如，表明当收集到一个按键时，协同程序应该结束，通过在此处选择一个KEYBOARD_RESPONSE项目。
- 每个项目都有一个*开始时间*。大多数项目也有一个*结束时间*。结束时间不适用于一次性项目；例如，SKETCHPADs立即显示并终止，因此没有结束时间。

具体来说，%FigCoroutinesInterface中的示例（来自停止信号任务示例）执行以下操作：

- 立即显示一个目标显示。
- 如果`stop_after`变量不为空，则在`stop_after`变量指定的间隔后，显示stop_signal显示。
- 在整个（2000毫秒）间隔期间，收集一个键盘响应。

时间流程由COROUTINES插件控制。因此，不使用在项目中指定的超时和持续时间值。例如，在%FigCoroutinesInterface中，KEYBOARD_RESPONSE将运行2000毫秒，无论在项目中指定的超时时间为多少。


## 支持的项目

目前，以下项目受到支持（此列表可能不完整）：

- FEEDBACK
- INLINE_SCRIPT
- KEYBOARD_RESPONSE
- LOGGER
- MOUSE_RESPONSE
- SAMPLER
- SYNTH
- SKETCHPAD

## 在协同程序中使用inline_script项目

当您在COROUTINES中使用INLINE_SCRIPT项目时，运行阶段的工作方式与您可能习惯的稍有不同。具体来说，运行阶段在COROUTINES的每次迭代中都会执行。此外，运行阶段应该只包含执行时间非常短的代码；这是因为耗时的操作会阻止COROUTINES的进行，从而干扰COROUTINES中其他项目的计时。要结束协同程序，您可以引发一个`AbortCoroutines()`异常。

例如，假设您有一个COROUTINES包含两个KEYBOARD_RESPONSE项目，*kb1* 和 *kb2*，您希望在收集到两个按键后运行协同程序，超时时间为5000毫秒。您可以创建以下协同结构：

%--
figure:
 source: FigCoroutinesTwoResponses.png
 caption: 收集两次键盘响应的协同程序
 id: FigCoroutinesTwoResponses
--%

*check_responses* INLINE_SCRIPT在准备阶段将两个响应变量都设置为空字符串：

```python
#该代码在协同程序开始时执行
response_kb1 = ''
response_kb2 = ''
```

然后，在运行阶段检查是否设置了两个变量，如果都设置了，就中止协同程序：

```python
#对于Python来说，非空字符串是True值
#此代码将被多次执行！
if response_kb1 and response_kb2:
    raise AbortCoroutines()
```

## 运行时表达式

在COROUTINES中，与SEQUENCE项目中的情况相比，运行时表达式的行为有所不同。具体而言，协同程序在准备阶段评估运行时表达式。另请参阅：

- %link: prepare-run%