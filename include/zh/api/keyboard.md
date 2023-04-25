<div class="ClassDoc YAMLDoc" markdown="1">

# 类 __Keyboard__

`Keyboard` 类用于收集键盘响应。通常使用 `Keyboard()` 工厂函数创建一个 `Keyboard` 对象，如 [创建键盘](#creating-a-keyboard) 部分所述。

__示例__

~~~ .python
# 等待有一个 'z' 或 'x' 按键，超时时间为 3000 毫秒
my_keyboard = Keyboard(keylist=['z', 'x'], timeout=3000)
start_time = clock.time()
key, end_time = my_keyboard.get_key()
response = key
response_time = end_time - start_time
~~~

[TOC]

## 需要知道的事情

### 创建键盘

通常使用 `Keyboard()` 工厂函数创建一个 `Keyboard` :

~~~ .python
my_keyboard = Keyboard()
~~~

如果需要设置默认行为，还可以将 [Response keywords](#response-keywords) 传递给 `Keyboard()`

~~~ .python
my_keyboard = Keyboard(timeout=2000)
~~~

### 按键名称

- 在不同的后端，按键名称可能存在差异。
- 按键可以用字符或名称表示，并且不区分大小写。例如：
  - The key 'a' 可以表示为 'a' 和 'A'
  - 向上箭头可以表示为 'up' 和 'UP'
  - '/' 键可以表示为 '/', 'slash', 和 'SLASH'
  - 空格键可以表示为 'space' 和 'SPACE'
- 要找出按键的名称，你可以：
  - 单击 KEYBOARD_RESPONSE 项的 "列出可用按键" 按钮。
  - 使用 KEYBOARD_RESPONSE 项收集按键按压，并通过带有 "您按下了 [response]" 文本的 FEEDBACK 项显示按键名称。

### 响应关键词

接受 `**resp_args` 的函数可以使用以下关键字参数：

- `timeout` 指定毫秒为单位的超时值，或设置为 `None` 以禁用超时。
- `keylist` 指定接受的按键列表，或设置为 `None` 以接受所有按键。

~~~ .python
# 用 3000 毫秒超时获取左或右箭头按压
my_keyboard = Keyboard()
key, time = my_keyboard.get_key(keylist=[u'左', u'右'], timeout=3000)
~~~
  
响应关键词仅影响当前操作（除非传递给 `Keyboard()` ）。要更改所有后续操作的行为，请直接设置响应属性：

~~~ .python
# 用 5000 毫秒超时获取两个 A 或 B 键按压
my_keyboard = Keyboard()
my_keyboard.keylist = [u'a', u'b']
my_keyboard.timeout = 5000
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

或将响应选项传递给 [keyboard.__init__][__init__] :

~~~ .python
# 用 5000 毫秒超时获取两个 A 或 B 键按压
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

## flush(self)

清除所有待处理的键盘输入，不仅限于键盘。



__返回__

- 如果键已被按下（即，有东西要刷新），则返回 True，否则返回 False。


## get_key(\*arglist, \*\*kwdict)

收集单个按键按压。


__参数__

- **\*\*resp_args**: 可选的[响应关键词](#response-keywords)（`timeout` 和 `keylist`），将用于此次调用 `Keyboard.get_key()`。不影响后续操作。

__返回__

- 一个 `(key, timestamp)` 元组。如果发生超时，则 `key` 为 None。

__示例__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key(timeout=5000)
if response is None:
        print(u'发生了超时！')
~~~



## get_key_release(\*arglist, \*\*kwdict)

*自 v3.2.0 起*

收集单个按键释放。

*Important:* This
function currently assumes a QWERTY keyboard
layout (unlike
`Keyboard.get_key()`). This means that the returned
`key` may be
incorrect on non-QWERTY keyboard layouts. In addition,
this function is
not implemented for the *psycho* backend.

__参数__

- **\*\*resp_args**: 可选的[响应关键词](#response-keywords)（`timeout` 和 `keylist`），将用于此次调用 `Keyboard.get_key_release()`。不影响后续操作。

__返回__

- 一个 `(key, timestamp)` 元组。如果发生超时，`key` 为None。

__示例__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key_release(timeout=5000)
if response is None:
        print(u'发生超时！')
~~~



## get_mods(self)

返回当前按下的键盘修饰符（如shift、alt等）的列表。



__返回__

- 一个键盘修饰符列表。如果没有按下修饰符，则返回空列表。

__示例__

~~~ .python
my_keyboard = Keyboard()
moderators = my_keyboard.get_mods()
if u'shift' in moderators:
        print(u'按下了shift键！')
~~~



## show_virtual_keyboard(visible=True)

如果该后端支持的话，显示或隐藏虚拟键盘。仅当您希望在收集多字符响应时，虚拟键盘保持可见时，才需要此功能。否则，`Keyboard.get_key()` 将隐式地显示并隐藏单个字符响应的键盘。

对于不支持虚拟键盘的后端，此功能无效。

__参数__

- **visible**：如果应显示键盘，则为 True；否则为 False。

__示例__

~~~ .python
my_keyboard = Keyboard()
my_keyboard.show_virtual_keyboard(True)
response1, timestamp2 = my_keyboard.get_key()
response2, timestamp2 = my_keyboard.get_key()
my_keyboard.show_virtual_keyboard(False)
~~~



## synonyms(key)

为键提供一系列同义词，包括代码或名称。同义词包括所有变量作为类型和作为 Unicode 字符串（如果适用）。



__返回__

- 同义词列表


## valid_keys(self)

尝试猜测后端接受的键名。供内部使用。



__返回__

- 一个有效的键名列表。

</div>