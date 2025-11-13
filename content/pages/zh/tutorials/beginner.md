title: 初学者教程：注视线索
hash: 8b68f010d5f28f2e59818b6c6aac4308f317f2ced632ba0c36993b1e159c8432
locale: zh
language: Chinese

## 关于 OpenSesame

OpenSesame 是一个免费的行为实验开发程序，适用于心理学、神经科学和实验经济学。对于初学者来说，OpenSesame 提供了一个全面的图形化、点选式界面。对于高级用户，OpenSesame 支持 Python 脚本编写（本教程未涵盖此部分）。

## 关于本教程

本教程展示了如何使用 OpenSesame 创建一个简单但完整的心理学实验 [(Mathôt, Schreij, & Theeuwes, 2012; Mathôt & March, 2022)][references]。你将主要使用 OpenSesame 的图形用户界面（即无需 Python 内嵌代码），但你将对 OpenSesame 脚本做出一些小的修改。本教程大约需要一小时完成。

本教程假定你正在运行已应用所有最新更新的 OpenSesame 4.1。如果你看到提示“部分软件包可更新 (…)”，点击“安装更新 …”按钮以打开更新面板，然后点击“运行更新脚本”以执行实际更新。更新完成后请重启 OpenSesame。

## 实验介绍

在本教程中，你将创建一个凝视-线索实验，最初由 [Friesen 和 Kingstone（1998）][references] 提出。在该实验中，屏幕中央会呈现一张面孔（%FigGazeCuing）。这张面孔会看向左侧或右侧。一个目标字母（‘F’或‘H’）会出现在面孔的左侧或右侧。一个干扰刺激（字母‘X’）会出现在面孔的另外一侧。被试需尽快判断目标字母是‘F’还是‘H’。在一致条件下，面孔看向目标。在不一致条件下，面孔看向干扰物。你可能已经猜到，典型发现是，被试在一致条件下反应更快，即使注视方向并不能预测目标的位置。这表明我们的注意力会自动受他人凝视引导，即使在这种引导并无用处或仅仅是一张笑脸的情况下。

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  本教程中你将实现的凝视-线索实验范式 [(Friesen 和 Kingstone, 1998)][references]。该示例展示了非一致条件下的一个试次，因为笑脸看向了干扰物（‘X’）而非目标（‘F’）。
--%

实验包括练习阶段和正式实验阶段。每个试块结束后都会出现视觉反馈，每次错误反应后会播放一个声音。

实验设计：

- 为 *被试内* 设计，因为所有参与者都做所有条件
- 为 *完全交叉*（或全因子），因为所有条件组合都会出现
- 有三个因素（或因子）：
    - *凝视方向*，两个水平（左、右）
    - *目标位置*，两个水平（左、右）
    - *目标字母*，两个水平（F、H）

参见 %DesignScreencast 获得对实验逻辑和设计的详细解释：

%--
video:
 source: youtube
 id: DesignScreencast
 videoid: aWvibRH6D4E
 width: 640
 height: 360
 caption: |
  实验逻辑与设计的讲解。
--%

## 步骤 1：创建主流程

启动 OpenSesame 时，你会看到“入门！”选项卡（%FigGetStarted）。在“开始新实验”下方会显示模板列表，这些模板为新实验提供了便捷的起点。首次保存实验后，最近打开的实验会显示在“继续最近的实验”下面。

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  OpenSesame 启动时的“入门”面板。
--%

点击“Default template”以从最小实验模板开始。

默认情况下有一个主 SEQUENCE，称为 *experiment*。点击概览区域中的 *experiment*（默认位于左侧，见 %FigInterface），在标签区域打开其控制界面。*experiment* SEQUENCE 由两个项目组成：一个名为 *getting started* 的 `notepad`，和一个名为 *welcome* 的 SKETCHPAD。

<div class='info-box' markdown='1'>

__背景框__

__名称 vs 类型__ —— OpenSesame 中的项目具有名称和类型。名称和类型可以相同，但通常不同。例如，一个 SKETCHPAD 项目可以命名为 *my_target_sketchpad*。为了明确区分，我们将使用 `等宽字体` 表示项目类型，使用 *斜体* 表示名称。

__提示__ —— “扩展模板”是许多实验的良好起点，它已经包含了以试次为基础的实验的基本结构。

__提示__ —— 你可以点击项目标签右上角的帮助图标获取上下文相关的帮助。

__提示__ —— 经常保存（快捷键：`Ctrl+S`）你的实验！如果不幸（且很少见）发生数据丢失，通常可以从默认每 10 分钟自动创建的备份文件中恢复你的工作（菜单 → 工具 → 打开备份文件夹）。

__提示__ —— 除非你使用了“永久删除”（快捷键：`Shift+Del`），否则被删除的项目依然可以在“未使用项目”收纳箱中找到，直到你在“未使用项目”标签中选择“永久删除未使用项目”。你可以通过将已删除项目从“未使用项目”收纳箱拖拽回实验结构，把它们重新添加到 SEQUENCE 中。

