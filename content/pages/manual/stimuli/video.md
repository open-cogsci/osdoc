title: Video playback

[TOC]


## media_player_mpy plugin

The MEDIA_PLAYER_MPY plugin is based on MoviePy. It is included by default with the Windows and Mac OS packages of OpenSesame. If it is not installed, you can get it by installing the `opensesame-plugin-media-player-mpy` package, as described here:

- <https://rapunzel.cogsci.nl/manual/environment/>

The source code is hosted at:

- <https://github.com/dschreij/opensesame-plugin-mediaplayer>


## OpenCV

OpenCV is a powerful computer vision library, which contains (among many other things) routines for reading video files.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

The following example shows how to play back a video file, while drawing a red square on top of the video. This example assumes that you're using the legacy backend.

~~~ .python
import cv2
import numpy
import pygame
# Full path to the video file in file pool
path = pool['myvideo.avi']
# Open the video
video = cv2.VideoCapture(path)
# A loop to play the video file. This can also be a while loop until a key
# is pressed. etc.
for i in range(100):
    # Get a frame
    retval, frame = video.read()
    # Rotate it, because for some reason it otherwise appears flipped.
    frame = numpy.rot90(frame)
    # The video uses BGR colors and PyGame needs RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Create a PyGame surface
    surf = pygame.surfarray.make_surface(frame)
    # Now you can draw whatever you want onto the PyGame surface!
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # Show the PyGame surface!
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
~~~
