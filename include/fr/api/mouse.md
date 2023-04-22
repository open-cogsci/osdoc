<div class="ClassDoc YAMLDoc" markdown="1">

# classe __Mouse__

La classe `Mouse` est utilisée pour collecter les entrées de la souris. Vous créez généralement un
objet `Mouse` avec la fonction usine `Mouse()`, comme décrit dans la section [Créer une souris](#creer-une-souris).

__Exemple__

~~~ .python
# Dessinez un 'curseur mouse fixation-dot' jusqu'à ce qu'un bouton soit cliqué
ma_souris = Mouse()
mon_canvas = Canvas()
while True:
    bouton, position, horodatage = ma_souris.get_click(timeout=20)
    if bouton is not None:
        break
    (x,y), temps = ma_souris.get_pos()
    mon_canvas.clear()
    mon_canvas.fixdot(x, y)
    mon_canvas.show()
~~~

[TOC]

## Choses à savoir

### Créer une souris

Vous créez généralement une `Mouse` avec la fonction usine `Mouse()`:

~~~ .python
ma_souris = Mouse()
~~~

Facultativement, vous pouvez passer les mots-clés [Response](#response-keywords) à `Mouse()`
pour définir le comportement par défaut:

~~~ .python
ma_souris = Mouse(timeout=2000)
~~~

### Coordonnées

- Lorsque *Coordonnées uniformes* est réglé sur 'oui', les coordonnées sont relatives au
  centre de l'affichage. C'est-à-dire, (0,0) est le centre. Ceci est la valeur par défaut à partir d'OpenSesame 3.0.0.
- Lorsque *Coordonnées uniformes* est réglé sur 'non', les coordonnées sont relatives à
  haut-gauche de l'affichage. C'est-à-dire, (0,0) est en haut à gauche. C'était la valeur par défaut dans OpenSesame 2.9.X et versions antérieures.

### Numéros de boutons

Les boutons de la souris sont numérotés comme suit:

1. Bouton gauche
2. Bouton du milieu
3. Bouton droit
4. Défilement vers le haut
5. Défilement vers le bas

### Écrans tactiles

Lors de l'utilisation d'un écran tactile, un toucher est enregistré en tant que bouton 1
(bouton gauche).

### Mots-clés de réponse

Les fonctions qui acceptent `**resp_args` prennent les arguments de mots-clés suivants :

- `timeout` spécifie une valeur de délai en millisecondes ou est défini sur `None` pour
  désactiver le délai.
- `buttonlist` spécifie une liste de boutons qui sont acceptés ou est défini sur
  `None` accepter tous les boutons.
- `visible` indique si le curseur de la souris devient visible lorsqu'un clic est
  collecté (`True` ou `False`). Pour modifier immédiatement la visibilité du curseur, utilisez
  `Mouse.show_cursor()`.

~~~ .python
# Obtenir un appui sur le bouton gauche ou droit avec un délai de 3000 ms
ma_souris = Mouse()
bouton, heure = ma_souris.get_click(buttonlist=[1,3], timeout=3000)
~~~

Les mots-clés de réponse n'affectent que l'opération en cours (sauf lorsqu'ils sont passés à
`Mouse()` lors de la création de l'objet). Pour modifier le comportement pour toutes les opérations ultérieures, définissez les propriétés de réponse directement:

~~~ .python
# Obtenir deux pressions gauche ou droite avec un délai de 5000 ms
ma_souris = Mouse()
ma_souris.buttonlist = [1,3]
ma_souris.timeout = 5000
bouton1, temps1 = ma_souris.get_click()
bouton2, temps2 = ma_souris.get_click()
~~~

Ou passez les mots-clés de réponse à `Mouse()` lors de la création de l'objet:

~~~ .python
# Obtenir deux pressions gauche ou droite avec un délai de 5000 ms
ma_souris = Mouse(buttonlist=[1,3], timeout=5000)
bouton1, temps1 = ma_souris.get_click()
bouton2, temps2 = ma_souris.get_click()
~~~

## flush(self)

Efface toutes les entrées en attente, sans se limiter à la souris.

__Retourne__

- True si un bouton a été cliqué (c'est-à-dire s'il y avait quelque chose à
vider) et False sinon.

__Exemple__

~~~ .python
ma_souris = Mouse()
ma_souris.flush()
bouton, position, horodatage = ma_souris.get_click()
~~~

## get_click(\*arglist, \*\*kwdict)

Collecte un clic de souris.

__Paramètres__

- **\*\*resp_args** : facultatif [mot-clé de réponse](#response-keywords) qui sera utilisé
pour cet appel à `Mouse.get_click()`. Cela n'affecte pas
les opérations ultérieures.

__Retourne__

- Un tuple (bouton, position, horodatage). Le bouton et la position sont
`None` si un délai se produit. La position est un tuple (x, y) en coordonnées d'écran.

__Exemple__

~~~ .python
ma_souris = Mouse()
bouton, (x, y), horodatage = ma_souris.get_click(timeout=5000)
if bouton is None:
        print("Un délai d'attente s'est produit!")
~~~

## get_click_release(\*arglist, \*\*kwdict)

*Nouveau dans v3.2.0*

Collecte la libération d'un clic de souris.

*Important:* ce
fonction n'est actuellement pas implémentée pour le
backend *psycho*.

__Paramètres__

- **\*\*resp_args**: Facultatif [mots-clés de réponse](#response-keywords) qui seront utilisés
pour cet appel à `Mouse.get_click_release()`. Cela n'affecte pas
les opérations ultérieures.

__Renvoie__

- Un tuple (bouton, position, horodatage). Le bouton et la position sont
`None` en cas de dépassement du temps imparti. La position est un tuple (x, y) en
coordonnées de l'écran.

__Exemple__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click_release(timeout=5000)
if button is None:
        print("Un dépassement de temps s'est produit !")
~~~

## get_pos(self)

Renvoie la position actuelle du curseur.

__Renvoie__

- Un tuple (position, horodatage).

__Exemple__

~~~ .python
my_mouse = Mouse()
(x, y), timestamp = my_mouse.get_pos()
print("Le curseur était à (%d, %d)" % (x, y))
~~~

## get_pressed(self)

Renvoie l'état actuel des boutons de la souris. Une valeur True signifie
que le bouton est actuellement enfoncé.

__Renvoie__

- Un tuple (button1, button2, button3) de valeurs booléennes.

__Exemple__

~~~ .python
my_mouse = Mouse()
buttons = my_mouse.get_pressed()
b1, b2, b3 = buttons
print("Boutons de souris enfoncés actuellement : (%d,%d,%d)" % (b1,b2,b3))
~~~

## set_pos(pos=(0, 0))

Définit la position du curseur de la souris.

__Attention :__ `set_pos()` est
peu fiable et échouera silencieusement sur
certains systèmes.

__Paramètres__

- **pos**: Un tuple (x,y) pour les nouvelles coordonnées de la souris.

__Exemple__

~~~ .python
my_mouse = Mouse()
my_mouse.set_pos(pos=(0,0))
~~~

## show_cursor(show=True)

Change immédiatement la visibilité du curseur de la souris.

__Note :__
Dans la plupart des cas, vous préférerez utiliser le mot-clé `visible`,
qui
modifie la visibilité lors de la collecte des réponses,
c'est-à-dire
pendant l'appel à `mouse.get_click()`. Appeler
`show_cursor()` ne
changera pas implicitement la valeur de `visible`,
ce qui peut entraîner
un comportement quelque peu contre-intuitif où le curseur
est caché dès que
`get_click()` est appelé.

__Paramètres__

- **show**: Indique si le curseur est affiché (True) ou masqué (False).

## synonyms(button)

Donne une liste de synonymes pour un bouton de souris. Par exemple, 1 et
'left_button' sont des synonymes.

__Paramètres__

- **button**: Une valeur de bouton.

__Renvoie__

- Une liste de synonymes.

</div>