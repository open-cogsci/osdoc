<div class="ClassDoc YAMLDoc" markdown="1">

## Canvas(auto_prepare=True, \*\*style_args)

Une fonction d'usine qui crée un nouvel objet `Canvas`. Pour une
description des mots-clés possibles, voir :

- %link:manual/python/canvas%


__Renvoie__

- Un objet `Canvas`.

__Exemple__

~~~ .python
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~



## Experiment(osexp_path=None, log_path='defaultlog.csv', fullscreen=False, subject_nr=0, \*\*kwargs)

Une fonction d'usine qui crée un nouvel objet `Experiment`. Ceci est seulement
utile lorsqu'on implémente une expérience entièrement à travers un script Python,
plutôt que par l'interface utilisateur.


__Paramètres__

- **osexp_path** : Si un chemin vers un fichier `.osexp` est spécifié, ce fichier est ouvert et
peut être exécuté directement en appelant `Experiment.run()`. Si aucun fichier d'expérience
n'est spécifié, une expérience vide est initialisée.
- **log_path** : 
- **fullscreen** : 
- **subject_nr** : 
- **kwargs**: Arguments clés optionnels qui sont interprétés comme des variables expérimentales.
L'usage principal de ceci est de spécifier le backend à travers
le mot-clé `canvas_backend`.

__Renvoie__

- Un tuple (exp, win, clock, log) correspondant aux objets Experiment,
gestionnaire de fenêtre (spécifique au backend), Clock et Log.

__Exemple__

Pour implémenter une expérience entièrement de manière programmatique :

~~~ .python
from libopensesame.python_workspace_api import (
    Experiment, Canvas, Text, Keyboard)
exp, win, clock, log = Experiment(canvas_backend='legacy')
c = Canvas()
c += Text('Press any key')
c.show()
kb = Keyboard()
kb.get_key()
exp.end()
~~~

Pour charger un fichier d'expérience et l'exécuter :

~~~ .python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
~~~



## Form(\*args, \*\*kwargs)

Une fonction d'usine qui crée un nouvel objet `Form`. Pour une
description
des mots-clés possibles, voir :

- %link:manual/forms/widgets%


__Renvoie__

- Un objet `Form`.

__Exemple__

~~~ .python
form = Form()
label = Label(text='label')
button = Button(text='Ok')
form.set_widget(label, (0,0))
form.set_widget(button, (0,1))
form._exec()
~~~



## Keyboard(\*\*resp_args)

Une fonction d'usine qui crée un nouvel objet `Keyboard`. Pour une
description des mots-clés possibles, voir :

- %link:manual/python/keyboard%


__Renvoie__

- Un objet `Keyboard`.

__Exemple__

~~~ .python
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key, time = my_keyboard.get_key()
~~~



## Mouse(\*\*resp_args)

Une fonction d'usine qui crée un nouvel objet `Mouse`. Pour une
description
des mots-clés possibles, voir :

- %link:manual/python/mouse%


__Renvoie__

- Un objet `mouse`.

__Exemple__

~~~ .python
my_mouse = Mouse(keylist=[1,3], timeout=5000)
button, time = my_mouse.get_button()
~~~



## Sampler(src, \*\*playback_args)

Une fonction d'usine qui crée un nouvel objet `Sampler`. Pour une
description des mots-clés possibles, voir :

- %link:manual/python/sampler%


__Renvoie__

- Un objet SAMPLER.

__Exemple__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~



## Synth(osc='sine', freq=440, length=100, attack=0, decay=5)

Une fonction d'usine qui synthétise un son et le retourne sous forme d'
objet `Sampler`.


__Paramètres__

- **osc** : Oscillateur, peut être "sine", "saw", "square" ou "white_noise".
- **freq** : Fréquence, soit une valeur entière (valeur en hertz) ou une chaîne ("A1",
"eb2", etc.).
- **length** : La durée du son en millisecondes.
- **attack** : Le temps d'attaque (fade-in) en millisecondes.
- **decay** : Le temps de décroissance (fade-out) en millisecondes.

__Renvoie__

- Un objet SAMPLER.

__Exemple__

~~~ .python
my_sampler = Synth(freq=u'b2', length=500)
~~~



## copy_sketchpad(name)

Renvoie une copie du canvas d'un `sketchpad`.


__Paramètres__

- **name** : Le nom du `sketchpad`.

__Renvoie__

- Une copie du canvas du `sketchpad`.

__Exemple__

~~~ .python
my_canvas = copy_sketchpad('mon_sketchpad')
my_canvas.show()
~~~

## pause()

Met l'expérience en pause.

## register_cleanup_function(fnc)

Enregistre une fonction de nettoyage, qui est exécutée lorsque l'expérience se termine. Les fonctions de nettoyage sont exécutées à la toute fin, après la fermeture de l'affichage, du dispositif sonore et du fichier de journal. Les fonctions de nettoyage sont également exécutées lorsque l'expérience échoue.

__Exemple__

~~~ .python
def ma_fonction_de_nettoyage():
        print(u"L'expérience est terminée!")
register_cleanup_function(ma_fonction_de_nettoyage)
~~~

## reset_feedback()

Réinitialise toutes les variables de feedback à leur état initial.

__Exemple__

~~~ .python
reset_feedback()
~~~

## set_subject_nr(nr)

