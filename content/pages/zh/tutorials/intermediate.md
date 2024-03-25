title: 中级教程（Python）视觉搜索
hash: 2db5f6aa8a0276e362c99516e42c8d94a078dd3c52b5eacb7f4686da10b768df
locale: zh
language: Chinese

## 关于 OpenSesame

OpenSesame 是一个用户友好的程序，用于发展心理学、神经科学和实验经济学的行为实验。对于初学者来说，OpenSesame 拥有全面的图形化点击界面。对于高级用户，OpenSesame 支持 Python（仅限桌面端）和 JavaScript（桌面端和浏览器端）。

OpenSesame 在 [通用公共许可证 v3][gpl] 下免费提供。

## 关于本教程

本教程将展示如何使用OpenSesame创建一个基础的视觉搜索实验[(Mathôt, Schreij, & Theeuwes, 2012)][references]。我们将使用图形界面和 Python 脚本开发一个可以在传统实验室环境的桌面端运行的实验。我们建议使用者具备一些 OpenSesame 和 Python 的经验。本教程大约需要一个小时。

这个教程的 JavaScript 版本也可用。如果你想在浏览器中在线运行你的实验（使用 OSWeb），那么 JavaScript 教程就是你所需要的：

- %link:tutorials/intermediate-javascript%

## 资源

- __下载__ — 本教程假定您正在运行 OpenSesame 版本 4.0.0 或更新版本。您可以从以下网址下载最新版本的 OpenSesame：
	- %link:download%
- __文档__ — 专门的文档网站可以在以下网址找到：
	- <http://osdoc.cogsci.nl/>
- __论坛__ — 支持论坛可以在以下网址找到：
	- <http://forum.cogsci.nl/>
- __Sigmund__ -- SigmundAI 是一个拥有 OpenSesame 专家知识的 AI 助手，可以在以下网址找到：
	- <https://sigmundai.eu/>

## 实验

在这个教程中，您将创建一个基础的视觉搜索实验。这个实验类似于 [Treisman and Gelade (1980)][references] 的经典视觉搜索研究，但并不完全相同。

在这个实验中，参与者要搜索一个目标对象，它可以是黄色矩形、黄色圆形、蓝色矩形或蓝色圆形；目标的身份在实验的不同块中有所变化。参与者通过按下右箭头键（存在）或左箭头键（不存在）来指示目标是否存在。

除了目标之外，还会显示零个或多个干扰物对象。有三种条件，条件决定了干扰物的类型：

- 在 *Conjunction* 条件下，干扰物可以是任何形状和颜色，唯一的限制是干扰物不能与目标完全相同。例如，如果目标是一个黄色矩形，那么干扰物可以是黄色圆形、蓝色圆形和蓝色矩形。
- 在 *Shape Feature* 条件下，干扰物有与目标不同的形状，但颜色可以任意。例如，如果目标是一个黄色矩形，那么干扰物可以是黄色圆形和蓝色圆形。
- 在 *Color Feature* 条件下，干扰物可以是任何形状，但颜色要与目标不同。例如，如果目标是一个黄色矩形，那么干扰物可以是蓝色矩形和蓝色圆形。

每个试次后都会显示即时反馈：正确响应后显示绿点，错误响应后显示红点。每个实验块后都会显示关于平均响应时间和准确度的详细反馈。

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  您将在这个教程中实现的视觉搜索实验。
--%

这类实验显示了两个典型的发现：

- 在 Conjunction 条件下找到目标的时间比在两种特征条件下更长。
- 在 Conjunction 条件下，随着干扰物数量的增加，响应时间也会增加。这表明人们是逐个项目搜索目标；这被称为 *serial search*。
- 在特征条件（形状和颜色）下，响应时间不会或几乎不会随着干扰物数量的增加而增长。这表明人们是一次性处理整个显示内容；这被称为 *parallel search*。

根据Treisman和Gelade的特征整合理论，这些结果反映了在连接条件下，您需要将每个物体的颜色和形状结合或*绑定*。这种绑定需要注意力，因此您需要将注意力从一个对象移到下一个对象；这是缓慢的，解释了反应时间取决于有多少个物体。相比之下，在特征条件下，颜色和形状不需要被绑定，因此整个显示器可以在没有将注意力集中在每个物体上的情况下一次性处理。

## 实验设计

该设计：

