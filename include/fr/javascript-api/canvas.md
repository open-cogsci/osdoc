La classe `Canvas` est utilisée pour présenter des stimuli visuels. Vous créez généralement un objet `Canvas` avec la fonction de fabrique `Canvas()`. Comme `Canvas()` est une fonction, vous n'avez *pas* besoin d'utiliser `new` lors de son appel.
La classe JavaScript `Canvas` imite la classe Python `Canvas` correspondante.

__Les mots-clés de style__ peuvent être passés à toutes les fonctions qui acceptent `styleArgs`.
Les mots-clés de style peuvent également être définis comme propriétés de l'objet `Canvas`. Pour un
aperçu des mots-clés de style, voir la [documentation Python `Canvas`](%url:manual/python/canvas/).

__Important :__ JavaScript ne prend pas en charge les paramètres nommés (ou : les mots-clés).
Par conséquent, les paramètres sont passés via un `Object` avec des propriétés nommées et
des valeurs par défaut. Comme ceci :

```js
var myCanvas = Canvas()
// (correct) passez des paramètres comme un Object ...
myCanvas.fixdot({color: 'red'})
// (incorrect) ... et *non* comme des paramètres nommés
// myCanvas.fixdot(color='red')
myCanvas.show()
```

[TOC]

<a name="Canvas.arrow"></a>

### Canvas.arrow(obj)
Dessine une flèche. Une flèche est un polygone composé de 7 sommets, avec une
pointe de flèche pointant vers (ex, ey).



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.sx | <code>Number</code> | <code>0</code> | 
| obj.sy | <code>Number</code> | <code>0</code> | 
| obj.ex | <code>Number</code> | <code>50</code> | 
| obj.ey | <code>Number</code> | <code>0</code> | 
| obj.body_length | <code>Number</code> | <code>0.8</code> | 
| obj.body_width | <code>Number</code> | <code>0.5</code> | 
| obj.head_width | <code>Number</code> | <code>30</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
var w = vars.width / 2
var h = vars.height / 2
// Important : les paramètres sont passés comme un Object
myCanvas.arrow({sx: 0, sy: 0, w: w, h: h, head_width:100, body_length:0.5})
```
<a name="Canvas.clear"></a>

### Canvas.clear([styleArgs])
Efface le canevas avec la couleur d'arrière-plan actuelle. Notez qu'il est
	 généralement plus rapide d'utiliser un canevas différent pour chaque affichage expérimental
	 plutôt que d'utiliser un seul canevas et de le effacer et le redessiner
	 à plusieurs reprises.



| Param | Type | Default |
| --- | --- | --- |
| [styleArgs] | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.fixdot({color: 'green'})
myCanvas.show()
// faire quelque chose
myCanvas.clear()
myCanvas.fixdot({color: 'red'})
myCanvas.show()
```
<a name="Canvas.circle"></a>

### Canvas.circle(obj)
Dessine un cercle.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.r | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.circle({x: 100, y: 100, r: 50, fill: true, color:'red'})
```
<a name="Canvas.ellipse"></a>

### Canvas.ellipse(obj)
Dessine une ellipse.



| Param | Type | Default |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.ellipse({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.fixdot"></a>

### Canvas.fixdot(obj)
Dessine un point de fixation. Le style par défaut est moyen-ouvert.

- 'large-filled' est un cercle rempli avec un rayon de 16px.
- 'medium-filled' est un cercle rempli avec un rayon de 8px.
- 'small-filled' est un cercle rempli avec un rayon de 4px.
- 'large-open' est un cercle rempli avec un rayon de 16px et un trou de 2px.
- 'medium-open' est un cercle rempli avec un rayon de 8px et un trou de 2px.
- 'small-open' est un cercle rempli avec un rayon de 4px et un trou de 2px.
- 'large-cross' est une croix de 16px.
- 'medium-cross' est une croix de 8px.
- 'small-cross' est une croix de 4px.



| Param | Type | Par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.style | <code>String</code> | <code>&#x27;default&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.fixdot()
```
<a name="Canvas.gabor"></a>

