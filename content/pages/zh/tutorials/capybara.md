title: 猫，狗和水豚
uptodate: false
hash: 66f26fecbe543127ecd03e1ed499f5e5ab9f112189ee97bc58925aeb119dddac
locale: zh
language: Chinese

%--
图
 id: FigCapybara
 source: capybara.png
 caption: |
  一只水豚。
--%


[TOC]


## 关于

我们将创建一个简单的动物多感官整合任务，参与者将看到一幅狗、猫或水豚的图片。在显示图片时，会播放喵叫声或狗叫声。参与者通过在屏幕上的响应按钮上点击鼠标来报告显示的是狗还是猫。当显示水豚时，不应给出响应：这些是捕获试验。

我们有两个简单的预测：

- 当播放狗叫声时，参与者应该更快地识别狗；当播放喵叫声时，更快地识别猫。换句话说，我们预期多感官一致性效应。
- 当参与者看到水豚时，如果听到狗叫，他们更可能报告看到了狗；如果听到猫叫，更可能报告看到了猫。换句话说，虚警受声音的影响。


## 教程

### 步骤1：下载并启动OpenSesame

OpenSesame可用于Windows，Linux，Mac OS和Android（仅运行时）。本教程适用于OpenSesame 3.3.X。您可以从此处下载OpenSesame:

- %link:download%

当你启动OpenSesame时，您将得到一个实验模板的选择，以及（如果有）最近打开的实验列表（见 %FigStartUp）。

%--
图
 id: FigStartUp
 source: start-up.png
 caption: |
  启动OpenSesame窗口。
--%

*Extended template*为创建基于试验的实验提供了一个很好的起点。然而，在本教程中，我们将从头开始创建整个实验。因此，我们将继续使用已经加载的“默认模板”(%FigDefaultTemplate)。所以只需关闭“Get started!”和（如果显示）“Welcome!”选项卡。

%--
图
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  "默认模板"的结构，如概览区域所示。
--%

<div class='info-box' markdown='1'>

**背景框1：基本知识**

OpenSesame实验是*项目*的集合。项目是一个小的功能块，例如，可以用于呈现视觉刺激（SKETCHPAD项目）或记录按键（KEYBOARD_RESPONSE项目）。项目有类型和名称。例如，您可能有两个类型为KEYBOARD_RESPONSE名称为 *t1_response* 和 *t2_response* 的项目。为了使项目类型和项目名称之间的区别清楚，我们将使用这种风格的类型，*=*=与这种风格的名称。*=*

为了让您的实验更有结构，两种类型的项目尤为重要：LOOP和SEQUENCE。理解如何将LOOP和SEQUENCE结合起来构建实验可能是使用OpenSesame最棘手的部分，所以让我们先将其解决。

LOOP通常是您定义自变量的地方。在LOOP中，您可以创建一个表格，其中每一列对应一个变量，每一行对应一个要运行的项目的单个运行。为了更具体，让我们考虑以下*block_loop*（与本教程无关）：

%--
图
 id: FigLoopTable
 source: loop-table.png
 caption: |
  在循环表中定义的变量的示例。（此示例与本教程中创建的实验无关。）
--%

这个*block_loop*将执行*trial_sequence*四次。一次是当“soa”为100且“target”为“F”时，一次是当“soa”为100且“target”为“H”时，等等。默认情况下，循环表的行遍历顺序是随机的，但也可以在选项卡右上方设置为顺序。

序列（SEQUENCE）由依次执行的一系列项目组成。一个典型的序列是*trial_sequence*，它对应于一个单一试验。例如，一个基本的*trial_sequence*可能包括一个 SKETCHPAD，用于呈现刺激物，一个 KEYBOARD_RESPONSE，用于收集响应，以及一个 LOGGER，用于将试验信息写入日志文件。

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  一个用作试验序列的SEQUENCE项目示例。 （此示例与本教程中创建的实验无关。）
--%

