title: 威斯康星卡片分类测验
hash: 4199e2aea0b73c7c2aec2a427017e0f2de9ffa30a72377e12ed75900a1fbc9a1
locale: zh
language: Chinese

[TOC]

## 基本步骤

%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  威斯康星卡片分类测验（WCST）是对执行功能的神经心理测试。
--%

在本教程中，您将实现威斯康星卡片分类测验（WCST）。您还将学习如何在实验中嵌入Python代码。（关于此任务的OSWeb实现，请参阅[此教程](%url:wcst%)）。

在WCST中，参与者会看到四张刺激卡片，这些卡片在三个维度上有所不同：颜色（红色、绿色、蓝色、黄色）、形状（圆形、星形、三角形、十字形）以及图形数量（一、二、三或四）。参与者还会看到一张回应卡片，该卡片也有颜色、形状和数量。

参与者的任务是根据特定维度（例如颜色）或 *匹配规则* 将响应卡与正确的刺激卡进行匹配。最初，参与者不知道要在哪个维度上进行匹配，他们的任务是通过试误来找出匹配规则。

为了增加难度，在每五个正确响应之后，匹配规则都会发生变化。因此，参与者需要灵活地更新匹配规则。

### 步骤1：下载并启动OpenSesame

OpenSesame适用于Windows、Linux和Mac OS。本教程适用于OpenSesame 4.0或更高版本。

启动OpenSesame后，您可以选择模板实验，并且（如果有的话）会看到最近打开的实验列表（参见%FigStartUp）。

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  启动时的OpenSesame窗口。
--%

*Extended template* 对于创建使用区块试验结构的许多实验来说是一个很好的起点。然而，在本教程中，我们将从头开始创建整个实验，我们将使用已经加载的 "default template"（默认模板）（%FigDefaultTemplate）。所以，只需关闭 "Get started!" 和（如果显示） "Welcome!" 标签。

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  在概述区域中看到的“默认模板”的结构。
--%

### 步骤2：添加block_loop和trial_sequence

默认模板提供了三个项目：一个名为 *getting_started* 的NOTEPAD，一个名为 *welcome* 的SKETCHPAD以及一个名为 *experiment* 的SEQUENCE项目。我们不需要 *getting_started* 和 *welcome*，因此立即将它们删除。要执行此操作，请右键单击这些项目并选择“删除”。不要删除 *experiment*，因为它是实验的入口(即实验开始时调用的第一个项目)。

我们的实验将具有非常简单的结构。在层次结构的顶部是一个LOOP，我们将其命名为 *block_loop*。*block_loop* 是我们定义自变量的地方。要将 LOOP 添加到实验中，请将 ITEM 工具栏上的 LOOP 图标拖到概览区域的 *experiment* 项目上。

一个LOOP项目需要另一个项目来运行;通常情况下，以及在这种情况下，这是一个SEQUENCE项目。将ITEM 工具栏上的 SEQUENCE 图标拖到概览区域中的 *new_loop* 上。OpenSesame会询问您是否要将SEQUENCE插入到LOOP中还是插入到LOOP后。选择 "插入到new_loop"。

默认情况下，项目的名称如 *new_sequence*，*new_loop*，*new_sequence_2* 等。这些名称并不具有很好的信息性，因此最好对它们进行重命名。项目名称必须由字母数字字符和/或下划线组成。要重命名项目，请双击概览区域中的项目。将 *new_sequence* 重命名为 *trial_sequence* 表示它将对应一个试验。将 *new_loop* 重命名为 *block_loop*，表示它将对应一个试验区块。

最后，点击"New Experiment"以打开"General Properties "标签。点击实验的标题，将其重命名为"威斯康星卡片分类测验"。

实验的概述区域现在看起来如在%FigBasicStructure。

%--
图：
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  第2步结束时的概述区域。
--%


### 步骤3：导入图片和声音文件

对于这个实验，我们将使用扑克牌的图片。您可以从这里下载：

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

