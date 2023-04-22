title: Tutoriel sur le clignotement attentionnel (avancé)
uptodate: false
hash: 0839b90e673d98ada96093f196dbf697811876b9b26a432bee00c28dc11aa7f8
locale: fr
language: French

[TOC]

## Difficulté

Ce tutoriel suppose une connaissance de base d'OpenSesame, de la conception expérimentale et de Python. Un tutoriel d'introduction à OpenSesame se trouve ici :

- [/tutorials/step-by-step-tutorial/](/tutorials/step-by-step-tutorial/)

Des liens vers des tutoriels Python d'introduction se trouvent ici :

- [/python/about/](/python/about/)

## L'objectif

Dans ce tutoriel, nous mettrons en œuvre un paradigme de clignotement attentionnel, tel qu'introduit par [Raymond, Shapiro et Arnell (1992)](#références). Nous recréerons presque exactement l'expérience 2 de Raymond et al., avec seulement quelques modifications mineures. Dans cette expérience, le participant voit un flux de lettres, généralement appelé flux RSVP (pour Rapid Serial Visual Presentation). Il y a deux conditions. Dans la condition *expérimentale*, la tâche du participant est double :

- Signaler l'identité de la lettre blanche (toutes les autres lettres étaient noires).
- Indiquer si un 'X' était présent.

Dans la condition de contrôle, la tâche du participant consiste uniquement à ...

- Indiquer si un 'X' était présent.

La lettre blanche est appelée *T1* (ou 'cible'). Le 'X' est appelé *T2* (ou 'sonde'). Le résultat typique est que le T2 est souvent manqué lorsqu'il est présenté 200 à 500 ms après T1, mais seulement lorsque T1 doit être signalé. Ce phénomène est appelé *clignotement attentionnel*, car il semble que l'œil de votre esprit cligne brièvement après avoir vu T1. Mais étonnamment, le T2 n'est généralement pas manqué lorsqu'il suit immédiatement T1. Ceci est appelé *préservation au temps d'attente-1*. Les résultats de Raymond et al. (1992) ressemblaient à ceci :

