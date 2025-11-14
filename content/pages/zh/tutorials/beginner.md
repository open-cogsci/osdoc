title: 初学者教程：注视线索
hash: 1bc0db6f02f63201f3d90855479f82e8a246736a8141fb744439c06fe8783002
locale: zh
language: Chinese

## 关于 OpenSesame

OpenSesame 是一个免费的程序，用于快速开发心理学、认知神经科学和实验经济学的行为实验。对于初学者，OpenSesame 提供了一个全面的图形化、点选界面。对于高级用户，OpenSesame 支持 Python 和 JavaScript 脚本（本教程未涉及）。

## 关于本教程

我们将创建一个经典的凝视引导实验。这是一个有趣且引人入胜的实验范式，人们总是会不自觉地跟随面部看向的方向。

我们只会使用图形化界面。我们*不会*使用 Python 或 JavaScript 编码。（这是中级教程的内容。）本教程大约需要一小时。

## 你将学到什么

完成本教程后，你将会知道如何：

- 💡 使用 SEQUENCE 和 LOOP 项目构建实验结构
- 💡 在 LOOP 表中定义具有自变量的全因子实验设计
- 💡 使用 SKETCHPAD 项目创建视觉刺激
- 💡 使用 KEYBOARD_RESPONSE 项目收集反应
- 💡 使用 FEEDBACK 项目为参与者提供反馈
- 💡 使用 FORM_TEXT_DISPLAY 项目显示文本
- 💡 使用变量定义你的刺激
- 💡 使用条件（run-if）表达式控制实验流程
- 💡 在文件池中组织刺激文件
- 💡 日志数据

## 你需要准备什么

**OpenSesame 4.1 或更高版本**，并已安装所有更新。如果看到可用更新通知，请点击“Install updates...”，然后点击“Run update script”。更新后请重启 OpenSesame。你也可以在 OpenSesame 控制台手动运行以下命令来更新。

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

## 实验简介

如前所述，我们将创建一个最初由[Friesen 和 Kingstone (1998)][references]开发的凝视引导实验。具体流程如下：

1. 一个面孔出现在屏幕中央
2. 面孔看向左侧或右侧
3. 一个目标字母（‘F’ 或 ‘H’）出现在一侧
4. 一个干扰字母（‘X’）出现在另一侧
5. 参与者需尽快识别目标字母

实验包括练习阶段和实验阶段。每个区块结束后你会显示反馈。错误反应后会播放一段声音。

有趣的发现是什么？当面部看向目标时，人们反应更快，即使眼神方向并不能预测目标出现的位置。这说明人类会自动跟随他人的目光。

## 第一步：创建主序列

🎯 __目标：__ 本步骤中，我们将建立实验的基本结构：一个练习阶段（参与者可以练习任务）、一个实验阶段（我们将在此收集分析数据），以及这些阶段前后的提示屏幕。我们仅设置结构，细节将在后续实现。

启动 OpenSesame 时，会出现“Get started!” 选项卡（%FigGetStarted）。请选择 “Default template”。

打开名为 *experiment* 的主 SEQUENCE。默认包含两个项目：记事本（*getting_started*）和 SKETCHPAD（*welcome*）。


- 点击任何项目标签中的帮助图标以获取上下文帮助。
- 经常保存（Ctrl+S）。备份会自动创建（工具 → 打开备份文件夹）。
- 删除的项目可以从“未使用项目”中恢复，除非被永久删除（Shift+Del）。
- 请参见下图，我们将构建的结构。

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  Structure of the gaze-cuing experiment. Item types in bold, item names regular.
--%

</details>

移除默认项目：

- 右键点击 *getting_started* → 删除
- 右键点击 *welcome* → 删除

现在 *experiment* SEQUENCE 是空的。添加一个表单用于指令：

- 从工具栏中拖动一个 FORM_TEXT_DISPLAY（表单）到 *experiment*。这将在开始显示指令（我们将在第12步定义实际的指令）。

为练习阶段添加带有 SEQUENCE 的 LOOP：

- 将一个 LOOP 拖动到 *experiment*（放在指令表单之后）。
- 拖动一个 SEQUENCE 到 LOOP 中，并选择“插入到 [循环项目名称]”。

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多有关 LOOP/ SEQUENCE 结构的信息</summary>

你经常需要重复一系列事件，比如一次试次。这通常通过组合一个 LOOP（循环单个项目）和一个 SEQUENCE（按顺序运行多个项目）来实现。

举例：一个 *block_loop* 包含一个 *trial_sequence*，而 *trial_sequence* 又包含多个对应一次试次的项目。一起，这个 LOOP/ SEQUENCE 结构就对应了一组多次试次的区块。

