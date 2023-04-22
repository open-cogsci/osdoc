title: Atelier ESCoP 2019
hash: ba9ac3b22006747d79fa2d0dc0e7ba43a65c01a158eb14725b97a5f7ee352d57
locale: fr
language: French

## À propos de l'atelier

Cet atelier OpenSesame se déroulera lors d'un événement pré-conférence avant *ESCoP 2019*. La participation est gratuite et aucune inscription n'est requise.

L'atelier se compose de deux parties principales. Dans la première partie, correspondant aux étapes de base ci-dessous, nous créons ensemble une expérience complète. Dans la deuxième partie, correspondant aux missions supplémentaires ci-dessous, vous terminez et améliorez l'expérience par vous-même.




### Quand ?

- 25 septembre 2019
- 14h30 - 16h10

### Où ?

- Centre de conférence "La Pirámide de Arona" (Mare Nostrum Resort)
- Av. las Américas
- 38650 Arona
- Santa Cruz de Tenerife
- Espagne

### Plus d'informations

- Site de la conférence : <https://escop2019.webs.ull.es/>



## Les étapes de base



Vous allez mettre en œuvre le Wisconsin Card Sorting Test (WCST) et apprendre comment vous pouvez exécuter ce test en ligne avec OSWeb.

Dans le WCST, les participants voient quatre cartes stimulus, qui diffèrent sur trois dimensions : couleur (rouge, vert, bleu, jaune), forme (cercle, étoile, triangle, croix) et nombre de formes (un, deux, trois ou quatre). Les participants voient aussi une seule carte de réponse, qui a également une couleur, une forme et un nombre.

La tâche du participant est de faire correspondre la carte de réponse à la bonne carte stimulus, en fonction d'une dimension spécifique (par exemple, la couleur) ou d'une *règle de correspondance*. Le participant ne sait pas initialement sur quelle dimension faire correspondre, et sa tâche est de découvrir la règle de correspondance par essais et erreurs.

Pour compliquer les choses, la règle de correspondance change après chaque cinq réponses correctes. Par conséquent, le participant doit mettre à jour de manière flexible sa règle de correspondance.


### Étape 1: Téléchargez et démarrez OpenSesame

OpenSesame est disponible pour Windows, Linux et Mac OS. Ce tutoriel est écrit pour OpenSesame 3.2 et vous pouvez utiliser la version basée sur Python 2.7 (par défaut) ou Python 3.6. Vous pouvez télécharger OpenSesame à partir d'ici:

- %link:download%

Lorsque vous démarrez OpenSesame, il vous est proposé de choisir des expériences modèles et (le cas échéant) une liste des expériences ouvertes récemment (voir %FigStartUp).

Le modèle *Extended template* offre un bon point de départ pour créer de nombreuses expériences qui utilisent une structure de blocs-essais. Cependant, dans ce tutoriel, nous créerons toute l'expérience à partir de zéro et nous utiliserons le 'modèle par défaut', qui est déjà chargé au lancement d'OpenSesame (%FigDefaultTemplate). Fermez simplement les onglets 'Get started!' et (si affiché) 'Welcome!'.

Nous allons maintenant ajouter un LOOP et une SEQUENCE à notre expérience. Le modèle par défaut démarre avec trois éléments : un NOTEPAD appelé *getting_started*, un SKETCHPAD appelé *welcome*, et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et de *welcome*, alors supprimons-les tout de suite. Pour ce faire, faites un clic droit sur ces éléments et sélectionnez 'Supprimer'. Ne supprimez pas *experiment*, car c'est l'entrée de l'expérience (c'est-à-dire le premier élément qui est appelé lorsque l'expérience est lancée).

Notre expérience aura une structure très simple. En haut de la hiérarchie se trouve un LOOP, que nous appellerons *block_loop*. Le *block_loop* est l'endroit où nous définirons nos variables indépendantes. Pour ajouter un LOOP à votre expérience, faites glisser l'icône LOOP de la barre d'outils des éléments sur l'élément *experiment* dans la zone de vue d'ensemble.

Un élément LOOP a besoin d'un autre élément pour fonctionner; généralement, et dans ce cas aussi, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE depuis la barre d'outils des éléments sur l'élément *new_loop* dans la zone d'aperçu. OpenSesame vous demandera si vous souhaitez insérer la SEQUENCE dans ou après la LOOP. Sélectionnez "Insérer dans new_loop".

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est recommandé de les renommer. Les noms des éléments doivent être composés de caractères alphanumériques et/ou de traits de soulignement. Pour renommer un élément, double-cliquez sur l'élément dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un essai unique. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

