title: 威斯康星卡片分类测验
hash: c76af36f9cc3e81cddcf0d468272405a3bebc0c73931400b287f211d586c3db3
locale: zh
language: Chinese

[TOC]


## 基本步骤


%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  威斯康星卡片分类测验（WCST）是一种神经心理测试，测试执行功能。
--%


在本教程中，您将实现威斯康星卡片分类测试（WCST），并了解如何使用 OSWeb 在线运行此测试。

在 WCST 中，参与者会看到四张刺激卡片，卡片在三个维度上有所不同：颜色（红、绿、蓝、黄），形状（圆形、星形、三角形、十字形）和形状数量（一、二、三、四）。参与者还会看到一张响应卡，它也有颜色、形状和数量。

参与者的任务是根据特定维度（例如 颜色）或 *匹配规则* ，将响应卡与正确的刺激卡相匹配。参与者最初不知道要根据哪个维度进行匹配，他们的任务是通过试错来找出匹配规则。

更难的是，每五次正确响应后，匹配规则都会发生改变。因此，参与者需要灵活地更新他们的匹配规则。


### 步骤 1：下载并启动 OpenSesame

OpenSesame 可以在 Windows、Linux 和 Mac OS 上使用。本教程适用于 OpenSesame 4.0 及更高版本。

启动 OpenSesame 时，您将可以选择模板实验，并（如果有的话）看到最近打开实验的列表（请参见 %FigStartUp）。

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  启动时的 OpenSesame 窗口。
--%

“扩展模板”为创建使用块试验结构的许多实验提供了良好的起点。但是，在本教程中，我们将从头开始创建整个实验，并使用已经加载的“默认模板”（%FigDefaultTemplate）。因此，只需关闭“开始！”和（如果显示）“欢迎！”选项卡。

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  在概览区域中看到的“默认模板”的结构。
--%


### 步骤 2：添加 block_loop 和 trial_sequence

默认模板开始时有三个项目：一个名为 *getting_started* 的 NOTEPAD，一个名为 *welcome* 的 SKETCHPAD 和一个名为 *experiment* 的 SEQUENCE。我们不需要 *getting_started* 和 *welcome*，所以先删掉它们。右键单击这些项目，然后选择“删除”。不要删除 *experiment*，因为它是实验的开始入口（即在实验开始时调用的第一个项目）。

我们的实验将具有非常简单的结构。在层次结构的顶部是一个我们称为 *block_loop* 的 LOOP。*block_loop* 是我们将定义独立变量的地方。要将 LOOP 添加到实验中，请将 LOOP 图标从项目工具栏拖到概览区域中的 *experiment* 项目上。

LOOP 项目需要另一个项目来运行；通常情况下，在这种情况下也是这样，这是一个 SEQUENCE。将 SEQUENCE 项目从项目工具栏拖到概览区域中的 *new_loop* 项目上。OpenSesame 会询问您是否要将 SEQUENCE 插入到 LOOP 或之后。选择“插入到 new_loop”。

默认情况下，项目具有 *new_sequence*、*new_loop*、*new_sequence_2* 等名称。这些名称并不是很具有说明性，最好对它们进行重命名。项目名称必须由字母数字字符和/或下划线组成。要重命名项目，请双击概览区域中的项目。将 *new_sequence* 重命名为 *trial_sequence*，以表示它将对应一个试验。将 *new_loop* 重命名为 *block_loop*，以表示它将对应一个试验块。

最后，单击“新建实验”以打开常规属性选项卡。单击实验的名称，并将其重命名为“威斯康星卡片分类测试”。

我们实验的概览区域现在看起来像 %FigBasicStructure。

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  第2步完成后的概述区域。
--%


### 步骤3：导入图像和声音文件

对于这个实验，我们将使用扑克牌的图像。您可以从这里下载它们：

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

下载 `stimuli.zip` 并将其提取到某个地方（例如桌面）。接下来，在OpenSesame中，单击主工具栏中的"显示文件池"按钮（或：菜单→视图→显示文件池）。这将显示文件池，默认情况下在窗口的右侧。将刺激物从桌面（或您提取的文件位置）拖到文件池中，是将它们添加到文件池的最简便方法。或者，您可以单击文件池中的"+"按钮，通过出现的文件选择对话框添加文件。文件池将自动与您的实验一起保存。

