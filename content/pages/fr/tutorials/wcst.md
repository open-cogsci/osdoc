title: Test de tri de cartes du Wisconsin
hash: c76af36f9cc3e81cddcf0d468272405a3bebc0c73931400b287f211d586c3db3
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


Dans ce tutoriel, vous allez mettre en œuvre le Wisconsin Card Sorting Test (WCST) et apprendre comment vous pouvez exécuter ce test en ligne avec OSWeb.

Dans le WCST, les participants voient quatre cartes stimulus, qui diffèrent selon trois dimensions : couleur (rouge, vert, bleu, jaune), forme (cercle, étoile, triangle, croix) et nombre de formes (un, deux, trois ou quatre). Les participants voient également une seule carte de réponse, qui a également une couleur, une forme et un nombre.

Le rôle du participant est de faire correspondre la carte de réponse à la bonne carte stimulus, en fonction d'une dimension spécifique (par exemple la couleur), ou *règle de correspondance*. Le participant ne sait pas initialement quelle dimension utiliser pour faire correspondre, et sa tâche est de découvrir la règle de correspondance par essais et erreurs.

Pour compliquer les choses, la règle de correspondance change après chaque série de cinq bonnes réponses. Par conséquent, le participant doit adapter de manière flexible sa règle de correspondance.


### Étape 1: Télécharger et démarrer OpenSesame

OpenSesame est disponible pour Windows, Linux et Mac OS. Ce tutoriel est rédigé pour OpenSesame 4.0 ou une version ultérieure.