__提示__ —— %FigExperimentStructure 示意图展示了你将要创建的实验结构示意图。如果在教程过程中感到困惑，可以参考 %FigExperimentStructure 了解你所在的位置。

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  A schematic representation of the structure of the 'Gaze cuing' experiment. The item types are in bold face, item names in regular face.
--%

</div>


__移除不必要的项目__

我们不需要默认模板中的两个项目。右击概览区域中的 *getting_started*，选择“删除”（快捷键：`Del`）以移除。用同样的方法移除 *welcome*。此时 *experiment* SEQUENCE 为空。

__添加 form_text_display 项目显示说明信息__

顾名思义，`form_text_display` 负责显示文本。我们将用一个 `form_text_display` 在实验开始时向参与者展示说明。

点击概览区域中的 *experiment*，在标签区域打开其控制界面。你将看到一个空 SEQUENCE。从项目工具栏（“Form”分类下，见 %FigInterface）拖拽一个 `form_text_display` 到标签区域的 *experiment* SEQUENCE。当你松开鼠标时，一个新的 `form_text_display` 项目将被插入到 SEQUENCE 中。（我们将在第 12 步详细介绍。）

<div class='info-box' markdown='1'>

__背景框__

__提示__ —— 你可以把项目拖入概览区域和 SEQUENCE 标签界面中。

__提示__ —— 如果拖放操作存在歧义，将弹出菜单让你选择要进行的操作。

__提示__ —— `form_text_display` 只能显示文本。如果你需要展示图片等内容，可以使用 SKETCHPAD。我们将在第 5 步介绍 SKETCHPAD。

</div>

__为练习阶段添加 loop 项目，并内含新 sequence 项目__

我们需要在 *experiment* SEQUENCE 中添加一个 LOOP 项目。此 LOOP 将用于实验的练习阶段。点击 *experiment* SEQUENCE，在标签区域打开其控制界面。

将 LOOP 项从项目工具栏拖到 SEQUENCE 中，方式与添加 `form_text_display` 时相同。新项目会被插入到被拖放的项目下方，因此如果你将新的 LOOP 拖到之前创建的 `form_text_display` 上，它就会出现在你需要的位置：也就是在 `form_text_display` 后面。但如果你把新项目放错了地方也不用担心，因为你随时可以重新排序。

LOOP 本身不会执行任何操作。LOOP 总是需要另一个项目来运行。因此，你需要在新的 LOOP 里填充另一个项目。（如果你查看 loop 项，还会看到一个警告：“未选择项目”。）将 SEQUENCE 项从工具栏拖到 LOOP 项上。这时会弹出一个菜单，询问你是要将 SEQUENCE 插入到 LOOP 项之后还是插入到 LOOP 项之内。选择“插入到 new_loop”。（我们将在第2步再回到这里。）

<div class='info-box' markdown='1'>

__背景框__

__什么是 LOOP 项？__ —— LOOP 项为你的实验添加结构。它会重复运行另一个项目，通常是 SEQUENCE。LOOP 同时也是你定义自变量（即在实验中要操控的变量）的位置。

__什么是 SEQUENCE 项？__ —— SEQUENCE 项同样为实验添加结构。如其名所示，SEQUENCE 会依次运行多个其他项目。

__LOOP-SEQUENCE 结构__ —— 你经常会需要重复一系列事件。为了实现这一点，你需要用 LOOP 项包裹一个 SEQUENCE 项。SEQUENCE 本身并不会重复。它只是从第一个项目开始，依次运行，直到最后一个项目结束。通过用 LOOP 项“包裹”SEQUENCE，你可以使 SEQUENCE 重复多次。例如，一个 trial 通常对应一个名为 *trial_sequence* 的 SEQUENCE。一个包裹 *trial_sequence* 的 LOOP（通常叫 *block_loop*）就构成了一个 block。类似地，在实验的另一个层级，一个叫 *block_sequence* 的 SEQUENCE 可能包含一个 block 的试次，后面还有 FEEDBACK 展示。一个 *practice_phase* 的 LOOP 包裹这个“block” SEQUENCE，就构成了实验的练习阶段。现在这可能看起来有点抽象，但随着本教程的推进，你会逐渐熟悉 LOOP 和 SEQUENCE 的用法。

__小贴士__ —— 关于 SEQUENCE 和 LOOP 的更多信息，请参见：

- %link:loop%
- %link:sequence%

</div>

__为练习结束消息追加一个新的 form_text_display 项__

练习阶段结束后，我们需要告知参与者正式实验即将开始。为此我们需要另一个 `form_text_display`。返回 *experiment* SEQUENCE，将 `form_text_display` 从项目工具栏拖到 LOOP 项上。此时会弹出和前面一样的菜单。这次，选择“插入到 new_loop 之后”。（我们将在第12步回到这里。）

<div class='info-box' markdown='1'>

__小贴士__ —— 如果你不小心更改了 LOOP 要运行的项目，不用担心。你可以通过点击工具栏中的“撤销”按钮（`Ctrl+Shift+Z`）轻松撤销。