</details>

在练习结束后添加一个表单

- 在 *experiment* 中，再拖动一个 FORM_TEXT_DISPLAY，并选择“在 [练习循环项目名称] 后插入”。这将显示“练习结束”信息（第12步）。

为实验阶段添加一个 LOOP，复用与练习 LOOP 相同的 SEQUENCE 的链接副本：

- 拖动一个 LOOP 并插入到练习结束表单之后。
- 复用你为练习 LOOP 创建的 SEQUENCE：
  - 右键点击已有的 SEQUENCE > 复制（链接副本）。
  - 右键点击新的实验 LOOP > 粘贴 > “插入到 [实验循环]”。

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多关于链接副本与非链接副本的信息</summary>

当同一个项目在多个地方出现时，它们就是链接副本。使用链接副本很方便，因为如果你要更改该项目，只需修改一次即可。

非链接副本彼此独立，因此你可以更改其中一个而不影响其他的。

建议尽量使用链接副本！

</details>

添加一个结束表单：

- 拖动一个 FORM_TEXT_DISPLAY 并插入到实验循环之后。

为了清晰，重命名这些项目：

- new_form_text_display → *instructions*
- new_loop → *practice_loop*
- new_sequence → *block_sequence*（链接副本会自动更新）
- new_form_text_display_1 → *end_of_practice*
- new_loop_1 → *experimental_loop*
- new_form_text_display_2 → *end_of_experiment*

重命名实验：

- 在概览中点击 New experiment。重命名为“Tutorial: Gaze cuing”。然后保存（Ctrl+S）。

%--
figure:
 id: FigStep_1
 source: step1.png
 caption: |
  Overview at the end of Step 1.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多关于不同类型项目的信息</summary>

- SEQUENCE：按顺序运行各项。
- LOOP：重复另一项，通常是 SEQUENCE，并定义自变量。
- SKETCHPAD：呈现视觉刺激。提前准备，因此适用于需要精确计时的刺激。
- FEEDBACK：呈现视觉刺激。不是提前准备的，因此适合呈现最新内容，如关于参与者反应的反馈。
- KEYBOARD_RESPONSE：收集单次按键反应。
- SAMPLER：播放文件中的声音。
- LOGGER：将数据写入文件。
- RESET_FEEDBACK：在区块开始时重置反馈变量。
- FORM_TEXT_DISPLAY：使用表单布局显示文本。

</details>

## 步骤2：创建区块序列

🎯 __目标：__ 在本步骤中，我们将再次为实验添加结构。这一次我们要实现单一区块试次的结构，即 *block_sequence*。我们只设置结构，细节稍后再实现。

打开 *block_sequence*，并按顺序添加如下项目：

- RESET_FEEDBACK（在区块开始时重置反馈变量）
- LOOP，并在其中插入一个新的 SEQUENCE（处理实际的循环和试次逻辑）
- FEEDBACK（在区块结束时为参与者提供反馈）

重命名

- new_reset_feedback → *reset_feedback*
- new_loop → *block_loop*
- new_sequence → *trial_sequence*
- new_feedback → *feedback*

%--
figure:
 id: FigStep_2
 source: step2.png
 caption: |
  步骤2结束时的概览。
--%


## 步骤3：用自变量填充 block_loop

🎯 __目标：__ 在本步骤中，我们将定义实验的自变量（条件）。本实验是一个完全随机实验设计的例子，这意味着自变量从试次到试次会发生变化。

打开 *block_loop*。点击全因子设计。定义：

- `gaze_cue`：left，right
- `target_pos`：-300, 300（x坐标，单位为像素；0=中心；负值=左）
- `target_letter`：F，H

这将产生 2×2×2 = 8 种组合。我们还需要根据上述变量派生出若干变量。为此，你需要手动为每个变量添加一列，并在每个单元格中输入正确的值。

- `dist_pos`：每一行，如果 `target_pos` 为 -300，则设为 300；如果 `target_pos` 为 300，则设为 -300
- `correct_response`：F 为 z，H 为 m
- `congruency`：如果 gaze cue 朝向目标则为 congruent，否则为 incongruent

确保循环表包含 8 行。然后将 Repeat 设置为 3，这样每个区块最终有 3 × 8 = 24 个试次。

%--
figure:
 id: FigStep_3
 source: step3.png
 caption: |
  步骤3结束时的 *block_loop*。
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>进一步了解LOOP表</summary>

- 你可以从电子表格中复制-粘贴一张表，或者将 Source 设置为 file，加载 .csv/.xlsx 文件。
- Repeat 可以为小数。例如，将 Repeat 设置为 0.5 时，只随机抽取一半的行运行。

