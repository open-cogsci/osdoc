title: 中级教程（JavaScript）：视觉搜索
hash: 388eaf09923982d0aa520902c34577097ba883be1bae01e48c53293d53efad53
locale: zh
language: Chinese

[TOC]

## 关于OpenSesame

OpenSesame是一个用户友好的程序，用于开发心理学、神经科学和实验经济学方面的行为实验。对于初学者，OpenSesame具有全面的图形化、点击式界面。对于高级用户，OpenSesame支持Python（仅桌面端）和JavaScript（桌面和浏览器）。

OpenSesame在 [通用公共许可证v3][gpl] 下免费提供。

## 关于本教程

本教程介绍如何使用OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references] 创建一个基本的视觉搜索实验。我们将使用图形界面和JavaScript来开发一个可以在浏览器中在线运行的实验。推荐具备一定的OpenSesame和JavaScript经验。本教程大约需要一个小时。

本教程还提供基于Python的版本。如果您不需要在线运行实验，那么Python教程可能是您需要的：

- %link:tutorials/intermediate%

## 资源

- __下载__ —— 本教程假设您运行的是OpenSesame 4.0.0或更高版本，以及OSWeb 2.0或更高版本。您可以从以下地址下载OpenSesame的最新版本：
	- %link:download%
- __文档__ — 独立的文档网站可以在：
	- <http://osdoc.cogsci.nl/>
- __论坛__ — 支持论坛可以在：
	- <http://forum.cogsci.nl/>

## 实验

在本教程中，你将创建一个基本的视觉搜索实验。实验类似于 [Treisman and Gelade (1980)][references] 的经典视觉搜索研究，但并非完全相同。

在开始*构建*实验之前，你已经可以*参加*实验。这将让你对本教程的目标有一个很好的了解。

<a role="button" class="btn btn-success btn-align-left" href="https://jatos.mindprobe.eu/publix/1938/start?batchId=2191&generalMultiple">参加实验！</a>

在这个实验中，参与者寻找一个目标物体，可以是黄色的正方形、黄色的圆形、蓝色的正方形或蓝色的圆形；目标物的身份在试验块之间变化。参与者通过按右（出现）或左（消失）箭头键来表示目标是否存在。

除了目标之外，还会显示零个或多个干扰物。共有三种条件，条件决定了有哪些干扰物：

- 在*结构*条件下，干扰物可以是任何形状和颜色，唯一的限制是干扰物不能与目标相同。例如，如果目标是黄色正方形，那么干扰物就是黄色圆形、蓝色圆形和蓝色正方形。
- 在*形状特征*条件下，干扰物与目标的形状不同，但可以是任何颜色。例如，如果目标是黄色正方形，那么干扰物就是黄色圆形和蓝色圆形。
- 在*颜色特征*条件下，干扰物可以是任何形状，但颜色与目标不同。例如，如果目标是黄色正方形，那么干扰物就是蓝色正方形和蓝色圆形。

在每个实验后都会显示即时反馈：正确回答后显示绿点，错误回答后显示红点。在每个试验块结束后，将显示关于平均反应时间和准确性的详细反馈。

%--
图：
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  在本教程中，你将要实现的视觉搜索实验。
--%

这类实验通常有两个典型的发现：

- 在连接条件中找到目标所需的时间比在两个特征条件中要多。
- 在连接条件中，随着干扰物数量的增加，反应时间也会增加。这表明人们逐项搜索目标；这被称为*串行搜索*。
- 在特征条件下（形状和颜色都有），随着干扰物数量的增加，反应时间不会增加，或者几乎不会增加。这表明人们可以同时处理整个显示内容；这被称为*并行搜索*。

根据Treisman和Gelade的特征整合理论，这些结果反映了在连接条件下，您需要组合或*绑定*每个对象的颜色和形状。这种绑定需要注意力，因此您需要将注意力从一个对象转移到另一个对象；这很慢，解释了反应时间取决于有多少对象。相反，在特征条件下，颜色和形状不需要绑定，因此整个显示可以在不将注意力引向每一个对象的情况下进行一次扫描。

