<div class="ClassDoc YAMLDoc" id="sampler" markdown="1">

# class __sampler__

The SAMPLER module provides functionality to play sound samples.

__Example:__

~~~ .python
src = exp.pool['bark.ogg']
my_sampler = sampler(src, volume=.5)
my_sampler.play()
~~~

[TOC]

## Things to know

### Sampling rate

If you find that your sample plays to slowly (low pitch) or too quickly
(high pitch), make sure that the sampling rate of your sample matches
the sampling rate of the sampler backend as specified under backend
settings.

### Supported file formats

Sound files in `.wav` and `.ogg` format are supported. If you need to
convert samples from a different format, you can use
[Audacity](http://sourceforge.net/projects/audacity/).

### Backwards incompatible changes from 2.9 to 3.0

The following are now properties, as described under
[playback keywords]:

- [sampler.block]
- [sampler.duration]
- [sampler.fade_in]
- [sampler.pan]
- [sampler.pitch]
- [sampler.volume]

Therefore, the following will no longer work:

~~~ .python
sampler.volume(.5)
~~~

And has to be changed to:

~~~ .python
sampler.volume = .5
~~~

### Playback keywords

Functions that accept `**playback_args` take the following keyword
arguments:

- `volume` specifies a volume between `0.0` (silent) and `1.0`
  (maximum).
- `pitch` specifies a pitch (or playback speed), where values > 1
  indicate a higher pitch, and values < 1 indicate a lower pitch.
- `pan` specifies a panning, where values < 0 indicate panning to the
  left, and values > 0 indicate panning to the right. Alternatively, you
  can set pan to 'left' or 'right' to play only a single channel.
- `duration` specifies the duration of the the sound in milliseconds, or
  is set to `0` or `None` to play the full sound.
- `fade_in` specifies the fade-in time (or attack) of the sound, or is
  set to `0` or `None` to disable fade-in.
- `block` indicates whether the experiment should block (`True`) during
  playback or not (`False`).

~~~ .python
src = exp.pool['bark.ogg']
my_sampler = sampler(src)
my_sampler.play(volume=.5, pan='left')
~~~

Playback keywords only affect the current operation (except when passed
to [sampler.\_\_init\_\_][__init__]). To change the behavior for all
subsequent operations, set the playback properties directly:

~~~ .python
src = exp.pool['bark.ogg']
my_sampler = sampler(src)
my_sampler.volume = .5
my_sampler.pan = 'left'
my_sampler.play()
my_sampler.play()
~~~

Or pass the playback keywords to [sampler.\_\_init\_\_][__init__]:

~~~ .python
src = exp.pool['bark.ogg']
my_sampler = sampler(src, volume=.5, pan='left')
my_sampler.play()
my_sampler.play()
~~~

<div class="FunctionDoc YAMLDoc" id="sampler-__init__" markdown="1">

## function __sampler\.\_\_init\_\___\(experiment, src, \*\*playback\_args\)

Constructor to create a new SAMPLER object. You do not generally
call this constructor directly, but use the `sampler()` function,
which is described here: [/python/sampler/]().

__Example:__

~~~ .python
src = exp.pool[u'my_sound.ogg']
my_sampler = sampler(src, volume=.5)
~~~

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment
- `src` -- The full path to a `.wav` or `.ogg` file.
	- Type: unicode, str

__Keyword dict:__

- `**playback_args`: Optional [playback keywords] that will be used as the default for this SAMPLER object.

</div>

[sampler.__init__]: #sampler-__init__
[__init__]: #sampler-__init__

<div class="FunctionDoc YAMLDoc" id="sampler-close_sound" markdown="1">

## function __sampler\.close\_sound__\(experiment\)

Closes the mixer after the experiment is finished.

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment

</div>

[sampler.close_sound]: #sampler-close_sound
[close_sound]: #sampler-close_sound

<div class="FunctionDoc YAMLDoc" id="sampler-init_sound" markdown="1">

## function __sampler\.init\_sound__\(experiment\)

Initializes the pygame mixer before the experiment begins.

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment

</div>

[sampler.init_sound]: #sampler-init_sound
[init_sound]: #sampler-init_sound

<div class="FunctionDoc YAMLDoc" id="sampler-is_playing" markdown="1">

## function __sampler\.is\_playing__\(\)

Checks if a sound is currently playing.

__Returns:__

True if a sound is playing, False if not.

- Type: bool

</div>

[sampler.is_playing]: #sampler-is_playing
[is_playing]: #sampler-is_playing

<div class="FunctionDoc YAMLDoc" id="sampler-pause" markdown="1">

## function __sampler\.pause__\(\)

Pauses playback (if any).

__Example:__

~~~ .python
src = exp.pool[u'my_sound.ogg']
my_sampler = sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~

</div>

[sampler.pause]: #sampler-pause
[pause]: #sampler-pause

<div class="FunctionDoc YAMLDoc" id="sampler-play" markdown="1">

## function __sampler\.play__\(\*\*playback\_args\)

Plays the sound.

__Example:__

~~~ .python
src = exp.pool[u'my_sound.ogg']
my_sampler = sampler(src)
my_sampler.play(pitch=.5, block=True)
~~~

__Keyword dict:__

- `**playback_args`: Optional [playback keywords] that will be used for this call to [sampler.play]. This does not affect subsequent operations.

</div>

[sampler.play]: #sampler-play
[play]: #sampler-play

<div class="FunctionDoc YAMLDoc" id="sampler-resume" markdown="1">

## function __sampler\.resume__\(\)

Resumes playback (if any).

__Example:__

~~~ .python
src = exp.pool[u'my_sound.ogg']
my_sampler = sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~

</div>

[sampler.resume]: #sampler-resume
[resume]: #sampler-resume

<div class="FunctionDoc YAMLDoc" id="sampler-stop" markdown="1">

## function __sampler\.stop__\(\)

Stops the currently playing sound (if any).

__Example:__

~~~ .python
src = exp.pool[u'my_sound.ogg']
my_sampler = sampler(src)
my_sampler.play()
sleep(100)
my_sampler.stop()
~~~

</div>

[sampler.stop]: #sampler-stop
[stop]: #sampler-stop

<div class="FunctionDoc YAMLDoc" id="sampler-wait" markdown="1">

## function __sampler\.wait__\(\)

Blocks until the sound has finished playing or returns right away if no sound is playing.

__Example:__

~~~ .python
src = exp.pool[u'my_sound.ogg']
my_sampler = sampler(src)
my_sampler.play()
my_sampler.wait()
print('The sampler is finished!')
~~~

</div>

[sampler.wait]: #sampler-wait
[wait]: #sampler-wait

</div>

[sampler]: #sampler

