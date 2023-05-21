title: funciones aleatorias (random-ext)
hash: 2378ced3b07fc62eb554811208003828b6ca0c238abaf26bc4169762a25dbe64
locale: es
language: Spanish

La biblioteca `random-ext` está disponible como `random`. Esta biblioteca proporciona muchas funciones convenientes y de nivel superior para la aleatorización.

__Ejemplo:__

Dibuja ocho círculos con un color aleatorio y una ubicación que se toma al azar de una cuadrícula de cinco por cinco:

```js
let posiciones = xy_grid(5, 50)
posiciones = random.subArray(posiciones, 8)
const cnv = Canvas()
cnv.fixdot()
for (const [x, y] of posiciones) {
    cnv.circle({x: x, y: y, r: 20, fill: true, color: random.color()})
}
cnv.show()
```

Para obtener una descripción general, consulte:

- <https://www.npmjs.com/package/random-ext>