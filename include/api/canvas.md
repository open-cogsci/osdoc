<div class="ClassDoc YAMLDoc" id="canvas" markdown="1">

# class __canvas__

The `canvas` class is used to present visual stimuli.

__Example__:

~~~ .python
# Create and show a canvas with a central fixation dot
my_canvas = canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

[TOC]

## Things to know

### Coordinates

- When *Uniform coordinates* is set to 'yes', coordinates are
  relative to the center of the display. That is, (0,0) is the center.
  This is the default as of OpenSesame 3.0.0.
- When *Uniform coordinates* is set to 'no', coordinates are relative to
  the top-left of the display. That is, (0,0) is the top-left. This was
  the default in OpenSesame 2.9.X and earlier.

### Style keywords

All functions that accept `**style_args` take the following keyword
arguments:

- `color` specifies the foreground color. For valid color
  specifications, see [colors].
- `background_color` specifies the background color. For valid color
  specifications, see [colors].
- `fill` indicates whether rectangles, circles, polygons, and ellipses
  are filled (`True`), or drawn as an outline (`False`).
- `penwidth` indicates a penwidth in pixels and should be `int` or
  `float`.
- `bidi` indicates whether bidirectional-text support is enabled, and
  should be `True` or `False`.
- `html` indicates whether HTML-tags are interpreted, and should be
  `True` or `False`. For supported tags, see [/usage/text/]().
- `font_family` is the name of a font family, such as 'sans'.
- `font_italic` indicates whether text should italics, and should be
  `True` or `False`.
- `font_bold` indicates whether text should bold, and should be
  `True` or `False`.
- `font_underline` indicates whether text should underlined, and should
  be `True` or `False`.

~~~ .python
# Draw a green fixation dot
my_canvas = canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
~~~

Style keywords only affect the current drawing operation (except when
passed to [canvas.\_\_init\_\_][__init__]). To change the style for all
subsequent drawing operations, set style properties, such as
[canvas.color], directly:

~~~ .python
# Draw a red cross with a 2px penwidth
my_canvas = canvas()
my_canvas.color = u'red'
my_canvas.penwidth = 2
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

Or pass the style properties to [canvas.\_\_init\_\_][__init__]:

~~~ .python
# Draw a red cross with a 2px penwidth
my_canvas = canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

### Colors

You can specify colors in the following CSS3-compatible ways:

- __Color names:__ 'red', 'black', etc. A full list of valid color names
  can be found
  [here](http://www.w3.org/TR/SVG11/types.html#ColorKeywords).
- __Seven-character hexadecimal strings:__ '#FF0000', '#000000', etc.
  Here, values range from '00' to 'FF', so that '#FF0000' is bright red.
- __Four-character hexadecimal strings:__ '#F00', '#000', etc. Here,
  values range from '0' to 'F' so that '#F00' is bright red.
- __RGB strings:__ 'rgb(255,0,0)', 'rgb(0,0,0)', etc. Here, values
  range from '0' to '255' so that 'rgb(255,0,0)' is bright red.
- __RGB percentage strings:__ 'rgb(100%,0%,0%)', 'rgb(0%,0%,0%)', etc.
  Here, values range from '0%' to '100%' so that 'rgb(100%,0%,0%)' is
  bright red.
- __RGB tuples:__ `(255, 0, 0)`, `(0, 0 ,0)`, etc. Here, values range
  from `0` to `255` so that `(255,0,0)' is bright red.
- __Luminance values:__  `255`, `0`, etc. Here, values range from `0` to
  `255` so that `255` is white.

~~~ .python
# Various ways to specify green
my_canvas.fixdot(color=u'green')
my_canvas.fixdot(color=u'#00ff00')
my_canvas.fixdot(color=u'#0f0')
my_canvas.fixdot(color=u'rgb(0,255,0)')
my_canvas.fixdot(color=u'rgb(0%,100%,0%)')
my_canvas.fixdot(color=(0,255,0))
# Specify a luminance value (white)
my_canvas.fixdot(color=255)
~~~

%--
constant:
        arg_max_width: |
                The maximum width of the text in pixels, before wrapping to a
                new line, or `None` to wrap at screen edge.
        arg_bgmode: |
                Specifies whether the background is the average of col1 col2
                ('avg', corresponding to a typical Gabor patch), or equal to
                col2 ('col2'), useful for blending into the     background. Note:
                this parameter is ignored by the psycho backend, which uses
                increasing transparency for the background.
        arg_style: |
                Optional [style keywords] that specify the style of the current
                drawing operation. This does not affect subsequent drawing
                operations.
--%

<div class="FunctionDoc YAMLDoc" id="canvas-__init__" markdown="1">

## function __canvas\.\_\_init\_\___\(experiment, auto\_prepare=True, \*\*style\_args\)

Constructor to create a new `canvas` object. You do not generally
call this constructor directly, but use the `canvas()` function,
which is described here: [/python/common/]().

__Example:__

~~~ .python
# Example 1: Show a central fixation dot.
my_canvas = canvas()
my_canvas.fixdot()
my_canvas.show()

# Example 2: Show many randomly positioned fixation dot. Here we
# disable `auto_prepare`, so that drawing goes more quickly.
from random import randint
my_canvas = canvas(auto_prepare=False)
for i in range(1000):
        x = randint(0, my_canvas.width)
        y = randint(0, my_canvas.height)
        my_canvas.fixdot(x, y)
my_canvas.prepare()
my_canvas.show()
~~~

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment

__Keywords:__

- `auto_prepare` -- Indicates whether the canvas should be automatically prepared after each drawing operation, so that [canvas.show] will be maximally efficient. If auto_prepare is turned off, drawing operations may be faster, but [canvas.show] will take longer, unless [canvas.prepare] is explicitly called in advance. Generally, it only makes sense to disable auto_prepare when you want to draw a large number of stimuli, as in the second example below. Currently, the auto_prepare parameter only applies to the xpyriment backend, and is ignored by the other backends.
	- Type: bool
	- Default: True

__Keyword dict:__

- `**style_args`: Optional [style keywords], which will be used as the default for all drawing operations on this `canvas`.

</div>

[canvas.__init__]: #canvas-__init__
[__init__]: #canvas-__init__

<div class="FunctionDoc YAMLDoc" id="canvas-arrow" markdown="1">

## function __canvas\.arrow__\(sx, sy, ex, ey, body\_length=0\.8, body\_width=0\.5, head\_width=30, \*\*style\_args\)

Draws an arrow. An arrow is a polygon consisting of 7 vertices, with an arrowhead pointing at (ex, ey).

__Arguments:__

- `sx` -- The X coordinate of the arrow's base.
	- Type: int
- `sy` -- The Y coordinate of the arrow's base.
	- Type: int
- `ex` -- The X coordinate of the arrow's tip.
	- Type: int
- `ey` -- The Y coordinate of the arrow's tip..
	- Type: int

__Keywords:__

- `body_length` -- Proportional length of the arrow body relative to the full arrow [0-1].
	- Type: float
	- Default: 0.8
- `body_width` -- Proportional width (thickness) of the arrow body relative to the full arrow [0-1].
	- Type: float
	- Default: 0.5
- `head_width` -- Width (thickness) of the arrow head in pixels.
	- Type: float
	- Default: 30

__Keyword dict:__

- `**style_args`: No description.

</div>

[canvas.arrow]: #canvas-arrow
[arrow]: #canvas-arrow

<div class="FunctionDoc YAMLDoc" id="canvas-circle" markdown="1">

## function __canvas\.circle__\(x, y, r, \*\*style\_args\)

Draws a circle.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.circle(100, 100, 50, fill=True, color='red')
~~~

__Arguments:__

- `x` -- The center X coordinate of the circle.
	- Type: int
- `y` -- The center Y coordinate of the circle.
	- Type: int
- `r` -- The radius of the circle.
	- Type: int

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.circle]: #canvas-circle
[circle]: #canvas-circle

<div class="FunctionDoc YAMLDoc" id="canvas-clear" markdown="1">

## function __canvas\.clear__\(color=None, \*\*style\_args\)

Clears the canvas with the current background color. Note that it is generally faster to use a different canvas for each experimental display than to use a single canvas and repeatedly clear and redraw it.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
sleep(1000)
my_canvas.clear()
my_canvas.fixdot(color='red')
my_canvas.show()
~~~

__Keywords:__

- `color` -- Deprecated. Specify `background_color` as part of `style_args` instead.
	- Default: None

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.clear]: #canvas-clear
[clear]: #canvas-clear

<div class="FunctionDoc YAMLDoc" id="canvas-close_display" markdown="1">

## function __canvas\.close\_display__\(experiment\)

Closes the display after the experiment is finished.

__Arguments:__

- `experiment` -- An experiment object.
	- Type: experiment

</div>

[canvas.close_display]: #canvas-close_display
[close_display]: #canvas-close_display

<div class="FunctionDoc YAMLDoc" id="canvas-copy" markdown="1">

## function __canvas\.copy__\(canvas\)

Turns the current `canvas` into a copy of the passed `canvas`.

__Note:__

If you want to create a copy of a SKETCHPAD `canvas`, you can also
use the `inline_script.copy_sketchpad` function.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.fixdot(x=100, color='green')
my_copied_canvas = canvas()
my_copied_canvas.copy(my_canvas)
my_copied_canvas.fixdot(x=200, color="blue")
my_copied_canvas.show()
~~~

__Arguments:__

- `canvas` -- The `canvas` to copy.
	- Type: canvas

</div>

[canvas.copy]: #canvas-copy
[copy]: #canvas-copy

<div class="FunctionDoc YAMLDoc" id="canvas-ellipse" markdown="1">

## function __canvas\.ellipse__\(x, y, w, h, \*\*style\_args\)

Draws an ellipse.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.ellipse(-10, -10, 20, 20, fill=True)
~~~

__Arguments:__

- `x` -- The left X coordinate.
	- Type: int
- `y` -- The top Y coordinate.
	- Type: int
- `w` -- The width.
	- Type: int
- `h` -- The height.
	- Type: int

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.ellipse]: #canvas-ellipse
[ellipse]: #canvas-ellipse

<div class="FunctionDoc YAMLDoc" id="canvas-fixdot" markdown="1">

## function __canvas\.fixdot__\(x=None, y=None, style=u'default', \*\*style\_args\)

Draws a fixation dot. The default style is medium-open.

- 'large-filled' is a filled circle with a 16px radius.
- 'medium-filled' is a filled circle with an 8px radius.
- 'small-filled' is a filled circle with a 4px radius.
- 'large-open' is a filled circle with a 16px radius and a 2px hole.
- 'medium-open' is a filled circle with an 8px radius and a 2px hole.
- 'small-open' is a filled circle with a 4px radius and a 2px hole.
- 'large-cross' is 16px cross.
- 'medium-cross' is an 8px cross.
- 'small-cross' is a 4px cross.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.fixdot()
~~~

__Keywords:__

- `x` -- The X coordinate of the dot center, or None to draw a horizontally centered dot.
	- Type: int, NoneType
	- Default: None
- `y` -- The Y coordinate of the dot center, or None to draw a vertically centered dot.
	- Type: int, NoneType
	- Default: None
- `style` -- The fixation-dot style. One of: default, large-filled,
medium-filled, small-filled, large-open, medium-open,
small-open, large-cross, medium-cross, or small-cross.
default equals medium-open.
	- Type: str, unicode
	- Default: 'default'

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.fixdot]: #canvas-fixdot
[fixdot]: #canvas-fixdot

<div class="FunctionDoc YAMLDoc" id="canvas-gabor" markdown="1">

## function __canvas\.gabor__\(x, y, orient, freq, env=u'gaussian', size=96, stdev=12, phase=0, col1=u'white', col2=u'black', bgmode=u'avg'\)

Draws a Gabor patch. Note: The exact rendering of the Gabor patch
depends on the back-end.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.gabor(100, 100, 45, .05)
~~~

__Arguments:__

- `x` -- The center X coordinate.
	- Type: int
- `y` -- The center Y coordinate.
	- Type: int
- `orient` -- Orientation in degrees [0 .. 360].
	- Type: float, int
- `freq` -- Frequency in cycles/px of the sinusoid.
	- Type: float, int

__Keywords:__

- `env` -- The envelope that determines the shape of the patch. Can be "gaussian", "linear", "circular", or "rectangular".
	- Type: str, unicode
	- Default: 'gaussian'
- `size` -- A size in pixels.
	- Type: float, int
	- Default: 96
- `stdev` -- Standard deviation in pixels of the gaussian. Only applicable to gaussian envelopes.
	- Type: float, int
	- Default: 12
- `phase` -- Phase of the sinusoid [0.0 .. 1.0].
	- Type: float, int
	- Default: 0
- `col1` -- A color for the peaks.
	- Type: str, unicode
	- Default: 'white'
- `col2` -- A color for the troughs. Note: The psycho back-end
ignores this parameter and always uses the inverse of
`col1` for the throughs.
	- Type: str, unicode
	- Default: 'black'
- `bgmode` -- %arg_bgmode
	- Type: str, unicode
	- Default: 'avg'

</div>

[canvas.gabor]: #canvas-gabor
[gabor]: #canvas-gabor

<div class="PropertyDoc YAMLDoc" id="canvas-height" markdown="1">

## property __canvas.height__

The height of the canvas. This is a read-only property.

</div>

[canvas.height]: #canvas-height
[height]: #canvas-height

<div class="FunctionDoc YAMLDoc" id="canvas-image" markdown="1">

## function __canvas\.image__\(fname, center=True, x=None, y=None, scale=None\)

Draws an image from file. This function does not look in the file pool, but takes an absolute path.

__Example:__

~~~ .python
my_canvas = canvas()
# Determine the absolute path:
path = exp.pool[u'image_in_pool.png']
my_canvas.image(path)
~~~

__Arguments:__

- `fname` -- The filename of the image. If this is a `str` it is assumed to be in utf-8 encoding.
	- Type: str, unicode

__Keywords:__

- `center` -- A bool indicating whether coordinates indicate the center (True) or top-left (False).
	- Type: bool
	- Default: True
- `x` -- The X coordinate, or `None` to draw a horizontally centered image.
	- Type: int, NoneType
	- Default: None
- `y` -- The Y coordinate, or `None` to draw a vertically centered image.
	- Type: int, NoneType
	- Default: None
- `scale` -- The scaling factor of the image. `None` or 1 indicate the original size. 2.0 indicates a 200% zoom, etc.
	- Type: float, int, NoneType
	- Default: None

</div>

[canvas.image]: #canvas-image
[image]: #canvas-image

<div class="FunctionDoc YAMLDoc" id="canvas-init_display" markdown="1">

## function __canvas\.init\_display__\(experiment\)

Initializes the display before the experiment begins.

__Arguments:__

- `experiment` -- An experiment object.
	- Type: experiment

</div>

[canvas.init_display]: #canvas-init_display
[init_display]: #canvas-init_display

<div class="FunctionDoc YAMLDoc" id="canvas-line" markdown="1">

## function __canvas\.line__\(sx, sy, ex, ey, \*\*style\_args\)

Draws a line.

__Arguments:__

- `sx` -- The left X coordinate.
	- Type: int
- `sy` -- The top Y coordinate.
	- Type: int
- `ex` -- The right X coordinate.
	- Type: int
- `ey` -- The bottom Y coordinate.
	- Type: int

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.line]: #canvas-line
[line]: #canvas-line

<div class="FunctionDoc YAMLDoc" id="canvas-noise_patch" markdown="1">

## function __canvas\.noise\_patch__\(x, y, env=u'gaussian', size=96, stdev=12, col1=u'white', col2=u'black', bgmode=u'avg'\)

Draws a patch of noise, with an envelope. The exact rendering of the noise patch depends on the back-end.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.noise_patch(100, 100, env='circular')
~~~

__Arguments:__

- `x` -- The center X coordinate.
	- Type: int
- `y` -- The center Y coordinate.
	- Type: int

__Keywords:__

- `env` -- The envelope that determines the shape of the patch. Can be "gaussian", "linear", "circular", or "rectangular".
	- Type: str, unicode
	- Default: 'gaussian'
- `size` -- A size in pixels.
	- Type: float, int
	- Default: 96
- `stdev` -- Standard deviation in pixels of the gaussian. Only applicable to gaussian envelopes.
	- Type: float, int
	- Default: 12
- `col1` -- The first color.
	- Type: str, unicode
	- Default: 'white'
- `col2` -- The second color. Note: The psycho back-end ignores this
parameter and always uses the inverse of `col1`.
	- Type: str, unicode
	- Default: 'black'
- `bgmode` -- %arg_bgmode
	- Type: str, unicode
	- Default: 'avg'

</div>

[canvas.noise_patch]: #canvas-noise_patch
[noise_patch]: #canvas-noise_patch

<div class="FunctionDoc YAMLDoc" id="canvas-polygon" markdown="1">

## function __canvas\.polygon__\(vertices, \*\*style\_args\)

Draws a polygon that defined by a list of vertices. I.e. a shape of points connected by lines.

__Example:__

~~~ .python
my_canvas = canvas()
n1 = 0,0
n2 = 100, 100
n3 = 0, 100
my_canvas.polygon([n1, n2, n3])
~~~

__Arguments:__

- `vertices` -- A list of tuples, where each tuple corresponds to a vertex. For example, [(100,100), (200,100), (100,200)] will draw a triangle.
	- Type: list

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.polygon]: #canvas-polygon
[polygon]: #canvas-polygon

<div class="FunctionDoc YAMLDoc" id="canvas-prepare" markdown="1">

## function __canvas\.prepare__\(\)

Finishes pending canvas operations (if any), so that a subsequent call to [canvas.show] is extra fast. It's only necessary to call this function if you have disabled `auto_prepare` in [canvas.__init__].

</div>

[canvas.prepare]: #canvas-prepare
[prepare]: #canvas-prepare

<div class="FunctionDoc YAMLDoc" id="canvas-rect" markdown="1">

## function __canvas\.rect__\(x, y, w, h, \*\*style\_args\)

Draws a rectangle.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.rect(-10, -10, 20, 20, fill=True)
~~~

__Arguments:__

- `x` -- The left X coordinate.
	- Type: int
- `y` -- The top Y coordinate.
	- Type: int
- `w` -- The width.
	- Type: int
- `h` -- The height.
	- Type: int

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.rect]: #canvas-rect
[rect]: #canvas-rect

<div class="FunctionDoc YAMLDoc" id="canvas-show" markdown="1">

## function __canvas\.show__\(\)

Shows, or 'flips', the canvas on the screen.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.fixdot()
t = my_canvas.show()
exp.set('time_fixdot', t)
~~~

__Returns:__

A timestamp of the time at which the canvas actually appeared on the screen, or a best guess if precise temporal information is not available. For more information about timing, see </misc/timing>. Depending on the back-end the timestamp is an `int` or a `float`.

- Type: int, float

</div>

[canvas.show]: #canvas-show
[show]: #canvas-show

<div class="PropertyDoc YAMLDoc" id="canvas-size" markdown="1">

## property __canvas.size__

The size of the canvas as a `(width, height)` tuple. This is a read-only property.

</div>

[canvas.size]: #canvas-size
[size]: #canvas-size

<div class="FunctionDoc YAMLDoc" id="canvas-text" markdown="1">

## function __canvas\.text__\(text, center=True, x=None, y=None, max\_width=None, \*\*style\_args\)

Draws text.

__Example:__

~~~ .python
my_canvas = canvas()
my_canvas.text('Some text with <b>boldface</b> and <i>italics</i>')
~~~

__Arguments:__

- `text` -- A string of text.
	- Type: str, unicode

__Keywords:__

- `center` -- A bool indicating whether the coordinates reflect the center (True) or top-left (False) of the text.
	- Type: bool
	- Default: True
- `x` -- The X coordinate, or None to draw horizontally centered text.
	- Type: int, NoneType
	- Default: None
- `y` -- The Y coordinate, or None to draw vertically centered text.
	- Type: int, NoneType
	- Default: None
- `max_width` -- %arg_max_width
	- Type: int, NoneType
	- Default: None

__Keyword dict:__

- `**style_args`: %arg_style

</div>

[canvas.text]: #canvas-text
[text]: #canvas-text

<div class="FunctionDoc YAMLDoc" id="canvas-text_size" markdown="1">

## function __canvas\.text\_size__\(text, max\_width=None, \*\*style\_args\)

Determines the size of a text string in pixels.

__Example:__

~~~ .python
my_canvas = canvas()
w, h = my_canvas.text_size('Some text')
~~~

__Arguments:__

- `text` -- A string of text.
	- Type: str, unicode

__Keywords:__

- `max_width` -- %arg_max_width
	- Type: int, NoneType
	- Default: None

__Keyword dict:__

- `**style_args`: %arg_style

__Returns:__

A (width, height) tuple containing the dimensions of the text string.

- Type: tuple

</div>

[canvas.text_size]: #canvas-text_size
[text_size]: #canvas-text_size

<div class="PropertyDoc YAMLDoc" id="canvas-width" markdown="1">

## property __canvas.width__

The width of the canvas. This is a read-only property.

</div>

[canvas.width]: #canvas-width
[width]: #canvas-width

</div>

[canvas]: #canvas

