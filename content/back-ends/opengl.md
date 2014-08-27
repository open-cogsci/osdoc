---
layout: osdoc
title: OpenGL
group: Back-ends
permalink: /opengl/
---

The opengl back-end is built on top of [PyGame][] in OpenGL mode, using [PyOpenGL][]. The upside is that this back-end is hardware accelerated, temporally precise, and can potentially be used for all kinds of fancy drawing operations (3D etc.). The downside is that it is tricky to use directly. For more information, please refer to the documentation of [PyGame][] and [PyOpenGL][].

Enabling the OpenGL back-ends
-----------------------------

As of OpenSesame 0.27, the OpenGL back-end has been deprecated in favour of the xpyriment back-end, which offers in many ways the same functionality. It is therefore no longer available in the back-end selection box in the user interface. To nevertheless select the OpenGL back-end, click on the *Script editor* button of the *General properties* tab, and set the back-end variables as follows:

	set canvas_backend opengl
	set keyboard_backend legacy
	set mouse_backend legacy
	set sampler_backend legacy
	set synth_backend legacy

*With thanks to Per Sederberg*

[pygame]: http://www.pygame.org/
[pyopengl]: http://pyopengl.sourceforge.net/documentation/index.html