%--
figure:
 id: FigResults
 source: FigResults.svg
 caption: |
  Précision du T2 en fonction de la position sérielle du T2 par rapport au T1 ('temps d'attente'). Un temps d'attente de 0 signifie que le T1 et le T2 étaient identiques (c'est-à-dire un 'X' blanc). Adapté de Raymond et al. (1992).
--%

## Étape 1 : Télécharger et démarrer OpenSesame

OpenSesame est disponible pour Windows, Linux, Mac OS (expérimental) et Android (runtime uniquement). Ce tutoriel est écrit pour OpenSesame 3.0.X. Vous pouvez télécharger OpenSesame à partir d'ici :

- <http://osdoc.cogsci.nl/>

Lorsque vous démarrez OpenSesame, on vous proposera des expériences modèles et une liste d'expériences récemment ouvertes (%FigStartup).

%--
figure
 id: FigStartup
 source: FigStartup.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

## Étape 2 : Choisir un modèle, une police et des couleurs

Le "modèle étendu" fournit la structure de base d'une expérience typique basée sur des essais avec une phase de pratique et une phase expérimentale. Comme notre expérience correspond très bien à ce modèle, nous allons l'utiliser. Par conséquent, double-cliquez sur "Extended template" pour l'ouvrir.

Dans l'onglet "General tab" qui apparaît maintenant, vous pouvez spécifier les propriétés générales de votre expérience. Pour cette expérience, nous voulons utiliser des lettres noires sur un fond gris. De plus, la taille de police par défaut de 18 est un peu petite, alors changez-la pour 32. Enfin, il est recommandé de donner à votre expérience un nom et une description informatifs. Votre onglet "General tab" ressemble maintenant à %FigGeneralTab.

%--
figure:
 id: FigGeneralTab
 source: FigGeneralTab.png
 caption: |
  L'onglet "General tab" est l'endroit où vous définissez les propriétés générales de votre expérience.
--%

## Étape 3 : Mettre en œuvre la contrebalancement

Dans Raymond et al. (1992), les conditions expérimentales et de contrôle étaient mélangées entre les blocs : les participants faisait d'abord un bloc complet dans une condition, puis un bloc complet dans l'autre condition. L'ordre des conditions était contrebalancé, de sorte que la moitié des participants commençaient par la condition expérimentale, et l'autre moitié par la condition de contrôle.

Commençons par la partie contrebalancement, et utilisons le numéro du participant pour décider quelle condition est testée en premier. Nous devons faire cela dès le début de l'expérience, et nous devons utiliser des scripts Python pour le faire.

Ainsi, faites glisser un INLINE_SCRIPT de la barre d'outils des éléments vers le haut de l'expérience. Changez le nom du nouvel élément en *counterbalance*. Dans la phase de *Préparation* de l'élément *counterbalance*, entrez le script suivant :

~~~ .python
if var.subject_parity == 'even':
	var.condition1 = 'experimental'
	var.condition2 = 'control'
else:
	var.condition1 = 'control'
	var.condition2 = 'experimental'
~~~

Ok, prenons un moment pour comprendre ce qui se passe ici.

La première chose à savoir est que les variables expérimentales sont des propriétés de l'objet `var`. Les variables expérimentales sont des variables que vous avez définies vous-même, par exemple dans un élément LOOP, ainsi que des variables intégrées. Une telle variable expérimentale intégrée est `subject_parity`, qui est automatiquement définie sur 'even' lorsque l'expérience est lancée avec un numéro de sujet pair (0, 2, 4, etc.), et sur 'odd' lorsque le numéro de sujet est impair (1, 3, 5, etc.).

Nous créons ensuite deux nouvelles variables expérimentales `condition1` et `condition2`. En définissant ces propriétés comme `var`, nous les rendons disponibles ailleurs dans OpenSesame, en dehors des éléments INLINE_SCRIPT. Ainsi, cette ligne :

~~~ .python
var.condition1 = 'experimental'
~~~

... crée une variable expérimentale avec le nom `condition1`, et lui donne la valeur 'experimental'. À l'étape 4, nous utiliserons cette variable pour déterminer quelle condition est testée en premier.

En d'autres termes, ce script dit ce qui suit :

- Tous les sujets pairs commencent par la condition expérimentale.
- Tous les sujets impairs commencent par la condition de contrôle.

<div class='info-box' markdown='1'>

### Liens

- [/python/var/](/python/var/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/miscellaneous/counterbalancing/](/miscellaneous/counterbalancing/)

</div>

## Étape 4 : Définir des variables expérimentales qui varient entre les blocs

Comme mentionné ci-dessus, les conditions varient entre les blocs. Pour comprendre comment cela fonctionne dans OpenSesame, il est préférable de commencer par le bas (voir %FigStructure), avec ...

- la *trial_sequence*, qui correspond (comme vous vous en doutez) à un essai unique. Un niveau au-dessus ...
- la *block_loop* correspond à un seul bloc d'essais. C'est donc là que vous définiriez les variables expérimentales qui varient au sein d'un bloc. Un niveau au-dessus ...
- la *block_sequence* correspond à un seul bloc d'essais plus les événements qui se produisent avant et après chaque bloc, tels que les commentaires sur la précision après chaque bloc et les instructions avant chaque bloc. Un niveau au-dessus ...
- la *practice_loop* et *experimental_loop* correspondent à plusieurs blocs d'essais pendant respectivement la phase d'entraînement et la phase non-entraînement (expérimentale). C'est donc là que vous définiriez les variables expérimentales qui varient entre les blocs.

En d'autres termes, nous devons définir nos manipulations entre blocs près du haut de la hiérarchie expérimentale, dans la *practice_loop* et *experimental_loop*.

%--
figure:
 id: FigStructure
 source: FigStructure.png
 caption: |
  Un fragment de la structure expérimentale tel qu'il est présenté dans la zone d'aperçu.
--%

Cliquez sur *practice_loop* pour ouvrir l'élément. Pour l'instant, il n'y a qu'une seule variable, `practice`, qui a la valeur 'yes' pendant un cycle (c'est-à-dire un bloc).

Au travail ! Ajoutez une variable appelée `condition`, changez le nombre de cycles en 2 et changez l'ordre en 'sequentiel'.
Utilisez ensuite les variables précédemment créées `condition1` et `condition2` pour déterminer quelle condition est exécutée en premier et quelle condition est exécutée en deuxième (voir %FigPracticeLoop). Pour indiquer que quelque chose est le nom d'une variable et non une valeur littérale, placez des crochets autour du nom de la variable : '[my_variable]'

%--
figure:
 id: FigPracticeLoop
 source: FigPracticeLoop.png
 caption: |
  L'élément *practice_loop* après l'étape 4.
--%

Faites la même chose pour *experimental_loop*, sauf que la variable `practice` a la valeur 'non'. (La variable `practice` n'a pas de réelle fonction. Elle permet simplement de filtrer facilement tous les essais pratiques lors de l'analyse des données.)

<div class='info-box' markdown='1'>

### Liens

- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/miscellaneous/counterbalancing/](/miscellaneous/counterbalancing/)

</div>

## Étape 5 : Créer des instructions

Comme la tâche diffère entre les blocs, nous devons afficher un écran d'instructions avant chaque bloc. La *block_sequence* est l'endroit pour le faire, car, comme expliqué ci-dessus, elle correspond à un seul bloc d'essais et aux événements qui se produisent avant et après chaque bloc.

Il existe différents éléments que nous pourrions utiliser pour un écran d'instructions, mais nous utiliserons le SKETCHPAD. Insérez deux nouveaux SKETCHPADs en haut de *block_sequence* en les faisant glisser depuis la barre d'outils des éléments. Renommez les SKETCHPADs en *instructions_experimental* et *instructions_control*. Cliquez sur les deux éléments pour ajouter un texte d'instruction, comme indiqué dans %FigInstructions.

%--
figure:
 id: FigInstructions
 source: FigInstructions.png
 caption: |
  Un exemple de texte d'instruction dans l'élément *instructions_experimental*.
--%

Pour l'instant, les deux écrans d'instructions sont affichés avant chaque bloc, ce que nous ne voulons pas. Au lieu de cela, nous voulons montrer seulement l'élément *instructions_experimental* dans la condition expérimentale, et seulement l'élément *instructions_control* dans la condition de contrôle. Nous pouvons le faire avec des instructions conditionnelles ('run if').

Cliquez sur *block_sequence* pour l'ouvrir. Vous verrez une liste de noms d'éléments, tout comme dans la zone de vue d'ensemble, sauf que chaque élément a le texte « always » à côté. Ce sont des instructions run-if, et elles déterminent les conditions d'exécution d'un élément. Double-cliquez sur l'instruction run-if à côté de *instructions_experimental* et ajoutez le texte suivant :

~~~
[condition] = experimental
~~~

Cela signifie que *instructions_experimental* ne sera exécuté que lorsque la variable `condition` a la valeur 'experimental'. Analogiquement, changez l'instruction run-if pour *instructions_control* à :

~~~
[condition] = control
~~~

Votre *block_sequence* devrait maintenant ressembler à %FigBlockSequence.

%--
figure:
 id: FigBlockSequence
 source: FigBlockSequence.png
 caption: |
  L'élément *block_sequence* à la fin de l'étape 5.
--%

<div class='info-box' markdown='1'>

### Liens

- [/usage/sequences-and-loops/](/usage/sequences-and-loops/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)
- [/usage/text/](/usage/text/)

</div>

## Étape 6 : Modifier les retours

Ouvrez *feedback*. Par défaut, dans le modèle étendu, le participant reçoit des commentaires sur la vitesse (`avg_rt`) et la précision (`acc`) après chaque bloc expérimental. Cependant, notre expérience ne nécessite pas de réponses rapides, et nous devrions donc seulement fournir des commentaires sur la précision. Modifiez l'élément *feedback* pour qu'il ressemble à %FigFeedback.

%--
figure:
 id: FigFeedback
 source: FigFeedback.png
 caption: |
  L'élément *block_sequence* à la fin de l'étape 6.
--%

<div class='info-box' markdown='1'>

### Liens

- [/usage/feedback/](/usage/feedback/)
- [/usage/text/](/usage/text/)

</div>

## Étape 7 : Définir les variables expérimentales qui varient au sein d'un bloc

Raymond et al. (1992) font varier la position de T2 par rapport à T1 de 0 à 8, où 0 signifie qu'une lettre est à la fois T1 et T2 (c'est-à-dire un 'X' blanc). Ils ont également des essais où il n'y a pas de T2. Tout cela varie au sein d'un bloc. Il y a différentes façons de coder cela, mais la plus simple est d'utiliser deux variables :

- `lag` indique la position de T2 par rapport à T1. Il a une valeur de 0 à 8, ou aucune valeur s'il n'y a pas de T2.
- `T2_present` est 'y' pour les essais où il y a un T2 et 'n' pour les essais où il n'y a pas de T2. Bien sûr, ceci est redondant, car `T2_present` est 'y' sur tous les essais où `lag` a une valeur. Mais c'est pratique de définir `T2_present`, car nous pouvons l'utiliser plus tard pour spécifier la réponse T2 correcte.

Cliquez sur *block_loop* et créez un tableau de variables comme indiqué dans %FigBlockLoop.

%--
figure:
 id: FigBlockLoop
 source: FigBlockLoop.png
 caption: |
  L'élément *block_loop* après l'étape 7.
--%

<div class='info-box' markdown='1'>

### Liens

- [/usage/sequences-and-loops/](/usage/sequences-and-loops/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Étape 8 : Définir la séquence d'essai

Nous allons utiliser un élément INLINE_SCRIPT pour faire la majeure partie du travail, et donc notre *trial_sequence* est assez simple. Il se compose de :

1. Un SKETCHPAD (appelé *fixation*) pour montrer un point de fixation.
2. Un élément INLINE_SCRIPT (appelé *RSVP*) qui met en œuvre le flux RSVP.
3. Un SKETCHPAD (appelé *ask_T1*) qui demande au participant de signaler T1.
4. Une réponse au clavier (appelée *response_T1*) qui recueille le rapport T1.
5. Un SKETCHPAD (appelé *ask_T2*) qui demande au participant de signaler T2.
6. Une réponse au clavier (appelée *response_T2*) qui recueille le rapport T2.
7. Un LOGGER (appelé *logger*) qui écrit toutes les données dans un fichier journal.

Faites glisser tous les éléments nécessaires de la barre d'outils des éléments dans *trial_sequence*, réorganisez-les si nécessaire et donnez-leur des noms informatifs. Utilisez également des instructions run-if pour collecter une réponse T1 uniquement dans la condition expérimentale. Votre séquence d'essai devrait maintenant ressembler à %FigTrialSequence.

%--
figure:
 id: FigTrialSequence
 source: FigTrialSequence.png
 caption: |
  L'élément *trial_sequence* après l'étape 8.
--%

<div class='info-box' markdown='1'>

### Liens

- [/usage/sequences-and-loops/](/usage/sequences-and-loops/)
- [/usage/variables-and-conditional-statements/](/usage/variables-and-conditional-statements/)

</div>

## Étape 9 : Créer le flux RSVP (phase de préparation)

Maintenant, nous arrivons à la partie amusante mais délicate : la mise en œuvre du flux RSVP. Cliquez sur *RSVP* pour ouvrir l'élément. Vous voyez deux onglets : *Prepare* et *Run*. La règle d'or est d'ajouter tout le code lié à la préparation des stimuli à l'onglet *Prepare*, et tout le code lié à la présentation des stimuli à l'onglet *Run*. Commençons par les choses préparatoires, donc passez à l'onglet *Prepare*.

Tout d'abord, nous devons importer les modules Python que nous prévoyons d'utiliser :

~~~ .python
import random
import string
~~~

Ensuite, nous devons définir plusieurs variables qui déterminent les détails du flux RSVP. Nous les ferons propriétés de l'objet `var`, c'est-à-dire les transformer en variables expérimentales. Ce n'est pas nécessaire, mais cela a l'avantage qu'ils seront automatiquement enregistrés.

~~~ .python
# La couleur de T1
var.T1_color = 'blanc'
# Le temps de présentation de chaque stimulus
# (arrondi à la valeur supérieure compatible avec le taux de rafraîchissement)
var.letter_dur = 10
# L'intervalle entre les stimuli
# (arrondi à la valeur supérieure compatible avec le taux de rafraîchissement)
var.isi = 70
~~~

Ensuite, nous allons créer le flux de lettres. Raymond et al. ont quelques règles :

- Le nombre de lettres qui précèdent T1 est sélectionné aléatoirement entre 7 et 15.
- Le nombre de lettres qui suivent T1 est toujours 8.
- Les lettres sont échantillonnées aléatoirement et sans remplacement à partir de toutes les lettres majuscules sauf 'X' (qui est utilisé pour T2).

Traduisons ces règles en Python:

~~~ .python
# La position de T1 est aléatoire entre 7 et 15. Notez que la première position est
# 0, donc la position indique le nombre de stimuli précédents.
var.T1_pos = random.randint(7, 15)
# Le décalage maximum, c'est-à-dire le nombre de lettres qui suivent T1.
var.max_lag = 8
# La longueur du flux est la position de T1 + le décalage maximum + 1. Nous avons besoin
# d'ajouter 1, car nous comptons à partir de 0, donc la longueur d'une liste est toujours
# 1 de plus que son index maximum.
var.stream_len = var.T1_pos + var.max_lag + 1
# Nous prenons toutes les lettres majuscules, qui ont été prédéfinies dans le module `string`.
# La conversion en `list` crée une liste de caractères.
lettres = list(string.ascii_uppercase)
# Nous supprimons 'X' de cette liste.
lettres.remove('X')
# Choisissez au hasard un nombre `stream_len` de lettres
stim_list = random.sample(lettres, var.stream_len)
~~~

Ok, `stim_list` contient maintenant toutes les lettres qui composent notre flux RSVP lors d'un essai donné, sauf le T2 (s'il est présent). Par conséquent, lors des essais où T2 est présent, nous devons remplacer la lettre à la position T2 par un 'X'.

~~~ .python
if var.T2_present == 'y':
    var.T2_pos = var.T1_pos + var.lag
    stim_list[var.T2_pos] = 'X'
~~~

Nous avons maintenant une variable appelée `stim_list` qui spécifie les lettres de notre flux RSVP. Il s'agit d'une `liste` qui pourrait contenir quelque chose comme : `['M', 'F', 'O', 'P', 'S', 'R', 'Y', 'C', 'U', 'Z', 'G', 'A', 'T', 'E', 'H', 'J', 'V', 'N', 'B', 'K', 'X', 'Q']`. Notez que `stim_list` n'est pas une variable expérimentale, c'est-à-dire qu'elle n'est pas une propriété de l'objet `var`. C'est parce que les variables expérimentales ne peuvent pas être des listes : L'objet `var` transformerait la liste en une chaîne de caractères, et ce n'est pas ce que nous voulons !

La prochaine étape consiste à créer une `liste` d'objets `canvas`, chacun contenant une seule lettre de `stim_list`. Un objet `canvas` correspond à un affichage de stimulus visuel statique, c'est-à-dire à une image de notre flux RSVP. Vous pouvez créer un objet canvas en utilisant la fonction `canvas()`, qui est l'une des fonctions communes d'OpenSesame que vous pouvez appeler sans avoir besoin d'importer quoi que ce soit.

~~~ .python
# Créez une liste vide pour les objets canvas.
liste_canvas_lettre = []
# Parcourez toutes les lettres de `stim_list`. `enumerate()` est une fonction pratique
# qui retourne automatiquement des tuples (index, élément). Dans notre cas, l'index (`i`)
# reflète la position dans le flux RSVP. Cette astuce Python, dans laquelle vous attribuez
# une seule valeur à deux variables, est appelée déballage de tuple.
for i, stim in enumerate(stim_list):
    # Créez un objet `canvas`.
    lettre_canvas = canvas()
    # Si nous sommes à la position de T1, nous changeons la couleur de l'avant-plan, parce que
    # T1 est blanc, alors que la couleur par défaut (spécifiée dans l'onglet Général) est
    # noire.
    if i == var.T1_pos:
        lettre_canvas.set_fgcolor(var.T1_color)
    # Dessinez la lettre !
    lettre_canvas.text(stim)
    # Et ajoutez le canvas à la liste.
    liste_canvas_lettre.append(lettre_canvas)
~~~

Nous devons également créer un `canvas` vierge à afficher pendant l'intervalle inter-stimuli :

~~~ .python
canvas_vide = canvas()
~~~

Enfin, nous définissons l'identité de T1 en tant que variable expérimentale, car elle a été déterminée de manière aléatoire dans le script :

~~~ .python
# Extrait T1 de la liste
var.T1 = stim_list[var.T1_pos]
~~~

Préparation terminée !

<div class='info-box' markdown='1'>

### Liens

- [/python/about/](/python/about/)
- [/python/canvas/](/python/canvas/)
- <https://docs.python.org/2/library/random.html>
- <https://docs.python.org/2/library/string.html>
- <https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences>

</div>

## Étape 10 : Exécuter le flux RSVP (phase d'exécution)

Maintenant, passons à l'onglet *Exécuter* de l'élément `RSVP`. Ici, nous ajoutons le code nécessaire pour afficher tous les objets `canvas` que nous avons créés lors de la phase *Préparer*. Et ce n'est pas si difficile ! Tout ce que nous avons à faire est de :

- Pour chaque canvas de lettre dans la liste letter-canvas
    - Afficher le canvas de lettre
    - Attendre `letter_dur` millisecondes
    - Afficher le canvas vide
    - Attendre `isi` millisecondes

Cela se traduit presque directement en Python :

~~~ .python
for letter_canvas in letter_canvas_list:
    letter_canvas.show()
    clock.sleep(var.letter_dur)
    blank_canvas.show()
    clock.sleep(var.isi)
~~~

Fait !

<div class='info-box' markdown='1'>

### Liens

- [/python/about/](/python/about/)
- [/python/canvas/](/python/canvas/)
- [/python/clock/](/python/clock/)

</div>

## Étape 11 : Créer un point de fixation

Après tout ce codage, il est temps de revenir à quelque chose de plus simple : définir le point de fixation. Cliquez sur *fixation* pour ouvrir l'élément. Changez la durée à 995. Cette valeur sera arrondie à la valeur la plus proche compatible avec le taux de rafraîchissement de votre moniteur, qui est de 1000 ms pour la plupart des taux de rafraîchissement courants. Dessinez un point de fixation au centre, en utilisant l'outil fixation-dot (le point avec le petit trou dedans).

%--
figure:
 id: FigFixation
 source: FigFixation.png
 caption: |
  Le SKETCHPAD *fixation* après l'étape 11.
--%

## Étape 12 : Définir la collecte des réponses

Nous allons collecter les réponses comme suit :

- Demander T1
- Collecter une réponse, qui est une seule pression de touche correspondant à T1. Donc si T1 était 'A', le participant devrait appuyer sur la touche 'a'.
- Demander T2
- Collecter une réponse, qui est 'y' lorsque T2 était présent et 'n' lorsque T2 était absent.

Nous utiliserons le SKETCHPAD *ask_T1* pour demander T1 au participant. Cliquez sur *ask_T1* pour ouvrir l'élément, et ajoutez une ligne de texte, comme "Veuillez taper la lettre blanche". Changez la durée à 0. Cette durée de 0 ms ne signifie pas que le texte est montré seulement pendant 0 ms, mais que l'expérience passe immédiatement à l'élément suivant, qui est *response_T1*.

Ouvrez *response_T1*. La seule chose que nous avons à faire est de définir la réponse correcte. Pour ce faire, nous pouvons utiliser la variable expérimentale `T1` que nous avons définie lors de la préparation du flux RSVP. Par conséquent, entrez '[T1]' dans le champ 'Réponse correcte'.

Ouvrez *ask_T2*, et ajoutez une ligne de texte, comme "Avez-vous vu un X ? (y/n)". Là encore, réglez la durée sur 0, afin que l'expérience passe immédiatement à l'élément suivant, qui est *response_T2*.

Ouvrez *response_T2*. Là encore, nous devons définir la réponse correcte, cette fois en utilisant la variable `T2_present`, que nous avions définie dans le *block_loop*. Par conséquent, ajoutez '[T2_present]' dans le champ 'Réponse correcte'. Il est également utile de limiter les réponses autorisées à 'y' et 'n', afin que les participants n'appuient pas accidentellement sur la mauvaise touche. Vous pouvez le faire en entrant une liste de touches séparées par des points-virgules dans le champ 'Réponses autorisées' (c'est-à-dire 'y;n').

