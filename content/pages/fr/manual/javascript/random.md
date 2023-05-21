title: fonctions aléatoires (random-ext)
hash: 2378ced3b07fc62eb554811208003828b6ca0c238abaf26bc4169762a25dbe64
locale: fr
language: French

La bibliothèque `random-ext` est disponible sous le nom `random`. Cette bibliothèque offre de nombreuses fonctions pratiques et de niveau supérieur pour la randomisation.

__Exemple :__

Tirez huit cercles avec une couleur aléatoire et une position tirée au hasard dans une grille de cinq par cinq :

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

Pour un aperçu, voir :

- <https://www.npmjs.com/package/random-ext>