Lorsque vous démarrez OpenSesame, on vous propose une sélection d'expériences template, et (le cas échéant) une liste d'expériences ouvertes récemment (voir %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

Le *modèle étendu* offre un bon point de départ pour créer de nombreuses expériences utilisant une structure en blocs-essais. Cependant, dans ce tutoriel, nous créerons l'ensemble de l'expérience à partir de zéro et utiliserons le 'modèle par défaut', qui est déjà chargé lorsque OpenSesame est lancé (%FigDefaultTemplate). Fermez simplement les onglets 'Commencer !' et (le cas échéant) 'Bienvenue !'.

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  La structure du 'modèle par défaut' visible dans la zone d'aperçu.
--%


### Étape 2 : Ajouter un block_loop et un trial_sequence

Le modèle par défaut commence avec trois éléments : un BLOC-NOTES appelé *getting_started*, un SKETCHPAD appelé *welcome* et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et *welcome*, alors supprimons-les tout de suite. Pour ce faire, faites un clic droit sur ces items et sélectionnez 'Supprimer'. Ne supprimez pas *experiment*, car il est l'entrée de l'expérience (c'est-à-dire le premier élément qui est appelé lorsque l'expérience commence).

Notre expérience aura une structure très simple. Au sommet de la hiérarchie se trouve une BOUCLE, que nous appellerons *block_loop*. La *block_loop* est l'endroit où nous définirons nos variables indépendantes. Pour ajouter une BOUCLE à votre expérience, faites glisser l'icône BOUCLE de la barre d'outils des éléments sur l'élément *experiment* dans la zone d'aperçu.

Un élément BOUCLE a besoin d'un autre élément pour s'exécuter ; généralement, et dans ce cas également, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE de la barre d'outils des éléments sur l'élément *new_loop* dans la zone d'aperçu. OpenSesame vous demandera si vous voulez insérer la SEQUENCE dans ou après la BOUCLE. Sélectionnez 'Insérer dans new_loop'.

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est préférable de les renommer. Les noms d'éléments doivent être composés de caractères alphanumériques et/ou d'underscores. Pour renommer un élément, double-cliquez sur l'élément dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un essai unique. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

Enfin, cliquez sur 'Nouvelle expérience' pour ouvrir l'onglet Propriétés générales. Cliquez sur le titre de l'expérience et renommez-le en 'Wisconsin Card Sorting Test'.

La zone d'aperçu de notre expérience ressemble maintenant à celle du %FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%

### Étape 3 : Importer des images et des fichiers audio

Pour cette expérience, nous utiliserons des images pour les cartes à jouer. Vous pouvez les télécharger ici :

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton "Afficher le pool de fichiers" dans la barre d'outils principale (ou : Menu → Affichage → Afficher le pool de fichiers). Cela affichera le pool de fichiers, par défaut sur le côté droit de la fenêtre. La manière la plus simple d'ajouter les stimuli au pool de fichiers est de les glisser-déposer depuis le bureau (ou l'endroit où vous avez extrait les fichiers) dans le pool de fichiers. Sinon, vous pouvez cliquer sur le bouton "+" dans le pool de fichiers et ajouter les fichiers à l'aide de la boîte de dialogue de sélection de fichiers qui apparaît. Le pool de fichiers sera automatiquement enregistré avec votre expérience.

Après avoir ajouté tous les stimuli, votre pool de fichiers ressemble à %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Le pool de fichiers contenant les stimuli.
--%


### Étape 4: Créer une présentation de cartes statique

Pour commencer, nous créerons une présentation avec quatre cartes de stimulus et une carte de réponse. Cependant, pour l'instant, les cartes montrées ne dépendront pas des variables; c'est-à-dire que nous créerons une présentation *statique*.

Faites glisser un SKETCHPAD dans *trial_sequence*, et renommez-le *card_display*. Utilisez l'outil d'image pour dessiner quatre cartes dans une rangée horizontale près du haut de l'écran; ce seront les cartes de stimulus. Dessinez une seule carte près du bas de l'affichage; ce sera la carte de réponse. Ajoutez également du texte pour indiquer au participant ce qu'il doit faire, à savoir appuyer sur `a`, `b`, `c`, ou `d` pour indiquer quelle carte de stimulus correspond à la carte de réponse. Le texte exact, la mise en page et les cartes dépendent de vous ! Conseils : vous pouvez utiliser l'option *scale* pour ajuster la taille des cartes; vous pouvez changer la couleur d'arrière-plan dans l'onglet Propriétés générales, que vous pouvez ouvrir en cliquant sur l'élément de niveau supérieur de l'expérience.

Pour moi, le résultat ressemble à ceci :

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Un SKETCHPAD avec des cartes définies de manière statique.
--%


### Étape 5 : Rendre la carte de réponse variable

Pour le moment, nous montrons toujours la même carte de réponse (dans l'exemple ci-dessus, un seul triangle bleu). Mais bien sûr, nous voulons montrer une carte de réponse différente à chaque essai. Pour ce faire, nous devons d'abord définir les variables qui déterminent quelle carte de réponse nous montrerons. Nous le ferons dans la *block_loop*.

Ouvrez la *block_loop*. La table LOOP est maintenant vide. Pour déterminer la couleur, la forme et le nombre de la carte de réponse, nous pourrions créer manuellement trois colonnes (`response_color`, `response_shape` et `response_number`) et 64 lignes pour toutes les combinaisons possibles de couleurs, formes et nombres. Mais ce serait beaucoup de travail. Au lieu de cela, nous utiliserons l'assistant de conception à facteurs complets, que vous pouvez ouvrir en cliquant sur le bouton "Conception à facteurs complets". (Une conception à facteurs complets est une conception dans laquelle toutes les combinaisons possibles de niveaux de variables se produisent.) Dans cet assistant, vous créez une colonne pour chacune des trois variables, et dans les cellules ci-dessous, entrez les valeurs possibles pour cette variable (voir %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  L'assistant de conception à facteurs complets vous permet de générer facilement de grandes tables LOOP correspondant à des conceptions à facteurs complets.
--%


Ensuite, cliquez sur le bouton OK. La *block_loop* contient maintenant les 64 combinaisons de couleurs, de nombres et de formes (voir %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  La *block_loop* à la fin de l'étape 5.
--%

Maintenant, retournez au *card_display*. Chaque élément dans OpenSesame est défini par un script. Ce script est généré automatiquement par l'interface utilisateur. Parfois, il peut être pratique (ou même nécessaire) de modifier ce script directement. La raison la plus courante de modifier le script d'un élément est d'ajouter des variables au script, ce que nous allons faire maintenant !

Pour afficher le script, cliquez sur le bouton "Afficher" puis sélectionnez "Afficher le script". (Le bouton Afficher est le bouton du milieu en haut à droite des contrôles d'élément.) Cela ouvrira un éditeur de script.

Le script pour *card_display* consiste principalement en des commandes `draw`, qui définissent chacune des cinq cartes, ainsi que les différents éléments de texte. Repérez la ligne qui correspond à la carte de réponse. Vous pouvez la trouver en regardant la coordonnée Y, qui doit être positive (c'est-à-dire dans la partie inférieure de l'affichage), ou en regardant le nom du fichier image.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Dans mon exemple, le fichier image pour la carte de réponse est toujours `"1-blue-triangle.png"`. Mais bien sûr, nous ne voulons pas toujours montrer un seul triangle bleu. Au lieu de cela, nous voulons que le fichier d'image dépende des variables que nous avons définies dans le *block_loop*. Pour ce faire, remplacez le nombre par `{response_number}`, la couleur par `{response_color}`, et la forme par `{response_shape}` : (Les accolades indiquent qu'il s'agit des noms de variables.)


```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Cliquez sur Appliquer pour accepter les modifications apportées au script. La carte de réponse a maintenant été remplacée par une icône de point d'interrogation. Cela est dû au fait qu'OpenSesame ne sait pas comment afficher un aperçu d'une image qui a été définie à l'aide de variables. Mais ne vous inquiétez pas : l'image sera affichée lorsque vous exécuterez l'expérience !

### Étape 6 : Rendre les cartes de stimuli variables

Les cartes de stimuli doivent être sélectionnées plus ou moins au hasard, mais chaque couleur, forme et nombre ne doit apparaître qu'une seule fois ; c'est-à-dire qu'il ne devrait jamais y avoir deux cartes rouges ou deux cartes avec des triangles. (Si c'était le cas, la procédure de correspondance deviendrait ambiguë.) Pour y parvenir, nous pouvons utiliser le *mélange horizontal*, qui est une fonctionnalité puissante mais inhabituelle de l'élément LOOP.

- %link:loop%

Tout d'abord, ouvrez le *block_loop* et créez 12 (!) nouvelles colonnes pour définir les cartes de stimuli : `color1`, pour la couleur de la première carte, `color2`, `color3`, `color4`, et `shape1` ... `shape4`, et `number1` ... `number4`. Chaque colonne a la même valeur sur chaque ligne (voir %FigLoopTable2).


%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  Le *block_loop* lors de l'étape 6.
--%


Mais nous n'avons pas encore fini! En ce moment, la première carte de stimulus est toujours un seul cercle rouge, la deuxième deux triangles bleus, etc. Pour rendre cela aléatoire, nous disons à OpenSesame de permuter aléatoirement (mélanger horizontalement) les valeurs des quatre variables de couleur, les quatre variables de forme et les quatre variables de nombre. Pour ce faire, ouvrez le script pour le *block_loop*. À l'avant-dernière ligne (juste avant `run trial_sequence`) ajoutez les commandes suivantes :

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Cliquez sur Appliquer pour accepter le script. Pour voir si cela a fonctionné, cliquez sur le bouton Aperçu. Cela montrera un aperçu de la manière dont la table LOOP sera mélangée pendant l'expérience. Est-ce que cela semble bon ?

Revenez maintenant au *card_display* et faites en sorte que l'image de la première carte de stimulus dépende de la variable `color1`, `shape1`, et `number1`, et de manière analogue pour les autres cartes de stimulus. (Si vous n'êtes pas sûr de savoir comment faire, revisitez l'étape 5.)

### Étape 7 : Déterminer la réponse correcte (pour une règle de correspondance)

Pour l'instant, nous allons supposer que les participants font toujours correspondre les formes. (L'une des assignations supplémentaires consiste à l'améliorer.)

Actuellement, la durée de *card_display* est définie sur 'keypress'. Cela signifie que le *card_display* est affiché jusqu'à ce qu'une touche soit enfoncée, mais cela ne permet pas de contrôler comment cette touche est gérée. Par conséquent, changez la durée à 0 et insérez une KEYBOARD_RESPONSE directement après le *card_display*. Renommez la KEYBOARD_RESPONSE en *press_a* et spécifiez que la réponse correcte est 'a' et que les réponses autorisées sont 'a; b; c; d'.

Mais ce n'est pas suffisant ! Pour l'instant, il y a un seul élément de réponse qui suppose que la réponse correcte est toujours 'a'. Nous n'avons pas encore précisé *quand* la réponse correcte est 'a', ni n'avons considéré les essais où la réponse correcte est 'b', 'c' ou 'd'.

Pour ce faire, créez d'abord trois autres éléments KEYBOARD_RESPONSE : *press_b*, *press_c* et *press_d*. Ils sont tous les mêmes, sauf pour la réponse correcte, qui est définie pour chacun d'eux séparément et doit être respectivement 'b', 'c' et 'd'.

Enfin, dans la *trial_sequence*, utilisez les instructions Run If pour décider dans quelle condition chacun des quatre éléments KEYBOARD_RESPONSE doit être exécuté (décidant ainsi quelle est la réponse correcte). Pour *press_a*, la condition est que `shape1` doit être égal à `response_shape`. Pourquoi ? Eh bien, parce que cela signifie que la forme de la première carte de stimulus est égale à la forme de la carte de réponse, et dans ce cas, la réponse correcte est 'a'. Cette condition correspond à l'instruction run-if suivante : `shape1 = response_shape`. Les instructions run-if pour les autres éléments KEYBOARD_RESPONSE sont analogues (voir FigTrialSequence1).

### Étape 8 : Donner un retour d'information au participant

OpenSesame suit automatiquement si une réponse était correcte ou non, en définissant la variable `correct` respectivement à 1 ou 0. (À condition, bien sûr, que vous ayez spécifié la réponse correcte, comme nous l'avons fait à l'étape 7.) Nous pouvons utiliser cela pour donner un retour d'information au participant sur la question de savoir s'ils ont répondu correctement ou non.

Pour ce faire, ajoutez deux nouveaux SKETCHPADs à la *trial_sequence* et appelez-les *correct_feedback* et *incorrect_feedback*. Ensuite, spécifiez lequel des deux doit être exécuté en utilisant une instruction run-if (voir FigTrialSequence2).

Enfin, ajoutez du contenu utile aux deux SKETCHPADs. Par exemple, pour *correct_feedback*, vous pouvez utiliser un point de fixation vert, et pour *incorrect_feedback* vous pouvez utiliser un point de fixation rouge, dans les deux cas affichés pendant 500 ms (c'est-à-dire en définissant la durée du SKETCHPAD sur 500). Les points colorés sont un moyen agréable et discret de fournir des informations.

### Étape 9 : Tester l'expérience

Vous avez maintenant créé une implémentation de base (mais incomplète !) du Wisconsin Card Sorting Test. (Vous compléterez l'implémentation dans le cadre des travaux supplémentaires ci-dessous.)

Pour tester l'expérience, cliquez soit sur le bouton quick-run (les doubles flèches bleues) soit sur le bouton Run in fullscreen (la flèche verte).


## Travaux supplémentaires

### Supplémentaire 1 (facile) : Ajouter un enregistreur

OpenSesame n'enregistre pas automatiquement les données. Au lieu de cela, vous devez ajouter explicitement un élément `logger` à votre expérience. Dans une expérience basée sur des essais, un `logger` est généralement le dernier élément de la *trial_sequence*, de sorte qu'il enregistre toutes les données collectées au cours de l'essai.

Pour l'instant, notre WCST ne consigne aucune donnée. Il est temps de régler ça !

### Supplémentaire 2 (facile) : Inspecter le fichier de données

*Nécessite d'avoir terminé Supplémentaire 1*.

Donnez à l'expérience un court test. Inspectez maintenant le fichier journal dans un programme comme Excel, LibreOffice Calc ou JASP. Identifiez les variables pertinentes et réfléchissez à la manière dont vous pourriez analyser les résultats.

__Pro-tip:__ Définissez la valeur de répétition de la *block_loop* sur 0,1 pour réduire le nombre d'essais lors des tests.


### Extra 3 (facile): Ajouter des instructions et un écran d'au revoir

Une bonne expérience vient avec des instructions claires. Et une expérience polie dit au revoir aux participants lorsqu'ils ont terminé. Vous pouvez utiliser un SKETCHPAD ou un FORM_TEXT_DISPLAY pour cela.

### Extra 4 (moyen): Définir la réponse correcte et la règle de correspondance avec JavaScript

Pour inclure des scripts dans OSWeb, vous pouvez utiliser l'objet INLINE_JAVASCRIPT, qui prend en charge JavaScript. (Mais il ne fournit pas actuellement toutes les fonctionnalités offertes par le INLINE_SCRIPT Python habituel !). Voir
[ici](https://osdoc.cogsci.nl/4.0/manual/javascript/about/) pour plus de détails.

Jusqu'à présent, la règle de correspondance est toujours de correspondre par forme. Pour modifier cela, ajoutez un INLINE_JAVASCRIPT au début de l'expérience, et utilisez le script suivant (dans la phase *prepare*) pour définir aléatoirement la variable `matching_rule` sur 'shape', 'number', ou 'color'.

```javascript
function choice(choices) {
    // JavaScript n'a pas de fonction intégrée de choix, donc nous la définissons
    // ici.
    // utilisez let pour introduire une nouvelle variable temporaire
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}


// utilisez var pour introduire une nouvelle variable globale
var matching_rule = choice(['shape', 'number', 'color'])
```

Ajoutez maintenant un autre INLINE_JAVASCRIPT au début de la *trial_sequence*. Dans la phase *prepare*, ajoutez un script pour définir la variable `correct_response` sur 'a', 'b', 'c' ou 'd'. Pour cela, vous avez besoin d'une série d'instructions `if` qui examinent d'abord la règle de correspondance, puis la forme qui correspond à la forme de la réponse (pour la règle de correspondance de forme) ou la couleur qui correspond à la couleur de la réponse (pour la règle de correspondance de couleur), etc.

Pour commencer, voici une partie de la solution (mais elle doit être complétée !):

```javascript
if (matching_rule === 'shape') {
    if (shape1 === response_shape) correct_response = 'a'
    // Pas encore terminé
} // Pas encore terminé

// Imprimons quelques informations dans la fenêtre de débogage
console.log('matching_rule = ' + matching_rule)
console.log('correct_response = ' + correct_response)
```


### Extra 5 (difficile): Changer périodiquement la règle de correspondance

Jusqu'à présent, la règle de correspondance est déterminée aléatoirement au début de l'expérience, mais elle reste constante tout au long de l'expérience. Dans un véritable WCST, la règle de correspondance change périodiquement, généralement après que le participant a effectué un nombre fixe de réponses correctes.

Pour mettre en œuvre cela, vous avez besoin d'un autre INLINE_JAVASCRIPT. Voici quelques conseils pour commencer :

- Utilisez une variable de compteur qui s'incrémente de 1 après une réponse correcte et est réinitialisée à 0 après une réponse incorrecte.
- Lorsque vous changez la règle de correspondance, assurez-vous qu'elle n'est pas (par coïncidence) réglée à nouveau sur la même règle de correspondance.


### Extra 6 (vraiment difficile): Restreindre la carte de réponse

Actuellement, la carte de réponse peut se superposer à une carte de stimulus sur plusieurs dimensions. Par exemple, si l'une des cartes de stimulus est un cercle bleu unique, la carte de réponse peut être deux cercles bleus, se chevauchant ainsi à la fois sur la couleur et la forme. Dans un véritable WCST, la carte de réponse ne doit se chevaucher avec chaque carte de stimulus sur au plus une dimension.

Cela dépend de vous. Pas de conseils cette fois-ci!


### Extra 7 (facile): Exécuter l'expérience en ligne avec JATOS

Notre WCST est compatible avec OSWeb, ce qui signifie que vous pouvez l'exécuter dans un navigateur. Pour tester si cela fonctionne encore, vous pouvez sélectionner le backend OSWeb dans l'onglet des propriétés générales de l'élément d'expérience. Une fois sélectionné, vous pouvez simplement cliquer sur le bouton vert et l'expérience commencera dans votre navigateur par défaut.

Cependant, pour collecter des données réelles pour l'une de vos études, vous voudrez importer l'expérience dans JATOS et utiliser JATOS pour générer un lien que vous pouvez distribuer à vos participants. C'est beaucoup plus facile qu'il n'y paraît ! Pour plus d'informations, voir :

- %link:manual/osweb/workflow%


## Solutions

Vous pouvez télécharger l'expérience complète, y compris les solutions des exercices supplémentaires, ici :

- <https://osf.io/f5er2/>