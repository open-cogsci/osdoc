<div class="ClassDoc YAMLDoc" markdown="1">

## Canvas(auto_prepare=True, \*\*style_args)

一个创建新`Canvas`对象的工厂函数。有关可能的关键字说明，请参见:

- %link:manual/python/canvas%


__返回__

- 一个`Canvas`对象。

__示例__

~~~ .python
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~



## Experiment(osexp_path=None, log_path='defaultlog.csv', fullscreen=False, subject_nr=0, \*\*kwargs)

一个创建新`Experiment`对象的工厂函数。这仅在通过Python脚本实现实验时有用，
而不是通过用户界面。


__参数__

- **osexp_path**：如果指定了到`.osexp`文件的路径，则会打开该文件并且
只需通过调用`Experiment.run()`就可以运行。如果没有指定实验
文件，则会初始化一个空实验。
- **log_path**：
- **fullscreen**：
- **subject_nr**：
- **kwargs**：可选的关键字参数，用作实验变量。主要是通过
`canvas_backend`关键字指定后端。

__返回__

- 一个形如 (exp, win, clock, log) 的元组，对应于实验、
窗口句柄（特定于后端）、Clock 和 Log 对象。

__示例__

要完全以程序方式实现实验：

~~~ .python
from libopensesame.python_workspace_api import (
    Experiment, Canvas, Text, Keyboard)
exp, win, clock, log = Experiment(canvas_backend='legacy')
c = Canvas()
c += Text('Press any key')
c.show()
kb = Keyboard()
kb.get_key()
exp.end()
~~~

要加载实验文件并运行它：

~~~ .python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
~~~



## Form(\*args, \*\*kwargs)

一个创建新`Form`对象的工厂函数。有关可能的关键字说明，请参见：

- %link:manual/forms/widgets%


__返回__

- 一个`Form`对象。

__示例__

~~~ .python
form = Form()
label = Label(text='label')
button = Button(text='Ok')
form.set_widget(label, (0,0))
form.set_widget(button, (0,1))
form._exec()
~~~



## Keyboard(\*\*resp_args)

一个创建新`Keyboard`对象的工厂函数。有关可能的关键字说明，请参见：

- %link:manual/python/keyboard%


__返回__

- 一个`Keyboard`对象。

__示例__

~~~ .python
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key, time = my_keyboard.get_key()
~~~



## Mouse(\*\*resp_args)

一个创建新`Mouse`对象的工厂函数。有关可能的关键字说明，请参见：

- %link:manual/python/mouse%


__返回__

- 一个`mouse`对象。

__示例__

~~~ .python
my_mouse = Mouse(keylist=[1,3], timeout=5000)
button, time = my_mouse.get_button()
~~~



## Sampler(src, \*\*playback_args)

一个创建新`Sampler`对象的工厂函数。有关可能的关键字说明，请参见：

- %link:manual/python/sampler%


__返回__

- 一个SAMPLER对象。

__示例__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~



## Synth(osc='sine', freq=440, length=100, attack=0, decay=5)

一个合成声音并将其作为一个`Sampler`对象返回的工厂函数。


__参数__

- **osc**：振荡器，可以是 "sine"，"saw"，"square"或 "white_noise"。
- **freq**：频率，可以是整数值（赫兹值）或字符串（"A1"，
"eb2"等）。
- **length**：声音的长度，以毫秒为单位。
- **attack**：以毫秒为单位的起始（渐入）时间。
- **decay**：以毫秒为单位的衰减（渐出）时间。

__返回__

- 一个SAMPLER对象。

__示例__

~~~ .python
my_sampler = Synth(freq=u'b2', length=500)
~~~



## copy_sketchpad(name)

返回`sketchpad`画布的副本。


__参数__

- **name**：`sketchpad`的名称。

__返回__

- `sketchpad`画布的副本。

__示例__

~~~ .python
my_canvas = copy_sketchpad('my_sketchpad')
my_canvas.show()
~~~



## pause()

暂停实验。



## register_cleanup_function(fnc)

注册一个清理函数，该函数在实验结束时执行。清理函数在显示器、声音设备和日志文件关闭后执行。实验崩溃时也会执行清理函数。



__示例__

~~~ .python
def my_cleanup_function():
        print(u'实验已完成！')
register_cleanup_function(my_cleanup_function)
~~~



## reset_feedback()

将所有反馈变量重置为初始状态。



__示例__

