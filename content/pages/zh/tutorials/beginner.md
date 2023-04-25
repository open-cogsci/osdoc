title: 初学者教程：注视线索
hash: 4b8cd383d0beb70ff7280b358bcb4c15a73635e4fb62d7260bc4b1e16d992e65
locale: zh
language: Chinese

[TOC]

## 关于 OpenSesame

OpenSesame是一个简化心理学、神经科学和实验经济学行为实验开发的程序。对于初学者，OpenSesame拥有全面的图形化、点击式界面。对于高级用户，OpenSesame 支持 Python 脚本编写(本教程不涉及这部分内容)。

OpenSesame 根据[通用公共许可证 v3][gpl]免费提供。

## 关于本教程

本教程通过OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012; Mathôt & March, 2022)][references] 展示如何创建一个简单而完整的心理学实验。您将主要使用 OpenSesame 的图形用户界面（即没有 Python 内联编码），尽管您将对 OpenSesame 脚本做些许修改。本教程大约需要一个小时。

## 资源

- __下载__--本教程假设您正在运行 OpenSesame 版本 4.0.0 或更高。要检查您正在运行的版本，请参阅"开始"选项卡的右下角（见 %FigGetStarted）。您可以从以下链接下载 OpenSesame 的最新版本：
	- %link:download%
- __文档__--专门的文档网站可以在以下链接找到：
	- <http://osdoc.cogsci.nl/>
- __论坛__--支持论坛地址为：
	- <http://forum.cogsci.nl/>

## 实验

在本教程中，您将创建一个[Friesen 和 Kingstone (1998)][references]介绍的注视线索实验。在这个实验中，一个面孔出现在屏幕中央（%FigGazeCuing）。这张脸朝向右或左。目标字母（“F”或“H”）出现在脸的左侧或右侧。干扰刺激（字母“X”）出现在脸的另一侧。任务是尽快指出目标字母是“F”还是“H”。在一致条件下，面孔望向目标。在不一致条件下，面孔望向干扰物。您可能已经猜到，典型的结果是，即使注视方向不能预测目标位置，参与者在一致条件下的反应速度也比不一致条件下快。这表明，我们的注意力会受到其他人注视的自动引导，即使在这种情况下没有任何目的。（甚至当面孔只是一个笑脸时！）

%--
图示：
 id: FigGazeCuing
 源: gaze-cuing.png
 标题： |
  您将在本教程中实现的注视线索范例[(Friesen and Kingstone, 1998)][references]。这个示例描述了一个不一致条件的试验，因为笑脸看着干扰物（“X”），而不是目标（“F”）。
--%

实验分为练习和实验阶段。视觉反馈将在每组试验后呈现。每次错误响应后将播放声音。

## 实验设计

此设计：

- 是*被试内*的，因为所有参与者都完成所有条件
- 是*完全交叉*（或全因子）的，因为所有条件组合均会出现
- 有三个因素（或因素）：
    - *注视方向*，两个水平（左，右）
    - *目标方向*，两个水平（左，右）
    - *目标字母*，两个水平（F，H）
- 有 N 名参与者

另请参见 %DesignScreencast，以获取实验逻辑和设计的解释：


%--
视频：
 来源: youtube
 id: DesignScreencast
 视频id: aWvibRH6D4E
 宽度: 640
 高度: 360
 标题：  |
  实验逻辑和设计的解释。
--%

## 步骤1：创建主序列

当您启动 OpenSesame 时，会看到“开始！”选项卡（%FigGetStarted）。在“开始新实验”下方显示了一系列模板。这些模板为新实验提供了便利的起点。在您首次保存实验后，最近打开的实验将显示在“继续进行最近的实验”下。页面底部有指向文档（包括本教程）、社区论坛和专业（付费）支持选项页面的链接。当然还有一个链接，您可以在那里给我们买咖啡，帮助我们在为您提供最佳免费软件时保持清醒！

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  OpenSesame启动时的“开始”对话框。
--%

点击“默认模板”以启动最小实验模板。

默认情况下有一个名为*实验*的主SEQUENCE。在概述区（默认位于左侧，请参阅％FigInterface）中点击*实验*以在选项卡区域中打开其控件。*实验* SEQUENCE 包含两个项目：名为*快速入门*的 `notepad` 和名为*欢迎*的 SKETCHPAD。

我们不需要这两个项目。在概述区域右键点击* getting_started *，然后选择“删除”（快捷键：“Del”）。以相同方式删除*欢迎*。*实验* SEQUENCE 现在为空。

%--
figure:
 id: FigInterface
 source: interface.png
 caption: "OpenSesame界面的默认布局。"
--%

<div class='info-box' markdown='1'>

__背景框__

__名称与类型__ -- OpenSesame 中的项目具有名称和类型。名称和类型可以相同，但通常不同。例如，一个 SKETCHPAD 项可以有名为 *my_target_sketchpad* 的名称。为了明确这个区别，我们将使用 `等宽` 表示项目类型，用*斜体*表示名称。

__提示__ --“扩展模板”是许多实验的良好起点。它已经包含了基于试验的实验的基本结构。

