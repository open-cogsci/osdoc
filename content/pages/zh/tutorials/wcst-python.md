title: 威斯康星卡片分类测验
uptodate: false
hash: 62801ccad4fe18407f604f09c0a01cdc6bafc8cd4b09f38777af7ebaa44f1c71
locale: zh
language: Chinese

[TOC]


## 基本步骤

%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  威斯康辛卡片分类测验（WCST）是一种神经心理学检测执行功能的方法。
--%

在本教程中，您将实现威斯康辛卡片分类测验（WCST）。您还将学习如何在实验中嵌入Python代码。 (有关此任务的OSWeb实现,请参阅[本教程](％url:wcst％))。

在WCST中，参与者会看到四张刺激卡片，这些卡片在三个维度上有所不同：颜色（红、绿、蓝、黄）、形状（圆、星、三角、十字）和形状数量（一、二、三、四）。参与者还会看到一张单独的回应卡，其中也包含颜色、形状和数量。

参与者的任务是根据特定维度（例如颜色）或*匹配规则*将回应卡与正确的刺激卡进行匹配。参与者最初并不知道应根据哪个维度进行匹配，他或她的任务是通过反复试验来找出匹配规则。

为了增加难度，在每五个正确回应后，匹配规则会发生变化。因此，参与者需要灵活地更新他们的匹配规则。



### 第1步：下载并启动OpenSesame

OpenSesame适用于Windows、Linux和Mac OS。本教程适用于OpenSesame 3.2及更高版本。

当您启动OpenSesame时，您将可以选择实验模板，并且（如果有）还可以看到最近打开的实验列表(见%FigStartUp)。

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  启动OpenSesame窗口.
--%

*扩展模板* 为您创建具有块-试验结构的许多实验提供了一个很好的起点。然而，在本教程中，我们将从头开始创建整个实验，我们将使用“默认模板”，在启动OpenSesame时已经加载了（%FigDefaultTemplate)。因此，只需关闭'开始'和（如果显示）'欢迎'标签。

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  默认模板的结构如概览区所示。
--%

### 第2步： 添加一个block_loop和 trial_sequence

默认模板从三个项目开始：一个名为 *getting_started* 的便签，一个名为 *welcome* 的草图版，和一个名为 *experiment* 的序列。我们不需要 *getting_started* 和 *welcome*，所以现在就让我们去掉它们。为此，请右键单击这些项目并选择"删除"。不要删除 *experiment* ，因为它是实验的入口（即实验开始时调用的第一个项目）。

我们的实验将具有非常简单的结构。最顶层是一个名为 *block_loop* 的循环。 *block_loop* 是我们定义独立变量的地方。要将循环添加到实验中，请将不翻译项工具栏上的循环图标拖动到概览区域中的 *experiment* 模块上。

一个循环项目需要另一个项目来运行；通常，在这种情况下，这也是一个序列。将不翻译项工具栏上的序列项拖动到概览区域中的 *new_loop* 项目上。OpenSesame会询问您是否要将序列插入循环中还是在循环后。选择'插入到new_loop中'。

默认情况下，项目具有诸如 *new_sequence*，*new_loop*，*new_sequence_2* 等命名。这些名称并不是很具信息性，而且将它们重新命名是一种好习惯。项目名称必须由字母数字字符和/或下划线组成。要重命名项目，请双击概览区域中的项目。将 *new_sequence* 重命名为 *trial_sequence* ，以表示它将对应单个试验。将 *new_loop* 重命名为 *block_loop*，以表示它将对应一组试验。

最后，点击“新实验”以打开“常规属性”选项卡。点击实验的标题，将其重命名为“威斯康星随机卡片排序测验”。

我们实验的概述区现在看起来像%FigBasicStructure。

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  第2步结束时的概述区域。
--%


### 步骤3：导入图像和声音文件

对于这个实验，我们将使用扑克牌的图像。您可以从这里下载：

-%static:attachments/wisconsin-card-sorting-test/stimuli.zip%

