title: 视频播放
hash: a3addf316f97e40c4be8ba9a0bcb131cf86555b8bcc9616dfd23957587f38442
locale: zh
language: Chinese

[TOC]


## media_player_mpy 插件

MEDIA_PLAYER_MPY 插件基于 MoviePy。它默认包含在 OpenSesame 的 Windows 和 Mac OS 软件包中。如果没有安装，您可以通过安装 `opensesame-plugin-media-player-mpy` 软件包来获取它，如下所述：

- <https://rapunzel.cogsci.nl/manual/environment/>

源代码托管在：

- <https://github.com/dschreij/opensesame-plugin-mediaplayer>


## OpenCV

OpenCV 是一个强大的计算机视觉库，其中包含用于读取视频文件的例程（以及其他许多功能）。

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

以下示例显示如何播放视频文件，同时在视频上绘制一个红色正方形。此示例假设您使用的是遗留后端。

~~~ .python
import cv2
import numpy
import pygame
# 文件池中视频文件的完整路径
path = pool['myvideo.avi']
# 打开视频
video = cv2.VideoCapture(path)
# 播放视频文件的循环。这也可以是一个 while 循环，直到按下某个键等。
for i in range(100):
    # 获取帧
    retval, frame = video.read()
    # 旋转它，因为由于某种原因，它否则会出现翻转。
    frame = numpy.rot90(frame)
    # 视频使用 BGR 颜色，而 PyGame 需要 RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 创建 PyGame 表面
    surf = pygame.surfarray.make_surface(frame)
    # 现在你可以在 PyGame 表面上画任何你想画的东西！
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # 显示 PyGame 表面！
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
~~~