## 实验设计

此设计：

- 是*在主题内*，因为所有参与者都进行了所有条件
- 是*完全交叉*（或全因子），因为所有条件的组合都出现
- 有三个条件（或因子）：
	- 在块内变化：
		- `set_size`有三个级别（1、5、15），或SS<sub>3</sub>
		- `condition`有三个级别（连接、特征_形状、特征_颜色），或CN<sub>3</sub>
		- `target_present`有两个级别（存在、不存在），或TP<sub>2</sub>
	- 在块之间变化：
		- `target_shape`有两个级别（正方形、圆形），或TS<sub>2</sub>
		- `target_color`有两个级别（黄色、蓝色），或TC<sub>2</sub>
- 有N个主题，或<u>S</u><sub>N</sub>

您可以将此设计写为<u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

有关实验设计符号的更多信息，请参阅：

- %link:experimentaldesign%

## 第1步：创建实验的基本结构

启动OpenSesame，在“开始！”选项卡中选择扩展模板。此模板提供了许多认知心理学实验通常具有的基本结构，例如我们将在此处创建的实验。

扩展模板包含一些我们不需要的项目。删除以下项目：

- *about_this_template*
- *practice_loop*
- *end_of_practice*

删除这些项目后，它们仍可在“未使用的项目”回收站中看到。要永久删除这些项目，请单击“未使用的项目”回收站，然后单击“永久删除未使用的项目”按钮。

最后，为实验起一个好名字，例如“视觉搜索”。要做到这一点，请打开通用属性选项卡（在概览区域中点击“扩展模板”）并单击实验名称进行编辑。

还将OpenSesame配置为在浏览器上运行实验，而非桌面上。

概览区域现在应该看起来像%FigStep1:

%--
图：
 id：FigStep1
 source：step1.png
 caption：|
   第1步结束时的概览区域。
--%


## 第2步：定义在块之间变化的实验变量

如上所述，在我们的实验中，有两个变量在块之间变化：`target_shape`和`target_color`。因此，我们需要在*experimental_loop*中定义这些变量。为了理解为什么，请考虑图%FigStep1中显示的结构，从底部（即最缩进的级别）开始。

- *trial_sequence* 对应一个单独的试验
- *block_loop* 对应一组试验
	- 因此，在*trial_sequence*的每次运行中，此处定义的变量会有所不同；换句话说，在*block_loop*中定义的变量在__块内__变化。
- *block_sequence* 对应一组试验，其前面是对反馈变量的重置，后面是参与者的反馈
- *experimental_loop* 对应多组试验
	- 因此，在*block_sequence*的每次运行中，此处定义的变量会有所不同；换句话说，在*experimental_loop*中定义的变量在__块之间__变化。
- *experiment* 对应整个实验，即一个指导屏幕，然后是多组试验，最后是实验结束屏幕

点击experimental loop，并定义：

- `target_shape`，可以是'square'或'circle'；和
- `target_color`，可以是'yellow'或'blue'。

我们有一个全因子设计，这意味着所有2 × 2 = 4的组合都必须发生。*experimental_loop*的表格现在应该如%FigStep2所示：

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  在步骤2结束时，*experimental_loop*的表格。
--%

## 步骤3：在每个试验块开始时给出指导

现在，实验以一个单独的*instructions*屏幕开始。在我们的案例中，我们希望在每组试验之前给予指导，告诉参与者要查找什么目标（因为目标之间的身份有所不同）。

__将指令移至block_sequence__

因此，拿起*instructions*项目并将其拖到*block_sequence*上。一个弹出窗口会出现，问您是要：

- 将项目插入到*block_sequence*中，在这种情况下，*instructions*将成为*block_sequence*的第一个项目；或者
- 在*block_sequence*之后插入项目，在这种情况下，*instructions*将移到*block_sequence*之后的某个位置。

选择第一个选项('插入到')。现在*block_sequence*以指代屏幕开头，这正是我们想要的。

__添加指导文字__

点击*instructions*以打开它，并添加合适的指导文字，例如：

