Die `Canvas`-Klasse wird verwendet, um visuelle Reize darzustellen. Im Allgemeinen
erstellt man ein `Canvas`-Objekt mit der `Canvas()`-Factory-Funktion. Da
`Canvas()` eine Funktion ist, muss man bei ihrem Aufruf *nicht* `new` verwenden.
Die JavaScript `Canvas`-Klasse ahmt die entsprechende Python `Canvas`
Klasse nach.

__Style-Keywords__ können an alle Funktionen übergeben werden, die `styleArgs` akzeptieren.
Style-Keywords können auch als Eigenschaften des `Canvas`-Objekts festgelegt werden. Eine Übersicht über die Style-Keywords finden Sie in der
[Python `Canvas` Dokumentation](%url:manual/python/canvas%).

__Wichtig:__ JavaScript unterstützt keine benannten Parameter (oder: Stichworte).
Daher werden Parameter als `Object` mit benannten Eigenschaften und
Standardwerten übergeben. So:

```js
var myCanvas = Canvas()
// (korrekt) Parameter als Object übergeben ...
myCanvas.fixdot({color: 'red'})
// (falsch) ... und *nicht* als benannte Parameter
// myCanvas.fixdot(color='red')
myCanvas.show()
```

[TOC]

<a name="Canvas.arrow"></a>

### Canvas.arrow(obj)
Zeichnet einen Pfeil. Ein Pfeil besteht aus 7 Eckpunkten, mit einer
Pfeilspitze, die auf (ex, ey) zeigt.



| Param | Typ | Standard |
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

**Beispiel**  
```js
var myCanvas = Canvas()
var w = vars.width / 2
var h = vars.height / 2
// Wichtig: Parameter werden als Object übergeben
myCanvas.arrow({sx: 0, sy: 0, w: w, h: h, head_width:100, body_length:0.5})
```
<a name="Canvas.clear"></a>

### Canvas.clear([styleArgs])
Löscht die Leinwand mit der aktuellen Hintergrundfarbe. Beachten Sie, dass es
 im Allgemeinen schneller ist, für jede Experimentanzeige eine andere Leinwand zu verwenden, als eine einzelne Leinwand mehrfach zu löschen und neu zu zeichnen.



| Param | Typ | Standard |
| --- | --- | --- |
| [styleArgs] | <code>Object</code> | <code>{}</code> | 

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.fixdot({color: 'green'})
myCanvas.show()
// etwas tun
myCanvas.clear()
myCanvas.fixdot({color: 'red'})
myCanvas.show()
```
<a name="Canvas.circle"></a>

### Canvas.circle(obj)
Zeichnet einen Kreis.



| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.r | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.circle({x: 100, y: 100, r: 50, fill: true, color:'red'})
```
<a name="Canvas.ellipse"></a>

### Canvas.ellipse(obj)
Zeichnet eine Ellipse.



| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.ellipse({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.fixdot"></a>

### Canvas.fixdot(obj)
Zeichnet einen Fixationspunkt. Der Standardstil ist mittel-offen.

- 'large-filled' ist ein gefüllter Kreis mit einem Radius von 16px.
- 'medium-filled' ist ein gefüllter Kreis mit einem Radius von 8px.
- 'small-filled' ist ein gefüllter Kreis mit einem Radius von 4px.
- 'large-open' ist ein gefüllter Kreis mit einem Radius von 16px und einem 2px Loch.
- 'medium-open' ist ein gefüllter Kreis mit einem Radius von 8px und einem 2px Loch.
- 'small-open' ist ein gefüllter Kreis mit einem Radius von 4px und einem 2px Loch.
- 'large-cross' ist ein 16px Kreuz.
- 'medium-cross' ist ein 8px Kreuz.
- 'small-cross' ist ein 4px Kreuz.

| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  |
| obj.x | <code>Number</code> | <code>0</code> |
| obj.y | <code>Number</code> | <code>0</code> |
| obj.style | <code>String</code> | <code>&#x27;default&#x27;</code> |
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> |

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.fixdot()
```
<a name="Canvas.gabor"></a>

### Canvas.gabor(obj)
Zeichnet einen Gabor-Patch.

| Param | Typ | Standard |
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

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.gabor({x: 100, y: 100, orient: 45, freq: .05})
```
<a name="Canvas.image"></a>

### Canvas.image(obj)
Zeichnet ein Bild aus einer Datei im Dateipool.

| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  |
| obj.fname | <code>String</code> |  |
| obj.center | <code>Boolean</code> | <code>true</code> |
| obj.x | <code>Number</code> | <code>0</code> |
| obj.y | <code>Number</code> | <code>0</code> |
| obj.scale | <code>Number</code> | <code>1</code> |
| obj.rotation | <code>Number</code> | <code>0</code> |
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> |

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.image({fname: 'image_in_pool.png'})
```
<a name="Canvas.line"></a>

### Canvas.line(obj)
Zeichnet eine Linie.

| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  |
| obj.sx | <code>Number</code> | <code>0</code> |
| obj.sy | <code>Number</code> | <code>0</code> |
| obj.ex | <code>Number</code> | <code>50</code> |
| obj.ey | <code>Number</code> | <code>0</code> |
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> |

**Beispiel**  
```js
var myCanvas = Canvas()
var ex = vars.width / 2
var ey = vars.height / 2
myCanvas.line({sx: 0, sy: 0, ex: ex, ey: ey})
```
<a name="Canvas.noise_patch"></a>

### Canvas.noise\_patch(obj)
Zeichnet einen Rauschfleck mit einer Hülle.

| Param | Typ | Standard |
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

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.noise_patch({x: 100, y: 100, env: 'circular'})
```
<a name="Canvas.polygon"></a>

### Canvas.polygon(obj)
Zeichnet ein Polygon, das durch eine Liste von Eckpunkten definiert ist. D.h. eine Form aus
Punkten, die durch Linien verbunden sind.



| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.vertices | <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> |  | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Beispiel**  
```js
var myCanvas = Canvas()
var n1 = [0,0]
var n2 = [100, 100]
var n3 = [0, 100]
myCanvas.polygon({vertices: [n1, n2, n3]})
```
<a name="Canvas.rect"></a>

### Canvas.rect(obj)
Zeichnet ein Rechteck.



| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.rect({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.show"></a>

### Canvas.show() ⇒ <code>Number</code>
Zeigt oder "flippt" das Canvas auf dem Bildschirm.


**Gibt zurück**: <code>Number</code> - Ein Zeitstempel der Zeit, zu der das Canvas auf
    dem Bildschirm erschienen ist.
<a name="Canvas.text"></a>

### Canvas.text(obj)
Zeichnet Text.



| Param | Typ | Standard |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.text | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Beispiel**  
```js
var myCanvas = Canvas()
myCanvas.text({text: 'Etwas Text'})
```