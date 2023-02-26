title: Sound

The most common way to play sound is using the SAMPLER item, for playback of audio files, or the SYNTH item, for playback of simple beeps, etc.

[TOC]

## The sampler

The SAMPLER plays back a single sound file, typically from the file pool.

Sound files are always played back at the sampling rate that is used by the OpenSesame sampler backend. If your sample appears to be sped up (high pitch) or slowed down (low pitch), you can adjust the sampling rate of your sound file in a sound editor, or change the sampling rate used by the OpenSesame sampler backend (under 'Show backend settings and info' in the General tab).

The SAMPLER has a few options:

- *Sound file* indicates the file to be played.
- *Volume* between 0 (silent) and 1 (normal volume).
- *Pan* turns the right (negative values) or left (positive values) channel down. For full panning, enter 'left' or 'right',
- *Pitch* indicates the playback speed, where 1 corresponds to the original speed.
- *Stop after* indicates for how long the sound file should be played. For example, a value of 100 ms means that playback will be stopped after 100 ms, regardless of how long the sound file is. A value of 0 ms means that the sound file will be played back completely.
- *Fade in* indicates the fade-in time for the sound file. For example, a value of 100 ms means that the sound file will start silent, and build up to maximum value in 100 ms.
- *Duration* indicates the duration of the sampler item, before the next item is presented. This doesn't need to match the length of the sound file. For example, if the duration of the sampler is set to 0 ms, OpenSesame will advance directly to the item that follows the SAMPLER (e.g., a sketchpad), *while the sound file continues playing in the background*. In addition to a numeric value, you can set duration to:
	- 'keypress' to wait for a key press
	- 'mouseclick' to wait for a mouse click
	- 'sound' to wait until the sampler has finished playing.

## The synth

The SYNTH is a basic sound synthesizer.

You can specify a
number of options:

- *Waveform* can be set to sine, sawtooth, square, or white noise
- *Attack* is the time it takes for the sound the reach maximum volume (i.e. fade in).
- *Decay* is the time it takes for the sound to die out (i.e. fade out). Note that the decay occurs within the length of the sound.
- *Volume* between 0 and 100%
- *Pan* turns the right (negative values) or left (positive values) channel down. Setting pan to -20 or 20 completely mutes the right or left channel, respectively.
- *Length* indicates the length of the sound (in milliseconds).
- *Duration* indicates the duration of the SYNTH item, before the next item is presented. This doesn't need to match the length of the sound. For example, the duration of the SYNTH may be set to 0ms, in order to advance directly to the next item (e.g., a SKETCHPAD), while the sound continues playing in the background. In addition to a numeric value, you can set the duration to 'keypress', to wait for a keyboard press, 'mouseclick', to wait for a mouse click, or 'sound', to wait until the SYNTH has finished playing.

## Sound playback in Python

You can use the SAMPLER object and the SYNTH function to present visual stimuli in Python:

- %link:sampler%
- %link:manual/python/common%


## Audio Low Latency plugins

The main goal of the Audio Low Latency plugins, developed by Bob Rosbag, is to play and record audio with minimal and predictable latencies to achieve a high accuracy and precision. The `PyAlsaAudio` package which uses the Linux ALSA audio system provided the best results within Python. `PortAudio` and `sounddevice` are cross-platform and work on both Windows as Linux.

The plugins are not installed by default, but can be installed through pip:

```bash
pip install opensesame-plugin-audio-low-latency
```

See also:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>
