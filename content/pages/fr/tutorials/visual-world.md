title: Monde visuel
uptodate: false
hash: 4ac4d55fb2dfdae5994a02f5232db7371e19d2ec696b2f027b0405c5e625da78
locale: fr
language: French

[TOC]

## À propos de ce tutoriel

Ce tutoriel suppose une connaissance de base d'OpenSesame et, pour certaines parties, de Python. Par conséquent, si vous n'êtes pas familier avec OpenSesame ou Python, je vous recommande de suivre les tutoriels débutant et intermédiaire avant de continuer avec ce tutoriel :

- %link:beginner%
- %link:intermediate%

Dans ce tutoriel, vous apprendrez les éléments suivants :

- Suivi oculaire avec PyGaze
- Faire des choses en parallèle avec `coroutines`
- Utiliser des opérations `loop` avancées

## À propos de l'expérience

Dans ce tutoriel, nous mettrons en œuvre un *paradigme du monde visuel*, qui a été introduit par Cooper (1974; pour un examen, voir aussi Huettig, Rommers, et Meyer, 2011). Dans ce paradigme, les participants entendent une phrase prononcée, pendant qu'ils regardent un écran avec plusieurs objets. Nous utiliserons quatre objets distincts présentés dans les quatre quadrants de l'écran (%FigParadigm).

%--
figure:
 id: FigParadigm
 source: visual-world-paradigm.svg
 caption: >
  Un schéma de notre séquence d'essai. Il s'agit d'un exemple d'essai de correspondance complète, car l'objet cible (la pomme) est directement mentionné dans la phrase parlée. Stimuli tirés des stimuli [BOSS](https://sites.google.com/site/bosstimuli/) (Brodeur et al., 2010).
--%

La phrase parlée fait référence à un ou plusieurs des objets. Par exemple, une pomme (l'objet cible) peut être montrée pendant que la phrase parlée "au petit déjeuner, la fille a mangé une pomme" est jouée. Dans ce cas, la cible correspond à la phrase complète. La phrase peut également faire référence indirectement à un objet montré. Par exemple, une pomme (là encore l'objet cible) peut être montrée pendant que la phrase parlée "au petit déjeuner, la fille a mangé une banane" est jouée. Dans ce cas, l'objet cible correspond à la phrase sémantiquement, car une banane et une pomme sont tous les deux des fruits qu'une fille peut manger au petit déjeuner.

Pendant l'expérience, la position des yeux est enregistrée et la proportion de fixations sur les objets cibles et les objets non-cibles est mesurée dans le temps. La découverte typique est alors que les yeux sont attirés vers les objets cibles; c'est-à-dire que les participants regardent principalement les objets qui sont directement ou indirectement mentionnés par la phrase parlée. Et plus la référence est directe, plus cet effet est fort.

Formalisons ceci davantage. Notre expérience aura la conception suivante :

- Un facteur (Target Match) avec deux niveaux (Full ou Semantic), varié au sein des sujets. Dans la condition Full Match, l'objet cible est directement mentionné dans la phrase. Dans la condition de correspondance sémantique, l'objet cible est lié de manière sémantique à un objet mentionné dans la phrase.
- Nous avons 16 phrases parlées et seize objets cibles. Chaque phrase et chaque objet cible est montré deux fois : une fois dans la condition Full Match et une fois dans la condition Semantic Match.
- Nous avons 16 × 3 = 48 objets distracteurs, dont chacun (comme les cibles) est montré deux fois.
- Chaque essai commence avec un point de fixation pendant 1 s, suivi de la présentation des stimuli, suivi 1 s plus tard par le début de la phrase parlée. L'essai se termine 5 s plus tard.

## Le tutoriel

### Étape 1 : Téléchargez et démarrez OpenSesame

OpenSesame est disponible pour Windows, Linux, Mac OS (expérimental) et Android (runtime uniquement). Ce tutoriel est écrit pour OpenSesame 3.2.X *Kafkaesque Koffka*. Pour pouvoir utiliser PyGaze, vous devez télécharger la version Python 2.7 (qui est la version par défaut). Vous pouvez télécharger OpenSesame ici :

