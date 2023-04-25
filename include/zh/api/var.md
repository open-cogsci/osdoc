<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __var__

__从 4.0.0 开始__：从 OpenSesame 4.0 开始，所有实验变量也可以在 Python 工作区使用。这意味着你不再需要 `var` 对象了。

`var` 对象用于访问实验变量。实验变量是存在于图形界面(GUI)中的变量，并且通常在 LOOP 项目中设置为自变量，使用花括号（`{my_variable}`）表示法表示，并由 LOGGER 项目进行记录。

实验开始时会自动创建一个 `var` 对象。除了以下列出的功能外，还支持以下语义：

__示例__：

~~~ .python
# 设置一个实验变量
var.my_variable = u'my_value'
# 获取一个实验变量
print(u'受试者编号 = %d' % var.subject_nr)
# 删除(取消设置)实验变量
del var.my_variable
# 检查实验变量是否存在
if
u'my_variable' in var:
    print(u'my_variable 存在！')
# 遍历所有实验变量
for var_name in var:
        print(u'找到变量：%s' % var_name)
~~~

[TOC]

## clear(preserve=[])

*自 3.1.2 开始*

清除所有实验变量。

__参数__

- **preserve**：不清除的变量名列表。

__示例__

~~~ .python
var.clear()
~~~



## get(var, default=None, _eval=True, valid=None)

获取实验变量。

__参数__

- **var**：要检索的变量。
- **default**：对于不存在的变量的默认值，或者 `None`表示没有默认值。
- **_eval**：返回值是否要评估变量引用。
- **valid**：有效值的列表，或 `None` 允许所有值。

__示例__

~~~ .python
print('my_variable = %s' % var.get(u'my_variable'))
# 等同于：
print('my_variable = %s' % var.my_variable)
# 但如果你想传递关键字参数，则需要使用 `get()`：
var.get(u'my_variable', default=u'a_default_value')
~~~



## has(var)

检查实验变量是否存在。

__参数__

- **var**：要检查的变量。

__示例__

~~~ .python
if var.has(u'my_variable'):
        print(u'my_variable 已定义！')
# 等同于：
if u'my_variable' in var:
        print(u'my_variable 已定义！')
~~~



## inspect(self)

生成所有实验变量的描述，包括现有的和假设的。

__返回__

- 一个字典，其中变量名是键，值是具有源、值和存活键的字典。



## items(self)

返回 (variable_name, value) 元组的列表。请参阅 `var.vars()` 关于此功能的非详尽性说明。

__返回__

- 一个 (variable_name, value) 元组的列表。

__示例__

~~~ .python
for varname, value in var.items():
        print(varname, value)
~~~



## set(var, val)

设置实验变量。

__参数__

- **var**：要赋值的变量。
- **val**：要赋值的值。

__示例__

~~~ .python
var.set(u'my_variable', u'my_value')
# 等同于
var.my_variable = u'my_value'
~~~



## unset(var)

删除变量。

__参数__

- **var**：要删除的变量。

__示例__

~~~ .python
var.unset(u'my_variable')
# 等同于：
del var.my_variable
~~~



## vars(self)

返回实验变量的列表。由于实验变量可以存储在多个地方，因此此列表可能不是详尽无遗的。也就是说，`u'my_var' in var` 可能返回 `True`，尽管 u'my_var' 不在此功能返回的变量列表中。

__返回__

- 一个变量名的列表。

__示例__

~~~ .python
for varname in var.vars():
        print(varname)
~~~



</div>