Comment les réponses seront-elles enregistrées ? Chaque élément de réponse définit des variables `response`, `correct` et `response_time`. De plus, pour distinguer les réponses définies par différents éléments, chaque élément de réponse définit ces mêmes variables suivies de `_[item name]`. En d'autres termes, dans cette expérience, les variables de réponse intéressantes seraient `correct_T1_response` et `correct_T2_response`.

<div class='info-box' markdown='1'>

### Liens

- [/usage/collecting-responses/](/usage/collecting-responses/)
- [/usage/text/](/usage/text/)

</div>

## Étape 13 : Spécifier le nombre et la longueur des blocs

Vous avez maintenant une expérience entièrement fonctionnelle, mais une chose doit encore être faite : définir la longueur et le nombre de blocs. Nous utiliserons la structure suivante :

- 1 bloc de pratique de 9 essais dans chaque condition.
- 5 blocs expérimentaux de 36 essais dans chaque condition.

Tout d'abord, ouvrez *block_loop*. La valeur de "Répéter" est actuellement définie sur 1, ce qui signifie que chaque essai est exécuté une fois, donnant une longueur de bloc de 18 essais. Nous voulons spécifier la valeur "Répéter" avec une variable, afin que nous puissions avoir une valeur différente pour les blocs de pratique et expérimentaux. Pour ce faire, nous devons apporter une petite modification au script de *block_loop*. Cliquez sur le bouton "Afficher" en haut à droite de l'onglet (le milieu des trois boutons), et sélectionnez "Afficher le script". Cela masquera les commandes graphiques et montrera le script OpenSesame sous-jacent. Modifier maintenant cette ligne...