- %link:download%

(Si vous démarrez OpenSesame pour la première fois, vous verrez un onglet Welcome. Fermez cet onglet.) Lorsque vous démarrez OpenSesame, il vous sera proposé de choisir des expériences de modèles et, le cas échéant, une liste d'expériences récemment ouvertes (voir %FigStartUp). Cliquez sur "Default Template" pour commencer avec une expérience presque vide.

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

### Étape 2 : Construire la structure principale de l'expérience

Pour l'instant, construisez la structure principale suivante pour votre expérience (voir aussi %FigMainStructure) :

1. Nous commençons par un écran d'instructions. Ce sera un `sketchpad`.
2. Ensuite, nous exécutons un bloc d'essais. Ce sera une seule `séquence`, correspondant à un seul essai, à l'intérieur d'une seule `boucle`, correspondant à un bloc d'essais. Vous pouvez laisser la séquence d'essai vide pour l'instant !
3. Enfin, nous terminons avec un écran d'au revoir.

Nous devons également changer la couleur de premier plan de l'expérience en noir et la couleur d'arrière-plan en blanc. C'est parce que nous utiliserons des images qui ont un fond blanc, et nous ne voulons pas que ces images ressortent !

Et n'oubliez pas de donner à votre expérience un nom sensé et de la sauvegarder !

%--
figure:
 id: FigMainStructure
 source: main-structure.png
 caption: |
  La structure principale de l'expérience.
--%

### Étape 3 : Importer les fichiers dans le pool de fichiers

Pour cette expérience, nous avons besoin de stimuli : des fichiers sonores pour les phrases prononcées et des fichiers d'images pour les objets. Téléchargez-les à partir du lien ci-dessous, extrayez le fichier `zip` et placez les stimuli dans le pool de fichiers de votre expérience (voir aussi %FigFilePool).

- %static:attachments/visual-world/stimuli.zip%

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Le pool de fichiers de votre expérience après que tous les stimuli ont été ajoutés.
--%

### Étape 4 : Définir les variables expérimentales dans la boucle de blocs

La *boucle de blocs* est l'endroit où nous définissons les variables expérimentales en les entrant dans un tableau, où chaque ligne correspond à un essai et chaque colonne correspond à une variable expérimentale.

Pour l'instant, nous définissons uniquement la condition Full Match, dans laquelle l'objet cible est directement mentionné dans la phrase parlée. (Nous ajouterons la condition Semantic Match dans le cadre des travaux supplémentaires.)

Nous avons besoin des variables suivantes. Tout d'abord, ajoutez simplement des colonnes au tableau de la boucle, sans donner de contenu aux lignes.

- `pic1` — le nom de la première image (par exemple, 'apple.jpg')
- `pic2` — le nom de la deuxième image
- `pic3` — le nom de la troisième image
- `pic4` — le nom de la quatrième image
- `pos1` — la position de la première image (par exemple, 'topleft')
- `pos2` — la position de la première image
- `pos3` — la position de la première image
- `pos4` — la position de la première image
- `sound` — le nom d'un fichier son contenant une phrase parlée (par exemple, 'apple.ogg').

L'objet cible correspondra toujours à `pic1`. Nous avons les objets cibles suivants ; c'est-à-dire que pour les objets suivants, nous avons des fichiers sonores qui s'y réfèrent. Copiez-collez simplement la liste suivante dans la colonne `pic1` du tableau :

~~~
apple.jpg
armchair.jpg
banana.jpg
bear.jpg
card.jpg
cello.jpg
chicken.jpg
cookie.jpg
croissant.jpg
dice.jpg
egg.jpg
guitar.jpg
keyboard.jpg
mouse.jpg
sofa.jpg
wolf.jpg
~~~

Et faites de même pour les fichiers sonores :

~~~
apple.ogg
armchair.ogg
banana.ogg
bear.ogg
card.ogg
cello.ogg
chicken.ogg
cookie.ogg
croissant.ogg
dice.ogg
egg.ogg
guitar.ogg
keyboard.ogg
mouse.ogg
sofa.ogg
wolf.ogg
~~~

