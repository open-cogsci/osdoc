title: Test de tri de cartes du Wisconsin
hash: 4199e2aea0b73c7c2aec2a427017e0f2de9ffa30a72377e12ed75900a1fbc9a1
locale: fr
language: French

[TOC]

## Les étapes de base

%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  Le Wisconsin Card Sorting Test (WCST) est un test neuropsychologique des fonctions exécutives.
--%

Dans ce tutoriel, vous allez mettre en œuvre le Wisconsin Card Sorting Test (WCST). Vous apprendrez également à intégrer du code Python dans l'expérience. (Pour la mise en œuvre de cette tâche dans OSWeb, consultez [ce tutoriel](%url:wcst%)).

Dans le WCST, les participants voient quatre cartes stimulus, qui diffèrent selon trois dimensions : couleur (rouge, vert, bleu, jaune), forme (cercle, étoile, triangle, croix) et nombre de formes (un, deux, trois ou quatre). Les participants voient également une seule carte de réponse, qui a également une couleur, une forme et un nombre.

La tâche du participant est de faire correspondre la carte de réponse à la bonne carte stimulus, en fonction d'une dimension spécifique (par exemple la couleur), ou d'une *règle de correspondance*. Le participant ne sait initialement pas sur quelle dimension faire correspondre, et sa tâche est de découvrir la règle de correspondance par essais et erreurs.

Pour compliquer les choses, la règle de correspondance change après cinq réponses correctes. Par conséquent, le participant doit mettre à jour de manière flexible sa règle de correspondance.

### Étape 1: Téléchargez et démarrez OpenSesame

OpenSesame est disponible pour Windows, Linux et Mac OS. Ce tutoriel est écrit pour OpenSesame 4.0 ou version ultérieure.

Lorsque vous démarrez OpenSesame, on vous propose de choisir parmi les expériences de modèle et (le cas échéant) une liste d'expériences récemment ouvertes (voir %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

Le *modèle étendu* offre un bon point de départ pour créer de nombreuses expériences qui utilisent une structure de bloc-essai. Cependant, dans ce tutoriel, nous créerons l'expérience complète à partir de zéro et nous utiliserons le "modèle par défaut", qui est déjà chargé lorsque OpenSesame est lancé (%FigDefaultTemplate). Fermez simplement les onglets "Commencer!" et "Bienvenue!" (si affiché).

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  La structure du "modèle par défaut" comme on le voit dans la zone d'aperçu.
--%

### Étape 2: Ajouter un block_loop et trial_sequence

Le modèle par défaut commence avec trois éléments: un NOTEPAD appelé *getting_started*, un SKETCHPAD appelé *welcome* et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et *welcome*, alors supprimons-les tout de suite. Pour ce faire, cliquez avec le bouton droit de la souris sur ces éléments et sélectionnez "Supprimer". Ne supprimez pas *experiment*, car il s'agit de l'entrée de l'expérience (c'est-à-dire le premier élément appelé lorsque l'expérience est démarrée).

Notre expérience aura une structure très simple. En haut de la hiérarchie se trouve une boucle LOOP, que nous appellerons *block_loop*. C'est dans *block_loop* que nous définirons nos variables indépendantes. Pour ajouter une boucle LOOP à votre expérience, faites glisser l'icône LOOP de la barre d'outils des éléments sur l'élément *experiment* dans la zone d'aperçu.

Un élément LOOP a besoin d'un autre élément pour fonctionner ; généralement, et dans ce cas également, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE depuis la barre d'outils des éléments sur l'élément *new_loop* dans la zone d'aperçu. OpenSesame vous demandera si vous souhaitez insérer la SEQUENCE dans ou après la LOOP. Sélectionnez "Insérer dans new_loop".

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est recommandé de les renommer. Les noms d'éléments doivent être composés de caractères alphanumériques et/ou de traits de soulignement. Pour renommer un élément, double-cliquez sur l'élément dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un seul essai. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

Enfin, cliquez sur "Nouvelle expérience" pour ouvrir l'onglet des propriétés générales. Cliquez sur le titre de l'expérience et renommez-le en "Wisconsin Card Sorting Test".

