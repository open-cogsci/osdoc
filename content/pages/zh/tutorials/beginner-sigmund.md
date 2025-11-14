title: SigmundAI 教程：注视线索
hash: 80f0a9ae4381f62b46aa6b1cca4b807990e8235070ac5187f47bc98a6f028d00
locale: zh
language: Chinese

## 关于本教程

在本教程中，你将通过与 SigmundAI（你的 OpenSesame AI 助手）合作，构建一个心理学实验。你将学会如何向 Sigmund 提供清晰的指令、发现并修正错误，以及以前所未有的速度构建实验。

我们将创建一个经典的凝视提示（gaze-cuing）实验。这是一个有趣的实验范式，人们会不由自主地跟随一张脸的视线方向。

本教程是在[初学者教程](%url:beginner%)基础上进行的，实验内容相同，但会演示如何借助 AI 共同完成。

## 你将学到什么

完成本教程后，你将掌握以下技能：

- 💡 向 Sigmund 提供清晰、有效的指令
- 💡 将复杂任务拆解为简单步骤
- 💡 发现和纠正 Sigmund 的错误（没错，AI 也会犯错！）
- 💡 快速搭建实验结构
- 💡 高效地与 AI 协作

## 你需要的准备

**OpenSesame 4.1 或更高版本**，并已安装所有更新。如果你看到有可用更新的通知，请点击“安装更新...”然后点击“运行更新脚本”。更新后重启 OpenSesame。你也可以在 OpenSesame 控制台手动执行以下命令来更新。

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**OpenSesame 基础知识。** 如果你是新手，请首先学习[初学者教程](%url:beginner%)。理解基础知识将帮助你更有效地与 Sigmund 协作。AI 很强大，但无法替代对原理的理解。