</details>


## 步骤4：将图片和音频文件添加到文件池

🎯 __目标：__ 本步骤使用文件池将刺激文件（图片和一个音频）与实验打包绑定。

下载以下文件：

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

打开文件池（Ctrl+P）并将文件拖入其中。或使用 + 按钮添加。文件池会自动与实验一起打包。

%--
figure:
 id: FigStep_4
 source: step4.png
 caption: |
  步骤4结束时的文件池。
--%

## 步骤5：用项目填充试次序列

🎯 __目标：__ 在本步骤中，我们将定义试次序列。现在我们只添加所需的项目，暂不定义细节，稍后再做。 

一次试次包括：

1. 注视点 — 750 毫秒 — SKETCHPAD  
2. 中性凝视 — 750 毫秒 — SKETCHPAD  
3. 注视线索 — 500 毫秒 — SKETCHPAD  
4. 目标 — 0 毫秒 — SKETCHPAD（0 毫秒的时长使实验能立刻进入反应收集阶段）  
5. 反应收集 — KEYBOARD_RESPONSE  
6. 错误音效 — SAMPLER（仅在错误时运行）  
7. 日志 — LOGGER  

打开 *trial_sequence*，并按照上面顺序排列项目。完成后重命名如下：

- *new_sketchpad* → *fixation_dot*
- *new_sketchpad_1* → *neutral_gaze*
- *new_sketchpad_2* → *gaze_cue*
- *new_sketchpad_3* → *target*
- *new_keyboard_response* → *keyboard_response*
- *new_sampler* → *incorrect_sound*
- *new_logger* → *logger*

在 *trial_sequence* 中，将 *incorrect_sound* 的 run-if 设置为：`correct == 0`。这里要用双等号（`==`），用于判断两个值是否相等。此处是判断 `correct` 是否等于 0。如果误用了单等号（如 `correct = 1`），运行实验时会遇到 `SyntaxError` 错误。

%--
figure:
 id: FigStep_5
 source: step5.png
 caption: |
  *trial_sequence* 在第五步结束后的界面。
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多关于变量与 run-if 表达式的知识</summary>

变量和条件（run-if）表达式非常强大！查阅 %link:manual/variables%

</details>


## 第六步：绘制 sketchpad 项目

🎯 __目标：__ 本步骤中，我们将定义试次序列里的四个 SKETCHPAD 项：注视点、中性凝视（直视）、注视线索（看向左侧或右侧）、目标显示（线索还在偏左或右时，两个字母分别呈现在两侧）。

将实验的背景色设为白色，前景色设为黑色：

- 点击实验标题打开通用属性
- 将背景色设为“white”，前景色设为“black”

定义注视点：

- 打开 *fixation_dot*
- 选择 fixdot 元素。它是画布左侧垂直工具栏中的注视点图标。
- 在显示屏中心 (0, 0) 绘制注视点
- 设置时长为 745 毫秒。显示时长会自动向上取整到目标时长 750 毫秒。

<details class='info-box' markdown='1'>

<summary markdown='1'>为什么在希望显示 750 毫秒时要设置 745 毫秒？</summary>

显示内容是周期性刷新的。在 60 Hz 显示器上，一次刷新周期是 1000 / 60 = 16.67 毫秒。这意味着，在 60 Hz 上，显示时长只能是 16.67 的倍数。

745 不是 16.67 的倍数，因此时长会被向上取整至最近的倍数，即 750 毫秒。

详情见：

- %link:timing%

</details>

定义中性凝视显示：

- 打开 *neutral_gaze*
- 选择 image 元素
- 在屏幕中心绘制图片，并在文件池弹框中选择 `gaze_neutral.png`
- 设置时长为 745 毫秒

定义注视线索显示：

- 打开 *gaze_cue*
- 在屏幕中心绘制 `gaze_left.png`

但是，我们并不总是要显示 `gaze_left.png`。我们希望变量 `gaze_cue` 为“left”时显示 `gaze_left.png`，为“right”时显示 `gaze_right.png`。也就是说，应该显示 `gaze_{gaze_cue}.png`，其中花括号表示要插入变量。

我们可以通过编辑项目脚本实现。点击 “选择视图”（右上角三个图标的中间一个） → “查看脚本”。这可以显示定义该项目的 OpenSesame 脚本（注意这不是 Python 或 JavaScript！）。按照下方所示更改 `draw image` 命令。顺便，也可以指定时长（注意 495 毫秒会被自动向上取整到 500 毫秒，如前述）。

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

