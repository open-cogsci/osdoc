title: OpenSesame 3的重要变化
hash: 5ff5aa4ddc6076985d2733031a24955084f95edb98e5b60980505b16b020ae44
locale: zh
language: Chinese

[TOC]

## 3.3版的更改

OpenSesame 3.3带来了几个重大改进，使得开发实验更加容易。OpenSesame 3.3与3.2完全向后兼容。

### Rapunzel：一个新的代码编辑器

Rapunzel 是一个以Python和R的数字计算为重点的代码编辑器。从技术上讲，Rapunzel是OpenSesame的一组扩展。但它看起来和行为就像是一个独立的程序。编码愉快！

- <https://rapunzel.cogsci.nl/>

### 一个新的inline_script编辑器

关于Rapuznel的开发：INLINE_SCRIPT项目现在使用另一个库（`PyQode`）进行代码编辑。因此，代码编辑器现在支持您从现代代码编辑器中期望的许多功能，包括代码内省和静态代码检查。

### 更多颜色空间

OpenSesame现在原生支持HSV、HSL和CIElab颜色空间。

- %link:manual/python/canvas%

### 基于PsychoPy的新声音后端

现在默认后端是*psycho*。 此后端的一个优点是声音演示的时间应该更好。 如果您听到声音播放时的卡顿（点击音），您仍然可以回退到*psycho_legacy*后端，该后端使用旧的基于PyGame的声音系统。

### 支持在coroutines中的inline_script项目

您现在可以在`coroutines`中使用`inline_script`项目。 与使用自定义生成器函数的旧方法相比，这使得将Python脚本与coroutines结合起来更容易。

- %link:coroutines%

### OpenSesame： 

## 3.2版的更改

OpenSesame 3.2带来了几个重大改进，使得开发实验更加容易。OpenSesame 3.2与3.1完全向后兼容。

### 更好的，符合PEP-8的Python API

PEP-8是Python的风格指南。许多现代Python软件遵循PEP-8准则，但由于历史原因，OpenSesame没有。从3.2开始，公共API现在遵循这样的准则：类的名称（以及生成类的工厂函数）应为`CamelCase`，而对象和函数的名称应为`underscore_case`。实际上，这意味着您现在可以像这样创建`Canvas`对象：

~~~ .python
my_canvas = Canvas() # 注意大写字母C！
my_canvas.fixdot()
my_canvas.show()
~~~

当然，旧的`underscore_case`名称仍作为别名提供，因此保留了向后兼容性。

表单API也已简化。您不再需要导入`libopensesame.widgets`，也不需要将`exp`作为第一个参数传递：

