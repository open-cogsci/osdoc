title: backends
reviewed: false

The *back-end* is the software layer that deals with input (keyboard input, mouse input, etc.) and output (display presentation, sound playback, etc.). There are many Python libraries that offer this type of functionality and OpenSesame could, in principle, use any one of them. For this reason, OpenSesame is back-end independent, in the sense that you can choose which back-end should be used. Currently there are five different back-ends: `legacy`, `psycho`, `droid`, `xpyriment`, and `opengl` (deprecated).

[TOC]

## Differences and some tips

Usually, you won't notice which back-end is used. The differences between back-ends are largely technical, and, as long as you use the graphical user interface or the `openexp` Python modules, all back-ends work the same way. However, there are a number of reasons to prefer one back-end over another in a particular situation.

- Not all back-end are equally accurate when it comes to [timing].
	- Tip: If you care about millisecond precision timing, use `xpyriment` or `psycho`.
- Not all back-ends are equally fast when it comes to generating stimuli.
	- Tip: If [forms] are slow, use `legacy`.
	- Tip: If the intertrial interval is long (due to stimulus preparation), use `legacy`.
- You can make use of back-end specific functionality when writing Python inline code.
	- Tip: If you want to use PsychoPy functionality, use `psycho`.
	- Tip: If you want to use Expyriment functionality, use `xpyriment`.
	- Tip: If you want to use PyGame functionality, use `legacy`.
- Not all back-ends are supported on all platforms.

## Selecting a back-end

The easiest way to select a back-end is using the combobox in the "General tab" of the experiment (%FigSelect).

%--
figure:
 id: FigSelect
 source: fig-select.png
 caption: "The back-end selection combobox."
--%

If you view the general script (select "Show script editor"), you will see that there are actually five distinct back-ends, for the canvas, keyboard, mouse, sampler and synth. The combobox-method automatically selects an appropriate, pre-defined combination of back-ends, but you could, in theory, mix and match.

For example, if you select the `psycho` back-end, the following code will be generated:

	set mouse_backend "psycho"
	set sampler_backend "legacy"
	set keyboard_backend "psycho"
	set canvas_backend "psycho"
	set synth_backend "legacy"

## xpyriment

The xpyriment back-end is built on top of [Expyriment][], a library that has been designed specifically for creating cognitive and neuroscientific experiments. It is a light-weight hardware-accelerated back-end with excellent timing properties. If you care about temporal precision, but do not plan on generating complex stimuli (i.e. Gabor patches, random-dot gratings, etc.) xpyriment is a good choice.

### Using Expyriment directly

You can find extensive documentation on Expyriment at <http://www.expyriment.org/doc>. The following code snippet shows a line of text:

~~~ .python
from expyriment import stimuli
text = stimuli.TextLine('This is expyriment!')
text.present()
~~~

### Installing Expyriment on Ubuntu

Ubuntu users can install Expyriment from the Cogsci.nl PPA:

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install expyriment

### Citation

Although Expyriment is bundled with the binary distributions of OpenSesame, it is a separate project. When appropriate, please provide the following citation in addition to citing OpenSesame:

Krause, F., & Lindemann, O. (in press). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*.
{: .reference}

## psycho

The psycho back-end is built on top of [PsychoPy][], a library that has been designed specifically for creating psychological experiments. It is hardware accelerated and provides high level routines for creating complex visual stimuli (drifting gratings, etc.). If you care about timing and plan on creating complex stimuli, Psycho is a good choice.

### Using PsychoPy directly

You can find extensive documentation on PsychoPy at <http://www.psychopy.org/>. When using PsychoPy in OpenSesame, it is important to know that the main window can be accessed as `self.experiment.window` or simply `win`. So the following code snippet draws a Gabor patch:

~~~ .python
from psychopy import visual
gabor = visual.PatchStim(win, tex="sin", size=256, mask="gauss", sf=0.05, ori=45)
gabor.draw()
win.flip()
~~~

An example experiment that uses PsychoPy can be found here: [tilt_adaptation_psychopy.opensesame][example]

### Tutorials

A tutorial specifically for using PsychoPy from within OpenSesame:

- <http://www.cogsci.nl/blog/tutorials/211-a-bit-about-patches-textures-and-masks-in-psychopy>

And a more general PsychoPy tutorial:

- <http://gestaltrevision.be/wiki/coding>

### Citation

Although PsychoPy is bundled with the binary distributions of OpenSesame, it is a separate project. When appropriate, please cite the following papers in addition to citing OpenSesame:

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Peirce, J. W. (2009). Generating stimuli for neuroscience using PsychoPy. *Frontiers in Neuroinformatics*, *2*(10). doi:10.3389/neuro.11.010.2008
{: .reference}

## legacy

The legacy back-end is built on top of [PyGame][] in non-OpenGL mode. The downside of this is that there is no hardware acceleration, and the timing properties are not as good as that of the psycho or xpyriment back-ends. The upside is that PyGame is very easy to use, very reliable, and well supported on a wide range of platforms.

### Mouse-cursor visibility

On some systems, the mouse cursor is not visible when using the *legacy* back-end in fullscreen mode. You can work around this is the following ways:

1. Open the *legacy* back-end settings and set "Double buffering" to "no".
	- *Note:* This may disable v-sync, which can be important for time critical experiments, as discussed here: [/miscellaneous/timing/](/miscellaneous/timing/).
2. Open the *legacy* back-end settings and set "Custom cursor" to "yes".
3. Switch to another back-end.

### Using PyGame directly

PyGame is well documented and you can find everything you need to know about using PyGame on <http://www.pygame.org/docs/>. Specific to OpenSesame is the fact that the display surface is stored as `self.experiment.window` or simply `win`. So the following code snippet, which you could paste into an inline_script item, draws a red rectangle to the display:

~~~ .python
import pygame # Import the PyGame module
pygame.draw.rect(self.experiment.window, pygame.Color("red"),
	[20, 20, 100, 100]) # Draw a red rectangle. Not shown yet...
pygame.display.flip() # Update the display to show the red rectangle.
~~~

## droid

The droid back-end is built on top of the [PyGame subset for Android][pgs4a] and allows you to run your OpenSesame experiments on Android devices, using the [OpenSesame runtime for Android][runtime]. The droid back-end is in most ways identical to the [legacy][] back-end.

[runtime]: /getting-opensesame/android/
[pgs4a]: http://pygame.renpy.org/
[legacy]: /back-ends/legacy
[pygame]: http://www.pygame.org/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org
[example]: https://github.com/smathot/OpenSesame/blob/master/examples/tilt_adaptation_psychopy.opensesame


[inline-script]: /python/about
[legacy]: /back-ends/legacy
[opengl]: /back-ends/opengl
[xpyriment]: /back-ends/xpyriment
[psycho]: /back-ends/psycho
[droid]: /back-ends/droid
[timing]: /miscellaneous/timing
[forms]: /forms/about
