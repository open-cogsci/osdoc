`Canvas`类用于呈现视觉刺激。您通常可以通过`Canvas()`工厂函数创建一个`Canvas`对象。因为`Canvas()`是一个函数，所以调用它时*不*需要使用`new`。JavaScript `Canvas`类模仿了相应的Python `Canvas`类。

__样式关键词__可以传递给所有接受`styleArgs`的函数。样式关键词也可以设置为`Canvas`对象的属性。有关样式关键词的概述，请参阅[Python `Canvas`文档](%url:manual/python/canvas/)。

__重要提示：__ JavaScript不支持命名参数（或称：关键字）。因此，参数通过带有命名属性和默认值的`Object`传递。就像这样：

```js
var myCanvas = Canvas()
// （正确）将参数作为对象传递...
myCanvas.fixdot({color: 'red'})
// （错误）...而不是作为命名参数
// myCanvas.fixdot(color='red')
myCanvas.show()
```

[TOC]

<a name="Canvas.arrow"></a>

### Canvas.arrow(obj)
绘制一个箭头。箭头是由7个顶点组成的多边形，箭头指向（ex，ey）。



| 参数 | 类型 | 默认值 |
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

**示例**  
```js
var myCanvas = Canvas()
var w = vars.width / 2
var h = vars.height / 2
// 重要：参数作为一个对象传递
myCanvas.arrow({sx: 0, sy: 0, w: w, h: h, head_width:100, body_length:0.5})
```
<a name="Canvas.clear"></a>

### Canvas.clear([styleArgs])
以当前背景颜色清除画布。注意，通常使用不同的画布为每个实验
	 显示比使用单个画布并反复清除和重绘
	 这是更快的。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| [styleArgs] | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.fixdot({color: 'green'})
myCanvas.show()
// 做某事
myCanvas.clear()
myCanvas.fixdot({color: 'red'})
myCanvas.show()
```
<a name="Canvas.circle"></a>

### Canvas.circle(obj)
绘制一个圆。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.r | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.circle({x: 100, y: 100, r: 50, fill: true, color:'red'})
```
<a name="Canvas.ellipse"></a>

### Canvas.ellipse(obj)
绘制一个椭圆。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.ellipse({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.fixdot"></a>

### Canvas.fixdot(obj)
绘制一个固定点。默认样式为中等打开。

- 'large-filled' 是一个半径为 16px 的实心圆。
- 'medium-filled' 是一个半径为 8px 的实心圆。
- 'small-filled' 是一个半径为 4px 的实心圆。
- 'large-open' 是一个半径为 16px，中心区域为 2px 空隙的实心圆。
- 'medium-open' 是一个半径为 8px，中心区域为 2px 空隙的实心圆。
- 'small-open' 是一个半径为 4px，中心区域为 2px 空隙的实心圆。
- 'large-cross' 是一个 16px 的十字形。
- 'medium-cross' 是一个 8px 的十字形。
- 'small-cross' 是一个 4px 的十字形。

| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.style | <code>String</code> | <code>&#x27;default&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.fixdot()
```
<a name="Canvas.gabor"></a>

### Canvas.gabor(obj)
绘制一个 gabor 斑块。



| 参数 | 类型 | 默认值 |
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

**示例**  
```js
var myCanvas = Canvas()
myCanvas.gabor({x: 100, y: 100, orient: 45, freq: .05})
```
<a name="Canvas.image"></a>

### Canvas.image(obj)
从文件池的文件中绘制图像。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.fname | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.scale | <code>Number</code> | <code>1</code> | 
| obj.rotation | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.image({fname: 'image_in_pool.png'})
```
<a name="Canvas.line"></a>

### Canvas.line(obj)
绘制直线。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.sx | <code>Number</code> | <code>0</code> | 
| obj.sy | <code>Number</code> | <code>0</code> | 
| obj.ex | <code>Number</code> | <code>50</code> | 
| obj.ey | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
var ex = vars.width / 2
var ey = vars.height / 2
myCanvas.line({sx: 0, sy: 0, ex: ex, ey: ey})
```
<a name="Canvas.noise_patch"></a>

### Canvas.noise\_patch(obj)
绘制一个具有包络的噪声补丁。



| 参数 | 类型 | 默认值 |
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

**示例**  
```js
var myCanvas = Canvas()
myCanvas.noise_patch({x: 100, y: 100, env: 'circular'})
```
<a name="Canvas.polygon"></a>

### Canvas.polygon(obj)
绘制由顶点列表定义的多边形。即由线连接的点构成的形状。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.vertices | <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> |  | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
var n1 = [0,0]
var n2 = [100, 100]
var n3 = [0, 100]
myCanvas.polygon({vertices: [n1, n2, n3]})
```
<a name="Canvas.rect"></a>

### Canvas.rect(obj)
绘制矩形。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.rect({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.show"></a>

### Canvas.show() ⇒ <code>Number</code>
显示或"翻转"屏幕上的画布。


**返回**: <code>Number</code> - 画布出现在屏幕上的时间的时间戳。  
<a name="Canvas.text"></a>

### Canvas.text(obj)
绘制文本。



| 参数 | 类型 | 默认值 |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.text | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**示例**  
```js
var myCanvas = Canvas()
myCanvas.text({text: 'Some text'})
```