**SigmundAI 订阅。** 你需要一个在 [sigmundai.eu](https://sigmundai.eu/) 的有效订阅。

## 将 OpenSesame 连接到 Sigmund

Sigmund 是专为 OpenSesame 设计的 AI 助手。与 ChatGPT 这类通用聊天机器人不同，Sigmund：

- 充分了解 OpenSesame 的细节
- 直接在 OpenSesame 界面内工作
- 能自动对你的实验做出更改

只需登录 [sigmundai.eu](https://sigmundai.eu/)，OpenSesame 内的 Sigmund 面板会自动连接：

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>

## 实验简介

如前所述，我们将创建一个最初由 [Friesen 和 Kingstone (1998)][references] 开发的凝视提示实验。具体流程如下：

1. 屏幕中央出现一张人脸
2. 人脸的视线向左或向右
3. 目标字母（‘F’或‘H’）在一侧出现
4. 干扰字母（‘X’）在另一侧出现
5. 参与者尽快识别目标字母

有趣的发现是：当脸的视线朝向目标时，人们反应更快，尽管视线方向无法预测目标出现的位置。这表明人类会自动关注他人的视线方向。

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  凝视提示实验范式 [(Friesen and Kingstone, 1998)][references]。此示例展示了一个**不一致**试次，因为人脸的视线看向干扰项（‘X’），而不是目标（‘F’）。
--%

## 步骤 1：创建主序列

让我们从搭建基本结构开始。实验包含两个阶段：练习阶段和实验阶段。每个阶段都需要在开始前显示说明，在结束后显示提示信息。明确的结构有助于你和 Sigmund 保持条理。

与 Sigmund 沟通时，要具体说明！明确告诉 Sigmund 你想要什么，也要说明你*暂时不需要*什么，这样可以防止 Sigmund 一次性做太多操作。

💬 **对话示例：**

```text
Hi Sigmund! I'd like to build a gaze-cuing experiment together. Let's start with the basic structure:

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

- 一张面部图像，表现为中性、左看和右看
- 参与者出错时播放的声音

Sigmund 无法为你下载文件，因此你需要手动完成这一步。请下载以下文件并将它们拖入你的 file pool：

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

file pool 应该如 %FigStep4 所示。

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## 第5步：构建 trial_sequence

现在是时候创建单个试次的结构了。每个试次会发生以下流程：

1. 显示注视点（准备好！）
2. 显示中性面部（即将出现面孔）
3. 显示凝视线索（面部向左或向右看）
4. 显示目标和干扰项（该作答啦！）
5. 收集键盘反应
6. 播放错误提示音（只在作答错误时）
7. 记录数据

错误提示音只应在错误试次播放。这需要用到 run-if 表达式：一条决定某项何时运行的条件语句。

💬 **提示：**

```text
让我们把如下项目加入 trial_sequence：

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — 只在作答错误后播放
- logger (logger)

现在只需新建这些项目，无需填写内容。可以做到吗？
```

此任务需要多个操作，Sigmund 有时会出错。一定要仔细检查他的工作。

Sigmund 在此阶段常见的错误：

- 忘记创建某些项目
- 忘记为 *incorrect_sound* 添加 run-if 表达式

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%

如果 Sigmund 出错（例如遗漏了 logger 或 run-if 表达式），请温和地用具体的指令提醒他：

💬 **提示**（根据缺失内容调整）：

```text
我注意到 logger 缺失了，可以补上吗？

随后，请选择 trial_sequence，并为 incorrect_sound sampler 添加 run-if 表达式。记得，run-if 表达式需要在包含此项目的 sequence 里设置，而不是项目本身。
```

为什么 Sigmund 会出错？AI 难以预测，任何任务都可能出错。但 Sigmund 在多步骤任务上尤其容易犯错。上面的任务一共需要9项独立操作！当你布置复杂任务时，一定要仔细检查结果。

你的 *trial_sequence* 应如 %FigStep5 所示。

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## 第6步：绘制显示项目

现在开始有趣的部分：创建参与者将看到的内容！我们会逐一制作每个显示界面。

首先，设置颜色并绘制初始注视点。凝视刺激使用白色背景，因此我们需要白底配黑色元素。

💬 **提示：**

```text
请将实验设置修改为黑色刺激配白色背景。然后在 fixation_dot 项中添加注视点，并将其显示时长设为 745 毫秒。
```

接着是中性面孔显示：

💬 **提示：**

```text
很好！现在加入中性凝视图片，显示时长设为 745 毫秒。
```

Sigmund 应该能想到使用 file pool 中的 *gaze_neutral.png* 文件。记得查看 sketchpad 确认！

接下来是凝视线索显示（面部方向）：

💬 **提示：**

```text
完美！现在添加凝视线索界面，显示时长为 495 毫秒。
```

Sigmund 应该用 `gaze_cue` 变量，显示 *gaze_left.png* 或 *gaze_right.png*。

最后，是目标显示（最复杂的一项）：

💬 **提示：**


```text
非常好！现在创建目标显示界面。它应显示：

- 注视线索（面部仍注视）
- 左侧或右侧的目标字母（取决于 target_pos）
- 另一侧显示一个‘X’
```

时长应设为 0，因为接下来要用 *keyboard_response* 项等待输入。请确认 Sigmund 是否已正确完成！


## 步骤 7：配置键盘响应

现在我们需要收集被试的答案。

💬 **提示：**

```text
请将 keyboard_response 配置为 2000 毫秒超时。只接受正确的响应按键（z 和 m）。
```


## 步骤 8：设置错误声音

当被试犯错时，应听到反馈声音。

💬 **提示：**

```text
现在配置 incorrect_sound sampler 播放错误提示音文件。
```


## 步骤 9：创建反馈界面

每个区块后，被试应能看到自己的表现如何。

💬 **提示：**

```text
在 feedback 项中添加反馈，显示该区块的平均准确率和反应时。
```


## 步骤 10：设置区块重复次数

现在我们需要指定每个区块重复的次数。

💬 **提示：**

```text
将练习阶段设置为 2 个区块，正式实验阶段设置为 8 个区块。并创建一个 'practice' 变量（是或否），以便我们能在数据中区分练习和正式实验试次。
```


## 步骤 11：编写说明页面

被试需要知道实验流程！让 Sigmund 编写简明清晰的实验说明。

💬 **提示：**

```text
请为实验编写清晰简洁的说明，并编写练习结束和实验结束时的友好提示。内容可自行斟酌！
```

仔细阅读说明。它们是否通顺、清晰？如有需要，可让 Sigmund 进行修改！


## 步骤 12：测试和调试！

重要时刻到了。让我们运行实验！点击蓝色快速运行按钮，看看会发生什么。你可能会遇到错误！这很正常。比如可能出现如下错误：

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "An error appears. Don't panic!"
--%

发生了什么？练习结束那个项在 acc 变量尚未生成时就尝试显示它。这是因为 OpenSesame 的 prepare-run 阶段机制：项会提前准备，有时此时变量还没被定义。

Sigmund 通常能修复此类问题。错误弹出时只需点击 “Ask Sigmund to fix this”。修复后再次尝试运行实验。如有必要，重复此过程。

完成！恭喜你，与 Sigmund 一起完成了整个实验的构建！

💬 **最终提示：**

```text
谢谢你，Sigmund！做得很棒！
```


## 关键要点

你已经学会如何高效与 AI 副驾驶协作啦！主要经验包括：

- ✅ **提示要具体、清楚**。
- ✅ **将复杂任务拆解为简单步骤**，不要一次要求太多。
- ✅ **始终检查 Sigmund 的成果**，AI 也会犯错！
- ✅ **出现问题要积极追问**。
- ✅ **要有耐心**，调试是实验流程的一部分。

多练习后，你和 Sigmund 将成为黄金搭档！🤝


## 参考文献

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references