Enfin, cliquez sur "New experiment" pour ouvrir l'onglet Propriétés générales. Cliquez sur le titre de l'expérience et renommez-le "Wisconsin Card Sorting Test".

La zone d'aperçu de notre expérience ressemble maintenant à %FigBasicStructure.

%--
figure :
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%


### Étape 3 : Importer des images et des fichiers audio

Pour cette expérience, nous utiliserons des images pour les cartes à jouer. Vous pouvez les télécharger ici :

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton "Afficher le pool de fichiers" dans la barre d'outils principale (ou : Menu → Affichage → Afficher le pool de fichiers). Cela affichera le pool de fichiers, par défaut sur le côté droit de la fenêtre. La manière la plus simple d'ajouter les stimuli au pool de fichiers est de les faire glisser depuis le bureau (ou depuis l'endroit où vous avez extrait les fichiers) dans le pool de fichiers. Sinon, vous pouvez cliquer sur le bouton "+" dans le pool de fichiers et ajouter des fichiers en utilisant la boîte de dialogue de sélection de fichiers qui apparaît. Le pool de fichiers est automatiquement sauvegardé avec votre expérience.

Après avoir ajouté tous les stimuli, votre pool de fichiers ressemble à %FigFilePool.

%--
figure :
 id: FigFilePool
 source: file-pool.png
 caption: |
  Le pool de fichiers contenant les stimuli.
--%


### Étape 4 : Créer un affichage de carte statique

Pour commencer, nous créerons un affichage avec quatre cartes stimuli et une carte réponse. Cependant, les cartes affichées ne dépendront pas, pour l'instant, des variables ; autrement dit, nous créerons un affichage *statique*.

Faites glisser un SKETCHPAD dans *trial_sequence* et renommez-le en *card_display*. Utilisez l'outil d'image pour dessiner quatre cartes dans une rangée horizontale près du haut de l'affichage; ce seront les cartes stimuli. Dessinez une seule carte près du bas de l'affichage; ce sera la carte réponse. Ajoutez également du texte pour indiquer au participant ce qu'il doit faire, à savoir appuyer sur `a`, `b`, `c` ou `d` pour indiquer laquelle des cartes stimuli correspond à la carte réponse. Le texte exact, la disposition et les cartes dépendent de vous ! Astuces : vous pouvez utiliser l'option *scale* pour ajuster la taille des cartes ; vous pouvez changer la couleur d'arrière-plan dans l'onglet Propriétés générales, que vous pouvez ouvrir en cliquant sur l'élément de niveau supérieur de l'expérience.

Pour moi, le résultat ressemble à ça:

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Un SKETCHPAD avec des cartes définies statiquement.
--%


### Étape 5 : Rendre la carte de réponse variable

Pour l'instant, nous montrons toujours la même carte réponse (dans l'exemple ci-dessus, un seul triangle bleu). Mais bien sûr, nous voulons montrer une carte réponse différente à chaque essai. Pour ce faire, nous devons d'abord définir les variables qui déterminent quelle carte réponse nous allons montrer. Nous le ferons dans le *block_loop*.

Ouvrez la *block_loop*. La table LOOP est maintenant vide. Pour déterminer la couleur, la forme et le nombre de la carte réponse, nous pourrions créer manuellement trois colonnes (`response_color`, `response_shape` et `response_number`) et 64 lignes pour toutes les combinaisons possibles de couleurs, formes et nombres. Mais cela représenterait beaucoup de travail. Au lieu de cela, nous allons utiliser l'assistant de planification factorielle complète, que vous pouvez ouvrir en cliquant sur le bouton "Plan factoriel complet". (Un plan factoriel complet est un plan dans lequel toutes les combinaisons possibles de niveaux de variables se produisent.) Dans cet assistant, vous créez une colonne pour chacune des trois variables, et dans les cellules du dessous, entrez les valeurs possibles pour cette variable (voir %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  L'assistant de planification factorielle complète vous permet de générer facilement de grandes tables LOOP correspondant à des plans factoriels complets.
--%