</div>

__为实验阶段追加一个新的 loop 项，并包含之前创建的 sequence__

实验阶段也需要一个 LOOP 项，和练习阶段一样。因此，将 LOOP 从项目工具栏菜单拖放到 *_form_text_display* 上。

新创建的 LOOP（名为 *new_loop_1*）是空的，需要像之前创建的 LOOP 一样包含一个 SEQUENCE。不过，由于练习阶段和实验阶段的试次内容是相同的，所以它们可以共享同一个 SEQUENCE。因此，这里你无需从工具栏再拖一个新的 SEQUENCE，可以重用*已存在*的 SEQUENCE（即创建一个链接的副本）。

操作方法如下：右键点击之前创建的 *new_sequence*，选择“复制（链接）”。然后，右键点击 *new_loop_1* 并选择“粘贴”。在弹出的菜单中，选择“插入到 new_loop 1”。

<div class='info-box' markdown='1'>

__背景框__

__提示__ — *链接*副本和*非链接*副本之间有一个重要区别。如果你创建了一个项目的链接副本，你实际上是创建了同一个项目的另一个实例。因此，如果你修改了原始项目，链接副本也会随之改变。相比之下，如果你创建的是一个非链接副本，副本最初看起来会和原件一样（除了名字不同），但你可以编辑原件而不会影响非链接副本，反之亦然。

</div>

__添加一个新的 form_text_display 项目，用于告别信息__

当实验结束时，我们需要向参与者道别。为此我们需要另一个 `form_text_display` 项。返回到*experiment* SEQUENCE，并从项目工具栏拖动一个 `form_text_display` 到 *new_loop_1* 上。在弹出的菜单中，选择“插入到 new_loop_1 之后”。（我们会在第12步回到这里。）

__为新项目命名有意义的名称__

默认情况下，新项目的名称类似*new_sequence*和*new_form_text_display_2*。为项目命名有意义的名称是一种良好的做法。这样可以更容易理解实验的结构。如果需要，你也可以为每个项目添加描述。项目名称只能包含字母、数字和/或下划线。

- 在概览区选择*new_form_text_display*，在标签页顶部区域双击其标签，将其重命名为*instructions*。（概览区快捷键：`F2`）
- 将*new_loop*重命名为*practice_loop*。
- 将*new_sequence*重命名为*block_sequence*。由于你已经在*new_loop_1*中重用了该项目，名称也会自动同步更改。（这说明了在可能的情况下创建链接副本为何高效。）
- 将*new_form_text_display_1*重命名为*end_of_practice*。
- 将*new_loop_1*重命名为*experimental_loop*。
- 将*new_form_text_display_2*重命名为*end_of_experiment*。

__为整个实验命名有意义的名称__

整个实验也有一个标题和描述。在概览区点击“New experiment”。你可以用和为项目命名一样的方法重命名实验。当前的标题是“New experiment”。将实验重命名为“Tutorial: Gaze cuing”。与项目名称不同，实验标题可以包含空格等字符。

现在你实验的概览区看起来像 %FigStep1。现在是保存实验的好时机（快捷键：`Ctrl+S`）。

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of the step 1.
--%


## 步骤2：创建 block_sequence

在概览区点击*block_sequence*。此时，这个 SEQUENCE 是空的。我们希望*block_sequence*包含一个实验块的试次，然后是一个 FEEDBACK 显示。为此我们需要做以下事情：

__添加 reset_feedback 项目以重置反馈变量__

我们不希望反馈受到参与者在指导阶段或之前的实验块中按下的键的影响。因此，我们在每个实验块开始时重置反馈变量。为此我们需要一个 `reset_feedback` 项。从项目工具栏（在“相应收集”下）抓取`reset_feedback`，并将其拖到*block_sequence*中。

__添加一个新的 loop，其中包含一个新的 sequence，用于一组实验试次__

对于单个试次，我们需要一个 SEQUENCE。对于一组实验试次，我们需要多次重复这个 SEQUENCE。因此，对于一个实验块，我们需要用 LOOP 包裹一个 SEQUENCE。从项目工具栏拖动一个 LOOP 到*new_reset_feedback*上。接着，从项目工具栏拖动一个 SEQUENCE 到新建的 LOOP 上，并在弹出菜单中选择“插入到 new_loop 中”。（我们将在第3步回到这里。）

__添加一个 feedback 项__

在每个试验区块结束后，我们希望向被试提供反馈，以便让被试知道自己的表现如何。为此，我们需要一个 FEEDBACK 项目。从项目工具栏中将一个 FEEDBACK 拖放到 *new_loop* 上，并在出现的弹出菜单中选择“Insert after loop”。（我们将在步骤 10 返回到这一部分。）

__给新项目起有意义的名称__

重命名：（如果你不记得如何操作，请参考步骤 1。）

- 将 *new_loop* 重命名为 *block_loop*
- 将 *new_sequence* 重命名为 *trial_sequence*
- 将 *new_reset_feedback* 重命名为 *reset_feedback*
- 将 *new_feedback* 重命名为 *feedback*

