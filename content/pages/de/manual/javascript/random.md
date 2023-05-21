title: Zufallsfunktionen (random-ext)
hash: 2378ced3b07fc62eb554811208003828b6ca0c238abaf26bc4169762a25dbe64
locale: de
language: German

Die `random-ext` Bibliothek ist als `random` verfügbar. Diese Bibliothek bietet viele praktische, höherstufige Funktionen für Zufallsverteilungen.

__Beispiel:__

Zeichnen Sie acht Kreise mit einer zufälligen Farbe und einer Position, die zufällig aus einem fünf mal fünf Raster ausgewählt wird:

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

Für einen Überblick, siehe:

- <https://www.npmjs.com/package/random-ext>