点击“应用”。视图现在切换回图形控件视图。图像现在显示为一个问号。别担心！在实验过程中会显示正确的图像。

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多关于实验中存在的变量</summary>

打开变量检查器（Ctrl+I），查看实验中存在哪些变量。当实验运行时，你还可以实时看到它们的数值变化！

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: |
  变量检查器。
--%

</details>

定义目标显示：

- 打开 *target*
- 在显示中心绘制 `gaze_left.png`。
- 选择 textline 元素
- 在显示屏左侧某处绘制“{target_letter}”。具体坐标并不重要，因为稍后我们会用变量代替。和之前一样，大括号表示应插入 `target_letter` 变量。
- 在显示屏右侧某处绘制“X”

编辑项目脚本（选择视图 → 查看脚本）。同样，注视线索应取决于 `gaze_cue` 变量。另外，目标字母的 X 坐标应依赖于 `target_pos` 变量，而 “X” 的 X 坐标应依赖于 `dist_pos` 变量。

重要的是，我们将持续时间设置为 0。这并不意味着目标会以 0 毫秒显示。相反，这意味着实验会立即进入下一个项目，即 KEYBOARD_RESPONSE。换句话说，一旦目标显示，反应收集就马上开始！

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x="{target_pos}" y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="X" x="{dist_pos}" y=0 z_index=0
~~~

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多在 OpenSesame 脚本中使用复杂变量表达式</summary>

在 OpenSesame 脚本中，你可以用大括号包含复杂表达式。例如，对于 “X” 的位置，与其指定 `x="{dist_pos}"`，我们也可以指定 `x="{-1 * target_pos}"`。这是利用了 Python 的[格式化字符串字面量](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)。

</details>


## 步骤7：配置 keyboard_response 项目

🎯 __目标：__ 本步骤中，我们将配置参与者可以用来响应的按键，以及参与者作答的时限。

打开 *keyboard_response*：

- 将 Correct response 留空。默认将使用 `correct_response` 变量（来自第3步）。
- 将 Allowed responses 设置为 `z;m`
- 将 Timeout 设置为 `2000` 毫秒
- Event type 保持为 keypress

%--
figure:
 id: FigStep_7
 source: step7.png
 caption: |
  步骤7结束时的 KEYBOARD_RESPONSE。
--%


## 步骤8：配置 sampler

🎯 __目标：__ 本步骤我们将指定错误反馈后要播放的音频。

打开 *incorrect_sound*。点击浏览，从文件池中选择 `incorrect.ogg`。

%--
figure:
 id: FigStep_8
 source: step8.png
 caption: |
  步骤8结束时的 *incorrect_sound*。
--%


## 步骤9：配置 logger

🎯 __目标：__ 本步骤我们将回顾数据如何被记录。

打开 *logger*。默认情况下，“自动记录所有变量”是启用的。这是良好的实践，所以这里我们不需要做任何更改！

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多自定义日志记录</summary>

你还可以排除你不希望被记录的特定变量。你也可以完全禁用自动记录，并手动选择你希望被记录的特定变量。这样做有助于保持日志文件的整洁。然而，务必仔细检查所有需要的变量都被正确记录！

</details>

## 第10步：绘制反馈项目

🎯 __目标：__ 在此步骤中，我们将定义参与者在每个区块结束时收到的表现反馈。

打开 *feedback*。将持续时间保持为 'keypress'。添加以下反馈文本：

```text
区块结束

你的平均反应时间为 {avg_rt} 毫秒
你的正确率为 {acc} %

按任意键继续
```

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: |
  *feedback* 在第10步结束时的显示。
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多关于反馈变量的信息</summary>

OpenSesame 会自动跟踪反馈变量：

- `response` 是上一次反应的值。例如："z"、"left" 等。
- `correct` 在正确反应后为1，错误反应后为0
- `response_time` 是上一次反应的反应时间（以毫秒为单位）
- `acc` 是自反馈变量被重置以来的正确反应百分比，在本案例中是在区块开始时由 RESET_FEEDBACK 项目重置的
- `avg_rt` 是自反馈变量被重置以来的平均反应时间

另见：

- %link:manual/variables%

</details>

## 第11步：设置练习和实验阶段的区块数量

🎯 __目标：__ 在此步骤中，我们将为练习阶段和实验阶段指定试验区块的数量。

打开 *practice_loop*，将 Repeat 设置为2，这样我们就有两个练习区块。还要在循环表中添加一个 practice 变量，并将其设为 'yes'。这很方便，因为在数据分析时可以轻松区分哪些试验属于练习阶段。

