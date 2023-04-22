## reset\_feedback()
Réinitialise toutes les variables de feedback à leur état initial.

**Exemple**  
```js
reset_feedback()
```
<a name="set_subject_nr"></a>

## set\_subject\_nr(nr)
Définit le numéro du sujet et sa parité (pair/ impair). Cette fonction est appelée
automatiquement lorsqu'une expérience est lancée. Vous n'avez donc besoin de l'appeler
vous-même que si vous écrasez le numéro de sujet spécifié au lancement de l'expérience.

| Param | Type | Description |
| --- | --- | --- |
| nr | <code>Number</code> | Le numéro du sujet |

**Exemple**  
```js
set_subject_nr(1)
console.log('Numéro de sujet = ' + vars.subject_nr)
console.log('Parité du sujet = ' + vars.subject_parity)
```
<a name="sometimes"></a>

## sometimes([p])
Renvoie vrai avec une certaine probabilité. (Pour une randomisation plus avancée,
utilisez le package `random-ext`, disponible sous `random`.)

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| [p] | <code>Number</code> | <code>.5</code> | La probabilité de renvoyer vrai |

**Exemple**  
```js
if (sometimes()) {
  console.log('Parfois, vous gagnez')
} else {
  console.log('Parfois, vous perdez')
}
```
<a name="xy_from_polar"></a>

## xy\_from\_polar(rho, phi, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Convertit des coordonnées polaires (distance, angle) en coordonnées cartésiennes
(x, y).

**Retour**: <code>Array.&lt;Number&gt;</code> - Un tableau [x, y].  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| rho | <code>Number</code> |  | La coordonnée radiale, également distance ou excentricité. |
| phi | <code>Number</code> |  | La coordonnée angulaire. Cela reflète une rotation     horaire en degrés (c'est-à-dire pas en radians), où 0 est tout droit à droite. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Le point de référence. |

**Exemple**  
```js
// ECMA 5.1
var xy1 = xy_from_polar(100, 45)
var xy2 = xy_from_polar(100, -45)
var c = Canvas()
c.line({sx: xy1[0], sy: xy1[1], ex: -xy1[0], ey: -xy1[1]})
c.line({sx: xy2[0], sy: xy2[1], ex: -xy2[0], ey: -xy2[1]})
c.show()
// ECMA 6
let [x1, y1] = xy_from_polar(100, 45)
let [x2, y2] = xy_from_polar(100, -45)
let c = Canvas()
c.line({sx: x1, sy: y1, ex: -x1, ey: -y1})
c.line({sx: x2, sy: y2, ex: -x2, ey: -y2})
c.show()
```
<a name="xy_to_polar"></a>

## xy\_to\_polar(x, y, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Convertit des coordonnées cartésiennes (x, y) en coordonnées polaires (distance,
angle).