__提示__ --您可以点击项目选项卡右上角的帮助图标以获取上下文敏感的帮助。

__提示__ --经常保存（快捷键：“Ctrl+S”）您的实验！在发生数据丢失的不幸（和不太可能）事件中，您通常可以从每隔 10 分钟（默认值）自动创建的备份中恢复您的工作（菜单 → 工具 → 打开备份文件夹）。

__提示__ --除非您使用了“永久删除”（快捷键：“Shift+Del”），否则已删除的项目仍可在“未使用项目”垃圾桶中找到，直到您在“未使用项目”选项卡中选择“永久删除未使用项目”为止。您可以通过将它们从“未使用项目”垃圾桶拖到实验的某个地方，将删除的项目重新添加到 SEQUENCE 中。

__提示__ -- %FigExperimentStructure 以示意方式显示您将创建的实验的结构。在本教程中，如果您感到困惑，可以参考 %FigExperimentStructure 以了解您所处的位置。

%--
figure：
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  “凝视线索”实验结构的示意表示。项目类型用粗体表示，项目名称用普通字体表示。
--%

</div>

__添加 form_text_display 项目以显示指导__

顾名思义，`form_text_display` 是一个显示文本的表格。我们将使用 `form_text_display` 在实验开始时向参与者提供指导。

在概述区域中点击 *实验* 以在选项卡区域中打开其控件。您将看到一个空的 SEQUENCE。将 `form_text_display` 从项目工具栏（在“表格”下，请参阅 %FigInterface）拖到选项卡区域的 *实验* SEQUENCE 上。松开鼠标后，新的 `form_text_display` 项目将插入到 SEQUENCE 中。（我们将在第12步中回到这一点。）

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 您可以将项目拖到概述区域和SEQUENCE标签中。

__提示__ -- 如果放置操作不明确，一个弹出菜单会询问您想要执行哪个操作。

__提示__ -- `form_text_display` 仅显示文本。如果您需要图像等，可以使用 SKETCHPAD 项目。我们将在步骤5中了解到 SKETCHPAD。

</div>

__附加一个包含新序列项目的循环项目，用于练习阶段__

我们需要将一个 LOOP 项目附加到 *experiment* SEQUENCE。我们将为实验的练习阶段使用此 LOOP。单击 *experiment* SEQUENCE 以在选项卡区域中打开其控件。

将 LOOP 项目从项目工具栏拖入SEQUENCE，就像之前添加了 `form_text_display` 一样。新项目会在放置处项目的下方插入，因此如果将新的 LOOP 放置在先前创建的 `form_text_display` 上，则它会出现在您想要的位置：在 `form_text_display` 后面。 但如果将新项目放在错误的地方，请不要担心，因为您以后可以随时重新排序。

单独的 LOOP 并不会做任何事情。LOOP 总是需要另一个项目来运行。因此，您需要用另一个项目填充新的 LOOP 项目。（如果您查看循环项目，您还会看到一个警告：“未选择项目”。）将 SEQUENCE 项目从项目工具栏拖到 LOOP 项目上。 将出现一个弹出菜单，询问您是否要在 LOOP 项目之后或者放入 LOOP 项目。选择“插入到 new_loop”。（我们将在第二步中回顾这一点。）

<div class ='info-box' markdown='1'>

__背景框__

__LOOP 项目是什么？__ -- LOOP 是一种添加实验结构的项目。 它会重复执行另一个项目，通常是 SEQUENCE。 LOOP 也是您通常定义自变量的地方，即实验中您操作的变量。

__SEQUENCE 项目是什么？__ -- SEQUENCE 项目也为您的实验添加了结构。 如名称所示，SEQUENCE依次运行多个其他项目。

__LOOP-SEQUENCE 结构__ -- 您经常需要重复一系列事件。 为此，您需要一个包含有 SEQUENCE 项目的 LOOP 项目。 本身，SEQUENCE 不会重复。它只是从第一个项目开始，以最后一个项目结束。通过将 LOOP 项目“包裹”在 SEQUENCE 外部，您可以多次重复 SEQUENCE。 例如，单个测试通常对应于一个名为*trial_sequence*的单个 SEQUENCE。 环绕此 *trial_sequence* 的 LOOP（通常称为 *block_loop*） 则构成了一个实验块。 同样，但在实验的另一个层面上，SEQUENCE（通常称为 *block_sequence*）可能包含单个实验块，后跟 FEEDBACK 显示。绕着“块”SEQUENCE 的 *practice_phase* LOOP 将构成实验的练习阶段。 这可能看起来有些抽象，但随着教程的进行，您将熟悉 LOOP 和 SEQUENCE 的使用。

__提示__ -- 有关 SEQUENCE 和 LOOP 的更多信息，请参阅：

- %link:loop%
- %link:sequence%

</div>

__附加一个新的 form_text_display 项目，用于练习结束消息__

练习阶段结束后，我们希望告知参与者真正的实验将要开始。为此，我们需要另一个 `form_text_display`。回到 *experiment* SEQUENCE，将 `form_text_display` 从项目工具栏拖到 LOOP 项目上。和以前一样，将出现相同的弹出菜单。这次，请选择“在 new_loop 之后插入”。（我们将在第12步中回顾这一点。）

