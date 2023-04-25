title: 内隐联结任务
uptodate: false
hash: d71135886d1eab5c8ea213f440c31193dc6e9c150ad7be41af10263195d05180
locale: zh
language: Chinese

## 内隐联结任务

内隐联结任务衡量了概念（例如年轻人和老年人）之间的关联和评价（例如好和坏）。其思路是，当相关项目共享相同的反应键时，进行反应会更容易（因此*更快*）。

在这里，我们将衡量年轻人和老年人，好与坏之间的关联。我们假设年轻的参与者（潜意识里）将积极的词与年轻的面孔联系在一起，而不是将其与老年面孔联系在一起。

## 教程录屏

此教程也提供了一个录屏：

%--
video:
 source: youtube
 id: Screencast
 videoid: zd-nxgGOGlE
 width: 640
 height: 360
 caption: |
  IAT教程的录屏。
--%


## 实验层次结构

为了测试这个预测，参与者需要完成四个试验块（%Task）。

- __第一块__ - 参与者将*词汇*分类为*积极*或*消极*。分类名称显示在屏幕的左上角和右上角，参与者用左手或右手按一个按钮来表示中央显示的词属于哪个类别
- __第二块__ - 参与者将*面孔*分类为*老年*或*年轻*，同样是通过左手或右手进行回应
- __第三块__ - 是第一块和第二块的结合。在这个例子中，*积极*和*年轻*这两个词出现在左上方，而*消极*和*老年*这两个词出现在右上方。因为我们假设（年轻的）参与者对年轻脸孔有更积极的态度，所以我们称这种映射为*一致的*
- __第四块__ - 同样是第一块和第二块的结合，但这次映射是*不一致的*

%--
figure:
 id: Task
 source: IAT-task.png
 caption: |
  内隐联结任务的四个试验块概述。
--%

## 预测

我们预测参与者对年轻人的偏好大于对老年人的偏好，因此当年轻和积极共享一个反应键，老年和消极共享一个反应键时，对词汇的分类会更容易（与相反的映射相比）。这应该导致在一致的块中的反应速度比在不一致的块中更快（%Prediction）。

%--
figure:
 id: Prediction
 source: prediction.png
 caption: |
  我们预测参与者在组合*积极/年轻*和*消极/老年*类别时更容易对词汇和面孔进行分类（与相反的类别组合相比）。
--%


## 试验顺序

为了测试这个预测，我们将创建以下试验顺序（%TrialSequence）：

- 每个试验开始时有一个 __固定点__（500毫秒）
- 接下来，__两个类别名称__ 出现在屏幕的左上角和右上角。
- 待分类的 __刺激__ 出现在中央
- 参与者通过 __按键__ 表示刺激属于左侧类别还是右侧类别
- 记录当前试验的 __变量__

%--
figure:
 id: TrialSequence
 source: trial_sequence.png
 caption: |
  IAT （第一个试验块的）典型试验顺序的示意表示。
--%

## 启动 OpenSesame

启动 OpenSesame 时，您会看到一个“入门！”选项卡，其中显示了模板列表以及最近打开的实验（%GetStarted）。为了节省时间，我们将使用"扩展模板"。

%--
figure:
 id: GetStarted
 source: get-started.png
 caption: |
  OpenSesame的欢迎窗口。在这里，我们将使用“扩展模板”。
--%

打开扩展模板后，我们将保存我们的实验。要做到这一点，点击 *文件* -> *保存*（快捷键：`Ctrl+S`），浏览到适当的文件夹并为您的实验起一个有意义的名字。

## 概览区域

*概览区域* 显示了我们实验的层次结构。为了简化我们的结构，在删除实践模块之后，我们开始。为此，执行以下操作：

- 在名为*practice loop*的项目上右键单击
- 单击"删除" (快捷键： `Del`)
- 对*end_of_practice*项目执行相同操作

现在您的实验概览区域应该是这样的：

%--
图示:
 id: Overview
 source: overview.png
 caption: |
  您的实验概览区域.
--%

## 第一部分：词汇分类

### 步骤1：修改块循环

首先，我们创建IAT的第一部分（％Task中的Block 1），在其中参与者必须将词汇分类为正面或负面。 因为我们会创建多个任务块，因此*block_loop*名称并不是很有说明性。 所以我们重命名它：

- 在*block_loop*项目上右键单击，选择重命名（快捷键：`F2`），并将其命名为*words_block_loop*

接下来，我们希望在*block_loop item*中定义以下三个变量：

