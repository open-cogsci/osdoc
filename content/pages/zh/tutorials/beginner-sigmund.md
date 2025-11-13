title: SigmundAI 教程：注视线索
hash: d5304ea6608e83e51e1a0e01bbc9e8efc6602bc92944fcf1444d2848f9e097fe
locale: zh
language: Chinese

## 关于本教程

在本教程中，你将与 SigmundAI（你在 OpenSesame 上的 AI 副驾驶）一起协作，构建一个心理学实验。你将学会如何向 Sigmund 提出清晰的指令，发现并修正错误，并比以往更高效地搭建实验。

我们要制作一个经典的凝视线索（gaze-cuing）实验。这是一个有趣且引人入胜的实验范式，在这种实验中，人们会不由自主地跟随面孔注视的方向。

本教程是在[初学者教程](%url:beginner%)基础上升级的，使用相同的实验，但教你如何借助 AI 助手来完成。

## 你将学到什么

完成本教程后，你将能够：

- ✅ 向 Sigmund 提供清晰、有效的指令
- ✅ 将复杂任务拆分为简单步骤
- ✅ 发现并纠正 Sigmund 的错误（没错，AI 也会出错！）
- ✅ 快速搭建实验结构
- ✅ 高效地与 AI 副驾驶协同工作

## 你需要什么

**OpenSesame 4.1 或更高版本**，并安装了所有更新。如果你看到有可用更新的通知，请点击“安装更新…”然后点击“运行更新脚本”。更新后请重启 OpenSesame。你也可以手动在 OpenSesame 控制台运行以下命令进行更新。

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**OpenSesame 基础知识。** 第一次接触 OpenSesame？请先阅读[初学者教程](%url:beginner%)。理解基础知识会帮助你更好地与 Sigmund 协作。AI 很强大，但无法替代你对原理的理解。

