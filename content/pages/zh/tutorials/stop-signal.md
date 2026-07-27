title: 停止信号任务（使用 coroutines）
hash: a90dc175aa27f6f7bdfc95ae0c91f7aa1f0aacaeeac9a505a63772d5a363d5d5
locale: zh
language: Chinese

[TOC]

## 关于 OpenSesame

OpenSesame 是一款用户友好的程序，用于开发心理学、神经科学和实验经济学中的行为实验。对于初学者，OpenSesame 提供了完整的图形化点击式界面。对于高级用户，OpenSesame 支持 Python（仅桌面版）和 JavaScript（桌面版和浏览器版）。

OpenSesame 基于 [General Public License v3][gpl] 免费提供。

## 关于本教程

本教程展示如何在 OpenSesame 中使用 `coroutines` 插件创建一个停止信号任务。该实验基于 [Logan, Cowan and Davis (1984)][references] 的简单反应时版本。本教程的主要目标不仅是构建这个任务，还要理解 coroutines 如何使多个事件被放置在单个试次时间线上。

## 资源

- __下载__ — 本教程假定你运行的是 OpenSesame 4.1 或更高版本，并且在桌面端运行实验。你可以从以下地址下载 OpenSesame 的最新版本：
	- <https://osdoc.cogsci.nl/4.1/download/>
- __文档__ — 专门的文档网站位于：
	- <http://osdoc.cogsci.nl/>
- __论坛__ — 支持论坛位于：
	- <http://forum.cogsci.nl/>
- __Sigmund__ — SigmundAI 是一位具备 OpenSesame 专业知识的 AI 助手，可在以下地址找到：
	- <https://sigmundai.eu/>

## 实验

在这个实验中，被试需要对屏幕上出现的字母尽可能快速地作出反应。在大多数试次中，当字母出现时，他们应按下空格键。在一些试次中，字母出现后不久会播放一个音调，被试应尽量抑制自己的反应。该任务的目标是估计停止信号反应时（SSRT），这是一个用于衡量抑制过程速度的潜在指标。要可靠地估计 SSRT，需要被试在 go 试次中快速反应，并且仅在出现停止信号时尝试抑制反应。

该实验使用四个字母：`E`、`F`、`H` 和 `L`。无论显示哪个字母，反应总是相同的。这使得该任务成为停止信号范式的简单反应时版本。

每个试次具有如下结构：

- 呈现一个注视点 500 ms。
- 注视点之后呈现一个字母。
- 字母出现时打开反应窗口。
- 在 stop 试次中，经过短暂延迟后播放一个 900-Hz 音调。
- 字母之后呈现一个掩蔽。
- 试次总时长固定为 3500 ms。

%--
figure:
 id: Fig_paradigm
 source: stop_paradigm.png
 caption: A schematic overview of the stop-signal paradigm implemented in this tutorial.
--%

这类任务通常表明，当停止信号延迟较长时，被试抑制反应的可能性低于延迟较短时。如果被试预期会出现停止信号，他们有时可能会策略性地放慢速度。因此，指导语应强调被试需要快速反应，并且不要等待音调。

## 实验设计

该设计：

- 是被试内设计，因为所有被试都完成所有试次类型
- 包括 go 试次和 stop 试次
- 在 stop 试次中包括四种停止信号延迟：
	- `50`
	- `100`
	- `150`
	- `200`
- 包括四个字母：
	- `E`
	- `F`
	- `H`
	- `L`

loop 表包含 80 行，并重复四次，因此总共有四个区块，每个区块 80 个试次。

现在我们将一步一步构建这个实验。

## 第 1 步：创建实验的基本结构

启动 OpenSesame 并创建一个新实验。在本教程中，主 sequence 名为 `experiment`，并包含：

- `new_form_consent`
- `instructions`
- `simple_rt`

`simple_rt` item 是一个 loop，其中包含该实验的试次结构。

概览区域现在应如下所示：