~~~ .python
reset_feedback()
~~~



## set_subject_nr(nr)

设置受试者号码和奇偶性。启动实验时会自动调用此功能，因此您只需要在覆盖启动实验时指定的受试者号码时自己调用它。


__参数__

- **nr**: 受试者号码。

__示例__

~~~ .python
set_subject_nr(1)
print('受试者号码 = %d' % var.subject_nr)
print('受试者奇偶性 = %s' % var.subject_parity)
~~~



## sometimes(p=0.5)

以一定的概率返回True。 (更高级的随机化，请使用Python `random`模块。)


__参数__

- **p**: 返回True的概率。

__返回__

- True 或 False

__示例__

~~~ .python
if sometimes():
        print('有时你赢')
else:
        print('有时你输')
~~~



## xy_circle(n, rho, phi0=0, pole=(0, 0))

生成圆中的一系列点（x,y坐标）。这可以用于以圆形排列绘制刺激物。


__参数__

- **n**: 要生成的x,y坐标的数量。
- **rho**: 第一个点的径向坐标，距离或偏心距。
- **phi0**: 第一个坐标的角坐标。这是逆时针旋转的度数（即不是弧度），0为正右方。
- **pole**: 参考点。

__返回__

- 一个（x,y）坐标元组列表。

__示例__

~~~ .python
# 在中心固定点周围绘制8个矩形
c = Canvas()
c.fixdot()
for x, y in xy_circle(8, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_distance(x1, y1, x2, y2)

给出两点之间的距离。


__参数__

- **x1**: 第一个点的x坐标。
- **y1**: 第一个点的y坐标。
- **x2**: 第二个点的x坐标。
- **y2**: 第二个点的y坐标。

__返回__

- 两点之间的距离。



## xy_from_polar(rho, phi, pole=(0, 0))

将极坐标（距离，角度）转换为笛卡尔坐标（x, y）。


__参数__

- **rho**: 径向坐标，距离或偏心距。
- **phi**: 角坐标。这是度数（即非弧度）中的顺时针旋转，0为正右方。
- **pole**: 参考点。

__返回__

- 一个 (x, y) 坐标元组。

__示例__

~~~ .python
# 绘制一个十字形
x1, y1 = xy_from_polar(100, 45)
x2, y2 = xy_from_polar(100, -45)
c = Canvas()
c.line(x1, y1, -x1, -y1)
c.line(x2, y2, -x2, -y2)
c.show()
~~~



## xy_grid(n, spacing, pole=(0, 0))

生成网格中的一系列点（x,y坐标）。这可以用于以网格形式绘制刺激物。


__参数__

- **n**: 一个`int`，表示列数和行数，例如`n=2`表示2x2网格，或者一个(n_col, n_row)元组，例如`n=(2,3)`表示2x3网格。
- **spacing**: 一个数字值，表示单元格之间的间距，或者一个(col_spacing, row_spacing)元组。
- **pole**: 参考点。

__返回__

- 一个 (x,y) 坐标元组列表。

__示例__

~~~ .python
# 绘制一个4x4矩形网格
c = Canvas()
c.fixdot()
for x, y in xy_grid(4, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_random(n, width, height, min_dist=0, pole=(0, 0))

生成具有最小间距的随机点列表（x，y坐标），间距为每对点之间的间距。当无法生成坐标列表时，此函数会引发异常，这通常是因为点太多，min_dist设置得太高，或者宽度或高度设置得太低。

__参数__

- **n**：要生成的点的数量。
- **width**：随机点场的宽度。
- **height**：随机点场的高度。
- **min_dist**：每个点之间的最小距离。
- **pole**：参考点。

__返回__

- 一个（x，y）坐标元组列表。

__示例__

~~~ .python
# 在随机网格中绘制50个矩形
c = Canvas()
c.fixdot()
for x, y in xy_random(50, 500, 500, min_dist=40):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_to_polar(x, y, pole=(0, 0))

将笛卡尔坐标（x，y）转换为极坐标（距离，角度）。

__参数__

- **x**：X坐标。
- **y**：Y坐标。
- **pole**：参考点。

__返回__

- 一个（rho，phi）坐标元组。在这里，`rho`是径向坐标，也是距离或离心率。`phi`是以度为单位的角坐标（即非弧度），反映逆时针旋转，其中0是直接向右。

__示例__

~~~ .python
rho, phi = xy_to_polar(100, 100)
~~~



</div>