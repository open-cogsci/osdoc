---
layout: osdoc
title: Psycho
group: Back-ends
permalink: /psycho/
level: 1
sortkey: 008.004
---

The psycho back-end is built on top of [PsychoPy][], a library that has been designed specifically for creating psychological experiments. It is hardware accelerated and provides high level routines for creating complex visual stimuli (drifting gratings, etc.). If you care about timing and plan on creating complex stimuli, Psycho is a good choice.

Using PsychoPy directly
-----------------------

You can find extensive documentation on PsychoPy at <http://www.psychopy.org/>. When using PsychoPy in OpenSesame, it is important to know that the main window can be accessed as `self.experiment.window` or simply `win`. So the following code snippet draws a Gabor patch:

{% highlight python %}
from psychopy import visual
gabor = visual.PatchStim(win, tex="sin", size=256, mask="gauss", sf=0.05, ori=45)
gabor.draw()
win.flip()
{% endhighlight %}

An example experiment that uses PsychoPy can be found here: [tilt_adaptation_psychopy.opensesame][example]

Citation
--------

Although PsychoPy is bundled with the binary distributions of OpenSesame, it is a separate project. When appropriate, please cite the following papers in addition to citing OpenSesame:

###### Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017
###### Peirce, J. W. (2009). Generating stimuli for neuroscience using PsychoPy. *Frontiers in Neuroinformatics*, *2*(10). doi: 10.3389/neuro.11.010.2008

[psychopy]: http://www.psychopy.org/
[example]: https://github.com/smathot/OpenSesame/blob/master/examples/tilt_adaptation_psychopy.opensesame