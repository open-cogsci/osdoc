title: 随机功能 (random-ext)
hash: 2378ced3b07fc62eb554811208003828b6ca0c238abaf26bc4169762a25dbe64
locale: zh
language: Chinese

`random-ext`库以`random`的形式提供。此库为随机化提供了许多方便的高级功能。

__示例：__

从一个五乘五的网格中随机抽取一个位置，绘制八个随机颜色的圆形：

```js
let positions = xy_grid(5, 50)
positions = random.subArray(positions, 8)
const cnv = Canvas()
cnv.fixdot()
for (const [x, y] of positions) {
    cnv.circle({x: x, y: y, r: 20, fill: true, color: random.color()})
}
cnv.show()
```

有关概述，请参见：

- <https://www.npmjs.com/package/random-ext>