<div class ='info-box' markdown='1'>

__提示__ -- 如果您不小心更改了 LOOP 的项目以运行，请不要担心。您可以通过在工具栏中点击“撤消”按钮（`Ctrl+Shift+Z`）轻松撤消。

</div>

__为实验阶段附加一个新的循环项目，并包含先前创建的序列__

与练习阶段一样，我们需要一个 LOOP 项目进行实验阶段。因此，将 LOOP 从项目工具栏菜单拖到 *_form_text_display*。

新创建的 LOOP（名为 *new_loop_1*）为空，应填充一个 SEQUENCE，就像我们之前创建的 LOOP 一样。然而，由于实践阶段和实验阶段的试验是相同的，它们可以使用相同的 SEQUENCE。因此，与其从项目工具栏拖动一个新的 SEQUENCE，不如使用 *现有* 的一个（即创建一个链接副本）。

要做到这一点，请右键单击之前创建的 *new_sequence*，然后选择“复制（链接）”。现在，右键单击 *new_loop_1* 并选择“粘贴”。在出现的弹出菜单中，选择“插入到 new_loop 1”。

<div class='info-box' markdown='1'>

__背景框__

__提示__ —— *链接* 复制和 *非链接* 复制之间有一个重要的区别。如果您创建一个链接副本，您将创建同一项目的另一个副本。因此，如果修改原始项目，链接副本也会发生变化。相反，如果您创建了一个非链接副本，副本最初看起来是相同的（名称除外），但您可以编辑原始副本而不会影响非链接副本，反之亦然。

</div>

__添加一个新的 form_text_display 项目，用于告别信息__

当实验结束时，我们应该向参与者道别。为此，我们需要另一个`form_text_display`项目。回到 *experiment* SEQUENCE，从项目工具栏将 `form_text_display`拖到 *new_loop_1*。在出现的弹出菜单中，选择 "在 new_loop_1 之后插入"。（我们将在第12步回到这里。）

__给新项目起个合理的名字__

默认情况下，新项目的名称类似于 *new_sequence* 和 *new_form_text_display_2*。给项目起个合理的名字是一种好习惯。这将使得更容易理解实验的结构。如果愿意，还可以为每个项目添加描述。项目名称必须由字母数字字符和 / 或下划线组成。

- 在概述区选择 *new_form_text_display*，在选项卡区域顶部双击其标签，将项目重命名为 *instructions*。（概述区快捷方式：`F2`）
- 将 *new_loop* 重命名为 *practice_loop*。
- 将 *new_sequence* 重命名为 *block_sequence*。因为你在 *new_loop_1* 中重用了这个项目，所以这个名字也会自动更改。（这说明在有可能的情况下创建链接副本是有效的。）
- 将 *new_form_text_display_1* 重命名为 *end_of_practice*。
- 将 *new_loop_1* 重命名为 *experimental_loop*。
- 将 *new_form_text_display_2* 重命名为 *end_of_experiment*。

__给整个实验起个合理的名字__

实验本身也有一个标题和描述。在概述区单击“新实验”。可以像重命名项目一样重命名实验。当前的标题是“新实验”。将实验重命名为“教程：注视提示”。与项目名称不同，实验标题可以包含空格等。

你的实验概述区现在看起来像这样 %FigStep1。现在是保存实验的好时机（快捷键：'Ctrl+S'）。

%--
figure：
 id：FigStep1
 source：step1.png
 caption:|
  步骤1结束时的概述区。
--%

## 第2步：创建块序列

在概述中点击 *block_sequence*。此刻这个 SEQUENCE 是空的。我们希望 *block sequence* 包含一个试验块，然后是一个 FEEDBACK 显示。为此我们需要执行以下操作：

__追加一个 reset_feedback 项目以重置反馈变量__

我们不希望我们的反馈受到参与者在指导阶段或者之前试验块中所做的按键的影响。因此，我们通过重置反馈变量开始每个试验块。为此我们需要一个 `reset_feedback` 项目。从项目工具栏（在“响应收集”下）抓取 `reset_feedback` 并将其拖到 *block_sequence* 上。

__追加一个新循环，包含一个新序列，用于试验块__

对于单个试验，我们需要一个SEQUENCE。对于一个试验块，我们需要多次重复这个SEQUENCE。因此，对于一个试验块，我们需要在SEQUENCE周围包裹一个LOOP。从项目工具栏拖动一个LOOP到*new_reset_feedback*。接下来，从项目工具栏拖动一个SEQUENCE到新创建的LOOP上，并在弹出的菜单中选择“插入到new_loop”。（我们将在步骤3中回到这一点。）

__添加一个反馈项目__

在每个试验块之后，我们希望向参与者提供反馈，以便参与者了解他/她的表现。为此我们需要一个FEEDBACK项目。从项目工具栏中拖动一个FEEDBACK到*new_loop*上，并在弹出的菜单中选择“在循环后插入”。（我们将在步骤10中回到这一点。）