%--
figure:
 id: Fig_overview
 source: stop_overview.png
 caption: The overview area of the stop-signal experiment.
--%

## 步骤 2：添加同意表单和说明屏幕

该示例实验以一个同意表单开始。从技术角度来看，这一步是可选的，但在许多真实实验中，在任务开始之前请求参与者提供知情同意是有用或必要的。

在同意表单之后，参与者会看到一个说明屏幕。说明内容解释说，每当出现一个字母时，参与者都应按下空格键，但当他们听到停止音时，应尽量抑制反应。说明还应强调，参与者在作答前不应等待音调出现。

说明 item 可以如下所示：

%--
figure:
 id: Fig_instructions
 source: stop_instructions.png
 caption: The instruction screen shown before the experiment starts.
--%

## 步骤 3：创建 trial loop

trial 结构在一个名为 `simple_rt` 的 loop 中定义。这个 loop 包含 80 行，并重复四次。在每次重复中，trial 的顺序都会被随机化。

每一行至少定义以下变量：

- `letters`
- `is_stop`
- `delay`
- `correct_response`

对于 go trials：

- `is_stop` 为 `no`
- `delay` 为 `0`
- `correct_response` 为 `space`

对于 stop trials：

- `is_stop` 为 `yes`
- `delay` 为 `50`、`100`、`150` 或 `200` 之一
- `correct_response` 为 `None`

这是使用 `keyboard_response` item 内置评分功能的一种便捷方式。在 go trials 中，按下空格是正确的。在 stop trials 中，抑制反应是正确的，因为正确反应被定义为 `None`。

loop 表应如下所示：

%--
figure:
 id: Fig_loop
 source: stop_loop.png
 caption: The loop table that defines go trials and stop trials.
--%

## 步骤 4：创建 trial items

coroutine 使用了几个 item，这些 item 应首先单独创建。

### 4.1 注视点

插入一个新的 sketchpad，并将其重命名为 `fixation`。在上面绘制一个中央注视点。虽然 sketchpad 有自己的持续时间设置，但这个 item 的时序稍后将由 coroutine 控制。

### 4.2 字母显示

插入一个新的 sketchpad，并将其重命名为 `letter`。添加一个文本元素，用于显示变量 `{letters}` 的值，以便显示的字母在不同 trial 之间变化。`{letters}` 周围的花括号表示这不是字面文本，而是实验变量 `letters` 的值，该变量在 loop 表中定义。

letter sketchpad 应如下所示：

%--
figure:
 id: Fig_letter
 source: stop_letter.png
 caption: The letter sketchpad, which shows the value of the variable `letters`.
--%

### 4.3 掩蔽

插入一个新的 sketchpad，并将其重命名为 `mask`。在当前实验中，这个 sketchpad 是空的，因此它主要作为 trial 时间线中的一个占位符。与其他 sketchpad 一样，它的实际时序稍后将由 coroutine 决定。

### 4.4 反应 item

插入一个新的 `keyboard_response` item，并将其重命名为 `resp_simple_rt`。将允许的反应设置为 `space`。当这个 item 在 coroutine 内部使用时，反应窗口将由 coroutine 时间线控制，而不是由该 item 自身的超时设置控制。

keyboard response 设置应如下所示：

%--
figure:
 id: Fig_keyboard
 source: stop_keyboard.png
 caption: The keyboard response item configured to collect a spacebar response.
--%

### 4.5 停止信号

插入一个新的 `synth` item，并将其重命名为 `stop_signal`。设置：

- waveform 为 `sine`
- frequency 为 `900`
- length 为 `500`
- duration 为 `0`

将 duration 设为 `0` 可确保声音开始播放后，coroutine 立即继续执行，而不是等待声音播放结束。

%--
figure:
 id: Fig_synth
 source: stop_synth.png
 caption: The synth item configured to produce a 900-Hz tone lasting 500 ms.
--%

### 4.6 Logger

