<div class="ClassDoc YAMLDoc" markdown="1">

# 类 __Mouse__

`Mouse` 类用于获取鼠标输入。您通常使用 `Mouse()` 工厂函数创建
`Mouse` 对象，将其描述在
章节[创建鼠标](#creating-a-mouse)中。

__示例__

~~~ .python
# 在点击鼠标按键之前绘制 '固定点鼠标光标'
my_mouse = Mouse()
my_canvas = Canvas()
while True:
    button, position, timestamp = my_mouse.get_click(timeout=20)
    if button is not None:
        break
    (x,y), time = my_mouse.get_pos()
    my_canvas.clear()
    my_canvas.fixdot(x, y)
    my_canvas.show()
~~~

[TOC]

## 需要了解的事项

### 创建鼠标

您通常使用 `Mouse()` 工厂函数创建一个 `Mouse`：

~~~ .python
my_mouse = Mouse()
~~~

或者，您可以将 [响应关键字](#response-keywords)传递给 `Mouse()`
以设置默认行为 ：

~~~ .python
my_mouse = Mouse(timeout=2000)
~~~

### 坐标

- 当将 *Uniform coordinates* 设置为 'yes' 时，坐标相对于显示器的中心，即 (0,0) 是中心。这是 OpenSesame 3.0.0 及以后的默认值。
- 当将 *Uniform coordinates* 设置为 'no' 时，坐标相对于显示器的左上角，即 (0,0) 是左上角。这是在 OpenSesame 2.9.X 和早期版本中的默认值。

### 按钮编号

鼠标按钮编号如下：

1. 左键
2. 中键
3. 右键
4. 向上滚动
5. 向下滚动

### 触摸屏

在使用触摸屏时，触摸会被注册为按钮 1（左键）。

### 响应关键词

接受 `**resp_args` 的函数接受以下关键字参数：

- `timeout` 指定毫秒单位的超时值，或设置为 `None` 以禁用超时。
- `buttonlist` 指定接受的按钮列表，或设置为 `None` 以接受所有钮。
- `visible` 表示在收集点击时鼠标光标是否变为可见（'True' 或 'False'）。要立即改变光标的可见性，请使用 `Mouse.show_cursor()`。

~~~ .python
# 获取左键或右键点击，超时为 3000 ms
my_mouse = Mouse()
button, time = my_mouse.get_click(buttonlist=[1,3], timeout=3000)
~~~

响应关键字仅影响当前操作（在创建对象时传递给
`Mouse()` 时除外）。要更改所有后续操作的行为，请直接设置响应属性 ：

~~~ .python
# 获取两个左键或右键按压，5000 ms 超时
my_mouse = Mouse()
my_mouse.buttonlist = [1,3]
my_mouse.timeout = 5000
button1, time1 = my_mouse.get_click()
button2, time2 = my_mouse.get_click()
~~~

或者在创建对象时将响应关键字传递给 `Mouse()` ：

~~~ .python
# 获取两个左键或右键按压，5000 ms 超时
my_mouse = Mouse(buttonlist=[1,3], timeout=5000)
button1, time1 = my_mouse.get_click()
button2, time2 = my_mouse.get_click()
~~~

## flush(self)

清除所有待处理的输入，而不仅仅限于鼠标。



__返回__

- 如果点击了一个按钮（即有东西可以刷新），则为 True ，否则为 False。

__示例__

~~~ .python
my_mouse = Mouse()
my_mouse.flush()
button, position, timestamp = my_mouse.get_click()
~~~



## get_click(\*arglist, \*\*kwdict)

收集鼠标点击。


__参数__

- **\*\*resp_args**：可选的 [响应关键字](#response-keywords)，将在此次调用 `Mouse.get_click()` 中使用。这种情况不影响
后续操作。

__返回__

- 一个 (button, position, timestamp) 元组。如果发生超时，按钮和位置为
`None`。位置是屏幕坐标中的 (x，y) 元组。

__示例__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click(timeout=5000)
if button is None:
        print('发生超时！')
~~~



## get_click_release(\*arglist, \*\*kwdict)

*New in v3.2.0*

收集鼠标点击释放。

*重要提示：* 当前尚未为
*psycho* 后端实现此功能。

__参数__

- **\*\*resp_args**：用于此次调用 `Mouse.get_click_release()` 的可选[响应关键词](#response-keywords)。这不影响后续操作。

__返回__

- 一个（按钮，位置，时间戳）元组。如果发生超时，按钮和位置为 `None`。位置是一个（x，y）元组，以屏幕坐标表示。

__示例__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click_release(timeout=5000)
if button is None:
        print('发生超时！')
~~~



## get_pos(self)

返回光标的当前位置。

__返回__

- 一个（位置，时间戳）元组。

__示例__

~~~ .python
my_mouse = Mouse()
(x, y), timestamp = my_mouse.get_pos()
print('光标位于（%d， %d）' % (x, y))
~~~



## get_pressed(self)

返回鼠标按钮的当前状态。True 值表示按钮当前被按下。

__返回__

- 一个（button1，button2，button3）布尔值元组。

__示例__

~~~ .python
my_mouse = Mouse()
buttons = my_mouse.get_pressed()
b1, b2, b3 = buttons
print('当前按下的鼠标按钮：（%d，%d，%d）' % (b1,b2,b3))
~~~



## set_pos(pos=(0, 0))

设置鼠标光标的位置。

__警告：__ `set_pos()` 是
不可靠的，在
某些系统上会无声失效。

__参数__

- **pos**：新鼠标坐标的（x，y）元组。

__示例__

~~~ .python
my_mouse = Mouse()
my_mouse.set_pos(pos=(0,0))
~~~



## show_cursor(show=True)

立即更改鼠标光标的可见性。

__注意：__
在大多数情况下，您将要使用 `visible`
关键字，这
在响应收集期间更改可见性，
即当
`mouse.get_click()` 被调用时。调用
`show_cursor()` 不会
隐式更改 `visible` 的值，
这可能导致
稍显不直观的行为，即光标
在 `get_click()` 被调用时隐藏。

__参数__

- **show**：指示光标显示（True）还是隐藏（False）。



## synonyms(button)

提供鼠标按钮的同义词列表。例如，1 和
'left_button' 是同义词。


__参数__

- **button**：按钮值。

__返回__

- 同义词列表。

</div>