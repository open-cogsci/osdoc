## reset\_feedback()
重置所有反馈变量为初始状态。

**示例**  
```js
reset_feedback()
```
<a name="set_subject_nr"></a>

## set\_subject\_nr(nr)
设置受试者编号和奇偶性。当实验开始时，该函数会被自动调用，因此您只需在覆盖实验启动时指定的主题编号时才需调用它。



| 参数 | 类型 | 描述 |
| --- | --- | --- |
| nr | <code>Number</code> | 受试者编号 |

**示例**  
```js
set_subject_nr(1)
console.log('Subject nr = ' + vars.subject_nr)
console.log('Subject parity = ' + vars.subject_parity)
```
<a name="sometimes"></a>

## sometimes([p])
以一定的概率返回真。 (对于更高级的随机化，使用 `random-ext` 包，可用作 `random`。)



| 参数 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| [p] | <code>Number</code> | <code>.5</code> | 返回 true 的概率 |

**示例**  
```js
if (sometimes()) {
  console.log('有时候你赢了')
} else {
  console.log('有时候你输了')
}
```
<a name="xy_from_polar"></a>

## xy\_from\_polar(rho, phi, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
将极坐标 (距离、角度) 转换为笛卡尔坐标 (x, y)。

**返回**: <code>Array.&lt;Number&gt;</code> - 一个 [x, y] 数组。  

| 参数 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| rho | <code>Number</code> |  | 径向坐标，也称为距离或偏心率。 |
| phi | <code>Number</code> |  | 角坐标。 这反映了顺时针 旋转的角度（即不是弧度），其中 0 是直接向右。 |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | 参考点。 |

**示例**  
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
将笛卡尔坐标（x，y）转换为极坐标（距离，角度）。

**返回**: <code>Array.&lt;Number&gt;</code> - 一个 [rho, phi] 数组。 这里，“rho”是径向 坐标，也是距离或偏心率。`phi`是角度坐标（以度为单位，即不是弧度），反映了逆时针旋转，其中0为直接向右。  

| 参数 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| x | <code>Number</code> |  | X坐标。 |
| y | <code>Number</code> |  | Y坐标 |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | 参考点。 |

**示例**  
```js
// ECMA 5.1 (浏览器 + 桌面)
var rho_phi = xy_to_polar(100, 100)
var rho = rho_phi[0]
var phi = rho_phi[1]
// ECMA 6 (仅浏览器)
let [rho, phi] = xy_to_polar(100, 100)
```
<a name="xy_distance"></a>

## xy\_distance(x1, y1, x2, y2) ⇒ <code>Number</code>
给出两个点之间的距离。

**返回**: <code>Number</code> - 两点之间的距离。  

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x1 | <code>Number</code> | 第一个点的x坐标。 |
| y1 | <code>Number</code> | 第一个点的y坐标。 |
| x2 | <code>Number</code> | 第二个点的x坐标。 |
| y2 | <code>Number</code> | 第二个点的y坐标。 |

<a name="xy_circle"></a>

## xy\_circle(n, rho, [phi0], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
生成一个点列表（x、y坐标）在一个圆中。这可用于以圆形排列绘制刺激。

**返回**：<code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - 一个由 [x,y] 坐标数组组成的数组。

| 参数 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | 要生成的 x,y 坐标的数量。 |
| rho | <code>Number</code> |  | 第一个坐标的径向坐标，也称为距离或偏心率。 |
| [phi0] | <code>Number</code> | <code>0</code> | 第一个坐标的角坐标。 顺时针旋转度数（即不是弧度）， 其中 0 是直接向右。 |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | 参考点。 |

**示例**  
```js
// 在一个中央注视点周围绘制 8 个矩形
// ECMA 5.1（浏览器 + 桌面）
var c = Canvas()
c.fixdot()
var points = xy_circle(8, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (仅限浏览器)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_circle(8, 100)) {
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
```

<a name="xy_grid"></a>

## xy\_grid(n, spacing, [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
生成一个网格中的点列表（x,y坐标）。这可用于
以网格排列绘制刺激。


**返回**：<code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - 一个由 [x,y] 坐标数组组成的数组。

| 参数 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| n | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | 表示列和行的数字，`n=2`表示 2x2 网格，或者一个 [n_col, n_row] 数组，如 `n=[2,3]`表示 2x3 网格。 |
| spacing | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | 表示单元格间距的数值，或者一个 [col_spacing, row_spacing] 数组。 |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | 参考点。 |

**示例**  
```js
// 绘制一个 4x4 网格的矩形
// ECMA 5 (桌面 + 浏览器)
var c = Canvas()
c.fixdot()
var points = xy_grid(4, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (仅限浏览器)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_grid(4, 100)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```

<a name="xy_random"></a>

## xy\_random(n, width, height, [min_dist], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
生成一个随机点（x,y坐标）列表，每对点之间最小间距
。当坐标列表无法生成时，此函数将抛出错误
通常是因为点太多、最小距离设置得太高或宽度或高度
设置太低。


**返回**：<code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - 由 [x,y] 坐标数组组成的数组。

| 参数 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | 要生成的坐标数量。 |
| width | <code>Number</code> |  | 随机点所在区域的宽度。 |
| height | <code>Number</code> |  | 随机点所在区域的高度。 |
| [min_dist] | <code>Number</code> | <code>0</code> | 每个点之间的最小距离。 |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | 参考点。 |

**示例**  
```js
// 在随机网格中绘制 50 个矩形
// ECMA 5 (桌面 + 浏览器)
var c = Canvas()
c.fixdot()
var points = xy_random(50, 500, 500, 40)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()   
// ECMA 6 (仅限浏览器)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_random(50, 500, 500, 40)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```