```text
操作指南

寻找 {target_color} {target_shape}

如果找到请按右箭头键
如果没有找到请按左箭头键

按任意键开始
```

花括号中的 '{target_color}' 和 '{target_shape}' 表示这些不是文字，而是指我们在*experimental_loop*中定义的变量。当实验运行时，这些变量的值将显示在此处，参与者将看到（例如）“寻找黄色圆形”。

__给出目标的视觉预览__

向参与者展示他们需要找到的实际刺激也是很好的。要做到这一点：

- 在显示器的中心绘制一个填充的圆形（确保它与文本不重叠）；
- 将圆形的颜色更改为'{target_color}'。这意味着圆形的颜色取决于变量`target_color`的值；和
- 将show-if表达式更改为`target_shape == 'circle'`。这是一个Python表达式，用于检查变量 `target_shape` 是否为 'circle'。 请注意，尽管在浏览器中运行实验时您*不能*使用Python的全部功能`inline_script`项目，但您*可以*为这些简单的条件表达式使用Python。

换句话说，我们画了一个圆，它的颜色由 `target_color`决定；而且，只有在变量 `target_shape` 为 'circle' 时，这个圆才会显示。有关变量和show-if语句的更多信息，请参阅：

- %link:manual/variables%

我们使用相同的技巧来绘制一个正方形：

- 在显示器的中心绘制一个填充的正方形；
- 将正方形的颜色更改为 '{target_color}'；和
- 将show-if语句更改为 `target_shape == 'square'`

*instructions* 屏幕现在应该如 %FigStep3 所示：

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  完成步骤3后的*instructions*屏幕。
--%

## 步骤4：定义在区块内变化的实验变量

我们的实验在区块内有三个变量在变化：`condition`，`set_size`和`target_present`。如在步骤2中所述，我们需要在*block_loop*中定义这些变量，以便它们在每次运行*trial_sequence*时变化。

这三个变量总共有3 × 3 × 2 = 18种不同的组合。我们可以手动输入这些表格，但是，因为我们有完全因子设计，我们还可以使用完全因子设计向导。要执行此操作，请首先打开*block_loop*，然后单击“完全因子设计”按钮。

在接下来出现的表格中，将变量名称放在第一行，将值放在下面的行上，如%FigFullFactorial所示。

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  完成步骤3后的*instructions*屏幕。
--%

现在单击"确定"以生成完整设计。*block_loop* 的表格现在应该看起来像 %FigStep4。

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  完成步骤4后的*block_loop*表格。
--%

## 步骤5：创建试验序列并添加初始化脚本

我们希望我们的试验序列如下所示：

- 固定点，我们将使用SKETCHPAD。
- 搜索显示，我们将使用自定义的INLINE_JAVASCRIPT在JavaScript中创建。
- 响应收集，我们将使用KEYBOARD_RESPONSE。
- 数据记录，我们将使用LOGGER。
- （我们还想在每次试验后立即得到反馈，但稍后我们会回到这一点。）

因此，*trial_sequence* 中唯一缺少的是 INLINE_JAVASCRIPT。

- 在*sketchpad*之后插入新的INLINE_JAVASCRIPT，并将其重命名为*search_display_script*。
- 将*sketchpad*重命名为*fixation_dot*，以便明确其功能；并
- 将*fixation_dot*的持续时间更改为500，以便将固定点显示500毫秒。（应该已经有一个固定点绘制；如果没有，可以在*fixation_dot*的中心绘制一个。）

我们还需要在实验开始时添加一个初始化脚本。我们仅将其用于定义（`let`）一个将容纳我们要绘制的`Canvas`对象的变量。在JavaScript中，您必须对变量进行严格一次定义，这就是为什么我们不能在*trial_sequence*中执行此操作。

- 在*experiment*序列的顶部插入新的INLINE_JAVASCRIPT，并将其重命名为*init*。

概览区现在应如%FigStep5所示。

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  步骤5结束时的概览区域。
--%

## 步骤6：生成搜索显示

__自上而下和防御式编程__