你的实验总览现在应如 %FigStep2 所示。请记得定期保存你的实验。

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## 步骤3：使用自变量填充 block loop

正如其名，*block_loop* 对应一个试验区块。在上一步中，我们创建了 *block_loop*，但我们还需要定义将在区块内变化的自变量。我们的实验包含三个自变量：

- __gaze_cue__ 可以为 'left' 或 'right'。
- __target_pos__（目标位置）可以是 '-300' 或 '300'。这些值代表目标在像素坐标中的 X 坐标（0 = 屏幕中心）。直接使用坐标值而不是 'left' 和 'right'，在之后我们创建目标呈现时会更方便（见步骤5）。
- __target_letter__（目标字母）可以是 'F' 或 'H'。

因此，我们的实验有 2 x 2 x 2 = 8 个水平。尽管8个水平不是很多（大多数实验会更多），我们也无需手动输入所有组合。点击总览中的 *block_loop* 打开其标签页。现在点击“Full-factorial design” 按钮。在变量向导中，只需在第一行输入变量名，在其下方的几行输入各自的水平即可（见 %FigVariableWizard）。选择“Ok”后，你会看到 *block_loop* 填充了全部8种可能的组合。

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  The loop variable wizard in Step 3.
--%

在生成的循环表中，每一行对应 *trial_sequence* 的一次运行。就我们而言，*trial_sequence* 的一次运行对应一个试验，因此循环表中的每一行对应一条试验。每一列对应一个变量，该变量在每条试验中可以有不同的值。

但我们还没完成。我们还需添加三个变量：干扰项的位置、正确反应以及一致性（congruency）。

- __dist_pos__ —— 在第一个空列的首行输入 'dist_pos'，这会自动添加一个名为 'dist_pos' 的实验变量。在其下的各行，“target_pos”为 -300 时输入 '300'，“target_pos”为 300 时输入 '-300'。换句话说，目标和干扰项应分别位于相对的位置。
- __correct_response__ —— 在另一个空列创建一个名为 'correct_response' 的变量。当 'target_letter' 为 'F' 时，“correct_response”设为 'z'；当 'target_letter' 为 'H' 时，设为 'm'。这意味着被试看到 'F' 时应按 'z' 键，看到 'H' 时应按 'm' 键。（如果 'z' 与 'm' 在你的键盘布局中操作不便，可选择其他按键，例如在 AZERTY 键盘上 'w' 与 'n' 更合适。）
- __congruency__ —— 创建另一个名为 'congruency' 的变量。当 'target_pos' 为 '-300' 且 'gaze_cue' 为 'left'，或 'target_pos' 为 '300' 且 'gaze_cue' 为 'right' 时，'congruency' 设为 'congruent'。也就是说，如果脸部注视目标，该试验为一致（congruent）。当脸部注视干扰项时，将 'congruency' 设为 'incronguent'。虽然运行实验不需要“congruency”变量，但用于后续分析数据非常有用。

我们还需要做最后一件事。'Repeat' 目前设为 '1.00'，这意味着每个循环只执行一次。所以现在的 block 包含 8 个试次，这有点太少了。合理的 block 试次数是 24，因此请将 'Repeat' 设为 3.00（3 次重复 x 8 个循环 = 24 个试次）。你无需更改 'Order'，因为我们需要的正是 'random'。

现在 *block_loop* 如 %FigStep3 所示。请记住要经常保存你的实验。

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

__背景框__

__提示__ —— 你可以在你喜欢的电子表格程序中准备循环表，并将其复制粘贴到 LOOP 变量表中。

__提示__ —— 你可以将循环表保存在单独的文件（`.xlsx` 或 `.csv` 格式）中，并直接使用此文件。方法是，在 'Source' 下选择 'file'。

__提示__ —— 你可以将 'Repeat' 设置为非整数。例如，若将 'Repeat' 设为 '0.5'，只有一半试次（随机选取）会被执行。

</div>

## 步骤4：添加图片和音频文件到文件池

我们将使用文件中的图片作为刺激材料。此外，如果被试反应错误，我们将播放一段音频。为此我们需要一份音频文件。

你可以在这里下载所需文件（在大多数网页浏览器中，你可以右键点击链接并选择“另存为”或类似选项）:

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

下载这些文件（比如保存到桌面）后，你可以将它们添加到文件池中。如果文件池没有显示（默认在窗口的右侧），请点击主工具栏上的“显示文件池”按钮（快捷键：`Ctrl+P`）。最简单的添加方法是将这四个文件从桌面（或你下载到的地方）拖到文件池中。或者，你也可以点击文件池中的“+”按钮，通过弹出的文件选择对话框添加文件。文件池会自动和你的实验一起保存。

此时你的文件池如 %FigStep4 所示。请记得经常保存你的实验。

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

## 步骤5：用项目填充 trial sequence

我们实验的一个试次包含如下流程：