添加所有刺激物后，您的文件池看起来像 %FigFilePool。

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  包含刺激物的文件池。
--%


### 步骤4：创建静态卡片显示

首先，我们将创建一个带有四个刺激卡片和一个响应卡片的显示。然而，这里展示的卡牌不会依赖于变量；也就是说，我们将创建一个*静态*显示。

将 SKETCHPAD 拖到 *trial_sequence* 中，并将其重命名为 *card_display*。使用图像工具在显示顶部附近的水平行上绘制四张卡片；这将是刺激卡片。在显示底部附近绘制一张单独的卡片；这将是响应卡片。还要添加一些文字，以示参与者他或她要做什么，即按 `a`、`b`、`c` 或 `d` 来表示刺激卡片中哪张与响应卡片相匹配。具体的文字、布局和卡片由您决定！提示：您可以使用 *scale* 选项调整卡片的尺寸；您可以在"通用属性"选项卡中更改背景颜色，通过点击实验的顶级项目打开通用属性选项卡。

对于我，结果看起来像这样：


%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  具有静态定义卡片的SKETCHPAD。
--%


### 步骤5：使响应卡片可变

现在我们总是显示相同的响应卡片（在上面的示例中是一个蓝色的三角形）。但是我们当然希望在每次试验中显示不同的响应卡片。为此，我们首先需要在 *block_loop* 中定义决定哪个响应卡片我们将展示的变量。

打开 *block_loop*。LOOP 表现在是空的。要确定响应卡片的颜色、形状和数量，我们可以手动创建三列（`response_color`、`response_shape` 和 `response_number`）和64行，用于所有可能的颜色、形状和数量的组合。但这将是大量的工作。相反，我们将使用全因素设计向导，您可以通过点击"全因素设计"按钮来打开它。（全因素设计是一种所有可能的变量水平组合都出现的设计。）在此向导中，为这三个变量中的每一个创建一列，在下面的单元格中输入该变量的可能值（详见%FigDesignWizard）。

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  全因素设计向导允许您轻松生成对应于全因素设计的大型LOOP表。
--%

接下来，点击“确定”按钮。*block_loop* 现在包含所有64种颜色、数字和形状的组合（详见 %FigLoopTable1）。

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  第5步结束时的*block_loop*。
--%

现在回到 *card_display*。OpenSesame 中的每个项目都通过脚本定义。这个脚本是由用户界面自动生成的。有时直接编辑这个脚本会很方便（甚至是必要的）。编辑项目脚本的最常见原因是向脚本添加变量，这也是我们现在要做的！

要查看脚本，请点击 "View" 按钮并选择 "View script"。（查看按钮位于项目控件右上角的中间按钮。）这将打开一个脚本编辑器。

*card_display* 的脚本主要由 `draw` 命令组成，这些命令定义了五张卡片以及各种文本元素。找到与响应卡对应的行。您可以通过查看 Y 坐标来找到它，这应该是正的（即显示屏的下部），或者通过查看图像文件的名称。

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

现在，在我的例子中，响应卡的图像文件始终是 `"1-blue-triangle.png"`。但是当然我们并不总是想要显示一个蓝色的三角形。相反，我们希望图像文件取决于我们在 *block_loop* 中定义的变量。为此，请将数字替换为 `{response_number}`，颜色替换为 `{response_color}`，形状替换为 `{response_shape}`：(大括号表示这些是变量名的引用。)