- 是*在主题内*，因为所有参与者都进行所有条件
- 是*完全交叉*（或满阶因子），因为所有条件组合都会出现
- 有三个条件（或因素）：
	- 在块内变化：
		- `set_size`具有三个级别（1，5，15），或SS<sub>3</sub>
		- `condition`具有三个级别（conjunction，feature_shape，feature_color），或CN<sub>3</sub>
		- `target_present`具有两个级别（present，absent），或TP<sub>2</sub>
	- 在块间变化：
		- `target_shape`具有两个级别（square，circle），或TS<sub>2</sub>
		- `target_color`具有两个级别（yellow，blue），或TC<sub>2</sub>
- 有N个受试者，或<u>S</u><sub>N</sub>

您可以将此设计写为<u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

有关实验设计表示法的更多信息，请参阅：

- %link:experimentaldesign%

## 步骤1：创建实验的基本结构

启动OpenSesame，然后在“开始！”选项卡中选择“Extended模板”。这个模板提供了许多认知心理学实验（比如我们将要创建的这个实验）通用的基本结构。

Extended模板包含一些我们不需要的项目。删除以下项目：

- *about_this_template*
- *practice_loop*
- *end_of_practice*

删除这些项目后，它们仍然可以在“未使用项目”的回收站中看到。要永久删除这些项目，请单击“未使用项目”的回收站，然后单击“永久删除未使用项目”。

最后，为实验起一个好名字，例如“Visual search”。为此，请打开通用属性标签页（通过在概览区域中单击“Extended模板”），然后单击实验名称进行编辑。

现在，概览区域应该与%FigStep1相符：

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  第一步结束时的概览区域。
--%

## 步骤2：定义在块之间变化的实验变量

如上所述，在我们的实验中，两个变量在块之间变化：`target_shape`和`target_color`。因此，我们需要在*experimental_loop*中定义这些变量。要理解为什么，请考虑%FigStep1中所示的结构，从最底部（即最缩进水平）开始稍微了解。

- *trial_sequence* 对应一个试验
- *block_loop* 对应一系列的试验
	- 因此，在此处定义的变量针对每次运行的*trial_sequence*变化；换句话说，在* block_loop *中定义的变量是__ 在块内 __的变化。
- *block_sequence* 对应一个试验序列，包括重置反馈变量之前以及参与者反馈之后
- *experimental_loop* 对应多个试验序列
	- 因此，在此处定义的变量针对每次运行的* block_sequence *变化；换句话说，在* experimental_loop *中定义的变量是__ 在块间 __的变化。
- *experiment* 对应整个实验，包括说明屏幕，多个试验序列，和实验结束屏幕

单击实验循环，并定义：

- `target_shape`，可以是'square' 或 'circle'；和
- `target_color`，可以是'yellow' 或 'blue'。

我们有一个完全因子设计，也就是说所有的 2 × 2 = 4 种组合都必须出现。现在 *experimental_loop* 的表格应该像 %FigStep2 那样：

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  第二步结束后，*experimental_loop*的表格。
--%

## 步骤 3：在每个 block 开始时给出指导

现在，实验以一个单独的 *instructions* 屏幕开始。在我们的案例中，我们希望在每个试验 block 之前给出指导，告诉参与者要寻找哪个目标（因为目标在不同的 block 间有所不同）。

__将指导移至 block_sequence 中__

因此，拖拽 *instructions* 项目到 *block_sequence* 中。这时会弹出一个对话框，询问您是否要：

- 将该项目插入到 *block_sequence* 中，在这种情况下，*instructions* 会成为 *block_sequence* 的第一个项目；或者
- 在 *block_sequence* 之后插入该项目，在这种情况下，*instructions* 会移到 *block_sequence* 之后的某个位置。

选择第一个选项（'插入到'）。现在 *block_sequence* 以指导界面开始，这正是我们想要的。

__添加指导性文本__

点击 *instructions* 打开它，并输入一段好的指导性文本，如：

```text
指导

寻找 {target_color} {target_shape}

如果找到了，按右箭头键
如果没找到，按左箭头键

按任意键开始
```

大括号“{target_color}”和“{target_shape}”表示这些不是字面文本，而是我们在 *experimental_loop* 中定义的变量。当实验运行时，这些变量的值将出现在这里，参与者将看到（例如）“寻找黄色圆圈”。

__给出目标的视觉预览__

