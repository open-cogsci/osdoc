title: Python-like iterators (pythonic)

The `pythonic` library provides Python-like functions for iterating over arrays. Available functions are: `range()`, `enumerate()`, `items()`, `zip()`, and `zipLongest()`.

__Example:__

Draw a five by five grid of incrementing numbers:

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

For an overview, see:

- <https://www.npmjs.com/package/pythonic>
