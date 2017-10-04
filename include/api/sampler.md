<div class="ClassDoc YAMLDoc" id="Sampler" markdown="1">

# class __Sampler__

The `Sampler` class provides functionality to play sound samples. You
generally create a `Sampler` object with the `Sampler()` factory
function, as described in the section
[Creating a Sampler](#creating-a-sampler).

__Example:__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
my_sampler.play()
~~~

[TOC]

## Things to know

### Creating a Sampler

You generally create a `Sampler` with the `Sampler()` factory function,
which takes the full path to a sound file as the first argument.

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
~~~

Optionally, you can pass [Playback keywords](#playback-keywords) to
`Sampler()` to set the default behavior:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
~~~

### Sampling rate

If you find that your sample plays to slowly (low pitch) or too quickly
(high pitch), make sure that the sampling rate of your sample matches
the sampling rate of the sampler back-end as specified under back-end
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
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.play(volume=.5, pan='left')
~~~

Playback keywords only affect the current operation (except when passed
to [sampler.\_\_init\_\_][__init__]). To change the behavior for all
subsequent operations, set the playback properties directly:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.volume = .5
my_sampler.pan = 'left'
my_sampler.play()
my_sampler.play()
~~~

Or pass the playback keywords to [sampler.\_\_init\_\_][__init__]:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
my_sampler.play()
~~~

<div class="FunctionDoc YAMLDoc" id="Sampler-is_playing" markdown="1">

## function __Sampler\.is\_playing__\(\)

Checks if a sound is currently playing.

__Example:__

~~~ .python
src = pool[u'my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
if my_sampler.is_playing():
        print('The sampler is still playing!')
~~~

__Returns:__

True if a sound is playing, False if not.

- Type: bool

</div>

<div class="FunctionDoc YAMLDoc" id="Sampler-pause" markdown="1">

## function __Sampler\.pause__\(\)

Pauses playback (if any).

__Example:__

~~~ .python
src = pool[u'my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~

</div>

<div class="FunctionDoc YAMLDoc" id="Sampler-play" markdown="1">

## function __Sampler\.play__\(\*\*playback\_args\)

Plays the sound.

__Example:__

~~~ .python
src = pool[u'my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play(pitch=.5, block=True)
~~~

__Keyword dict:__

- `**playback_args`: Optional [playback keywords] that will be used for this call to [sampler.play]. This does not affect subsequent operations.

</div>

<div class="FunctionDoc YAMLDoc" id="Sampler-resume" markdown="1">

## function __Sampler\.resume__\(\)

Resumes playback (if any).

__Example:__

~~~ .python
src = pool[u'my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~

</div>

<div class="FunctionDoc YAMLDoc" id="Sampler-stop" markdown="1">

## function __Sampler\.stop__\(\)

Stops the currently playing sound (if any).

__Example:__

~~~ .python
src = pool[u'my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.stop()
~~~

</div>

<div class="FunctionDoc YAMLDoc" id="Sampler-wait" markdown="1">

## function __Sampler\.wait__\(\)

Blocks until the sound has finished playing or returns right away if no sound is playing.

__Example:__

~~~ .python
src = pool[u'my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
my_sampler.wait()
print('The sampler is finished!')
~~~

</div>

</div>

