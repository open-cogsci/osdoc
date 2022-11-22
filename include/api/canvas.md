<div class="ClassDoc YAMLDoc" id="Canvas" markdown="1">

# class __Canvas__

The `Canvas` class is used to present visual stimuli. You generally
create a `Canvas` object with the `Canvas()` factory function, as
described in the section [Creating a Canvas](#creating-a-canvas).

__Example__:

~~~ .python
# Create and show a canvas with a central fixation dot
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

__Example__:

As of OpenSesame 3.2, you can also add `Canvas` elements as objects.
See also the section on [Naming, accessing, and modifying elements](#naming-accessing-and-modifying-elements).

~~~ .python
# Create a canvas with a fixation dot and a rectangle
my_canvas = Canvas()
my_canvas['my_fixdot'] = FixDot()
my_canvas.show()
~~~

[TOC]

## Things to know

### Creating a Canvas

You generally create a `Canvas` with the `Canvas()` factory function:

~~~ .python
my_canvas = Canvas()
~~~

Optionally, you can pass [Style keywords](#style-keywords) to `Canvas()`
to set the default style:

~~~ .python
my_canvas = Canvas(color='green')
my_canvas.fixdot() # Will be green
~~~

### Style keywords

All functions that accept `**style_args` take the following keyword
arguments:

- `color` specifies the foreground color. For valid color
        specifications, see [colors](#colors).
- `background_color` specifies the background color. For valid color
        specifications, see [colors](#colors).
- `fill` indicates whether rectangles, circles, polygons, and ellipses
        are filled (`True`), or drawn as an outline (`False`).
- `penwidth` indicates a penwidth in pixels and should be `int` or
        `float`.
- `html` indicates whether HTML-tags are interpreted, and should be
        `True` or `False`. For supported tags, see [/usage/text/]().
- `font_family` is the name of a font family, such as 'sans'.
- `font_size` is a font size in pixels.
- `font_italic` indicates whether text should italics, and should be
        `True` or `False`.
- `font_bold` indicates whether text should bold, and should be
        `True` or `False`.
- `font_underline` indicates whether text should underlined, and should
        be `True` or `False`.

~~~ .python
# Draw a green fixation dot
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
~~~

Style keywords only affect the current drawing operation (except when
passed to `Canvas()` while creating the `Canvas`). To change the style
for all subsequent drawing operations, set style properties, such as
`canvas.color`, directly:

~~~ .python
# Draw a red cross with a 2px penwidth
my_canvas = Canvas()
my_canvas.color = u'red'
my_canvas.penwidth = 2
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

Or pass the style properties to `Canvas()`:

~~~ .python
# Draw a red cross with a 2px penwidth
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

### Colors

You can specify colors in the following ways. This includes CSS3-type
color specifications, but also supports some extra specifications,
such as CIE l\* a\* b\* color space.

__Version note:__ The `hsv`, `hsl`, and `lab` color spaces are new in
v3.3.0.

- __Color names:__ 'red', 'black', etc. A full list of valid color names
        can be found
        [here](http://www.w3.org/TR/SVG11/types.html#ColorKeywords).
- __Seven-character hexadecimal strings:__ `#FF0000`, `#000000`, etc.
        Here, values range from `00` to `FF`, so that `#FF0000` is bright red.
- __Four-character hexadecimal strings:__ `#F00`, `#000`, etc. Here,
        values range from '0' to 'F' so that `#F00` is bright red.
- __RGB strings:__ `rgb(255,0,0)`, `rgb(0,0,0)`, etc. Here, values
        range from 0 to 255 so that `rgb(255,0,0)` is bright red.
- __RGB percentage strings:__ `rgb(100%,0%,0%)`, `rgb(0%,0%,0%)`, etc.
        Here, values range from 0% to 100% so that `rgb(100%,0%,0%)` is
        bright red.
- __RGB tuples:__ `(255, 0, 0)`, `(0, 0 ,0)`, etc. Here, values range
        from `0` to `255` so that `(255,0,0)' is bright red.
- __HSV strings:__ `hsv(120, 100%, 100%)`. In the [HSV](https://en.wikipedia.org/wiki/HSL_and_HSV)
        color space, the hue parameter is an angle from 0 to 359, and the
        saturation and value parameters are percentages from 0% to 100%.
- __HSL strings:__ `hsl(120, 100%, 50%)`. In the [HSL](https://en.wikipedia.org/wiki/HSL_and_HSV)
        color space, the hue parameter is an angle from 0 to 359, and the
        saturation and lightness parameters are percentages from 0% to 100%.
- __LAB strings:__ `lab(53, -20, 0)`. In the [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)
        color space, the parameters reflect lightness (`l*`),
        green-red axis (`a*`, negative is green), and blue-yellow axis
        (`b*`, negative is blue). This uses the D65 white point and the
        sRGB transfer function, as implemented [here](https://www.psychopy.org/_modules/psychopy/tools/colorspacetools.html).
- __Luminance values:__  `255`, `0`, etc. Here, values range from `0` to
        `255` so that `255` is white.

~~~ .python
# Various ways to specify green
my_canvas.fixdot(color='green')  # Dark green
my_canvas.fixdot(color='#00ff00')
my_canvas.fixdot(color='#0f0')
my_canvas.fixdot(color='rgb(0, 255, 0)')
my_canvas.fixdot(color='rgb(0%, 100%, 0%)')
my_canvas.fixdot(color='hsl(100, 100%, 50%)')
my_canvas.fixdot(color='hsv(0, 100%, 100%)')
my_canvas.fixdot(color='lab(53, -20, 0)')  # Dark green
my_canvas.fixdot(color=(0, 255, 0))
# Specify a luminance value (white)
my_canvas.fixdot(color=255)
~~~

### Naming, accessing, and modifying elements

As of OpenSesame 3.2, the `Canvas` supports an object-based interface
that allows you to name elements, and to access and modify elements
individually, without having to redraw the entire `Canvas`.

For example, the following will first add a red `Line` element to a
`Canvas` and show it, then change the color of the line to green and
show it again, and then finally delete the line and show the canvas
again (which is now blank). The name of the element (`my_line`) is used
to refer to the element for all the operations.

~~~ .python
my_canvas = Canvas()
my_canvas['my_line'] = Line(-100, -100, 100, 100, color='red')
my_canvas.show()
clock.sleep(1000)
my_canvas['my_line'].color = 'green'
my_canvas.show()
clock.sleep(1000)
del my_canvas['my_line']
my_canvas.show()
~~~

You can also add an element without explicitly providing a name for it.
In that case, a name is generated automatically (e.g. `stim0`).

~~~ .python
my_canvas = Canvas()
my_canvas += FixDot()
my_canvas.show()
~~~

If you add a list of elements, they will be automatically grouped
together, and you can refer to the entire group by name.

~~~ .python
my_canvas = Canvas()
my_canvas['my_cross'] = [
        Line(-100, 0, 100, 0),
        Line(0, -100, 0, 100)
]
my_canvas.show()
~~~

To check whether a particular `x,y` coordinate falls within the bounding
rectangle of an element, you can use `in`:

~~~ .python
my_mouse = Mouse(visible=True)
my_canvas = Canvas()
my_canvas['rect'] = Rect(-100, -100, 200, 200)
my_canvas.show()
button, (x, y), time = my_mouse.get_click()
if (x, y) in my_canvas['rect']:
        print('Clicked in rectangle')
else:
        print('Clicked outside of rectangle')
~~~

You can also get a list of the names of all elements that contain an
`x,y` coordinate, using the `Canvas.elements_at()` function, documented
below.

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
                Optional [style keywords](#style-keywords) that specify the
                style of the current drawing operation. This does not affect
                subsequent drawing operations.
        arg_center: |
                A bool indicating whether the coordinates reflect the center
                (`True`) or top-left (`False`) of the text.
--%

<div class="FunctionDoc YAMLDoc" id="Canvas-arrow" markdown="1">

## function __Canvas\.arrow__\(sx, sy, ex, ey, body\_length=0\.8, body\_width=0\.5, head\_width=30, \*\*style\_args\)

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

<div class="PropertyDoc YAMLDoc" id="Canvas-bottom" markdown="1">

## property __Canvas.bottom__

The y coordinate of the bottom edge of the display. This is a read-only property.

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-circle" markdown="1">

## function __Canvas\.circle__\(x, y, r, \*\*style\_args\)

Draws a circle.

__Example:__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.circle(100, 100, 50, fill=True, color='red')
# Element interface
my_canvas['my_circle'] = Circle(100, 100, 50, fill=True, color='red')
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

<div class="FunctionDoc YAMLDoc" id="Canvas-clear" markdown="1">

## function __Canvas\.clear__\(\*\*style\_args\)

Clears the canvas with the current background color. Note that it is generally faster to use a different canvas for each experimental display than to use a single canvas and repeatedly clear and redraw it.

__Example:__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
clock.sleep(1000)
my_canvas.clear()
my_canvas.fixdot(color='red')
my_canvas.show()
~~~

__Keyword dict:__

- `**style_args`: %arg_style

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-copy" markdown="1">

## function __Canvas\.copy__\(canvas\)

Turns the current `Canvas` into a copy of the passed `Canvas`.

__Warning:__

Copying `Canvas` objects can result in unpredictable behavior. In
many cases, a better solution is to recreate multiple `Canvas`
objects from scratch, and/ or to use the element interface to
update `Canvas` elements individually.

__Example:__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(x=100, color='green')
my_copied_canvas = Canvas()
my_copied_canvas.copy(my_canvas)
my_copied_canvas.fixdot(x=200, color="blue")
my_copied_canvas.show()
~~~

__Arguments:__

- `canvas` -- The `Canvas` to copy.
	- Type: canvas

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-elements_at" markdown="1">

## function __Canvas\.elements\_at__\(x, y\)

*New in v3.2.0*

Gets the names of elements that contain a particular `x, y`
coordinate.

__Example:__

~~~ .python
# Create and show a canvas with two partly overlapping rectangles
my_canvas = Canvas()
my_canvas['right_rect'] = Rect(x=-200, y=-100, w=200, h=200, color='red')
my_canvas['left_rect'] = Rect(x=-100, y=-100, w=200, h=200, color='green')
my_canvas.show()
# Collect a mouse click and print the names of the elements that
# contain the clicked point
my_mouse = Mouse(visible=True)
button, pos, time = my_mouse.get_click()
if pos is not None:
    x, y = pos
    print('Clicked on elements: %s' % my_canvas.elements_at(x, y))
~~~

__Arguments:__

- `x` -- An X coordinate.
	- Type: int, float
- `y` -- A Y coordinate.
	- Type: int, float

__Returns:__

A `list` of element names that contain the coordinate `x, y`.

- Type: list

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-ellipse" markdown="1">

## function __Canvas\.ellipse__\(x, y, w, h, \*\*style\_args\)

Draws an ellipse.

__Example:__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.ellipse(-10, -10, 20, 20, fill=True)
# Element interface
my_canvas['my_ellipse'] = Ellipse(-10, -10, 20, 20, fill=True)
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

<div class="FunctionDoc YAMLDoc" id="Canvas-fixdot" markdown="1">

## function __Canvas\.fixdot__\(x=None, y=None, style=u'default', \*\*style\_args\)

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
my_canvas = Canvas()
# Function interface
my_canvas.fixdot()
# Element interface
my_canvas['my_fixdot'] = FixDot()
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

<div class="FunctionDoc YAMLDoc" id="Canvas-gabor" markdown="1">

## function __Canvas\.gabor__\(x, y, orient, freq, env=u'gaussian', size=96, stdev=12, phase=0, col1=u'white', col2=u'black', bgmode=u'avg'\)

Draws a Gabor patch. Note: The exact rendering of the Gabor patch
depends on the back-end.

__Example:__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.gabor(100, 100, 45, .05)
# Element interface
my_canvas['my_gabor'] = Gabor(100, 100, 45, .05)
~~~

__Arguments:__

- `x` -- The center X coordinate.
	- Type: int
- `y` -- The center Y coordinate.
	- Type: int
- `orient` -- Orientation in degrees [0 .. 360]. This refers to a
clockwise rotation from a vertical.

__Version note:__ In version 3.2.6 and earlier, the
orientation was *counterclockwise* for the *legacy* and
*xpyriment* backends, and clockwise for the *psycho*
backends. As of 3.2.7, the orientation is *clockwise*
for all backends.
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

<div class="PropertyDoc YAMLDoc" id="Canvas-height" markdown="1">

## property __Canvas.height__

The height of the canvas. This is a read-only property.

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-image" markdown="1">

## function __Canvas\.image__\(fname, center=True, x=None, y=None, scale=None, rotation=None\)

Draws an image from file. This function does not look in the file pool, but takes an absolute path.

__Example:__

~~~ .python
my_canvas = Canvas()
# Determine the absolute path:
path = exp.pool[u'image_in_pool.png']
# Function interface
my_canvas.image(path)
# Element interface
my_canvas['my_image'] = Image(path)
~~~

__Arguments:__

- `fname` -- The filename of the image. When using Python 2, this should be either `unicode` or a utf-8-encoded `str`. When using Python 3, this should be either `str` or a utf-8-encoded `bytes`.
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
- `rotation` -- The rotation of the image `None` or 0 indicate the original rotation. Positive values indicate a clockwise rotation in degrees.
	- Type: float, int, NoneType
	- Default: None

</div>

<div class="PropertyDoc YAMLDoc" id="Canvas-left" markdown="1">

## property __Canvas.left__

The x coordinate of the left edge of the display. This is a read-only property.

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-line" markdown="1">

## function __Canvas\.line__\(sx, sy, ex, ey, \*\*style\_args\)

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

<div class="FunctionDoc YAMLDoc" id="Canvas-lower_to_bottom" markdown="1">

## function __Canvas\.lower\_to\_bottom__\(element\)

Lowers an element to the bottom, so that it is drawn first; that is, it becomes the background.

__Arguments:__

- `element` -- A SKETCHPAD element, or its name.
	- Type: Element, str

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-noise_patch" markdown="1">

## function __Canvas\.noise\_patch__\(x, y, env=u'gaussian', size=96, stdev=12, col1=u'white', col2=u'black', bgmode=u'avg'\)

Draws a patch of noise, with an envelope. The exact rendering of the noise patch depends on the back-end.

__Example:__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.noise_patch(100, 100, env='circular')
# Element interface
my_canvas['my_noise_patch'] = NoisePatch(100, 100, env='circular')
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

<div class="FunctionDoc YAMLDoc" id="Canvas-polygon" markdown="1">

## function __Canvas\.polygon__\(vertices, \*\*style\_args\)

Draws a polygon that defined by a list of vertices. I.e. a shape of points connected by lines.

__Example:__

~~~ .python
my_canvas = Canvas()
n1 = 0,0
n2 = 100, 100
n3 = 0, 100
# Function interface
my_canvas.polygon([n1, n2, n3])
# Element interface
my_canvas['my_polygon'] = Polygon([n1, n2, n3])
~~~

__Arguments:__

- `vertices` -- A list of tuples, where each tuple corresponds to a vertex. For example, [(100,100), (200,100), (100,200)] will draw a triangle.
	- Type: list

__Keyword dict:__

- `**style_args`: %arg_style

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-raise_to_top" markdown="1">

## function __Canvas\.raise\_to\_top__\(element\)

Raises an element to the top, so that it is drawn last; that is, it becomes the foreground.

__Arguments:__

- `element` -- A SKETCHPAD element, or its name.
	- Type: Element, str

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-rect" markdown="1">

## function __Canvas\.rect__\(x, y, w, h, \*\*style\_args\)

Draws a rectangle.

__Example:__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.rect(-10, -10, 20, 20, fill=True)
# Element interface
my_canvas['my_rect'] = Rect(-10, -10, 20, 20, fill=True)
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

<div class="PropertyDoc YAMLDoc" id="Canvas-right" markdown="1">

## property __Canvas.right__

The x coordinate of the right edge of the display. This is a read-only property.

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-show" markdown="1">

## function __Canvas\.show__\(\)

Shows, or 'flips', the canvas on the screen.

__Example:__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
t = my_canvas.show()
exp.set('time_fixdot', t)
~~~

__Returns:__

A timestamp of the time at which the canvas actually appeared on the screen, or a best guess if precise temporal information is not available. For more information about timing, see </misc/timing>. Depending on the back-end the timestamp is an `int` or a `float`.

- Type: int, float

</div>

<div class="PropertyDoc YAMLDoc" id="Canvas-size" markdown="1">

## property __Canvas.size__

The size of the canvas as a `(width, height)` tuple. This is a read-only property.

</div>

<div class="FunctionDoc YAMLDoc" id="Canvas-text" markdown="1">

## function __Canvas\.text__\(text, center=True, x=None, y=None, max\_width=None, \*\*style\_args\)

Draws text.

__Example:__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.text('Some text with <b>boldface</b> and <i>italics</i>')
# Element interface
my_canvas['my_text'] = Text('Some text with <b>boldface</b> and <i>italics</i>')
~~~

__Arguments:__

- `text` -- A string of text. When using Python 2, this should be either `unicode` or a utf-8-encoded `str`. When using Python 3, this should be either `str` or a utf-8-encoded `bytes`.
	- Type: str, unicode

__Keywords:__

- `center` -- %arg_center
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

<div class="FunctionDoc YAMLDoc" id="Canvas-text_size" markdown="1">

## function __Canvas\.text\_size__\(text, center=True, max\_width=None, \*\*style\_args\)

Determines the size of a text string in pixels.

__Example:__

~~~ .python
my_canvas = Canvas()
w, h = my_canvas.text_size('Some text')
~~~

__Arguments:__

- `text` -- A string of text.
	- Type: str, unicode

__Keywords:__

- `center` -- %arg_center
	- Type: bool
	- Default: True
- `max_width` -- %arg_max_width
	- Type: int, NoneType
	- Default: None

__Keyword dict:__

- `**style_args`: %arg_style

__Returns:__

A (width, height) tuple containing the dimensions of the text string.

- Type: tuple

</div>

<div class="PropertyDoc YAMLDoc" id="Canvas-top" markdown="1">

## property __Canvas.top__

The y coordinate of the top edge of the display. This is a read-only property.

</div>

<div class="PropertyDoc YAMLDoc" id="Canvas-width" markdown="1">

## property __Canvas.width__

The width of the canvas. This is a read-only property.

</div>

</div>

