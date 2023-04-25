title: 后端
hash: 1447d1754e76a00442c1709babb3c8b9ef77f76eb2aeb0c1e6bb57c9a232512c
locale: zh
language: Chinese

*后端*是处理输入（键盘输入，鼠标输入等）和输出（显示展示，声音播放等）的软件层。有很多库提供此类功能，原则上，OpenSesame可以使用其中任何一个。出于这个原因，OpenSesame是后端独立的，这意味着您可以选择要使用哪个后端。目前有四个后端：*legacy*，*psycho*，*xpyriment* 和 *osweb*。

[TOC]

## 差异与一些建议

通常，您不会注意到使用的是哪个后端。后端之间的

您可以在 <http://www.psychopy.org/> 上找到关于PsychoPy的详尽文档。在OpenSesame中使用PsychoPy时，重要的是要知道主窗口可以作为`self.experiment.window` 或简称为 `win` 进行访问。因此，以下代码片段绘制一个Gabor patch：

~~~ .python
from psychopy import visual
gabor = visual.PatchStim(win, tex="sin", size=256, mask="gauss", sf=0.05, ori=45)
gabor.draw()
win.flip()
~~~

### 教程

一个专门针对在OpenSesame中使用PsychoPy的教程：

- <http://www.cogsci.nl/blog/tutorials/211-a-bit-about-patches-textures-and-masks-in-psychopy>

以及一个更通用的PsychoPy教程：

- <http://gestaltrevision.be/wiki/coding>

### 引用

虽然PsychoPy是与OpenSesame的二进制发行版捆绑在一起的，但它是一个单独的项目。在适当的情况下，请除了引用OpenSesame外，还请引用以下论文：

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Peirce, J. W. (2009). Generating stimuli for neuroscience using PsychoPy. *Frontiers in Neuroinformatics*, *2*(10). doi:10.3389/neuro.11.010.2008
{: .reference}

## legacy

legacy后端是在[PyGame][]的非OpenGL模式下构建的。这样做的缺点是没有硬件加速，时序属性不如psycho或xpyriment后端。优点是PyGame非常容易使用，非常可靠，并在广泛的平台上得到很好的支持。

### 鼠标光标可见性

在某些系统上，当在全屏模式下使用*legacy*后端时，鼠标光标可能不可见。您可以通过以下方法解决这个问题：

1. 打开*legacy*后端设置，将“双缓冲”设置为“否”。
	- *注意：*这可能会禁用v-sync，这对于时间关键的实验可能非常重要，如[此处](%link:timing%)所讨论的。
2. 打开*legacy*后端设置，将“自定义光标”设置为“是”。
3. 切换到另一个后端。

### 直接使用 PyGame

PyGame文档齐全，您可以在<http://www.pygame.org/docs/>上找到有关使用PyGame的所有信息。对于OpenSesame，特定的是显示表面存储为`self.experiment.window` 或简称为 `win`。因此，您可以将以下代码片段粘贴到INLINE_SCRIPT项中，将一个红色矩形绘制到显示屏幕上：

~~~ .python
import pygame # 导入PyGame模块
pygame.draw.rect(self.experiment.window, pygame.Color("red"),
	[20, 20, 100, 100]) # 绘制一个红色的矩形。还没有显示...
pygame.display.flip() # 更新显示以显示红色矩形。
~~~

## osweb

*osweb* 后端是基于OSWeb构建的，允许您在浏览器中运行实验。有关更多信息，请参见：

- %link:manual/osweb/workflow%