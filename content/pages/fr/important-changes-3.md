title: Changements importants dans OpenSesame 3
hash: 5ff5aa4ddc6076985d2733031a24955084f95edb98e5b60980505b16b020ae44
locale: fr
language: French

[TOC]


## Changements dans la version 3.3

OpenSesame 3.3 apporte plusieurs améliorations majeures qui facilitent encore plus le développement d'expériences. OpenSesame 3.3 est entièrement compatible avec la version 3.2.


### Rapunzel : un nouvel éditeur de code

Rapunzel est un éditeur de code, axé sur le calcul numérique avec Python et R. Techniquement, Rapunzel est un ensemble d'extensions pour OpenSesame. Mais il ressemble et se comporte comme un programme autonome. Bon codage !

- <https://rapunzel.cogsci.nl/>


### Un nouvel éditeur de inline_script

En rapport avec le développement de Rapuznel : L'élément INLINE_SCRIPT utilise maintenant une autre bibliothèque (`PyQode`) pour l'éditeur de code. En conséquence, l'éditeur de code prend désormais en charge bon nombre des fonctionnalités que l'on attend d'un éditeur de code moderne, y compris l'introspection du code et la vérification statique du code.


### Plus d'espaces de couleurs

OpenSesame prend désormais en charge de manière native les espaces de couleurs HSV, HSL et CIElab.

- %link:manuel/python/canvas%


### Un nouveau backend sonore basé sur PsychoPy

Le backend par défaut est désormais *psycho*. L'un des avantages de ce backend est que la synchronisation de la présentation du son devrait être meilleure. Si vous rencontrez des saccades (lecture de son désynchronisée), vous pouvez toujours revenir au backend *psycho_legacy*, qui utilise l'ancien système de sons basé sur PyGame.


### Support des éléments inline_script dans les coroutines

Vous pouvez désormais utiliser des éléments `inline_script` dans les `coroutines`. Cela facilite la combinaison de scripts Python avec des coroutines, par rapport à l'ancienne méthode d'écriture d'une fonction de générateur personnalisée.

- %link:coroutine%


### OpenSesame : 


## Changements dans la version 3.2

OpenSesame 3.2 apporte plusieurs améliorations majeures qui facilitent encore plus le développement d'expériences. OpenSesame 3.2 est entièrement compatible avec la version 3.1.

### Une meilleure API Python, conforme à la PEP-8

La PEP-8 est un guide de style pour Python. Beaucoup de logiciels Python modernes suivent les directives PEP-8 - mais, pour des raisons historiques, OpenSesame ne le faisait pas. À partir de la version 3.2, l'API publique suit désormais la directive selon laquelle les noms de classes (et les fonctions d'usine qui génèrent des classes) doivent être en `CamelCase`, tandis que les noms d'objets et de fonctions doivent être en `underscore_case`. En pratique, cela signifie que vous créez maintenant un objet `Canvas` comme suit :

~~~ .python
my_canvas = Canvas() # Notez le C majuscule !
my_canvas.fixdot()
my_canvas.show())
~~~

Bien sûr, les anciens noms en `underscore_case` sont toujours disponibles en tant qu'alias, de sorte que la compatibilité ascendante est préservée.

L'API pour les formulaires a également été simplifiée. Vous n'avez plus besoin d'importer `libopensesame.widgets`, et vous n'avez plus besoin de passer `exp` comme premier argument :