你可以以分层的方式组合LOOP和SEQUENCE，以创建试验块以及练习和实验阶段。例如，*trial_sequence*由*block_loop*调用。这些共同对应一个试验块。向上一级，*block_sequence*由*practice_loop*调用。这些共同对应实验的练习阶段。

</div>

### 步骤2：添加block_loop和trial_sequence

默认模板开始时有三个项目：名为*getting_started*的NOTEPAD，名为*welcome*的SKETCHPAD和名为*experiment*的SEQUENCE。我们不需要*getting_started*和*welcome*，所以立刻删除它们。右键单击这些项目，然后选择“删除”。不要删除*experiment*，因为它是实验的入口（即实验开始时调用的第一个项目）。

我们的实验结构非常简单。在层次结构的顶部，有一个我们将称之为*block_loop*的LOOP。我们将再*block_loop*中定义我们的自变量（另请参见背景框1)。要将LOOP添加到实验中，请将项目工具栏中的LOOP图标拖放到概览区域中的*experiment*项目上。

一个LOOP项目需要另一个项目才能运行；通常情况下，就像在这个例子中一样，这是一个SEQUENCE。将项目工具栏中的SEQUENCE项目拖到概览区域中的*new_loop*项目上。OpenSesame会要求您是否要将SEQUENCE插入到LOOP中或在LOOP之后。选择“插入到new_loop”。

默认情况下，项目的名称如*new_sequence*，*new_loop*，*new_sequence_2*等。这些名称不是很有信息含量，建议重命名它们。项目名称必须由字母数字字符和/或下划线组成。要重命名项目，请在概览区域双击项目。将*new_sequence*重命名为*trial_sequence*，表示它将对应于一个单一的小试。将*new_loop*重命名为*block_loop*，以表示它将对应于一组试验。

我们实验的概览区域现在看起来如%FigStep3。

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  步骤2结束时的概览区域。
--%

<div class='info-box' markdown='1'>

**背景框3：未使用的项目**

__提示__ – 删除的项目仍在未使用的项目箱中，除非您在未使用的项目选项卡中选择“永久删除未使用的项目”。您可以通过将它们从未使用的项目箱中托出并放入SEQUENCE或LOOP中，将删除的项目重新添加到实验中。

</div>

### 步骤3：导入图像和声音文件

在这个实验中，我们将使用猫、狗和水豚的图像。我们还将使用喵和汪的声音样本。您可以从下面这个链接下载所需的所有文件：

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

下载 `stimuli.zip` 并将其解压缩到某个地方（例如桌面）。接下来，在OpenSesame中，点击主工具栏中的 “显示文件池” 按钮（或：菜单→视图→显示文件池）。这将显示文件池，默认情况下在窗口的右侧。将刺激添加到文件池的最简单方法是从桌面（或您解压缩文件的任何地方）将它们拖放到文件池中。或者，您可以在文件池中点击 “+” 按钮，通过出现的文件选择对话框添加文件。文件池将自动保存在您的实验中。

添加完所有刺激后，您的文件池看起来如 %FigStep4 中所示。

%--
图：
 id: FigStep4
 source: step4.png
 caption: |
  第三步结束时的文件池。
--%

### 第四步：在 block_loop 中定义实验变量

从概念上讲，我们的实验具有完全交叉的 3×2 设计：我们有三种类型的视觉刺激（猫、狗和水豚），它们与两种类型的听觉刺激（喵和汪）共同发生。然而，我们有五个示例用于每种刺激类型：五个喵声、五个水豚图片等。从技术的角度来看，将我们的实验视为 5×5×3×2 的设计是有意义的，其中图片数量和声音数量是具有五个水平的因素。