~~~
set repeat "1"
~~~

... en ...

~~~
set repeat "[block_repeat]"
~~~

... et cliquez sur "Appliquer et fermer". Cela signifie que la variable `repeat` est maintenant définie en fonction d'une autre variable, `block_repeat`. OpenSesame vous dira qu'il ne connaît plus la longueur du bloc (voir %FigVariableLoop), mais c'est bon : Tant que la variable `block_repeat` est définie, tout fonctionnera bien.

%--
figure:
 id: FigVariableLoop
 source: FigVariableLoop.png
 caption: |
  Si la longueur d'une LOOP est définie de manière variable, OpenSesame vous en informe.
--%

Maintenant, ouvrez *practice_loop*. Ajoutez une variable `block_repeat` et donnez-lui la valeur 0,5. Cela signifie que 0,5 x 18 = 9 cycles de *block_loop* seront exécutés, comme nous le souhaitons.

Maintenant, ouvrez *experimental_loop*. Ajoutez à nouveau une variable `block_repeat` et donnez-lui la valeur 2. Cela signifie que chaque bloc a une longueur de 2 x 18 = 36 essais. Modifiez également le nombre de cycles à 10 et disposez la table de boucle de manière à avoir d'abord cinq blocs de `condition1`, suivis de cinq blocs de `condition2` (voir %FigExperimentalLoop).