向参与者展示她需要寻找的实际刺激也是很好的。为此：

- 在显示器中心绘制一个已填充的圆（确保它不会与文本重叠）；
- 将圆的颜色改为“{target_color}”。这意味着圆的颜色取决于变量 `target_color` 的值；以及
- 更改 show-if 表达式为 `target_shape == 'circle'`。这是一个通过 Python 表达式检查变量 `target_shape` 是否为 “circle”。

换句话说，我们画了一个颜色由 `target_color` 确定的圆；另外，当变量 `target_shape` 的值为“circle”时，只显示这个圆。有关变量和 show-if 语句的更多信息，请参阅：

- %link:manual/variables%

我们使用相同的方法绘制一个方形：

- 在显示器中心绘制一个已填充的方形；
- 将方形的颜色改为“{target_color}”；以及
- 更改 show-if 语句为 `target_shape == 'square'`

现在，*instructions* 屏幕应该像 %FigStep3 那样：

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  第三步结束后，*instructions*屏幕的样子。
--%

## 步骤 4：定义实验内变化的变量

在我们的实验中，`condition`、`set_size` 和 `target_present` 这三个变量在 block 内变化。如步骤 2 所述，我们需要在 *block_loop* 中定义这些变量，以便它们在每次运行 *trial_sequence* 时都能变化。

这三个变量总共有 3 × 3 × 2 = 18 种不同的组合。我们可以手动输入表格中的组合，但是因为我们采用了完全因子设计，所以我们也可以使用完全因子设计向导。首先打开 *block_loop*，然后点击 “完全因子设计” 按钮。

在出现的表格中，将变量名放在第一行，将值放在下面的行中，如 %FigFullFactorial：

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  第三步结束后，*instructions*屏幕的样子。
--%

现在点击 “Ok” 生成完整设计。*block_loop* 的表格现在应该像 %FigStep4 那样。

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  第4步结束时的*block_loop*表格。
--%

## 第5步： 创建试验序列

我们希望我们的试验序列如下所示：

- 固定点，我们将使用 SKETCHPAD。
- 搜索显示，我们将使用自定义的 INLINE_SCRIPT 在 Python 中创建。
- 响应收集，我们将使用 KEYBOARD_RESPONSE。
- 数据记录，我们将使用 LOGGER。
- （我们还希望在每次试验后立即得到反馈，但我们稍后会回到这一点。）

所以唯一缺少的是一条 INLINE_SCRIPT。

- 插入一条新的 INLINE_SCRIPT，放在 *sketchpad* 之后，并将其重命名为 *search_display_script*。
- 将 *sketchpad* 重命名为 *fixation_dot*，以便明确其功能；并且
- 将 *fixation_dot* 的持续时间更改为500，这样固定点会显示500毫秒。（应该已经有了一个绘制的固定点；如果没有，请在 *fixation_dot* 的中心画一个。）

概述区现在应该如 %FigStep5 所示。

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  第5步结束时的概述区域。
--%

## 第6步：生成搜索显示

__自上而下和防御性编程__

现在事情变得有趣了：我们将开始使用 Python 编程。我们将遵循两个指导原则：*自上而下* 和 *防御性* 编程。

- *自上而下编程* 意味着我们从最抽象的逻辑开始，不费心于逻辑应该如何实现。一旦最抽象层面的逻辑就位，我们将转移到稍微不那么抽象的逻辑层面，依此类推，直至到达实现的细节。此技术有助于保持代码结构化。
- *防御性编程* 意味着我们假设我们会犯错误。因此，为了保护我们自己免受伤害，我们在代码中构建了一些完整性检查。

*注意：* 下面的解释假设你对 Python 代码有一定的了解。如果 `list`、`tuple` 和函数之类的概念对你来说没有任何意义，那么最好先学习一个入门 Python 教程，例如这个：

- <https://pythontutorials.eu/>

代码逻辑如 %FigHierarchy 所示。这些数字表示我们将实现功能的顺序，从抽象级别开始。

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  绘制视觉搜索显示的代码逻辑。
--%

__准备和运行阶段__

打开 *search_display_script* 并切换到 Prepare 标签。OpenSesame 区分两个执行阶段：

