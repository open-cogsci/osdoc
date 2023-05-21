title: random functions (random-ext)


The `random-ext` library is available as `random`. This library provides many convenient, higher-level functions for randomization.

__Example:__

Draw eight circle with a random color and a location that is randomly sampled from a five by five grid:

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

For an overview, see:

- <https://www.npmjs.com/package/random-ext>