~~~ .python
form = Form()
button = Button(text=u'Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### 图形板和画布的改进

#### 访问和修改Canvas元素

`Canvas`的元素现在是可以命名、访问和修改的对象。这意味着您不再需要重绘整个画布来更改单个元素。例如，您可以绘制一个旋转的手臂，如下所示：

~~~ .python
my_canvas = Canvas()
my_canvas['arm'] = Line(0, 0, 0, 0)
for x, y in xy_circle(n=100, rho=100):
    my_canvas['arm'].ex = x
    my_canvas['arm'].ey = y
    my_canvas.show()
    clock.sleep(10)
~~~

SKETCHPAD还允许您为元素命名。

有关更多信息，请参阅：

- %link:manual/python/canvas%

#### 改进了对HTML和非拉丁脚本的支持

现在通过Qt呈现文本，这是一个现代的库（也用于图形界面）。这意味着您现在可以在文本中使用真正的HTML。这也意味着从左到右的脚本和其他非拉丁脚本呈现得更好。

#### 图像可以旋转

现在可以旋转图像。这同时适用于SKETCHPAD项目和`Canvas`对象。

#### 使用极坐标

如果您右键单击SKETCHPAD元素，可以选择“指定极坐标”。这允许您根据极坐标计算笛卡尔（x，y）坐标，这在创建圆形配置时特别有用。

### 表单改进

#### 改进的表单性能

现在在使用* psycho *和* xpyriment * 后端时，表单的速度要快得多。这是因为现在可以单独更新`Canvas`元素。


#### 表单输入验证

您现在可以验证表单输入。也就是说，您可以阻止表单关闭，直到满足某些条件。此外，您可以排除来自`TextInput`小部件的输入字符。

有关更多信息，请参阅：

- %link:manual/forms/validation%


### 键盘改进

#### 支持键释放事件

`Keyboard()`对象现在有一个`get_key_release()`功能，允许您收集键释放。由于底层库的限制，该功能有两个重要的局限性：

- 在非QWERTY键盘布局上返回的`key`可能不正确
- *psycho*后端尚未实施该功能

有关更多信息，请参阅：

- %link:manual/response/keyboard%


### 鼠标改进

#### 支持鼠标释放事件

`Mouse()`对象现在有一个`get_click_release()`功能，允许您收集鼠标点击释放。当前尚未实施* psycho *后端的此功能。

有关更多信息，请参阅：

- %link:manual/response/mouse%

#### 使用sketchpads定义感兴趣区域

现在可以在`mouse_response`项目中定义链接的SKETCHPAD。如果您这样做，SKETCHPAD上的元素名称将自动用作鼠标点击的感兴趣区域（ROIs）。

### 强制结束您的实验

现在，您可以通过在主工具栏中单击Kill按钮强制结束实验。这意味着您不再需要打开进程/任务管理器来结束失控的实验！

### 改进的Mac OS支持

Mac OS包已从头开始重建，由%-- github: {user: dschreij} --％建立。Mac OS的体验现在应该更加顺畅，快速且不易崩溃。

### 土耳其文翻译

完整的土耳其文翻译已由% -- github: {user: aytackarabay} --％提交。这意味着OpenSesame现在完全翻译成法文，德文和土耳其文。其他几种语言也提供了部分翻译。


## 3.1版改进

OpenSesame 3.1带来了许多方便实验开发的改进。OpenSesame 3.1与3.0完全向后兼容。

### 新外观！

OpenSesame有一个新的图标主题，基于Sam Hewitt的[Moka](https://snwh.org/moka)。此外，用户界面已根据一致的人机界面指南进行重新设计。我们希望您喜欢我们喜欢的新外观！

### 重新设计的循环

现在使用LOOP更加简单，并允许您限制随机化；这使得可以防止相同的刺激连续两次出现。

有关更多信息，请参阅：

- %link:loop%

### 并行处理：并行执行事务

现在默认包含了COROUTINES插件。COROUTINES允许并行运行多个其他项目；这使得例如在呈现一系列SKETCHPAD时连续收集按键变得可能。

有关更多信息，请参阅：

- %link:coroutines%

### 开放科学框架集成

您现在可以登录[开放科学框架](http://osf.io)（OSF），并在计算机和OSF之间轻松同步实验和数据。感谢[开放科学中心](http://cos.io/)支持此功能！

有关更多信息，请参阅：

- %link:osf%

### 响应对象

有一个新的标准Python对象：`responses`。在实验过程中，它会跟踪收集的所有响应。

有关更多信息，请参阅：

- %link:responses%

## 3.0版的变化

OpenSesame 3.0带来了许多改进，使开发实验更加容易。大多数更改都是向后兼容的。也就是说，您仍可以使用旧方式进行操作。但是，有少数几个更改是不向后兼容的，了解它们非常重要。

### 向后不兼容的变化

#### 采样器属性

采样器(SAMPLER)对象有一些属性，这些属性以前是函数。这包括：

- `sampler.fade_in`
- `sampler.pan`
- `sampler.pitch`
- `sampler.volume`

有关更多信息，请参阅：

- %link:sampler%

####CSS3兼容的颜色

您现在可以使用CSS3兼容的颜色规格，如下所述：

- %link:manual/python/canvas%

如果您使用颜色名称（例如`red`，`green`等），这可能会导致颜色略有不同。例如，根据CSS3，`green`现在是`#008000`而不是之前的`#00FF00`。

### 新文件格式（.osexp）

OpenSesame现在以`.osexp`格式保存实验。当然，您仍然可以打开旧格式文件（`.opensesame`和`.opensesame.tar.gz`）。有关更多信息，请参阅：

- %link:fileformat%

### 简化的Python API

#### 不再需要self与exp

调用常用函数时，不再需要添加`self.`或`exp.`前缀。例如，以下示例将以编程方式将受试者编号设为2：

~~~ .python
set_subject_nr(2)
~~~

有关常用函数的列表，请参阅：

- %link:manual/python/common%

#### `var`对象：轻松获取和设置实验变量

使用`self.get()`获取和`exp.set()`设置实验变量的旧方法已被简化的语法替代。例如，设置变量`condition`，以便在SKETCHPAD等中使用`[condition]`表示它：

~~~ .python
var.condition = 'easy`'
~~~

要获得在循环（LOOP）中定义的实验变量`condition`，例如：

~~~ .python
print('Condition is %s' % var.condition)
~~~

有关更多信息，请参阅：

- %link:var%

#### `clock`对象：时间函数

现在可以通过`clock`对象使用时间函数：

~~~ .python
print('Current timestamp: %s' % clock.time())
clock.sleep(1000) # Sleep for 1 s
~~~

有关更多信息，请参阅：

- %link:clock%

#### `pool`对象：访问文件池

现在可以通过`pool`对象（支持类似“字典”（dict）的接口，但实际上并非真正的Python “字典”）访问文件池：

~~~ .python
path = pool['image.png']
print('The full path to image.png is: %s' % path)
~~~

有关更多信息，请参阅：

- %link:pool%

####不再需要从openexp.*导入*

不再需要导入`openexp`类，并将`exp`作为第一个参数传递。取而代之的是，要创建`canvas`对象，您可以简单地执行：

~~~ .python
my_canvas = canvas()
~~~

还有类似的工厂函数（如这些被称为的）用于`keyboard`，`mouse`和SAMPLER。

有关更多信息，请参阅：

- %link:manual/python/common%

#### 合成器现在成为采样器

合成器（SYNTH）不再作为一个独立的类。取而代之的是，它是一个返回已用合成样品填充的采样器（SAMPLER）对象的函数。

### 用户界面改进

#### IPython调试窗口

现在将IPython（用于科学计算的交互式Python终端）用于调试窗口。

#### 实时变量检查器

变量检查器现在在实验运行期间以及实验结束后显示您变量的实际值。

#### 撤消操作

您终于可以撤消操作了！

#### 新的颜色方案

默认颜色方案现在是 *Monokai*。与之前的默认方案*Solarized*相比，再次采用了暗色方案，但对比度更高。这增加了可读性并且看起来很好！

### 一致的坐标

以前，OpenSesame使用混合的、不一致的屏幕坐标：在使用Python代码时，`0,0`是显示屏的左上角，而在使用SKETCHPAD项目等时，`0,0`是显示屏的中心。从3.0开始，显示中心始终是`0,0`，也适用于Python代码。

如果您想切换回旧的行为，您可以在常规选项卡中禁用“统一坐标”选项。出于向后兼容性的考虑，在打开旧实验时会自动禁用“统一坐标”。

### 在文本字符串中使用Python

您现在可以使用`[=...]` 语法将Python嵌入到文本字符串中。例如，以下文本字符串在SKETCHPAD中：

~~~
两倍的二等于[=2*2]
~~~

... 将显示：

~~~
两倍的二等于4
~~~

有关详细信息，请参见：

- %link:text%

### 支持Python 3

OpenSesame现在支持Python >= 3.4。然而，OpenSesame的许多依赖项，特别是PsychoPy和Expyriment，仅支持Python 2。因此，Python 2.7仍然是Python的默认版本。