__为新项目取一个有意义的名字__

重命名：（如果您不记得如何操作，请参看步骤1。）

- *new_loop* 改为 *block_loop*
- *new_sequence* 改为 *trial_sequence*
- *new_reset_feedback* 改为 *reset_feedback*
- *new_feedback* 改为 *feedback*

您现在的实验概述看起来像 %FigStep2。请记住定期保存您的实验。

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## 步骤3：用独立变量填充试验块循环

如名称所示，*block_loop* 对应一个试验块。在上一步中，我们创建了*block_loop*，但我们仍需要定义在试验块内会发生变化的独立变量。我们的实验有三个独立变量：

- __gaze_cue__ 可以是“左”或“右”。
- __target_pos__（目标位置）可以是“-300”或“300”。这些值反映目标的X坐标（0=中心）用像素表示。在创建目标显示时（参见步骤5），直接使用坐标而不是“左”和“右”会比较方便。
- __target_letter__（目标字母）可以是“F”或“H”。

因此，我们的实验有2 x 2 x 2 = 8个水平。虽然8个水平并不算多（大多数实验都会有更多），但我们不需要手动输入所有可能的组合。在概览中点击*block_loop*以打开它的标签。现在点击“全因子设计”按钮。在变量向导中，您只需将所有变量的名称输入在第一行，然后将级别输入在名称下方的行（见%FigVariableWizard）。如果您选择“确定”，您会看到*block_loop*已填充了所有8种可能的组合。

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  The loop variable wizard in Step 3.
--%

在生成的循环表中，每行对应一个*trial_sequence*的运行。因为，在我们的例子中，一个*trial_sequence*的运行对应一个试验，所以我们循环表中的每一行对应一个试验。每列对应一个变量，每个试验的值可以不同。

但是我们还没有完成。我们还需要添加三个变量：干扰物的位置、正确反应和一致性。

- __dist_pos__ -- 在第一行的第一个空列中输入'dist_pos'。这会自动添加一个名为'dist_pos'的新实验变量。在下面的行中，将'target_pos'为-300的地方输入'300'，将'target_pos'为300的地方输入'-300'。换句话说，目标和干扰物应该相互对立。
- __correct_response__ -- 在另一个空列中创建一个名为'correct_response'的变量。将'target_letter'为'F'的'correct_response'设为'z'，将'target_letter'为'H'的'correct_response'设为'm'。这意味着，如果参与者看到"F"，她应按"z"键；如果看到"H"，她应按"m"键。（如果'z'和'm'键在你的键盘布局上不方便，可以选择其他键；例如，AZERTY键盘上'w'和'n'键更合适。）
- __congruency__ -- 创建一个名为'congruency'的变量。将'target_pos'为'-300'且'gaze_cue'为'left'的'congruency'设为'congruent'，将'target_pos'为'300'且'gaze_cue'为'right'的'congruency'设为'congruent'。换句话说，如果脸看着目标，试验就是一致的。将'congruency'设为'incronguent'，以便脸看着干扰物的试验。'congruency'变量在运行实验时并不是必需的；但是，它在以后分析数据时非常有用。

我们还需要做最后一件事。'Repeat'目前设置为'1.00'。这意味着每个周期将执行一次。这样，现在的实验块包括了8个试验，有点短。一个合理的实验块长度是24，所以将'Repeat'设置为3.00（3次重复x8个周期=24次试验）。你不需要更改'Order'，因为'random'正是我们想要的。

现在*block_loop*看起来像%FigStep3。请记得定期保存您的实验。

%--
图：
 id: FigStep3
 source: step3.png
 caption: "完成步骤3后的*block_loop*。"
--%

<div class ='info-box' markdown='1'>

__背景框__

__提示__ -- 你可以在你喜欢的电子表格程序中准备循环表，然后将其复制粘贴到LOOP变量表中。

__提示__ -- 你可以在单独的文件中指定循环表（以`.xlsx`或`.csv`格式），并直接使用此文件。为此，请在“Source”下选择“file”。

__提示__ -- 你可以为“Repeat”设置一个非整数值。例如，通过将“Repeat”设置为“0.5”，只会执行一半的试验（随机选择）。

</div>

## 步骤4：将图像和声音文件添加到文件池

对于我们的刺激，我们将使用文件中的图像。此外，如果参与者出错，我们将播放声音。为此我们需要一个声音文件。

你可以在此处下载所需的文件（在大多数网络浏览器中，你可以右键单击链接并选择“另存为”或类似选项）：

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

下载这些文件（例如，到桌面）后，你可以将它们添加到文件池。如果文件池当前不可见（默认在窗口右侧），请单击主工具栏上的“显示文件池”按钮（快捷方式：`Ctrl+P`）。将四个文件添加到文件池的最简单方法是将它们从桌面（或你下载文件的任何地方）拖放到文件池中。或者，你也可以单击文件池中的“+”按钮，并使用出现的文件选择对话框添加文件。文件池将自动保存在您的实验中。

你的文件池现在看起来像%FigStep4。请记得定期保存您的实验。