Le reste des images sont des distracteurs. Copiez-collez la liste suivante dans les colonnes `pic2`, `pic3` et `pic4`, de telle manière que chaque colonne ait exactement 16 lignes. (Si vous faites accidentellement un tableau de plus de 16 lignes, sélectionnez simplement les lignes superflues, faites un clic droit et supprimez-les.)

~~~
basketball01.jpg
basketballhoop02.jpg
baignoire.jpg
battery02b.jpg
hache.jpg
cuirassé.jpg
raquetteplage01a.jpg
belt03b.jpg
etagere.jpg
capsule.jpg
bol01.jpg
gantdebox02a.jpg
camionnette.jpg
bracelet01.jpg
modèlecervel.jpg
brique.jpg
bulldozer.jpg
_autotamponneuse.jpg
buste.jpg
bouton01.jpg
cactus.jpg
calculatrice01.jpg
calendrier.jpg
appareilphoto01b.jpg
cd.jpg
ventilateur_plafond02.jpg
téléphone portable.jpg
moufle04.jpg
monument.jpg
lune.jpg
motortour02.jpg
flaconhuilemoteur03b.jpg
mrpatatetête.jpg
coupe-ongles03b.jpg
pincenef03a.jpg
tabledenuit.jpg
nintendods.jpg
panneauinterdictionstationner.jpg
four.jpg
tétines02a.jpg
potdepeinture01.jpg
pantalon.jpg
avion_papier.jpg
trombone02.jpg
fontaine_publique.jpg
_parasolterrasse.jpg
taille-crayon03b.jpg
moulinàpoivre01a.jpg
~~~

Maintenant, nous devons spécifier les positions. Il suffit de définir :

- `pos1` comme 'enhautagauche'
- `pos2` comme 'enhautadroite'
- `pos3` comme 'enbasagauche'
- `pos4` comme 'enbasadroite'

Votre tableau de boucle devrait maintenant ressembler à %FigLoopTable.

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  Le tableau `loop` après que toutes les variables expérimentales ont été définies.
--%

### Étape 5 : Appliquer des opérations de boucle avancées

Bien que vous ayez défini toutes les variables expérimentales, le tableau `loop` n'est pas encore terminé ! Voyons ce qui ne va pas :

__Positions__