下载`stimuli.zip`并将其提取到某个地方（例如，桌面上）。接下来，在OpenSesame中，单击主工具栏上的“显示文件池”按钮（或：菜单→视图→显示文件池）。这将显示文件池，默认情况下位于窗口右侧。将刺激物添加到文件池的最简单方法是将它们从桌面（或您提取文件的任何地方）拖放到文件池中。或者，您可以点击文件池中的“+”按钮，然后使用出现的文件选择对话框添加文件。文件池将自动与您的实验一起保存。

添加完所有刺激物后，您的文件池看起来像%FigFilePool。

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  包含刺激物的文件池。
--%


### 步骤4：创建静态卡片显示

首先，我们将创建一个包含四个刺激卡和一个响应卡的显示屏。然而，显示的卡片将不会取决于变量；也就是说，我们会创建一个*静态*显示屏。

将SKETCHPAD拖放到*trial_sequence*中，并将其重命名为*card_display*。使用图像工具在显示屏顶部附近的水平行上绘制四张卡片；这些将是刺激卡片。在显示屏底部附近绘制一张卡片；这将是响应卡。另外添加一些文本，告知参与者需要执行的操作，即按`a`、`b`、`c`或`d`表示哪张刺激卡与响应卡相匹配。具体的文本、布局和卡片由您决定！提示：您可以使用*scale*选项调整卡片大小；您可以通过点击实验顶级项目来打开通用属性选项卡，然后在其中更改背景颜色。

对我来说，结果如下：


%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  具有静态定义卡片的SKETCHPAD。
--%


### 步骤5：使响应卡变量化

现在我们总是显示相同的响应卡（在上面的例子中是一个蓝色三角形）。但当然，我们希望在每次试验中显示不同的响应卡片。为此，我们首先需要定义决定我们将显示哪个响应卡片的变量。我们将在*block_loop*中定义这些变量。

打开*block_loop*。LOOP表格现在为空。为了确定响应卡片的颜色、形状和数量，我们可以手动创建三列（`response_color`，`response_shape`和`response_number`）和64行，用于所有可能的颜色、形状和数字组合。但那将是很多工作。相反，我们将使用全因子设计向导，您可以通过点击“全因子设计”按钮打开它。（全因子设计是指所有可能的变量级别组合都出现的设计。）在这个向导中，为这三个变量中的每一个创建一列，并在下面的单元格中输入该变量的可能值（见%FigDesignWizard）。

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  全因子设计向导让您能够轻松生成对应于全因子设计的大型LOOP表格。
--%


接下来，点击确定按钮。*block_loop*现在包含了所有64个颜色、数字和形状的组合（见%FigLoopTable1）。

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  第5步结束时的*block_loop*。
--%

现在返回到 *card_display*。OpenSesame 中的每个项目都通过脚本定义。这个脚本是由用户界面自动生成的。有时直接编辑脚本可能会方便（甚至有必要）。编辑项目脚本的最常见原因是在脚本中添加变量，也正是我们现在要做的！

要查看脚本，请单击“View”按钮并选择“View script”。 (查看按钮位于项目控件右上角中间位置。) 这将打开脚本编辑器。

*card_display* 的脚本主要由 `draw` 命令组成，这些命令定义了五个卡片及不同文本元素。查找与响应卡片对应的行。你可以通过查看 Y 坐标（应为正值，即位于显示的底部）或查看图像文件名来找到它。

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

现在，在我的示例中，响应卡的图像文件始终为 "1-blue-triangle.png "。但当然我们并不总是想展示一个蓝色的三角形。相反，我们希望让图像文件依赖于我们在 *block_loop* 中定义的变量。要这样做，请将数字替换为 `[response_number]`，颜色替换为 `[response_color]`，形状替换为 `[response_shape]`：(方括号表示这些是变量名。)

