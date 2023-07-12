title: OpenSesame 作为 Python 库（无图形界面）
hash: f402b6dd5bcb95ef27e11fded05dd0fb27ec738f984dad3ea0c2ccc950ffbe1e
locale: zh
language: Chinese

您也可以通过将OpenSesame作为Python模块来完全通过编程方式编写实验。这主要适合喜欢编程而不是使用图形用户界面的人。

将OpenSesame用作Python模块的工作方式与在用户界面中使用Python `inline_script`项目的方式相差无几，但有两个显著的例外：

- 需要从`libopensesame.python_workspace_api`明确导入函数和类。所有在[公共函数](％url：manual / python / common％)下描述的函数和类都可用。
- 需要使用 `Experiment()`工厂函数明确创建`experiment`对象。

一个简单的Hello World实验看起来是这样的：

```python
from libopensesame.python_workspace_api import \
  Experiment, Canvas, Keyboard, Text

# 使用遗留后端初始化实验窗口
exp, win, clock, log = Experiment(canvas_backend='legacy')
# 准备刺激画布和键盘
cnv = Canvas()
cnv += Text('Hello world')
kb = Keyboard()
# 显示画布，等待键按，并结束实验
cnv.show()
kb.get_key()
exp.end()
```

您也可以通过编程方式打开一个`.osexp`实验文件并执行它：

```python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
```