1. __注视点__ —— 750 毫秒，SKETCHPAD 项目
2. __中性凝视__ —— 750 毫秒，SKETCHPAD 项目
3. __凝视线索__ —— 500 毫秒，SKETCHPAD 项目
4. __目标__ —— 0 毫秒，SKETCHPAD 项目
5. __收集反应__ —— KEYBOARD_RESPONSE 项目
6. __如果反应错误播放一段音频__ —— SAMPLER 项目
7. __将反应记录到文件__ —— LOGGER 项目

在概览中点击 *trial_sequence* 以打开 *trial_sequence* 标签。从项目工具栏中取出一个 SKETCHPAD 并拖入 *trial_sequence*。再重复三次，使 *trial_sequence* 包含四个 SKETCHPAD。接着，依次加入一个 KEYBOARD_RESPONSE 项目、一个 SAMPLER 项目和一个 LOGGER 项目。

同样，为了让 *trial_sequence* 更易理解，我们需要重命名这些新项目。请重命名为：

- *new_sketchpad* 改为 *fixation_dot*
- *new_sketchpad_1* 改为 *neutral_gaze*
- *new_sketchpad_2* 改为 *gaze_cue*
- *new_sketchpad_3* 改为 *target*
- *new_keyboard_response* 改为 *keyboard_response*
- *new_sampler* 改为 *incorrect_sound*
- *new_logger* 改为 *logger*

默认情况下，项目始终会被执行，这由运行条件表达式 `True` 表示。然而，我们希望对 *incorrect_sound* 项目进行更改，这个项目只应在出现错误时才被执行。为此，我们需要在 *trial_sequence* 选项卡中，将“Run if”表达式更改为 `correct == 0`。这是可行的，因为 *keyboard_response* 项目会自动创建一个 `correct` 变量，其值为 `1`（正确）、`0`（错误）或 `undefined`（这依赖于在第3步定义的 `correct_response` 变量）。双等号是 Python 语法，表示用来比较两个内容是否相等，在本例中即变量 `correct` 是否等于0。要更改运行条件表达式，双击它（快捷键：`F3`）。

现在 *trial_sequence* 如 %FigStep5 所示。

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%

<div class='info-box' markdown='1'>

__知识框__

__SKETCHPAD 项目是什么？__ -- SKETCHPAD 用于呈现视觉刺激：文本、几何图形、注视点、Gabor补丁等。你可以利用内置绘图工具在 SKETCHPAD 上绘制。

__KEYBOARD_RESPONSE 项目是什么？__ -- KEYBOARD_RESPONSE 项目用于收集参与者来自键盘的单次反应。

__SAMPLER 项目是什么？__ -- SAMPLER 项目用于播放声音文件中的声音。

__LOGGER 项目是什么？__ -- LOGGER 项目将数据写入日志文件。这非常重要：如果你忘记加入 LOGGER 项目，实验期间不会有数据被记录！

__提示__ -- 变量和条件“if”表达式非常强大！想了解更多内容，请参阅：

- %link:manual/variables%

</div>

## 步骤6：绘制 sketchpad 项目

我们在第5步创建的 SKETCHPAD 项目目前还是空白的。现在是时候来绘制一些内容了！

__将背景色设置为白色__

点击概览区的 *fixation_dot* 以打开其选项页。SKETCHPAD 仍然是深灰色，而我们下载的图像背景是白色。噢，我们忘了将实验的背景色设为白色（默认是深灰色）！点击概览区中的 'Tutorial: Gaze cuing' 打开‘General properties’选项卡。将“Foreground”改为“black”，将“Background”改为“white”。

<div class='info-box' markdown='1'>

__知识框__

__提示__ -- 若要更精细地控制颜色，也可以使用十六进制RGB表示法（如 `#FF000` 表示红色），使用多种色彩空间，或使用颜色选择工具。参见：

- %link:manual/python/canvas%

</div>

__绘制注视点__

返回 *fixation_dot*，方法是在概览中点击 *fixation_dot*。现在，点击带有十字光标的按钮选中注视点元素。将鼠标移至 sketchpad 上时，可在右上角看到屏幕坐标。将（前景）颜色设置为“black”。点击屏幕中央（0, 0），绘制中央注视点。

最后，将“Duration”字段从“keypress”更改为“745”，因为我们希望注视点展示750毫秒。等等……*为什么我们不直接设为750ms的时长？* 原因是实际显示呈现的时长始终会向上取整为与你显示器刷新率兼容的数值。这听起来可能有点复杂，但对于大多数用途，遵循以下经验法则就够用了：

1. 选择一个与你的显示器刷新率相适应的时长。例如，如果你的显示器刷新率为60 Hz，这意味着每一帧持续16.7毫秒（= 1000毫秒/60 Hz）。因此，在60 Hz的显示器上，你应始终选择16.7毫秒的倍数作为时长，比如16.7、33.3、50、100等。
2. 在SKETCHPAD的时长字段中，指定一个比你目标时长稍微少几毫秒的数值。所以如果你想显示SKETCHPAD 50毫秒，选择45。如果你想显示SKETCHPAD 1000毫秒，选择995。以此类推。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 关于实验计时的详细讨论，请参见：

