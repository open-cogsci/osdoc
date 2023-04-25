title: 视觉世界
uptodate: false
hash: 4ac4d55fb2dfdae5994a02f5232db7371e19d2ec696b2f027b0405c5e625da78
locale: zh
language: Chinese

[TOC]

## 关于此教程

本教程假定您已经具备了 OpenSesame 的基本知识，以及部分 Python 知识。所以，如果您不熟悉 OpenSesame 或 Python, 建议您在学习本教程之前阅读初级和中级教程：

- %link:beginner%
- %link:intermediate%

在本教程中，您将学到以下内容：

- 使用 PyGaze 实现眼动追踪
- 使用 `coroutines` 并行处理
- 使用高级的 `loop` 操作


## 关于实验

在本教程中，我们将实现一个*视觉世界范式*，该范式由 Cooper (1974) 首次提出（关于此范式的综述请参阅 Huettig, Rommers 和 Meyer，2011）。在这种范式中，参与者听到一段口头表述，同时观察带有若干物体的显示屏。我们将使用四个独立的物体，分别呈现在显示屏的四个象限（%FigParadigm）。

%--
figure:
id: FigParadigm
source: visual-world-paradigm.svg
caption: >>
 示范我们的试验顺序。这是一个完全匹配试验的示例，因为目标物体（苹果）在口头表述中被直接提及。刺激来自于 [BOSS](https://sites.google.com/site/bosstimuli/) 刺激库（Brodier et al., 2010）.
%--

口头表述会提及一个或多个物体。例如，在播放 "在早餐时，女孩吃了一个苹果" 语句时，现实中可以出现一个苹果（目标物体）。在这种情况下，目标物体与句子完全匹配。句子还可以间接提及现实中的物体。例如，在播放 "在早餐时，女孩 吃了一个香蕉" 语句时，现实中可以出现一个苹果（同样是目标物体）。在这种情况下，目标物体与句子在语义上匹配，因为香蕉和苹果都是女孩早餐时可能吃的水果。

实验过程中，记录眼睛位置，并随时间测量目标物体和非目标物体的凝视比例。然后可以发现典型的结果，即参与者的眼睛会被吸引到目标物体上；也就是说，参与者会更多地看口头表述直接或间接提及的物体。引用越直接，这种效果越强。

现在让我们对实验设计进行更正式的说明。我们的实验将具有以下设计：

- 一个因素（目标匹配）有两个水平（完全匹配或语义匹配），在参与者之间变化。在完全匹配条件下，目标物体会在句子中被直接提及。在语义匹配条件下，目标物体与句子中提及的物体在语义上存在关联。
- 我们有16个口头语句和16个目标物体。每个语句和每个目标物体都会出现两次：一次在完全匹配条件下，另一次在语义匹配条件下。
- 我们有16 × 3 = 48个干扰物体，每个物体（与目标相同）会出现两次。
- 每个试验以1秒钟的注视点开始，然后呈现刺激物，1秒后开始播放口头语句。试验在5秒后结束。


## 教程


### 第1步：下载并启动 OpenSesame

OpenSesame 可用于 Windows，Linux，Mac OS（实验性）和 Android（仅运行时）。本教程为 OpenSesame 3.2.X *Kafkaesque Koffka* 版本编写。为了能够使用 PyGaze，您应该下载 Python 2.7 版本（这是默认版本）。您可以从这里下载OpenSesame：

- %link:download%

（如果您是第一次启动 OpenSesame ，您会看到一个欢迎标签页。请关闭此标签页。）启动 OpenSesame 后，将为您提供实验模板选择，以及（如果有）最近打开的实验列表（见 %FigStartUp）。点击'默认模板'以从一个几乎为空的实验开始。


%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  开启 OpenSesame 窗口。
--%


### 第2步：构建实验的主要结构

现在，为您的实验构建以下主要结构（参见 %FigMainStructure）：

1. 我们从一个说明屏幕开始。这将是一个 `sketchpad`。
2. 接下来，我们进行一个试验块。这将是一个单独的 `sequence`，对应一个单独的试验，放在一个单独的 `loop` 中，对应一个试验块。你现在可以先将试验序列留空！
3. 最后，我们以一篇告别屏幕结束。

我们还需要将实验的前景色更改为黑色，背景色更改为白色。这是因为我们将使用具有白色背景的图像，而我们不希望这些图像突出显示！

还有，别忘了给你的实验取个合理的名称，并保存它！

%--
figure:
 id: FigMainStructure
 source: main-structure.png
 caption: |
  实验的主要结构。
--%


### 第 3 步：将文件导入文件池

对于这个实验，我们需要刺激：用于口头句子的声音文件和用于物体的图像文件。从下面的链接下载它们，解压缩 `zip` 文件，并将刺激放在您的实验文件池中（参见 %FigFilePool）。

- %static:attachments/visual-world/stimuli.zip%

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  将所有刺激添加到实验后的文件池。
--%


### 第 4 步：在 block_loop 中定义实验变量

*block_loop* 是我们定义实验变量的地方，通过将它们输入到一个表格中，其中每一行对应一个试验，每一列对应一个实验变量。

现在，我们仅定义完全匹配条件，即在口头句子中直接提到目标物品（我们将作为额外任务添加语义匹配条件）。

我们需要以下变量。首先，只需将表格的行内容添加到循环表格中。

- `pic1` — 第一张图片的名称（例如 'apple.jpg'）
- `pic2` — 第二张图片的名称
- `pic3` — 第三张图片的名称
- `pic4` — 第四张图片的名称
- `pos1` — 第一张图片的位置（例如 'topleft'）
- `pos2` — 第一张图片的位置
- `pos3` — 第一张图片的位置
- `pos4` — 第一张图片的位置
- `sound` — 包含口语句子的声音文件的名称（例如 'apple.ogg'）。

目标物体将始终与 `pic1` 对应。我们有以下目标对象；也就是说，对于以下对象，我们有涉及它们的声音文件。将以下列表简单复制粘贴到表格的 `pic1` 列：

~~~
apple.jpg
armchair.jpg
banana.jpg
bear.jpg
card.jpg
cello.jpg
chicken.jpg
cookie.jpg
croissant.jpg
dice.jpg
egg.jpg
guitar.jpg
keyboard.jpg
mouse.jpg
sofa.jpg
wolf.jpg
~~~

对声音文件执行相同操作：

~~~
apple.ogg
armchair.ogg
banana.ogg
bear.ogg
card.ogg
cello.ogg
chicken.ogg
cookie.ogg
croissant.ogg
dice.ogg
egg.ogg
guitar.ogg
keyboard.ogg
mouse.ogg
sofa.ogg
wolf.ogg
~~~

其余的图片是干扰项。将以下列表复制粘贴到 `pic2`、`pic3` 和 `pic4` 列，使每列恰好有 16 行。（如果不小心使表格的长度超过 16 行，只需选择多余的行，右键单击并删除它们。）

~~~
篮球01.jpg
篮球框02.jpg
浴缸.jpg
电池02b.jpg
战斧.jpg
战舰.jpg
沙滩球拍01a.jpg
皮带03b.jpg
书架.jpg
瓶盖.jpg
碗01.jpg
拳击手套02a.jpg
箱式卡车.jpg
手链01.jpg
脑模型.jpg
砖.jpg
推土机.jpg
碰碰车.jpg
半身像.jpg
钮扣01.jpg
仙人掌.jpg
计算器01.jpg
日历.jpg
照相机01b.jpg
光盘.jpg
吊扇02.jpg
手机.jpg
连指手套04.jpg
纪念碑.jpg
月亮.jpg
快艇02.jpg
机油瓶03b.jpg
土豆先生.jpg
指甲钳03b.jpg
针鼻钳03a.jpg
床头柜.jpg
任天堂DS.jpg
禁止泊车标志.jpg
炉子.jpg
安抚奶嘴02a.jpg
油漆罐01.jpg
裤子.jpg
纸飞机.jpg
回形针02.jpg
公园喷泉.jpg
露台伞.jpg
铅笔刀03b.jpg
胡椒磨01a.jpg
~~~

现在我们需要指定位置。只需设置：

- `pos1` 为 'topleft'（左上角）
- `pos2` 为 'topright'（右上角）
- `pos3` 为 'bottomleft'（左下角）
- `pos4` 为 'bottomright' (右下角）

您的循环表现在应该看起来像%FigLoopTable。

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  在定义所有实验变量后，“循环”表的样子。
--%

### 步骤5：应用高级循环操作

尽管现在您已经定义所有实验变量，但“循环”表还没有完成！让我们看看哪里出了问题：

__位置__

`pos1` 始终在左上角，这意味着 `pic1`（目标对象）始终显示在显示区的左上角！（假设我们将实施试验顺序，以使这些位置以这种方式使用。）对于 `pos2`，`pos3` 和 `pos4` 也是如此。

我们可以通过对 `pos[x]列`进行水平洗牌来解决此问题。也就是说，对于每一行，我们随机交换这些行的值，使得：

~~~
pos1        pos2         pos3        pos4
topleft     topright     bottomleft  bottomright
topleft     topright     bottomleft  bottomright
…
~~~

变成（比如说）这样：

~~~
pos1        pos2         pos3        pos4
bottomleft  topleft      topright    bottomright
topright    bottomright  topright    bottomleft
…
~~~

要做到这一点，请查看*block_loop*的脚本，并将以下代码行添加到脚本的结尾：

~~~
shuffle_horiz pos1 pos2 pos3 pos4
~~~

然后点击“应用并关闭”。如果现在点击"预览"，您将获得一个预览，如果实验真的运行，您的循环表可能会是什么样的。您会看到 `pos[x]` 列已经水平洗牌，这意味着图片将随机显示位置！

__干扰项__

干扰图片总是与相同的目标对象链接在一起。例如，'basketball01.jpg' 总是与目标 'apple.jpg' 一起出现。但这并不是我们想要的！相反，我们希望干扰和目标之间的配对是随机的，并且对于所有参与者都不同。（除非偶然出现两名参与者之间的相同配对。）

我们可以通过垂直洗牌 `pic2`、`pic3` 和 `pic4` 列来解决这个问题。也就是说，应该单独洗牌每一列的顺序。要做到这一点，请再次查看脚本，并将以下行添加到脚本的最后：

~~~
shuffle pic2
shuffle pic3
shuffle pic4
~~~

然后点击“应用并关闭”。如果现在点击"预览"，您会看到`循环`表已经正确随机化了！

有关高级循环操作的更多信息，请参阅：

- %link:manual/structure/loop%

<div class='info-box' markdown='1'>

__问题__

在这一点上，您可能会想知道为什么我们不同时也需要水平洗牌 `pic2`，`pic3` 和 `pic4` 这些列。但我们不需要！你知道为什么吗？

</div>


### 步骤6：创建试验序列

如%FigParadigm所示，我们的试验序列很简单，包括：

- 中心固定点（一个`sketchpad`）
- 1000毫秒后：刺激显示（另一个`sketchpad`）
- 1000毫秒后：开始播放声音（一个`sampler`），而刺激显示仍然保持在屏幕上
- 5000毫秒后：试验结束

目前，试验序列是纯粹的顺序，我们可以仅使用`sequence`来实现，就像我们在其他教程中所做的那样。然而，作为额外任务之一，我们希望在试验序列*期间*分析眼睛位置；换句话说，稍后我们将需要同时进行两个操作，因此我们需要一个`coroutines`项目。 （即使我们现在还没有做任何需要这个的事情。）

所以我们希望建立以下结构：

- *trial_sequence* 应包含一个`coroutines`项目（我们称之为*trial_coroutines*）,后面跟着一个`logger`项目。
- *trial_coroutines* 的持续时间应为 7000 毫秒，并包含三个项目：
  - 显示固定点的`sketchpad`（我们称之为 *fixation_dot*）在 0 毫秒后显示
  - 显示刺激显示的`sketchpad`（我们称之为 *objects*）在 1000 毫秒后显示
  - 发出声音的`sampler`（我们称之为 *spoken_sentence* ）在 2000 毫秒后显示

您的实验结构现在应如 %FigCoroutinesStructure 所示。

%--
figure:
 id: FigCoroutinesStructure
 source: coroutines-structure.png
 caption: |
  定义试验序列后的实验结构。
--%


### 步骤 7：定义视觉刺激

__fixation_dot__

*fixation_dot* 的定义非常简单：只需在上面画一个中心固定点。

注意，您不需要指定`sketchpad`的持续时间，正如您通常需要的那样；这是因为该项目是 *trial_coroutines* 的一部分，由指示的开始和结束时间确定。


__objects__

要定义 *objects*，首先创建一个原型显示，即实验中一个特定试验可能会呈现的示例。更具体地说，画一个中心固定点，并在四个象限中的每一个中绘制任意图像，如 %FigObjectsPrototype 所示。

还为四个对象分别命名：`pic1`、`pic2`、`pic3` 和 `pic4`。我们将在额外任务中使用这些名称来执行感兴趣区域（ROI）分析。

%--
figure:
 id: FigObjectsPrototype
 source: objects-prototype.png
 caption: |
  一个原型显示，每个象限都有一个任意对象。
--%

当然，我们不希望一次又一次地展示相同的对象。相反，我们希望 `pic[x]` 变量指定显示的对象，以及 `pos[x]` 变量指定这些对象的显示位置。让我们从第一个对象开始：左上角的对象，在我的示例中是一个苹果。

查看脚本并找到与第一个对象相关的行。在我的示例中，这是以下行：
 name=pic1
~~~ .python
draw image center=1 file="apple.jpg" scale=1 show_if=always x=-256 y=-192 z_index=0
~~~

现在将 `file="apple.jpg"` 更改为 `file=[pic1]`。这将确保显示的目标图片与 `pic1`变量中指定的图片一致，而不总是显示相同的苹果。

那么我们如何使用`pos1`（值为 'topleft', 'bottomright' 等） 来指定图像的X和Y坐标呢？为此，我们利用可以在 OpenSesame 脚本中嵌入 Python 表达式的特点，即使用`[=python_expression]`表示法：

- 将 `x=-256` 改为 `x="[=-256 if 'left' in var.pos1 else 256]"`
- 将 `y=-192` 改为 `y="[=-192 if 'top' in var.pos1 else 192]"`

对其他图像执行相同的操作，直到脚本看起来像这样：

~~~ .python
绘制 fixdot color=black show_if=always style=default x=0 y=0 z_index=0
绘制 image center=1 file="[pic1]" scale=1 show_if=always x="[=-256 if 'left' in var.pos1 else 256]" y="[=-192 if 'top' in var.pos1 else 192]" z_index=0
绘制 image center=1 file="[pic2]" scale=1 show_if=always x="[=-256 if 'left' in var.pos2 else 256]" y="[=-192 if 'top' in var.pos2 else 192]" z_index=0
绘制 image center=1 file="[pic3]" scale=1 show_if=always x="[=-256 if 'left' in var.pos3 else 256]" y="[=-192 if 'top' in var.pos3 else 192]" z_index=0
绘制 image center=1 file="[pic4]" scale=1 show_if=always x="[=-256 if 'left' in var.pos4 else 256]" y="[=-192 if 'top' in var.pos4 else 192]" z_index=0
~~~


<div class='info-box' markdown='1'>

__亲自试试：`if`表达式__

如果你不熟悉 Python `if` *表达式*（与传统的 `if` *语句*略有不同），请打开调试窗口，然后输入以下行：

~~~ .python
print('This is shown if True' if True else 'This is shown if False')
~~~

你看到了什么？现在将 `if True else` 更改为 `if False else`，然后再次运行该行。你现在看到了什么？你明白逻辑了吗？

</div>


### 步骤 8：定义声音

定义声音很简单：只需打开 *spoken_sentence* 项，然后在 "Sound file" 框中输入 '[sound]'，表示变量 `sound` 指定声音文件。


### 步骤 9：添加基本眼动跟踪

使用 OpenSesame 默认安装的 [PyGaze](%url:manual/eyetracking/pygaze%) 插件进行眼动跟踪。一般程序如下：

- 在实验开始时，使用 `pygaze_init` 项*初始化并校准*眼动跟踪器。在此，您还可以指示您要使用的眼动跟踪器。 在此期间，选择高级虚拟眼动跟踪器方便您使用鼠标模拟眼球运动。
- 在每次试验之前，使用 `pygaze_drift_correct` 项执行*漂移校正*程序。在漂移校正过程中，屏幕上显示一个点，参与者看着它。 这使眼动跟踪器能够了解到眼位测量中的漂移误差有多大。误差处理方式取决于您的眼动跟踪器和设置：
  - 漂移误差用于单点校准
  - 或者进行简单检查，看漂移误差是否不超过某个最大误差，如果超过最大误差，则提供重新校准的可能性。
- 接下来，在每次试验之前，仍然使用 `pygaze_start_recording` 项告诉眼动跟踪器开始收集数据。您可以指定一个状态消息，以表示每次试验的开始。在此状态消息中包括试验编号是方便的（例如 'start_trial [count_trial_sequence]'）。
- 在每次试验结束时，使用 `pygaze_log` 项将数据发送到眼动跟踪器日志文件。 启用 “自动检测并记录所有变量” 选项是方便的。
- 最后，在每次试验结束时，使用 `pygaze_stop_recording` 项告诉眼动跟踪器停止记录。

您的实验结构现在应该如 %FigEyeTrackingStructure 所示。


%--
图片：
 id: FigEyeTrackingStructure
 source: eye-tracking-structure.png
 caption: |
  添加 PyGaze 项目进行眼动跟踪后的实验结构。
--%


### 步骤 10：定义说明和告别屏幕

到目前为止，我们还没有向 *instructions* 和 *goodbye* 项中添加任何内容。因此，在运行实验之前，请打开这些项目并添加一些文本。

### 步骤 11：运行实验！

恭喜你——你已经实现了一个视觉世界范式！现在是时候通过点击橙色播放按钮（快捷键：`Ctrl+Shift+W`）快速测试运行一下您的实验了。


## 额外任务

### 额外 1：定义语义匹配条件

到目前为止，我们只实现了完全匹配条件，即目标对象（例如“苹果”）在口头句子中被明确提及（例如“早餐时，女孩吃了一个苹果”）。

现在，请同样实现语义匹配条件，在此条件下，每个目标（例如“苹果”）与一个语义相关的口头句子配对（例如“早餐时，女孩吃了一个香蕉”）。刺激物已经创建，以便每个目标对象有一个语义相关的口头句子。

从其他方面来说，语义匹配条件应与完全匹配条件相同。

并且不要忘记创建一个表示条件的变量！

### 额外 2：使用Python常量定义坐标

目前，在 *objects* 脚本中，对象的坐标已经被硬编码，意思是坐标已经直接输入到脚本中：

~~~ .python
x="[=-256 if 'left' in var.pos1 else 256]"
~~~

在实验开始时，在 `inline_script` 中定义坐标（`XLEFT`，`XRIGHT`，`YTOP`和`YBOTTOM`）为常量，然后在 *objects* 脚本中引用这些常量，这样做更优雅。

<div class='info-box' markdown='1'>

__Python 中的常量__

在计算机科学中，*常量* 是具有不可改变的值的变量。在 Python 中，您可以始终更改变量，所以从严格意义上讲，常量在语言中不存在。但是，如果您有一个变量，将其视为一个常量（即您定义一次并且永远不要更改其值），通常是通过将变量名写为 `ALL_CAPS` 来表示。

这些命名约定在 Python 的 PEP-8 样式指南中有描述：

- <https://www.python.org/dev/peps/pep-0008/>

</div>

### 额外 3：在线分析眼位（具有挑战性！）

在*trial_coroutines*中，您可以输入生成器函数的名称（见下面对生成器的解释）。在这里，我们输入 `roi_analysis` 名称，同时在实验开始时的 `inline_script` 中创建一个定义该函数的部分。

下面是一个部分实现的 `roi_analysis()` 函数。您能完成 TODO 列表吗？

~~~ .python
def roi_analysis():

	# sample_nr 将用于为每个 500ms 样本创建不同的变量名
	sample_nr = 0
	# 此首次 yield 指示生成器已完成准备
	yield
	# 检索 objects sketchpad 的画布。我们需要在标志准备结束的 yield 语句之后执行此操作，因为这是确保画布对象已构建（这也会发生）的准备过程。
	canvas = items['objects'].canvas
	while True:
		# 我们每 500ms 只想分析一个注视样本。这样我们才不会在日志文件中产生太多列。如果没有到分析注视样本的时间，只需 yield 再继续。
		if not clock.once_in_a_while(ms=500):
			yield # 以便 coroutines 中的其他项目可以运行
			continue
		#
		# TODO:
		#
		# - 从眼动仪获取眼位坐标
		#   （提示：使用 eyetracker.sample()）
		# - 检测此坐标处的任何 sketchpad 元素（如果有的话）
		#   （提示：使用 canvas.elements_at()）
		# - 如果这些元素中包括 pic1（目标对象），请将
		#   var.on_target_[sample_nr] 设为 1，否则设为 0
		#   （提示：使用 var.set()）
~~~

另请参阅：

- %link:manual/structure/coroutines%

<div class='info-box' markdown='1'>

__Python 中的生成器函数__

在 Python 中，*生成器* 函数是带有 `yield` 语句的函数。`yield` 语句类似于 `return` 语句，因为它会停止函数。然而，“return” 永久停止一个函数，而 “yield” 仅暂停一个函数 - 而且该函数可以从“yield” 点之后继续。

</div>

## 下载实验

您可以从这里下载完整的实验：

- <https://osf.io/z27rt/>

## 参考文献

Brodeur, M. B., Dionne-Dostie, E., Montreuil, T., Lepage, M., & Op de Beeck, H. P. (2010). 标准化刺激库（BOSS）：一套新的480张认知研究中用作视觉刺激的规范物体照片。*PloS ONE*, *5*(5), e10773. doi:10.1371/journal.pone.0010773
{: .reference}

Cooper, R. M. (1974). 通过口头语言的意义来控制眼球注视：一种实时研究语言识别、记忆和语言处理的新方法。*认知心理学*, *6*(1), 84–107. doi:10.1016/0010-0285(74)90005-X
{: .reference}

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze：一个开源、跨平台的眼动实验编程工具箱。*行为研究方法*, *46*(4), 913–921. doi:10.3758/s13428-013-0422-2
{: .reference}

Huettig, F., Rommers, J., & Meyer, A. S. (2011). 使用视觉世界范例研究语言处理：一个回顾和评价。*心理学行为*, *137*(2), 151–171. doi:10.1016/j.actpsy.2010.11.003
{: .reference}

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame：一个用于社会科学的开源、图形化实验构建器。*行为研究方法*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}