La zone d'aperçu de notre expérience ressemble maintenant à %FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%


### Étape 3 : Importer des images et des fichiers sonores

Pour cette expérience, nous utiliserons des images pour les cartes à jouer. Vous pouvez les télécharger ici :

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton "Afficher le pool de fichiers" dans la barre d'outils principale (ou : Menu → Affichage → Afficher le pool de fichiers). Cela affichera le pool de fichiers, par défaut sur le côté droit de la fenêtre. La manière la plus simple d'ajouter les stimuli au pool de fichiers est de les faire glisser depuis le bureau (ou là où vous avez extrait les fichiers) dans le pool de fichiers. Vous pouvez également cliquer sur le bouton '+' dans le pool de fichiers et ajouter des fichiers à l'aide de la boîte de dialogue de sélection de fichiers qui apparaît. Le pool de fichiers sera automatiquement sauvegardé avec votre expérience.

Après avoir ajouté tous les stimuli, votre pool de fichiers ressemble à %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Le pool de fichiers contenant les stimuli.
--%


### Étape 4 : Créer un affichage de cartes statiques

Pour commencer, nous créerons un affichage avec quatre cartes stimulus et une carte réponse. Cependant, les cartes affichées ne dépendront pas, pour l'instant, des variables ; autrement dit, nous créerons un affichage *statique*.

Faites glisser un SKETCHPAD dans *trial_sequence*, et renommez-le en *card_display*. Utilisez l'outil Image pour dessiner quatre cartes dans une rangée horizontale près du haut de l'affichage ; ce seront les cartes stimulus. Dessinez une seule carte près du bas de l'affichage ; ce sera la carte réponse. Ajoutez également du texte pour indiquer au participant ce qu'il doit faire, c'est-à-dire appuyer sur `a`, `b`, `c` ou `d` pour indiquer laquelle des cartes stimulus correspond à la carte réponse. Le texte exact, la disposition et les cartes dépendent de vous ! Astuces : vous pouvez utiliser l'option *scale* pour ajuster la taille des cartes ; vous pouvez modifier la couleur de fond dans l'onglet Propriétés générales, que vous pouvez ouvrir en cliquant sur l'élément de niveau supérieur de l'expérience.

Pour moi, le résultat ressemble à ceci :

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Un SKETCHPAD avec des cartes définies statiquement.
--%


### Étape 5 : Rendre la carte réponse variable

Pour l'instant, nous montrons toujours la même carte réponse (dans l'exemple ci-dessus, un seul triangle bleu). Mais bien sûr, nous voulons montrer une carte réponse différente à chaque essai. Pour ce faire, nous devons d'abord définir les variables qui déterminent quelle carte réponse nous montrerons. Nous ferons cela dans le *block_loop*.

Ouvrez le *block_loop*. La table LOOP est maintenant vide. Pour déterminer la couleur, la forme et le nombre de la carte réponse, nous pourrions créer manuellement trois colonnes (`response_color`, `response_shape` et `response_number`) et 64 lignes pour toutes les combinaisons possibles de couleurs, formes et nombres. Mais cela serait beaucoup de travail. Au lieu de cela, nous utiliserons l'assistant de conception factorielle complète, que vous pouvez ouvrir en cliquant sur le bouton "Conception factorielle complète". (Un plan factoriel complet est un plan dans lequel toutes les combinaisons possibles de niveaux de variable se produisent.) Dans cet assistant, vous créez une colonne pour chacune des trois variables et dans les cellules ci-dessous, entrez les valeurs possibles pour cette variable (voir %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  L'assistant de conception factorielle complète vous permet de générer facilement de grandes tables LOOP correspondant à des plans factoriels complets.
--%


