<div class="ClassDoc YAMLDoc" markdown="1">

# classe __Canvas__

{% set arg_max_width = "La largeur maximale du texte en pixels, " +
"avant de passer à une nouvelle ligne, ou `None` pour ajuster à la bordure de l'écran." %}

{% set arg_bgmode = "Spécifie si l'arrière-plan est la moyenne de " +
"col1 et col2 ('avg', correspondant à un patch de Gabor typique), ou " + 
"égal à col2 ('col2'), utile pour se fondre dans l'arrière-plan. Remarque: " +
"ce paramètre est ignoré par le backend psycho, qui utilise une augmentation " + 
"de la transparence pour l'arrière-plan." %}

{% set arg_style = "Mots-clés de [style optionnels](#style-keywords) qui " + 
"spécifient le style de l'opération de dessin en cours. Cela n'affecte pas " + 
"les opérations de dessin ultérieures." %}

{% set arg_center = "Un booléen indiquant si les coordonnées reflètent " + 
"le centre (`True`) ou haut-gauche (`False`) du texte." %}

La classe `Canvas` est utilisée pour présenter des stimuli visuels. Vous créez généralement un
objet `Canvas` avec la fonction de fabrique `Canvas()`, comme décrit dans la section
[Création d'un Canvas](#creating-a-canvas).

__Exemple__ :

~~~ .python
# Créer et afficher un canvas avec un point de fixation central
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

__Exemple__ :

Vous pouvez également ajouter des éléments `Canvas` en tant qu'objets. Voir aussi la section sur [Nommer,
accéder et modifier les éléments](#naming-accessing-and-modifying-elements).

~~~ .python
# Créer un canvas avec un point de fixation et un rectangle
my_canvas = Canvas()
my_canvas['my_fixdot'] = FixDot()
my_canvas.show()
~~~

[TOC]

## Choses à savoir

### Création d'un Canvas

Vous créez généralement un `Canvas` avec la fonction de fabrique `Canvas()` :

~~~ .python
my_canvas = Canvas()
~~~

Facultativement, vous pouvez passer des [mots-clés de style](#style-keywords) à `Canvas()` pour définir
le style par défaut :

~~~ .python
my_canvas = Canvas(color='green')
my_canvas.fixdot() # Sera vert
~~~

### Mots-clés de style

Toutes les fonctions qui acceptent `**style_args` prennent les arguments de mot-clé suivants:

- `color` spécifie la couleur de l'avant-plan. Pour les spécifications de couleur valides, voir
  [couleurs](#colors).
- `background_color` spécifie la couleur de l'arrière-plan. Pour les spécifications de couleur valides, voir [couleurs](#colors).
- `fill` indique si les rectangles, cercles, polygones et ellipses sont
  remplis (`True`) ou dessinés sous forme de contour (`False`).
- `penwidth` indique une largeur de crayon en pixels et doit être `int` ou `float`.
- `html` indique si les balises HTML sont interprétées et doit être `True` ou
  `False`.
- `font_family` est le nom d'une famille de polices, tel que 'sans'.
- `font_size` est une taille de police en pixels.
- `font_italic` indique si le texte doit être en italique et doit être `True` ou
  `False`.
- `font_bold` indique si le texte doit être en gras et doit être `True` ou
  `False`.
- `font_underline` indique si le texte doit être souligné et doit être
  `True` ou `False`.

~~~ .python
# Dessiner un point de fixation vert
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
~~~

Les mots-clés de style n'affectent que l'opération de dessin en cours (sauf lorsqu'ils sont passés à
`Canvas()` lors de la création du `Canvas`). Pour changer le style pour toutes les opérations de dessin ultérieures, définissez directement les propriétés de style, telles que `canvas.color` :

~~~ .python
# Dessiner une croix rouge avec une largeur de crayon de 2px
my_canvas = Canvas()
my_canvas.color = 'red'
my_canvas.penwidth = 2
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

Ou passez les propriétés de style à `Canvas()` :

~~~ .python
# Dessiner une croix rouge avec une largeur de crayon de 2px
my_canvas = Canvas(color='red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

### Couleurs

Vous pouvez spécifier des couleurs de différentes manières. Cela inclut les spécifications de couleur de type CSS3, mais prend également en charge des spécifications supplémentaires, telles que l'espace colorimétrique CIE l* a* b*.

__Note de version :__ Les espaces de couleur `hsv`, `hsl` et `lab` sont nouveaux dans la version 3.3.0.

- __Noms de couleurs :__ 'red', 'black', etc. Une liste complète des noms de couleurs valides peut être
  trouvée [ici](http://www.w3.org/TR/SVG11/types.html#ColorKeywords).
- __Chaines hexadécimales de sept caractères :__ `#FF0000`, `#000000`, etc. Ici,
  les valeurs vont de `00` à `FF`, de sorte que `#FF0000` est rouge vif.
- __Chaines hexadécimales de quatre caractères :__ `#F00`, `#000`, etc. Ici, les valeurs
  vont de '0' à 'F' de sorte que `#F00` est rouge vif.
- __Chaînes RGB :__ `rgb(255,0,0)`, `rgb(0,0,0)`, etc. Ici, les valeurs vont de
  0 à 255 pour que `rgb(255,0,0)` soit rouge vif.
- __Chaînes en pourcentage RGB :__ `rgb(100%,0%,0%)`, `rgb(0%,0%,0%)`, etc. Ici,
  les valeurs vont de 0% à 100% de sorte que `rgb(100%,0%,0%)` soit rouge vif.
- __Tuples RGB :__ `(255, 0, 0)`, `(0, 0 ,0)`, etc. Ici, les valeurs vont de `0`
  à `255` pour que `(255,0,0)` soit rouge vif.
- __Chaînes HSV :__ `hsv(120, 100%, 100%)`. Dans l'espace couleur [HSV](https://en.wikipedia.org/
  wiki/HSL_and_HSV), le paramètre de teinte est un angle de 0 à 359,
  et les paramètres de saturation et de valeur sont des pourcentages de 0% à 100%.
- __Chaînes HSL :__ `hsl(120, 100%, 50%)`. Dans l'espace couleur [HSL](https://en.wikipedia.org/
  wiki/HSL_and_HSV), le paramètre de teinte est un angle de 0 à 359,
  et les paramètres de saturation et de luminosité sont des pourcentages de 0% à 100%.
- __Chaînes LAB :__ `lab(53, -20, 0)`. Dans l'espace couleur [CIELAB](https://en.wikipedia.org/
  wiki/CIELAB_color_space), les paramètres reflètent la luminosité (`l*`),
  l'axe vert-rouge (`a*`, négatif est vert) et l'axe bleu-jaune (`b*`, négatif
  est bleu). Ceci utilise le point blanc D65 et la fonction de transfert sRGB, comme
  mis en œuvre [ici](https://www.psychopy.org/_modules/psychopy/tools/
  colorspacetools.html).
- __Valeurs de luminance :__  `255`, `0`, etc. Ici, les valeurs vont de `0` à `255`
  pour que `255` soit blanc.

~~~ .python
# Différentes façons de spécifier le vert
my_canvas.fixdot(color='green')  # Vert foncé
my_canvas.fixdot(color='#00ff00')
my_canvas.fixdot(color='#0f0')
my_canvas.fixdot(color='rgb(0, 255, 0)')
my_canvas.fixdot(color='rgb(0%, 100%, 0%)')
my_canvas.fixdot(color='hsl(100, 100%, 50%)')
my_canvas.fixdot(color='hsv(0, 100%, 100%)')
my_canvas.fixdot(color='lab(53, -20, 0)')  # Vert foncé
my_canvas.fixdot(color=(0, 255, 0))  # Spécifier une valeur de luminance (blanc)
~~~

### Nommer, accéder et modifier les éléments

À partir d'OpenSesame 3.2, le `Canvas` prend en charge une interface orientée objet qui permet
de nommer les éléments, et d'accéder et de modifier les éléments individuellement, sans
avoir à redessiner l'ensemble du `Canvas`.

Par exemple, la suite ajoutera d'abord un élément `Line` rouge à un `Canvas`
et l'affichera, puis changera la couleur de la ligne en vert et l'affichera à nouveau,
et enfin supprimera la ligne et montrera à nouveau le canevas (qui est maintenant vide).
Le nom de l'élément (`my_line`) est utilisé pour se référer à l'élément pour toutes les
opérations.

~~~ .python
my_canvas = Canvas()
my_canvas['my_line'] = Line(-100, -100, 100, 100, color='red')
my_canvas.show()
clock.sleep(1000)
my_canvas['my_line'].color = 'green'
my_canvas.show()
clock.sleep(1000)
del my_canvas['my_line']
my_canvas.show()
~~~

Vous pouvez également ajouter un élément sans fournir explicitement de nom pour celui-ci. Dans ce
cas, un nom est généré automatiquement (par exemple `stim0`).

~~~ .python
my_canvas = Canvas()
my_canvas += FixDot()
my_canvas.show()
~~~

Si vous ajoutez une liste d'éléments, ils seront automatiquement regroupés ensemble, et
vous pouvez vous référer au groupe entier par son nom.

~~~ .python
my_canvas = Canvas()
my_canvas['my_cross'] = [    Line(-100, 0, 100, 0),    Line(0, -100, 0, 100)]
my_canvas.show()
~~~

Pour vérifier si une coordonnée `x,y` particulière se trouve dans le rectangle englobant
d'un élément, vous pouvez utiliser `in`:

~~~ .python
my_mouse = Mouse(visible=True)
my_canvas = Canvas()
my_canvas['rect'] = Rect(-100, -100, 200, 200)
my_canvas.show()
button, (x, y), time = my_mouse.get_click()
if (x, y) in my_canvas['rect']:
    print('Clicked in rectangle')
else:
    print('Clicked outside of rectangle')
~~~

Vous pouvez également obtenir une liste des noms de tous les éléments qui contiennent une coordonnée `x, y`
en utilisant la fonction `Canvas.elements_at()`, documentée ci-dessous.

## arrow(sx, sy, ex, ey, body_length=0.8, body_width=0.5, head_width=30, \*\*style_args)

Dessine une flèche. Une flèche est un polygone composé de 7 sommets,
avec une pointe de flèche pointant vers (ex, ey).

__Paramètres__

- **sx**: La coordonnée X de la base de la flèche.
- **sy**: La coordonnée Y de la base de la flèche.
- **ex**: La coordonnée X de la pointe de la flèche.
- **ey**: La coordonnée Y de la pointe de la flèche.
- **body_length**: Longueur proportionnelle du corps de la flèche par rapport à la flèche entière
[0-1].
- **body_width**: Largeur (épaisseur) proportionnelle du corps de la flèche par rapport à la
flèche entière [0-1].
- **head_width**: Largeur (épaisseur) de la tête de la flèche en pixels.


## circle(x, y, r, \*\*style_args)

Dessine un cercle.

__Paramètres__

- **x**: La coordonnée X du centre du cercle.
- **y**: La coordonnée Y du centre du cercle.
- **r**: Le rayon du cercle.
- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface de fonction
my_canvas.circle(100, 100, 50, fill=True, color='red')
# Interface d'élément
my_canvas['my_circle'] = Circle(100, 100, 50, fill=True, color='red')
~~~



## clear(\*arglist, \*\*kwdict)

Efface le canevas avec la couleur d'arrière-plan actuelle. Notez que cela
est généralement plus rapide d'utiliser un canevas différent pour chaque affichage expérimental que d'utiliser un seul canevas et de le vider et le redessiner à plusieurs reprises.

__Paramètres__

- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
clock.sleep(1000)
my_canvas.clear()
my_canvas.fixdot(color='red')
my_canvas.show()
~~~



## copy(canvas)

Transforme le `Canvas` actuel en une copie du `Canvas` passé.

__Avertissement :__

Copier des objets `Canvas` peut entraîner un comportement imprévisible. Dans de nombreux
cas, une meilleure solution consiste à recréer plusieurs objets `Canvas` à partir de
zéro, et / ou à utiliser l'interface d'élément pour mettre à jour les éléments `Canvas`
individuellement.

__Paramètres__

- **canvas**: Le `Canvas` à copier.

__Exemple__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(x=100, color='green')
my_copied_canvas = Canvas()
my_copied_canvas.copy(my_canvas)
my_copied_canvas.fixdot(x=200, color="blue")
my_copied_canvas.show()
~~~





## elements_at(x, y)

* Nouveau dans v3.2.0 *

Obtient les noms des éléments qui contiennent une
coordonnée `x, y` particulière.

__Paramètres__

- **x**: Une coordonnée X.
- **y**: Une coordonnée Y.

__Renvoie__

- Une `list` de noms d'éléments qui contiennent la coordonnée `x, y`.

__Exemple__

~~~ .python
# Créez et affichez un canevas avec deux rectangles partiellement superposés
my_canvas = Canvas()
my_canvas['right_rect'] = Rect(x=-200, y=-100, w=200, h=200, color='red')
my_canvas['left_rect'] = Rect(x=-100, y=-100, w=200, h=200, color='green')
my_canvas.show()
# Collectez un clic de souris et imprimez les noms des éléments qui
# contiennent le point cliqué
my_mouse = Mouse(visible=True)
button, pos, time = my_mouse.get_click()
if pos is not None:
    x, y = pos
    print('Cliqué sur les éléments: %s' % my_canvas.elements_at(x, y))
~~~



## ellipse(x, y, w, h, \*\*style_args)

Dessine une ellipse.

__Paramètres__

- **x**: La coordonnée X gauche.
- **y**: La coordonnée Y supérieure.
- **w**: La largeur.
- **h**: La hauteur.
- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface de fonction
my_canvas.ellipse(-10, -10, 20, 20, fill=True)
# Interface d'élément
my_canvas['my_ellipse'] = Ellipse(-10, -10, 20, 20, fill=True)
~~~



## fixdot(x=None, y=None, style='default', \*\*style_args)

Dessine un point de fixation. Le style par défaut est medium-open.

- 'large-filled' est un cercle rempli avec un rayon de 16px.
- 'medium-filled' est un
cercle rempli avec un rayon de 8px.
- 'small-filled' est un cercle rempli
avec un rayon de 4px.
- 'large-open' est un cercle rempli avec un rayon de 16px
et un trou de 2px.
- 'medium-open' est un cercle rempli avec un rayon de 8px
et un trou de 2px.
- 'small-open' est un cercle rempli avec un rayon de 4px et
un trou de 2px.
- 'large-cross' est une croix de 16px.
- 'medium-cross' est une croix de 8px
- 'small-cross' est une croix de 4px.

__Paramètres__

- **x**: La coordonnée X du centre du point, ou None pour dessiner un point horizontalement
centré.
- **y**: La coordonnée Y du centre du point, ou None pour dessiner un point verticalement
centré.
- **style**: Le style du point de fixation. L'un des éléments suivants: default, large-filled,
medium-
filled, small-filled, large-open, medium-open,
small-open, large-
cross, medium-cross, ou small-cross.
default égale medium-open.
- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface de fonction
my_canvas.fixdot()
# Interface d'élément
my_canvas['my_fixdot'] = FixDot()
~~~



## gabor(x, y, orient, freq, env='gaussian', size=96, stdev=12, phase=0, col1='white', col2='black', bgmode='avg')

Dessine un patch Gabor. Note: Le rendu exact du patch Gabor
dépend du back-end.


__Paramètres__

- **x**: La coordonnée X du centre.
- **y**: La coordonnée Y du centre.
- **orient**: Orientation en degrés [0 .. 360]. Cela fait référence à une
rotation horaire à partir d'une verticale.
- **freq**: Fréquence en cycles/px du sinus.
- **env**: L'enveloppe qui détermine la forme du patch. Peut être
"gaussian", "linear", "circular" ou "rectangular".
- **size**: Une taille en pixels.
- **stdev**: Écart type en pixels du gaussien. Applicable uniquement aux
enveloppes gaussiennes.
- **phase**: Phase du sinus [0.0 .. 1.0].
- **col1**: Une couleur pour les pics.
- **col2**: Une couleur pour les creux. Note : Le back-end psycho
ignore cette
paramètre et utilise toujours l'inverse de
`col1` pour les creux.
- **bgmode**: {{arg_bgmode}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface de fonction
my_canvas.gabor(100, 100, 45, .05)
# Interface d'élément
my_canvas['my_gabor'] = Gabor(100, 100, 45, .05)
~~~



## image(fname, center=True, x=None, y=None, scale=None, rotation=None)

Dessine une image à partir d'un fichier. Cette fonction ne cherche pas dans le fichier
pool, mais prend un chemin absolu.


__Paramètres__

- **fname**: Le nom de fichier de l'image. Lors de l'utilisation de Python 2, cela doit être
soit `unicode` soit un `str` encodé en utf-8. Lors de l'utilisation de Python 3,
cela doit être soit `str` soit un `bytes` encodé en utf-8.
- **center**: Un booléen indiquant si les coordonnées indiquent le centre (True) ou
haut-gauche (False).
- **x**: La coordonnée X ou `None` pour dessiner une image horizontalement centrée.
- **y**: La coordonnée Y ou `None` pour dessiner une image verticalement centrée.
- **scale**: Le facteur d'échelle de l'image. `None` ou 1 indiquent la taille originale.
2.0 indique un zoom de 200%, etc.
- **rotation**: La rotation de l'image. `None` ou 0 indiquent la rotation originale.
Les valeurs positives indiquent une rotation horaire en degrés.

__Exemple__

~~~ .python
my_canvas = Canvas()
# Déterminer le chemin absolu :
path = exp.pool['image_in_pool.png']
# Interface de fonction
my_canvas.image(path)
# Interface d'élément
my_canvas['my_image'] = Image(path)
~~~



## line(sx, sy, ex, ey, \*\*style_args)

Dessine une ligne.


__Paramètres__

- **sx**: La coordonnée X gauche.
- **sy**: La coordonnée Y supérieure.
- **ex**: La coordonnée X droite.
- **ey**: La coordonnée Y inférieure.
- **\*\*style_args**: {{arg_style}}


## lower_to_bottom(element)

Abaisse un élément vers le bas, de sorte qu'il soit dessiné en premier; c'est
à dire qu'il devient l'arrière-plan.


__Paramètres__

- **element**: Un élément SKETCHPAD, ou son nom.


## noise_patch(x, y, env='gaussian', size=96, stdev=12, col1='white', col2='black', bgmode='avg')

Dessine un patch de bruit, avec une enveloppe. Le rendu exact du
patch de bruit dépend du back-end.


__Paramètres__

- **x**: Coordonnée X centrale.
- **y**: Coordonnée Y centrale.
- **env**: L'enveloppe qui détermine la forme du patch. Peut être
"gaussian", "linéaire", "circulaire" ou "rectangulaire".
- **size**: Une taille en pixels.
- **stdev**: Écart type en pixels du gaussien. Applicable uniquement aux
enveloppes gaussiennes.
- **col1**: La première couleur.
- **col2**: La deuxième couleur. Remarque: Le back-end psycho ignore ce
paramètre
et utilise toujours l'inverse de `col1`.
- **bgmode**: {{arg_bgmode}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface fonction
my_canvas.noise_patch(100, 100, env='circulaire')
# Interface élément
my_canvas['my_noise_patch'] = NoisePatch(100, 100, env='circulaire')
~~~



## polygon(sommets, \*\*style_args)

Dessine un polygone défini par une liste de sommets. C'est-à-dire une forme de
points reliés par des lignes.


__Paramètres__

- **sommets**: Une liste de tuples, où chaque tuple correspond à un sommet. Par
exemple, [(100,100), (200,100), (100,200)] dessinera un triangle.
- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
n1 = 0,0
n2 = 100, 100
n3 = 0, 100
# Interface fonction
my_canvas.polygon([n1, n2, n3])
# Interface élément
my_canvas['my_polygon'] = Polygon([n1, n2, n3])
~~~



## prepare(self)

Termine les opérations de canevas en attente (le cas échéant), de sorte qu'un
appel ultérieur à [canvas.show] soit extrêmement rapide. Il est seulement nécessaire d'appeler cette
fonction si vous avez désactivé `auto_prepare` lors de l'initialisation du
`Canvas`.




## raise_to_top(element)

Place un élément au premier plan, de sorte qu'il soit dessiné en dernier ; c'est-à-dire, il
devient le premier plan.


__Paramètres__

- **element**: Un élément SKETCHPAD ou son nom.


## rect(x, y, w, h, \*\*style_args)

Dessine un rectangle.


__Paramètres__

- **x**: Coordonnée X gauche.
- **y**: Coordonnée Y supérieure.
- **w**: La largeur.
- **h**: La hauteur.
- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface fonction
my_canvas.rect(-10, -10, 20, 20, fill=True)
# Interface élément
my_canvas['my_rect'] = Rect(-10, -10, 20, 20, fill=True)
~~~



## rename_element(old_name, new_name)

Renomme un élément.




## show(self)

Affiche ou 'bascule' le canvas à l'écran.



__Retour__

- Un horodatage du moment où le canevas est réellement apparu sur
l'écran, ou une meilleure estimation si des informations temporelles précises ne sont pas
disponibles. Pour plus d'informations sur le timing, voir </misc/timing>.
En fonction du back-end, l'horodatage est un `int` ou un `float`.

__Exemple__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
t = my_canvas.show()
exp.set('time_fixdot', t)
~~~



## text(texte, center=True, x=None, y=None, max_width=None, \*\*style_args)

Dessine du texte.


__Paramètres__

- **texte**: Une chaîne de texte. Lors de l'utilisation de Python 2, cela devrait être soit
`unicode` ou une chaîne `str` encodée en utf-8. Lors de l'utilisation de Python 3, cela
devrait être soit `str` ou des `bytes` encodées en utf-8.
- **center**: {{arg_center}}
- **x**: La coordonnée X, ou None pour dessiner le texte centré horizontalement.
- **y**: La coordonnée Y, ou None pour dessiner le texte centré verticalement.
- **max_width**: {{arg_max_width}}
- **\*\*style_args**: {{arg_style}}

__Exemple__

~~~ .python
my_canvas = Canvas()
# Interface fonction
my_canvas.text('Du texte en <b>gras</b> et en <i>italique</i>')
# Interface élément
my_canvas['my_text'] = Text('Du texte en <b>gras</b> et en <i>italique</i>')
~~~



## text_size(texte, center=True, max_width=None, \*\*style_args)

Détermine la taille d'une chaîne de texte en pixels.


__Paramètres__

- **texte**: Une chaîne de texte.
- **center**: {{arg_center}}
- **max_width**: {{arg_max_width}}
- **\*\*style_args**: {{arg_style}}

__Retour__

- Un tuple (largeur, hauteur) contenant les dimensions de la chaîne de texte
.

__Exemple__

~~~ .python
my_canvas = Canvas()
w, h = my_canvas.text_size('Du texte')
~~~



</div>