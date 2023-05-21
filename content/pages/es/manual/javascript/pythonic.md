title: Iteradores estilo Python (pythonic)
hash: 9f318dbb1d6b665f7f44a463c1545a783b4706fc4de08f3b2e077d0f7147b21b
locale: es
language: Spanish

La biblioteca `pythonic` proporciona funciones similares a Python para iterar sobre matrices. Las funciones disponibles son: `range()`, `enumerate()`, `items()`, `zip()`, y `zipLongest()`.

__Ejemplo:__

Dibuja una cuadrícula de cinco por cinco de números incrementales:

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

Para obtener una descripción general, consulta:

- <https://www.npmjs.com/package/pythonic>