Ensuite, cliquez sur le bouton OK. Le *block_loop* contient maintenant les 64 combinaisons de couleurs, de nombres et de formes (voir %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  Le *block_loop* à la fin de l'étape 5.
--%

Maintenant, retournez au *card_display*. Chaque élément d'OpenSesame est défini par un script. Ce script est généré automatiquement par l'interface utilisateur. Parfois, il peut être pratique (ou même nécessaire) d'éditer ce script directement. La raison la plus courante pour modifier le script d'un élément est d'ajouter des variables au script, ce que nous allons faire maintenant!

Pour voir le script, cliquez sur le bouton "View" et sélectionnez "View script". (Le bouton de visualisation est le bouton du milieu en haut à droite des contrôles d'élément.) Cela ouvrira un éditeur de script.

Le script pour *card_display* se compose principalement de commandes `draw` qui définissent chacune des cinq cartes, ainsi que des différents éléments de texte. Repérez la ligne correspondant à la carte de réponse. Vous pouvez la trouver en regardant la coordonnée Y, qui doit être positive (c'est-à-dire dans la partie inférieure de l'affichage), ou en regardant le nom du fichier image.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Maintenant, dans mon exemple, le fichier image pour la carte de réponse est toujours `"1-blue-triangle.png"`. Mais bien sûr, nous ne voulons pas toujours montrer un seul triangle bleu. Au lieu de cela, nous voulons que le fichier image dépende des variables que nous avons définies dans le *block_loop*. Pour ce faire, remplacez le nombre par `{response_number}`, la couleur par `{response_color}`, et la forme par `{response_shape}`: (Les crochets indiquent que ceux-ci font référence aux noms de variables.)


```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Cliquez sur Apply pour accepter les modifications apportées au script. La carte de réponse a maintenant été remplacée par une icône en forme de point d'interrogation. Cela est dû au fait qu'OpenSesame ne sait pas comment afficher un aperçu d'une image qui a été définie à l'aide de variables. Mais ne vous inquiétez pas: l'image sera affichée lorsque vous exécuterez l'expérience!


### Étape 6: Rendez les cartes stimulus variables

Les cartes stimulus doivent être sélectionnées plus ou moins au hasard, mais chaque couleur, forme et nombre ne doit apparaître qu'une seule fois; c'est-à-dire qu'il ne devrait jamais y avoir deux cartes rouges ou deux cartes avec des triangles. (S'il y en avait, la procédure de correspondance deviendrait ambigüe.) Pour y parvenir, nous pouvons utiliser un *mélange horizontal*, une fonctionnalité puissante mais inhabituelle de l'élément LOOP.

- %link:loop%

Tout d'abord, ouvrez le *block_loop* et créez 12 (!) nouvelles colonnes pour définir les cartes stimulus: `color1`, pour la couleur de la première carte, `color2`, `color3`, `color4`, et `shape1` ... `shape4`, et `number1`... `number4`. Chaque colonne a la même valeur sur chaque ligne (voir %FigLoopTable2).


%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  Le *block_loop* lors de l'étape 6.
--%


Mais nous n'avons pas encore terminé! Pour l'instant, la première carte stimulus est toujours un seul cercle rouge, la deuxième deux triangles bleus, etc. Pour rendre cela aléatoire, nous disons à OpenSesame d'échanger aléatoirement (mélanger horizontalement) les valeurs des quatre variables de couleur, les quatre variables de forme et les quatre variables de nombre. Pour ce faire, ouvrez le script pour le *block_loop*. À l'avant-dernière ligne (juste avant `run trial_sequence`), ajoutez les commandes suivantes:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Cliquez sur Apply pour accepter le script. Pour voir si cela a fonctionné, cliquez sur le bouton Preview. Cela montrera un aperçu de la façon dont le tableau LOOP sera randomisé pendant l'expérience. Est-ce que ça a l'air bien?

Maintenant, retournez au *card_display* et faites en sorte que l'image de la première carte stimulus dépende de la variable `color1`, `shape1` et `number1`, et analogiquement pour les autres cartes stimulus. (Si vous ne savez pas comment faire, revenez à l'étape 5.)


### Étape 7: Déterminer la bonne réponse (pour une règle de correspondance)


Pour l'instant, nous allons supposer que les participants correspondent toujours à la forme. (L'une des missions supplémentaires consiste à améliorer cela.)

Actuellement, la durée de *card_display* est définie sur 'keypress'. Cela signifie que le *card_display* est affiché jusqu'à ce qu'une touche soit enfoncée, mais cela ne permet pas de contrôler comment cette pression de touche est gérée. Par conséquent, changez la durée à 0 et insérez une KEYBOARD_RESPONSE juste après le *card_display*. Renommez la KEYBOARD_RESPONSE en *press_a* et spécifiez que la réponse correcte est 'a' et que les réponses autorisées sont 'a;b;c;d'.

%--
figure:
 id: FigPressA
 source: press-a.png
 caption: |
  One of the KEYBOARD_RESPONSE items defined in step 7.
--%


Mais ce n'est pas suffisant! En ce moment, il y a un seul élément de réponse qui suppose que la réponse correcte est toujours 'a'. Nous n'avons pas encore spécifié *quand* la réponse correcte est 'a', et nous n'avons pas non plus envisagé les essais pour lesquels la réponse correcte est 'b', 'c' ou 'd'.

Pour ce faire, créez d'abord trois autres éléments KEYBOARD_RESPONSE : *press_b*, *press_c* et *press_d*. Ceux-ci sont tous les mêmes, sauf pour la réponse correcte, qui est définie pour chacun d'eux séparément et doit être respectivement 'b', 'c' et 'd'.

Enfin, dans la *trial_sequence*, utilisez des instructions Run If pour décider dans quelle condition chacun des quatre éléments KEYBOARD_RESPONSE doit être exécuté (déterminant ainsi quelle est la réponse correcte). Pour *press_a*, la condition est que `shape1` doit être égal à `response_shape`. Pourquoi? Eh bien, parce que cela signifie que la forme de la première carte stimulus est égale à la forme de la carte réponse, et dans ce cas, la réponse correcte est 'a'. Cette condition correspond à l'instruction run-if suivante : `shape1 = response_shape`. Les instructions run-if pour les autres éléments KEYBOARD_RESPONSE sont analogues (voir %FigTrialSequence1).

%--
figure:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 caption: |
  The *trial_sequence* at the end of step 7.
--%


### Étape 8 : Donner un retour d'information au participant

OpenSesame suit automatiquement si une réponse était correcte ou non, en définissant la variable `correct` à respectivement 1 ou 0. (À condition, bien sûr, que vous ayez spécifié la réponse correcte, comme nous l'avons fait à l'étape 7.) Nous pouvons utiliser cela pour donner un retour d'information au participant sur le fait qu'il a répondu correctement ou non.

Pour ce faire, ajoutez deux nouveaux SKETCHPADs à la *trial_sequence* et appelez-les *correct_feedback* et *incorrect_feedback*. Ensuite, spécifiez lequel des deux doit être exécuté en utilisant une instruction run-if (voir %FigTrialSequence2).

%--
figure:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 caption: |
  The *trial_sequence* at the end of step 8.
--%


Enfin, ajoutez un contenu utile aux deux SKETCHPADs. Par exemple, pour *correct_feedback* vous pourriez utiliser un point de fixation vert, et pour *incorrect_feedback* vous pourriez utiliser un point de fixation rouge, dans les deux cas affiché pendant 500 ms (c'est-à-dire en réglant la durée du SKETCHPAD à 500). Les points colorés sont un moyen discret de fournir un retour d'information.


### Étape 9 : Tester l'expérience

Vous avez maintenant créé une mise en œuvre basique (mais incomplète !) du Wisconsin Card Sorting Test. (Vous compléterez la mise en œuvre dans le cadre des missions supplémentaires ci-dessous.)

Pour tester l'expérience, cliquez sur le bouton quick-run (les doubles flèches bleues) ou sur le bouton Run in fullscreen (la flèche verte).


## Missions supplémentaires


### Supplément 1 (facile) : Ajouter un enregistreur

OpenSesame ne journalise pas automatiquement les données. Au lieu de cela, vous devez explicitement ajouter un élément `logger` à votre expérience. Dans une expérience basée sur des essais, un `logger` est généralement le dernier élément de la *trial_sequence*, de sorte qu'il enregistre toutes les données collectées lors de l'essai.

En ce moment, notre WCST ne consigne aucune donnée. Il est temps de corriger ça !


### Supplément 2 (facile) : Inspecter le fichier de données

*Nécessite que vous ayez terminé le supplément 1*.

Faites un court essai de l'expérience. Inspectez maintenant le fichier journal dans un programme comme Excel, LibreOffice Calc ou JASP. Identifiez les variables pertinentes et réfléchissez à la manière dont vous pourriez analyser les résultats.

__Pro-tip :__ Réglez la valeur de répétition de *block_loop* sur 0.1 pour réduire le nombre d'essais lors des tests.

### Bonus 3 (facile) : Ajouter des instructions et un écran d'au revoir

Une bonne expérience est accompagnée d'instructions claires. Et une expérience polie dit au revoir aux participants lorsqu'ils ont terminé. Vous pouvez utiliser un SKETCHPAD pour ce faire.

### Bonus 4 (intermédiaire) : Définir la réponse correcte et la règle de correspondance à travers un script Python en ligne

Pour inclure des scripts Python dans OpenSesame, vous pouvez utiliser l'élément INLINE_SCRIPT.

Jusqu'à présent, la règle de correspondance est toujours de correspondre par forme. Pour changer cela, ajoutez un élément INLINE_SCRIPT au début de l'expérience et utilisez le script suivant (dans la phase *prepare*) pour définir aléatoirement la variable `matching_rule` sur 'shape', 'number' ou 'color'.

```python
import random

matching_rule = random.choice(['shape', 'number', 'color'])
```

Ajoutez maintenant un autre élément INLINE_SCRIPT au début de la *trial_sequence*. Dans la phase *prepare*, ajoutez un script pour définir la variable `correct_response` sur 'a', 'b', 'c' ou 'd'. Pour ce faire, vous avez besoin d'une série d'instructions `if` qui examinent d'abord la règle de correspondance, puis qui cherchent quelle forme correspond à la forme de réponse (pour la règle de correspondance de forme) ou quelle couleur correspond à la couleur de réponse (pour la règle de correspondance de couleur) etc.

Pour commencer, voici une partie de la solution (mais elle doit être complétée !) :

```python
if matching_rule == 'shape':
    if shape1 == response_shape:
        correct_response = 'a'
    # Pas encore terminé
# Pas encore terminé

# Imprimons quelques informations dans la fenêtre de débogage
print('matching_rule = {}'.format(matching_rule))
print('correct_response = {}'.format(correct_response))
```

### Bonus 5 (difficile) : Changer périodiquement la règle de correspondance

Jusqu'à présent, la règle de correspondance est déterminée aléatoirement au début de l'expérience, mais elle reste constante tout au long de l'expérience. Dans un véritable WCST, la règle de correspondance change périodiquement, généralement après que le participant a effectué un nombre fixe de réponses correctes.

Pour mettre en œuvre cela, vous avez besoin d'un autre INLINE_SCRIPT. Voici quelques conseils pour commencer :

- Utilisez une variable de compteur qui s'incrémente de 1 après une réponse correcte, et qui est réinitialisée à 0 après une réponse incorrecte.
- Lors du changement de la règle de correspondance, assurez-vous qu'elle n'est pas (par coïncidence) définie sur la même règle de correspondance à nouveau.

### Bonus 6 (vraiment difficile) : Restreindre la carte de réponse

Actuellement, la carte de réponse peut se chevaucher avec une carte de stimulus sur plusieurs dimensions. Par exemple, si l'une des cartes de stimulus est un cercle bleu unique, la carte de réponse peut être deux cercles bleus, se chevauchant donc à la fois en couleur et en forme. Dans un véritable WCST, la carte de réponse devrait se chevaucher avec chaque carte de stimulus sur au plus une dimension.

Celle-ci vous revient. Pas d'indices cette fois !

## Solutions

Vous pouvez télécharger l'expérience complète, y compris les solutions des missions bonus, ici :

- <https://osf.io/f5er2/>
