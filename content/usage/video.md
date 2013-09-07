---
layout: osdoc
title: Video playback
group: Usage
permalink: /video/
---

Overview
--------

- [media_player_vlc plug-in](#media_player_vlc)
- [media_player plug-in](#media_player)
- [OpenCV](#opencv)

media_player_vlc plug-in {#media_player_vlc}
------------------------

As of OpenSesame 0.27, a plug-in based on the well-known VLC media player is included by default in the Windows release. You can download the latest version of the plug-in from here:

- <https://github.com/dschreij/media_player_vlc>

In addition, you need to install the VLC media player in the default location:

- <http://www.videolan.org/>

*Troubleshooting:* If you encounter a black screen when running your experiment in fullscreen (i.e. the video appears to play, but you don't see anything), please try using a different back-end (i.e. switch from *legacy* to *xpyriment* or vice versa), or change the back-end settings for the *legacy* back-end.

media_player plug-in {#media_player}
--------------------

In OpenSesame 0.26, a media_player plug-in based on FFMpeg was included by default in the Windows release. Because the Python bindings for FFMpeg are not compatible with Python 2.7, this plug-in is unfortunately no longer included with recent (Python 2.7 based) builds of OpenSesame. If you want to use the media_player plug-in, you can download an older version of OpenSesame or run OpenSesame from source with a Python 2.6 environment.

- Media_player source: <https://github.com/dschreij/media_player>

OpenCV {#opencv}
------

OpenCV is a powerful computer vision library, which contains (among many other things) routines for reading video files.

- <http://opencv.willowgarage.com/documentation/python/index.html>

The following snippet shows how to playback a video. This assumes that you are running the *legacy* back-end, or the *xpyriment* back-end without OpenGL.

{% highlight python %}

import cv
import pygame

# Full path to the video file
path = exp.get_file('my_video.avi')

# Open the video and determine the video dimensions
video = cv.CreateFileCapture(path)
width = cv.GetCaptureProperty(video, cv.CV_CAP_PROP_FRAME_WIDTH)
height = cv.GetCaptureProperty(video, cv.CV_CAP_PROP_FRAME_HEIGHT)

# The video needs to be converted twice, so we need to intermediate OpenC
# matrices
src_tmp = cv.CreateMat(exp.height, exp.width, cv.CV_8UC3)
src_rgb = cv.CreateMat(exp.height, exp.width, cv.CV_8UC3)

# A loop to play the video file. This can also be a while loop until a key
# is pressed. etc.
for i in range(100):

	# Get a frame, resize it to the full screen, convert it to the proper
	# color format, and finally convert it to a PyGamesurface
	src = cv.QueryFrame(video)
	cv.Resize(src, src_tmp)
	cv.CvtColor(src_tmp, src_rgb, cv.CV_BGR2RGB)
	surf = pygame.image.frombuffer(src_rgb.tostring(), cv.GetSize(src_rgb), 'RGB')

	# Now you can draw whatever you want onto the PyGame surface!
	pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))

	# Show the PyGame surface!
	exp.surface.blit(surf, (0, 0))
	pygame.display.flip()

{% endhighlight %}