现在事情将变得有趣：我们将开始使用 JavaScript 进行编程。我们将使用两个指导原则：*自上而下*和*防御式*编程。

- *自上而下编程* 意味着我们从最抽象的逻辑开始，而不去管这个逻辑是如何实现的。一旦最抽象的逻辑到位，我们将会进行到较少的抽象逻辑，依此类推，直到我们到达实现的细节。这种技巧有助于保持代码结构。
- *防御性编程* 意味着我们假设我们会犯错误。因此，为了保护我们自己，我们将在代码中构建完整性检查。

*注意:* 以下解释假设您对 JavaScript 有些了解。如果像`Array`，`for`循环和函数之类的概念对您来说没有意义，那么最好先浏览一个入门 JavaScript 教程。您可以在此处找到 JavaScript 教程的链接：

- %link:manual/javascript/about%

代码的逻辑如 %FigHierarchy 所示。数字显示了我们将实现功能的顺序，从抽象级别开始。

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  代码绘制视觉搜索显示器的逻辑.
--%

__使用 let, var 和 const 声明变量__

在JavaScript中，在可以使用变量之前，您必须先 '声明' 它。(在 Python 中不需要这样做。) 在我们的例子中，我们将使用一个名为 `c` 的变量，因此我们需要声明它。为此，请打开 *init* 脚本的准备选项卡，并使用 `let` 关键字声明变量 `c`：

```js
let c
```

我们有三种声明变量的不同方式：

- 使用 `let`，如我们在这里所做的。在 OpenSesame 中，这使 JavaScript 可以使用该变量，但在用户界面中不能将其作为实验变量。
- 使用 `var`。在 OpenSesame 中，这使电子界面中的实验变量也可以使用该变量。(稍后我们将对 correct_response 变量进行此操作。)
- 使用 `const`。 这与 `var` 类似，但重要区别在于变量不能在后面重新分配。

__准备和运行阶段__

打开 *search_display_script* 并切换到准备选项卡。OpenSesame 区分两个执行阶段：

- 在准备阶段，每个项目都可以准备自己; 每个项目的内容可能不同：对于 SKETCHPAD，这意味着绘制画布（但不显示）；对于 SAMPLER，这意味着加载声音文件（但不进行播放）。
- 在运行阶段，实际执行每个项目； 同样，这取决于项目的内容：对于 SKETCHPAD，这意味着显示之前准备好的画布；对于 SAMPLER，这意味着播放之前加载的音频文件。

对于 INLINE_JAVASCRIPT，您需要自己决定将什么放入准备阶段，什么放入运行阶段。在我们的案例中，是相当明确的：我们将准备阶段划分为绘制画布的代码，而运行阶段则用于显示画布（较小部分）。

参见：

- %link:prepare-run%


__实现抽象层次__

从最抽象的层次开始：定义一个绘制视觉搜索显示的功能。我们不详细说明如何做到这一点；我们只是假定有一个函数可以实现这一功能，然后我们将在之后详细考虑这个问题——这就是自顶向下编程。

在准备选项卡中输入以下代码：

```js
c = draw_canvas()
```

在这里发生了什么？我们...

- 调用 `draw_canvas()`，它返回一个我们将存储为 `c` 的 `Canvas` 对象；换句话说，`c` 是对应搜索显示器的 `Canvas` 对象。这就假定函数 `draw_canvas()` 存在，即使我们还没有定义它。

`Canvas` 对象是一个单独的显示器；在某种程度上，它是 SKETCHPAD 的 JavaScript 对等物。另请参阅：

- %link:manual/javascript/canvas%

现在，通过定义 `draw_canvas()` （在到目前为止的脚本之上）我们进一步详细说明：

```js
/**
 * 绘制搜索画布。
 * @return A Canvas
 **/
function draw_canvas() {
    let c = Canvas()
    let xy_list = xy_random(set_size, 500, 500, 75)
    if (target_present === 'present') {
        let [x, y] = xy_list.pop()
        draw_target(c, x, y)
    } else if (target_present !== 'absent') {
        throw 'target_present 的无效值 ' + target_present
    }
    for (let [x, y] of xy_list) {
        draw_distractor(c, x, y)
    }
    return c
}
```

