title: 关于Python
hash: f909cf66bfb509985a9c3a131043cd177b0810ba2e22a2faacbe879979114123
locale: zh
language: Chinese

在OpenSesame中，您可以仅使用图形用户界面（GUI）来创建复杂的实验。但有时您会遇到GUI所提供的功能不足的情况。在这些情况下，您可以向实验中添加Python代码。

在OSWeb的在线实验中不支持Python。如果您需要在线运行实验，您必须使用[JavaScript](%url:manual/javascript/about%)。

[TOC]

## 学习Python

您可以在 <https://pythontutorials.eu/> 找到一组基本教程和练习，帮助您开始学习Python。

## OpenSesame的图形用户界面中的Python

### 单个Python工作区

所有Python代码在单个Python工作区中执行。这意味着在一个INLINE_SCRIPT中定义的变量在所有其他INLINE_SCRIPT中以及内嵌在运行-如果语句和文本字符串中的Python语句中都是可以访问的。同样的原则适用于模块：一旦导入，它们就随处可用。

例如，您可以在一个 INLINE_SCRIPT 中构建`Canvas`...

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
~~~

... 并在另一个 INLINE_SCRIPT 中显示它...

~~~ .python
my_canvas.show()
~~~

### Inline_script项目

要在实验中使用Python代码，需要向实验中添加一个INLINE_SCRIPT项目。您可以通过将Python图标（蓝/黄图标）从项目工具栏拖放到实验序列中来实现这一点。完成此操作后，您将看到类似于 %FigInlineScript的内容。

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: INLINE_SCRIPT项目。
--%

可以看到，INLINE_SCRIPT项目有两个选项卡：一个用于准备阶段，另一个用于运行阶段。首先执行准备阶段，以便项目为时间关键的运行阶段做准备。在准备阶段构造`Canvas`对象、`Sampler`对象等是一种良好的实践，这样它们就可以在运行阶段无延迟地呈现。但这仅是约定，两个阶段都可以执行任意Python代码。

有关准备-运行策略的更多信息，请参见：

- %link:prepare-run%

### 条件（"if"）表达式

您可以在条件表达式中使用单行Python表达式。例如，您可以将以下Python脚本用作运行-如果表达式（另请参见%FigRunIf）：

~~~ .python
correct == 1 and response_time < 1000
~~~

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: 在SEQUENCE项目的运行-if语句中使用Python脚本。
--%

有关条件（"if"）表达式的更多信息，请参见：

- %link:manual/variables%

### 文本字符串中的Python

您可以使用{...}语法在文本字符串中嵌入Python语句。这适用于简单的变量引用，还适用于单行表达式。例如，您可以将以下文本添加到SKETCHPAD中：

```text
分辨率为{width} x {height} px，共计{width * height}像素
```

根据您的实验分辨率，这可能会被计算为：

```text
分辨率为1024 x 768 px，共786432像素
```

有关变量和文本的更多信息，请参见：

- %link:manual/variables%
- %link:manual/stimuli/text%

### Jupyter控制台（调试窗口）

OpenSesame将标准输出重定向到控制台（或：调试窗口），您可以通过Control + D或通过菜单（菜单->查看->显示调试窗口；请参阅%FigDebugNormal）激活控制台。您可以使用`print()`打印到控制台。

~~~ .python
print('这将显示在调试窗口中！')
~~~

