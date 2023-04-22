title: Test de Tri de Cartes du Wisconsin
uptodate: false
hash: 62801ccad4fe18407f604f09c0a01cdc6bafc8cd4b09f38777af7ebaa44f1c71
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

Dans ce tutoriel, vous allez mettre en œuvre le Wisconsin Card Sorting Test (WCST). Vous apprendrez également comment intégrer du code Python dans l'expérience. (Pour la mise en œuvre de cette tâche dans OSWeb, consultez [ce tutoriel](%url:wcst%)).

Dans le WCST, les participants voient quatre cartes stimulus, qui diffèrent selon trois dimensions : couleur (rouge, vert, bleu, jaune), forme (cercle, étoile, triangle, croix) et nombre de formes (une, deux, trois ou quatre). Les participants voient également une seule carte réponse, qui a aussi une couleur, une forme et un nombre.

La tâche du participant consiste à faire correspondre la carte réponse à la bonne carte stimulus, en fonction d'une dimension spécifique (par exemple la couleur), ou *règle de correspondance*. Le participant ne sait pas initialement sur quelle dimension faire correspondre, et sa tâche est de découvrir la règle de correspondance par essais et erreurs.

Pour compliquer les choses, la règle de correspondance change après chaque cinq réponses correctes. Le participant doit donc mettre à jour de manière flexible leur règle de correspondance.

### Étape 1 : Télécharger et démarrer OpenSesame

OpenSesame est disponible pour Windows, Linux et Mac OS. Ce tutoriel est rédigé pour OpenSesame 3.2 ou supérieur.

