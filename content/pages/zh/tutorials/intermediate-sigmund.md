title: SigmundAI 教程：视觉搜索任务
hash: 2662b1ce900715b74ee381b68acb991140b33a5656bfb23c5b7bee6cd4c44cec
locale: zh
language: Chinese

[TOC]

## 关于本教程

本教程将展示如何在 OpenSesame 中使用直接集成到 OpenSesame 界面中的 AI 副驾驶 SigmundAI，创建一个经典的视觉搜索实验。你将不必完全手动搭建实验，而是会学习如何与 Sigmund 协作来构建完整的实验结构、定义因子设计，并通过脚本逻辑实现动态刺激生成。


## 你将学到什么

在本教程结束时，你将知道如何：

- 💡 向 Sigmund 提供清晰且有效的指令
- 💡 将复杂任务拆分为简单步骤
- 💡 发现并纠正 Sigmund 的错误（是的，AI 也会犯错！）
- 💡 快速构建实验结构
- 💡 与 Sigmund 一起编写脚本
- 💡 高效地与 AI 副驾驶协作

## 将 OpenSesame 连接到 Sigmund 

Sigmund 是专为 OpenSesame 设计的 AI 助手。与 ChatGPT 这样的通用聊天机器人不同，Sigmund：

- 对 OpenSesame 了如指掌
- 直接在 OpenSesame 界面内工作
- 可以自动对你的实验进行更改