**Retour**: <code>Array.&lt;Number&gt;</code> - Un tableau [rho, phi]. Ici, `rho` est la coordonnée radiale,
    également distance ou excentricité. `phi` est la coordonnée
    angulaire en degrés (c'est-à-dire pas en radians) et reflète une
    rotation anti-horaire, où 0 est tout droit à droite.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| x | <code>Number</code> |  | La coordonnée X. |
| y | <code>Number</code> |  | La coordonnée Y |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Le point de référence. |

**Exemple**  
```js
// ECMA 5.1 (navigateur + bureau)
var rho_phi = xy_to_polar(100, 100)
var rho = rho_phi[0]
var phi = rho_phi[1]
// ECMA 6 (navigateur uniquement)
let [rho, phi] = xy_to_polar(100, 100)
```
<a name="xy_distance"></a>

## xy\_distance(x1, y1, x2, y2) ⇒ <code>Number</code>
Donne la distance entre deux points.

**Retour**: <code>Number</code> - La distance entre les deux points.  

| Param | Type | Description |
| --- | --- | --- |
| x1 | <code>Number</code> | La coordonnée x du premier point. |
| y1 | <code>Number</code> | La coordonnée y du premier point. |
| x2 | <code>Number</code> | La coordonnée x du deuxième point. |
| y2 | <code>Number</code> | La coordonnée y du deuxième point. |

<a name="xy_circle"></a>

## xy\_circle(n, rho, [phi0], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Génère une liste de points (coordonnées x,y) dans un cercle. Ceci peut être
utilisé pour dessiner des stimuli dans un arrangement circulaire.

**Renvoie**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Un tableau de tableaux de coordonnées [x,y].  

| Param | Type | Par défaut | Description |
| --- | --- | --- | --- |
| n | <code>Nombre</code> |  | Le nombre de coordonnées x,y à générer. |
| rho | <code>Nombre</code> |  | La coordonnée radiale, également distance ou excentricité,     du premier point. |
| [phi0] | <code>Nombre</code> | <code>0</code> | La coordonnée angulaire pour la première coordonnée.     Il s'agit d'une rotation antihoraire en degrés (c'est-à-dire pas en radians),     où 0 est tout droit à droite. |
| [pole] | <code>Array.&lt;Nombre&gt;</code> | <code>[0, 0]</code> | Le point de référence. |

**Exemple**  
```js
// Dessinez 8 rectangles autour d'un point de fixation central
// ECMA 5.1 (navigateur + bureau)
var c = Canvas()
c.fixdot()
var points = xy_circle(8, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (navigateur uniquement)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_circle(8, 100)) {
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
```
<a name="xy_grid"></a>

## xy\_grid(n, espacement, [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Génère une liste de points (coordonnées x,y) dans une grille. Ceci peut être utilisé
pour dessiner des stimuli dans un arrangement en grille.


**Renvoie**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Un tableau de tableaux de coordonnées [x,y].  

| Param | Type | Par défaut | Description |
| --- | --- | --- | --- |
| n | <code>Nombre</code> \| <code>Array.&lt;Number&gt;</code> |  | Un nombre qui indique le nombre de     colonnes et de rangées, de sorte que `n=2` indique une grille 2x2, ou un tableau [n_col,     n_row], de sorte que `n=[2,3]` indique une grille 2x3. |
| espacement | <code>Nombre</code> \| <code>Array.&lt;Number&gt;</code> |  | Une valeur numérique qui indique l'     espacement entre les cellules, ou un tableau [col_spacing, row_spacing]. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Le point de référence. |

**Exemple**  
```js
// Dessinez une grille 4x4 de rectangles
// ECMA 5 (bureau + navigateur)
var c = Canvas()
c.fixdot()
var points = xy_grid(4, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (navigateur uniquement)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_grid(4, 100)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```
<a name="xy_random"></a>

## xy\_random(n, largeur, hauteur, [min_dist], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Génère une liste de points aléatoires (coordonnées x,y) avec un minimum
espacement entre chaque paire de points. Cette fonction générera une erreur
lorsque la liste des coordonnées ne peut pas être générée, généralement parce qu'il y a
trop de points, le min_dist est trop élevé, ou la largeur ou la hauteur sont
trop bas.


**Renvoie**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Un tableau de tableaux de coordonnées [x,y].  

| Param | Type | Par défaut | Description |
| --- | --- | --- | --- |
| n | <code>Nombre</code> |  | Le nombre de points à générer. |
| largeur | <code>Nombre</code> |  | La largeur du champ avec des points aléatoires. |
| hauteur | <code>Nombre</code> |  | La hauteur du champ avec des points aléatoires. |
| [min_dist] | <code>Nombre</code> | <code>0</code> | La distance minimale entre chaque point. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Le point de référence. |

**Exemple**  
```js
// Dessinez 50 rectangles dans une grille aléatoire
// ECMA 5 (bureau + navigateur)
var c = Canvas()
c.fixdot()
var points = xy_random(50, 500, 500, 40)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()   
// ECMA 6 (navigateur uniquement)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_random(50, 500, 500, 40)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```