### Canvas.gabor(obj)
Dessine un patch Gabor.



| Param | Type | Par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.orient | <code>Number</code> | <code>0</code> | 
| obj.freq | <code>Number</code> | <code>.1</code> | 
| obj.env | <code>String</code> | <code>&#x27;gaussian&#x27;</code> | 
| obj.size | <code>Number</code> | <code>96</code> | 
| obj.stdev | <code>Number</code> | <code>12</code> | 
| obj.phase | <code>Number</code> | <code>0</code> | 
| obj.col1 | <code>String</code> | <code>&#x27;white&#x27;</code> | 
| obj.col2 | <code>String</code> | <code>&#x27;black&#x27;</code> | 
| obj.bgmode | <code>String</code> | <code>&#x27;avg&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.gabor({x: 100, y: 100, orient: 45, freq: .05})
```
<a name="Canvas.image"></a>

### Canvas.image(obj)
Dessine une image à partir d'un fichier dans le pool de fichiers.



| Param | Type | Par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.fname | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.scale | <code>Number</code> | <code>1</code> | 
| obj.rotation | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.image({fname: 'image_in_pool.png'})
```
<a name="Canvas.line"></a>

### Canvas.line(obj)
Dessine une ligne.



| Param | Type | Par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.sx | <code>Number</code> | <code>0</code> | 
| obj.sy | <code>Number</code> | <code>0</code> | 
| obj.ex | <code>Number</code> | <code>50</code> | 
| obj.ey | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
var ex = vars.width / 2
var ey = vars.height / 2
myCanvas.line({sx: 0, sy: 0, ex: ex, ey: ey})
```
<a name="Canvas.noise_patch"></a>

### Canvas.noise\_patch(obj)
Dessine un patch de bruit, avec une enveloppe.



| Param | Type | Par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| obj.env | <code>String</code> | <code>&#x27;gaussian&#x27;</code> | 
| obj.size | <code>Number</code> | <code>96</code> | 
| obj.stdev | <code>Number</code> | <code>12</code> | 
| obj.col1 | <code>String</code> | <code>&#x27;white&#x27;</code> | 
| obj.col2 | <code>String</code> | <code>&#x27;black&#x27;</code> | 
| obj.bgmode | <code>String</code> | <code>&#x27;avg&#x27;</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.noise_patch({x: 100, y: 100, env: 'circular'})
```
<a name="Canvas.polygon"></a>

### Canvas.polygon(obj)
Dessine un polygone défini par une liste de sommets. C'est-à-dire une forme
de points reliés par des lignes.

| Param | Type | Valeur par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.vertices | <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> |  | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
var n1 = [0,0]
var n2 = [100, 100]
var n3 = [0, 100]
myCanvas.polygon({vertices: [n1, n2, n3]})
```
<a name="Canvas.rect"></a>

### Canvas.rect(obj)
Dessine un rectangle.

| Param | Type | Valeur par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.x | <code>Number</code> | <code>-50</code> | 
| obj.y | <code>Number</code> | <code>-25</code> | 
| obj.w | <code>Number</code> | <code>100</code> | 
| obj.h | <code>Number</code> | <code>50</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.rect({x: -10, y: -10, w: 20, h: 20, fill:true})
```
<a name="Canvas.show"></a>

### Canvas.show() ⇒ <code>Number</code>
Affiche, ou 'retourne', le canevas à l'écran.

**Renvoie**: <code>Number</code> - Un horodatage du moment où le canevas est apparu sur
    l'écran.
<a name="Canvas.text"></a>

### Canvas.text(obj)
Dessine du texte.

| Param | Type | Valeur par défaut |
| --- | --- | --- |
| obj | <code>Object</code> |  | 
| obj.text | <code>String</code> |  | 
| obj.center | <code>Boolean</code> | <code>true</code> | 
| obj.x | <code>Number</code> | <code>0</code> | 
| obj.y | <code>Number</code> | <code>0</code> | 
| ..obj.styleArgs | <code>Object</code> | <code>{}</code> | 

**Exemple**  
```js
var myCanvas = Canvas()
myCanvas.text({text: 'Du texte'})
```