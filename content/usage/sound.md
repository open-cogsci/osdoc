---
layout: osdoc
title: Sound playback and timing
group: Usage
permalink: /sound/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## The `sampler` item

The `sampler` item provides an easy way to play back sound files (%FigSampler).

*Important note:* If you find that your sample plays to slowly (low pitch) or too quickly (high pitch), make sure that the sampling rate of your sample matches the sampling rate of the sampler back-end as specified under back-end settings.

%--
figure:
 source: sampler.png
 id: FigSampler
 caption: The `sampler` item.
--%

## The `synth` item

The `synth` item provides an easy way to generate and play back simple generated sounds (%FigSynth).

%--
figure:
 source: synth.png
 id: FigSynth
 caption: The `synth` item.
--%

## Timing

By default, OpenSesame uses [PyGame] for sound playback. PyGame is stable and robust, but it's timing properties are quite poor. In practice, you should expect a temporal jitter of around 30ms. Therefore, if you require very accurate temporal precision when presenting auditory stimuli you may want to write an inline_script that plays back sound using a different module, such as [PyAudio].

Some benchmarks tests of PyGame sound timing can be found on the Expyriment wiki:

- <http://docs.expyriment.org/Timing.html#audio>

## Sound input

For information about sound input, see this page:

- [/devices/soundrecorder](/devices/soundrecorder)

[pygame]: http://www.pygame.org/
[pyaudio]: http://people.csail.mit.edu/hubert/pyaudio/