Lorsque vous démarrez OpenSesame, on vous propose un choix d'expériences modèle, et (le cas échéant) une liste d'expériences récemment ouvertes (voir %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

Le *modèle étendu* offre un bon point de départ pour créer de nombreuses expériences qui utilisent une structure de bloc-essai. Cependant, dans ce tutoriel, nous créerons l'ensemble de l'expérience à partir de zéro, et nous utiliserons le 'modèle par défaut', qui est déjà chargé lorsque OpenSesame est lancé (%FigDefaultTemplate). Fermez simplement les onglets 'Commencer !' et (si affiché) 'Bienvenue !'.

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  La structure du 'Modèle par défaut' vue dans la zone d'aperçu.
--%

### Étape 2 : Ajouter un block_loop et un trial_sequence

Le modèle par défaut commence avec trois éléments : un NOTEPAD appelé *getting_started*, un SKETCHPAD appelé *welcome* et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et *welcome*, alors supprimons-les tout de suite. Pour ce faire, faites un clic droit sur ces éléments et sélectionnez 'Supprimer'. Ne supprimez pas *experiment*, car c'est l'entrée de l'expérience (c'est-à-dire le premier élément appelé lorsque l'expérience est lancée).

Notre expérience aura une structure très simple. Au sommet de la hiérarchie se trouve une LOOP, que nous appellerons *block_loop*. Le *block_loop* est l'endroit où nous définirons nos variables indépendantes. Pour ajouter une LOOP à votre expérience, faites glisser l'icône LOOP depuis la barre d'outils des éléments sur l'élément *experiment* dans la zone d'aperçu.

Un élément LOOP a besoin d'un autre élément pour être exécuté ; généralement, et dans ce cas également, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE depuis la barre d'outils des éléments sur l'élément *new_loop* dans la zone d'aperçu. OpenSesame vous demandera si vous voulez insérer la SEQUENCE dans ou après la LOOP. Sélectionnez 'Insérer dans new_loop'.

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est recommandé de les renommer. Les noms des éléments doivent être constitués de caractères alphanumériques et/ou de tirets bas. Pour renommer un élément, double-cliquez sur l'élément dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un seul essai. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

Enfin, cliquez sur 'Nouvelle expérience' pour ouvrir l'onglet Propriétés générales. Cliquez sur le titre de l'expérience et renommez-le 'Wisconsin Card Sorting Test'.

La zone d'aperçu de notre expérience ressemble maintenant à celle de %FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%


### Étape 3: Importer des images et des fichiers sonores

Pour cette expérience, nous utiliserons des images pour les cartes à jouer. Vous pouvez les télécharger ici :

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton "Afficher le pool de fichiers" dans la barre d'outils principale (ou: Menu → Affichage → Afficher le pool de fichiers). Cela affichera le pool de fichiers, par défaut sur le côté droit de la fenêtre. La façon la plus simple d'ajouter les stimuli au pool de fichiers est de les faire glisser à partir du bureau (ou de l'endroit où vous avez extrait les fichiers) vers le pool de fichiers. Vous pouvez également cliquer sur le bouton '+' dans le pool de fichiers et ajouter des fichiers à l'aide de la boîte de dialogue de sélection de fichiers qui apparaît. Le pool de fichiers sera automatiquement sauvegardé avec votre expérience.

Après avoir ajouté tous les stimuli, votre pool de fichiers ressemblera à celui de %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Le pool de fichiers contenant les stimuli.
--%


### Étape 4: Créer un affichage de cartes statique

Pour commencer, nous créerons un affichage avec quatre cartes stimulis et une carte réponse. Cependant, pour l'instant, les cartes affichées ne dépendront pas des variables ; autrement dit, nous allons créer un affichage *statique*.

Faites glisser un SKETCHPAD dans *trial_sequence* et renommez-le *card_display*. Utilisez l'outil image pour dessiner quatre cartes dans une rangée horizontale près du haut de l'affichage ; il s'agira des cartes stimulis. Dessinez une seule carte près du bas de l'affichage ; ce sera la carte réponse. Ajoutez également du texte pour indiquer au participant ce qu'il doit faire, à savoir appuyer sur `a`, `b`, `c` ou `d` pour indiquer laquelle des cartes stimulis correspond à la carte réponse. Le texte exact, la disposition et les cartes sont à vous de choisir ! Astuces : vous pouvez utiliser l'option *scale* pour ajuster la taille des cartes ; vous pouvez changer la couleur d'arrière-plan dans l'onglet Propriétés Générales, que vous pouvez ouvrir en cliquant sur l'élément de niveau supérieur de l'expérience.

Pour moi, le résultat ressemble à ceci :

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Un SKETCHPAD avec des cartes définies de manière statique.
--%


### Étape 5: Rendre la carte réponse variable

Pour l'instant, nous montrons toujours la même carte réponse (dans l'exemple ci-dessus, un seul triangle bleu). Mais bien sûr, nous voulons afficher une carte réponse différente à chaque essai. Pour cela, nous devons d'abord définir les variables qui déterminent quelle carte réponse nous allons montrer. Nous le ferons dans le *block_loop*.

Ouvrez le *block_loop*. La table LOOP est maintenant vide. Pour déterminer la couleur, la forme et le nombre de la carte réponse, nous pourrions créer manuellement trois colonnes (`response_color`, `response_shape` et `response_number`) et 64 lignées pour toutes les combinaisons possibles de couleurs, formes et nombres. Mais cela représenterait beaucoup de travail. À la place, nous utiliserons l'assistant de conception à facteurs complets, que vous pouvez ouvrir en cliquant sur le bouton "full-factorial design". (Une conception à facteurs complets est une conception dans laquelle toutes les combinaisons possibles de niveaux de variables se produisent.) Dans cet assistant, vous créez une colonne pour chacune des trois variables, et dans les cellules ci-dessous, vous entrez les valeurs possibles pour cette variable (voir %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  L'assistant de conception à facteurs complets vous permet de générer facilement de grandes tables LOOP correspondant à des conceptions à facteurs complets.
--%


Ensuite, cliquez sur le bouton OK. Le *block_loop* contient maintenant toutes les 64 combinaisons de couleurs, nombres et formes (voir %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  Le *block_loop* à la fin de l'étape 5.
--%

Revenez maintenant au *card_display*. Chaque élément d'OpenSesame est défini par un script. Ce script est généré automatiquement par l'interface utilisateur. Parfois, il peut être pratique (ou même nécessaire) de modifier ce script directement. La raison la plus courante de modifier le script d'un élément est d'ajouter des variables au script, ce que nous ferons maintenant !

Pour afficher le script, cliquez sur le bouton "View" et sélectionnez "View script". (Le bouton "View" est le bouton du milieu en haut à droite des contrôles de l'élément.) Cela ouvrira un éditeur de script.

Le script pour *card_display* se compose principalement de commandes `draw`, qui définissent chacune des cinq cartes, ainsi que des divers éléments textuels. Repérez la ligne correspondant à la carte de réponse. Vous pouvez la trouver en regardant la coordonnée Y, qui devrait être positive (c'est-à-dire dans la partie inférieure de l'affichage), ou en regardant le nom du fichier image.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Actuellement, dans mon exemple, le fichier image de la carte de réponse est toujours `"1-blue-triangle.png"`. Mais bien sûr, nous ne voulons pas toujours montrer un seul triangle bleu. Au lieu de cela, nous voulons que le fichier image dépende des variables que nous avons définies dans le *block_loop*. Pour ce faire, remplacez le nombre par `[response_number]`, la couleur par `[response_color]`, et la forme par `[response_shape]`: (Les crochets indiquent que ceux-ci font référence à des noms de variables.)

```
draw image center=1 file="[response_number]-[response_color]-[response_shape].png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Cliquez sur "Apply" pour accepter les modifications apportées au script. La carte de réponse a maintenant été remplacée par une icône en forme de point d'interrogation. C'est parce qu'OpenSesame ne sait pas comment montrer un aperçu d'une image qui a été définie en utilisant des variables. Mais ne vous inquiétez pas : l'image sera affichée lorsque vous exécuterez l'expérience!

### Étape 6 : Rendre les cartes stimulus variables

Les cartes stimulus doivent être sélectionnées plus ou moins au hasard, mais chaque couleur, forme et nombre doit apparaître une seule fois ; c'est-à-dire qu'il ne devrait jamais y avoir deux cartes rouges ou deux cartes avec des triangles. (S'il y en avait, la procédure de correspondance deviendrait ambiguë.) Pour ce faire, nous pouvons utiliser la *mélange horizontal*, qui est une fonctionnalité puissante mais inhabituelle de l'élément LOOP.

- %link:loop%

Tout d'abord, ouvrez le *block_loop* et créez 12 (!) nouvelles colonnes pour définir les cartes stimulus : `color1`, pour la couleur de la première carte, `color2`, `color3`, `color4`, et `shape1` ... `shape4`, et `number1` ... `number4`. Chaque colonne a la même valeur sur chaque ligne (voir %FigLoopTable2).

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  Le *block_loop* lors de l'étape 6.
--%

Mais nous n'avons pas encore terminé ! Actuellement, la première carte stimulus est toujours un cercle rouge unique, la deuxième deux triangles bleus, etc. Pour mélanger cela, nous disons à OpenSesame d'échanger aléatoirement (mélanger horizontalement) les valeurs des quatre variables de couleur, des quatre variables de forme et des quatre variables de nombre. Pour ce faire, ouvrez le script pour le *block_loop*. À l'avant-dernière ligne (juste avant `run trial_sequence`) ajoutez les commandes suivantes:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Cliquez sur "Apply" pour accepter le script. Pour voir si cela a fonctionné, cliquez sur le bouton Preview (Aperçu). Cela montrera un aperçu de comment la table LOOP sera mélangée au hasard pendant l'expérience. Est-ce que ça a l'air bien ?

Revenez maintenant au *card_display* et faites en sorte que l'image de la première carte stimulus dépende de la variable `color1`, `shape1`, et `number1`, et analogiquement pour les autres cartes stimulus. (Si vous ne savez pas comment faire, reprenez l'étape 5.)

### Étape 7 : Déterminer la réponse correcte (pour une règle de correspondance)

Pour l'instant, nous allons supposer que les participants font toujours correspondre la forme. (L'une des missions supplémentaires consiste à améliorer cela.)

Actuellement, la durée de *card_display* est définie sur 'keypress'. Cela signifie que le *card_display* est affiché jusqu'à ce qu'une touche soit pressée, mais cela ne permet pas de contrôler comment cette pression de touche est gérée. Par conséquent, changez la durée à 0 et insérez un KEYBOARD_RESPONSE directement après le *card_display*. Renommez le KEYBOARD_RESPONSE en *press_a* et spécifiez que la réponse correcte est 'a' et que les réponses autorisées sont 'a; b; c; d'.

Mais ce n'est pas suffisant ! En ce moment, il y a un seul élément de réponse qui suppose que la réponse correcte est toujours 'a'. Nous n'avons pas encore précisé *quand* la réponse correcte est 'a', ni examiné les essais pour lesquels la réponse correcte est 'b', 'c' ou 'd'.

Pour ce faire, créez d'abord trois autres éléments KEYBOARD_RESPONSE : *press_b*, *press_c* et *press_d*. Ils sont tous les mêmes, sauf pour la réponse correcte, qui est définie pour chacun d'eux séparément et doit être respectivement 'b', 'c' et 'd'.

Enfin, dans la *trial_sequence*, utilisez des instructions Run If pour décider dans quelle condition chacun des quatre éléments KEYBOARD_RESPONSE doit être exécuté (déterminant ainsi quelle est la réponse correcte). Pour *press_a*, la condition est que `shape1` doit être égale à `response_shape`. Pourquoi ? Eh bien, parce que cela signifie que la forme de la première carte stimulus est égale à la forme de la carte de réponse, et dans ce cas, la réponse correcte est 'a'. Cette condition correspond à l'instruction run-if suivante : `[shape1] = [response_shape]`. Les instructions run-if pour les autres éléments KEYBOARD_RESPONSE sont analogues (voir %FigTrialSequence1).

### Étape 8 : Donner un retour d'information au participant

OpenSesame suit automatiquement si une réponse était correcte ou non, en définissant la variable `correct` à respectivement 1 ou 0. (À condition, bien sûr, que vous ayez spécifié la réponse correcte, ce que nous avons fait à l'étape 7.) Nous pouvons utiliser cela pour donner un retour d'information au participant sur le fait qu'il a répondu correctement ou non.

Pour ce faire, ajoutez deux nouveaux SKETCHPADs à la *trial_sequence* et appelez-les *correct_feedback* et *incorrect_feedback*. Ensuite, spécifiez lequel des deux doit être exécuté en utilisant une instruction run-if (voir %FigTrialSequence2).

Enfin, ajoutez des contenus utiles aux deux SKETCHPADs. Par exemple, pour *correct_feedback*, vous pouvez utiliser un point de fixation vert, et pour *incorrect_feedback*, vous pouvez utiliser un point de fixation rouge, dans les deux cas affiché pendant 500 ms (c'est-à-dire en réglant la durée du SKETCHPAD à 500). Les points colorés sont un moyen discret de fournir des commentaires.

### Étape 9 : Tester l'expérience

Vous avez maintenant créé une implémentation de base (mais incomplète !) du test de tri de cartes du Wisconsin. (Vous compléterez l'implémentation dans le cadre des exercices supplémentaires ci-dessous.)

Pour tester l'expérience, cliquez sur le bouton de lancement rapide (les doubles flèches bleues) pour tester l'expérience sur le bureau (voir %FigRunButtons). Si l'expérience fonctionne comme prévu sur le bureau, cliquez sur le bouton de lancement dans un navigateur (la flèche à l'intérieur d'un cercle vert) pour tester l'expérience dans un navigateur.

## Affectations supplémentaires

### Extra 1 (facile) : Ajouter un logger

OpenSesame ne consigne pas automatiquement les données. Au lieu de cela, vous devez ajouter explicitement un élément `logger` à votre expérience. Dans une expérience basée sur des essais, un `logger` est généralement le dernier élément de la *trial_sequence*, afin qu'il consigne toutes les données collectées pendant l'essai.

En ce moment, notre WCST ne consigne aucune donnée. Il est temps de régler cela !

### Supplément 2 (facile) : Inspecter le fichier de données

*Nécessite d'avoir terminé le Supplément 1*.

Faites un court essai de l'expérience. Inspectez maintenant le fichier de journalisation dans un programme comme Excel, LibreOffice Calc ou JASP. Identifiez les variables pertinentes et réfléchissez à la manière dont vous pourriez analyser les résultats.

__Astuce :__ Réglez la valeur de répétition de la *block_loop* sur 0,1 pour réduire le nombre d'essais lors des tests.

### Supplément 3 (facile) : Ajouter des instructions et un écran d'au revoir

Une bonne expérience est accompagnée d'instructions claires. Et une expérience polie dit au revoir aux participants lorsqu'ils ont terminé. Vous pouvez utiliser un SKETCHPAD pour cela.

### Supplément 4 (moyen): Définir la réponse correcte et la règle de correspondance via du script Python en ligne

Pour inclure des scripts Python dans OpenSesame, vous pouvez utiliser l'élément INLINE_SCRIPT.

Jusqu'à présent, la règle de correspondance est toujours de correspondre par forme. Pour changer cela, ajoutez un élément INLINE_SCRIPT au début de l'expérience et utilisez le script suivant (dans la phase *prepare*) pour définir aléatoirement la variable `matching_rule` sur 'shape', 'number' ou 'color'.

```python
import random

var.matching_rule = random.choice(['shape', 'number', 'color'])
```

Ajoutez maintenant un autre élément INLINE_SCRIPT au début de la *trial_sequence*. Dans la phase *prepare*, ajoutez un script pour définir la variable `correct_response` sur 'a', 'b', 'c' ou 'd'. Pour ce faire, vous avez besoin d'une série d'instructions `if`, qui examinent d'abord la règle de correspondance, puis la forme qui correspond à la forme de la réponse (pour la règle de correspondance par forme) ou la couleur qui correspond à la couleur de la réponse (pour la règle de correspondance par couleur) etc.

Pour commencer, voici une partie de la solution (mais elle doit être complétée !) :

```python
if var.matching_rule == 'shape':
    if var.shape1 == var.response_shape:
        var.correct_response = 'a'
    # Pas encore terminé
# Pas encore terminé

# Imprimons quelques informations dans la fenêtre de débogage
print('matching_rule = {}'.format(var.matching_rule))
print('correct_response = {}'.format(var.correct_response))
```

### Supplément 5 (difficile) : Modifier périodiquement la règle de correspondance

Jusqu'à présent, la règle de correspondance est déterminée aléatoirement au début de l'expérience, mais reste constante tout au long de l'expérience. Dans un véritable WCST, la règle de correspondance change périodiquement, généralement après que le participant a obtenu un nombre fixe de réponses correctes.

Pour cela, vous avez besoin d'un autre INLINE_SCRIPT. Voici quelques conseils pour commencer :

- Utilisez une variable compteur qui s'incrémente de 1 après une réponse correcte et est réinitialisée à 0 après une réponse incorrecte.
- Lors de la modification de la règle de correspondance, assurez-vous qu'elle n'est pas (par coïncidence) réglée à nouveau sur la même règle de correspondance.

### Supplément 6 (vraiment difficile) : Contraindre la carte de réponse

En ce moment, la carte de réponse peut chevaucher une carte de stimulus sur plusieurs dimensions. Par exemple, si l'une des cartes de stimulus est un cercle bleu unique, la carte de réponse peut être deux cercles bleus, chevauchant ainsi à la fois la couleur et la forme. Dans un véritable WCST, la carte de réponse ne doit chevaucher chaque carte de stimulus sur pas plus d'une dimension.

Celle-ci vous appartient. Pas de conseils cette fois !

## Solutions

Vous pouvez télécharger l'expérience complète, y compris les solutions des tâches supplémentaires, ici :

- <https://osf.io/f5er2/>