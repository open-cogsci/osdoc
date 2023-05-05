La clase `Canvas` se utiliza para presentar estímulos visuales. Generalmente
se crea un objeto `Canvas` con la función de fábrica `Canvas()`. Debido a que
`Canvas()` es una función, *no* es necesario usar `new` al llamarla.
La clase de JavaScript `Canvas` imita la clase `Canvas` de Python correspondiente.

__Palabras clave de estilo__ se pueden pasar a todas las funciones que aceptan `styleArgs`.
Las palabras clave de estilo también se pueden establecer como propiedades del objeto `Canvas`. Para una
descripción general de las palabras clave de estilo, consulte la
[Documentación de `Canvas` en Python](%url:manual/python/canvas%).

__Importante:__ JavaScript no admite parámetros con nombre (o: palabras clave).
Por lo tanto, los parámetros se pasan como un `Object` con propiedades nombradas y
valores predeterminados. Así:

```js
var myCanvas = Canvas()
// (correcto) pasar parámetros como un objeto ...
myCanvas.fixdot({color: 'red'})
// (incorrecto) ... y *no* como parámetros nombrados
// myCanvas.fixdot(color='red')
myCanvas.show()
```

[TOC]

<a name="Canvas.arrow"></a>

### Canvas.arrow(obj)
Dibuja una flecha. Una flecha es un polígono compuesto por 7 vértices, con una
cabeza de flecha apuntando a (ex, ey).



| Param | Tipo | Predeterminado |
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

**Ejemplo**  
```js
var myCanvas = Canvas()
var w = vars.width / 2
var h = vars.height / 2
// Importante: los parámetros se pasan como un objeto
myCanvas.arrow({sx: 0, sy: 0, w: w, h: h, head_width:100, body_length:0.5})
```
<a name="Canvas.clear"></a>

### Canvas.clear([styleArgs])
Limpia el lienzo con el color de fondo actual. Tenga en cuenta que es
	 generalmente más rápido usar un lienzo diferente para cada pantalla experimental
	 que usar un único lienzo y borrarlo y volver a dibujarlo
	 repetidamente.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| [styleArgs] | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.fixdot({color: 'green'})
myCanvas.show()
// hacer algo
myCanvas.clear()
myCanvas.fixdot({color: 'red'})
myCanvas.show()
```
<a name="Canvas.circle"></a>

### Canvas.circle(obj)
Dibuja un círculo.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.r | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.circle({x: 100, y: 100, r: 50, fill: true, color:'red'})
```
<a name="Canvas.ellipse"></a>

### Canvas.ellipse(obj)
Dibuja una elipse.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.ellipse({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.fixdot"></a>

### Canvas.fixdot(obj)
Dibuja un punto de fijación. El estilo predeterminado es medium-open.

- 'large-filled' es un círculo relleno con un radio de 16px.
- 'medium-filled' es un círculo relleno con un radio de 8px.
- 'small-filled' es un círculo relleno con un radio de 4px.
- 'large-open' es un círculo relleno con un radio de 16px y un agujero de 2px.
- 'medium-open' es un círculo relleno con un radio de 8px y un agujero de 2px.
- 'small-open' es un círculo relleno con un radio de 4px y un agujero de 2px.
- 'large-cross' es una cruz de 16px.
- 'medium-cross' es una cruz de 8px.
- 'small-cross' es una cruz de 4px.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.style | <code>String</code> | <code>&#x27;default&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.fixdot()
```
<a name="Canvas.gabor"></a>

### Canvas.gabor(obj)
Dibuja un parche de Gabor.



| Param | Tipo | Predeterminado |
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

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.gabor({x: 100, y: 100, orient: 45, freq: .05})
```
<a name="Canvas.image"></a>

### Canvas.image(obj)
Dibuja una imagen de un archivo en la piscina de archivos.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.fname | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.scale | <code>Number</code> | <code>1</code> | 
| obj.rotation | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.image({fname: 'image_in_pool.png'})
```
<a name="Canvas.line"></a>

### Canvas.line(obj)
Dibuja una línea.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.sx | <code>Number</code> | <code>0</code> | 
| obj.sy | <code>Number</code> | <code>0</code> | 
| obj.ex | <code>Number</code> | <code>50</code> | 
| obj.ey | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
var ex = vars.width / 2
var ey = vars.height / 2
myCanvas.line({sx: 0, sy: 0, ex: ex, ey: ey})
```
<a name="Canvas.noise_patch"></a>

### Canvas.noise\_patch(obj)
Dibuja un parche de ruido, con un sobre.



| Param | Tipo | Predeterminado |
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

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.noise_patch({x: 100, y: 100, env: 'circular'})
```
<a name="Canvas.polygon"></a>

### Canvas.polygon(obj)
Dibuja un polígono definido por una lista de vértices. Es decir, una forma de
puntos conectados por líneas.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.vertices | <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> |  | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
var n1 = [0,0]
var n2 = [100, 100]
var n3 = [0, 100]
myCanvas.polygon({vertices: [n1, n2, n3]})
```
<a name="Canvas.rect"></a>

### Canvas.rect(obj)
Dibuja un rectángulo.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.rect({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.show"></a>

### Canvas.show() ⇒ <code>Number</code>
Muestra, o 'voltea', el canvas en la pantalla.


**Devuelve**: <code>Number</code> - Una marca de tiempo en la que el lienzo apareció en
    la pantalla.
<a name="Canvas.text"></a>

### Canvas.text(obj)
Dibuja texto.



| Param | Tipo | Predeterminado |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.text | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Ejemplo**  
```js
var myCanvas = Canvas()
myCanvas.text({text: 'Algún texto'})
```