- %link:timing%

__提示__ -- SKETCHPAD的持续时间可以以毫秒为单位的数值，也可以输入'keypress'或'mouseclick'，分别用于收集键盘按键或鼠标点击。在这种情况下，SKETCHPAD的作用类似于KEYBOARD_RESPONSE项目（但选项更少）。

__提示__ -- 请确保（前景）颜色设置为黑色。否则你将在白色背景上绘制白色内容，将无法看到任何东西！

</div>

__绘制中性凝视__

打开*neutral_gaze* SKETCHPAD。现在通过点击带有山景图标的按钮选择图片工具。在屏幕中心（0, 0）单击。“从池中选择文件”对话框会出现。选择文件`gaze_neutral.png`，并点击“选择”按钮。中性凝视的图片现在将正对你出现在屏幕中央！最后，像之前一样，将“持续时间”字段从“keypress”更改为“745”。（再次注意，这意味着在大多数显示器上持续时间为750毫秒！）

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- OpenSesame可以处理多种图片格式。然而，某些（非标准的）`.bmp`格式可能会导致问题。如果发现无法显示`.bmp`图片，可以将其转换为其它格式，如`.png`。你可以使用[GIMP]等免费工具轻松转换图片格式。
</div>

__绘制视线线索__

打开*gaze_cue* SKETCHPAD，再次选择图片工具。在屏幕中心（0, 0）处点击，选择文件`gaze_left.png`。

但还没完！因为视线线索不应总是“left”，而应该取决于变量`gaze_cue`，这个变量我们在步骤3里已经定义。不过，通过将`gaze_left.png`绘制到SKETCHPAD上，我们已经生成了一段脚本，只需做一个小改动就可以确保正确的图片被显示。点击*gaze_cue*标签右上角的“选择视图”按钮，选择“查看脚本”。你现在会看到与我们刚刚创建的sketchpad对应的脚本：

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

我们唯一需要做的就是将`gaze_left.png`替换为`gaze_{gaze_cue}.png`。这意味着OpenSesame将利用变量`gaze_cue`（其值为`left`或`right`）来决定显示哪张图片。

既然如此，不妨也把持续时间改为“495”（四舍五入为500！）。脚本现在如下：

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

点击右上角的“应用”按钮以保存你对脚本的更改，并返回常规控件界面。OpenSesame会警告你，由于图片由变量定义，无法显示，因此会显示一个占位图片。别担心，实验运行时会正确显示该图片！

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 变量检查器（快捷键：`Ctrl+I`）是一个强大的工具，可以帮助你了解在实验中定义了哪些变量，以及它们的当前值（见 %FigVariableInspector）。当实验没有运行时，大多数变量还没有值。但如果你在窗口中运行实验，并让变量检查器保持可见，你可以实时看到变量的变化。这对于调试实验非常有用。

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "变量检查器是便捷地概览实验中所有变量的方式。"
--%

</div>

__绘制目标__

我们希望目标显示包含三个对象：目标字母、干扰字母和注视线索（见 %FigGazeCuing）。和之前一样，我们将先用SKETCHPAD编辑器创建一个静态显示。之后，只需对脚本做一些小的改动，使具体显示内容依赖于变量。

点击概览中的*target*，打开target标签页，像之前一样，在屏幕中央绘制`gaze_left.png`图片。现在点击带有“A”图标的按钮，选中绘制文本工具。将前景色改为“黑色”（如果不是的话）。默认字体大小是18像素，对于本实验来说稍小一些，所以改为32像素。接下来，在SKETCHPAD上点击(-320, 0)位置（X坐标不必精确为320，因为之后会改成变量）。在弹出的对话框里输入"{target_letter}"，以绘制目标字母（绘制文本时可以直接使用变量）。类似地，点击(320, 0)，绘制一个“X”（干扰项始终是X）。

现在，点击标签页右上角的“选择视图”按钮，并选择“查看脚本”，打开脚本编辑器。脚本应如下所示：

~~~ .python
set duration keypress
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

像之前一样，将`gaze_left.png`改为`gaze_{gaze_cue}.png`。同时，我们还需要让目标和干扰项的位置分别取决于变量`target_pos`和`dist_pos`。只需将`-320`改为`{target_pos}`，将`320`改为`{dist_pos}`。注意保留Y坐标`0`。此时脚本应如下：

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

点击“应用”按钮应用脚本并返回普通项目控制界面。

最后，将“Duration”字段设为“0”。这并不是表示目标只呈现0毫秒，而是实验会立即进入下一个项目（即*keyboard_response*）。由于*keyboard_response*会等待响应，但不会更改屏幕内容，因此目标会一直保持可见，直到作出反应。

记得经常保存你的实验。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- SKETCHPAD 的每个元素都有一个“显示条件 (Show if)”选项，用于指定何时显示该元素。你可以用它根据某些变量隐藏/显示 SKETCHPAD 上的元素，和在 SEQUENCE 中使用 run-if 语句类似。