在这里发生了什么？我们 …

- 使用工厂函数`Canvas()`创建一个空画布`c`。
- 使用另一个常用函数`xy_random()`生成一个随机的`x, y`坐标数组，称为`xy_list`。此数组决定了显示刺激的位置。位置从一个 500 × 500 px 的区域中采样，最小间距为 75 px。
- 检查实验变量`target_present`是否具有值'present'；如果是，则从`xy_list`中`pop()`一个`x, y`元组，并在此位置绘制目标。这里假设有一个函数`draw_target()`，尽管我们还没有定义它。
- 如果`target_present`既不是'present'也不是'absent'，我们会`throw`一个错误；这是防御性编程，并保护我们免受拼写错误（例如，如果我们错误地输入了'presenr' 而不是 'present'）。
- 遍历所有剩余的`x, y`值，并在每个位置绘制一个干扰物。这假设有一个函数`draw_distractor()`，尽管我们还没有定义它。
- 返回`c`，现在已经在其上绘制了搜索显示。

有几个常用函数，如`Canvas()`和`xy_random()`，它们在 INLINE_JAVASCRIPT 项中始终可用。请参阅：

- %link:manual/javascript/common%

实验变量是全局变量。这就是为什么您可以引用在 *block_loop* 中定义的`set_size`，即使在脚本中从未明确定义过变量 `set_size`。对于`target_shape`、`target_color`、`condition`等也是如此。请参阅：

- %link:var%


__实现中级层次__

现在我们再往下走一步，通过定义`draw_target`（在目前为止的剩余脚本之上）：

```js
/**
 * 绘制目标。
 * @param c 一个画布
 * @param x 一个x坐标
 * @param y 一个y坐标
 **/
function draw_target(c, x, y) {
    draw_shape(c, x, y, target_color, target_shape)
}
```

这里发生了什么？我们……

- 调用另一个函数`draw_shape()`，并指定需要绘制的颜色和形状。这假设有一个`draw_shape()`函数，尽管我们还没有定义它。

我们也定义`draw_distractor`（在目前为止的剩余脚本之上）：

```js
/**
 * 绘制单个干扰物。
 * @param c 一个画布
 * @param x 一个x坐标
 * @param y 一个y坐标
 **/
function draw_distractor(c, x, y) {
    if (condition === 'conjunction') {
        draw_conjunction_distractor(c, x, y)
    } else if (condition === 'feature_shape') {
        draw_feature_shape_distractor(c, x, y)
    } else if (condition === 'feature_color') {
        draw_feature_color_distractor(c, x, y)
    } else {
        throw 'Invalid condition: ' + condition
    }
}
```

这里发生了什么？我们……

- 根据条件调用另一个函数来绘制更具体的干扰物。
- 检查`condition`是否具有预期的值。如果没有，我们`throw`一个错误。这是防御性编程！否则，如果我们在某个地方犯了一个拼写错误，干扰物可能会在没有产生错误消息的情况下不显示。

现在我们定义一个用于绘制连接条件下的干扰物的函数（在目前为止的剩余脚本之上）：

```js
/**
 * 绘制连接条件下的单个干扰物：可以是任何形状和颜色的对象，但不能与目标相同。
 * @param c 一个画布。
 * @param x 一个x坐标。
 * @param y 一个y坐标。
 **/
function draw_conjunction_distractor(c, x, y) {
    let conjunctions = [
        ['yellow', 'circle'],
        ['blue', 'circle'],
        ['yellow', 'square'],
        ['blue', 'square']
    ]
    let [color, shape] = random.pick(conjunctions)
    while (color === target_color && shape === target_shape) {
        [color, shape] = random.pick(conjunctions)
    }
    draw_shape(c, x, y, color, shape)
}
```

这里发生了什么？我们 …