```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

点击 Apply 以接受对脚本的更改。响应卡现已被一个问号图标替换。这是因为 OpenSesame 不知道如何显示使用变量定义的图像的预览。但别担心：当你运行实验时，图像将被显示！

### 步骤6：使刺激卡片可变

刺激卡片应该或多或少是随机选择的，但每种颜色、形状和数字只出现一次；也就是说，不能有两张红色卡片或两张带三角形的卡片。（如果有，匹配程序将变得模糊不清。）为了实现这一点，我们可以使用 *横向洗牌*，这是 LOOP 项目中功能强大但不同寻常的一个功能。

- %link:loop%

首先，打开 *block_loop* 并创建12个（！）新列来定义刺激卡片：`color1`，用于第一张卡片的颜色，`color2`，`color3`，`color4`，以及`shape1`...`shape4`，`和number1`...`number4`。 每个列在每一行上都有相同的值（见 %FigLoopTable2）。

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  步骤 6 时的 *block_loop*。
--%

但我们还没有完成！现在，第一张刺激卡总是一个单独的红圈，第二张是两个蓝三角形等。为了实现这一点，我们告诉 OpenSesame 随机交换（水平洗牌）四个颜色变量、四个形状变量和四个数字变量的值。为此，请打开 *block_loop* 的脚本。在倒数第二行（在 `run trial_sequence` 之前）添加以下命令：

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

点击 Apply 以接受脚本。要查看是否起作用，请点击预览按钮。这将显示实验期间 LOOP 表将如何随机化的预览。看起来不错吗？

现在回到 *card_display*，让第一张刺激卡的图像取决于变量 `color1`、`shape1` 和 `number1`，对其他刺激卡也是如此。 （如果您不确定如何做，请重新看一下步骤5。）

### 步骤7：确定正确的响应（对于一个匹配规则）

现在，我们假设参与者始终按形状匹配。（改进的一个额外任务是这样的。）

现在，*card_display* 的持续时间设置为 'keypress'。这意味着 *card_display* 将一直显示，直到按下一个键，但它并没有控制如何处理这个按键。因此，将持续时间更改为 0，并在 *card_display* 之后立即插入键盘响应。将键盘响应重命名为 *press_a*，并指定正确的响应是 'a'，允许的响应是 'a;b;c;d'。

%--
figure:
 id: FigPressA
 source: press-a.png
 caption: |
  在第 7 步中定义的一个键盘响应项。
--%

但这还不够！现在有一个假设正确响应总是 'a' 的单一响应项。我们还没有指定 *何时* 正确的响应是 'a'，也没有考虑到正确响应为 'b'、'c' 或 'd' 的试验。

为了实现这一点，首先创建另外三个键盘响应项： *press_b*，*press_c* 和 *press_d*。它们的区别仅在于正确的响应，这是分别为 'b'、'c' 和 'd' 的每个单独定义。

最后，在 *trial_sequence* 中，使用 Run If 语句来决定在哪种条件下应执行四个键盘响应项之一（从而决定正确的响应是什么）。对于 *press_a*，条件是 `shape1` 应等于 `response_shape`。为什么？因为这意味着第一个刺激卡片的形状等于响应卡片的形状，在这种情况下，正确的响应是 'a'。这个条件对应于以下运行 if 语句：`shape1 = response_shape`。其他键盘响应项的运行 if 语句类似（见 %FigTrialSequence1）。

%--
figure:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 caption: |
  第 7 步结束时的 *trial_sequence*。
--%

### 第 8 步：给参与者反馈

OpenSesame 会自动记录响应是正确还是错误，分别将变量 `correct` 设置为 1 或 0。（当然，前提是你已经指定了正确的响应，就像我们在第 7 步中做的那样。）我们可以用这个来告诉参与者他们的反应是正确还是错误。

为此，在 *trial_sequence* 中添加两个新的 SKETCHPAD 并将其命名为 *correct_feedback* 和 *incorrect_feedback*。然后，使用运行 if 语句指定应执行哪一个（请参见 %FigTrialSequence2）。

%--
figure:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 caption: |
  第 8 步结束时的 *trial_sequence*。
--%

最后，为这两个 SKETCHPAD 添加一些有用的内容。例如，对于 *correct_feedback* 你可以使用绿色的定位点，对于 *incorrect_feedback* 你可以使用红色的定位点，两种情况下都显示 500 毫秒（即将 SKETCHPAD 的持续时间设置为 500）。彩色的小点是一种不引人注意的反馈方法。

### 第 9 步：测试实验

您现在已经创建了威斯康星卡片分类测试的基本（但不完整！）实施。（作为以下额外任务的一部分，您将完成实施。）

要测试实验，您可以单击快速运行按钮（蓝色双箭头）或全屏运行按钮（绿色箭头）。

## 额外任务

### 额外 1（简单）：添加记录器

OpenSesame 不会自动记录数据。相反，您需要为实验显式添加 `logger` 项目。在基于试验的实验中，`logger` 通常是 *trial_sequence* 的最后一项，以便记录在试验期间收集的所有数据。

现在，我们的 WCST 不记录任何数据。是时候解决这个问题了！

### 额外 2（简单）：检查数据文件

*需要您完成了 Extra 1*。

对实验进行简短的测试运行。现在用类似 Excel、LibreOffice Calc 或 JASP 的程序检查日志文件。确定相关变量，思考您如何分析结果。

__Pro-tip:__ 将 *block_loop* 的重复值设置为0.1，以在测试过程中减少试次数。

### 额外 3 (简单)：添加说明和告别屏幕

一个好的实验需要明确的说明。一个礼貌的实验会在参与者完成实验时向他们表示再见。您可以使用 SKETCHPAD 或 FORM_TEXT_DISPLAY 来实现这一点。

### 额外 4 (中等)：通过 JavaScript 设置正确的响应和匹配规则

要在 OSWeb 中包含脚本，您可以使用 INLINE_JAVASCRIPT 项目，它支持 JavaScript。 (但是它目前还不提供常规 Python INLINE_SCRIPT 中提供的所有功能！)关于详细信息，请参考[这里](https://osdoc.cogsci.nl/4.0/manual/javascript/about/)。

到目前为止，匹配规则始终是通过形状进行匹配。要改变这一点，将 INLINE_JAVASCRIPT 项目添加到实验开始，并使用以下脚本（在 *prepare* 阶段）将变量 `matching_rule` 随机设置为 'shape'，'number' 或 'color'。

```javascript
function choice(choices) {
    // JavaScript 没有内置的选择功能，所以我们在这里定义它
    // 使用 let 引入一个临时新变量
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}