__提示__ -- 请确保（前景）颜色设置为黑色，否则你会在白底上画白色，看不到任何内容！

</div>

## 步骤7：配置 keyboard_response 项

点击总览中的 *keyboard_response* 以打开其标签页。你会看到三个选项：正确反应（Correct response）、允许反应（Allowed responses）、超时（Timeout）和事件类型（Event type）。

我们已经在第3步中设置了 `correct_response` 变量。除非我们明确指定正确反应，否则 OpenSesame 会自动使用 `correct_response` 变量（如果可用）。因此，我们无需更改此处的“正确反应”字段。

我们需要设置允许的反应。在允许反应字段中输入“z;m”（如果你选择了其他按键则输入其它按键）。分号用于分隔不同的反应。现在，KEYBOARD_RESPONSE 只接受“z”和“m”键，其他所有按键（除了“escape”键）都会被忽略，“escape”键用于暂停实验。

我们还希望设置一个超时时间，它指定 KEYBOARD_RESPONSE 等待的最长时间间隔，然后将该反应视为错误并将“response”变量设置为“None”。“2000”毫秒是个不错的值。

我们不需要更改 Event type，因为我们希望参与者按下按键来作答（keypress，默认）而不是松开按键（keyrelease）。

现在，KEYBOARD_RESPONSE 看起来如 %FigStep7 所示。

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "The KEYBOARD_RESPONSE at the end of Step 7."
--%

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 默认情况下，KEYBOARD_RESPONSE 会使用 `correct_response` 变量来判断反应是否正确。但你也可以使用其他变量。为此，在正确反应字段中输入花括号括起来的变量名（如 `{my_variable}`）。

__提示__ -- 如果启用了“清除挂起按键”（默认启用），当调用 KEYBOARD_RESPONSE 项时，所有待处理的按键都会被清除。这可以防止携带效应，比如参与者在实验过程中非响应部分意外按下了按键。

__提示__ -- 若要使用特殊按键（如“/”或上箭头键），你可以使用按键名称（如“up” 和 “space”）或相关字符（如“/” 和 “]”）。“列出所有可用按键（List available keys）”按钮可以显示所有有效按键名称的列表。

</div>

## 步骤8：配置错误音效 (sampler) 项

*incorrect_sound* 项无需太多操作：我们只需选择要播放的声音。点击总览中的 *incorrect_sound* 打开其标签页。点击“浏览 (Browse)”按钮，从文件池中选择 `incorrect.ogg`。

此时 sampler 如 %FigStep8 所示。

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "The *incorrect_sound* item at the end of Step 8."
--%

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 你可以用变量来指定要播放的声音，只需在文件名中用花括号括起来变量名即可作为（部分）文件名。例如：`{a_word}.ogg`

__提示__ -- SAMPLER 支持 `.ogg`、`.mp3` 和 `.wav` 格式的音频文件。如果你有其他格式的音频文件，[Audacity] 是一个很棒的免费工具可以用来转换音频（以及更多用途）。

</div>

## 步骤9：配置变量 logger

其实我们无需配置变量 LOGGER，但我们还是来看一下。点击总览中的 *logger* 以打开其标签页。你会看到“自动记录所有变量（Automatically log all variables）”选项已被选中。这意味着 OpenSesame 会记录所有内容，这样很好。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 如果你希望日志文件简洁，可以关闭“自动记录所有变量”选项，并手动选择要记录的变量，方法是在“添加自定义变量”中手动输入变量名，或将变量从变量检查器中拖到 LOGGER 表格中。你也可以保持“自动记录所有变量”选项开启，并排除你不关心的变量。

__最重要的建议__ -- 总是要三次核查你实验中是否记录了所有必要的变量！最佳检查方法是运行实验并检查生成的日志文件。

</div>

## 步骤10：绘制反馈项

每个实验区块结束后，我们希望呈现反馈信息给被试，让他们知道自己完成得怎么样。因此，在第2步中，我们已经在 *block_sequence* 的最后添加了一个名为 *feedback* 的 FEEDBACK 项。

点击概览中的 *feedback* 打开其标签页，选择“绘制文本”工具，将前景色设为“黑色”（如果尚未设为黑色），并点击 (0, 0)。现在输入以下文本：

```text
区块结束

你的平均反应时是 {avg_rt} 毫秒
你的准确率是 {acc} %

按任意键继续
```

因为我们希望反馈项一直显示，直到被试愿意继续（即，直到他/她按下某个键），所以将“持续时间”字段保留为“keypress”。

现在的反馈项如 %FigStep_10 所示。

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "The feedback item at the end of Step 10."
--%

<div class='info-box' markdown='1'>

__背景框__

__什么是反馈项？__ -- FEEDBACK 项和 SKETCHPAD 项几乎完全相同。唯一的区别是 FEEDBACK 项不会提前准备好。这意味着你可以用它来呈现需要最新被试信息的反馈。你不应该用 FEEDBACK 项来呈现对时间精度要求高的显示，因为它不是提前准备好的，因此时间精度不如 SKETCHPAD。另见：