要进行连接，只需登录 [sigmundai.eu](https://sigmundai.eu)。OpenSesame 中的 Sigmund 面板将自动连接：

<video controls width ="100%"> 
    <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>
<p align="center"><em>视频 1. 将 OpenSesame 连接到 Sigmund。</em></p>


## 实验 

在本教程中，你将创建一个基础的视觉搜索实验。该实验与 [Treisman and Gelade (1980)][references] 的经典视觉搜索研究相似，但并不完全相同。

在这个实验中，参与者要搜索一个目标物体，该目标可能是黄色方形、黄色圆形、蓝色方形或蓝色圆形；目标的身份在不同试次块之间变化。参与者通过按右方向键（存在）或左方向键（不存在）来指示目标是否出现。

除了目标之外，还会呈现零个或多个干扰物体。实验有三种条件，条件决定了干扰物的类型：

- 在 *Conjunction* 条件中，干扰物可以具有任意形状和颜色，唯一的限制是干扰物不能与目标完全相同。因此，例如，如果目标是一个黄色方形，那么干扰物就是黄色圆形、蓝色圆形和蓝色方形。

- 在 *Shape Feature* 条件中，干扰物的形状与目标不同，但可以具有任意颜色。因此，例如，如果目标是一个黄色方形，那么干扰物就是黄色圆形和蓝色圆形。

- 在 *Color Feature* 条件中，干扰物可以具有任意形状，但颜色与目标不同。因此，例如，如果目标是一个黄色方形，那么干扰物就是蓝色方形和蓝色圆形。

每个试次之后都会立即显示反馈：反应正确后显示一个绿色圆点，反应错误后显示一个红色圆点。每个试次块结束后，会显示关于平均反应时和正确率的详细反馈。

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg.png
 caption: The visual-search experiment that you will implement in this tutorial.
--%


像这样的实验通常会显示出两个典型发现：

- 在 Conjunction 条件下，找到目标所需的时间比在两个 Feature 条件下更长。
- 在 Conjunction 条件下，随着干扰物数量增加，反应时也会增加。这表明人们是一次搜索一个项目来寻找目标；这称为 *serial search*。
- 在 Feature 条件中（包括形状和颜色），随着干扰物数量增加，反应时不会增加，或几乎不会增加。这表明人们会同时处理整个显示内容；这称为 *parallel search*。

根据 Treisman 和 Gelade 的特征整合理论，这些结果反映出，Conjunction 条件要求你将每个物体的颜色和形状结合起来，或者说 *bind* 起来。这种绑定需要注意，因此你需要将注意从一个物体转移到下一个物体；这个过程很慢，并解释了为什么反应时取决于物体的数量。相比之下，在 Feature 条件中，颜色和形状不需要被绑定，因此整个显示可以在一次扫描中完成处理，而不需要将注意指向每一个物体。

## Step 1: 构建主要结构  

在我们开始构建实验之前，先理解实验在 OpenSesame 中是如何组织的会很有帮助。  
在 OpenSesame 中，一个实验由一些 item 组成，这些 item 控制着什么会发生，以及以什么顺序发生。  
我们首先想要定义这个结构，这样 Sigmund 就可以在此基础上继续构建。  

我们实验的基本框架包括：

1. 主要实验 sequence —— 这包含整个实验
2. 一个放置一般说明的位置 —— 参与者在实验开始前需要说明。
3. 一个定义不同实验 block 的 loop —— loop 会将实验的一部分重复多次。在我们的例子中，每一次重复都对应一个实验 block。
4. 一个定义每个 block 内部发生什么的 sequence —— 这个 sequence 之后将包含 trial 和 block 特定的逻辑。
5. 以及最后一个结束屏幕 —— 这样参与者就知道实验何时结束。

使用这样清晰的结构能让我们和 Sigmund 都保持条理。如果我们试图让 Sigmund 一次性构建所有内容，Sigmund 就更有可能出错，而且我们也会更难发现错误并进行修复。  

所以，让我们先搭好框架，之后再补充细节！


💬 **Prompt:**

```text
Hi Sigmund! I’d like to build a visual search experiment. Please create this structure without adding content yet:

- experiment (sequence)
  - instructions (sketchpad)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_message (sketchpad)
```

当 Sigmund 完成后，概览区应当看起来像 %FigStep1： 

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area after creating the main structure.
--%


在继续之前，我们应该请 Sigmund 为实验起一个合适的名字，并移除任何不必要的 item： 


💬 **Prompt:**
```text
Please remove unnecessary default items and give the experiment a clear title.
```

%--
figure:
 id: FigStep1b
 source: step1b.png
 caption: |
  The overview area at the end of Step 1.
--%


## Step 2: 构建 block_sequence 

这个 visual search 实验是分层的。也就是说，实验包含 block，而 block 本身又包含 trial。在每个 block 中，参与者会完成多个 trial，寻找相同的目标。重要的是我们不要混淆这些层级，否则目标可能会在不同 trial 之间发生变化！ 


下一步是构建单个 block 的结构。每个 block 应当包含： 

1. 告诉参与者目标是什么的说明
2. 一个运行该 block 所有 trial 的 loop 
3. 一个 block 反馈屏幕

💬 **Prompt:**

```text
Now create the block_sequence contents. It should look like this:

- block_sequence (sequence)
  - block_instructions (sketchpad)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)
  
Just build the structure for now.
```

你的概览现在应当看起来像 %FigStep2。

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%


## Step 3: 定义 block 间变量

目标有两个特征，形状和颜色，这些特征会在区组之间变化。因此，Sigmund 需要在外层循环（experimental_loop）中定义这些特征。  
如果我们改为在试次循环内部定义这些变量，那么目标就会在每个试次都变化，而不是每个区组变化一次。

现在我们告诉 Sigmund 在 experimental_loop 中定义变量，以创建 circle/square 和 blue/yellow 的所有组合。


💬 **提示：**

```text
Please define the variables in experimental_loop so that all combinations of:

  1. target_shape (circle/square)
  2. target_color (blue/yellow)

occur equally often across blocks.
```

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The table of experimental_loop at the end of step 3."
--%


## 第 4 步：定义试次条件

在每个区组内，有三个因素会在试次之间变化：

1. 条件（conjunction / shape / color）
2. 刺激数量（1 / 5 / 15）
3. 目标是否出现。

我们希望 Sigmund 为所有组合创建试次条件，即完整析因设计。
3 个条件 x 3 个集合大小 x 2 个出现水平 = 18 种试次类型

💬 **提示：**

```text
Now define the block_loop variables. This should be a full factorial design with:

- condition: conjunction, feature_shape, feature_color
- set_size: 1, 5, 15
- target_present: present, absent

Please create all combinations.
```

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The table of block_loop at the end of step 4."
--%


## 第 5 步：构建试次序列

现在我们需要定义单个试次中会发生什么。先来创建这些项目，我们会在接下来的步骤中添加内容。
在单个试次中，我们会：

1. 显示一个注视点  
2. 显示主要搜索界面（这需要一个 Python inline_script）
3. 获取参与者的反应  
4. 记录我们需要的数据  
5. 向参与者提供反馈  


💬 **提示：**

```text
Please add items to trial_sequence in this order:

- fixation (sketchpad)
- search_display_script (inline_script)
- keyboard_response (keyboard_response)
- logger (logger)
- green_feedback (sketchpad)
- red_feedback (sketchpad)

Only create the items for now, don’t add content yet.
```

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The trial_sequence at the end of Step 5."
--%


## 第 6 步：注视显示

让我们开始添加内容吧！让 Sigmund 在 sketchpad 上画一个注视点： 

💬 **提示：**

```text
Please draw a central fixation dot in the fixation item and set its duration to 500 ms.
```

%--
figure:
 id: FigStep6
 source: step6.png
 caption: "The fixation display"
--%


## 第 7 步：生成视觉搜索界面

生成视觉搜索界面超出了 OpenSesame 图形界面所能做到的范围。我们需要动态生成刺激、随机放置，以及条件逻辑。OpenSesame 可以通过 Python（`inline_script`）或 JavaScript（`inline_javscript`）来实现这一点。在我们的例子中，我们将使用 Python。我们已经在第 5 步中向 trial_sequence 添加了一个（空的）inline_script。

但如果我们不能或不想自己编写脚本怎么办？Sigmund 可以帮我们完成！告诉 Sigmund 为我们编写所需的脚本： 

💬 **提示：**

```text
Now implement the search display using the inline script. It should:

- create a canvas
- generate random non-overlapping positions
- draw the target if present
- draw distractors based on the condition:
  - conjunction: any shape/color except target combination
  - feature_shape: shape must differ from target
  - feature_color: color must differ from target
- use the set_size variable for the number of items
- raise an error if invalid values occur

The script should show the canvas.
```

由于这个任务稍微复杂一些，Sigmund 有时会出错。不过，Sigmund 也许能自己修复这些错误！尝试运行实验，如果返回错误，就让 Sigmund 修复它。

一个常见错误的例子是，Sigmund 有时会忘记导入 Python 库，例如 `random`。如果你注意到这一点，你可以指出来并请 Sigmund 修复它！

💬 **提示词：**

```text
看起来你忘记导入 random 了。请修复它！
```

如果一切顺利，你现在就可以运行实验了（尽管它仍然不完整），并且它会显示如下界面：

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "A visual search display."
--%


## 步骤 8：定义正确反应

Sigmund 先前加入的 keyboard_response 项会根据一个名为 correct_response 的变量来检查答案。所以我们必须在收集反应之前定义什么是正确答案。我们可以让 Sigmund 用一个 inline script 来完成：

💬 **提示词：**

```text
添加逻辑，让实验知道正确反应是什么。

- 如果 target_present 存在 → correct_response 是右箭头键。
- 如果 target_present 不存在 → correct_response 是左箭头键。

请使用一个新的 inline script 来实现，并将其放在 keyboard response item 之前。
```

## 步骤 9：配置 keyboard_response

只有左箭头键和右箭头键是有效反应，因此我们要限制参与者只能使用这两个键。如果参与者在合理时间内没有作答，我们还可以让 Sigmund 在固定时间后自动进入下一试次（即 timeout）。

💬 **提示词：**

```text
请配置 keyboard response，使其满足以下条件：

- timeout 为 3000 ms
- 只允许左箭头键和右箭头键
```

## 步骤 10：创建反馈显示

接下来，我们希望让参与者知道他们是否正确识别了某个试次中 target 的存在。告诉 Sigmund 动态设置反馈 sketchpads：

💬 **提示词：**

```text
现在配置反馈 sketchpads：

- green_feedback 应显示一个绿色注视点，持续 500 ms
- red_feedback 应显示一个红色注视点，持续 500 ms

仅在正确反应后显示绿色，仅在错误反应后显示红色。
```

## 步骤 11：区组说明

参与者需要知道他们要寻找什么！让 Sigmund 制作说明屏幕，并显示当前 target 的示意图：

💬 **提示词：**

```
请在 block_instructions 中添加说明，告诉参与者要搜索哪个 target，这基于当前区组的 target shape 和 color。以视觉方式展示 target 的样子。
```

%--
figure:
 id: FigStep11
 source: step11.png
 caption: "The instruction display."
--%


## 步骤 12：区组反馈

每个区组结束后，我们会根据正确率和反应时给参与者反馈他们的表现。让 Sigmund 为我们制作这个界面：

💬 **提示词：**

```text
配置 feedback item，使其显示该区组的平均正确率和反应时。
```

%--
figure:
 id: FigStep12
 source: step12.png
 caption: "The block feedback display."
--%


## 步骤 13：结束信息

最后，我们添加一条结束信息。

💬 **提示词：**

```text
在 end_message 中设置一条实验结束信息。
```

## 完成

恭喜，实验已经完成！你可以点击蓝色双箭头按钮（快捷键：Ctrl+W）来进行一次测试运行。

下面是一个完成后的 visual-search 区组示例：

<video controls width="100%">
  <source src="/video/visual-search-demo.mp4" type="video/mp4">
</video>

<p align="center"><em>视频 2. 已完成的 visual-search 区组演示。</em></p>

为了确保实验运行良好，请检查你是否能识别以下元素：

1. 每个区组开始时都有说明，显示当前 target 的 shape 和 color
2. 每个试次都有一个注视点，并且每个试次后都会立即显示正确的反馈
3. 在各个试次中，set size 和 target presence 会发生变化
4. 每个区组结束后都有一个表现总结

如果你注意到一些小的 bug 或错误——别担心。Sigmund 通常可以自己修复这些。试着运行实验，如果出现错误，只需向 Sigmund 描述问题并让他修复即可。例如，当你指出时，Sigmund 通常可以修复缺失的 imports、不正确的变量名，或小的逻辑错误。学会测试你的实验，并以迭代的方式请求 Sigmund 进行有针对性的修复，是高效使用 AI copilot 工作的重要一环。

## References

<div class='reference' markdown='1'>
Treisman, A. M., & Gelade, G. (1980). 注意的特征整合理论。*Cognitive Psychology*, *12*(1), 97–136. doi:10.1016/0010-0285(80)90005-5
</div>

[references]: #references