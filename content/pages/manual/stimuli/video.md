title: Video playback
complete: false

[TOC]

## media_player_gst plug-in

The `media_player_gst` plug-in is built on the Gstreamer framework. Downloads and installation instructions can be found here:

- <https://github.com/dschreij/media_player_gst/>

## media_player_vlc plug-in

As of OpenSesame 0.27, a plug-in based on the well-known VLC media player is included by default in the Windows release. You can download the latest version of the plug-in from here:

- <https://github.com/dschreij/media_player_vlc>

In addition, you need to install the VLC media player in the default location:

- <http://www.videolan.org/>

*Troubleshooting:* If you encounter a black screen when running your experiment in fullscreen (i.e. the video appears to play, but you don't see anything), please try using a different back-end (i.e. switch from *legacy* to *xpyriment* or vice versa), or change the back-end settings for the *legacy* back-end.

## media_player plug-in

In OpenSesame 0.26, a media_player plug-in based on FFMpeg was included by default in the Windows release. Because the Python bindings for FFMpeg are not compatible with Python 2.7, this plug-in is unfortunately no longer included with recent (Python 2.7 based) builds of OpenSesame. If you want to use the media_player plug-in, you can download an older version of OpenSesame or run OpenSesame from source with a Python 2.6 environment.

- Media_player source: <https://github.com/dschreij/media_player>

## OpenCV

OpenCV is a powerful computer vision library, which contains (among many other things) routines for reading video files.

- <http://docs.opencv.org/trunk/doc/py_tutorials/py_tutorials.html>

%LstExampleCV1 shows how to playback a video using `cv`, the Python module for OpenCV 1. %LstExampleCV2 shows (approximately) the same thing using `cv2`, the Python module for OpenCV 2. This assumes that you are running the *legacy* back-end, or the *xpyriment* back-end without OpenGL.

%--
code:
 id: LstExampleCV1
 source: opencv-example.py
 syntax: python
 caption: "Playing back video in an `inline_script` with OpenCV 1."
--%

%--
code:
 id: LstExampleCV2
 source: opencv2-example.py
 syntax: python
 caption: "Playing back video in an `inline_script` with OpenCV 2."
--%
