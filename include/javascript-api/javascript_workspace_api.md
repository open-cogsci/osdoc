

## reset\_feedback()
Resets all feedback variables to their initial state.


**Example**  
```js
reset_feedback()
```
<a name="set_subject_nr"></a>

## set\_subject\_nr(nr)
Sets the subject number and parity (even/ odd). This function is called
automatically when an experiment is started, so you only need to call it
yourself if you overwrite the subject number that was specified when the
experiment was launched.



| Param | Type | Description |
| --- | --- | --- |
| nr | <code>Number</code> | The subject number |

**Example**  
```js
set_subject_nr(1)
console.log('Subject nr = ' + vars.subject_nr)
console.log('Subject parity = ' + vars.subject_parity)
```
<a name="sometimes"></a>

## sometimes([p])
Returns true with a certain probability. (For more advanced randomization,
use the `random-ext` package, which is available as `random`.)



| Param | Type | Default | Description |
| --- | --- | --- | --- |
| [p] | <code>Number</code> | <code>.5</code> | The probability of returning true |

**Example**  
```js
if (sometimes()) {
  console.log('Sometimes you win')
} else {
  console.log('Sometimes you lose')
}
```
<a name="xy_from_polar"></a>

## xy\_from\_polar(rho, phi, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Converts polar coordinates (distance, angle) to Cartesian coordinates
(x, y).


**Returns**: <code>Array.&lt;Number&gt;</code> - An [x, y] array.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| rho | <code>Number</code> |  | The radial coordinate, also distance or eccentricity. |
| phi | <code>Number</code> |  | The angular coordinate. This reflects a clockwise     rotation in degrees (i.e. not radians), where 0 is straight right. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | The reference point. |

**Example**  
```js
// ECMA 5.1
var xy1 = xy_from_polar(100, 45)
var xy2 = xy_from_polar(100, -45)
var c = Canvas()
c.line({sx: xy1[0], sy: xy1[1], ex: -xy1[0], ey: -xy1[1]})
c.line({sx: xy2[0], sy: xy2[1], ex: -xy2[0], ey: -xy2[1]})
c.show()
// ECMA 6
let [x1, y1] = xy_from_polar(100, 45)
let [x2, y2] = xy_from_polar(100, -45)
let c = Canvas()
c.line({sx: x1, sy: y1, ex: -x1, ey: -y1})
c.line({sx: x2, sy: y2, ex: -x2, ey: -y2})
c.show()
```
<a name="xy_to_polar"></a>

## xy\_to\_polar(x, y, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Converts Cartesian coordinates (x, y) to polar coordinates (distance,
angle).


**Returns**: <code>Array.&lt;Number&gt;</code> - An [rho, phi] array. Here, `rho` is the radial
    coordinate, also distance or eccentricity. `phi` is the angular
    coordinate in degrees (i.e. not radians), and reflects a
    counterclockwise rotation, where 0 is straight right.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| x | <code>Number</code> |  | The X coordinate. |
| y | <code>Number</code> |  | The Y coordinate |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | The reference point. |

**Example**  
```js
// ECMA 5.1 (browser + desktop)
var rho_phi = xy_to_polar(100, 100)
var rho = rho_phi[0]
var phi = rho_phi[1]
// ECMA 6 (browser only)
let [rho, phi] = xy_to_polar(100, 100)
```
<a name="xy_distance"></a>

## xy\_distance(x1, y1, x2, y2) ⇒ <code>Number</code>
Gives the distance between two points.


**Returns**: <code>Number</code> - The distance between the two points.  

| Param | Type | Description |
| --- | --- | --- |
| x1 | <code>Number</code> | The x coordinate of the first point. |
| y1 | <code>Number</code> | The y coordinate of the first point. |
| x2 | <code>Number</code> | The x coordinate of the second point. |
| y2 | <code>Number</code> | The y coordinate of the second point. |

<a name="xy_circle"></a>

## xy\_circle(n, rho, [phi0], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Generates a list of points (x,y coordinates) in a circle. This can be
used to draw stimuli in a circular arrangement.


**Returns**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - An array of [x,y] coordinate arrays.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | The number of x,y coordinates to generate. |
| rho | <code>Number</code> |  | The radial coordinate, also distance or eccentricity,     of the first point. |
| [phi0] | <code>Number</code> | <code>0</code> | The angular coordinate for the first coordinate.     This is a counterclockwise rotation in degrees (i.e. not radians),     where 0 is straight right. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | The reference point. |

**Example**  
```js
// Draw 8 rectangles around a central fixation dot
// ECMA 5.1 (browser + desktop)
var c = Canvas()
c.fixdot()
var points = xy_circle(8, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (browser only)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_circle(8, 100)) {
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
```
<a name="xy_grid"></a>

## xy\_grid(n, spacing, [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Generates a list of points (x,y coordinates) in a grid. This can be used
to draw stimuli in a grid arrangement.


**Returns**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - An array of [x,y] coordinate arrays.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| n | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | A number that indicates the number of     columns and rows, so that `n=2` indicates a 2x2 grid, or a [n_col,     n_row] array, so that `n=[2,3]` indicates a 2x3 grid. |
| spacing | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | A numeric value that indicates the     spacing between cells, or a [col_spacing, row_spacing] array. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | The reference point. |

**Example**  
```js
// Draw a 4x4 grid of rectangles
// ECMA 5 (desktop + browser)
var c = Canvas()
c.fixdot()
var points = xy_grid(4, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (browser only)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_grid(4, 100)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```
<a name="xy_random"></a>

## xy\_random(n, width, height, [min_dist], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Generates a list of random points (x,y coordinates) with a minimum
spacing between each pair of points. This function will throw an error
when the coordinate list cannot be generated, typically because there are
too many points, the min_dist is set too high, or the width or height are
set too low.


**Returns**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - An array of [x,y] coordinate arrays.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | The number of points to generate. |
| width | <code>Number</code> |  | The width of the field with random points. |
| height | <code>Number</code> |  | The height of the field with random points. |
| [min_dist] | <code>Number</code> | <code>0</code> | The minimum distance between each point. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | The reference point. |

**Example**  
```js
// Draw a 50 rectangles in a random grid
// ECMA 5 (desktop + browser)
var c = Canvas()
c.fixdot()
var points = xy_random(50, 500, 500, 40)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()   
// ECMA 6 (browser only)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_random(50, 500, 500, 40)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```
