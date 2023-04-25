<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __srbox__

如果在实验开始时插入srbox插件，SRBOX的实例会自动成为实验对象的一部分，
并且可以在 inline_script 项目中作为 SRBOX 访问。

__重要提示1：__

如果你不指定设备，插件将尝试自动检测
SR 盒子端口。然而，在某些系统上这会导致实验冻结，所以最好明确指定一个设备。

__重要提示2：__

您
需要在调用 [srbox.get_button_press] 之前调用 [srbox.start] 以将 SR 盒子置于发送模式，
以收集按键按下。

__示例：__
~~~ .python
t0 = clock.time()
srbox.start()
button, t1 = srbox.get_button_press(allowed_buttons=[1, 2],
                                    require_state_change=True)
if button == 1:
    response_time = t1 - t0
print(f'按钮 1 在 {response_time} 毫秒内被按下！')
srbox.stop()
~~~
[TOC]

## get_button_press(allowed_buttons=None, timeout=None, require_state_change=False)

从 SR 盒子收集按键按下。


__参数__

- **allowed_buttons**：接受的按钮列表或 'None' 以接受所有
按钮。有效按钮为 1 至 8 的整数。
- **timeout**：以毫秒为单位的超时值或 'None' 表示没有超时。
- **require_state_change    表示是否接受已经按下的按钮**: (False)，或者 是否只接受从未按下到按下的状态改变(True)。

__返回值__

- 一个 `(button_list, timestamp)` 元组。`button_list` 为 `None` 如果没有
按钮被按下（即发生了超时）。

## send(ch)

向 SR 盒子发送一个字符。发送'`'以关闭所有灯,'a'表示灯1开,'b'表示灯2开，'c'表示灯1和2都开等。

__参数__

- **ch**：要发送的字符。如果传递了 `str`，则使用 utf-8 编码将其编码为
`bytes`。

## start(self)

打开发送模式，使 SR 盒子开始发送输出。
当您调用
[srbox.get_button_press] 时，SR 盒子必须处于发送模式中。




## stop(self)

关闭发送模式，使 SR 盒子停止输出。

</div>