- 在准备阶段，每个项目都有机会为自己做好准备；具体含义取决于项目：对于 SKETCHPAD，这意味着绘制画布（但不显示）；对于 SAMPLER，这意味着加载声音文件（但不播放）；等等。
- 在运行阶段，每个项目会被实际执行；同样地，具体含义取决于项目：对于 SKETCHPAD，这意味着显示之前准备好的画布；对于 SAMPLER，这意味着播放先前加载的声音文件。

对于 INLINE_SCRIPT，你需要自己决定将哪些内容放在准备阶段，将哪些内容放在运行阶段。区分通常很明确：在我们的案例中，我们将绘制画布的代码放在准备阶段，将显示画布的代码（较小部分）放在运行阶段。

另请参阅：

- %link:prepare-run%

__实现抽象层次__

我们从最抽象的层次开始：定义一个绘制视觉搜索显示的函数。我们不指定*如何*实现这个功能；我们只是假设有一个函数可以实现这个功能，我们稍后再考虑细节，这就是自上而下编程。

在 Prepare 标签中输入以下代码：

~~~ .python
c = draw_canvas()
~~~

这里发生了什么？我们…

- 调用 `draw_canvas()`，它返回一个我们作为`c`存储的`Canvas`对象；换句话说，`c`是一个与搜索显示对应的`Canvas`对象。这假设有一个函数`draw_canvas()`，尽管我们还没有定义它。

一个`Canvas`对象是一个单一的显示；从某种意义上说，它是SKETCHPAD的Python对等物。详见：

- %link:manual/python/canvas%

现在我们通过定义`draw_canvas()`来向下走一步（在迄今为止的剩余脚本之上）：

~~~ .python
def draw_canvas():
    """绘制搜索画布。

    返回
    -------
    Canvas
    """
    c = Canvas()
    xy_list = xy_random(n=set_size, width=500, height=500, min_dist=75)
    if target_present == 'present':
        x, y = xy_list.pop()
        draw_target(c, x, y)
    elif target_present != 'absent':
        raise Exception(f'Invalid value for target_present: {target_present}')
    for x, y in xy_list:
        draw_distractor(c, x, y)
    return c
~~~

这里发生了什么？我们…

- 使用工厂函数`Canvas()`创建一个空的画布`c`。
- 使用另一个通用函数`xy_random()`生成一个随机的`x, y`坐标列表，称为`xy_list`。此列表确定了呈现刺激的位置。
- 检查实验变量`target_present`是否具有值'present'；如果是，则从`xy_list`中“弹出”一个`x，y`元组，并在此位置绘制目标。这假设有一个函数`draw_target()`，尽管我们还没有定义它。
- 如果`target_present`既不是'present'也不是'absent'，我们引发一个`Exception`；这是防御性编程，可以保护我们免受拼写错误（例如，如果我们错误地输入了'presenr'而不是'present'）。
- 遍历所有剩余的`x，y`元组并在每个位置绘制干扰物。这假设有一个函数`draw_distractor()`，尽管我们还没有定义它。
- 返回`c`，现在已经在其上绘制了搜索显示。

有几个通用函数，例如`Canvas()`和`xy_random()`，始终可用。详见：

- %link:manual/python/common%

实验变量是全局变量。这就是为什么即使在脚本中从未显式定义变量`set_size`，您仍然可以引用*block_loop*中定义的`set_size`。对于`target_shape`、`target_color`、`condition`等也是如此。详见：

- %link:var%

__实现中间层__

现在我们通过定义`draw_target`再向下走一步（在迄今为止的剩余脚本之上）：

~~~ .python
def draw_target(c, x, y):
    """绘制目标。

    参数
    -------
    c: Canvas
    x: int
    y: int
    """
    draw_shape(c, x, y, color=target_color, shape=target_shape)
~~~

这里发生了什么？我们…

- 调用另一个函数`draw_shape()`，并指定需要绘制的颜色和形状。这假设有一个函数`draw_shape()`，尽管我们还没有定义它。

我们还定义`draw_distractor`（在迄今为止的剩余脚本之上）：

~~~ .python
def draw_distractor(c, x, y):
    """绘制一个干扰物。

    参数
    -------
    c: Canvas
    x: int
    y: int
    """
    if condition == 'conjunction':
        draw_conjunction_distractor(c, x, y)
    elif condition == 'feature_shape':
        draw_feature_shape_distractor(c, x, y)
    elif condition == 'feature_color':
        draw_feature_color_distractor(c, x, y)
    else:
        raise Exception(f'Invalid condition: {condition}')
