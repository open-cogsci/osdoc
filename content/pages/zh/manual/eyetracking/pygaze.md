title: PyGaze (眼动追踪)
hash: 80766dbbeccf44569af795eddea4817ca3fd7e30726a50587814ffbfd94c5c8a
locale: zh
language: Chinese

[TOC]

## 关于

PyGaze是一个用于眼球追踪的Python库。一组插件允许您在OpenSesame中使用PyGaze。关于PyGaze的更多信息，请访问:

- <http://www.pygaze.org/>

请引用PyGaze如下：

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: An open-source, cross-platform toolbox for minimal-effort programming of eyetracking experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0422-2
{: .reference}

## 支持的眼球追踪器

PyGaze支持以下眼球追踪器：

- [EyeLink](%link:eyelink%)
- [EyeTribe](%link:eyetribe%)

对于以下眼球追踪器，有实验性支持：

- [EyeLogic](%link:eyelogic%)
- [GazePoint / OpenGaze](%link:gazepoint%)
- [SMI](%link:smi%)
- [Tobii](%link:tobii%)

您还可以使用WebGazer.js在在线实验中执行基本的眼球追踪：

- [WebGazer.js](%link:webgazer%)

PyGaze还包括两个用于测试目的的虚拟眼球追踪器：

- __简单虚拟__  - 什么都不做。
- __高级虚拟__  - 鼠标模拟眼动。

## 安装PyGaze

### Windows

如果您使用的是OpenSesame的官方Windows软件包，那么PyGaze已经安装。

### Ubuntu

如果您使用Ubuntu，您可以从Cogsci.nl PPA获得PyGaze：

```
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install python-pygaze
```

如果您使用Python 3，将最后一个注释更改为：

```
sudo apt-get install python3-pygaze
```

## pip安装（所有平台）

您可以使用`pip`安装PyGaze：

```
pip install python-pygaze
```

### Anaconda（所有平台）

```
conda install python-pygaze -c cogsci
```

## PyGaze OpenSesame 插件

以下PyGaze插件可用：

- PYGAZE_INIT - 初始化PyGaze。此插件通常插入实验开始部分。
- PYGAZE_DRIFT_CORRECT - 实现漂移校正过程。
- PYGAZE_START_RECORDING - 将PyGaze置于录制模式。
- PYGAZE_STOP_RECORDING - 使PyGaze脱离录制模式。
- PYGAZE_WAIT - 暂停，直到发生事件，例如扫视开始。
- PYGAZE_LOG - 记录实验变量和任意文本。

## 示例

要查看如何使用PyGaze插件的示例，请参阅随OpenSesame附带的PyGaze模板。

以下是如何在Python INLINE_SCRIPT中使用PyGaze的示例：

~~~ .python
# 创建一个键盘和画布对象
my_keyboard = Keyboard(timeout=0)
my_canvas = Canvas()
my_canvas['dot'] = Circle(x=0, y=0, r=10, fill=True)
# 循环 ...
while True:
	# ... 直到按下空格键
	key, timestamp = my_keyboard.get_key()
	if key == 'space':
		break
	# 从pygaze获取凝视位置 ...
	x, y = eyetracker.sample()
	# ... 并绘制一个基于验证凝视的点！
	my_canvas['dot'].x = x + my_canvas.left
	my_canvas['dot'].y = y + my_canvas.top
	my_canvas.show()
~~~

## 功能概述

要在OpenSesame中初始化PyGaze，请将PYGAZE_INIT插件插入您的实验。一旦完成此操作，一个`eyetracker`对象将可用，其提供如下功能：

%-- include: include/api/eyetracker.md --%