下载 `stimuli.zip` 文件并将其解压缩到某个地方（例如您的桌面）。接着，在OpenSesame中，点击主工具栏上的“显示文件池”按钮（或：菜单→视图→显示文件池）。这将在窗口右侧显示文件池。将刺激物从桌面（或您解压缩文件的地方）拖到文件池中是将刺激物添加到文件池中的最简单方法。另外，您可以点击文件池中的“+”按钮，然后使用出现的文件选择对话框添加文件。文件池将自动保存在您的实验中。

添加完所有刺激物后，您的文件池看起来如在%FigFilePool。

%--
图：
 id: FigFilePool
 source: file-pool.png
 caption: |
  包含刺激物的文件池。
--%


### 步骤4：创建一个静态的纸牌展示

首先，我们将创建一个带有四张刺激卡片和一张响应卡片的显示。然而，现在，显示的卡片并不取决于变量；也就是说，我们将创建一个*静态*显示。

将SKETCHPAD拖到 *trial_sequence*，并将其重命名为 *card_display*。使用图像工具在显示器顶部附近的水平行中绘制四张卡片；这些将是刺激卡。在显示器底部附近画一张卡片；这将是响应卡。还可以添加一些文本来告诉参与者他或她需要做什么，即按 `a`、`b`、`c` 或 `d` 指示哪张刺激卡与响应卡匹配。具体的文本、布局和卡片由您决定！提示：您可以使用 *scale* 选项调整卡片的大小；您可以通过点击实验的顶层项目打开通用属性选项卡，从而更改背景颜色。

对我来说，结果看起来是这样的：

%--
图：
 id: FigStaticCards
 source: static-cards.png
 caption: |
  具有静态定义卡片的 SKETCHPAD。
--%


### 步骤5：使响应卡片可变

现在我们总是显示相同的响应卡片（上例中的蓝色三角形）。但是，我们当然希望在每个试验中显示不同的响应卡片。为此，我们首先需要定义决定我们将显示哪张响应卡片的变量。我们将在 *block_loop*中进行此操作。

打开 *block_loop*。LOOP表现在是空的。为了确定响应卡片的颜色、形状和数字，我们可以手动创建三列（ `response_color`,`response_shape` 和 `response_number`）以及64行，以涵盖所有颜色、形状和数字的组合。但这将是很多工作。相反，我们将使用全因素设计向导，您可以通过单击“全因素设计”按钮打开它。（全因素设计是一种所有可能的变量水平组合都会发生的设计。）在此向导中，为其中的三个变量创建一列，然后在下面的单元格中输入该变量的可能值（见%FigDesignWizard）。

%--
figure：
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  全因素设计向导可让您轻松生成与全因素设计相对应的大型LOOP表。
--%


接下来，点击确定按钮。 *block_loop* 现在包含颜色、数字和形状的所有64种组合（参见%FigLoopTable1）。

%--
图：
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  第5步结束时的 *block_loop*。
--%

现在回到 *card_display*。OpenSesame中的每个项目都是通过脚本定义的。这个脚本是由用户界面自动生成的。有时候直接编辑这个脚本是很方便的（甚至必要的），我们现在也需要这样做！

要查看脚本，请单击“查看”按钮，然后选择“查看脚本”。 （查看按钮位于项目控件右上角的中间按钮。）这将打开一个脚本编辑器。

*card_display* 的脚本主要由 `draw` 命令组成，这些命令定义了五张卡片以及各种文本元素。找到与响应卡对应的行。您可以通过查看 Y 坐标（应为正数，即显示器的下方）或查看图像文件的名称来找到它。

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

现在，在我的例子中，响应卡的图像文件总是`“1-blue-triangle.png”`。但当然我们并不总是想展示一个蓝色的三角形。相反，我们希望图像文件取决于我们在 *block_loop* 中定义的变量。为此，请用 `{response_number}` 替换数字，用 `{response_color}` 替换颜色，用 `{response_shape}` 替换形状：（方括号表示这些是变量名）