- __stimulus__ -- 待分类词汇
- __category__ -- 词汇所属的类别
- __correct_response__ -- 参与者应给出的反应

要创建这些变量：

- 通过在概览区域中单击它来打开*words_block_loop*的选项卡
- 最初你会看到一个空表格
- 双击第一列的表头（最初称为 "empty_column"）并将其命名为 "stimulus"
- 用每行一个的形式填充包含六个正面和六个负面词汇的第一列
- 创建一个包含 "category" 表头的第二列，然后标示每个刺激属于哪个类别（*POSITIVE* 或 *NEGATIVE*）
- 创建第三列，将其命名为 *correct_response*，并为每个刺激指示正确的反应
- 要确定响应规则，我们可以说：
    - 单词 *POSITIVE* 将显示在屏幕的左侧，而单词 *NEGATIVE* 将显示在右侧
    - 为了表示一个词汇属于左侧，参与者必须按 'e'，而对于右侧，他们必须按 'i'。

<div class='info-box' markdown='1'>

__提示__ -- *correct_response*是一个内置变量，允许 OpenSesame 跟踪参与者的表现，如 'acc'（准确度或正确百分比）。

</div>

您的*words_block_loop*的内容现在应该如下所示：

%--
figure:
 id: Overview
 source: words_block_loop.png
 caption: |
  IAT的第一个块循环表包含三个实验变量及其值。
--%

### 步骤 2：修改试验序列

如％TrialSequence所示，在每次试验中，我们要：

1. 显示一个注视点
2. 在屏幕中心显示刺激，并在屏幕的上方两侧显示两个类别
3. 收集按键响应
4. 将变量保存到输出文件

这四个步骤被称为 *events*，我们将通过在*试验序列*中使用*items*来实现这些步骤。但首先，因为实验的每一部分序列都略有不同（见％Task），让我们将其重命名为*words_trial_sequence*。

对于前两个事件，我们将使用`sketchpad`项目。 高级模板已经包含一个sketchpad项目。 若要添加第二个项目：

- 从*项目工具栏*中抓取一个`sketchpad`项目
- 将其拖放到*words_trial_sequence*中

%--
视频:
 source: youtube
 id: DragDrop
 videoid: vvJewWTjlts
 width: 640
 height: 360
 caption: |
  拖放项目.
--%


<div class='info-box' markdown='1'>

__提示__ -- 若要使一个项目出现在另一个项目的*后面*，请将其拖放到这个其他项目*上*。

</div>



默认情况下，OpenSesame会为项目赋予诸如 *sketchpad*，*new_sketchpad* 和 *new_sketchpad_1* 之类的名称。因为这些名称没有说明性，我们将项目重命名为更有意义的名称。要执行此操作：

- 在概览区域的项目上右键单击（快捷键：`F2`）
- 选择"重命名"
- 分别将两个`sketchpad`项目命名为 *fixation* 和 *word*

试验序列的最后两个事件（收集响应和保存数据）已经分别由`keyboard_response`项目和`logger`项目表示。

现在，您的概览区域应该是这样的：

%--
图片：
 id: OverviewWordBlock
 source: overview_words_block.png
 caption: |
  实验（第一部分）的新概览。
--%


### 步骤3：修改试验序列中的项目

#### 定位

下一步是向试验序列中的项目添加内容。我们从表示试验开始时定位点的`sketchpad`开始。

- 通过在概览区域中点击它来打开*定位*标签页。因为我们选择了“扩展模板”，OpenSesame已经为我们创建了一个定位点。我们需要更改的唯一事物是定位点在屏幕上保持的时间
- 点击“持续时间”框，将其值更改为500


#### 文字

__绘制类别名称__

定位点消失后，我们希望在显示器的左上角和右上角显示两个类别名称（请参阅%TrialSequence）。为此，

- 通过在概览区域中点击它来打开*文字*标签页
- 从黑白工具栏中选择“绘制文本线”元素
- 点击描画台左上四分之一处的某个地方
- 输入“积极”
- 重复此过程在相反的位置显示字符“消极”

__绘制刺激物__

接下来，我们要在屏幕中央显示待分类刺激。重要的是，刺激是 _*可变的*_。这意味着显示哪个单词取决于*words_block_loop*当前执行的哪一行。为了让OpenSesame知道它可以在块循环中找到单词变量的值，我们使用*方括号语法*。这样做：

- 选择`绘制文本线`描画台元素
- 点击屏幕的中心
- 输入：

~~~ .python
[stimulus]
~~~


<div class='info-box' markdown='1'>