Ensuite, cliquez sur le bouton OK. La *block_loop* contient maintenant les 64 combinaisons de couleurs, nombres et formes (voir %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  La *block_loop* à la fin de l'étape 5.
--%

Revenez maintenant à la *card_display*. Chaque élément dans OpenSesame est défini par un script. Ce script est généré automatiquement par l'interface utilisateur. Parfois, il peut être pratique (ou même nécessaire) d'éditer directement ce script. La raison la plus courante pour éditer le script d'un élément est d'ajouter des variables au script, ce que nous allons faire maintenant !

Pour afficher le script, cliquez sur le bouton "Afficher" et sélectionnez "Afficher le script". (Le bouton Afficher se trouve au milieu des commandes d'élément en haut à droite.) Cela ouvrira un éditeur de script.

Le script pour *card_display* se compose principalement de commandes `draw`, qui définissent chacune des cinq cartes, ainsi que des différents éléments de texte. Repérez la ligne correspondant à la carte réponse. Vous pouvez la trouver en regardant l'axe des Y, qui doit être positif (c'est-à-dire dans la partie inférieure de l'affichage) ou en regardant le nom du fichier image.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

En ce moment, dans mon exemple, le fichier image pour la carte réponse est toujours `"1-blue-triangle.png"`. Mais bien sûr, nous ne voulons pas toujours montrer un seul triangle bleu. Au lieu de cela, nous voulons avoir le fichier image en fonction des variables que nous avons définies dans la *block_loop*. Pour ce faire, remplacez le nombre par `[response_number]`, la couleur par `[response_color]` et la forme par `[response_shape]`: (Les crochets indiquent qu'il s'agit des noms de variables.)

```
draw image center=1 file="[response_number]-[response_color]-[response_shape].png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Cliquez sur Appliquer pour accepter les modifications apportées au script. La carte réponse a maintenant été remplacée par une icône en forme de point d'interrogation. Cela est dû au fait qu'OpenSesame ne sait pas comment afficher un aperçu d'une image qui a été définie à l'aide de variables. Mais ne vous inquiétez pas : l'image sera affichée lorsque vous exécuterez l'expérience !

### Étape 6: Rendre les cartes stimulus variables

Les cartes stimulus doivent être sélectionnées de manière plus ou moins aléatoire, mais chaque couleur, forme et nombre ne doit apparaître qu'une seule fois ; c'est-à-dire qu'il ne devrait jamais y avoir deux cartes rouges ou deux cartes avec des triangles. (S'il y en avait, la procédure de correspondance deviendrait ambiguë.) Pour y parvenir, nous pouvons utiliser le *mélange horizontal*, qui est une fonctionnalité puissante mais inhabituelle de l'élément LOOP.

- %link:loop%

D'abord, ouvrez le *block_loop* et créez 12 (!) nouvelles colonnes pour définir les cartes stimulus : `color1`, pour la couleur de la première carte, `color2`, `color3`, `color4`, et `shape1` ... `shape4`, et `number1` ... `number4`. Chaque colonne a la même valeur sur chaque ligne (voir %FigLoopTable2).

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  La *block_loop* pendant l'étape 6.
--%

Mais nous n'avons pas encore terminé! En ce moment, la première carte stimulus est toujours un seul cercle rouge, la seconde deux triangles bleus, etc. Pour randomiser cela, nous disons à OpenSesame de permuter aléatoirement (mélanger horizontalement) les valeurs des quatre variables de couleur, des quatre variables de forme et des quatre variables de nombre. Pour ce faire, ouvrez le script pour la *block_loop*. À l'avant-dernière ligne (juste avant `run trial_sequence`), ajoutez les commandes suivantes:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Cliquez sur Appliquer pour accepter le script. Pour voir si cela a fonctionné, cliquez sur le bouton Aperçu. Cela montrera un aperçu de la manière dont le tableau LOOP sera randomisé pendant l'expérience. Est-ce que ça a l'air bien?

Revenez maintenant au *card_display* et faites dépendre l'image de la première carte stimulus des variables `color1`, `shape1` et `number1`, et analogiquement pour les autres cartes stimulus. (Si vous n'êtes pas sûr de la manière de procéder, reportez-vous à l'étape 5.)


### Étape 7: déterminer la réponse correcte (pour une règle de correspondance)


Pour l'instant, nous allons supposer que les participants correspondent toujours par forme. (L'une des missions supplémentaires consiste à améliorer cela.)

En ce moment, la durée du *card_display* est définie sur 'keypress'. Cela signifie que le *card_display* est affiché jusqu'à ce qu'une touche soit enfoncée, mais cela ne fournit aucun contrôle sur la manière dont cette pression de touche est gérée. Par conséquent, changez la durée à 0 et insérez un KEYBOARD_RESPONSE directement après le *card_display*. Renommez la KEYBOARD_RESPONSE en *press_a* et spécifiez que la réponse correcte est 'a' et que les réponses autorisées sont 'a;b;c;d'.


%--
figure:
 id: FigPressA
 source: press-a.png
 légende: |
  L'un des éléments de KEYBOARD_RESPONSE définis à l'étape 7.
--%


Mais cela ne suffit pas! Pour l'instant, il y a un seul élément de réponse qui suppose que la réponse correcte est toujours 'a'. Nous n'avons pas encore spécifié *quand* la réponse correcte est 'a', et nous n'avons pas non plus examiné les essais pour lesquels la réponse correcte est 'b', 'c' ou 'd'.

Pour y parvenir, créez d'abord trois autres éléments KEYBOARD_RESPONSE: *press_b*, *press_c* et *press_d*. Ils sont tous les mêmes, sauf pour la réponse correcte, qui est définie pour chacun d'eux séparément et doit être respectivement 'b', 'c' et 'd'.

Enfin, dans le *trial_sequence*, utilisez des instructions Run If pour déterminer dans quelle condition chacun des quatre éléments KEYBOARD_RESPONSE doit être exécuté (décidant ainsi quelle est la réponse correcte). Pour *press_a*, la condition est que `shape1` doit être égal à `response_shape`. Pourquoi? Eh bien, parce que cela signifie que la forme de la première carte stimulus est égale à la forme de la carte réponse, et dans ce cas, la réponse correcte est 'a'. Cette condition correspond à l'instruction run-if suivante: `[shape1] = [response_shape]`. Les instructions run-if pour les autres éléments KEYBOARD_RESPONSE sont analogues (voir %FigTrialSequence1).


%--
figure:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 légende: |
  Le *trial_sequence* à la fin de l'étape 7.
--%


### Étape 8: donner un retour d'information au participant

OpenSesame suit automatiquement si une réponse était correcte ou non, en définissant la variable `correct` à respectivement 1 ou 0. (À condition, bien sûr, que vous ayez spécifié la réponse correcte, comme nous l'avons fait à l'étape 7.) Nous pouvons utiliser cela pour donner un retour d'information au participant sur le fait qu'il a répondu correctement ou non.

Pour ce faire, ajoutez deux nouveaux SKETCHPADs à la *trial_sequence* et appelez-les *correct_feedback* et *incorrect_feedback*. Ensuite, spécifiez lequel des deux doit être exécuté en utilisant une instruction run-if (voir %FigTrialSequence2).


%--
figure:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 légende: |
  Le *trial_sequence* à la fin de l'étape 8.
--%

Enfin, ajoutez du contenu utile aux deux SKETCHPADs. Par exemple, pour *correct_feedback*, vous pouvez utiliser un point de fixation vert, et pour *incorrect_feedback*, vous pourriez utiliser un point de fixation rouge, dans les deux cas montré pendant 500 ms (c'est-à-dire régler la durée du SKETCHPAD sur 500). Les points colorés sont un moyen discret et agréable pour fournir des commentaires.

### Étape 9 : Tester l'expérience

Vous avez maintenant créé une mise en œuvre de base (mais incomplète !) du Wisconsin Card Sorting Test. (Vous complèterez la mise en œuvre dans le cadre des missions supplémentaires ci-dessous.)

Pour tester l'expérience, cliquez sur le bouton quick-run (les deux flèches bleues) pour tester l'expérience sur le bureau (voir %FigRunButtons). Si l'expérience se déroule comme prévu sur le bureau, cliquez sur le bouton run-in-browser (la flèche à l'intérieur d'un cercle vert) pour tester l'expérience dans un navigateur.

## Missions supplémentaires

### Supplémentaire 1 (facile) : Ajouter un enregistreur

OpenSesame ne journalise pas automatiquement les données. À la place, vous devez ajouter explicitement un élément `logger` à votre expérience. Dans une expérience basée sur des essais, un `logger` est généralement le dernier élément du *trial_sequence*, de sorte qu'il consigne toutes les données collectées pendant l'essai.

Actuellement, notre WCST ne consigne aucune donnée. Il est temps de corriger cela !

### Supplémentaire 2 (facile) : Inspecter le fichier de données

*Nécessite d'avoir complété le supplément 1*.

Donnez à l'expérience un court test. Inspectez maintenant le fichier de journal dans un programme comme Excel, LibreOffice Calc ou JASP. Identifiez les variables pertinentes et réfléchissez à la manière d'analyser les résultats.

__Astuce__: Réglez la valeur de répétition du *block_loop* sur 0,1 pour réduire le nombre d'essais lors des tests.

### Supplémentaire 3 (facile) : Ajouter des instructions et un écran d'au revoir

Une bonne expérience est accompagnée d'instructions claires. Et une expérience polie dit au revoir aux participants lorsqu'ils ont terminé. Vous pouvez utiliser un SKETCHPAD pour cela.

__Astuce__: FORM_TEXT_DISPLAY n'est pas compatible avec OSWeb, vous ne devez donc pas l'utiliser pour les instructions si vous voulez exécuter votre expérience en ligne.

### Supplémentaire 4 (moyen): Définir la réponse correcte et la règle de correspondance avec JavaScript

Pour inclure des scripts dans OSWeb, vous pouvez utiliser l'élément INLINE_JAVASCRIPT, qui prend en charge JavaScript. (Mais il n'offre pas actuellement toutes les fonctionnalités offertes par le INLINE_SCRIPT Python habituel !)

Jusqu'à présent, la règle de correspondance est toujours de faire correspondre par forme. Pour changer cela, ajoutez un élément INLINE_JAVASCRIPT au début de l'expérience et utilisez le script suivant (dans la phase *préparer*) pour définir aléatoirement la variable `matching_rule` sur 'forme', 'nombre' ou 'couleur'.

```javascript
function choix(choix) {
    // JavaScript n'a pas de fonction de choix intégrée, nous la définissons
    // ici.
    let index = Math.floor(Math.random() * choix.length)
    return choix[index]
}

// L'objet vars contient toutes les variables expérimentales, comme l'objet var
// dans le script Python en ligne
vars.matching_rule = choix(['shape', 'number', 'color'])
```

Ajoutez maintenant un autre élément INLINE_JAVASCRIPT au début du *trial_sequence*. Dans la phase *préparer*, ajoutez un script pour définir la variable `correct_response` sur 'a', 'b', 'c' ou 'd'. Pour ce faire, vous avez besoin d'une série d'instructions `if` qui regardent d'abord la règle de correspondance, puis examinent quelle forme correspond à la forme de réponse (pour la règle de correspondance de forme) ou quelle couleur correspond à la couleur de réponse (pour la règle de correspondance de couleur) etc.

Pour commencer, voici une partie de la solution (mais elle doit être complétée !):

```javascript
if (vars.matching_rule === 'shape') {
    if (vars.shape1 === vars.response_shape) vars.correct_response = 'a'
    // Pas encore terminé
} // Pas encore terminé

// Affichons quelques informations dans la fenêtre de débogage
console.log('règle_de_correspondance = ' + vars.matching_rule)
console.log('réponse_correcte = ' + vars.correct_response)
```


### Supplément 5 (difficile) : Modifier périodiquement la règle de correspondance

Jusqu'à présent, la règle de correspondance est déterminée au hasard au début de l'expérience, mais reste constante tout au long de l'expérience. Dans un vrai WCST, la règle de correspondance change périodiquement, généralement après que le participant a fait un nombre fixe de réponses correctes.

Pour cela, vous avez besson d'un autre INLINE_JAVASCRIPT. Voici quelques conseils pour commencer :

- Utilisez une variable de compteur qui s'incrémente de 1 après une réponse correcte et qui est réinitialisée à 0 après une réponse incorrecte.
- Lorsque vous changez la règle de correspondance, assurez-vous qu'elle n'est pas (par hasard) réglée à nouveau sur la même règle de correspondance.


### Supplément 6 (vraiment difficile) : Restreindre la carte de réponse

Actuellement, la carte de réponse peut se chevaucher avec une carte de stimulus sur plusieurs dimensions. Par exemple, si l'une des cartes de stimulus est un cercle bleu unique, la carte de réponse peut être composée de deux cercles bleus, se chevauchant ainsi sur la couleur et la forme. Dans un vrai WCST, la carte de réponse ne doit se chevaucher avec chaque carte de stimulus que sur une dimension au maximum.

Celui-ci est à votre charge. Pas de conseils cette fois!


### Supplément 7 (facile) : Exécuter l'expérience en ligne avec JATOS

Notre WCST est compatible avec OSWeb, ce qui signifie que vous pouvez l'exécuter dans un navigateur. Pour tester si cela fonctionne toujours, vous pouvez cliquer sur le bouton run-in-browser dans OpenSesame.

Cependant, pour recueillir des données réelles avec l'expérience dans un navigateur, vous devez importer l'expérience dans JATOS et utiliser JATOS pour générer un lien que vous pouvez distribuer à vos participants. C'est beaucoup plus facile que cela en a l'air ! Pour plus d'informations, consultez :

- %link:manual/osweb/workflow%

## Solutions

Vous pouvez télécharger l'expérience complète, y compris les solutions aux tâches supplémentaires, ici :

- <https://osf.io/f5er2/>