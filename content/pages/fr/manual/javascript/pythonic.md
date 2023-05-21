title: Itérators de type Python (pythonic)
hash: 9f318dbb1d6b665f7f44a463c1545a783b4706fc4de08f3b2e077d0f7147b21b
locale: fr
language: French

La bibliothèque `pythonic` fournit des fonctions similaires à Python pour itérer sur des tableaux. Les fonctions disponibles sont : `range()`, `enumerate()`, `items()`, `zip()`, et `zipLongest()`.

__Exemple :__

Dessinez une grille de cinq par cinq avec des nombres incrémentés :

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

Pour un aperçu, consultez :

- <https://www.npmjs.com/package/pythonic>