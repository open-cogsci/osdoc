title: À propos de Python
hash: 99b67bfe88b7ad764c9bc1c2a5da5b4114e573e6c0e442ff7f88dc080051e6b2
locale: fr
language: French

Dans OpenSesame, vous pouvez créer des expériences complexes en utilisant uniquement l'interface graphique (GUI). Cependant, vous rencontrerez parfois des situations dans lesquelles les fonctionnalités offertes par la GUI sont insuffisantes. Dans ces cas, vous pouvez ajouter du code Python à votre expérience.

Python n'est pas pris en charge dans les expériences en ligne avec OSWeb. Si vous devez exécuter votre expérience en ligne, vous devez utiliser [JavaScript](%url:manual/javascript/about%) à la place.

[TOC]

## Apprendre Python

Vous pouvez trouver un ensemble de tutoriels et d'exercices de base pour commencer avec Python sur <https://pythontutorials.eu/>.

## Python dans l'interface graphique d'OpenSesame

### Un seul espace de travail Python

Tout le code Python est exécuté dans un seul espace de travail Python. Cela signifie que les variables définies dans un INLINE_SCRIPT sont accessibles dans tous les autres INLINE_SCRIPT, ainsi que dans les instructions Python intégrées dans les instructions run-if et les chaînes de texte. Le même principe s'applique aux modules : une fois `importé`, ils sont disponibles partout.

Par exemple, vous pouvez simplement construire le `Canvas` dans un INLINE_SCRIPT...

~~~ .python
mon_canvas = Canvas()
mon_canvas.fixdot()
~~~

... et le montrer dans un autre INLINE_SCRIPT ...

~~~ .python
mon_canvas.show()
~~~

### Éléments inline_script

Pour utiliser du code Python, vous devez ajouter un élément INLINE_SCRIPT à votre expérience. Vous pouvez le faire en faisant glisser l'icône Python (l'icône bleue/jaune) de la barre d'outils des éléments dans la séquence de l'expérience. Après avoir fait cela, vous verrez quelque chose comme %FigInlineScript.

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: L'élément INLINE_SCRIPT.
--%

Comme vous pouvez le voir, l'élément INLINE_SCRIPT se compose de deux onglets : un pour la phase de préparation et un pour la phase d'exécution. La phase de préparation est exécutée en premier, pour permettre aux éléments de se préparer pour la phase d'exécution sensible au temps. Il est recommandé de construire des objets `Canvas`, des objets `Sampler`, etc. pendant la phase de préparation, afin qu'ils puissent être présentés sans délai pendant la phase d'exécution. Mais il ne s'agit que d'une convention ; vous pouvez exécuter du code Python arbitraire pendant les deux phases.

Pour plus d'informations sur la stratégie de préparation-exécution, voir :

- %link:prepare-run%

### Expressions conditionnelles ("if")

Vous pouvez utiliser des expressions Python d'une seule ligne dans les expressions conditionnelles. Par exemple, vous pouvez utiliser le script Python suivant comme expression run-if (voir aussi %FigRunIf) :

~~~ .python
correct == 1 and response_time < 1000
~~~

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: Utilisation du script Python dans l'instruction run-if d'un élément SEQUENCE.
--%

Pour plus d'informations sur les expressions conditionnelles ("if"), voir :

- %link:manual/variables%

### Python dans les chaînes de texte

Vous pouvez intégrer des instructions Python dans les chaînes de texte en utilisant la syntaxe {...}. Cela fonctionne pour les références de variables simples, mais aussi pour les expressions d'une seule ligne. Par exemple, vous pouvez ajouter le texte suivant à un SKETCHPAD :

```text
La résolution est de {width} x {height} px, soit un total de {width * height} pixels
```

En fonction de la résolution de votre expérience, cela pourrait donner :

```text
La résolution est de 1024 x 768 px, soit un total de 786432 pixels
```

Pour plus d'informations sur les variables et le texte, voir :

- %link:manual/variables%
- %link:manual/stimuli/text%

### La console Jupyter (fenêtre de débogage)

OpenSesame redirige la sortie standard vers la console (ou : fenêtre de débogage), que vous pouvez activer avec la touche Contrôle + D ou via le menu (Menu -> Affichage -> Afficher la fenêtre de débogage ; voir %FigDebugNormal). Vous pouvez imprimer sur la console en utilisant `print()`.

~~~ .python
print('Ceci apparaîtra dans la fenêtre de débogage !')
~~~

