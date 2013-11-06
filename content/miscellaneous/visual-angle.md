---
layout: osdoc
title: Visual angle
group: Miscellaneous
permalink: /visual-angle/
level: 1
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About

You will often see that the size of visual stimuli is expressed in degrees of visual angle (°). Visual degrees express the angle between the straight lines from the extremities of the stimulus to the lens. So visual angle is related to the size that the stimulus subtends on the retina, but only indirectly: It is an angle measured from the eye's lens, as shown in %FigEye
	
%--
figure:
 id: FigEye
 source: fig-eye.png
 caption: A schematic illustration of degrees of visual angle. (Image adapted from [WikiMedia Commons](http://commons.wikimedia.org/wiki/File:Schematic_diagram_of_the_human_eye.svg).)
--%

The reason for using this somewhat odd measure of size is that it reflects the perceived size of a stimulus, which in psychological experiments is typically more important than its real size. For example, if you present a picture with a real width of 100 pixels on the monitor, the visual angle may correspond to 3°. If you move the monitor further away, the visual angle of the picture will decrease to, say, 2°. This reflects that the distance between a stimulus and an observer is important.

See also:

- <http://en.wikipedia.org/wiki/Visual_angle>

## Convert pixels to visual degrees

You will need to know three things in order to covert pixels to visual degrees:

- `h` is the height of the monitor in centimeters, which you can measure with a ruler. (e.g., 25cm)
- `d` is the distance from the participant to the monitor in centimeters, which you can measure with a ruler. (e.g., 60cm)
- `r` is the vertical resolution of the monitor in pixels, which you can find in your operating system's display settings (e.g., 768 px)

You can calculate the number of pixels per degree as shown in %LstDeg. You can execute this script in the OpenSesame debug window. Of course, you need to substitute all values so that they correspond to your setup. Note that a single visual degree typically corresponds to 30 - 60 pixels, depending on the distance and size of the monitor. If you obtain values that are far outside of this range, you have probably made a mistake.

%--
code:
 id: LstDeg
 syntax: python
 source: to-degrees.py
 caption: A Python script to convert pixels to visual degrees.
--%

## Convert visual degrees to pixels

Converting from visual degrees to pixels is simply the inverse of the procedure described above, and can be done as shown in %LstPix.
	
%--
code:
 id: LstPix
 syntax: python
 source: to-pixels.py
 caption: A Python script to convert pixels to visual degrees.
--%