- 定义一个列表 `conjunctions`，包含所有可能的颜色和形状组合。
- 从 `conjunctions` 中随机选择一个颜色和形状组合。
- 检查所选的颜色和形状是否都等于目标的颜色和形状。如果是这样，继续选择新的颜色和形状，直到不再是这种情况。毕竟，干扰物不能与目标完全相同！
- 调用另一个函数 `draw_shape()`，并指定将绘制的干扰物的颜色和形状。这 assumes that there is a function `draw_shape()`，尽管我们尚未定义它。

此外, 我们 …

- 使用 `random` 库，它对应于 `random-ext` 包。此库包含有用的随机化函数（如 `random.pick()`）并且是与 OSWeb 一起包含的非标准 JavaScript 库之一。

现在我们定义在形状特征条件下绘制干扰物的函数（在到目前为止的脚本剩余部分的上方）：

```js
/**
 *在特征形状条件下绘制单个干扰物：一个与目标形状不同但可以是任何颜色的对象。
 * @param c 一个画布。
 * @param x 一个 x 坐标。
 * @param y 一个 y 坐标。
 **/
function draw_feature_shape_distractor(c, x, y) {
    let colors = ['yellow', 'blue']
    let color = random.pick(colors)
    let shape
    if (target_shape === 'circle') {
        shape = 'square'
    } else if (target_shape === 'square') {
        shape = 'circle'
    } else {
        throw 'Invalid target_shape: ' + target_shape
    }
    draw_shape(c, x, y, color, shape)
}
```

这里发生了什么？我们 ...

- 随机选择一种颜色。
- 如果目标是圆形，选择一个方形；如果目标是方形，选择一个圆形。
- 如果 `target_shape` 不是 'circle' 也不是 'square'，`throw` 一个错误—— 更多的防御性编程！
- 调用另一个函数，`draw_shape()`，并指定将绘制的干扰物的颜色和形状。这 assumes that there is a function `draw_shape()`，尽管我们尚未定义它。

(define the added part in remarks similar to previous and preserve rest same)
现在我们定义在颜色特征条件下绘制干扰物的函数：

```js
/**
 * 在特征颜色条件下绘制单个干扰物：一个与目标颜色不同但可以是任何形状的对象。
 * @param c 一个画布。
 * @param x 一个 x 坐标。
 * @param y 一个 y 坐标。
 **/
function draw_feature_color_distractor(c, x, y) {
    let shapes = ['circle', 'square']
    let shape = random.pick(shapes)
    let color
    if (target_color === 'yellow') {
        color = 'blue'
    } else if (target_color === 'blue') {
        color = 'yellow'
    } else {
        throw 'Invalid target_color: ' + target_color
    }
    draw_shape(c, x, y, color, shape)
}
```

这里发生了什么？我们 ...

- 随机选择一个形状。
- 如果目标是黄色，选择一个蓝色；如果目标是蓝色，选择一个黄色。
- 如果 `target_color` 不是 'yellow' 也不是 'blue'，`throw` 一个错误—— 更多的防御性编程！
- 调用另一个函数，`draw_shape()`，并指定将绘制的干扰物的颜色和形状。这 assumes that there is a function `draw_shape()`，尽管我们尚未定义它。

__实现详细级别__

现在我们通过定义实际将形状绘制到画布的函数，详细了解所有内容（在脚本剩余部分的上方）：

```js
/**
 * 绘制单个形状。
 * @param c 一块画布。
 * @param x x坐标。
 * @param y y坐标。
 * @param color 颜色（黄色或蓝色）
 * @param shape 形状（正方形或圆形）
 **/
function draw_shape(c, x, y, color, shape) {
    if (shape === 'square') {
        // 参数作为对象传递！
        c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
    } else if (shape === 'circle') {
        // 参数作为对象传递！
        c.circle({x:x, y:y, r:25, color:color, fill:true})
    } else {
        throw '无效的形状：' + shape
    }
    if (color !== 'yellow' && color !== 'blue') {
        throw '无效的颜色：' + color
    }
}
```

这里发生了什么？我们...

- 检查应该绘制哪个形状。对于正方形，我们在画布上添加一个`rect()`元素。对于圆形，我们添加一个`circle()`元素。
- 检查形状是否为正方形或圆形，如果不是就`throw`错误。这是防御式编程的另一个示例！我们确保我们没有意外地指定了一个无效的形状。
- 检查颜色是否不是黄色或蓝色，如果不是就`throw`错误。