%--
figure:
 id: FigExperimentalLoop
 source: FigExperimentalLoop.png
 caption: |
  Si la longueur d'une LOOP est définie de manière variable, OpenSesame vous en informe.
--%

<div class='info-box' markdown='1'>

### Liens

- [/usage/opensesame-script/](/usage/opensesame-script/)

</div>

## Étape 14 : Exécutez l'expérience !

C'est tout. Vous pouvez maintenant lancer l'expérience !

%--
figure:
 id: FigDone
 source: FigDone.svg
 caption: Oui, vous l'avez fait !
--%

## Extra 1 : Vérifiez le minutage (et apprenez un peu de NumPy)

Dans les expériences critiques en termes de temps, vous devez toujours vérifier si le minutage est conforme à vos intentions. Lors de l'utilisation d'objets `canvas`, vous pouvez profiter du fait que la méthode `canvas.show()` renvoie le timestamp du début de l'affichage. Par conséquent, en premier lieu, nous maintenons deux listes : une pour suivre les débuts des lettres-canvas et une autre pour suivre les débuts des canvas vierges.

Pour ce faire, nous avons besoin d'une petite modification du script dans l'onglet *Run* de l'élément *RSVP* :

~~~ .python
l_letter_time = []
l_blank_time = []
for letter_canvas in letter_canvas_list:
    t1 = letter_canvas.show()
    l_letter_time.append(t1)
    clock.sleep(var.letter_dur)
    t2 = blank_canvas.show()
    l_blank_time.append(t2)
    clock.sleep(var.isi)
