The `Canvas` class is used to present visual stimuli. You generally
create a `Canvas` object with the `Canvas()` factory function. Because
`Canvas()` is a function, you do *not* need to use `new` when calling it.
The JavaScript `Canvas` class mimicks the corresponding Python `Canvas`
class.

__Style keywords__ can be passed to all functions that accept `styleArgs`.
Style keywords can also be set as properties of the `Canvas` object. For an
overview of style keywords, see the
[Python `Canvas` documentation](%url:manual/python/canvas%).

__Important:__ JavaScript doesn't support named parameters (or: keywords).
Therefore, parameters are passed an `Object` with named properties and
default values. Like so:

```js
var myCanvas = Canvas()
// (correct) pass parameters as an Object ...
myCanvas.fixdot({color: 'red'})
// (incorrect) ... and *not* as named parameters
// myCanvas.fixdot(color='red')
myCanvas.show()
```

[TOC]

<a name="Canvas.arrow"></a>

### Canvas.arrow(obj)
Draws an arrow. An arrow is a polygon consisting of 7 vertices, with an
arrowhead pointing at (ex, ey).



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.sx | <code>Number</code> | <code>0</code> | 
| obj.sy | <code>Number</code> | <code>0</code> | 
| obj.ex | <code>Number</code> | <code>50</code> | 
| obj.ey | <code>Number</code> | <code>0</code> | 
| obj.body_length | <code>Number</code> | <code>0.8</code> | 
| obj.body_width | <code>Number</code> | <code>0.5</code> | 
| obj.head_width | <code>Number</code> | <code>30</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
var w = vars.width / 2
var h = vars.height / 2
// Important: parameters are passed as an Object
myCanvas.arrow({sx: 0, sy: 0, w: w, h: h, head_width:100, body_length:0.5})
```
<a name="Canvas.clear"></a>

### Canvas.clear([styleArgs])
Clears the canvas with the current background color. Note that it is
	 generally faster to use a different canvas for each experimental
	 display than to use a single canvas and repeatedly clear and redraw
	 it.



| Param | Type | Default |
| --- | --- | --- |
| [styleArgs] | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.fixdot({color: 'green'})
myCanvas.show()
// do something
myCanvas.clear()
myCanvas.fixdot({color: 'red'})
myCanvas.show()
```
<a name="Canvas.circle"></a>

### Canvas.circle(obj)
Draws a circle.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.r | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.circle({x: 100, y: 100, r: 50, fill: true, color:'red'})
```
<a name="Canvas.ellipse"></a>

### Canvas.ellipse(obj)
Draws an ellipse.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.ellipse({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.fixdot"></a>

### Canvas.fixdot(obj)
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



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.style | <code>String</code> | <code>&#x27;default&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.fixdot()
```
<a name="Canvas.gabor"></a>

### Canvas.gabor(obj)
Draws a gabor patch.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.orient | <code>Number</code> | <code>0</code> | 
| obj.freq | <code>Number</code> | <code>.1</code> | 
| obj.env | <code>String</code> | <code>&#x27;gaussian&#x27;</code> | 
| obj.size | <code>Number</code> | <code>96</code> | 
| obj.stdev | <code>Number</code> | <code>12</code> | 
| obj.phase | <code>Number</code> | <code>0</code> | 
| obj.col1 | <code>String</code> | <code>&#x27;white&#x27;</code> | 
| obj.col2 | <code>String</code> | <code>&#x27;black&#x27;</code> | 
| obj.bgmode | <code>String</code> | <code>&#x27;avg&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.gabor({x: 100, y: 100, orient: 45, freq: .05})
```
<a name="Canvas.image"></a>

### Canvas.image(obj)
Draws an image from a file in the file pool.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.fname | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.scale | <code>Number</code> | <code>1</code> | 
| obj.rotation | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.image({fname: 'image_in_pool.png'})
```
<a name="Canvas.line"></a>

### Canvas.line(obj)
Draws a line.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.sx | <code>Number</code> | <code>0</code> | 
| obj.sy | <code>Number</code> | <code>0</code> | 
| obj.ex | <code>Number</code> | <code>50</code> | 
| obj.ey | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
var ex = vars.width / 2
var ey = vars.height / 2
myCanvas.line({sx: 0, sy: 0, ex: ex, ey: ey})
```
<a name="Canvas.noise_patch"></a>

### Canvas.noise\_patch(obj)
Draws a patch of noise, with an envelope.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.env | <code>String</code> | <code>&#x27;gaussian&#x27;</code> | 
| obj.size | <code>Number</code> | <code>96</code> | 
| obj.stdev | <code>Number</code> | <code>12</code> | 
| obj.col1 | <code>String</code> | <code>&#x27;white&#x27;</code> | 
| obj.col2 | <code>String</code> | <code>&#x27;black&#x27;</code> | 
| obj.bgmode | <code>String</code> | <code>&#x27;avg&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.noise_patch({x: 100, y: 100, env: 'circular'})
```
<a name="Canvas.polygon"></a>

### Canvas.polygon(obj)
Draws a polygon that defined by a list of vertices. I.e. a shape of
points connected by lines.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.vertices | <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> |  | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
var n1 = [0,0]
var n2 = [100, 100]
var n3 = [0, 100]
myCanvas.polygon({vertices: [n1, n2, n3]})
```
<a name="Canvas.rect"></a>

### Canvas.rect(obj)
Draws a rectangle.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.rect({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.show"></a>

### Canvas.show() ⇒ <code>Number</code>
Shows, or 'flips', the canvas on the screen.


**Returns**: <code>Number</code> - A timestamp of the time at which the canvas appeared on
    the screen.  
<a name="Canvas.text"></a>

### Canvas.text(obj)
Draws text.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.text | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Example**  
```js
var myCanvas = Canvas()
myCanvas.text({text: 'Some text'})
```