```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

单击应用以接受对脚本的更改。响应卡现在已被问号图标替代。这是因为OpenSesame不知道如何显示使用变量定义的图像的预览。但不用担心：当您运行实验时，图像将显示出来！

### 步骤6：使刺激卡片变量

刺激卡片应大致随机选择，但每个颜色、形状和数字只能出现一次；也就是说，永远不会出现两张红色卡片或两张带有三角形的卡片。（如果有，匹配过程会变得模棱两可。）为了实现这一点，我们可以使用*水平洗牌*，这是LOOP项目中一个功能强大但不寻常的特性。

- %link:loop%

首先，打开 *block_loop*，并创建12个（！）新列来定义刺激卡片：`color1`，用于第一张卡片的颜色，`color2`，`color3`，`color4`，以及`shape1` … `shape4`，和`number1` … `number4`。每个列在每一行上都有相同的值（参见 %FigLoopTable2）。

%--
figure：
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  步骤6中的 *block_loop* 。
--%

但我们还没有完成！现在，第一张刺激卡总在一个红色圆圈中，第二张为两个蓝色三角形，等等。要对此进行随机化，我们告诉OpenSesame随机交换四个颜色变量、四个形状变量和四个数字变量的值。为此，请打开 *block_loop* 的脚本。在倒数第二行（在 `run trial_sequence` 之前）添加以下命令：

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

单击应用以接受脚本。要查看是否有效果，单击预览按钮。这将显示在实验中如何随机化LOOP表格的预览。看起来不错吗？

现在回到 *card_display*，并让第一张刺激卡的图像根据变量`color1`、`shape1`和`number1`，其他刺激卡也类似。 （如果您不确定如何操作，请重新查看步骤5。）

### 步骤7：确定正确的响应（对于一个匹配规则）

暂时我们假定参与者始终按照形状进行匹配。（在Extra Assignments中要求对此进行改进。）

现在，*card_display* 的持续时间设为 “keypress”。这意味着 *card_display* 会一直显示，直到按下一个键，但它无法控制如何处理这个按键。因此，请将持续时间更改为0，并在 *card_display* 之后直接插入 KEYBOARD_RESPONSE。将 KEYBOARD_RESPONSE 重命名为 *press_a*，并指定正确响应为 'a' 以及允许的响应为 'a; b; c; d'。

%--
figure:
 id: FigPressA
 source: press-a.png
 caption: |
  在第7步中定义的一个 KEYBOARD_RESPONSE 项目。
--%

但这还不够！现在有一个单一的响应项目，它假定正确的响应始终为 'a'。我们尚未指定正确响应为 'a' 的条件，也没有考虑正确响应为 'b'，'c' 或 'd' 的试验。

为了实现这一点，首先创建三个更多的 KEYBOARD_RESPONSE 项目：*press_b*、*press_c* 和 *press_d*。除了为每个项目单独定义的正确响应之外，它们都是相同的，分别应为'b'，'c'和'd'。

最后，在 *trial_sequence* 中，使用 Run If 语句来决定在什么条件下应执行四个 KEYBOARD_RESPONSE 项目中的每一个（从而决定正确的响应是什么）。对于 *press_a*，条件是 `shape1` 应该等于 `response_shape`。为什么？那是因为这意味着第一个刺激卡片的形状等于响应卡片的形状，在这种情况下，正确的响应是 'a'。这个条件对应于以下的 run-if 语句：`shape1 = response_shape`。其他 KEYBOARD_RESPONSE 项目的 run-if 语句类似（见%FigTrialSequence1）。

%--
figure:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 caption: |
  第 7 步结束时的 *trial_sequence*。
--%

### 步骤8：给参与者提供反馈

只要已经指定了正确的响应（正如我们在第 7 步所做的那样），OpenSesame 会自动记录响应是正确还是错误，通过将变量 `correct` 分别设为 1 或 0。我们可以利用这个功能向参与者反馈他们是否做出了正确的答案。

为此，在 *trial_sequence* 中添加两个新的SKETCHPAD，并将它们命名为 *correct_feedback* 和 *incorrect_feedback*。然后，使用 run-if 语句确定应执行哪一个（见%FigTrialSequence2）。

%--
figure:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 caption: |
  第 8 步结束时的 *trial_sequence*。
--%

最后，在这两个SKETCHPAD中添加一些有用的内容。例如，对于 *correct_feedback*，您可以使用一个绿色的注视点，对于 *incorrect_feedback*，您可以使用一个红色的注视点，两者都显示 500 毫秒（将 SKETCHPAD 的持续时间设置为 500）。彩色圆点是提供反馈的一种不显眼的方式。

### 步骤9：测试实验

至此，您已经创建了一个基本（但不完整！）的威斯康星卡片分类测试实现（您将在下面的额外作业中完成实现）。

要测试实验，点击快速运行按钮（蓝色双箭头）或全屏运行按钮（绿色箭头）。

## Extra assignments

### 额外1（简单）：添加记录器

OpenSesame 不会自动记录数据，而是需要您在实验中显式添加 `logger` 项目。在基于试验的实验中，`logger` 通常是 *trial_sequence* 的最后一个项目，这样就可以记录试验过程中收集的所有数据。

现在，我们的 WCST 没有记录任何数据。是时候解决这个问题了！

### 额外2（简单）：查看数据文件

*完成额外1才能进行*。

给实验做一个简短的测试运行。现在在 Excel，LibreOffice Calc 或 JASP 这样的程序中查看日志文件。确定相关变量，并思考如何分析结果。

__提示：__ 将*block_loop*的重复值设置为0.1，以在测试期间减少试验次数。

### 额外任务 3（简单）：添加说明和再见屏幕

一个好的实验需要附带明确的说明。而一个有礼貌的实验在参与者完成时要向他们说再见。您可以使用SKETCHPAD来实现这一点。

### 额外任务 4（中等难度）：通过Python内联脚本设置正确的响应和匹配规则

要在OpenSesame中包含Python脚本，您可以使用INLINE_SCRIPT项目。

到目前为止，匹配规则始终是通过形状进行匹配。要更改此设置,在实验开始处添加一个INLINE_SCRIPT项目，并使用以下脚本（在*准备*阶段）随机设置变量`matching_rule`为'shape'、'number'或'color'。

```python
import random