__提示__ - 您在方括号之间输入的单词应该与在*word_block_loop*中创建的列标题完全相符。

</div>

这种方法非常方便，因为它避免了为每个积极和消极词各自制作单独的描画板。

__更改持续时间__

最后，我们将当前描画板的持续时间更改为0。这并不意味着当前描画板仅显示0毫秒。相反，由于`keyboard_response`项目紧随其后，它将一直显示在屏幕上，直到参与者按下某个键。

您的描画板现在应如下所示：

%--
图像：
 id: SketchpadWord
 source: sketchpad-word.png
 caption: |
  用于将类别名称和刺激显示在显示器上的`sketchpad`项目。
--%


经常尝试运行实验是一个好习惯，这样您可以立即调试。现在，通过按三个“运行”箭头之一进行测试运行。

<div class='info-box' markdown='1'>

__提示__ - 如果您想要对实验进行快速测试运行，您可能不必从给定的实验中运行所有项目。要缩短试验次数，您可以执行以下操作：

- 打开您的实验循环表格
- 将“重复”框中的值更改为小于1,00的值（例如0,1）
- （在某些系统上，小数点用逗号而不是句点表示）
- 在我们的示例中，这意味着OpenSesame将只运行*一*行（随机选择的），而不是运行全部12行
- 测试完成后，请不要忘记将“重复”还原为1,00

</div>


## 实验层次结构

IAT的区块比当前的区块要多。它还包含一个区块，其中需要把面部图片归类为年轻或者年老，还有两个区块包含了这两种任务的交织（见%任务）。这意味着我们需要创建另外三个试验区块，每个区块都有它们自己的试验序列。因此，实验的层级结构如下（当我们完成编程时，我们的概览区域应该呈现出这个结构）：

%--
figure:
 id: Hierarchy
 source: hierarchy.png
 caption: |
  IAT的实验层次。
--%

## Block 2：面部分类

我们首先要关注面部分类任务。更准确地说，我们将

- 创建一个额外的区块循环和试验序列
- 重用之前实验部分可以重用的所有内容
- 添加针对面部分类任务的新变量和事件

### 步骤 4：创建一个额外的 block_loop

- 从项目工具栏中找到一个`loop`元素
- 将它拖放到概览区域
- 为了让新的区块出现在第一个区块后面，将其放置在`words_block_loop`项目*之上*（参见%AppendLoopAndSequence）
- OpenSesame 会询问你是否希望将当前项目插入到`words_block_loop`中，还是在其后面。选择后者。

<div class='info-box' markdown='1'>

__提示__-- 如果你不小心把新项目放入 block loop *内*，可以按`Ctrl+Alt+Z`撤销。

</div>

- 为新循环取一个有意义的名字，例如 *faces_block_loop*

### 步骤 5：增加一个新的试验序列

尽管词汇分类任务的试验序列与面部分类任务有一定的重叠, 但它们并不相同。因此, 我们无法重用前面创建的试验序列。

**要创建新的序列:**

- 从项目工具栏中抓取一个`sequence`元素
- 将其放入*faces_block_loop*中
- 此次选择“插入到”（参见%AppendLoopAndSequence）
- 将项目重命名为*faces_trial_sequence*

%--
video:
 source: youtube
 id: AppendLoopAndSequence
 videoid: PVcXdAN3rjM
 width: 640
 height: 360
 caption: |
  步骤5和6：向实验中添加第2个区块及其相应的试验序列。
--%

### 步骤6：选择面部刺激

**下载面部刺激**

在任务的面部部分，我们需要6张年轻和6张年老面部的图片。为避免性别偏见影响我们的结果，最好在每个类别中使用相同数量的男性和女性面孔（即：三个）。

您可以在此处下载一个示例刺激集（JPG格式）:

- %static:attachments/iat/face-stimuli.zip%

在大多数网页浏览器中，您可以右键单击链接并选择“保存链接为”或类似选项。在您下载了这些文件（例如将其保存到“下载”文件夹中）之后，您可以解压缩它们。

**将JPG文件添加到文件池**

- 如果文件池尚未显示出来（默认在窗口的右侧），则请单击主工具栏中的“显示文件池”按钮（快捷键：`Ctrl+P`）。
- 单击加号以添加文件
- 浏览到“下载”文件夹（或者您保存并解压了*face-stimuli*文件夹的地方），然后添加这12个JPG文件。

文件池现在应该看起来类似于%FacesBlockLoop

### 步骤7：循环表格的内容