// 使用 var 引入一个全局新变量
var matching_rule = choice(['shape', 'number', 'color'])
```

现在将另一个 INLINE_JAVASCRIPT 项目添加到 *trial_sequence* 的开始。在 *prepare* 阶段，添加一个脚本将 `correct_response` 变量设置为 'a'，'b'，'c' 或 'd'。为此，您需要一系列 `if` 语句，首先查看匹配规则，然后查看哪个形状对应于反应形状（对于形状匹配规则）或哪种颜色对应于反应颜色（对于颜色匹配规则）等。

以下是解决方案的一部分（但需要完成！）：

```javascript
if (matching_rule === 'shape') {
    if (shape1 === response_shape) correct_response = 'a'
    // 还没完成
} // 还没完成

// 在调试窗口中打印一些信息
console.log('matching_rule = ' + matching_rule)
console.log('correct_response = ' + correct_response)
```

### 额外 5 (困难)：定期更改匹配规则

到目前为止，实验开始时随机确定匹配规则，然后在整个实验中保持不变。在真正的 WCST 中，匹配规则会定期更改，通常是在参与者做出固定数量的正确响应后。

要实现这一点，您需要另一个 INLINE_JAVASCRIPT。以下是一些指针来开始：

- 使用一个计数器变量，在正确响应后增加 1，在错误响应后重置为 0。
- 更改匹配规则时，请确保它不会（纯粹是个巧合）再次设置为相同的匹配规则。

### 额外 6 (非常困难)：限制响应卡

现在，响应卡可以在多个维度上与刺激卡重叠。例如，如果刺激卡之一是一个蓝色的圆圈，响应卡可能是两个蓝色的圆圈，从而在颜色和形状上都重叠。在真正的 WCST 中，响应卡与每个刺激卡在不超过一个维度的情况下重叠。

这次就交给你了。这次没有提示！

### 额外 7 (简单): 使用 JATOS 在线运行实验

我们的 WCST 与 OSWeb 兼容，这意味着您可以在浏览器中运行它。要测试这是否仍然有效，您可以在实验项目的通用属性选项卡中选择 OSWeb 后端。选择后，只需点击绿色按钮，实验将在您的默认浏览器中启动。

然而，要为您的研究收集实际数据，您需要将实验导入 JATOS，并使用 JATOS 生成一个可分发给参与者的链接。这比听起来容易得多！更多信息，请参考：

- %link:manual/osweb/workflow%

您可以从这里下载完整的实验，包括额外任务的解决方案：

- <https://osf.io/f5er2/>