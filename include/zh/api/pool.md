<div class="ClassDoc YAMLDoc" markdown="1">

# 实例 __pool__

`pool` 对象为文件池提供类似字典的访问方式。在检查文件池中的文件时，将搜索多个文件夹。
有关更多详细信息，请参阅 `pool.folders()`。

在实验启动时，将自动创建一个 `pool` 对象。

除了下面列出的函数以外，还支持以下语义：

__示范__

基本用法：

~~~ .python
# 获取文件池中文件的完整路径
print(f'img.png的完整路径是 {pool["img.png"]}')
# 检查文件是否在文件池中
if 'img.png' in pool:
    print('img.png在文件池中')
# 从文件池中删除文件
del pool['img.png']
# 遍历文件池中的所有文件。这将检索完整路径。
for path in pool:
    print(path)
# 检查文件池中的文件数量
print(f'文件池中有{len(pool)}个文件')
~~~

从文件池获取图像并使用`Canvas`显示它。

~~~ .python
image_path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(image_path)
my_canvas.show()
~~~

[TOC]

## add(path, new_name=None)

将文件复制到文件池。

__参数__

- **path**：磁盘上文件的完整路径。
- **new_name**：文件池中文件的新名称，或者为None以使用文件的原始名称。

__示范__

~~~ .python
pool.add('/home/username/Pictures/my_ing.png')
~~~



## clean_up(self)

删除文件池文件夹。




## fallback_folder(self)

回退文件池文件夹的完整路径，该文件夹为当前实验文件夹的`__pool__`子文件夹，如果此文件夹不存在，则返回`None`。回退文件池文件夹在与版本系统（如git）结合使用时很有用，因为即使文件池中有文件，也可以将实验保存为纯文本文件。



__返回__

- 

__示范__

~~~ .python
if pool.fallback_folder() is not None:
    print('存在回退文件池文件夹!')
~~~



## files(self)

返回文件池中的所有文件。

__返回__

- 全路径的列表。

__示范__

~~~ .python
for path in pool.files():
    print(path)
# 等效于：
for path in pool:
    print(path)
~~~



## folder(self)

返回（主）文件池文件夹的完整路径。这通常是一个临时文件夹，在实验完成时将其删除。

__返回__

- 主文件池文件夹的完整路径。

__示范__

~~~ .python
print(f'文件池文件夹位于：{pool.folder()}')
~~~



## folders(include_fallback_folder=True, include_experiment_path=False)

返回查找文件的完整路径时搜索的所有文件夹的列表。这些文件夹按顺序包括：

1. 文件池文件夹本身，由`pool.folder()`返回。
2. 当前实验的文件夹（如果存在）
3. 回退文件池文件夹，由`pool.fallback_folder()`返回（如果存在）

__参数__

- **include_fallback_folder**：如果回退文件池文件夹存在，是否包含回退文件池文件夹。
- **include_experiment_path**：如果实验文件夹存在，是否包含实验文件夹。

__返回__

- 所有文件夹的列表。

__示范__

~~~ .python
print('以下文件夹用于搜索文件：')
for folder in pool.folders():
    print(folder)
~~~



## in_folder(path)

检查路径是否在文件池文件夹中。这与`path in pool`语法不同的是，它仅检查主文件池文件夹，而不检查回退文件池文件夹和实验文件夹。

__参数__

- **path**：要检查的文件基本名称。

__返回__

- 

__示范__

~~~ .python
print(pool.in_folder('cue.png'))
~~~



## rename(old_path, new_path)

重命名文件池文件夹中的文件。

__参数__

- **old_path**：旧文件名。
- **new_path**：新文件名。

__示范__

~~~ .python
pool.rename('my_old_img.png', 'my_new_img.png')
~~~



## size(self)

获取文件池中所有文件的字节总大小。

__返回__

- 

__示范__

~~~ .python
print(f'文件池的大小是 {pool.size()} 字节')
~~~

</div>