~~~

Nous avons maintenant deux `list` avec des timestamps: `l_letter_time` et `l_blank_time` À partir de celles-ci, nous voulons déterminer la durée de présentation moyenne d'une lettre, la durée moyenne d'un espace vierge et l'écart-type pour les deux moyennes. Mais comme les `list` ne sont pas idéales pour ce genre de calculs numériques, nous allons les convertir en un autre type d'objet: un `numpy.array`.

~~~ .python
import numpy
a_letter_time = numpy.array(l_letter_time)
a_blank_time = numpy.array(l_blank_time)
~~~

Maintenant, nous pouvons facilement créer un tableau qui contient la durée de présentation de chaque lettre:

~~~ .python
a_letter_dur = a_blank_time - a_letter_time
~~~

Cela crée un nouveau tableau, `a_letter_dur`, dans lequel chaque élément est le résultat de la soustraction de l'élément correspondant dans `a_letter_time` de l'élément correspondant dans `a_blank_time`. Schématiquement :

    a_letter_dur    ->  [  1,  1,  1 ]
    =
    a_blank_time    ->  [ 11, 21, 31 ]
    -
    a_letter_time   ->  [ 10, 20, 30 ]

De même, mais légèrement plus compliqué, nous pouvons créer un nouveau tableau, `a_blank_dur`, dans lequel chaque élément est le résultat de la soustraction de l'élément *i* dans `a_blank_time` de l'élément *i+1* dans `a_letter_time`.

