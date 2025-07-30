title: 视频播放
hash: 135ac06d95735a29df2450dc840b4ab283182095a768134d3d35e7c85f031901
locale: zh
language: Chinese

[TOC]

## media_player_mpy 插件

[MEDIA_PLAYER_MPY](https://github.com/open-cogsci/opensesame-plugin-mediaplayer) 插件基于 MoviePy。它在 OpenSesame 中默认包含。（如果你使用的是自定义环境，可以通过安装 `opensesame-plugin-media_player_mpy` 包来获取。）

## OpenCV

OpenCV 是一个功能强大的计算机视觉库，其中包含（以及许多其他功能）读取视频文件的例程。

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

以下示例演示了如何播放视频文件，并在视频上绘制一个红色正方形。此示例假设你正在使用旧版后端。

```python
import cv2
import numpy
import pygame
# file pool中文件的完整视频文件路径
path = pool['myvideo.avi']
# 打开视频
video = cv2.VideoCapture(path)
# 循环播放视频文件。 这也可以替换为一个while循环，直到按下某个按键，等等。
for i in range(100):
    # 获取一帧
    retval, frame = video.read()
    # 旋转帧，因为出于某些原因否则视频看起来会翻转
    frame = numpy.rot90(frame)
    # 视频使用BGR颜色，PyGame需要RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 创建一个 PyGame surface
    surf = pygame.surfarray.make_surface(frame)
    # 现在你可以在 PyGame surface 上绘制任何你想要的内容了！
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # 显示 PyGame surface！
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
```