- %link:visual%

__反馈与变量__ -- 响应项会自动记录被试的准确率和平均反应时，分别保存在变量 'acc'（同义词：'accuracy'）和 'avg_rt'（同义词：'average_response_time'）中。另见：

- %link:manual/variables%

__提示__ -- 请确保（前景）颜色被设置为黑色，否则你会把白字写在白底上，看不到任何内容！

</div>

## 步骤11：设置练习阶段与实验阶段的长度

我们之前已经建立了 *practice_loop* 和 *experiment_loop* 项，这两项都会调用 *block_sequence*（即一个实验区块）。但目前它们都只调用了一次 *block_sequence*，也就是说练习阶段和正式实验阶段都只有一个区块。

点击 *practice_loop* 打开其标签页，将“重复”设置为“2.00”。这表示练习阶段包含两个区块。

点击 *experimental_loop* 打开其标签页，将“重复”设置为“8.00”。这表示实验阶段包含八个区块。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 你可以在 *practice_loop* 和 *experimental_loop* 中都创建一个变量 `practice`，并分别设置为“yes”和“no”。这样可以轻松记录哪些试次属于练习阶段。

</div>

## 步骤12：编写说明、练习结束与实验结束的表单

我想你可以自己完成这一步！只需打开相应项目，添加一些文本，用于呈现指导语、练习结束消息和实验结束消息。

<div class='info-box' markdown='1'>

__背景框__

__提示__ -- 你可以使用部分 HTML 标签来格式化文本。例如，*&lt;b&gt;这将是加粗的&lt;b&gt;* 和 *&lt;span color='red'&gt;这会显示为红色&lt;span&gt;*。更多信息请参见：

- %link:text%

</div>

## 步骤13：运行实验！

你已经完成了！点击工具栏中的「窗口中运行」（快捷键：`Ctrl+W`）或「全屏运行」（快捷键：`Ctrl+R`）按钮来运行你的实验。

<div class='info-box' markdown='1'>

__背景箱__

__提示__ —— 进行测试运行时，可以点击橙色的「窗口中运行」按钮（快捷键：`Ctrl+Shift+W`），这样不会询问你如何保存日志文件（因此仅适用于测试目的）。

</div>

## 理解错误

能够理解错误信息是在使用OpenSeame时必备的技能。毕竟，刚建立的实验很少能立刻毫无错误地运行！

假设我们在上述步骤中犯了一个错误。当试图运行实验时，我们会收到如下错误信息（%FigErrorMessage）：

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "An error message in OpenSesame."
--%

错误信息以名称开头，本例中为 `FStringError`，指明了错误的大致类型。接下来是一段简短的说明文字，此处为“Failed to evaluate f-string expression in the following text: gaze_{gaze_ceu}.png”。即使你不了解f-string是什么（它是一种包含大括号中Python代码的字符串），也能清楚这里的文本'{gaze_ceu}.png'出现了问题。

错误信息还指出，此错误来自 *gaze_cue* 条目的prepare阶段。

最后，错误信息具体说明了在评估文本'gaze_{gaze_ceu}.png'时出错的原因：名为'gaze_ceu'的变量未定义。

仔细阅读错误信息后，原因和解决办法大概已经浮现在你脑海：我们在 *gaze_cue* 条目中简单地拼写错误，把'{gaze_ceu}'写成了'{gaze_cue}'！由于没有名为`gaze_ceu`的变量，所以出现了错误。只需打开 *gaze_cue* 条目的脚本纠正拼写错误即可轻松解决。

## 最后：关于时间控制和backend选择的一些通用考虑

在实验的「通用属性」标签页（点击实验名称打开的标签页）中，你可以选择backend。backend是控制显示、输入设备、声音等的软件层。大多数实验可以在所有backend上运行，但有时出于时间控制的需要，更适合选择特定backend。目前有四种backend（具体可用与否取决于你的系统，并非所有三种都保证可用）：

- __psycho__ —— 基于PsychoPy [(Peirce, 2007)][references] 的硬件加速backend。这是默认选项。
- __xpyriment__ —— 基于Expyriment [(Krause & Lindeman, 2013)][references] 的硬件加速backend
- __legacy__ —— 一种“安全”的backend，基于PyGame。它在大多数平台上性能可靠，但由于缺乏硬件加速，其时间控制特性不如其他backend。
- __osweb__ —— 在浏览器中运行实验 [(Mathôt & March, 2022)][references]。

另见：

- %link:backends%
- %link:timing%

## 参考文献

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame：用于社会科学的开源图形实验构建器。*行为研究方法*, *44*(2), 314-324。doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). 使用OpenSesame和OSWeb在线进行语言学实验。*语言学习*。doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy：基于Python的心理物理学软件。*神经科学方法杂志*, *162*(1-2), 8-13。doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). 时钟的时间分辨率：对反应时测量的影响——坏时钟的好消息。*英国数学与统计心理学杂志*, *42*(1), 1-12。doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about