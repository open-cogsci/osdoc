title: 循环和独立变量
hash: f52d2b6f370a4abedc40605527622cea0ff9e57163ef51e6d8d4e39ff35789ec
locale: zh
language: Chinese

LOOP 项目有两个重要功能：

- 它可以多次运行另一个项目。
- 通常在此处定义您的实验中要操纵的自变量。

[TOC]

## 要运行的项目

LOOP 总是连接到单个其他项目：要运行的项目。您可以在标有 "Run" 的框中选择要运行的项目。 在大多数情况下，要运行的项目是 SEQUENCE ，它按顺序运行多个项目。

两个常见的SEQUENCE-LOOP结构是：

- 如果SEQUENCE对应于单个试验（通常称为 *trial_sequence*），则连接到此序列的LOOP对应于多个试验或块（通常称为 *block_loop*）。
- 如果SEQUENCE对应于经过反馈显示的试验块（通常称为 *block_sequence*），则连接到此序列的循环对应于多个块或完整的实验会话（通常称为 *experimental_loop*）。

## 定义自变量

循环表是定义自变量的简便强大方法。 表中的每一列都对应一个变量；每行对应一个周期，即变量的一个程度。 例如，一个简单的循环有一个变量（`animal`），它有两个周期（"cat" 和 "dog"），如下所示：

animal |
------ |
cat    |
dog    |

循环具有一些重要选项：

*Repeat* 表示每个周期应执行多少次。在上面的示例中，重复次数设置为2，这意味着当变量 `animal` 的值为 "cat" 时，将调用两次 *trial_sequence*；当 `animal` 的值为 "dog" 时也会调用两次（总共四次）。

*Order* 表示周期应按顺序执行还是按随机顺序执行。 随机化是完整的，也就是说，对所有周期 × 重复次数的试验列表都进行了随机化。

## 从文件中读取自变量

如果您要从文件中读取自变量，而不是将它们输入到循环表中，可以按以下步骤操作：

- 将 *Source* 设置为 *file*。
- 在 *File* 条目中选择一个 Excel（`.xlsx`）或 CSV（`.csv`）文件。

来源文件遵循与循环表相同的约定；即，每列对应一个变量，每行对应一个周期。

CSV 文件应符合以下格式：

- 纯文本
- 逗号分隔
- 双引号（用反斜杠转义字面上的双引号）
- UTF-8 编码

## 中断循环

如果您要在执行所有周期之前中断循环，可以指定一个中断表达式。此中断表达式遵循与其他条件表达式相同的语法，详见：

- %link:manual/variables%

例如，以下 break-if 语句会在给出正确答案后立即中断循环：

```python
correct == 1
```

*Evaluate on first cycle* 选项指示 break-if 语句是在第一个周期之前进行评估，这样可能一个周期也不会执行，还是仅在第二个周期之前进行评估，这样至少会执行一个周期。 在某些情况下，break-if 语句将引用仅在第一个周期之后定义的变量，在这种情况下，为避免出现 'Variable does not exist' 错误，您应禁用 'Evaluate on first cycle' 选项。

## 生成满因子设计

通过点击 *Full-factorial design*，您可以打开一个向导，用于轻松生成满因子设计，即每个因子组合都出现的设计。

## 伪随机化

您可以在循环项的脚本中添加伪随机化约束。 即使Order 设置为顺序，这也会洗牌行。（目前，这还不能通过GUI完成。）

示例：确保相同单词的重复（由 `word` 变量给定）之间至少间隔 4 个周期：

```python
constrain word mindist=4
```

示例：确保不重复相同的单词：

```python
constrain word maxrep=1
```

`constrain`命令必须在`setcycle`命令*之后*。

## 高级循环操作

高级循环操作的命令必须在`constrain`和`setcycle`命令之后。

### fullfactorial

`fullfactorial`指令将循环表视为全因子设计的输入。例如，以下循环表：

提示  | 时长
----- | --------
左    | 0
右    | 100
      | 200

将得到：

提示  | 时长
----- | --------
左    | 0
左    | 100
左    | 200
右    | 0
右    | 100
右    | 200

