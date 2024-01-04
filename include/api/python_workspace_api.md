<div class="ClassDoc YAMLDoc" markdown="1">

## Canvas(auto_prepare=True, \*\*style_args)

A factory function that creates a new `Canvas` object. For a
description of possible keywords, see:

- %link:manual/python/canvas%


__Returns__

- A `Canvas` object.

__Example__

~~~ .python
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~



## Experiment(osexp_path=None, log_path='defaultlog.csv', fullscreen=False, subject_nr=0, \*\*kwargs)

A factory function that creates a new `Experiment` object. This is only
useful when implementing an experiment entirely through a Python script,
rather than through the user interface.


__Parameters__

- **osexp_path**: If a path to an `.osexp` file is specified, this file is opened and
can be run directly by calling `Experiment.run()`. If no experiment
file is specified, an empty experiment is initialized.
- **log_path**: 
- **fullscreen**: 
- **subject_nr**: 
- **kwargs**: Optional keyword arguments that are interpreted as experimental
variables. The main use of this is to specify the backend through
the `canvas_backend` keyword.

__Returns__

- An (exp, win, clock, log) tuple corresponding to the Experiment,
window handle (backend-specific), Clock, and Log objects.

__Example__

To implement an experiment fully programmatically:

~~~ .python
from libopensesame.python_workspace_api import (
    Experiment, Canvas, Text, Keyboard)
exp, win, clock, log = Experiment(canvas_backend='legacy')
c = Canvas()
c += Text('Press any key')
c.show()
kb = Keyboard()
kb.get_key()
exp.end()
~~~

To load an experiment file and run it:

~~~ .python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
~~~



## Form(\*args, \*\*kwargs)

A factory function that creates a new `Form` object. For a
description
of possible keywords, see:

- %link:manual/forms/widgets%


__Returns__

- A `Form` object.

__Example__

~~~ .python
form = Form()
label = Label(text='label')
button = Button(text='Ok')
form.set_widget(label, (0,0))
form.set_widget(button, (0,1))
form._exec()
~~~



## Keyboard(\*\*resp_args)

A factory function that creates a new `Keyboard` object. For a
description of possible keywords, see:

- %link:manual/python/keyboard%


__Returns__

- A `Keyboard` object.

__Example__

~~~ .python
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key, time = my_keyboard.get_key()
~~~



## Mouse(\*\*resp_args)

A factory function that creates a new `Mouse` object. For a
description
of possible keywords, see:

- %link:manual/python/mouse%


__Returns__

- A `mouse` object.

__Example__

~~~ .python
my_mouse = Mouse(keylist=[1,3], timeout=5000)
button, time = my_mouse.get_button()
~~~



## Sampler(src, \*\*playback_args)

A factory function that creates a new `Sampler` object. For a
description of possible keywords, see:

- %link:manual/python/sampler%


__Returns__

- A SAMPLER object.

__Example__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~



## Synth(osc='sine', freq=440, length=100, attack=0, decay=5, \*\*playback_args)

A factory function that synthesizes a sound and returns it as a
`Sampler` object.


__Parameters__

- **osc**: Oscillator, can be "sine", "saw", "square" or "white_noise".
- **freq**: Frequency, either an integer value (value in hertz) or a string ("A1",
"eb2", etc.).
- **length**: The length of the sound in milliseconds.
- **attack**: The attack (fade-in) time in milliseconds.
- **decay**: The decay (fade-out) time in milliseconds.
- **\*\*playback_args**: Optional playback keywords, such as volume and pan, as described under
[/python/sampler/]().

__Returns__

- A SAMPLER object.

__Example__

~~~ .python
my_sampler = Synth(freq='b2', length=500)
~~~



## copy_sketchpad(name)

Returns a copy of a `sketchpad`'s canvas.


__Parameters__

- **name**: The name of the `sketchpad`.

__Returns__

- A copy of the `sketchpad`'s canvas.

__Example__

~~~ .python
my_canvas = copy_sketchpad('my_sketchpad')
my_canvas.show()
~~~



## pause()

Pauses the experiment.




## register_cleanup_function(fnc)

Registers a clean-up function, which is executed when the experiment
ends. Clean-up functions are executed at the very end, after the display,
sound device, and log file have been closed. Clean-up functions are also
executed when the experiment crashes.



__Example__

~~~ .python
def my_cleanup_function():
        print(u'The experiment is finished!')
register_cleanup_function(my_cleanup_function)
~~~



## reset_feedback()

Resets all feedback variables to their initial state.



__Example__

~~~ .python
reset_feedback()
~~~



## set_subject_nr(nr)