就像实验的前一部分（参见步骤1）我们需要三列来定义实验变量：*stimulus*，*category*和*correct_response*。唯一的区别是，这次刺激是刚刚添加到文件池的JPG文件。

关于正确的反应，我们假设：

- *YOUNG*类别出现在屏幕的左侧，而*OLD*类别出现在右侧
- 响应规则与之前相同

创建上述列，并确保您的区块循环以如下方式完成：

%--
图：
 id：FacesBlockLoop
 source：faces_block_loop.png
 caption：|
  文件池的内容和与IAT的第2阶段（分类人脸）相对应的循环表。
--%

<div class='info-box' markdown='1'>

__提示__ -- *stimulus* 列中的值应与文件池中的文件名完全相对应。否则，如果我们稍后要引用这些JPG，OpenSesame将无法找到它们。

</div>

### 步骤8：修改试验序列

现在，我们的新试验序列仍然为空。我们需要用以下事件来填充它（参见%TrialSequence）：

1. 显示500毫秒的定点
2. 展示一张脸的图片，以及两个类别名称（*OLD* 和 *YOUNG*）
3. 收集键盘响应
4. 将所有变量写入输出文件

__复制可重复使用的项目__

事件1，3和4与实验的单词部分相同。因此，我们可以通过复制相应的项目来重用它们。为此：

- 在概览区域中右键单击*fixation*（作为*words_trial_sequence*的一部分）
- 选择'复制（链接）'，因为我们想要创建同一项目的另一个实例
- 在*faces_trial_sequence*（即新序列）上右键单击
- 选择'粘贴'
- 选择'插入到...'
- 重复此过程以获取项目*keyboard_response* 和 *logger*（参见%LinkedCopies）


<div class='info-box' markdown='1'>

__提示__ -- 如果序列中的项目顺序混乱了，可以通过拖放来纠正

__提示__ -- 如果您意外地将副本放在概览区域的其他地方（即在您想要放置的试验序列之外），您可以随时按`Ctrl+Alt+Z`来撤销

</div>


%--
video：
 source：youtube
 id：LinkedCopies
 videoid：_vDGpPsSqIY
 width：640
 height：360
 caption：|
  使用链接式副本。
--%

### 步骤9：创建人脸展示

最后，我们需要创建一个新的`sketchpad`项目来展示面部刺激。为了实现这一点：

- 从概览区域中抓取一个`sketchpad`项目
- 将它拖放到*faces_trial_sequence*中


- 我们唯一需要做的就是将字符串 'of1.jpg' 替换为`[stimulus]`。这意味着 OpenSesame 使用变量`[stimulus]`（其中包含所有JPG名称）来确定应显示哪个图像。

~~~ .python
set duration 0
set description "Displays stimuli"
draw image center=1 file=[stimulus] scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text="YOUNG<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text=OLD x=320 y=-192 z_index=0
~~~

- 点击“应用并关闭”

接下来，我们要测试到目前为止实验是否有效。

## 组合块

### 一致映射

第三块是第一块和第二块的组合，因此参与者必须对单词和脸进行分类。映射是*一致的*，这样*积极*的单词和*年轻*的脸需要用左手进行响应，而*消极*的单词和*年老*的脸需要用右手进行响应（见％任务）。

### 第11步：创建第三个区块循环和试验序列

为了创建IAT的第三个区块，我们需要：

- 创建一个新的区块循环（并将其重命名为*congruent_block_loop*）（参见第四步）
- 在新的区块循环中创建一个新的试验序列，并将其命名为*congruent_trial_sequence*（参见第五步）。

你的实验概述现在应该是这样的（％OverviewWithCongruent）：

%--
figure:
  id: OverviewWithCongruent
  source: overview_with_congruent_loop.png
  caption: |
    插入第三个区块循环和试验序列后的实验概述。
--%

### 第12步：填充*congruent_block_loop*

一致区块循环的内容与单词区块循环和人脸区块循环非常相似，只是现在它包含了两种类型的刺激。因此：

- 将*word_block_loop* 的内容复制粘贴到 congruent_block_loop。这将占据第1行至第12行
- 对*faces_block_loop* 的内容执行相同操作。这将占据第13行至第24行
- （确保您不要将列标题复制两次）

### 第13步：填充*congruent_trial_sequence*

- 将项目* fixation*、* keyboard_response*和* logger*复制到新的试验序列中，就像在第8步那样进行操作
- 不幸的是，我们无法使用*word* sketchpad 和 *face* sketchpad 的副本，因为我们希望在显示器的左侧和右侧显示*两个*类别（即 POSITIVE 与 NEGATIVE 和 YOUNG 与 OLD）
- 因此，我们在congruent_trial_sequence中附加一个新的`sketchpad`项目，将其命名为*congruent_stimulus*。
- 确保新的sketchpad出现在固定点之后，位于`keyboard_response item`之前