```
draw image center=1 file="[response_number]-[response_color]-[response_shape].png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

点击 Apply 以接受脚本更改。响应卡现在被一个问号图标替换。这是因为 OpenSesame 不知道如何显示使用变量定义的图像预览。但别担心：当你运行实验时，图像会显示出来！


### 第6步：使刺激卡片具有变量性质

刺激卡片应该在很大程度上随机选择，但每种颜色、形状和数目只出现一次；也就是说，不应有两张红卡或两张带三角形的卡片。(如果有，匹配程序将变得模糊不清。)为了实现这一点，我们可以使用 *水平混洗*，这是 LOOP 项目的一个功能强大但不寻常的功能。

-%link:loop%

首先，打开 *block_loop* 并创建12（！）新列以定义刺激卡片：`color1`，用于第一张卡片的颜色，`color2`，`color3`，`color4`，以及 `shape1` ... `shape4`，和 `number1` ... `number4`。每列在每行都有相同的值（请参见 %FigLoopTable2）。

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  步骤6期间的 *block_loop*。
--%

但我们还没有完成！现在，第一张刺激卡片始终是一个红圈，第二张是两个蓝三角形，等等。要打乱这个顺序，我们告诉 OpenSesame 随机交换四个颜色变量、四个形状变量和四个数字变量的值。 为此，请打开 *block_loop* 的脚本。在倒数第二行（在 `run trial_sequence` 之前）添加以下命令：

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

点击 Apply 以接受脚本。 要查看是否有效，点击预览按钮。 此操作将显示实验期间 LOOP 表格的随机预览。 是不是看起来还不错？

现在返回到 *card_display*，并使第一张刺激卡的图像依赖于变量 `color1`、`shape1` 和 `number1`，其他刺激卡片以类似方式处理。(如果你不确定如何操作，请重新阅读第5步。)


### 第7步：确定正确的响应（针对一种匹配规则）

现在，我们假设参与者总是根据形状进行匹配。(改进这个问题的附加任务之一。)

现在，*card_display* 的持续时间设置为 'keypress'。这意味着 *card_display* 会显示直到有键被按下，但它不控制如何处理这个按键。因此，将持续时间更改为 0，并在 *card_display* 之后直接插入一个 KEYBOARD_RESPONSE。将 KEYBOARD_RESPONSE 重命名为 *press_a*，并指定正确的响应是 'a'，允许的响应是 'a;b;c;d'。

%--
图:
 id: FigPressA
 source: press-a.png
 caption: |
  在步骤 7 中定义的一个 KEYBOARD_RESPONSE 项目。
--%


但这还不够！现在有一个单独的响应项，假设正确的响应总是 'a'。我们还没有指定正确答案是 'a' 的*何时*，也没有考虑到正确答案为 'b'，'c' 或 'd' 的试验。

要做到这一点，首先创建另外三个 KEYBOARD_RESPONSE 项目：*press_b*，*press_c* 和 *press_d*。这些都是一样的，除了正确的响应，它们分别单独定义为 'b'，'c' 和 'd'。

最后，在 *trial_sequence* 中，使用 Run If 语句来决定在哪种条件下执行四个 KEYBOARD_RESPONSE 项目中的每一个（从而决定正确的响应是什么）。对于 *press_a*，条件是 `shape1` 应等于 `response_shape`。为什么？好吧，因为这意味着第一个刺激卡的形状等于响应卡的形状，而在这种情况下正确的响应是 'a'。这个条件对应于以下 run-if 语句：`[shape1] = [response_shape]`。其他 KEYBOARD_RESPONSE 项目的 run-if 语句是类似的（见 %FigTrialSequence1）。

%--
图:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 caption: |
  步骤 7 结束时的 *trial_sequence*。
--%


### 步骤 8：向参与者提供反馈

只要你指定了正确的响应（正如我们在步骤 7 中所做的），OpenSesame 就会自动跟踪一个响应是否正确，分别将变量 `correct` 设置为 1 或 0。我们可以利用这一点向参与者提供关于他们是否正确回答的反馈。

为此，在 *trial_sequence* 中添加两个新的 SKETCHPAD，分别称为 *correct_feedback* 和 *incorrect_feedback*。然后，使用 run-if 语句指定在哪种情况下应执行这两者之一（见 %FigTrialSequence2）。

%--
图:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 caption: |
  步骤 8 结束时的 *trial_sequence*。
--%


最后，为两个 SKETCHPAD 添加一些有用的内容。例如，对于 *correct_feedback*，您可以使用一个绿色的凝视点，对于 *incorrect_feedback*，您可以使用一个红色的凝视点，两种情况都显示500毫秒（即将 SKETCHPAD 持续时间设为 500）。彩色的凝视点是提供反馈的好方法。

### 步骤 9：测试实验

现在，您已经创建了威斯康星卡片分类测试的基本（但不完整！）实现。（您将作为下面的额外任务完成实现部分。）

%--
图：
 id: FigRunButtons
 source: run-buttons.png
 caption: |
  主工具栏包含按钮（从左到右）：全屏运行，窗口运行，快速运行（在窗口中运行，不询问日志文件或参与者编号），中止实验和在浏览器中运行。
--%


要测试实验，请单击快速运行按钮（蓝色双箭头）在桌面上测试实验（见 %FigRunButtons）。如果实验在桌面上按预期运行，请单击运行至浏览器按钮（绿色圆圈内的箭头）在浏览器中运行实验。

## 额外任务

### 额外1 (简单): 添加记录器

OpenSesame不会自动记录数据。相反，您需要在实验中显式添加一个`logger`项目。在试验为基础的实验中，`logger`通常是*trial_sequence*的最后一个项目，因此它记录在试验期间收集的所有数据。

现在，我们的WCST不记录任何数据。是时候解决这个问题了！


### 额外2（简单）：检查数据文件

*要求您已完成额外1*。

为实验进行简短的测试运行。现在使用Excel、LibreOffice Calc或JASP等程序检查日志文件。找出相关变量，并思考如何分析结果。

__专业提示：__将*block_loop*的重复值设置为0.1，以减少测试期间的试验次数。


### 额外3（简单）：添加说明和告别屏幕

一个好的实验需要清晰的说明。礼貌的实验会在完成后告别参与者。您可以使用SKETCHPAD来实现这一目标。


### 额外4（中等）：通过Python内联脚本设置正确的响应和匹配规则

要在OpenSesame中包含Python脚本，您可以使用INLINE_SCRIPT项目。

到目前为止，匹配规则总是通过形状进行匹配。要更改此内容，请在实验开始时添加一个INLINE_SCRIPT项目，并使用以下脚本（在*prepare*阶段）随机将变量`matching_rule`设置为'shape'，'number' 或 'color'。

```python
import random