OpenSesame 非常擅长生成全因素设计。首先，通过点击概述区域中的 *block_loop* 打开它。接下来，点击全因素设计按钮。这将打开一个生成全因素设计的向导，其工作方式非常简单：每一列对应一个实验变量（即一个因素）。第一行是变量的名称，下面的行包含所有可能的值（即水平）。在我们的例子中，我们可以将 5×5×3×2 的设计指定为 %FigLoopWizard 中所示。

%--
图：
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  循环向导生成全因素设计。
--%

点击“确定”后，您将看到现在有一个具有四行的循环表格，每个实验变量各一行。共有 150 个周期（=5×5×3×2），这意味着我们有 150 个独特的试验。您的循环表格现在看起来如 %FigStep5 中所示。

%--
图：
 id: FigStep5
 source: step5.png
 caption: |
  第四步结束时的循环表。
--%

### 第五步：在 trial_sequence 中添加项目

打开仍为空的 *trial_sequence*。是时候添加一些项目了！我们的基本 *trial_sequence* 是：

1. 一个SKETCHPAD在500毫秒内显示一个中央的注视点
2. 一个SAMPLER播放一个动物声音
3. 一个SKETCHPAD显示一个动物图片
4. 一个MOUSE_RESPONSE收集响应
5. 一个LOGGER将数据写入文件

要添加这些项目，只需将它们从项目工具栏一个接一个地拖放到 *trial_sequence* 中。如果您不小心将项目放在错误的位置，可以通过拖放来重新排序它们。将所有项目排列正确顺序后，为其中的每一个起一个合理的名称。概览区现在看起来如 %FigStep6 中所示。

%--
图：
 id: FigStep6
 source: step6.png
 caption: |
  第五步结束时的概览区域。
--%

### 第六步：定义中央注视点

在概览区域中单击 *fixation_dot*。这会打开一个基本的画板，您可以用它来设计您的视觉刺激。要绘制一个中央注视点，首先点击十字准线图标，然后点击显示器的中心，即位置（0,0）。

我们还需要指定注视点的可见时间。为此，请将持续时间从“按键”更改为 495ms，以指定 500ms 的持续时间。 （参见背景框 4中的解释。）

注视点项目现在看起来如 %FigStep7 中所示。

%--
图：
 id: FigStep7
 source: step7.png
 caption: |
  第六步结束时的 *fixation_dot* 项目。
--%

<div class='info-box' markdown='1'>

**背景框 4：选择正确的持续时间**

如果我们希望持续时间为500毫秒，为什么要指定持续时间为495？这是因为实际显示呈现持续时间总是向上舍入为与显示器刷新率兼容的值。这听起来可能很复杂，但对于大多数场合，下列经验法则足够：

1. 根据显示器的刷新率选择一个可能的持续时间。例如，如果显示器的刷新率为60Hz，这意味着每帧持续16.7毫秒（=1000毫秒/60Hz）。因此，在60Hz的显示器上，您应始终选择是16.7毫秒的倍数的持续时间，例如16.7、33.3、50、100等。
2. 在SKETCHPAD的持续时间字段中，指定一个比您要实现的时间短几毫秒的持续时间。所以，如果你想展示一个SKETCHPAD持续50毫秒，选择一个持续时间为45。 如果您想展示一个SKETCHPAD为1000毫秒，选择一个持续时间为995。等等。

有关实验定时的详细讨论，请参见：

- %link:timing%

</div>


### 步骤7：定义动物声音

打开*animal_sound*。SAMPLER项目提供了几个选项，最重要的是要播放的声音文件。点击浏览按钮打开文件池选择对话框，然后选择其中一个声音文件，例如 `bark1.ogg`。

当然，我们不想一遍又一遍地播放同样的声音！相反，我们要根据我们在*block_loop*（步骤5）中定义的变量`sound`和`sound_nr`来选择一个声音。要做到这一点，只需用方括号之间的该变量的名称替换您要根据变量取决的字符串的一部分。更具体地说，'bark1.ogg'变为'[sound][sound_nr].ogg'，因为我们想用变量`sound`的值替换'bark'，用'sound_nr'的值替换'1'。

