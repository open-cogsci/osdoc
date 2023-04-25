<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __log__

`log` 对象提供数据记录功能。实验开始时会自动创建一个 `log` 对象。

__示例__

~~~ .python
# 写入一行文本
log.write('我的自定义日志信息')
# 写入所有变量
log.write_vars()
~~~

[TOC]

## close(self)

关闭当前日志。



__示例__

~~~ .python
log.close()
~~~



## open(path)

打开当前日志。如果日志已经打开，它会被自动关闭并重新打开。


__参数__

- **path**：当前日志文件的路径。在大多数情况下（除非）使用自定义日志后端，这将是一个文件名。

__示例__

~~~ .python
# 打开一个新日志
log.open('/path/to/new/logfile.csv')
~~~



## write(msg, newline=True)

将一条信息写入日志。


__参数__

- **msg**：文本消息。在使用 Python 2 时，这应该是 `unicode` 或 utf-8 编码的 `str`。在使用 Python 3 时，这应该是 `str` 或 utf-8 编码的 `bytes`。
- **newline**：指定在消息后面是否写入换行符。

__示例__

~~~ .python
# 写入单个字符串文本
log.write(f'time = {clock.time()}')
~~~



## write_vars(var_list=None)

将变量写入日志。


__参数__

- **var_list**：要写入的变量名列表，如果为 None，则写入实验中存在的所有变量。

__示例__

~~~ .python
# 将所有变量写入日志文件
log.write_vars()
~~~



</div>