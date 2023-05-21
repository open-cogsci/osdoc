title: Python-ähnliche Iteratoren (pythonisch)
hash: 9f318dbb1d6b665f7f44a463c1545a783b4706fc4de08f3b2e077d0f7147b21b
locale: de
language: German

Die `pythonic` Bibliothek bietet Python-ähnliche Funktionen zum Iterieren über Arrays. Verfügbar sind die Funktionen: `range()`, `enumerate()`, `items()`, `zip()` und `zipLongest()`.

__Beispiel:__

Zeichne ein fünf mal fünf Raster mit aufsteigenden Zahlen:

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

Für eine Übersicht siehe:

- <https://www.npmjs.com/package/pythonic>