var.matching_rule = random.choice(['shape', 'number', 'color'])
```

现在，在*trial_sequence* 开始时添加另一个INLINE_SCRIPT项目。在*prepare*阶段，添加一个脚本来将`correct_response`变量设置为'a'，'b'，'c' 或 'd'。为此，您需要一系列`if`语句，首先查看匹配规则，然后查看哪个形状对应于响应形状(对于形状匹配规则)或哪个颜色对应于响应颜色(对于颜色匹配规则)等。

以下是解决方案的一部分（但需要完成！）：

```python
if var.matching_rule == 'shape':
    if var.shape1 == var.response_shape:
        var.correct_response = 'a'
    # 还没有完成
# 还没有完成

# 让我们将一些信息打印到调试窗口
print('matching_rule = {}'.format(var.matching_rule))
print('correct_response = {}'.format(var.correct_response))
```


### 额外5（困难）：周期性地改变匹配规则

到目前为止，在实验开始时随机确定匹配规则，但在整个实验中保持不变。在真正的WCST中，匹配规则会周期性地改变，通常在参与者给出固定数量的正确答案后改变。

要实现这一点，您需要另一个INLINE_SCRIPT。以下是一些入门提示：

- 使用一个计数器变量，在给出正确答案后递增1，错误答案后重置为0。
- 当更改匹配规则时，确保它不是（恰巧）再次设置为相同的匹配规则。


### 额外6（非常困难）：限制响应卡

现在，响应卡可以在多个维度上与刺激卡重叠。例如，如果其中一个刺激卡是一个蓝色圆圈，响应卡可能是两个蓝色圆圈，从而在颜色和形状上都有重叠。在真正的WCST中，响应卡与每个刺激卡的重叠度不应超过一个维度。

这次没有提示，这个问题交给你解决！


## 解决方案

您可以从这里下载完整的实验，包括额外任务的解决方案：

- <https://osf.io/f5er2/>