**SigmundAI 订阅。** 你需要一个有效的订阅，可在 [sigmundai.eu](https://sigmundai.eu/) 获取。

## 连接 OpenSesame 与 Sigmund

Sigmund 是专为 OpenSesame 设计的 AI 助手。与 ChatGPT 等通用聊天机器人不同，Sigmund：

- 熟悉 OpenSesame
- 直接在 OpenSesame 界面工作
- 可以自动修改你的实验

只需登录 [sigmundai.eu](https://sigmundai.eu/)，OpenSesame 中的 Sigmund 面板会自动连接：

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>

## 实验介绍

如前所述，我们将制作凝视线索实验，该实验最初由 [Friesen 和 Kingstone (1998)][references] 开发。流程如下：

1. 一张面孔出现在屏幕中央
2. 面孔向左或向右看
3. 一个目标字母（'F' 或 'H'）出现在一侧
4. 一个干扰字母（'X'）出现在另一侧
5. 参与者尽快识别目标字母

有趣的发现是什么？当面孔看向目标时，人们的反应速度更快，即使面孔的注视方向并不能预测目标出现在哪里。这说明人类会自动地跟随他人的目光。

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  凝视线索实验范式 [(Friesen and Kingstone, 1998)][references]。该例为**不一致**试次，因为面孔看向了干扰项（'X'）而不是目标（'F'）。
--%

## 步骤 1：创建主序列

我们先搭建基本结构。实验分为两个阶段：练习和正式实验。每个阶段在开始前需要有说明，在结束后需要有提示信息。从清晰的结构开始，有助于你和 Sigmund 都保持条理。

与 Sigmund 沟通时要具体！准确告诉他你的需求，也说明*暂时不需要*哪些内容。这样可以避免 Sigmund 一次性做得太多。

💬 **提示语：**

```text
Hi Sigmund! 我想一起搭建一个凝视线索实验。让我们从基础结构开始：

- experiment (sequence)
  - instructions (form_text_display)
  - practice_loop (loop)
    - block_sequence (sequence)
  - end_of_practice (form_text_display)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_of_experiment (form_text_display)
```

请创建这个结构，但暂时不要向各项中添加内容。我们会一步步进行！

完成 Sigmund 创建此结构后，让我们整理一下。请在单独的对话中提出，以避免让 Sigmund 一次承担太多任务。

💬 **提示：**

```text
很好！现在请移除我们不需要的项目，并为实验命名一个清晰的标题。
```

你的概览区域应该看起来像 %FigStep1。（你的实验标题可能略有不同，这没关系！）

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of Step 1.
--%

<div class='info-box' markdown='1'>

**💡 控制好 Sigmund！**

在 Sigmund 面板底部，你可以选择是否在 Sigmund 执行操作前进行审核。当开启时，你需要批准 Sigmund 的每个更改。

- **用于学习：** 请保持开启。你会了解 Sigmund 在做什么。
- **追求速度：** 当你熟悉之后可以关闭。

请记住，Sigmund 也会出错！尤其在开始时，请务必仔细检查结果。

</div>

## 步骤2：创建 block_sequence

现在让我们构建每个试次区块（block）中发生的流程。每个区块遵循如下模式：

1. 重置反馈（这样上一区块的表现不会影响到本区块的反馈）
2. 运行试次循环
3. 展示表现反馈

练习阶段和实验阶段都使用相同的 *block_sequence* 项。这称为链接副本。你更改其中之一，另一个也会相应改变。当一个实验过程在多个位置重复时（如一组试次），使用链接副本会很方便。

💬 **提示：**

```text
很好！现在让我们为 block_sequence 添加内容。它应在练习与实验阶段中共享（即链接副本）。结构如下：

- block_sequence (sequence)
  - reset_feedback (reset_feedback)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)

同样，仅需创建结构。内容稍后再加。准备好了吗？开始吧！
```

你的概览现在应该像 %FigStep2。

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## 步骤3：定义试次条件

每个实验都有自变量。这些是你要操控的变量。在我们的实验中，我们变化：

- 脸部望向的方向（左或右）
- 目标出现的位置（左 -300 或右 300）
- 目标字母（F 或 H）

我们还需计算：

- 干扰项的位置（与目标相反一侧）
- 正确反应按键（目标为 F 时按 z，目标为 H 时按 m）

因此，这是一个 2 × 2 × 2 设计，共有8种试次类型。

向 Sigmund 解释设计能帮助它理解逻辑，从而创建所有正确的组合。

💬 **提示：**

```text
现在让我们在 block_loop 里定义变量。这是一个 2 × 2 × 2 设计（共8行）：

- gaze_cue: left 或 right
- target_pos: -300 或 300（x坐标，负=左，0=中心）
- target_letter: F 或 H
- dist_pos: 与 target_pos 相反的一侧
- correct_response: 若 target_letter 为 F，则为 z；若为 H，则为 m

可以创建这个吗？谢谢！
```

你的 *block_loop* 现在应如 %FigStep3 所示，8行显示所有可能组合。

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

**🤖 选择适合你的 AI 模型！**

Sigmund 不是单一 AI，而是一个可调用多种模型的聊天机器人。在 [sigmundai.eu](https://sigmundai.eu) 上你可以选择不同模型。

本教程已用 **Claude Sonnet 4.5** 和 **GPT-5** 对话模式进行测试。

提示：

- 不同模型有各自优势。可多试几种，找到你最喜欢的。
- 专注问题解决的模型通常更慢，普通任务未必更优。

</div>

## 步骤4：将图片和声音添加到文件池

我们需要一些用于刺激的文件：

- 一张面部表情为中性、向左看、向右看的图片
- 当被试做出错误反应时播放的声音

Sigmund 无法为你下载文件，所以你需要手动完成这一步。请下载下列文件并拖入文件池：

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

file pool 应该看起来像 %FigStep4。

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## 第5步：构建trial序列

现在开始创建单个trial的结构。每个trial会发生以下事件：

1. 显示注视点（准备好！）
2. 显示中性面孔（面孔出现咯）
3. 显示凝视线索（面孔朝左或朝右看）
4. 显示目标和干扰项（需要做出反应了！）
5. 收集键盘反应
6. 播放错误音效（仅在错误反应时播放）
7. 记录数据

错误音效应该只在错误trial上播放。这需要用到run-if表达式：条件表达式决定某个项目是否执行。

💬 **提示：**

```text
Let's add items to the trial_sequence:

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — only play after an incorrect response
- logger (logger)

Just create the items for now, don't add content yet. Can you do that?
```

这个任务需要执行很多步骤，Sigmund 有时会弄错。一定要仔细检查他的工作。

**Sigmund在这里常见的错误：**

- 忘记创建某些项目
- 忘记为*incorrect_sound*添加run-if表达式

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%

如果Sigmund出现了失误（比如遗漏了logger或者run-if表达式），给他一个温和、具体的提醒：

💬 **提示**（根据缺失项调整）：

```text
I notice the logger is missing. Could you add it please? 

And then, could you select the trial_sequence and add a run-if expression for the incorrect_sound sampler? Remember, run-if expressions are set in the sequence that contains the item, not in the item itself.
```

为什么Sigmund会出错？AI不可预测，任何任务都可能出现错误。然而，Sigmund在处理多步任务时尤其容易出错。上面的任务就需要9个独立的操作！当你要求执行复杂任务时，一定要仔细检查结果。

你的*trial_sequence*应该看起来像%FigStep5。

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## 第6步：绘制显示项目

现在进入有趣的部分：创建被试将会看到的显示内容！我们将逐个完成每个显示项目。

首先，设置颜色并绘制初始注视点。我们的凝视刺激使用白色背景，所以需要白底黑字元素。

💬 **提示：**

```text
Could you change the experiment settings to use black stimuli on a white background? Then add a fixation dot to the fixation_dot item and set its duration to 745 ms.
```

接下来是中性面孔的显示：

💬 **提示：**

```text
Great! Now add the neutral gaze image. Duration should be 745 ms.
```

Sigmund 应该能想到使用文件池中的*gaze_neutral.png*。请查看sketchpad以确认！

然后是凝视线索（面部注视方向）：

💬 **提示：**

```text
Perfect! Now add the gaze cue display. It should show for 495 ms.
```

Sigmund 应该用`gaze_cue`变量来显示*gaze_left.png*或者*gaze_right.png*。

最后是目标显示（最复杂的一个）：

💬 **提示：**

```text
太棒了！现在创建目标显示界面。它应显示：

- 注视线索（面孔仍在注视）
- 左侧或右侧的目标字母（根据 target_pos 决定）
- 对侧显示一个“X”
```

时长应设置为0，因为接下来的 *keyboard_response* 项会等待输入。请核实 Sigmund 是否正确完成此项！


## 步骤7：配置键盘响应

现在我们需要收集参与者的反应。

💬 **提示：**

```text
请将键盘响应项设置为2000毫秒超时。只接受正确的响应按键（z 和 m）。
```


## 步骤8：设置错误提示音

当参与者出错时，应听到反馈声音。

💬 **提示：**

```text
现在将 incorrect_sound sampler 配置为播放错误音频文件。
```


## 步骤9：创建反馈显示界面

每个区块后，参与者应看到他们的表现。

💬 **提示：**

```text
在 feedback 项中添加反馈，显示本区块的平均正确率和反应时。
```


## 步骤10：设置区块重复次数

现在需要指定每个区块的重复次数。

💬 **提示：**

```text
将练习阶段设为2个区块，正式实验阶段设为8个区块。同时创建一个 'practice' 变量（yes 或 no），以便在数据中区分练习和正式实验试次。
```


## 步骤11：编写操作说明界面

参与者需要知道实验流程！让 Sigmund 写下清晰的操作说明。

💬 **提示：**

```text
请为本实验撰写清晰简明的说明，并在练习结束与实验结束时显示提示信息。内容请自行判断！
```

仔细阅读这些说明。它们是否有道理？是否清晰？如有需要，可要求 Sigmund 进行修改！


## 步骤12：测试与调试！

终于到了关键时刻。运行实验吧！点击蓝色的快速运行按钮，看看会发生什么。你可能会遇到一个错误！这很正常。比如可能出现以下错误：

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "An error appears. Don't panic!"
--%

出什么问题了？练习结束项尝试显示 `acc` 变量，而该变量此时还没有定义。这是因为 OpenSesame 的准备-运行阶段机制：项目会预先准备，但有时此时变量还未被定义。

Sigmund 通常可以解决此类问题。在出现错误时，点击 “让 Sigmund 修复此项” 按钮。错误修复后，再次运行实验。如有必要，反复进行。

完成！恭喜你。你和 Sigmund 一起构建了一个完整的实验！

💬 **最终提示：**

```text
谢谢你，Sigmund！干得漂亮！
```


## 关键要点总结

你已经学会了如何高效地与AI协作者合作！主要经验如下：

1. **在提示中要具体且清晰。**
2. **将复杂任务拆分为简单步骤。** 不要一次要求太多。
3. **始终检查 Sigmund 的工作。** AI 也会出错！
4. **当发现问题时，提出后续问题。**
5. **保持耐心。** 调试是流程的一部分。

多加练习，你和 Sigmund 会成为优秀的团队！🤝


## 参考文献

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references