`pos1` est toujours en haut à gauche, ce qui signifie que `pic1` (l'objet cible) est toujours présenté en haut à gauche de l'écran ! (En supposant que nous allons mettre en œuvre notre séquence de test de telle sorte que ces positions sont utilisées de cette manière.) Et il en va de même pour `pos2`, `pos3` et `pos4`.

Nous pouvons résoudre cela en mélangeant horizontalement les colonnes `pos[x]`. C'est-à-dire que pour chaque rangée, nous échangeons aléatoirement les valeurs de ces rangées, de sorte que cela :

~~~
pos1        pos2         pos3        pos4
enhautagauche     enhautadroite     enbasagauche  enbasadroite
enhautagauche     enhautadroite     enbasagauche  enbasadroite
…
~~~

Devient (par exemple) ceci :

~~~
pos1        pos2         pos3        pos4
enbasagauche  enhautagauche      enhautadroite    enbasadroite
enhautadroite    enbasadroite  enhautadroite    enbasagauche
…
~~~

Pour ce faire, affichez le script de *block_loop*, et ajoutez la ligne de code suivante à la toute fin du script :

~~~
shuffle_horiz pos1 pos2 pos3 pos4
~~~

Et cliquez sur « Appliquer et fermer ». Si vous cliquez maintenant sur « Aperçu », vous obtiendrez un aperçu de ce que votre tableau de boucle pourrait ressembler si l'expérience était réellement menée. Et vous verrez que les colonnes `pos[x]` sont mélangées horizontalement, ce qui signifie que les images seront présentées dans des positions aléatoires !

__Distracteurs__

Les images distractives sont toujours liées au même objet cible. Par exemple, « basketball01.jpg » se produit toujours avec la cible « apple.jpg ». Mais ce n'est pas ce que nous voulons ! Nous voulons plutôt que la liaison entre les distracteurs et les cibles soit aléatoire et différente pour tous les participants. (Sauf si par hasard une liaison identique se produit pour deux participants.)

Nous pouvons résoudre cela en mélangeant verticalement les colonnes `pic2`, `pic3` et `pic4`. Autrement dit, l'ordre de chacune de ces colonnes doit être mélangé indépendamment. Pour ce faire, affichez à nouveau le script et ajoutez les lignes suivantes à la toute fin du script :

~~~
shuffle pic2
shuffle pic3
shuffle pic4
~~~

Et cliquez sur « Appliquer et fermer ». Si vous cliquez maintenant sur « Aperçu », vous verrez que le tableau `loop` est correctement randomisé !

Pour plus d'informations sur les opérations de boucle avancées, voir :

- %link:manual/structure/loop%

<div class='info-box' markdown='1'>

__Question__

À ce stade, vous pouvez vous demander pourquoi nous ne devons pas également mélanger horizontalement les colonnes « pic2 », « pic3 » et « pic4 ». Mais nous ne le faisons pas ! Savez-vous pourquoi ?

</div>

### Étape 6 : Créez la séquence d'essai

Comme le montre %FigParadigm, notre séquence d'essai est simple et se compose de :

- Point de fixation central (un « sketchpad »)
- Après 1000 ms : Affichage du stimulus (un autre « sketchpad »)
- Après 1000 ms : Lancement de la lecture du son (un « sampler ») pendant que l'affichage du stimulus reste à l'écran
- Après 5000 ms : Fin de l'essai

Pour l'instant, la séquence d'essai est donc purement séquentielle, et nous pourrions la mettre en œuvre en utilisant uniquement une `sequence`, comme nous l'avons fait dans d'autres tutoriels. Cependant, dans l'un des devoirs supplémentaires, nous voulons analyser la position des yeux *pendant* la séquence d'essai ; en d'autres termes, plus tard, nous voudrons faire deux choses en parallèle, et donc nous avons besoin d'un élément `coroutines`. (Même si pour l'instant nous ne ferons rien qui nécessite cela.)

Nous voulons donc avoir la structure suivante :

- *trial_sequence* doit contenir un élément `coroutines` (appelons-le *trial_coroutines*) suivi d'un élément `logger`.
- *trial_coroutines* doit avoir une durée de 7000 ms et contenir trois éléments :
  - Un `sketchpad` pour le point de fixation (appelons-le *fixation_dot*) qui est montré après 0 ms
	- Un `sketchpad` pour l'affichage des stimuli (appelons-le *objects*) qui est montré après 1000 ms
	- Un `sampler` pour le son (appelons-le *spoken_sentence*) qui est montré après 2000 ms

La structure de votre expérience devrait maintenant ressembler à celle de %FigCoroutinesStructure.

%--
figure:
 id: FigCoroutinesStructure
 source: coroutines-structure.png
 caption: |
  La structure de l'expérience après avoir défini la séquence d'essai.
--%

### Étape 7 : Définir les stimuli visuels

__fixation_dot__

Le *fixation_dot* est facile à définir : il suffit de dessiner un point de fixation central sur celui-ci.

Notez que vous n'avez pas besoin de spécifier la durée du `sketchpad`, comme vous devriez normalement le faire ; cela est dû au fait que l'élément fait partie de *trial_coroutines*, et le timing est spécifié par le temps de début et de fin indiqué là-bas.

__objects__

Pour définir les *objects*, créez d'abord un prototype d'affichage, un exemple de ce à quoi un affichage *pourrait* ressembler lors d'un essai particulier. Plus précisément, dessinez un point de fixation central et dessinez une image arbitraire dans chacun des quatre quadrants, comme le montre %FigObjectsPrototype.

Donnez également à chacun des quatre objets un nom : `pic1`, `pic2`, `pic3` et `pic4`. Nous utiliserons ces noms dans les devoirs supplémentaires pour effectuer une analyse des régions d'intérêt (ROI).

%--
figure:
 id: FigObjectsPrototype
 source: objects-prototype.png
 caption: |
  Un prototype d'affichage avec un objet arbitraire dans chacun des quatre quadrants.
--%

Bien sûr, nous ne voulons pas montrer les mêmes objets encore et encore. Plutôt, nous voulons que les variables `pic[x]` spécifient quels objets sont montrés, et que les variables `pos[x]` spécifient où ces objets sont montrés. Commençons par le premier objet : l'objet en haut à gauche, qui dans mon exemple est une pomme.

Consultez le script et trouvez la ligne qui correspond au premier objet. Dans mon exemple, il s'agit de la ligne suivante :
 name=pic1
~~~ .python
draw image center=1 file="apple.jpg" scale=1 show_if=always x=-256 y=-192 z_index=0
~~~

Changez maintenant `file="apple.jpg"` en `file=[pic1]`. Cela permettra de montrer l'image cible telle que spécifiée dans la variable `pic1`, plutôt que toujours la même pomme.

Alors, comment pouvons-nous utiliser `pos1`, qui a des valeurs comme 'topleft', 'bottomright', etc., pour spécifier les coordonnées X et Y de l'image ? Pour ce faire, nous profitons du fait que nous pouvons intégrer des expressions Python dans le script OpenSesame, en utilisant la notation `[=python_expression]` :

- Changez `x=-256` en `x="[=-256 if 'left' in var.pos1 else 256]"` 
- Changez `y=-192` en `y="[=-192 if 'top' in var.pos1 else 192]"` 

Et faites la même chose pour les autres images, jusqu'à ce que le script ressemble à ceci :

~~~ .python
draw fixdot color=noir show_if=toujours style=default x=0 y=0 z_index=0
draw image center=1 file="[pic1]" scale=1 show_if=toujours x="[=-256 if 'left' in var.pos1 else 256]" y="[=-192 if 'top' in var.pos1 else 192]" z_index=0
draw image center=1 file="[pic2]" scale=1 show_if=toujours x="[=-256 if 'left' in var.pos2 else 256]" y="[=-192 if 'top' in var.pos2 else 192]" z_index=0
draw image center=1 file="[pic3]" scale=1 show_if=toujours x="[=-256 if 'left' in var.pos3 else 256]" y="[=-192 if 'top' in var.pos3 else 192]" z_index=0
draw image center=1 file="[pic4]" scale=1 show_if=toujours x="[=-256 if 'left' in var.pos4 else 256]" y="[=-192 if 'top' in var.pos4 else 192]" z_index=0
~~~


<div class='info-box' markdown='1'>

__Essayez-le vous-même : l'expression `if`__

Si vous n'êtes pas familier avec l'expression `if` en Python, qui est légèrement différente de l'instruction `if` traditionnelle, ouvrez la fenêtre de débogage et saisissez la ligne suivante :

~~~ .python
print('Ceci est affiché si True' if True else 'Ceci est affiché si False')
~~~

Que voyez-vous ? Changez maintenant `if True else` en `if False else` et exécutez à nouveau la ligne. Que voyez-vous maintenant ? Vous comprenez la logique ?

</div>


### Étape 8 : Définir le son

Définir le son est facile : ouvrez simplement l'élément *spoken_sentence* et entrez '[sound]' dans la case 'Sound file', indiquant que la variable `sound` spécifie le fichier son.


### Étape 9 : Ajouter un suivi oculaire de base

Le suivi oculaire est effectué avec les plug-ins [PyGaze](%url:manual/eyetracking/pygaze%), qui sont installés par défaut dans OpenSesame. La procédure générale est la suivante :

- Au début de l'expérience, l'eye tracker est *initialisé et calibré* avec l'élément `pygaze_init`. C'est également là que vous indiquez quel eye tracker vous souhaitez utiliser. Pendant, il est pratique de sélectionner le eye tracker Advanced Dummy, qui vous permet de simuler des mouvements oculaires avec la souris.
- Avant chaque essai, une procédure de *correction de dérive* est effectuée avec l'élément `pygaze_drift_correct`. Pendant la correction de dérive, un seul point est affiché à l'écran et le participant le regarde. Cela permet au eye tracker de voir combien d'erreur de dérive il y a dans la mesure de la position des yeux. La façon dont cette erreur est traitée dépend de votre eye tracker et de vos paramètres :
  - L'erreur de dérive est soit utilisée pour un recalibrage en un seul point.
  - Ou un simple contrôle est effectué pour voir si l'erreur de dérive ne dépasse pas une certaine erreur maximale, donnant la possibilité de recalibrer si l'erreur maximale est dépassée.
- Ensuite, toujours avant chaque essai, on demande au eye-tracker de commencer à collecter des données avec l'élément `pygaze_start_recording`. Vous pouvez spécifier un message d'état pour indiquer le début de chaque essai. Il est pratique d'intégrer un numéro d'essai dans ce message d'état (par exemple 'start_trial [count_trial_sequence]').
- À la fin de chaque essai, les données sont envoyées au fichier journal de l'eye-tracker avec l'élément `pygaze_log`. Il est pratique d'activer l'option 'Automatically detect and log all variables'.
- Enfin, à la toute fin de chaque essai, on demande au eye tracker d'arrêter l'enregistrement avec l'élément `pygaze_stop_recording`.

La structure de votre expérience doit maintenant être similaire à celle de %FigEyeTrackingStructure.


%--
figure:
 id: FigEyeTrackingStructure
 source: eye-tracking-structure.png
 caption: |
  La structure de l'expérience après avoir ajouté des éléments PyGaze pour le suivi oculaire.
--%


### Étape 10 : Définir les instructions et l'écran d'au revoir

Nous avons maintenant une expérience fonctionnelle ! Mais nous n'avons pas encore ajouté de contenu aux éléments *instructions* et *goodbye*. Donc, avant de lancer l'expérience, ouvrez ces éléments et ajoutez du texte.

### Étape 11 : Lancer l'expérience !

Félicitations - vous avez mis en œuvre un paradigme de monde visuel ! Il est maintenant temps de tester rapidement votre expérience en cliquant sur le bouton de lecture orange (raccourci : `Ctrl+Shift+W`).


## Travaux supplémentaires

### Supplément 1 : Définir la condition de correspondance sémantique

Jusqu'à présent, nous n'avons mis en œuvre que la condition de correspondance complète, dans laquelle l'objet cible (par exemple, 'pomme') est explicitement mentionné dans la phrase parlée (par exemple, 'au petit déjeuner, la fille a mangé une pomme').

Maintenant, mettez également en œuvre la condition de correspondance sémantique, dans laquelle chaque cible (par exemple, 'pomme') est associée à une phrase parlée sémantiquement liée (par exemple, 'au petit déjeuner, la fille a mangé une banane'). Les stimuli ont été créés de manière à ce qu'il y ait une phrase parlée sémantiquement liée pour chaque objet cible.

De toutes les autres manières, la condition de correspondance sémantique doit être identique à la condition de correspondance complète.

Et n'oubliez pas de créer une variable qui indique la condition !

### Extra 2 : Utiliser des constantes Python pour définir les coordonnées

Actuellement, les coordonnées des objets ont été codées en dur dans le script *objects*, en ce sens que les coordonnées ont été directement saisies dans le script :

~~~ .python
x="[=-256 si 'left' dans var.pos1 else 256]"
~~~

Il est plus élégant de définir les coordonnées (`XLEFT`, `XRIGHT`, `YTOP` et `YBOTTOM`) en tant que constantes dans un `inline_script` au début de l'expérience, puis de se référer à ces constantes dans le script *objects*.

<div class='info-box' markdown='1'>

__Constantes en Python__

En informatique, une *constante* est une variable dont la valeur ne peut pas être modifiée. En Python, vous pouvez toujours modifier des variables, donc les constantes n'existent pas strictement parlant dans le langage. Cependant, si vous avez une variable que vous traitez comme si c'était une constante (c'est-à-dire que vous la définissez une fois et ne changez jamais sa valeur), vous l'indiquez généralement en écrivant le nom de la variable en `MAJUSCULES`.

Ces conventions de nommage sont décrites dans les directives de style PEP-8 de Python :

- <https://www.python.org/dev/peps/pep-0008/>

</div>

### Extra 3 : Analyser en ligne la position des yeux (difficile !)

Dans *trial_coroutines*, vous pouvez indiquer le nom d'une fonction de générateur (voir ci-dessous pour une explication des générateurs). Entrez ici le nom `roi_analysis` et créez également un `inline_script` au début de l'expérience dans lequel nous définissons cette fonction.

Voici une fonction `roi_analysis()` partiellement implémentée. Pouvez-vous terminer la liste des tâches à faire ?

~~~ .python
def roi_analysis():

	# sample_nr sera utilisé pour créer un nom de variable différent pour chacun
	# échantillon de 500 ms
	sample_nr = 0
	# Ce premier rendement indique que le générateur a fini de se préparer
	yield
	# Récupérez le canevas du sketchpad des objets. Nous devons le faire après
	# la déclaration de rendement qui signale la fin de la préparation, parce que nous
	# sommes sûrs que l'objet canevas a été construit (ce qui se produit également)
	# lors de la préparation.
	canvas = items['objects'].canvas
	while True:
		# Nous ne voulons analyser un échantillon de regard que toutes les 500 ms. Cela est fait pour
		# que nous n'ayons pas trop de colonnes dans le fichier journal. Si ce n'est pas
		# le temps d'analyser un échantillon de regard, il suffit de céder et de continuer.
		if not clock.once_in_a_while(ms=500):
			yield # afin que d'autres éléments dans les coroutines puissent fonctionner
			continue
		#
		# TODO :
		#
		# - Obtenir une coordonnée de position des yeux du suivi des yeux
		#   (Astuce : Utiliser eyetracker.sample())
		# - Vérifier quels éléments de sketchpad sont à cette coordonnée (le cas échéant)
		#   (Astuce : utiliser canvas.elements_at())
		# - Si pic1 (l'objet cible) fait partie de ces éléments, définissez
		#   var.on_target_[sample_nr] sur 1, sinon sur 0
		#   (Astuce : utiliser var.set ())
~~~

Voir aussi :

- %link:manual/structure/coroutines%

<div class='info-box' markdown='1'>

__Fonctions de générateur en Python__

En Python, une fonction *générateur* est une fonction avec une déclaration `yield`. Une déclaration `yield` est similaire à une déclaration `return`, en ce sens qu'elle arrête une fonction. Cependant, alors que `return` arrête une fonction de manière permanente, `yield` suspend simplement une fonction, et la fonction peut ensuite reprendre à partir du point `yield`.

</div>

## Télécharger l'expérience

Vous pouvez télécharger l'expérience complète à partir d'ici :

- <https://osf.io/z27rt/>


## Références

Brodeur, M. B., Dionne-Dostie, E., Montreuil, T., Lepage, M., & Op de Beeck, H. P. (2010). La Banque de Stimuli Standardisés (BOSS), un nouvel ensemble de 480 photos normatives d'objets à utiliser comme stimuli visuels dans la recherche cognitive. *PloS ONE*, *5*(5), e10773. doi:10.1371/journal.pone.0010773
{: .reference}

Cooper, R. M. (1974). Le contrôle de la fixation des yeux par le sens du langage parlé: Une nouvelle méthodologie pour l'étude en temps réel de la perception du discours, de la mémoire et du traitement du langage. *Cognitive Psychology*, *6*(1), 84–107. doi:10.1016/0010-0285(74)90005-X
{: .reference}

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: Une boîte à outils open-source et multiplateforme pour la programmation d'expériences de suivi du regard avec un effort minimal. *Behavior Research Methods*, *46*(4), 913–921. doi:10.3758/s13428-013-0422-2
{: .reference}

Huettig, F., Rommers, J., & Meyer, A. S. (2011). Utilisation du paradigme du monde visuel pour étudier le traitement du langage: Un examen et une évaluation critique. *Acta Psychologica*, *137*(2), 151–171. doi:10.1016/j.actpsy.2010.11.003
{: .reference}

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un constructeur d'expériences graphiques open-source pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}