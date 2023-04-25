title: 准备-运行策略
hash: e91e8e57fbac78eb05547ef89cd9bbb3ae1f177e7d96e295fb31c6e7da95965d
locale: zh
language: Chinese

[TOC]

## 关于

实验通常由短暂的时间间隔（'试验'）组成，参与者在此期间感知刺激并执行任务。在试验期间应控制时间，但试验间隔的持续时间可能会出现一些不可预测的变化，因此，一个好的策略是在试验之前执行耗时任务，并在试验期间将执行的操作保持在最低限度。

OpenSesame通过从SEQUENCE项目中调用每个元素两次来实现这一点。这是*准备-运行策略*：

- 在准备阶段，项目有机会进行准备。例如，SYNTH 生成声音（但不播放）;SKETCHPAD 绘制画布（但不显示）。
- 在运行阶段，项目尽可能少地执行操作。例如，SYNTH 播放之前准备好的声音；SKETCHPAD 显示之前准备好的画布。

这降低了出现时间错误的风险。准备-运行策略在SEQUENCE项目级别实施，这通常包含实验的时间关键部分。这意味着在启动SEQUENCE之前，会出现一些不可预测的时间抖动。

## 项目具体说明

### loop项目

LOOP项不是提前准备的。在使用LOOP实现时间关键部分时，重要的是要考虑到这一点。例如，你可能会尝试使用LOOP项目实现以下的RSVP流：

~~~text
rsvp_loop item (4 cycles)
- stimulus_item
~~~

在这个构造中，*stimulus_item*将轮流被准备和运行四次，如下所示：

~~~text
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
prepare stimulus_item
run stimulus_item
~~~

因此，您需要验证*stimulus_item*的准备过程是否会导致时间错误。

### sequence项目

所有包含在SEQUENCE中的项目都是提前准备好的。因此，以下构造...

~~~text
trial_sequence
- fixation_sketchpad
- target_sketchpad
- keyboard_response
- logger
~~~

...将以以下方式执行...

~~~text
prepare fixation_sketchpad
prepare target_sketchpad
prepare keyboard_response
prepare logger
run fixation_sketchpad
run target_sketchpad
run keyboard_response
run logger
~~~

### sketchpad部分及反馈项目

SKETCHPAD和FEEDBACK项目在准备时有所不同。对于SKETCHPAD部分，在准备阶段进行准备；对于FEEDBACK项目，应在运行阶段进行准备。

要获得更多信息，请参阅：

- %link:manual/stimuli/visual%

### synth和sampler项目

对于SYNTH和SAMPLER项目，在准备阶段生成并预先加载声音。

### inline_script项目

在INLINE_SCRIPT项目中，你可以选择如何实现运行和准备策略。通常情况下，遵循以下准则是个好做法：

- 在准备阶段放入耗时较长的准备功能。例如，创建画布对象和生成声音。
- 在运行阶段投入尽可能少的代码。例如，仅显示之前准备好的画布。

### 其他项目和插件

一般来说，项目应遵循在准备阶段尽可能完成耗时较长的准备工作，同时在运行阶段尽量减少操作的原则。然而，每个插件的实现方式都不尽相同。如果您不确定某个特定情况，请在论坛上发表问题。

## 条件表达式（如果运行，如果显示，如果中断等）

在SEQUENCE项目中，'如果运行'（Run if）条件在运行阶段的最后时刻进行评估。因此，您可以使条件为`correct == 0`，这取决于之前已经调用的KEYBOARD_RESPONSE项目的结果。需要注意的是，'运行若'表达式仅适用于项目的运行阶段 - 准备阶段始终被执行。

在COROUTINES项目中，“Run if”条件在Prepare阶段进行评估。因此，条件不能依赖于在执行COROUTINES期间发生的事件。

在SKETCHPAD项目中，“Show if”条件在Prepare阶段进行评估，即在构建画布时。在FEEDBACK项目中，“Show if”条件在Run阶段进行评估（因为画布只在Run阶段构建）。