我们还需要更改SAMPLER的持续时间。默认情况下，持续时间为'sound'，这意味着实验会在播放声音时暂停。将持续时间更改为0。这并不意味着声音只会播放0毫秒，而是实验将立即继续进行到下一个项目，同时声音将继续在后台播放。*animal_sound* 项目现在看起来如同%FigStep8。

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  步骤7完成后，项目*animal_sound*。
--%

<div class='info-box' markdown='1'>

**背景框5：变量**

有关使用变量的详细信息，请参见：

- %link:manual/variables%

</div>

### 步骤8：定义动物图片

打开*animal_picture*。 通过点击带有像风景一样的图标的按钮来选择图像工具。 单击显示器中心（0，0）。 在出现的文件池对话框中，选择 `capybara1.png`。 现在树懒般的侧身透视图将从显示器中心懒洋洋地盯着你。 但是，我们当然不总是想显示同样的树懒。 相反，我们希望根据我们在*block_loop*（步骤4）中定义的变量`animal`和`pic_nr`中的图片。

我们可以使用与*animal_sound*的基本相同的方法，在虽然对图像稍有不同。 首先，右键单击树懒，然后选择“编辑脚本”。 这样，您可以编辑与树懒图片对应的以下行的OpenSesame脚本：

```python
draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0
```

现在将图像文件的名称从'capybara.png'更改为'[animal][pic_nr].png'：

```python
draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0
```

单击“确定”以应用更改。树懒现在消失了，换成了一个占位符图片，OpenSesame告诉您有一个对象未显示，因为它是使用变量定义的。别担心，实验过程中它会显示出来！

我们还添加了两个响应圈：

- 屏幕左侧有一个名为“狗”的圆圈（为了提醒参与者回应规则，可以在圆圈中添加带有“狗”文字的元素。这只是视觉上的。）
- 屏幕右侧有一个名为“猫”的圆圈（为了提醒参与者回应规则，可以在圆圈中添加带有“猫”文字的元素。）

我们将把这些圆圈用作鼠标响应中的*感兴趣区域*。更具体地说，因为我们给圆圈起了名字，所以我们的*mouse_response*项将能够检查鼠标点击是否落在其中一个圆圈内。我们将在第9步中回顾这个问题。

最后将“Duration”字段设置为“0”。这并不意味着图片仅呈现0毫秒，而是实验会立即前进到下一个项目（*response*）。由于*response*等待响应，但不改变屏幕上的内容，所以目标会一直可见，直到给出响应。

%--
figure:
 id: FigStep9
 source: step9.png
 caption: |
  第8步完成后的*animal_picture* SKETCHPAD。
--%

<div class='info-box' markdown='1'>

**背景框 6：图像格式**

__提示__-- OpenSesame可以处理各种图像格式。然而，一些（非标准）的`.bmp`格式已知会导致问题。如果发现`.bmp`图像无法显示，可以考虑使用其他格式，如`.png`。您可以使用免费工具如[GIMP]轻松转换图像。

</div>


### 第9步：定义响应

打开*mouse_response*项目。这是一个MOUSE_RESPONSE项目，它收集单个鼠标点击（或释放）。有几个选项：

- __正确响应__ — 这里你可以指示哪个鼠标按钮是正确的响应。但是，我们将根据参与者点击的位置来确定响应是否正确，而不是根据点击的按钮，所以我们可以保留此字段为空。
- __允许响应__是一个分号分隔的鼠标按钮列表，这些按钮被接受。让我们将其设置为“左键”。
- __超时__表示在响应设置为“无”之后的持续时间，实验将继续。在我们的实验中，超时很重要，因为参与者需要有机会在看到水豚时*不*回应。因此，我们将超时设置为2000。
- __关联草图板__指示应将其元素用作感兴趣区域的SKETCHPAD。我们将选择*animal_picture*。现在，如果我们点击名为“猫”的元素，`cursor_roi`变量将自动设置为“猫”。
- __可见鼠标光标__ - 指示在收集响应期间应显示鼠标光标。我们需要启用这个功能，以便参与者可以看到他们点击的位置。
- __刷新等待中的鼠标点击__表明我们应只接受新的键鼠标点击。最好保持启用（默认启用）。

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  第9步完成后的*mouse_response* MOUSE_RESPONSE。
--%