插入一个新的 `logger` item，并将其重命名为 `logger`。关闭 automatic logging，并手动记录关键变量。特别要确保包括 `letters`、`is_stop`、`delay`、`response`、`response_time` 和 `correct` 等变量。

logger 设置应如下所示：

%--
figure:
 id: Fig_logger
 source: stop_logger.png
 caption: The logger item configured to log the critical stop-signal variables.
--%

## 步骤 5：添加 coroutine item

现在插入一个 `coroutines` item，并将其重命名为 `coroutines`。这个 item 将定义每个 trial 在共享时间线上的时序。

将 coroutine 的总持续时间设置为 `3500`，并添加各个 trial items，使它们被放置在同一条 trial 时间线上。

在这个阶段，重要的是要记住，并非每个 OpenSesame item 都能在 coroutine 中使用。支持的 items 至少包括：

- `feedback`
- `inline_script`
- `keyboard_response`
- `logger`
- `mouse_response`
- `sampler`
- `synth`
- `sketchpad`

如果某个 item 不支持 coroutines，它就不能被放置在共享的 coroutine 时间线上。

## 步骤 6：配置 coroutines item

`coroutines` item 是实验的时间核心。它允许在单一时间线上协调多个 trial 事件，因此呈现、反应收集和声音调度可以在时间上重叠。

这对于 stop-signal task 尤其有用。fixation display 首先出现，随后 letter 出现，参与者可以在 trial 继续进行时作出反应，而 stop tone 只在部分 trials 中呈现，并且只在一个可变延迟之后呈现。普通的 sequence item 不太适合这种时间重叠，而 coroutine 正是为此类用途设计的。

### 6.1 coroutine 时间线

在这个实验中：

- `fixation` 在 `0` 开始
- `letter` 在 `500` 开始
- `resp_simple_rt` 在 `500` 开始
- `mask` 在 `1000` 开始
- `stop_signal` 仅在 stop trials 中于 `{delay + 500}` 开始
- `logger` 在 trial 结束时运行

`delay` 的值来自 loop table。由于 letter 在 `500` ms 出现，表达式 `{delay + 500}` 会相对于 letter onset 而不是相对于整个 trial 的开始来安排 stop signal。

### 6.2 `start`、`end` 和 `run_if` 的工作方式

coroutine 中的每一行都指定一个 item 应该在何时运行，以及在某些情况下何时停止。

- `start` 表示 item 何时开始，即在 coroutine 开始后多少毫秒。
- `end` 表示 item 何时停止，如果该 item 在一段时间内保持活动状态。
- `run_if` 表示该 item 是否需要运行。

这意味着 coroutine 不只是简单地列出 items。它定义了一条时间线，并将每个 item 放置在这条时间线上。

例如：

- `letter` 在 `500` 开始，这意味着 letter 会在 trial 开始后 500 ms 出现。
- `resp_simple_rt` 也在 `500` 开始，这意味着反应收集会在 letter 出现时开始。
- `stop_signal` 使用一个 `run_if` 条件，因此它只会在 stop trials 中播放。

stop signal 的一个典型 `run_if` 表达式是：

`is_stop == "yes"`

这个表达式会在每个 trial 上进行求值。在 stop trials 中，synth item 会运行。在 go trials 中，它会被跳过。

### 6.3 `end` 何时适用

并非 coroutine 中的每个 item 都以相同方式使用 `end`。

有些 items 实际上是一次性 item。例如，sketchpad 会准备一个 display，并在启动时将其显示出来。在实践中，这类 item 的重要设置通常是 `start` 时间。display change 会在那个时刻发生，而 sketchpad 本身不需要像 response item 或 sound item 那样保持活动状态。

其他项目确实会在一段时间内保持活动。例如，`keyboard_response` 可以在一个反应窗口内保持活动，而声音项目可以在音频播放期间保持活动。对于这些项目，`end` 是有意义的，因为它决定了该项目何时在 coroutine 时间线上停止活动。