### shuffle

`shuffle`无参数会随机整个表格。当指定列名时（`shuffle cue`），只对该列进行随机化。

### shuffle_horiz

`shuffle_horiz`水平地洗牌所有列。当指定多个列时，仅对这些列进行水平洗牌。

例如，将`shuffle_horiz word1 word2`应用于以下表格：

word1 | word2 | word3
----- | ----- | -----
cat   | dog   | bunny
cat   | dog   | bunny
cat   | dog   | bunny

结果可能是（即在`word1`和`word2`之间随机交换值，但不对`word3`进行操作）：

word1 | word2 | word3
----- | ----- | -----
dog   | cat   | bunny
dog   | cat   | bunny
cat   | dog   | bunny

### slice

`slice [from] [to]`从循环中选择一个切片。它需要一个起始索引和一个结束索引，其中0是第一行，负值是从后向前计数。(换句话说，就像在Python中的列表切片一样。)

例如，将`slice 1 -1`应用于以下表格：

word  |
----- |
cat   |
dog   |
bunny |
horse |

结果将是：

word  |
----- |
dog   |
bunny |

### sort

`sort [column]`排序单个列，而不改变其他列。

### sortby

`sortby [column]`根据单个列对整个表格进行排序。

### reverse

`reverse`反转整个表格的顺序。如果指定了列名（例如`reverse word`），只反转该列，而不改变其他列。

### roll

`roll [value]`将整个表格向前（对于正值）或向后（对于负值）滚动。如果指定了列名（例如`roll 1 word`），则只滚动该列，而不改变其他列。

例如，如果将`roll 1`应用于以下表格：

word  |
----- |
cat   |
dog   |
bunny |
horse |

结果将是：

word  |
----- |
horse |
cat   |
dog   |
bunny |

### weight

`weight [column]`根据指定列中的权重值重复每一行。

例如，如果将`weight w`应用于以下表格：

word  | w
----- | -
cat   | 0
dog   | 0
bunny | 2
horse | 1

结果将是：

word  | w
----- | -
bunny | 2
bunny | 2
horse | 1

## 预览循环

如果您已经设定了约束条件，或者使用了高级循环操作，则应检查结果是否符合预期。要这样做，您可以生成循环表格的预览，以便在运行实验时查看将要出现的（或在随机化情况下可能出现的）内容。

要生成预览，请点击*预览*按钮。

## 在Python内联脚本中访问循环表格

原始的LOOP表，就像您在OpenSesame用户界面中看到的那样，是一个名为`dm`的[`DataMatrix`](http://datamatrix.cogsci.nl/)对象，是LOOP项目的属性。

这个原始的LOOP表通常会以各种方式进行转换；例如，行的顺序可以进行随机化，行可以多次重复。转换后的LOOP同样是一个`DataMatrix`对象，称为`live_dm`。`live_dm`是在循环执行之前创建的，并在循环完成时设为`None`；换句话说，`live_dm`仅在LOOP的*运行*阶段可用。

最后，当前行的索引存储为实验变量`live_row`。也就是说，`live_row`指示`live_dm`当前激活的行。

那么假设我们有一个叫做 *block_loop* 的 LOOP。我们可以在 Python 内联脚本中像下面这样访问 LOOP 表格：

~~~ .python
print('原始的 loop 表格：')
print(items['block_loop'].dm)

print('转换后的 loop 表格：')
print(items['block_loop'].live_dm)

print('当前行：')
print(items['block_loop'].live_dm[var.live_row])
~~~

您甚至可以以编程方式定义 LOOP 表格。您需要在一个优先于 LOOP 的 INLINE_SCRIPT 的 Prepare 阶段中执行此操作。

```python
from datamatrix import DataMatrix

items['block_loop'].dm = DataMatrix(length=4)
items['block_loop'].dm.cue_side = 'left', 'right', 'left', 'right'
items['block_loop'].dm.cue_validity = 'valid', 'valid', 'invalid', 'invalid'
```

`DataMatrix` 对象是处理表格数据的强大结构。要了解更多信息，请参阅：

- <https://pydatamatrix.eu/>