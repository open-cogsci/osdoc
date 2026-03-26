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
- *Duration* indicates the duration of the SYNTH item, before the next item is presented. This doesn't need to match the length of the sound. For example, the duration of the SYNTH may be set to 0 ms, in order to advance directly to the next item (e.g., a SKETCHPAD), while the sound continues playing in the background. In addition to a numeric value, you can set the duration to 'keypress', to wait for a keyboard press, 'mouseclick', to wait for a mouse click, or 'sound', to wait until the SYNTH has finished playing.

## Sound timing in sampler and synth

Playing a sound in OpenSesame involves two independent controls: one that determines how long the sound itself plays, and one that determines how long the experiment waits at the current item before moving on. Understanding the difference between these two controls is essential for precise stimulus timing.

### Two independent controls

#### Sound length

| Item | Parameter | Description |
|---|---|---|
| **Sampler** | **Stop after** | Cuts the audio file short after the given number of ms. Set to `0` to play the file to its natural end. |
| **Synth** | **Length** | Directly sets how long the generated tone lasts (in ms). There is no natural end beyond the specified value. |

#### Item timing

Both SAMPLER and SYNTH share the *Duration* parameter, which controls how long the experiment stays on the item before moving to the next one. It does not directly affect the sound itself.

| Duration value | Behaviour |
|---|---|
| `0` | Move on immediately |
| *number* (ms) | Wait for the given number of ms, then move on |
| `sound` | Wait until the sound has finished playing |


### General rule

Let *sound length* refer to:
- *Stop after* for SAMPLER, or the file's natural length if *Stop after* is `0`
- *Length* for SYNTH

Then the following applies:

| Condition | Result |
|---|---|
| *Duration* **<** sound length | The item ends before the sound, so the sound continues into the next item |
| *Duration* = `sound` | The experiment waits until the sound finishes |
| *Duration* **≥** sound length | The item outlasts the sound, so playback has finished before the next item starts |

### Notes

- For SAMPLER, the actual playback time is the natural file length, unless *Stop after* is greater than `0`, in which case playback stops after the specified duration.
- For SYNTH, the actual playback time is always equal to *Length*.
- When *Duration* = `sound`, the experiment waits for the actual playback time, taking *Stop after* into account for SAMPLER.

### Sound continuing into the next item

A sound can continue playing after the current item has finished if *Duration* is shorter than the actual playback time. This can be intentional, for example when you want a sound to run in the background while the next item is shown. But it can also happen unintentionally if *Duration* is shorter than expected, in which case the sound may spill over into the next trial element.

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