~~~

这里发生了什么？我们…

- 根据条件调用另一个函数来绘制更具体的干扰物。
- 检查`condition`是否具有预期的值。如果没有，则我们引发一个`Exception`。这是防御性编程！如果没有这个检查，当我们在某处写错时，干扰物可能只是没有显示而没有引发错误信息。

现在我们定义一个函数，用于绘制Conjunction条件下的干扰物（在迄今为止的剩余脚本之上）：

~~~ .python
import random

def draw_conjunction_distractor(c, x, y):
    """在连接条件下绘制单个干扰物：可以是任何形状和颜色的物体，但不能与目标相同。

    参数
    ----------
    c: 画布
    x: int
    y: int
    """
    conjunctions = [('黄色', '圆形'),
                    ('蓝色',   '圆形'),
                    ('黄色', '正方形'),
                    ('蓝色',   '正方形')]
    conjunctions.remove((目标颜色, 目标形状))
    颜色, 形状 = random.choice(conjunctions)
    draw_shape(c, x, y, color=颜色, shape=形状)
~~~

这里发生了什么？我们...

- 定义一个列表`conjunctions`，其中包含所有可能的颜色和形状组合。
- 从这个列表中删除目标；这是必要的，因为干扰物不能与目标相同。
- 从`conjunctions`中随机选择一组颜色和形状组合。
- 调用另一个函数`draw_shape()`，并指定要绘制的干扰物的颜色和形状。这假设有一个函数`draw_shape()`，尽管我们还没有定义它。

此外，我们…

- 在脚本顶部添加`import random`这一行。这样我们才能使用`random`模块中的函数，比如`random.choice()`。

现在，我们在形状特征条件下定义绘制干扰物的功能（在`import`语句下方）：

~~~ .python
def draw_feature_shape_distractor(c, x, y):
    """在特征形状条件下绘制单个干扰物：一个与目标形状不同，但颜色不限的物体。

    参数
    ----------
    c: 画布
    x: int
    y: int
    """
    颜色 = ['黄色', '蓝色']
    color = random.choice(颜色)
    if 目标形状 == '圆形':
        形状 = '正方形'
    elif 目标形状 == '正方形':
        形状 = '圆形'
    else:
        raise Exception(f'无效的目标形状：{目标形状}')
    draw_shape(c, x, y, color=颜色, shape=形状)
~~~

这里发生了什么？我们…

- 随机选择颜色。
- 如果目标是圆形，选择正方形；如果目标是正方形，选择圆形。
- 如果`目标形状`既不是'圆形'也不是'正方形'，则引发`Exception`，防守式编程！
- 调用另一个函数`draw_shape()`，并指定要绘制的干扰物的颜色和形状。这假设有一个函数`draw_shape()`，尽管我们还没有定义它。

现在，我们在颜色特征条件下定义绘制干扰物的功能（在`import`语句下方）：

~~~ .python
def draw_feature_color_distractor(c, x, y):
    """在特征颜色条件下绘制单个干扰物：一个与目标颜色不同，但形状可任意的物体。

    参数
    ----------
    c: 画布
    x: int
    y: int
    """
    形状 = ['圆形', '正方形']
    shape = random.choice(形状)
    if 目标颜色 == '黄色':
        颜色 = '蓝色'
    elif 目标颜色 == '蓝色':
        颜色 = '黄色'
    else:
        raise Exception(f'无效的目标颜色：{目标颜色}')
    draw_shape(c, x, y, color=颜色, shape=形状)
~~~

这里发生了什么？我们…

- 随机选择形状。
- 如果目标是黄色，选择蓝色；如果目标是蓝色，选择黄色。
- 如果`目标颜色`既不是'黄色'也不是'蓝色'，则引发`Exception`，防守式编程！
- 调用另一个函数`draw_shape()`，并指定要绘制的干扰物的颜色和形状。这假设有一个函数`draw_shape()`，尽管我们还没有定义它。

__实现详细水平__

现在我们在细节上一步步深入，定义实际绘制图形到画布的函数（在`import`语句下方）：

~~~ .python
def draw_shape(c, x, y, color, shape):
    """画一个单独的形状。

参数
----------
c：画布
x：int
y：int
color：str
shape：str
"""
if shape == 'square':
    c += Rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=True)
