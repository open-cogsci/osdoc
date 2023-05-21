title: 类似 Python 的迭代器 (Pythonic)
hash: 9f318dbb1d6b665f7f44a463c1545a783b4706fc4de08f3b2e077d0f7147b21b
locale: zh
language: Chinese

`pythonic`库提供了类似Python的函数，用于遍历数组。可用的函数有：`range()`、`enumerate()`、`items()`、`zip()` 和 `zipLongest()`。

__示例：__

绘制一个五行五列的递增数字网格：

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

概述请参见：

- <https://www.npmjs.com/package/pythonic>