因此，一般来说：

- `start` 对所有项目都相关
- `end` 主要对那些在一段时间内保持活动的项目相关
- `run_if` 在项目只应在某些条件下运行时相关

### 6.4 这如何应用于停止信号任务

在当前实验中：

- `fixation`、`letter` 和 `mask` 主要用于在特定时刻更新显示
- `resp_simple_rt` 在反应窗口期间保持活动
- `stop_signal` 仅在 `is_stop == "yes"` 时启动
- `logger` 在试次结束时运行

这意味着，sketchpad 主要依赖其 `start` 时间，而反应项目和停止信号项目则更适合理解为在试次时间线的一部分中处于活动状态的项目。

### 6.5 项目持续时间如何与 coroutine 时序相关

在使用 coroutines 时，必须记住 coroutine 控制项目何时处于活动状态。换句话说，有效的时序由 coroutine 的 `start`、`end` 和 `run_if` 设置决定，而不是主要由各个项目内部的 duration 或 timeout 设置决定。

这就是为什么本实验中的 sketchpad 不需要它们自己的持续时间来定义试次结构。它们在时间线中的作用由 coroutine 决定。同样的逻辑也适用于 `keyboard_response`：即使该项目有自己的 timeout 设置，反应窗口实际上也是由 coroutine 时间线定义的。

`stop_signal` synth 很清楚地说明了这一点。它的声音属性，例如波形和长度，是在 synth 项目本身中定义的，但它开始的时刻是由 coroutine 定义的。

### 6.6 为什么停止信号 synth 使用 `duration = 0`

`stop_signal` 项目的声音长度为 500 ms，而 duration 为 `0`。这很重要，因为这意味着声音开始后 coroutine 会立即继续，而不是等待声音播放结束。

因此，音调可以在 coroutine 时间线其余部分继续进行时播放。这正是停止信号任务所需要的：信号必须在精确的时刻出现，但它不能暂停反应收集或试次的其余部分。

coroutine 设置应如下所示：

%--
figure:
 id: Fig_coroutines
 source: stop_coroutines.png
 caption: The coroutine item that controls the shared trial timeline.
--%

### 6.7 为什么 logger 放在 `3400`

在示例实验中，coroutine 的总时长为 `3500` ms，但 `resp_simple_rt` 和 `logger` 都设置为 `3400`。这意味着反应窗口会在 `3400` ms 时关闭，并且试次也会在同一时刻被记录，而不是在 coroutine 的最末端记录。

这很有用，因为它确保反应收集不会持续到试次被记录的时刻之后。同时，coroutine 最后的 `100` ms 保持未使用，作为 coroutine 本身结束前的一个小安全余量。

在实践中，这意味着当 logger 运行时，相关的反应变量，如 `response`、`response_time` 和 `correct`，都已经被设置好。

## 步骤 7：测试实验

当实验结构完成后，运行测试并确认：

- 注视点首先出现
- 字母在 500 ms 后出现
- 反应窗口随着字母出现而打开
- 停止音只在停止试次中播放
- 停止音的时序取决于 `delay`
- 试次时长始终为 3500 ms

检查日志文件也很有帮助，以确认 `letters`、`is_stop`、`delay`、`response`、`response_time` 和 `correct` 被正确存储。

## 完成

恭喜，实验已完成。你现在可以通过按下蓝色双箭头按钮（快捷键：`Ctrl+W`）来进行测试运行。

下面演示的是为教程目的而创建的该实验缩短版本。

<video controls width ="100%"> 
    <source src="/video/stop_demo.mp4" type="video/mp4">
</video>
<p align="center"><em>视频 1. 已完成的停止信号任务演示。</em></p>

## 参考文献

Logan, G. D., Cowan, W. B., & Davis, K. A. (1984). On the ability to inhibit simple and choice reaction time responses: A model and a method. *Journal of Experimental Psychology: Human Perception and Performance*, *10*(2), 276–291.

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324.

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html