~~~ .python
a_blank_dur = a_letter_time[1:] - a_blank_time[:-1]
~~~

Schématiquement :

    a_blank_dur         ->  [  9,  9 ]
    =
    a_letter_time[1:]   ->  [ 20, 30 ] # Les 10 premiers sont supprimés
    -
    a_blank_time[:-1]   ->  [ 11, 21 ] # Les 31 derniers sont supprimés

La prochaine étape consiste à utiliser les méthodes `array.mean()` et `array.std()` pour obtenir les moyennes et les écarts-types des durées en une seule fois. Pour inspecter ces valeurs, nous les définissons comme des variables expérimentales (c'est-à-dire comme des propriétés de l'objet `var`). De cette façon, elles seront enregistrées et visibles dans l'inspecteur de variables.

~~~ .python
var.mean_letter_dur = a_letter_dur.mean()
var.std_letter_dur = a_letter_dur.std()
var.mean_blank_dur = a_blank_dur.mean()
var.std_blank_dur = a_blank_dur.std()
~~~

Fait!

<div class='info-box' markdown='1'>

### Liens

- [/miscellaneous/timing/](/miscellaneous/timing/)
- <http://wiki.scipy.org/Tentative_NumPy_Tutorial>

</div>

## Supplément 2 : Ajouter des assertions pour vérifier votre expérience

Un proverbe néerlandais dit qu'une erreur est dans un petit coin. (Je soupçonne que selon le proverbe original, l'erreur, plutôt que le coin, était petite, mais peu importe.) Développer des expériences, ou tout type de logiciel, sans bogues est presque impossible. Cependant, vous pouvez vous protéger de nombreux bogues en intégrant des protections dans votre expérience.

Par exemple, notre expérience a deux conditions, définies comme «expérimental» et «contrôle». Mais que se passe-t-il si je fais une faute de frappe avec «experimental» comme «experimentel» dans la boucle expérimentale? L'expérience fonctionnerait toujours, mais elle ne fonctionnerait plus comme prévu. Par conséquent, nous voulons nous assurer que `condition` est soit "expérimental", soit "contrôle", mais rien d'autre. En termes informatiques, nous voulons *affirmer* que c'est le cas. Jetons un coup d'œil à comment nous pouvons le faire.

Tout d'abord, faites glisser un nouvel élément de script en ligne au début de la *séquence d'essai* et renommez-le *assertions*. Ajoutez la ligne suivante à l'onglet *Exécution* :

~~~ .python
assert(var.condition in ['experimental', 'control'])
~~~

Décortiquons cette ligne :

- `var.condition` fait référence à la variable expérimentale `condition`.
- `in ['experimental', 'control']` vérifie si cette variable correspond à l'un des éléments de la liste, c'est-à-dire si elle est "expérimental" ou "contrôle".
- `assert()` déclare qu'il *doit* y avoir une correspondance. Sinon, l'expérience se bloquera (une `AssertionError` sera levée).

En d'autres termes, ce que vous passez à `assert()` doit être `True`, sinon votre expérience se bloquera. Ceci est utile pour les vérifications de bon sens.