matching_rule = random.choice(['shape', 'number', 'color'])
```

现在，在*trial_sequence*开始时添加另一个INLINE_SCRIPT项目。 在*准备*阶段，添加一个脚本将`correct_response`变量设置为'a'、'b'、'c'或'd'。 为此，您需要一系列`if`语句，它们首先查看匹配规则，然后查看哪个形状与响应形状相对应（对于形状匹配规则）或哪个颜色与响应颜色相对应（对于颜色匹配规则）等。

为了开始实现这一点，这里是部分解决方案（但需要完善！）:


```python
if matching_rule == 'shape':
    if shape1 == response_shape:
        correct_response = 'a'
    # 还没完成
# 还没完成

# 让我们将一些信息打印到调试窗口
print('matching_rule = {}'.format(matching_rule))
print('correct_response = {}'.format(correct_response))
```

### 额外任务 5（困难）：定期更改匹配规则

到目前为止，匹配规则在实验开始时随机确定，但在实验过程中保持不变。在真正的WCST中，匹配规则会定期更改，通常是在参与者做出固定次数的正确响应后更改。

要实现这一点，您需要另一个INLINE_SCRIPT。以下是一些入门要点：

- 使用一个计数器变量，在正确响应后递增1，在错误响应后重置为0。
- 在更改匹配规则时，请确保它不是（偶然）再次设置为相同的匹配规则。

### 额外任务 6（非常困难）：限制响应卡

目前，响应卡可以在多个维度上与刺激卡重叠。例如，如果其中一个刺激卡是一个蓝色圆圈，响应卡可能是两个蓝色圆圈，从而在颜色和形状上都重叠。在真正的WCST中，响应卡与每个刺激卡重叠的维度不得超过一个。

这一次就由你来完成，不再给出指示了!

## 解决方案

您可以从以下链接下载完整的实验，包括额外任务的解决方案:

- <https://osf.io/f5er2/>