%--
图：
 id: FigStep4
 source: step4.png
 caption: "完成步骤4后的文件池。"
--%

## 步骤5：用项目填充试验序列

我们实验中的一个试验如下：

1. __固定点__ -- 750毫秒，SKETCHPAD项目
2. __中性注视__ -- 750毫秒，SKETCHPAD项目
3. __注视线索__ -- 500毫秒，SKETCHPAD项目
4. __目标__  -- 0毫秒，SKETCHPAD项目
5. __响应收集__ 	-- KEYBOARD_RESPONSE项目
6. __如果响应错误播放声音__ --  SAMPLER项目
7. __将响应记录到文件__ -- LOGGER项目

点击概述中的 *trial_sequence* 以打开 *trial_sequence* 标签页。从项目工具栏中选取一个 SKETCHPAD 并将其拖进 *trial_sequence*。再重复三次，使 *trial_sequence* 包含四个SKETCHPAD。接下来，选择并追加一个 KEYBOARD_RESPONSE 项目，一个 SAMPLER 项目，和一个 LOGGER 项目。

同样，我们将重命名新项目，以确保 *trial_sequence* 易于理解。重命名：

- *new_sketchpad* 为 *fixation_dot*
- *new_sketchpad_1* 为 *neutral_gaze*
- *new_sketchpad_2* 为 *gaze_cue*
- *new_sketchpad_3* 为 *target*
- *new_keyboard_response* 为 *keyboard_response*
- *new_sampler* 为 *incorrect_sound*
- *new_logger* 为 *logger*

缺省情况下，项目总是会被执行，这由 run-if 表达式 `True` 表示。然而，我们想为 *incorrect_sound* 项目更改这一点，该项目仅在出现错误时才执行。为此，我们需要在 *trial_sequence* 标签页中将 "Run if" 表达式更改为 `correct == 0`。这样做是有效的，因为 *keyboard_response* 项目会自动创建一个 `correct` 变量，它设置为 `1`（正确），`0`（错误）或 `undefined`（这取决于第3步中定义的 `correct_response` 变量）。双等号符号是 Python 语法，表示您要比较两者之间是否相等，这种情况下是变量 `correct` 是否等于0。要更改 run-if 表达式，请双击它（快捷键：`F3`）。

*trial_sequence* 现在看起来像 %FigStep5。

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "第五步结束后的 *trial_sequence*。"
--%

<div class='info-box' markdown='1'>

__背景框__

__什么是 SKETCHPAD 项目？__ -- SKETCHPAD 用于呈现视觉刺激：文本，几何形状，固定点，Gabor 图案等。您可以使用内置的绘图工具在 SKETCHPAD 上绘制。

__什么是 KEYBOARD_RESPONSE 项目？__ -- KEYBOARD_RESPONSE 项目从键盘收集参与者的单个响应。

__什么是 SAMPLER 项目？__ -- SAMPLER 项目从声音文件播放声音。

__什么是 LOGGER 项目？__ -- LOGGER 项目将数据写入日志文件。这非常重要：如果您忘记包含 LOGGER 项目，实验期间将不会记录任何数据！

__提示__ -- 变量和条件 "if" 表达式非常强大！要了解更多信息，请参阅：

- %link:manual/variables%

</div>

## 步骤6：绘制 sketchpad 项目

我们在步骤5中创建的 SKETCHPAD 项目仍然是空白的。现在是绘图的时候了！

__将背景颜色设置为白色__

点击概述区域中的 *fixation_dot* 以打开其标签页。SKETCHPAD 仍然是深灰色的，而我们下载的图像有白色背景。糟糕，我们忘记将实验的背景颜色设置为白色（默认为深灰色）！点击概述区域中的“注视引导教程”，打开“常规属性”标签页，将“前景”更改为“黑色”，将“背景”更改为“白色”。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 对于颜色的更精细控制，您还可以使用十六进制RGB表示法（例如，`#FF0000`代表红色），使用各种色彩空间，或使用颜色选择器工具。另请参阅：

- %link:manual/python/canvas%

</div>

__绘制固定点__

回到 *fixation_dot*，点击概述中的 *fixation_dot*。现在通过点击带十字线的按钮来选择 fixation-dot 元素。当您将光标移动到画板上时，可以在右上角看到屏幕坐标。将（前景）颜色设置为“黑色”。点击屏幕的中心（0，0）来画一个中央注视点。

最后，将“Duration”字段从“keypress”更改为“745”，因为我们希望呈现时间为750毫秒。等待……* 为什么我们不直接指定一个持续时间为750毫秒？* 原因是实际的显示呈现持续时间总是舍入为与您的显示器刷新率兼容的值。这可能听起来很复杂，但是对于大多数目的而言，以下经验法则就足够了：

1. 选择一种持续时间，根据您的显示器的刷新率来选择。例如，如果您的显示器的刷新率为60 Hz，则意味着每个帧持续16.7毫秒（= 1000毫秒/60 Hz）。因此，在60 Hz的显示器上，您应始终选择持续时间是16.7毫秒的倍数，例如16.7、33.3、50、100等。
2. 在SKETCHPAD的持续时间字段中，为您想要显示的持续时间选择比目标略低的数值。所以，如果您要显示一个SKETCHPAD50毫秒，选择持续时间为45；如果您要显示一个SKETCHPAD1000毫秒，则选择持续时间为995。等等。