控制台还是一个由[project Jupyter](https://jupyter.org)提供支持的交互式Python解释器。

## 了解的事情

### 常用函数

许多常用函数可以直接在INLINE_SCRIPT项目中使用，无需导入任何内容。例如：

~~~ .python
# `Canvas()`是一个工厂函数，返回一个`Canvas`对象
fixdot_canvas = Canvas()
if sometimes(): # 有时修正点是绿色的
    fixdot_canvas.fixdot(color='green')
else: # 有时它是红色的
    fixdot_canvas.fixdot(color='red')
fixdot_canvas.show()
~~~

如需常用函数的列表，参见：

-%link:manual/python/common%


### `var`对象：访问实验变量

__版本说明__从OpenSesame 4.0版本开始，所有实验变量都作为全局变量可用。这意味着你不再需要`var`对象。
{:.page-notification}

你可以通过`var`对象来访问实验变量：

~~~ .python
# OpenSesame <= 3.3（带var对象）
# 获取实验变量
print('my_variable is: %s' % var.my_variable)
# 设置实验变量
var.my_variable = 'my_value'

# OpenSesame >= 4.0（不带var对象）
# 获取实验变量
print('my_variable is: %s' % my_variable)
# 设置实验变量
my_variable = 'my_value'
~~~

`var`对象的完整概览可以在此处找到：

-%link:manual/python/var%


### `clock`对象：时间函数

基本的时间函数通过`clock`对象可以利用：

~~~ .python
# 获取当前的时间戳
t = clock.time()
# 等待1秒
clock.sleep(1000)
~~~

`clock`对象的完整概览可以在此处找到：

-%link:manual/python/clock%


### `log`对象：数据记录

数据记录通过`log`对象可以利用：

~~~ .python
# 写一行文本
log.write('My custom log message')
# 写入所有变量
log.write_vars()
~~~

`log`对象的完整概览可以在此处找到：

-%link:manual/python/log%


### `pool`对象：访问文件池

你可以通过`pool`对象获取文件池中文件的完整路径：

~~~ .python
# 显示文件池中的一个图片
path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(path)
my_canvas.show()
~~~

`pool`对象的完整概览可以在此处找到：

-%link:manual/python/pool%


### `responses`对象：访问参与者响应

`responses`对象记录了实验过程中收集的所有参与者响应。例如，列出迄今为止所有响应的正确性：

~~~ .python
for response in responses:
	print(response.correct)
~~~

`responses`对象的完整概览可以在此处找到：

-%link:manual/python/responses%


### `Canvas`类：呈现视觉刺激

`Canvas`类用于呈现视觉刺激。例如，你可以按以下方式显示一个固定点：

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

`Canvas`类的完整概览可以在此处找到：

-%link:manual/python/canvas%


### `Keyboard`类：收集按键操作

`Keyboard`类用于收集按键操作。例如，收集一个具有1000毫秒超时的按键操作：

~~~ .python
my_keyboard = Keyboard(timeout=1000)
key, time = my_keyboard.get_key()
~~~

`Keyboard`类的完整概览可以在此处找到：

-%link:manual/python/keyboard%


### `Mouse`类：收集鼠标点击和屏幕触摸

`Mouse`类用于收集鼠标点击和屏幕触摸。(OpenSesame在两者之间不做区分。)例如，收集一个具有1000毫秒超时的鼠标点击：

~~~ .python
my_mouse = Mouse(timeout=1000)
button, position, time = my_mouse.get_click()
~~~

`Mouse`类的完整概览可以在此处找到：

-%link:manual/python/mouse%


### `Sampler`类：声音播放

`Sampler`类用于播放声音样本。例如，播放一个简单的蜂鸣声：

~~~ .python
my_sampler = Sampler()
my_sampler.play()
~~~

`Sampler`类的完整概览可以在此处找到：

-%link:manual/python/sampler%


## 显示表现、响应收集等的替代模块


### `psychopy`

如果您正在使用*psycho* 后端，您可以直接使用各种 [PsychoPy] 模块。更多信息请查阅：

- ％link:backends％


### `expyriment`

如果您正在使用 *xpyriment* 后端，您可以直接使用各种 [Expyriment] 模块。更多信息请查阅：

- ％link:backends％

### `pygame`

如果您正在使用 *legacy*，*droid*，或 *xpyriment* (仅在 "Use OpenGL" 设置为 "no" 时)后端，您可以直接使用各种 [PyGame] 模块。更多信息请查阅：

- ％link:backends％


[python]: http://www.python.org/
[backends]: /backends/about-backends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org/
[pygame]: http://www.pygame.org/