Sets the subject number and parity (even/ odd). This function is called
automatically when an experiment is started, so you only need to call it
yourself if you overwrite the subject number that was specified when the
experiment was launched.


__Parameters__

- **nr**: The subject nr.

__Example__

~~~ .python
set_subject_nr(1)
print('Subject nr = %d' % var.subject_nr)
print('Subject parity = %s' % var.subject_parity)
~~~



## sometimes(p=0.5)

Returns True with a certain probability. (For more advanced
randomization, use the Python `random` module.)


__Parameters__

- **p**: The probability of returning True.

__Returns__

- True or False

__Example__

~~~ .python
if sometimes():
        print('Sometimes you win')
else:
        print('Sometimes you loose')
~~~



## xy_circle(n, rho, phi0=0, pole=(0, 0))

Generates a list of points (x,y coordinates) in a circle. This can be
used to draw stimuli in a circular arrangement.


__Parameters__

- **n**: The number of x,y coordinates to generate.
- **rho**: The radial coordinate, also distance or eccentricity, of the first
point.
- **phi0**: The angular coordinate for the first coordinate. This is a
counterclockwise rotation in degrees (i.e. not radians), where 0 is
straight right.
- **pole**: The reference point.

__Returns__

- A list of (x,y) coordinate tuples.

__Example__

~~~ .python
# Draw 8 rectangles around a central fixation dot
c = Canvas()
c.fixdot()
for x, y in xy_circle(8, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_distance(x1, y1, x2, y2)

Gives the distance between two points.


__Parameters__

- **x1**: The x coordinate of the first point.
- **y1**: The y coordinate of the first point.
- **x2**: The x coordinate of the second point.
- **y2**: The y coordinate of the second point.

__Returns__

- The distance between the two points.


## xy_from_polar(rho, phi, pole=(0, 0))

Converts polar coordinates (distance, angle) to Cartesian coordinates
(x, y).


__Parameters__

- **rho**: The radial coordinate, also distance or eccentricity.
- **phi**: The angular coordinate. This reflects a clockwise rotation in degrees
(i.e. not radians), where 0 is straight right.
- **pole**: The reference point.

__Returns__

- An (x, y) coordinate tuple.

__Example__

~~~ .python
# Draw a cross
x1, y1 = xy_from_polar(100, 45)
x2, y2 = xy_from_polar(100, -45)
c = Canvas()
c.line(x1, y1, -x1, -y1)
c.line(x2, y2, -x2, -y2)
c.show()
~~~



## xy_grid(n, spacing, pole=(0, 0))

Generates a list of points (x,y coordinates) in a grid. This can be
used to draw stimuli in a grid arrangement.


__Parameters__

- **n**: An `int` that indicates the number of columns and rows, so that `n=2`
indicates a 2x2 grid, or a (n_col, n_row) `tuple`, so that `n=(2,3)`
indicates a 2x3 grid.
- **spacing**: A numeric value that indicates the spacing between cells, or a
(col_spacing, row_spacing) tuple.
- **pole**: The reference point.

__Returns__

- A list of (x,y) coordinate tuples.

__Example__

~~~ .python
# Draw a 4x4 grid of rectangles
c = Canvas()
c.fixdot()
for x, y in xy_grid(4, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_random(n, width, height, min_dist=0, pole=(0, 0))

Generates a list of random points (x,y coordinates) with a minimum
spacing between each pair of points. This function will raise an
Exception when the coordinate list cannot be generated,  typically because
there are too many points, the min_dist is set too high, or the width or
height are set too low.


__Parameters__

- **n**: The number of points to generate.
- **width**: The width of the field with random points.
- **height**: The height of the field with random points.
- **min_dist**: The minimum distance between each point.
- **pole**: The reference point.

__Returns__

- A list of (x,y) coordinate tuples.

__Example__

~~~ .python
# Draw a 50 rectangles in a random grid
c = Canvas()
c.fixdot()
for x, y in xy_random(50, 500, 500, min_dist=40):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_to_polar(x, y, pole=(0, 0))

Converts Cartesian coordinates (x, y) to polar coordinates (distance,
angle).


__Parameters__

- **x**: The X coordinate.
- **y**: The Y coordinate.
- **pole**: The reference point.

__Returns__

- An (rho, phi) coordinate tuple. Here, `rho` is the radial coordinate,
also distance or eccentricity. `phi` is the angular coordinate in
degrees (i.e. not radians), and reflects a counterclockwise rotation,
where 0 is straight right.

__Example__

~~~ .python
rho, phi = xy_to_polar(100, 100)
~~~



</div>