您的实验概述现在应该如下所示（％OverviewWithCongruent）：

%--
图：
  id：OverviewWithCongruent
  source：overview_congruent_filled_in.png
  caption：|
    填充一致块的试验序列后的实验概述。
--%

### 第14步：调整*congruent_sketchpad* 的内容

打开*congruent_stimulus* sketchpad的选项卡，将其持续时间更改为0，而不是'keypress'。

__类别名称__

- 确保两个类别名称都出现在屏幕的左上角和右上角（见％任务）。使用以下映射：
    - 类别名称*POSITIVE*和*YOUNG*出现在左侧
    - *NEGATIVE* 和 *OLD* 出现在右侧

__字词刺激__

用与第1阶段相同的方式在屏幕中心显示字词刺激（见第3步）。使用`方括号语法`。

__脸部刺激__

以与第2阶段相同的方式在屏幕中心显示脸部刺激（见第9步）。添加

<div class='info-box' markdown='1'>

__提示__ - 如果你的sketchpad看起来很乱，不用担心。我们将在短时间内处理好这个问题。

</div>

## 第15步：使用 Show-if 语句

在实验的混合部分，我们希望OpenSesame确定它应该显示一个面孔还是一个单词。我们可以通过使用*Show-if语句*来实现这一点。更确切地说，我们希望stimulus_sketchpad：

- 当刺激是一个单词时（即，当块循环中的刺激列中的当前单元格是一个单词）*只*显示一个单词
- 当刺激是一个面孔时*只*显示一个面孔

为实现这一点：

- 向* congruent_block_loop *添加一列，并将其命名为* stimulus_type *
- 根据刺激为单元格赋值'单词'或'面孔'（请参阅％CongrLoop）

%--
 图：
  id：CongrLoop
  source： congruent_block_loop.png
  caption： |
   实验一致部分的块循环内容。
--%

接下来，使sketchpad的内容*依赖*于新创建列中的值：

- 选择草图板元素工具栏中的黑色箭头
- 单击问号（表示负责JPG文件显示的`Draw image element`）
- 点击属于此元素的`Show if`框，其默认设置为'总是'
- 使用方括号语法表明，只有当当前试验包含面孔图像时，才应该绘制草图板的这一部分，输入：

~~~ .python
[stimulus_type] = face
~~~

%--
视频：
  source： youtube
  id：RunIf
  videoid：jqGFefCmn1k
  width：640
  height：360
  caption：|
   在`sketchpad`项目中使用Run-if语句。
--%

- 对控制书面单词呈现的“Draw text element”执行相同操作。这次，Show-if语句应为

~~~ .python
[stimulus_type] = word
~~~

测试前三个实验块是否按预期工作。

## 不一致映射

## 步骤16：创建实验的不一致部分

### 任务

利用前面学到的知识构建最后的不一致实验部分。

一些建议：

- 给新项目（例如，新的`循环`和`顺序`项目）起有意义的名称（例如* incongruent_block_loop *，* incongruent_trial_sequence *）
- 复制每个块相同的项目（即定位点，键盘响应和记录器）
- 由于类别的映射（出现在左上角和右侧）应该交换，因此无法复制刺激草图板，使得：
    - 左侧显示* POSITIVE *和* OLD *
    - 右侧显示* NEGATIVE *和* YOUNG *（请参阅％Task）
- 应相应更改* correct_response *列中的值


<div class='info-box' markdown='1'>

__提示__您可以使用* congruent_stimulus *草图板的*未链接*副本来创建* incongruent_stimulus *草图板（除了类别名称* OLD *和* YOUNG *被交换外，几乎相同）。

与*链接*副本相比，*未链接*副本最初看起来是相同的（除了名称），但您可以在不影响未链接副本的情况下编辑原始副本，反之亦然。

</div>


## 额外任务：

### 容易：添加指令和告别画面

- `sketchpad`和`form_text_display`项目可以呈现文本
- 好的说明应简短而具体

### 中等：每次试验提供反馈

- 使用内置变量* correct *，具有
    - 如果参与者回应正确，则值为1
    - 如果参与者犯了错误，则值为0
- 提供反馈的一种简单方法是在错误回应之后短暂地呈现红点，在正确回应之后呈现绿点
- 使用Show-if语句