重要的是，`Canvas`函数接受一个指定所有参数名称的单一对象（`{}`），如下所示：

```js
// 正确：传递一个包含所有参数名称的单一对象
c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
// 错误：不要按顺序传递参数
// c.rect(x-25, y-25, 50, 50, color, true)
// 错误：JavaScript不支持命名参数
// c.rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=true)
```

__实现运行阶段__

因为我们已经在准备阶段完成了所有繁重的工作，所以运行阶段只是：

```js
c.show()
```

就是这样！现在你已经画了一个完整的视觉搜索显示。而且，更重要的是，你是以一种容易理解的方式完成这方面的工作，因为自顶向下的编程，和保险起见，因为防御性编程。

## 步骤7：定义正确的响应

要知道参与者是否正确响应，我们需要知道正确的响应。您可以在 *block_loop* 中显式定义此响应（如初学者教程所示）；但在这里我们将使用一些简单的JavaScript检查目标是否存在，然后相应地定义正确的响应。

为此，我们首先需要在 *init* 脚本的准备标签下声明变量，就在 `let c` 下面。这次，我们使用 `var` 关键字声明 `correct_response`，因为这使变量在用户界面中可用（而 `let` 则不会这样做）：

```js
var correct_response
```

接下来，在 *trial_sequence* 的开始位置插入一个新的INLINE_JAVASCRIPT，并将其重命名为 *correct_response_script*。在准备阶段，输入以下代码：

```js
if (target_present === 'present') {
    correct_response = 'right'
} else if (vars.target_present === 'absent') {
    correct_response = 'left'
} else {
    throw 'target_present 应该是缺席或出席，而不是 ' + target
}
```

这里发生了什么？我们...

- 根据目标是否存在检查。如果目标存在，正确的响应是'right'（右箭头键）；如果目标不存在，则正确的响应是 'left'（左箭头键）。实验变量`correct_response`会被OpenSesame自动使用；因此，我们不需要明确表示这个变量包含正确的响应。
- 根据目标是否存在或缺席检查，如果不是就`throw`错误 — 这是另一个防御编程的例子。

## 步骤8：给每次试验反馈

每次试验后的反馈可以激励参与者；然而，每次试验的反馈不应干扰实验的流程。给每次试验反馈的好方法是在正确响应后简要显示绿色的凝视点，在错误响应后显示红色的凝视点。

要实现这一点：

- 将两个新的SKETCHPAD插入*trial_sequence*，紧接在*keyboard_response*之后。
- 将其中一个SKETCHPAD重命名为*green_dot*，在上面画一个中央绿色固定点，并将其持续时间更改为500。
- 将另一个SKETCHPAD重命名为*red_dot*，在上面画一个中央红色固定点，并将其持续时间更改为500。

当然，在每次试验中只应显示其中一个点。为此，我们将在*trial_sequence*中指定run-if语句：

- 将*green_dot*的run-if语句更改为'correct == 1'，表示只在正确响应后显示。
- 将*red_dot*的run-if语句更改为'correct == 0'，表示只在错误响应后显示。

如果变量`correct_response`可用，变量`correct`会自动创建；这就是为什么我们在第7步中定义了`correct_response`。有关变量和run-if语句的更多信息，请参阅：

- %link:manual/variables%

*trial_sequence* 现在应该如%FigStep8所示。

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  第8步结束时的*trial_sequence*。
--%


## 完成！

恭喜，实验完成了！您可以通过单击工具栏上显示绿色圆圈内的灰色播放按钮（快捷键：`Alt+Ctrl+W`）来进行测试运行。

如果实验第一次尝试没有成功：不要担心，并冷静地找出错误的来源。崩溃是正常开发过程的一部分。但是，通过有序的工作方式，您可以节省大量时间和麻烦，就像我们在本教程中所做的那样。

## 参考文献

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[参考文献]: #参考文献
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