Quelques assertions supplémentaires :

~~~ .python
assert(var.T2_present in ['y', 'n'])
assert(var.lag in ['']+list(range(0,9)))
~~~

Et enfin une assertion un peu plus compliquée. Pouvez-vous comprendre ce qu'elle fait ?

~~~ .python
assert((var.lag == '') != (var.T2_present == 'y'))
~~~

<div class='info-box' markdown='1'>

### Liens

- <https://wiki.python.org/moin/UsingAssertionsEffectively>
- Conseils sur la programmation de protection dans Axelrod (2014, doi:10.3389/fpsyg.2014.01435)

</div>

## Supplément 3 : Utiliser directement PsychoPy

OpenSesame est indépendant du backend. Cela signifie que différentes bibliothèques peuvent être utilisées pour contrôler l'affichage, le son, la collecte des réponses, etc. Vous pouvez sélectionner le backend dans l'onglet Général.

Jusqu'à présent, nous avons utilisé l'objet `canvas` de OpenSesame, qui se mappe automatiquement sur les fonctions correctes du backend sélectionné. Par conséquent, vous n'avez pas à vous soucier des détails de chaque backend. Cependant, vous pouvez également utiliser directement les fonctions offertes par un backend spécifique, tel que PsychoPy. Ceci est particulièrement utile si vous souhaitez utiliser des fonctionnalités qui ne sont pas disponibles dans les propres modules d'OpenSesame.

Tout d'abord, pour utiliser PsychoPy, vous devez passer au moteur *psycho*, que vous pouvez faire dans l'onglet 'Propriétés générales' de votre expérience. Maintenant, lorsque vous démarrez l'expérience, OpenSesame initialisera automatiquement PsychoPy, et l'objet `psychopy.visual.Window` sera disponible sous le nom `win` dans les scripts INLINE.

Voyons maintenant comment nous pouvons mettre en œuvre notre flux RSVP dans PsychoPy. (Le script ci-dessous remplace la partie de la phase *Préparer* de *RSVP* dans laquelle nous avons créé `letter_canvas_list`.)

~~~ .python
from psychopy import visual
textstim_list = []
for i, stim in enumerate(stim_list):
    if i == var.T1_pos:
        color = 'white'
    else:
        color = 'black'
    # Tous les stimuli nécessitent un objet psychopy.visual.Window à passer en premier
    # argument. Dans OpenSesame, cet objet est disponible sous le nom `win`.
    textstim = visual.TextStim(win, text=stim, color=color)
    textstim_list.append(textstim)
~~~

La principale différence avec notre script précédent est que nous ne plaçons pas de texte sur un objet `canvas`. Au lieu de cela, le texte est un objet en soi (un `TextStim`), et il a sa propre méthode `draw()` pour le dessiner à l'écran.

Bien sûr, nous devons également mettre à jour la phase *Exécuter* du flux *RSVP*, qui ressemble maintenant à ceci :

~~~ .python
for textstim in textstim_list:
    textstim.draw()
    win.flip()
    clock.sleep(var.letter_dur)
    win.flip()
    clock.sleep(var.isi)
~~~

La principale différence ici est que nous devons appeler plusieurs méthodes pour afficher nos stimuli, au lieu de simplement `canvas.show()`. Tout d'abord, nous devons appeler la méthode `draw()` sur tous les stimuli que nous voulons montrer : `textstim.draw()` Ensuite, nous devons appeler `win.flip()` pour actualiser l'affichage afin que les stimuli deviennent réellement visibles. Si nous appelons `win.flip()` sans appeler la méthode `draw()` au préalable, comme nous le faisons avant l'intervalle inter-stimulus, cela a pour effet d'effacer l'affichage.

C'est tout !

<div class='info-box' markdown='1'>

### Liens

- [/backends/psycho/](/backends/psycho/)
- <http://www.psychopy.org/api/visual.html>

</div>

## Références

Axelrod, V. (2014). Minimiser les erreurs de programmation en neurosciences cognitives. *Frontiers in Psychology: Perception Science*, *5*, 1435. doi:10.3389/fpsyg.2014.01435
{: .reference}

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un générateur d'expériences graphiques open-source pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}

Peirce, J. W. (2007). PsychoPy : Logiciel de psychophysique en Python. Journal of Neuroscience Methods, 162(1-2), 8–13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Raymond, J. E., Shapiro, K. L., & Arnell, K. M. (1992). Suppression temporaire du traitement visuel dans une tâche RSVP: un clignotement attentionnel? *Journal of Experimental Psychology: Human Perception and Performance*, *18*(3), 849–860. doi:10.1037/0096-1523.18.3.849
{: .reference}

[OpenSesame runtime pour Android]: /getting-opensesame/android
[diapositives]: /attachments/neurospin2015-workshop-slides.pdf
[pdf]: /neurospin2015/index.pdf
[tutoriel étape par étape]: /tutorials/step-by-step-tutorial/