elif shape == 'circle':
    c += Circle(x=x, y=y, r=25, color=color, fill=True)
else:
    raise Exception(f'无效形状：{shape}')
if color not in ['yellow', 'blue']:
    raise Exception(f'无效颜色：{color}')
~~~

这里发生了什么？我们...

- 检查应该绘制哪种形状。对于方形，我们在画布上加入一个 `Rect()` 元素。对于圆形，我们添加一个 `Circle()` 元素。
- 检查形状是否为方形或圆形，如果不是则引发一个 `Exception`。这是防御性编程的另一个例子！我们确保我们没有意外地指定了一个无效的形状。
- 检查颜色是否为黄色或蓝色，如果不是则引发一个 `Exception`。

__实现运行阶段__

由于我们在准备阶段已经完成了所有的硬件工作，因此运行阶段就是：

~~~ .python
c.show()
~~~

就这样！现在您已经绘制了完整的视觉搜索显示。而且，重要的是，你已经通过自顶向下的编程和防御性编程，以一种容易理解和安全的方式完成了这个过程。

## 步骤 7：定义正确的响应

为了知道参与者是否做出了正确的回应，我们需要知道正确的回应。你可以在*block_loop*中显式地定义这个（如初学者教程中所介绍的）；但是在这里我们将使用一个简单的Python脚本，检查目标是否存在，然后相应地定义正确的响应。

为此，在*trial_sequence*的开头插入一个新的INLINE_SCRIPT，并将其重命名为*correct_response_script*。在准备阶段（不是运行阶段！），输入以下代码：

~~~ .python
if target_present == 'present':
    correct_response = 'right'
elif target_present == 'absent':
    correct_response = 'left'
else:
    raise Exception(f'target_present应该是absent或present，而不是{target} ')
~~~

这里发生了什么？我们...

- 检查目标是否存在。如果目标存在，则正确响应为 'right' (右箭头键)；如果目标不存在，则正确响应为 'left' (左箭头键)。实验性（全局）变量 `correct_response` 会自动被 *keyboard_response* 识别；因此，我们不需要明确指出这个变量包含正确的响应。
- 检查目标是否存在或不存在，如果不是，引发一个 `Exception` - 防御性编程的又一个例子。

## 步骤 8: 提供每次实验反馈

每次实验后的反馈可以激励参与者；然而，每次实验的反馈不应干扰实验的进行。一种很好的提供每次实验反馈的方法是：在正确的响应之后简要地显示一个绿色的固定点，在错误的响应之后显示一个红色的固定点。

为此，请按照以下步骤操作：

- 在*trial_sequence*中，在*keyboard_response*之后插入两个新的SKETCHPAD。
- 将一个SKETCHPAD重命名为*green_dot*，在其上绘制一个中心绿色的固定点，并将其持续时间更改为500。
- 将另一个SKETCHPAD重命名为*red_dot*，在其上绘制一个中心红色的固定点，并将其持续时间更改为500。

当然，在每次实验中只应显示其中的一个点。为了实现这个目标，我们将在*trial_sequence*中指定运行-如果表达式：

- 将*green_dot*的运行-如果表达式更改为 'correct == 1'，表示它只应在正确的答案后显示。
- 将*red_dot*的运行-如果表达式更改为 'correct == 0'，表示它只应在错误的答案后显示。

如果变量 `correct_response` 可用，则变量 `正确` 会自动创建；这就是为什么我们在第 7 步定义 `correct_response` 的原因。有关变量和运行-如果语句的更多信息，请参阅：

- ％链接：手册/变量％

此时*trial_sequence*应与 %FigStep8 类似。

图：
 id：FigStep8
 source：step8.png
 caption：
  第8步结束时的*trial_sequence*。

## 完成！

恭喜，实验已经完成！您可以通过按蓝色双箭头按钮来进行测试运行（快捷键：`Ctrl+W`）。

如果实验第一次尝试时没有成功：不要担心，冷静地找出错误来自哪里。崩溃是正常开发过程的一部分。但是按照我们在本教程中所做的结构化工作，你可以节省大量的时间和头疼问题。

## 参考文献

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame：一个用于社会科学的开源图形化实验构建器。*行为研究方法*，*44*(2)，314-324。 doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). 注意的特征整合理论。*认知心理学*，12(1)，97–136。 doi:10.1016/0010-0285(80)90005-5

</div>

[参考文献]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html