<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __items__

`items`对象提供类似字典的访问方式来访问项目。它主要用于以编程方式执行项目。

实验开始时，将自动创建一个`items`对象。

除了以下列出的功能外，还支持以下语义：

__示例__

~~~ .python
# 以编程方式准备并运行一个sketchpad项目。
items.execute('my_sketchpad')
# 检查项目是否存在
if 'my_sketchpad' in items:
    print('my_sketchpad exists')
# 删除一个项目
del items['my_sketchpad']
# 浏览所有项目名称
for item_name in items:
    print(item_name)
~~~

[TOC]

## execute(name)

执行项目的运行和准备阶段，并更新项目堆栈。


__参数__

- **name**：项目名称。

__示例__

~~~ .python
items.execute('target_sketchpad')
~~~



## new(_type, name=None, script=None, allow_rename=True)

创建一个新项目。


__参数__

- **_type**：项目类型。
- **name**：项目名称，或为None以根据项目类型选择唯一名称。
- **script**：定义脚本，或为None以开始一个空白项目。
- **allow_rename**：指示OpenSesame是否可以使用与提供的“name”不同的名称，以避免重复名称等情况。

__返回值__

- 新生成的项目。

__示例__

~~~ .python
items.new('sketchpad', name='my_sketchpad')
items['my_sketchpad'].prepare()
items['my_sketchpad'].run()
~~~



## prepare(name)

执行项目的准备阶段，并更新项目堆栈。


__参数__

- **name**：项目名称。

__示例__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## run(name)

执行项目的运行阶段，并更新项目堆栈。


__参数__

- **name**：项目名称。

__示例__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## valid_name(item_type, suggestion=None)

生成一个有效且类似于期望名称的唯一名称。


__参数__

- **item_type**：要为其提供名称建议的项目类型。
- **suggestion**：期望的名称，或在类型下选择一个名称。

__返回值__

- 唯一的名称。

__示例__

~~~ .python
valid_name = items.valid_name('sketchpad', 'an invalid name')
~~~



</div>