Définit le numéro de participant et la parité (pair/impair). Cette fonction est appelée automatiquement lorsqu'une expérience est lancée, vous n'avez donc besoin de l'appeler vous-même que si vous écrivez par-dessus le numéro de participant qui a été spécifié lors du lancement de l'expérience.

__Paramètres__

- **nr**: Le numéro de participant.

__Exemple__

~~~ .python
set_subject_nr(1)
print('Numéro de participant = %d' % var.subject_nr)
print('Parité = %s' % var.subject_parity)
~~~

## sometimes(p=0.5)

Retourne True avec une certaine probabilité. (Pour une randomisation plus avancée, utilisez le module `random` de Python.)

__Paramètres__

- **p**: La probabilité de retourner True.

__Retourne__

- True ou False

__Exemple__

~~~ .python
if sometimes():
        print('Parfois tu gagnes')
else:
        print('Parfois tu perds')
~~~

## xy_circle(n, rho, phi0=0, pole=(0, 0))

Génère une liste de points (coordonnées x,y) dans un cercle. Ceci peut être utilisé pour dessiner des stimuli dans un arrangement circulaire.

__Paramètres__

- **n**: Le nombre de coordonnées x,y à générer.
- **rho**: La coordonnée radiale, aussi appelée distance ou excentricité, du premier point.
- **phi0**: La coordonnée angulaire pour la première coordonnée. Il s'agit d'une rotation antihoraire en degrés (et non en radians), où 0 est à droite.
- **pole**: Le point de référence.

__Retourne__

- Une liste de tuples de coordonnées (x,y).

__Exemple__

~~~ .python
# Dessiner 8 rectangles autour d'un point de fixation central
c = Canvas()
c.fixdot()
for x, y in xy_circle(8, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

## xy_distance(x1, y1, x2, y2)

Indique la distance entre deux points.

__Paramètres__

- **x1**: La coordonnée x du premier point.
- **y1**: La coordonnée y du premier point.
- **x2**: La coordonnée x du second point.
- **y2**: La coordonnée y du second point.

__Retourne__

- La distance entre les deux points.

## xy_from_polar(rho, phi, pole=(0, 0))

Convertit les coordonnées polaires (distance, angle) en coordonnées cartésiennes (x, y).

__Paramètres__

- **rho**: La coordonnée radiale, c'est-à-dire la distance ou l'excentricité.
- **phi**: La coordonnée angulaire. Elle reflète une rotation dans le sens des aiguilles d'une montre en degrés (c'est-à-dire pas en radians), où 0 est droit devant.
- **pole**: Le point de référence.

__Retourne__

- Un tuple de coordonnées (x, y).

__Exemple__

~~~ .python
# Dessiner une croix
x1, y1 = xy_from_polar(100, 45)
x2, y2 = xy_from_polar(100, -45)
c = Canvas()
c.line(x1, y1, -x1, -y1)
c.line(x2, y2, -x2, -y2)
c.show()
~~~

## xy_grid(n, spacing, pole=(0, 0))

Génère une liste de points (coordonnées x,y) dans une grille. Ceci peut être utilisé pour dessiner des stimuli dans un arrangement en grille.

__Paramètres__

- **n**: Un `int` qui indique le nombre de colonnes et de lignes, de sorte que `n=2` indique une grille 2x2, ou un tuple (n_col, n_row), de sorte que `n=(2,3)` indique une grille 2x3.
- **spacing**: Une valeur numérique indiquant l'espacement entre les cellules, ou un tuple (col_spacing, row_spacing).
- **pole**: Le point de référence.

__Retourne__

- Une liste de tuples de coordonnées (x,y).

__Exemple__

~~~ .python
# Dessiner une grille 4x4 de rectangles
c = Canvas()
c.fixdot()
for x, y in xy_grid(4, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

## xy_random(n, width, height, min_dist=0, pole=(0, 0))

Génère une liste de points aléatoires (coordonnées x, y) avec un espacement minimum
entre chaque paire de points. Cette fonction générera une exception si la liste des coordonnées ne peut pas être générée, généralement parce qu'il y a trop de points, la min_dist est trop élevée, ou la largeur ou la hauteur sont trop faibles.


__Paramètres__

- **n** : Le nombre de points à générer.
- **width** : La largeur du champ avec des points aléatoires.
- **height** : La hauteur du champ avec des points aléatoires.
- **min_dist** : La distance minimale entre chaque point.
- **pole** : Le point de référence.

__Renvoie__

- Une liste de tuples de coordonnées (x, y).

__Exemple__

~~~ .python
# Dessiner 50 rectangles dans une grille aléatoire
c = Canvas()
c.fixdot()
for x, y in xy_random(50, 500, 500, min_dist=40):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_to_polar(x, y, pole=(0, 0))

Convertit les coordonnées cartésiennes (x, y) en coordonnées polaires (distance,
angle).


__Paramètres__

- **x** : La coordonnée X.
- **y** : La coordonnée Y.
- **pole** : Le point de référence.

__Renvoie__

- Un tuple de coordonnées (rho, phi). Ici, `rho` est la coordonnée radiale,
aussi distance ou excentricité. `phi` est la coordonnée angulaire en
degrés (c'est-à-dire pas en radians), et reflète une rotation antihoraire,
où 0 est tout droit à droite.

__Exemple__

~~~ .python
rho, phi = xy_to_polar(100, 100)
~~~



</div>