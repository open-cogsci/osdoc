<div class="ClassDoc YAMLDoc" markdown="1">

# 类 __Canvas__

{% set arg_max_width = "文本在换行前的最大像素宽度，" +
"或者为 `None` 以在屏幕边缘换行。" %}

{% set arg_bgmode = "指定背景是 col1 和 col2 的均值（'avg'，对应于典型的 Gabor patch），还是 " + 
"等于 col2（'col2'），适用于与背景融合。注意：此参数将被 psycho backend 忽略，该后端使用透明度递增来实现背景。" %}

{% set arg_style = "可选的[样式关键字](#style-keywords)，用于" + 
"指定当前绘图操作的样式。这不会影响后续的绘图操作。" %}

{% set arg_center = "一个布尔值，表示坐标描述的是" + 
"文本的中心（`True`）还是左上角（`False`）。" %}

`Canvas` 类用于呈现视觉刺激。你通常使用 `Canvas()` 工厂函数创建一个
`Canvas` 对象，如章节[创建画布](#creating-a-canvas)所述。

__示例__：

~~~ .python
# 创建并显示带有中心固定点的画布
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

__示例__：

你还可以将 `Canvas` 元素添加为对象。请参阅关于[命名、访问和修改元素](#naming-accessing-and-modifying-elements)的章节。

~~~ .python
# 创建一个带有固定点和矩形的画布
my_canvas = Canvas()
my_canvas['my_fixdot'] = FixDot()
my_canvas.show()
~~~

[TOC]

## 需要了解的事情

### 创建画布

您通常使用 `Canvas()` 工厂函数创建一个 `Canvas`：

~~~ .python
my_canvas = Canvas()
~~~

你还可以传递[样式关键字](#style-keywords) 给 `Canvas()`来设置
默认样式：

~~~ .python
my_canvas = Canvas(color='green')
my_canvas.fixdot() # 呈绿色
~~~

### 样式关键字

所有接受 `**style_args` 的函数采用以下关键字参数：

- `color` 指定前景颜色。有关有效的颜色规格，请参阅
  [colors](#colors)。
- `background_color` 指定背景颜色。有关有效的颜色规格，请参阅 [colors](#colors)。
- `fill` 标示矩形、圆形、多边形和椭圆是否
  填充（`True`），或者绘制轮廓（`False`）。
- `penwidth` 表示像素单位的笔宽，应为 `int` 或 `float`。
- `html` 表示是否解释 HTML 标签，应为 `True` 或
  `False`。
- `font_family` 是字体系列的名称，如 'sans'。
- `font_size` 是以像素为单位的字体大小。
- `font_italic` 表示文字是否斜体，应为 `True` 或
  `False`。
- `font_bold` 表示文字是否粗体，应为 `True` 或
  `False`。
- `font_underline` 表示文字是否带下划线，应为
  `True` 或 `False`。

~~~ .python
# 绘制绿色固定点
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
~~~

样式关键字只影响当前的绘图操作（创建 `Canvas` 时传递给
`Canvas()` 除外)。若要更改所有后续绘图操作的样式，请直接设置样式属性，例如 `canvas.color`：

~~~ .python
# 画一个红色 X 外形，笔宽为2px
my_canvas = Canvas()
my_canvas.color = 'red'
my_canvas.penwidth = 2
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

或者将样式属性传递给 `Canvas()`：

~~~ .python
# 画一个红色 X 外形，笔宽为2px
my_canvas = Canvas(color='red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

### 颜色

您可以通过以下方式指定颜色。这包括 CSS3 类型的颜色
规范，但还支持一些额外的规范，例如 CIE l* a*
b* 色空间。。

__版本说明:__ v3.3.0 中加入了 `hsv`、`hsl` 和 `lab` 色空间。

- __颜色名称：__ '红色'，'黑色'等。可以在[这里](http://www.w3.org/TR/SVG11/types.html#ColorKeywords)找到有效颜色名称的完整列表。
- __七个字符的十六进制字符串：__ `#FF0000`，`#000000`等。这里，值的范围从`00`到`FF`，因此`#FF0000`是亮红色。
- __四个字符的十六进制字符串：__ `#F00`，`#000`等。这里，值的范围从'0'到'F'，因此`#F00`是亮红色。
- __RGB字符串：__ `rgb(255,0,0)`，`rgb(0,0,0)`等。这里，值的范围从0到255，以使`rgb(255,0,0)`成为亮红色。
- __RGB百分比字符串：__ `rgb(100%,0%,0%)`，`rgb(0%,0%,0%)`等。这里，值的范围从0％到100％，使得`rgb(100%,0%,0%)`成为亮红色。
- __RGB元组：__ `(255, 0, 0)`，`(0, 0 ,0)`等。这里，值的范围为`0`至`255`，使得`(255,0,0)'成为亮红色。
- __HSV字符串：__ `hsv(120, 100%, 100%)`。在[HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)颜色空间中，色调参数是0到359之间的角度，饱和度和值参数是0％至100％的百分比。
- __HSL字符串：__ `hsl(120, 100%, 50%)`。在[HSL](https://en.wikipedia.org/wiki/HSL_and_HSV)颜色空间中，色调参数是0到359角度，饱和度和亮度参数是0％至100％的百分比。
- __LAB字符串：__ `lab(53, -20, 0)`。在[CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)颜色空间中，参数分别反映亮度（`l*`），绿红轴（`a*`，负为绿色），蓝黄轴（`b*`，负为蓝色）。这使用了D65白点和sRGB传输功能，如[此处](https://www.psychopy.org/_modules/psychopy/tools/colorspacetools.html)实施。
- __亮度值：__ `255`，`0`等。这里，值的范围从`0`到`255`，使得`255`是白色。

~~~ .python
# 指定绿色的各种方法
my_canvas.fixdot(color='green')  # 深绿色
my_canvas.fixdot(color='#00ff00')
my_canvas.fixdot(color='#0f0')
my_canvas.fixdot(color='rgb(0, 255, 0)')
my_canvas.fixdot(color='rgb(0%, 100%, 0%)')
my_canvas.fixdot(color='hsl(100, 100%, 50%)')
my_canvas.fixdot(color='hsv(0, 100%, 100%)')
my_canvas.fixdot(color='lab(53, -20, 0)')  # 深绿色
my_canvas.fixdot(color=(0, 255, 0))  # 指定亮度值（白色）
~~~

### 命名、访问和修改元素

从OpenSesame 3.2开始，`Canvas`支持基于对象的界面，允许您命名元素，并单独访问和修改元素，而无需重绘整个`Canvas`。

例如，以下操作首先将红色`Line`元素添加到`Canvas`并显示，然后将该线的颜色更改为绿色并再次显示，最后删除该线并再次显示画布（现在为空）。元素的名称（`my_line`）用于所有操作。

~~~ .python
my_canvas = Canvas()
my_canvas['my_line'] = Line(-100, -100, 100, 100, color='red')
my_canvas.show()
clock.sleep(1000)
my_canvas['my_line'].color = 'green'
my_canvas.show()
clock.sleep(1000)
del my_canvas['my_line']
my_canvas.show()
~~~

您还可以在不显式提供元素名称的情况下添加元素。这种情况下，名称将自动生成（例如`stim0`）。

~~~ .python
my_canvas = Canvas()
my_canvas += FixDot()
my_canvas.show()
~~~

如果您添加一个元素列表，它们将自动组合在一起，您可以按名称引用整个组。

~~~ .python
my_canvas = Canvas()
my_canvas['my_cross'] = [    Line(-100, 0, 100, 0),    Line(0, -100, 0, 100)]
my_canvas.show()
~~~

要检查特定的`x,y`坐标是否在元素的边界矩形内，可以使用`in`：

~~~ .python
my_mouse = Mouse(visible=True)
my_canvas = Canvas()
my_canvas['rect'] = Rect(-100, -100, 200, 200)
my_canvas.show()
button, (x, y), time = my_mouse.get_click()
if (x, y) in my_canvas['rect']:
    print('点击矩形内')
else:
    print('点击矩形以外')
~~~

您还可以使用`Canvas.elements_at()`函数获取包含`x,y`坐标的所有元素的名称列表，如下所述。

## arrow(sx, sy, ex, ey, body_length=0.8, body_width=0.5, head_width=30, \*\*style_args)

绘制箭头。箭头是由7个顶点组成的多边形，箭头指向(ex, ey)。

__参数__

- **sx**：箭头底部的X坐标。
- **sy**：箭头底部的Y坐标。
- **ex**：箭头尖端的X坐标。
- **ey**：箭头尖端的Y坐标。
- **body_length**：箭头主体相对于完整箭头的比例长度[0-1]。
- **body_width**：箭头主体相对于完整箭头的比例宽度（厚度）[0-1]。
- **head_width**：箭头头部的宽度（厚度）（像素）。

## circle(x, y, r, \*\*style_args)

绘制圆。

__参数__

- **x**：圆心的X坐标。
- **y**：圆心的Y坐标。
- **r**：圆的半径。
- **\*\*style_args**：{{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.circle(100, 100, 50, fill=True, color='red')
# 元素接口
my_canvas['my_circle'] = Circle(100, 100, 50, fill=True, color='red')
~~~



## clear(\*arglist, \*\*kwdict)

使用当前背景颜色清除画布。注意，对于每个实验显示，使用不同的画布通常比使用单个画布并反复清除和重绘更快。


__参数__

- **\*\*style_args**：{{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
clock.sleep(1000)
my_canvas.clear()
my_canvas.fixdot(color='red')
my_canvas.show()
~~~



## copy(canvas)

将当前`Canvas`变为传递的`Canvas`的副本。

__警告：__

复制`Canvas`对象可能导致不可预测的行为。在许多情况下，更好的解决方案是从头开始重新创建多个`Canvas`对象，和/或使用元素接口单独更新`Canvas`元素。

__参数__

- **canvas**：要复制的`Canvas`。

__示例__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(x=100, color='green')
my_copied_canvas = Canvas()
my_copied_canvas.copy(my_canvas)
my_copied_canvas.fixdot(x=200, color="blue")
my_copied_canvas.show()
~~~



## elements_at(x, y)

*在 v3.2.0 中新功能*

获取包含特定`x, y`坐标的元素的名称。

__参数__

- **x**：X坐标。
- **y**：Y坐标。

__返回__

- 包含坐标`x, y`的元素名称的`list`。

__示例__

~~~ .python
# 创建并显示一个画布，其中有两个部分重叠的矩形
my_canvas = Canvas()
my_canvas['right_rect'] = Rect(x=-200, y=-100, w=200, h=200, color='red')
my_canvas['left_rect'] = Rect(x=-100, y=-100, w=200, h=200, color='green')
my_canvas.show()
# 收集鼠标点击并打印包含点击点的元素的名称
my_mouse = Mouse(visible=True)
button, pos, time = my_mouse.get_click()
if pos is not None:
    x, y = pos
    print('Clicked on elements: %s' % my_canvas.elements_at(x, y))
~~~



## ellipse(x, y, w, h, \*\*style_args)

绘制椭圆。

__参数__

- **x**：左侧X坐标。
- **y**：顶部Y坐标。
- **w**：宽度。
- **h**：高度。
- **\*\*style_args**：{{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.ellipse(-10, -10, 20, 20, fill=True)
# 元素接口
my_canvas['my_ellipse'] = Ellipse(-10, -10, 20, 20, fill=True)
~~~



## fixdot(x=None, y=None, style='default', \*\*style_args)

绘制一个注视点。默认样式为中等-开放。

- 'large-filled' 是一个填充的圆，半径为16px。
- 'medium-filled' 是一个填充的圆，半径为8px。
- 'small-filled' 是一个填充的圆，半径为4px。
- 'large-open' 是一个半径为16px的填充圆，中心有一个2px的空洞。
- 'medium-open' 是一个半径为8px的填充圆，中心有一个2px的空洞。
- 'small-open' 是一个半径为4px的填充圆，中心有一个2px的空洞。
- 'large-cross' 是一个16px的十字形。
- 'medium-cross' 是一个8px的十字形。
- 'small-cross' 是一个4px的十字形。

__参数__

- **x**: 点中心的X坐标，或者为None以画出水平居中的点。
- **y**: 点中心的Y坐标，或者为None以画出垂直居中的点。
- **style**: 固定点的样式。其中之一：default, large-filled, medium-filled, small-filled, large-open, medium-open, small-open, large-cross, medium-cross, 或 small-cross。default 相当于 medium-open。
- **\*\*style_args**: {{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.fixdot()
# 元素接口
my_canvas['my_fixdot'] = FixDot()
~~~



## gabor(x, y, orient, freq, env='gaussian', size=96, stdev=12, phase=0, col1='white', col2='black', bgmode='avg')

绘制一个Gabor补丁。注意：Gabor补丁的精确渲染取决于后端。


__参数__

- **x**: 中心X坐标。
- **y**: 中心Y坐标。
- **orient**: 角度方向[0 .. 360]。表示从垂直开始的顺时针旋转。
- **freq**: 正弦波的周期（单位：px）。
- **env**: 用于确定补丁形状的包络。可以是"gaussian"（高斯），"linear"（线性），"circular"（圆形）或"rectangular"（矩形）。
- **size**: 以像素为单位的尺寸。
- **stdev**: 高斯的标准差（单位：像素）。仅适用于高斯包络。
- **phase**: 正弦波的相位 [0.0 .. 1.0]。
- **col1**: 用于表示峰值的颜色。
- **col2**: 用于表示波谷的颜色。注意：psycho后端会忽略这个参数，并总是使用`col1`的反色作为波谷。
- **bgmode**: {{arg_bgmode}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.gabor(100, 100, 45, .05)
# 元素接口
my_canvas['my_gabor'] = Gabor(100, 100, 45, .05)
~~~



## image(fname, center=True, x=None, y=None, scale=None, rotation=None)

从文件中绘制图像。此函数不会查找文件池，而是使用绝对路径。


__参数__

- **fname**: 图像的文件名。当使用Python 2时，这应为`unicode`或utf-8编码的`str`。当使用Python 3时，这应为`str`或utf-8编码的`bytes`。
- **center**: 一个布尔值，表示坐标是否表示中心 (True) 或左上角 (False)。
- **x**: X坐标，或`None`以画出水平居中的图像。
- **y**: Y坐标，或`None`以画出垂直居中的图像。
- **scale**: 图像的缩放因子。`None`或1表示原始尺寸。2.0表示200%的缩放，依此类推。
- **rotation**: 图像的旋转角度，`None`或0表示原始旋转。正值表示顺时针旋转的角度。

__示例__

~~~ .python
my_canvas = Canvas()
# 确定绝对路径：
path = exp.pool['image_in_pool.png']
# 函数接口
my_canvas.image(path)
# 元素接口
my_canvas['my_image'] = Image(path)
~~~



## line(sx, sy, ex, ey, \*\*style_args)

绘制一条线。


__参数__

- **sx**: 左侧X坐标。
- **sy**: 顶部Y坐标。
- **ex**: 右侧X坐标。
- **ey**: 底部Y坐标。
- **\*\*style_args**: {{arg_style}}


## lower_to_bottom(element)

将元素降低到底部，使其首先绘制；即，它变成背景。


__参数__

- **element**: 一个SKETCHPAD元素，或其名称。


## noise_patch(x, y, env='gaussian', size=96, stdev=12, col1='white', col2='black', bgmode='avg')

绘制一个带有包络的噪声块。噪声块的精确渲染取决于后端。


__参数__

- **x**：中心X坐标。
- **y**：中心Y坐标。
- **env**：确定贴片形状的封套。可以是 "高斯"、"线性"、"圆形"或"矩形"。
- **size**：像素尺寸。
- **stdev**：高斯的像素标准偏差。仅适用于高斯封套。
- **col1**：第一种颜色。
- **col2**：第二种颜色。请注意：psycho后端忽略此参数，始终使用`col1`的反色。
- **bgmode**：{{arg_bgmode}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.noise_patch(100, 100, env='circular')
# 元素接口
my_canvas['my_noise_patch'] = NoisePatch(100, 100, env='circular')
~~~



## polygon(vertices, \*\*style_args)

绘制由顶点列表定义的多边形。即由线连接的点构成的形状。


__参数__

- **vertices**：一个元组列表，每个元组对应一个顶点。例如，[(100,100), (200,100), (100,200)] 将绘制一个三角形。
- **\*\*style_args**：{{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
n1 = 0,0
n2 = 100, 100
n3 = 0, 100
# 函数接口
my_canvas.polygon([n1, n2, n3])
# 元素接口
my_canvas['my_polygon'] = Polygon([n1, n2, n3])
~~~



## prepare(self)

完成挂起的画布操作(如果有的话)，以便后续调用[canvas.show]非常快。只有在初始化`Canvas`时禁用了`auto_prepare`，才需要调用此函数。





## raise_to_top(element)

将元素提升到顶部，以使其最后绘制；也就是说，它成为前景。


__参数__

- **element**：一个SKETCHPAD元素或其名称。



## rect(x, y, w, h, \*\*style_args)

绘制矩形。


__参数__

- **x**：左侧X坐标。
- **y**：顶部Y坐标。
- **w**：宽度。
- **h**：高度。
- **\*\*style_args**：{{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.rect(-10, -10, 20, 20, fill=True)
# 元素接口
my_canvas['my_rect'] = Rect(-10, -10, 20, 20, fill=True)
~~~



## rename_element(old_name, new_name)

重命名元素。





## show(self)

在屏幕上显示或"翻转"画布。



__返回__

- 画布实际出现在屏幕上的时间的时间戳，或者如果精确的时间信息不可用，则返回最佳猜测。有关时间的详细信息，请参见</misc/timing>。根据后端，时间戳是`int`或`float`。

__示例__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
t = my_canvas.show()
exp.set('time_fixdot', t)
~~~



## text(text, center=True, x=None, y=None, max_width=None, \*\*style_args)

绘制文本。


__参数__

- **text**：一段文本字符串。在使用Python 2时，这应该是`unicode`或utf-8编码的`str`。在使用Python 3时，这应该是`str`或utf-8编码的`bytes`。
- **center**：{{arg_center}}
- **x**：X坐标，或为None以绘制水平居中的文本。
- **y**：Y坐标，或为None以绘制垂直居中的文本。
- **max_width**：{{arg_max_width}}
- **\*\*style_args**：{{arg_style}}

__示例__

~~~ .python
my_canvas = Canvas()
# 函数接口
my_canvas.text('这里有<b>粗体</b>和<i>斜体</i>的文字')
# 元素接口
my_canvas['my_text'] = Text('这里有<b>粗体</b>和<i>斜体</i>的文字')
~~~



## text_size(text, center=True, max_width=None, \*\*style_args)

确定以像素为单位的文本字符串大小。


__参数__

- **text**：一段文本字符串。
- **center**：{{arg_center}}
- **max_width**：{{arg_max_width}}
- **\*\*style_args**：{{arg_style}}

__返回__

- 一个(width, height)元组，包含文本字符串的尺寸。

__示例__

~~~ .python
my_canvas = Canvas()
w, h = my_canvas.text_size('一些文本')
~~~



</div>