打开 *experimental_loop*，将 Repeat 设置为8。同样，添加一个 practice 变量，但这次设置为 'no'。

## 第12步：编写 instruction、*end_of_practice* 和 *end_of_experiment* 表单

🎯 __目标：__ 在此步骤中，我们将在实验过程中添加简明的信息性指示消息。

打开三个 FORM_TEXT_DISPLAY 项，并输入简短、清晰的说明。好的说明应简洁、完整并具体！

## 第13步：运行实验！

🎯 __目标：__ 在此步骤中，我们将对实验进行第一次测试运行！

工具栏中的双蓝色箭头是快速运行（Ctrl+Shift+W）按钮。它会用一个虚拟被试编号与日志文件位置在窗口中启动实验。这主要用于开发阶段。

单绿色箭头是全屏运行（Ctrl+R）按钮。它首先会询问被试编号和日志文件，并让你选择是否全屏运行或在窗口中运行实验。这主要用于数据收集阶段。

点击这两个按钮之一，测试运行你的实验吧！

🏁 如果实验能运行，你就完成啦！但在结束之前，我们还需要回顾最后两个重要点，它们与调试和后端选择有关：

## 有效调试与理解错误

在构建实验时出现错误是正常的。请仔细阅读错误，并尝试理解它们的含义。这是实现有效调试的唯一正确方法！

%FigErrorMessage 展示了一个错误信息的示例：

- 错误类型为 `FStringError`
- 描述指出：“无法在以下文本中评估f-string表达式：`gaze_{gaze_cue}.png`”
- 错误发生在 *gaze_cue* 项目的准备阶段
- traceback 是一个 Python 错误信息。它是上述描述的技术性版本。

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: |
  OpenSesame中的一条错误信息。
--%

一旦你明白错误的来源，就可以尝试修复它。在本例中，错误出现在第6步定义 *gaze_cue* 项目时的一个拼写错误。`gaze_{gaze_ceu}.png` 应该为 `gaze_{gaze_cue}.png`。很容易修复！

<details class='info-box' markdown='1'>

<summary markdown='1'>了解更多高效调试技巧</summary>

高效调试是一项重要技能。学会它可以为你节省大量时间和避免挫败感！查看下方链接获取更多技巧：

- %link:manual/debugging%

</details>

## 时序与后端选择

在实验的“常规属性”标签页（点击实验名称后打开的标签页）中，你可以选择后端。后端是控制显示、输入设备、声音等的软件层。大多数实验适用于所有后端，但选择某一后端通常有其理由，主要与时序有关。当前有四种后端：

- __psycho__ 是默认后端。基于 PsychoPy，提供出色的时序表现 [(Peirce, 2007)][references]。
- xpyriment —— 基于 Expyriment，也提供出色的时序 [(Krause & Lindemann, 2013)][references]。
- legacy —— 作为备选方案，兼容更多系统，但时序精度较低
- osweb —— 在浏览器中运行实验 [(Mathôt & March, 2022)][references]

参见：

- %link:backends%
- %link:timing%

## 关键要点

你已经学会了如何构建一个简单但完整的实验！

- ✅ 实验结构通常通过组合 SEQUENCE 和 LOOP 项构建
- ✅ 变量通常在 LOOP 表中定义
- ✅ 对时间敏感的视觉刺激通常用 SKETCHPAD 呈现
- ✅ 受试者反馈通常用 FEEDBACK 项目呈现
- ✅ FORM_TEXT_DISPLAY 便于呈现文本
- ✅ 变量和表达式可用大括号插入。例如：`{gaze_cue}`
- ✅ Run-if 表达式在 SEQUENCE 中定义，决定哪些项目实际运行。例如：`correct == 0`
- ✅ 在采集数据前，务必通过全面测试运行验证时序和日志文件

## 后续步骤

你现在已经具备基本的 OpenSesame 知识。这足以构建许多简单实验。然而，你可能还需进一步学习！以下是合理的下一步建议：

- [学习如何与 SigmundAI 一起构建实验](%url:beginner-sigmund%)
- [学习如何在实验中使用 Python 代码](%url:intermediate%)
- [学习如何在在线实验中使用 JavaScript 代码](%url:intermediate-javascript%)

## 参考文献

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. Social Science Computer Review. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? Behavior Research Methods, 42, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. Psychonomic Bulletin & Review, 5, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. Behavior Research Methods. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. Behavior Research Methods, 44(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. Language Learning. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R.，& Giray, M. (1989)。时钟的时间分辨率：对反应时测量的影响——坏时钟的好消息。《英国数学与统计心理学杂志》，42(1)，1-12。doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about