~~~ .python
form = Form()
button = Button(text=u'Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### Améliorations du sketchpad et du Canvas

#### Accéder et modifier les éléments du Canvas

Les éléments d'un `Canvas` sont maintenant des objets qui peuvent être nommés, accessibles et modifiés. Cela signifie que vous n'avez plus besoin de redessiner un canvas entier pour changer un seul élément. Par exemple, vous pouvez dessiner un bras tournant comme suit :

~~~ .python
my_canvas = Canvas()
my_canvas['arm'] = Line(0, 0, 0, 0)
for x, y in xy_circle(n=100, rho=100):
	my_canvas['arm'].ex = x
	my_canvas['arm'].ey = y
	my_canvas.show()
	sleep(clock, 10)
~~~

Le SKETCHPAD permet également de nommer des éléments.

Pour plus d'informations, voir :

- %link:manuel/python/canvas%


#### Amélioration de la prise en charge du HTML et des scripts non latins

Le texte est maintenant rendu par Qt, qui est une bibliothèque moderne (la même bibliothèque qui est également utilisée pour l'interface graphique). Cela signifie que vous pouvez maintenant utiliser du vrai HTML dans votre texte. Cela signifie également que les scripts de gauche à droite et d'autres scripts non latins sont rendus beaucoup mieux.


#### Les images peuvent être tournées

Les images peuvent maintenant être tournées. Cette fonction est valable à la fois pour les éléments SKETCHPAD et les objets `Canvas`.

#### Travailler avec des coordonnées polaires

Si vous faites un clic droit sur un élément SKETCHPAD, vous pouvez sélectionner 'Spécifier les coordonnées polaires'. Cela vous permet de calculer les coordonnées cartésiennes (x, y) à partir des coordonnées polaires, ce qui est particulièrement utile si vous souhaitez créer des configurations circulaires.

### Améliorations des formulaires

#### Performance améliorée des formulaires

Les formulaires sont désormais beaucoup plus rapides lors de l'utilisation des backends *psycho* et *xpyriment*. Ceci est dû au fait que les éléments `Canvas` peuvent maintenant être mis à jour individuellement, comme décrit ci-dessus.

#### Validation de l'entrée du formulaire

Vous pouvez désormais valider l'entrée d'un formulaire, c'est-à-dire empêcher la fermeture d'un formulaire tant que certains critères ne sont pas respectés. De plus, vous pouvez exclure des caractères en tant qu'entrée des widgets `TextInput`.

Pour plus d'informations, voir:

- %link:manual/forms/validation%

### Améliorations clavier

#### Support des événements de relâchement de touches

L'objet `Keyboard()` dispose désormais d'une fonction `get_key_release()`, qui vous permet de récupérer les relâchements de touches. En raison des limitations des bibliothèques sous-jacentes, cette fonction présente deux limitations importantes :

- La `key` retournée peut être incorrecte sur les dispositions de clavier autres que QWERTY
- La fonction n'a pas été mise en œuvre pour le backend *psycho*

Pour plus d'informations, voir:

- %link:manual/response/keyboard%

### Améliorations de la souris

#### Support des événements de relâchement des clics de la souris

L'objet `Mouse()` dispose désormais d'une fonction `get_click_release()`, qui vous permet de récupérer les relâchements des clics de souris. Cette fonction n'est actuellement pas mise en œuvre pour le backend *psycho*.

Pour plus d'informations, voir:

- %link:manual/response/mouse%

#### Utiliser des sketchpads pour définir des zones d'intérêt

Vous pouvez maintenant définir un SKETCHPAD lié dans un élément `mouse_response`. Si vous faites cela, les noms des éléments sur le SKETCHPAD seront automatiquement utilisés comme zones d'intérêt (ROIs) pour les clics de souris.

### Mettre fin à votre expérience de force

Vous pouvez désormais mettre fin de force à votre expérience en cliquant sur le bouton Kill dans la barre d'outils principale. Cela signifie que vous n'avez plus besoin d'ouvrir un gestionnaire de processus/tâches pour mettre fin aux expériences incontrôlables !

### Support amélioré pour Mac OS

Les packages Mac OS ont été entièrement reconstruits par %-- github: {user: dschreij} --%. L'expérience Mac OS devrait désormais être bien plus fluide, rapide et moins sujette aux plantages.

### Une traduction turque

Une traduction turque complète a été apportée par %-- github: {user: aytackarabay} --%. Cela signifie qu'OpenSesame est maintenant entièrement traduit en français, allemand et turc. Une traduction partielle est disponible dans plusieurs autres langues.

## Changements dans la version 3.1

OpenSesame 3.1 apporte de nombreuses améliorations qui rendent encore plus facile le développement d'expériences. OpenSesame 3.1 est entièrement compatible avec la version 3.0.

### Un nouveau look !

OpenSesame a un nouveau thème d'icônes, basé sur [Moka](https://snwh.org/moka) de Sam Hewitt. De plus, l'interface utilisateur a été repensée sur la base de directives d'interface humaine cohérentes. Nous espérons que vous aimerez ce nouveau look autant que nous !

### Une boucle redessinée

La LOOP est désormais plus facile à utiliser et vous permet de contraindre l'aléa; cela permet, par exemple, d'empêcher qu'un même stimulus se répète deux fois d'affilée.

Pour plus d'informations, voir:

- %link:loop%

### Coroutines: faire les choses en parallèle

Le plugin COROUTINES est désormais inclus par défaut. Les COROUTINES vous permettent d'exécuter plusieurs autres éléments en parallèle ; cela permet, par exemple, de collecter en continu des pressions de touches tout en présentant une série de SKETCHPADs.

Pour plus d'informations, voir:

- %link:coroutines%

### Intégration du cadre scientifique ouvert

Vous pouvez désormais vous connecter à [Open Science Framework](http://osf.io) (OSF) depuis OpenSesame, et synchroniser sans effort les expériences et les données entre votre ordinateur et l'OSF. Merci au [Center for Open Science](http://cos.io/) pour le soutien de cette fonctionnalité!

Pour plus d'informations, voir:

- %link:osf%

### Un objet de réponses 

Il y a un nouvel objet Python standard : `responses`. Celui-ci garde une trace de toutes les réponses collectées au cours de l'expérience.

Pour plus d'informations, voir :

- %link:responses%

## Changements dans la version 3.0

OpenSesame 3.0 a apporté de nombreuses améliorations qui rendent encore plus facile le développement d'expériences. La plupart des changements sont rétrocompatibles. En d'autres termes, vous pouvez toujours faire les choses de l'ancienne manière. Cependant, quelques changements ne sont pas rétrocompatibles, et il est important d'en être conscient.

### Changements non rétrocompatibles

#### Propriétés de Sampler

L'objet SAMPLER a un certain nombre de propriétés qui étaient auparavant des fonctions. Cela concerne :

- `sampler.fade_in`
- `sampler.pan`
- `sampler.pitch`
- `sampler.volume`

Pour plus d'informations, voir :

- %link:sampler%

#### Couleurs compatibles CSS3

Vous pouvez désormais utiliser des spécifications de couleurs compatibles CSS3, comme décrit ici :

- %link:manual/python/canvas%

Si vous utilisez des noms de couleurs (par exemple 'red', 'green', etc.), cela peut entraîner des couleurs légèrement différentes. Par exemple, selon CSS3, 'green' est `#008000` au lieu de (comme c'était le cas auparavant) `#00FF00`.

### Nouveau format de fichier (.osexp)

OpenSesame enregistre désormais les expériences au format `.osexp`. Bien sûr, vous pouvez toujours ouvrir les anciens formats (`.opensesame` et `.opensesame.tar.gz`). Pour plus d'informations, voir :

- %link:fileformat%

### API Python simplifiée

#### Plus de self et exp

Il n'est plus nécessaire de préfixer `self.` ou `exp.` lors de l'appel de fonctions couramment utilisées. Par exemple, cela définira de manière programmatique le numéro de sujet à 2 :

~~~ .python
set_subject_nr(2)
~~~

Pour une liste des fonctions courantes, voir :

- %link:manual/python/common%

#### L'objet `var` : accès et modification faciles des variables expérimentales

L'ancienne façon d'utiliser `self.get()` pour obtenir et `exp.set()` pour définir des variables expérimentales a été remplacée par une syntaxe plus simple. Par exemple, pour définir la variable `condition`, afin de pouvoir la référencer en tant que `[condition]` dans les SKETCHPADs, etc. :

~~~ .python
var.condition = 'easy`'
~~~

Et pour obtenir une variable expérimentale `condition` qui a été, par exemple, définie dans une LOOP :

~~~ .python
print('Condition is %s' % var.condition)
~~~

Pour plus d'informations, voir :

- %link:var%

#### L'objet `clock` : fonctions de temps

Les fonctions de temps sont maintenant disponibles via l'objet `clock` :

~~~ .python
print('Current timestamp: %s' % clock.time())
clock.sleep(1000) # Sleep for 1 s
~~~

Pour plus d'informations, voir :

- %link:clock%

#### L'objet `pool` : accès à la pool de fichiers

La pool de fichiers est maintenant accessible via l'objet `pool`, qui prend en charge une interface de type `dict` (mais qui n'est pas vraiment un `dict` Python) :

~~~ .python
path = pool['image.png']
print('The full path to image.png is: %s' % path)
~~~

Pour plus d'informations, voir :

- %link:pool%

#### Plus de from openexp.* import *

Il n'est plus nécessaire d'importer les classes `openexp`, et de passer `exp` en tant que premier argument. Au lieu de cela, pour créer un objet `canvas`, vous pouvez simplement faire :

~~~ .python
my_canvas = canvas()
~~~

Il existe des fonctions similaires (comme on les appelle) pour `keyboard`, `mouse`, et SAMPLER.

Pour plus d'informations, voir :

- %link:manual/python/common%

#### Le synth est maintenant un échantillonneur

Le SYNTH n'est plus une classe à part entière. Au lieu de cela, c'est une fonction qui retourne un objet SAMPLER qui a été rempli avec un échantillon synthétisé.

### Améliorations de l'interface utilisateur

#### Une fenêtre de débogage IPython

IPython, un terminal Python interactif pour le calcul scientifique, est désormais utilisé pour la fenêtre de débogage.

#### Un inspecteur de variables en direct

L'inspecteur de variables affiche désormais les valeurs réelles de vos variables pendant l'exécution de votre expérience et après la fin de celle-ci.

#### Annuler

Vous pouvez enfin annuler vos actions !

#### Un nouveau schéma de couleurs

Le schéma de couleurs par défaut est maintenant *Monokai*. Encore un schéma de couleurs sombres, mais avec un contraste plus élevé que le précédent par défaut, *Solarized*. Cette augmentation devrait augmenter la lisibilité. Et ça a l'air bien !

### Coordonnées cohérentes

Précédemment, OpenSesame utilisait des coordonnées d'écran mixtes et incohérentes : `0,0` était en haut à gauche de l'affichage lors de l'utilisation du code Python, et au centre de l'affichage lors de l'utilisation des éléments SKETCHPAD, etc. À partir de la version 3.0, le centre de l'affichage est toujours `0,0`, également dans le code Python.

Si vous souhaitez revenir à l'ancien comportement, vous pouvez désactiver l'option "Coordonnées uniformes" dans l'onglet général. Pour des raisons de compatibilité ascendante, les "Coordonnées uniformes" sont automatiquement désactivées lorsque vous ouvrez une ancienne expérience.

### Utiliser Python dans les chaînes de texte

Vous pouvez désormais intégrer Python dans les chaînes de texte en utilisant la syntaxe `[=...]`. Par exemple, la chaîne de texte suivante dans un SKETCHPAD :

~~~
Deux fois deux égale [=2*2]
~~~

... affichera :

~~~
Deux fois deux égale 4
~~~

Pour plus d'informations, consultez :

- %link:text%

### Support de Python 3

OpenSesame prend désormais en charge Python >= 3.4. Cependant, plusieurs dépendances d'OpenSesame, notamment PsychoPy et Expyriment, sont uniquement en Python 2. Par conséquent, Python 2.7 reste la version par défaut de Python.