La console est également un interpréteur Python interactif alimenté par [projet Jupyter](https://jupyter.org).

## Choses à savoir

### Fonctions courantes

De nombreuses fonctions courantes sont directement disponibles dans un élément INLINE_SCRIPT, sans avoir besoin d'importer quoi que ce soit. Par exemple :

~~~ .python
# `Canvas()` est une fonction usine qui renvoie un objet `Canvas`
fixdot_canvas = Canvas()
if sometimes(): # Parfois, le fixdot est vert
    fixdot_canvas.fixdot(color='green')
else: # Parfois, il est rouge
    fixdot_canvas.fixdot(color='red')
fixdot_canvas.show()
~~~

Pour une liste des fonctions courantes, consultez :

- %link:manual/python/common%


### L'objet `var` : Accès aux variables expérimentales

__Note de version__ Depuis OpenSesame 4.0, toutes les variables expérimentales sont disponibles en tant que variables globales. Cela signifie que vous n'avez plus besoin de l'objet `var`.
{:.page-notification}

Vous pouvez accéder aux variables expérimentales via l'objet `var` :

~~~ .python
# Obtenir une variable expérimentale
print('my_variable est : %s' % var.my_variable)
# Définir une variable expérimentale
var.my_variable = 'my_value'
~~~

Un aperçu complet de l'objet `var` se trouve ici :

- %link:manual/python/var%


### L'objet `clock` : Fonctions de temps

Les fonctions de temps de base sont disponibles via l'objet `clock` :

~~~ .python
# Obtenir l'horodatage actuel
t = clock.time()
# Attendre pendant 1 s
clock.sleep(1000)
~~~

Un aperçu complet de l'objet `clock` se trouve ici :

- %link:manual/python/clock%


### L'objet `log` : Enregistrement des données

L'enregistrement des données est disponible via l'objet `log` :

~~~ .python
# Écrire une ligne de texte
log.write('Mon message de journal personnalisé')
# Écrire toutes les variables
log.write_vars()
~~~

Un aperçu complet de l'objet `log` se trouve ici :

- %link:manual/python/log%


### L'objet `pool` : Accès au pool de fichiers

Vous obtenez le chemin complet d'un fichier dans le pool de fichiers via l'objet `pool` :

~~~ .python
# Afficher une image du pool de fichiers
path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(path)
my_canvas.show()
~~~

Un aperçu complet de l'objet `pool` se trouve ici :

- %link:manual/python/pool%


### L'objet `responses` : Accès aux réponses des participants

L'objet `responses` suit toutes les réponses des participants qui ont été collectées pendant l'expérience. Par exemple, pour lister la justesse de toutes les réponses jusqu'à présent :

~~~ .python
for response in responses:
	print(response.correct)
~~~

Un aperçu complet de l'objet `responses` se trouve ici :

- %link:manual/python/responses%


### La classe `Canvas` : Présentation de stimuli visuels

La classe `Canvas` est utilisée pour présenter des stimuli visuels. Par exemple, vous pouvez afficher un point de fixation comme suit :

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

Un aperçu complet de la classe `Canvas` se trouve ici :

- %link:manual/python/canvas%


### La classe `Keyboard` : Collecte des touches du clavier

La classe `Keyboard` est utilisée pour collecter les pressions sur les touches. Par exemple, pour collecter une pression de touche avec un délai d'expiration de 1000 ms :

~~~ .python
my_keyboard = Keyboard(timeout=1000)
key, time = my_keyboard.get_key()
~~~

Un aperçu complet de la classe `Keyboard` se trouve ici :

- %link:manual/python/keyboard%


### La classe `Mouse` : Collecte des clics de souris et des écrans tactiles

La classe `Mouse` est utilisée pour collecter les clics de souris et les écrans tactiles. (OpenSesame ne fait pas de distinction entre les deux.) Par exemple, pour collecter un clic de souris avec un délai d'expiration de 1000 ms :

~~~ .python
my_mouse = Mouse(timeout=1000)
button, position, time = my_mouse.get_click()
~~~

Un aperçu complet de la classe `Mouse` se trouve ici :

- %link:manual/python/mouse%


### La classe `Sampler` : Lecture de sons

La classe `Sampler` est utilisée pour lire des échantillons sonores. Par exemple, pour lire un simple bip :

~~~ .python
my_sampler = Sampler()
my_sampler.play()
~~~

Un aperçu complet de la classe `Sampler` se trouve ici :

- %link:manual/python/sampler%


## Modules alternatifs pour la présentation d'affichages, la collecte de réponses, etc.


### `psychopy`

Si vous utilisez le backend *psycho*, vous pouvez utiliser directement les différents modules [PsychoPy]. Pour plus d'informations, consultez :

- %link:backends%


### `expyriment`

Si vous utilisez le backend *xpyriment*, vous pouvez utiliser directement les différents modules [Expyriment]. Pour plus d'informations, consultez :

- %link:backends%

### `pygame`

Si vous utilisez le backend *legacy*, *droid*, ou *xpyriment* (uniquement avec "Use OpenGL" réglé sur "non"), vous pouvez utiliser directement les différents modules [PyGame]. Pour plus d'informations, consultez :

- %link:backends%


[python]: http://www.python.org/
[backends]: /backends/about-backends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org/
[pygame]: http://www.pygame.org/