<div class='info-box' markdown='1'>

__背景框__

__提示__ - 关于实验时间的详细讨论，请参阅：

- %link:timing%

__提示__ - SKETCHPAD的持续时间可以是毫秒值，也可以输入“keypress”或“mouseclick”来收集按键或鼠标点击。在这种情况下，SKETCHPAD的工作方式与KEYBOARD_RESPONSE选项相似（但选项较少）。

__提示__ - 确保（前景）颜色设置为黑色。否则，您会在白色上画白色，什么也看不到！

</div>

__绘制中性凝视__

打开 *neutral_gaze* SKETCHPAD。现在通过点击带有山景图标的按钮来选择图像工具。点击屏幕中心（0，0）。将出现“从资源池选择文件”对话框。选择文件`gaze_neutral.png`，然后点击“选择”按钮。中性凝视图像现在会从屏幕中央凝视着您！最后，像以前一样，将“Duration”字段从“keypress”更改为“745”。（再次注意，在大多数显示器上，这意味着持续时间为750毫秒！）

<div class='info-box' markdown='1'>

__背景框__

__提示__ - OpenSesame可以处理各种图像格式。但是，某些（非标准）`.bmp`格式已知会引起问题。如果您发现`.bmp`图像未显示，您可以将其转换为其他格式，例如`.png`。您可以使用免费工具，如 [GIMP] 轻松转换图像。
</div>

__绘制凝视线索__

打开 *gaze_cue* SKETCHPAD，并再次选择图像工具。点击屏幕中心（0，0），并选择`gaze_left.png`文件。

但我们还没有完成！因为凝视线索不应总是“向左”，而应该取决于变量`gaze_cue`，我们在第3步中定义了这个变量。但是，通过将`gaze_left.png`图像绘制到SKETCHPAD，我们生成了一个脚本，只需稍作修改就能确保显示正确的图像。在*gaze_cue*选项卡的右上角点击“选择视图”按钮，然后选择“查看脚本”。您现在将看到与我们刚刚创建的草图板相对应的脚本：

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

我们需要做的唯一事情就是将`gaze_left.png`替换为`gaze_{gaze_cue}.png`。这意味着OpenSesame使用变量“gaze_cue”（其值为“左”和“右”）来确定应该显示哪个图像。

既然我们讨论到这里，我们还可以将持续时间更改为'495'（四舍五入为500！）。现在脚本看起来像这样：

~~~ .python
set duration 495
set description "显示刺激"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

点击右上角的“应用”按钮，将更改应用于脚本并返回到常规项目控件。OpenSesame将警告你无法显示图像，因为它是用变量定义的，并且将显示占位符图像代替。别担心，在实验过程中将显示正确的图像！

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 变量检查器（快捷键：`Ctrl+I`）是查找在你的实验中已经定义的哪些变量以及它们的值的强大方法（请参见%FigVariableInspector）。当你的实验没有运行时，大多数变量尚未设置值。但是当你在窗口中运行实验并同时查看变量检查器时，你可以实时看到变量的变化。这对于调试实验非常有用。

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "变量检查器是获取实验中存在的变量概述的便捷方式。"
--%

</div>

__绘制目标__

我们希望目标显示包括三个对象：目标字母、干扰字母和注视线索（请参见%FigGazeCuing）。与以前一样，我们首先使用SKETCHPAD编辑器创建一个静态显示。在此之后，我们只需要对脚本进行细微更改，以便确切的显示取决于变量。

在概述中点击* target *打开目标选项卡，然后像以前一样在屏幕的中心绘制`gaze_left.png`图片。现在点击带有'A'图标的按钮以选择绘制文字工具。将前景色更改为“黑色”（如果尚未更改）。默认字体大小为18 px，对于我们的目的来说有点小，因此将字体大小更改为32 px。现在单击SKETCHPAD上的（-320，0）（X坐标不需要完全为320，因为我们将此值更改为变量）。在出现的对话框中输入“{target_letter}”，绘制目标字母（在绘制文本时，您可以直接使用变量）。类似地，点击（320，0）并绘制“X”（干扰物始终为“X”）。

现在通过单击选项卡右上角的“选择视图”按钮并选择“查看脚本”来打开脚本编辑器。脚本如下所示：

~~~ .python
set duration keypress
set duration keypress
set description "显示刺激"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

像之前一样，将`gaze_left.png`更改为`gaze_{gaze_cue}.png`。我们还需要使目标和干扰物的位置分别取决于变量`target_pos`和`dist_pos`。为此，只需将`-320`更改为`{target_pos}`，将`320`更改为`{dist_pos}`。确保保留`0`，这是Y坐标。现在脚本看起来像这样：

~~~ .python
set duration keypress
set description "显示刺激"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

点击“应用”按钮以应用脚本并返回常规项目控件。

