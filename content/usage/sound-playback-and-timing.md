---
layout: osdoc
title: Sound playback and timing
group: Usage
permalink: /sound-playback-and-timing/
---

By default, OpenSesame uses [PyGame][] for sound playback. PyGame is stable and robust, but it's timing properties are quite poor. In practice, you should expect a temporal jitter of around 30ms. Therefore, if you require very accurate temporal precision when presenting auditory stimuli you may want to write an inline_script that plays back sound using a different module, such as [PyAudio][].

Some benchmarks tests, which should generalize to OpenSesame, can be found on the Expyriment wiki: <http://code.google.com/p/expyriment/wiki/Timing#Audio>

If you have any benchmarks on the temporal precision of sound playback using OpenSesame or, more generally, in Python, let me know!

Known issues
------------

When using the psycho back-end on Windows, sound playback may occasionally fail on some systems (there will be no error, but you won't hear anything). I'm not sure what the cause of this problem is, but it's generally solved by a reboot or by restarting OpenSesame. If you consistently encounter this problem, please seek assistance on the forum!

[pygame]: http://www.pygame.org/
[pyaudio]: http://people.csail.mit.edu/hubert/pyaudio/