### 第10步：定义记录器

我们不需要配置LOGGER，因为默认设置就很好；但是让我们研究一下它。在概述区单击*logger*将其打开。您会看到“记录所有变量（推荐）”选项已被选中。这意味着OpenSesame会记录所有内容，这是可以的。

<div class='info-box' markdown='1'>

**背景框 8：始终检查您的数据！**

__一个统领一切的建议__ — 始终三倍检查实验中记录的所有必需变量！检查这一点的最佳方法是运行试验并查看生成的日志文件。

</div>

### 第11步：完成！（有点……）

您现在应该能够运行您的实验。还有很多改进空间，您将在下面的额外任务部分继续完善实验。但基本结构已经有了！

点击主工具栏中的“全屏运行”（`Control+R`）按钮进行测试运行。

<div class='info-box' markdown='1'>

**背景框 11：快速运行**

__提示__ — 测试运行可以通过点击橙色的“在窗口中运行”按钮更快地执行，它不会询问您如何保存日志文件（因此只能用于测试目的）。

</div>


## 额外任务

下面的额外任务需要您自己解决。这些任务的解决方案可以在[实验文件](https://osf.io/2gr3a/)中找到。但解决它们的最佳方法就是自己动手！


### 容易：添加说明和告别屏幕

- SKETCHPAD和FORM_TEXT_DISPLAY项目可以呈现文本
- 好的说明短而具体


### 容易：检查数据

- 请先自行运行一次实验。您可以通过将*block_loop*的重复值设置为小于1来减少试验次数。
- 在Excel, LibreOffice或JASP中打开数据文件


### 中等：每个试验提供反馈

- 要执行此操作，您需要已经定义了正确的响应！（详见下文。）
- 提供反馈的一个好方法且不引人注意的方法是，在错误响应后短暂呈现红点，在正确响应后呈现绿点
- 使用Run If语句！


### 中等：对响应规则进行对易

- 变量`subject_parity`为“偶数”或“奇数”
- 对于偶数和奇数参与者，使用两个不同的动物图片SKETCHPAD和MOUSE_RESPONSE项目


### 中等：不要重复同一张动物图片

- 您可以将随机化约束指定为高级循环操作


### 困难：确定响应是否正确

- 需要一个INLINE_SCRIPT
- 将变量`correct`设为错误响应的0，正确响应的1
- 如果出现超时，变量`response`是字符串“无”
- 否则，变量`cursor_roi`包含了所有被点击的元素名称（来自链接的SKETCHPAD），用分号分隔。可能会点击上多个元素，例如动物图片和响应圈重叠时


### 困难：将试验分成多个组

- 在trial_sequence的结尾添加一个SKETCHPAD，邀请参与者休息片刻
- 使用Run If语句仅在每15次试验后运行此SKETCHPAD
- 完成此操作需要模块运算符（`%`）和变量`count_trial_sequence`


### 困难：为在线运行实验进行调整

- 需要一个INLINE_JAVASCRIPT
- 目前，OSWeb不支持将MOUSE_RESPONSE链接到SKETCHPAD。这意味着您需要用确定`cursor_x`的变量来确定参与者点击的位置，以及响应是否正确。
- OSWeb不支持INLINE_SCRIPT项目


## 参考文献

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: 适用于社会科学的开源图形实验构建器。 *行为研究方法*，*44*(2)，314-324。 doi:10.3758/s13428-011-0168-7
{: .reference}