最后，将“Duration”字段设置为“0”。这并不意味着目标仅呈现 0 毫秒，而是实验将立即前进到下一个项目（*keyboard_response*）。因为 *keyboard_response* 等待响应，但不会改变屏幕上的内容，目标将一直可见，直到给出答案。

请记住定期保存您的实验。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 每个 SKETCHPAD 的元素都有一个 “Show if” 选项，指定应该何时显示元素。您可以使用此选项根据某些变量隐藏/显示来源于 SKETCHPAD 的元素，类似于 SEQUENCE 中的 run-if 语句。

__提示__ -- 确保（前景）颜色设置为黑色。否则，您将在白色上绘制白色，看不到任何东西！

</div>

## 步骤 7：配置键盘响应项目

点击概述中的 *keyboard_response* 以打开其选项卡。你会看到三个选项：正确响应、允许响应、超时和事件类型。

我们已在步骤 3 中设置了 `correct_response` 变量。除非我们明确指定正确的响应，否则 OpenSesame 会自动使用可用的 `correct_response` 变量。因此，我们不需要在此处更改 “Correct response” 字段。

我们确实需要设置允许的响应。在允许响应字段中输入 'z;m'（或者如果您选择了其他响应键，则输入其他键）。分号用于分隔响应。KEYBOARD_RESPONSE 现在仅接受 'z' 和 'm' 键。所有其他按键都被忽略，但 'escape' 除外，它会暂停实验。

我们还想设置一个超时，这是 KEYBOARD_RESPONSE 在决定响应错误并将 'response' 变量设置为 'None' 之前的最大间隔。'2000'（毫秒）是一个好值。

我们不需要更改事件类型，因为我们希望参与者通过按键（按键，默认）而不是释放键（键释放）来作出反应。

现在 KEYBOARD_RESPONSE 如 %FigStep7 所示。

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "步骤 7 结束时的 KEYBOARD_RESPONSE。"
--%

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 默认情况下，KEYBOARD_RESPONSE 将使用 `correct_response` 变量来确定响应是否正确。但是您也可以使用其他变量。要做到这一点，在正确响应字段中输入带有大括号的变量名（`{my_variable}`）。

__提示__ -- 如果启用了 “刷新待处理按键”（默认情况下是启用的），则在调用 KEYBOARD_RESPONSE 项目时会丢弃所有待处理的按键。这可以防止实验参与者在试验的非响应部分意外按下键时出现的过度影响。

__提示__ -- 要使用特殊键，如 '/' 或向上箭头键，你可以使用键名称（例如 'up' 和 'space'）或关联的字符（例如 '/' 和 ']'）。 “列出可用键” 按钮提供了所有有效键名的概述。

</div>

## 步骤 8：配置错误（采样器）项目

*incorrect_sound* 项目不需要太多工作：我们只需要选择要播放的声音。点击概述中的 *incorrect_sound* 以打开其选项卡。单击 “浏览” 按钮并从文件池中选择 `incorrect.ogg`。

现在采样器看起来像 %FigStep8。

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "步骤 8 结束时的 *incorrect_sound* 项目。"
--%

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 您可以使用变量来指定要播放的声音，方法是将变量名称作为（部分）文件名，变量名之间用大括号表示。例如：`{a_word}.ogg`

__提示__ -- 采样器支持 `.ogg`，`.mp3` 和 `.wav` 格式的文件。如果您拥有不同格式的音频文件，[Audacity] 是一个很棒的免费工具，可以用来转换音频文件（以及更多功能）。

</div>

## 步骤9：配置变量记录器

实际上，我们不需要配置变量LOGGER，但让我们还是看一下。点击概览中的 *logger* 以打开它的选项卡。您会看到“自动记录所有变量”的选项被选中。这意味着 OpenSesame 记录所有内容，这是可以的。

<div class='info-box' markdown='1'>

__背景说明__

__提示__——如果您喜欢干净的日志文件，可以禁用“自动记录所有变量”的选项，并手动选择变量，要么手动输入变量名称（“添加自定义变量”），要么将变量从变量检查器拖动到记录器表中。您还可以保持“自动记录所有变量”的选项，并排除您不感兴趣的变量。

__一条制胜的提示__——始终仔细检查实验中是否记录了所有必要的变量！检查这一点的最佳方法是运行实验并查看生成的日志文件。

</div>

## 步骤10：绘制反馈项目

在每组试验结束后，我们希望向参与者提供反馈，让他/她了解自己的表现。因此，在第2步中，我们将一个名为 *feedback* 的反馈项目添加到 *block_sequence* 的末尾。

点击概览中的 *feedback* 以打开它的选项卡，选择绘制文本工具，将前景色更改为“黑色”（如果尚未更改），然后点击（0, 0）。现在输入以下文本：

```text
End of block

Your average response time was {avg_rt} ms
Your accuracy was {acc} %

Press any key to continue
```

由于我们希望反馈项目保持可见，只要参与者愿意（即，直到他/她按下某个键），我们将“持续时间”字段保持为“按键”。

反馈项目现在看起来像 %FigStep_10。

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "第10步结束时的反馈项目。"
--%

<div class='info-box' markdown='1'>

