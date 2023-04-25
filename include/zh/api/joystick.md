<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __joystick__

如果在实验开始时插入JOYSTICK插件，一个
JOYSTICK对象会自动成为实验对象的一部分
并且可以在INLINE_SCRIPT项目中用`joystick`引用。

{% set arg_joybuttonlist = "接受的按钮列表或" +
"`None` 以接受所有按钮。" %}
{% set arg_timeout = "以毫秒为单位的超时值或`None`代表无" +
"超时。" %}

[TOC]

## flush(self)

清除所有挂起的输入，不仅限于游戏手柄。



__返回__

- 如果有待处理的joyinput（即有内容需要清除），则返回 True；否则返回 False。


## get_joyaxes(timeout=None)

等待游戏手柄轴移动。


__参数__

- **timeout**：以毫秒为单位的超时值或`None`以使用默认超时。

__返回__

- 一个`(position, timestamp)` 元组。如果发生超时，`position`为`None`。否则，`position`是一个`(x, y, z)`元组。


## get_joyballs(timeout=None)

等待游戏手柄跟踪球移动。


__参数__

- **timeout**：以毫秒为单位的超时值或`None`以使用默认超时。

__返回__

- 一个`(position, timestamp)` 元组。如果发生超时，`position`为`None`。


## get_joybutton(joybuttonlist=None, timeout=None)

收集游戏手柄按键输入。


__参数__

- **joybuttonlist**：要接受的按钮的列表或`None`以使用默认的joybuttonlist。
- **timeout**：以毫秒为单位的超时值或`None`以使用默认超时。

__返回__

- 一个 (joybutton, timestamp) 元组。如果发生超时，joybutton 为`None`。


## get_joyhats(timeout=None)

等待游戏手柄帽子移动。


__参数__

- **timeout**：以毫秒为单位的超时值或`None`以使用默认超时。

__返回__

- 一个`(position, timestamp)` 元组。如果发生超时，`position`为`None`。否则，`position`是一个`(x, y)`元组。


## get_joyinput(joybuttonlist=None, timeout=None)

等待任何游戏手柄输入（按钮、轴、帽子或球）。


__参数__

- **joybuttonlist**：要接受的按钮的列表或`None`以使用默认的joybuttonlist。
- **timeout**：以毫秒为单位的超时值或`None`以使用默认超时。

__返回__

- 一个 (event, value, timestamp) 元组。如果发生超时，`value` 为`None`。`event`是 'None'，'joybuttonpress'，'joyballmotion'，'joyaxismotion' 或 'joyhatmotion'中的一个


## input_options(self)

生成一个列表，列出可用的按钮、轴、球和帽子的数量。



__返回__

- 一个输入数量的列表：[按钮，轴，球，
帽子]。


## set_joybuttonlist(joybuttonlist=None)

设置接受的按钮列表。


__参数__

- **joybuttonlist**：{{arg_joybuttonlist}}


## set_timeout(timeout=None)

设置超时。


__参数__

- **timeout**：{{arg_timeout}}


</div>