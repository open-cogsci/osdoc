<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __clock__

`clock` 对象提供基本的时间函数。实验开始时将自动创建一个 `clock` 对象。

__示例__

~~~ .python
# 获取睡眠1000ms前后的时间戳
t0 = clock.time()
clock.sleep(1000)
t1 = clock.time()
time_passed = t1 - t0
print(f'这应该是1000: {time_passed}')
~~~

[TOC]

## loop_for(ms, throttle=None, t0=None)

*在 v3.2.0 中新增*

一个固定时间循环的迭代器。

__参数__

- **ms**：要循环的毫秒数。
- **throttle**：每次迭代之间的休眠周期。
- **t0**：起始时间。如果为“None”，起始时间为迭代开始时的时刻。

__返回__

- 

__示例__

~~~ .python
for ms in clock.loop_for(100, throttle=10):
    print(ms)
~~~



## once_in_a_while(ms=1000)

*在 v3.2.0 中新增*

周期性地返回 `True`。这主要用于执行应该偶尔执行的代码（例如在 `for` 循环中）。

__参数__

- **ms**：最小等待时间。

__返回__

- 如果自上次调用 `Clock.once_in_a_while()` 以来的最小等待时间已过，则返回 `True`，否则返回 `False`。

__示例__

~~~ .python
for i in range(1000000):
    if clock.once_in_a_while(ms=50):
        # 每50ms只执行一次该代码
        print(clock.time())
~~~



## sleep(ms)

睡眠（暂停）一段时间。

__参数__

- **ms**：要睡眠的毫秒数。

__示例__

~~~ .python
# 创建两个画布对象...
my_canvas1 = Canvas()
my_canvas1.text('1')
my_canvas2 = Canvas()
my_canvas2.text('2')
# ...并在1s间隔显示它们
my_canvas1.show()
clock.sleep(1000)
my_canvas2.show()
~~~



## time()

以毫秒为单位给出当前时间戳。时间戳的绝对含义（即何时为0）取决于后端。

__返回__

- 时间戳。

__示例__

~~~ .python
t = clock.time()
print(f'当前时间是 {t}')
~~~



</div>