__背景说明__

__什么是反馈项目？__—— 反馈项目与 SKETCHPAD 项目几乎相同。唯一的区别在于反馈项目不是预先准备好的。这意味着您可以使用它来提供关于参与者反应的即时信息。您不应使用反馈项目来展示时间关键性的显示，因为事实上，它不是预先准备好的，这意味着它的时间属性不如 SKETCHPAD 项目。另请参见：

- %link:visual %

__反馈与变量__——响应项目自动跟踪参与者的准确性和平均响应时间，在变量`acc`（同义词：`accuracy`）和`avg_rt`（同义词：`average_response_time`）中记录。另请参见：

- %link: manual/variables %

__提示__——确保（前景）颜色设置为黑色。否则，您将在白色上绘制白色，看不到任何东西！

</div>

## 步骤11：设置实践阶段和实验阶段的长度

我们之前已创建 *practice_loop* 和 *experiment_loop* 项目，它们都调用 *block_sequence*（即一组试验）。然而，现在它们只调用一次 *block_sequence*，这意味着实践和实验阶段都只有一个试验块。

点击 *practice_loop* 以打开其选项卡，将“重复”设置为“2.00”。这意味着实践阶段包括两个实验块。

点击 *experimental_loop* 以打开其选项卡，将“重复”设置为“8.00”。这意味着实验阶段包括八个实验块。

<div class='info-box' markdown='1'>

__背景说明__

__提示__——您可以在 *practice_loop* 和 *experimental_loop* 中创建一个变量 `practice`，分别将其设置为“yes”和“no”。这是跟踪哪些试验属于练习阶段的简便方法。

</div>

## 步骤12： 编写 instruction、end_of_practice 和 end_of_experiment 表单

我想你可以独自完成这个步骤！只需打开相应的项目并添加一些文本来显示说明、练习结束时的消息和实验结束时的消息。

<div class='info-box' markdown='1'>

__背景框__

__提示__--你可以使用一部分HTML标签来格式化你的文本。例如，*&lt;b&gt;这将是粗体&lt;b&gt;* 和 *&lt;span color='red'&gt;这将是红色&lt;span&gt;*。有关更多信息，请参阅：

- %link:text%

</div>

## 步骤13：运行实验！

你已经完成了！点击工具栏中的“在窗口中运行”（快捷键：“Ctrl+W”）或“全屏运行”（快捷键：“Ctrl+R”）按钮运行你的实验。

<div class='info-box' markdown='1'>

__背景框__

__提示__--通过点击橙色的“在窗口中运行”按钮（快捷键：“Ctrl+Shift+W”），测试运行会执行得更快，它不会询问你如何保存日志文件（因此只应用于测试目的）。

</div>


## 理解错误

在使用OpenSeame时，理解错误消息是一项至关重要的技巧。毕竟，新建的实验很少能立即运行且无任何错误！

假设我们在上面的步骤中犯了一个错误。当尝试运行实验时，我们收到以下错误消息（%FigErrorMessage）：

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "在OpenSesame中的错误消息。"
--%

错误消息以一个名称开始，这种情况下为“FStringError”，这表明错误的一般类型。接着是一段简短的解释性文字，例如：“在以下文本中无法评估f-string表达式：gaze_{gaze_ceu}.png“。即使没有理解什么是f字符串（它是包含大括号中的Python代码的字符串），也很明显“{gaze_ceu}.png”的文本有问题。

错误消息还表示错误来自*gaze_cue*项目的准备阶段。

最后，错误消息表明在评估“gaze_{gaze_ceu}.png”时发生了什么问题：名称'gaze_ceu'没有定义。

仔细阅读错误消息时，原因和解决方案可能已经浮现在你的脑海中：我们在*gaze_cue*项目中犯了一个简单的拼写错误，写成了'{gaze_ceu}'而不是'{gaze_cue}'！结果出现错误，因为没有变量名为`gaze_ceu`。通过打开*gaze_cue*项目的脚本并修复拼写错误可以轻松解决这个问题。

## 最后：关于时间和后端选择的一些一般性考虑

在实验的“一般属性”选项卡中(通过点击实验名称打开的选项卡)，你可以选择一个后端。后端是控制显示器、输入设备、声音等的软件层。虽然大多数实验都适用于所有后端，但是有些原因会让你更倾向于选择一个后端而不是另一个后端，主要与时间有关。目前有四个后端（取决于你的系统，可能不是所有的三个都可用）：

- __psycho__--基于PsychoPy[(Peirce, 2007)][references]的硬件加速后端。这是默认值。
- __xpyriment__--基于Expyriment[(Krause & Lindeman, 2013)][references]的硬件加速后端。
- __legacy__--基于PyGame的“安全”后端。在大多数平台上提供可靠性能，但由于缺乏硬件加速，其时间属性不如其他后端。
- __osweb__--在浏览器中运行实验[(Mathôt & March, 2022)][references]。

另请参阅：

- %link:backends%
- %link:timing%


## 参考文献

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Time resolution of clocks: Effects on reaction time measurement—Good news for bad clocks. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[参考文献]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about
