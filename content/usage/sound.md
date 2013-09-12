---
layout: osdoc
title: Sound playback and timing
group: Usage
permalink: /sound/
---

By default, OpenSesame uses [PyGame] for sound playback. PyGame is stable and robust, but it's timing properties are quite poor. In practice, you should expect a temporal jitter of around 30ms. Therefore, if you require very accurate temporal precision when presenting auditory stimuli you may want to write an inline_script that plays back sound using a different module, such as [PyAudio].

Some benchmarks tests of PyGame sound timing can be found on the Expyriment wiki:
	
- <http://code.google.com/p/expyriment/wiki/Timing#Audio>

[pygame]: http://www.pygame.org/
[pyaudio]: http://people.csail.mit.edu/hubert/pyaudio/