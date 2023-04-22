title: Tâche d'Association Implicite
uptodate: false
hash: d71135886d1eab5c8ea213f440c31193dc6e9c150ad7be41af10263195d05180
locale: fr
language: French

## Tâche d'association implicite

La tâche d'association implicite mesure la force des associations entre les concepts (par exemple, les jeunes et les personnes âgées) et les évaluations (par exemple, bon et mauvais). L'idée est que donner une réponse est plus facile (et donc *plus rapide*) lorsque des éléments liés partagent la même touche de réponse.

Ici, nous mesurerons l'association entre les jeunes et les vieux, et les bonnes et les mauvaises choses. Nous faisons l'hypothèse que les jeunes participants associent (inconsciemment) les mots positifs aux visages jeunes plutôt qu'aux visages âgés.

## Didacticiel sous forme de screencast

Ce didacticiel est également disponible sous forme de screencast :

%--
video:
 source: youtube
 id: Screencast
 videoid: zd-nxgGOGlE
 width: 640
 height: 360
 caption: |
  Un screencast du didacticiel IAT.
--%

## Hiérarchie expérimentale

Pour tester cette prédiction, les participants réalisent quatre blocs d'essais (%Task)

- __Bloc 1__ - Les participants catégorisent les *mots* comme *POSITIFS* ou *NÉGATIFS*. Les noms de catégories apparaissent en haut à gauche et en haut à droite de l'écran, et les participants appuient sur un bouton avec leur main gauche ou droite pour indiquer à quelle catégorie appartient un mot présenté au centre.
- __Bloc 2__ - Les participants catégorisent les *visages* comme *VIEUX* ou *JEUNES*, à nouveau en effectuant une réponse de la main gauche ou droite.
- __Bloc 3__ - Est une combinaison des blocs 1 et 2. Dans cet exemple, les mots *POSITIFS* et *JEUNES* apparaissent en haut à gauche tandis que les mots *NÉGATIFS* et *VIEUX* apparaissent en haut à droite. Comme nous supposons que les participants (jeunes) ont une attitude plus positive envers les visages jeunes, nous appelons cette correspondance *congruente*.
- __Bloc 4__ - Est de nouveau une combinaison des blocs 1 et 2, mais cette fois la correspondance est *incongruente*.

%--
figure:
 id: Task
 source: IAT-task.png
 caption: |
  Aperçu des quatre blocs de la tâche d'association implicite.
--%

## Prédiction

La prédiction est que les participants ont une préférence pour les jeunes par rapport aux personnes âgées, de sorte qu'il est plus facile de catégoriser les mots lorsque les jeunes et les positifs partagent une touche de réponse, et les vieux et les négatifs partagent une touche de réponse (par rapport au mappage inverse). Cela devrait entraîner des réponses *plus rapides* dans le bloc congruent que dans le bloc incongruent (%Prediction).

%--
figure:
 id: Prediction
 source: prediction.png
 caption: |
  Nous prédisons que les participants trouveront plus facile de catégoriser les mots et les visages si les catégories *POSITIF/ JEUNE* et *NÉGATIF/ VIEUX* sont combinées (par rapport à l'inverse).
--%

## Séquence d'essai

Afin de tester cette prédiction, nous allons créer la séquence d'essai suivante (%TrialSequence) :

- Chaque essai commence par un __point de fixation__ (500 ms)
- Ensuite, les __deux noms de catégorie__ apparaissent en haut à gauche et à droite de l'écran.
- Le __stimulus__ à catégoriser apparaît au centre
- Les participants indiquent par une __touche__ si le stimulus appartient à la catégorie de gauche ou de droite
- Les variables de l'essai en cours sont __enregistrées__

%--
figure:
 id: TrialSequence
 source: trial_sequence.png
 caption: |
  Représentation schématique d'une séquence d'essai typique de la (premier bloc de la) IAT.
--%

## Lancer OpenSesame

Lorsque vous démarrez OpenSesame, vous verrez un onglet "Commencer !", qui vous montre une liste de modèles ainsi que des expériences récemment ouvertes  (%GetStarted). Pour gagner du temps, nous utiliserons le modèle "Extended".

%--
figure:
 id: GetStarted
 source: get-started.png
 caption: |
  Fenêtre de bienvenue d'OpenSesame. Ici, nous utilisons le modèle "Extended".
--%

Après avoir ouvert le modèle étendu, nous enregistrons notre expérience. Pour ce faire, cliquez sur *File* -> *Save* (raccourci : `Ctrl+S`), naviguez jusqu'au dossier approprié et donnez un nom significatif à votre expérience.

## Zone de présentation

La *zone de présentation* montre la structure hiérarchique de notre expérience. Pour simplifier notre structure, nous commençons par supprimer le bloc de pratique. Pour ce faire :

- Cliquez avec le bouton droit sur l'élément appelé *practice loop*
- Cliquez sur "Supprimer" (raccourci: `Suppr`)
- Faites de même pour l'élément *end_of_practice*

La zone d'aperçu de votre expérience devrait maintenant ressembler à ceci :

%--
figure:
 id: Overview
 source: overview.png
 caption: |
  La zone d'aperçu de votre expérience.
--%

## Bloc 1 : catégorisation des mots

### Étape 1 : Modifier la boucle de bloc

Nous commençons par créer le premier bloc du TAI (Bloc 1 dans %Task) dans lequel les participants doivent catégoriser les mots comme étant positifs ou négatifs. Comme nous créerons plusieurs blocs, le nom *block_loop* n'est pas très informatif. Nous le renommons donc :

- Cliquez avec le bouton droit sur l'élément *block_loop*, choisissez renommer (raccourci : `F2`) et appelez-le *words_block_loop*

Ensuite, nous voulons définir les trois variables suivantes dans l'élément *block_loop* :

- __stimulus__ -- Le mot à catégoriser
- __category__ -- La catégorie à laquelle appartient le mot
- __correct_response__ -- La réponse que les participants sont censés donner

Pour créer ces variables :

- Ouvrez l'onglet du *words_block_loop* en cliquant dessus dans la zone d'aperçu
- Vous verrez initialement un tableau vide
- Double-cliquez sur l'en-tête de la première colonne (initialement appelée 'empty_column') et appelez-la 'stimulus'
- Remplissez la première colonne avec six mots positifs et six mots négatifs, un par ligne
- Créez une deuxième colonne avec l'en-tête 'category' et indiquez à quelle catégorie (*POSITIVE* ou *NEGATIVE*) chaque stimulus appartient
- Créez une troisième colonne, appelez-la *correct_response* et indiquez la réponse correcte pour chaque stimulus
- Pour déterminer la règle de réponse, disons que :
    - Le mot *POSITIVE* apparaîtra sur le côté gauche de l'écran, tandis que le mot *NEGATIVE* apparaîtra sur le côté droit
    - Pour indiquer qu'un mot appartient au côté gauche, les participants doivent appuyer sur 'e', tandis que pour le côté droit, ils doivent appuyer sur 'i'.
    
<div class='info-box' markdown='1'>

__Astuce__ -- *correct_response* est une variable intégrée qui permet à OpenSesame de suivre la performance des participants, telle que 'acc' (pour l'exactitude ou le pourcentage correct).

</div>

Le contenu de votre *words_block_loop* devrait maintenant ressembler à ceci :

%--
figure:
 id: Overview
 source: words_block_loop.png
 caption: |
  Le tableau de boucle du premier bloc du TAI contient les trois variables expérimentales et leurs valeurs.
--%

### Étape 2 : Modifier la séquence d'essai

Comme indiqué dans %TrialSequence, lors de chaque essai, nous voulons :

1. Afficher un point de fixation
2. Afficher le stimulus au centre et les deux catégories sur chaque côté supérieur de l'écran
3. Recueillir une réponse par pression de touche
4. Enregistrer les variables dans le fichier de sortie

Ces quatre étapes sont appelées *événements*, et nous allons les réaliser en utilisant des *éléments* dans la *séquence d'essai*. Mais d'abord, comme la séquence d'essai sera légèrement différente pour chaque bloc de l'expérience (voir %Task), renommons-la en *words_trial_sequence*.

Pour les deux premiers événements, nous utiliserons des objets `sketchpad`. Le modèle avancé contient déjà un objet sketchpad. Pour en ajouter un deuxième :

- Prenez un élément `sketchpad` dans la *barre d'outils des éléments*
- Faites-le glisser et déposez-le dans la *words_trial_sequence*

%--
video:
 source: youtube
 id: DragDrop
 videoid: vvJewWTjlts
 width: 640
 height: 360
 caption: |
  Faire glisser et déposer les éléments.
--%

<div class='info-box' markdown='1'>

__Astuce__ -- Pour faire apparaître un élément *après* un autre élément, déposez-le *sur* cet autre élément.

</div>

Par défaut, OpenSesame donne à ses éléments des noms tels que *sketchpad*, *new_sketchpad* et *new_sketchpad_1*. Comme ces noms ne sont pas informatifs, nous renommons les éléments en quelque chose de plus significatif. Pour ce faire :

- Faites un clic droit sur l'élément dans la zone d'aperçu (raccourci : `F2`)
- Choisissez "Renommer"
- Appelez respectivement les deux éléments `sketchpad` *fixation* et *word*

Les deux derniers événements de la séquence d'essai (collecte de la réponse et sauvegarde des données) sont déjà représentés par l'élément `keyboard_response` et l'élément `logger`, respectivement.

Votre zone d'aperçu devrait maintenant ressembler à ceci :



%--
figure:
 id: OverviewWordBlock
 source: overview_words_block.png
 caption: |
  Nouvel aperçu de (la première partie de) l'expérience.
--%


### Étape 3 : Modifier les éléments de la séquence d'essai

#### Fixation

La prochaine étape consiste à ajouter du contenu aux éléments de la séquence d'essai. Nous commençons par le `sketchpad` qui représente le point de fixation au début de chaque essai.

- Ouvrez l'onglet *fixation* en cliquant dessus dans la zone d'aperçu. Parce que nous avons choisi le "Modèle étendu", OpenSesame a déjà créé un point de fixation pour nous. La seule chose que nous devons changer est la durée pendant laquelle le point de fixation restera à l'écran
- Cliquez sur la case "Durée" et changez sa valeur en 500


#### Mot

__Dessinez les noms de catégorie__

Après la disparition du point de fixation, nous voulons afficher les deux noms de catégorie en haut à gauche et à droite de l'écran (voir %TrialSequence). Pour ce faire,

- Ouvrez l'onglet *word* en cliquant dessus dans la zone d'aperçu
- Sélectionnez l'élément `Draw textline` dans la barre d'outils noir et blanc
- Cliquez quelque part dans le quadrant supérieur gauche du sketchpad
- Tapez 'POSITIF'
- Répétez cette procédure pour faire apparaître le mot 'NÉGATIF' sur le côté opposé

__Dessinez le stimulus__

Ensuite, nous voulons montrer le stimulus à catégoriser au centre de l'écran. Le stimulus est _*variable*_. Cela signifie que le mot affiché dépend de la ligne en cours d'exécution dans la boucle *words_block_loop*. Pour indiquer à OpenSesame que la valeur de la variable de mot se trouve dans la boucle de bloc, nous utilisons la *syntaxe des crochets*. Pour ce faire :

- Sélectionnez l'élément `draw textline` du sketchpad
- Cliquez sur le centre de l'écran
- Tapez :

~~~ .python
[stimulus]
~~~


<div class='info-box' markdown='1'>

__Astuce__ -- Le mot que vous tapez entre crochets doit correspondre exactement à l'en-tête de colonne que vous avez créé dans la boucle *word_block_loop*.

</div>

Cette méthode est très pratique, car elle évite de devoir créer des sketchpads séparés pour chaque mot positif et négatif.

__Changer la durée__

Enfin, nous changeons la durée de ce sketchpad à 0. Cela ne signifie pas que le sketchpad actuel sera affiché seulement 0 ms. Au lieu de cela, comme un élément `keyboard_response` suit juste après, il restera à l'écran jusqu'à ce que le participant appuie sur une touche.

Votre sketchpad devrait maintenant ressembler à ceci:

%--
figure:
 id: SketchpadWord
 source: sketchpad-word.png
 caption: |
  L'élément `sketchpad` utilisé pour dessiner les noms de catégorie et le stimulus sur l'affichage.
--%


Il est recommandé d'essayer de lancer votre expérience souvent, afin de pouvoir la déboguer immédiatement. À ce stade, faisons un essai en appuyant sur l'une des trois flèches "exécuter".

<div class='info-box' markdown='1'>

__Astuce__ -- Si vous voulez faire un test rapide de votre expérience, vous n'aurez peut-être pas besoin de lancer tous les éléments d'un bloc donné. Pour raccourcir le nombre d'essais, vous pouvez faire ce qui suit :

- Ouvrez la table de votre boucle de bloc
- Changez la valeur dans la case 'Répéter' en quelque chose de plus petit que 1,00 (par exemple, 0,1)
- (Sur certains systèmes, les décimales sont indiquées par une virgule plutôt qu'un point)
- Dans notre exemple, cela signifie qu'OpenSesame ne lancera qu'une seule ligne (sélectionnée aléatoirement) au lieu de toutes les 12
- N'oubliez pas de remettre "Répéter" à 1,00 lorsque vous avez terminé les tests

</div>


## Hiérarchie expérimentale

L'IAT contient plus de blocs que celui actuel. Il contient également un bloc dans lequel des images de visages doivent être catégorisées comme jeunes ou vieux, et deux blocs contenant les deux tâches mélangées (voir %Task). Cela signifie que nous devons créer trois autres blocs d'essais, chacun contenant sa propre séquence d'essais. La structure hiérarchique de l'expérience se présente donc comme suit (et lorsque nous aurons terminé la programmation, notre zone d'aperçu devrait ressembler à ceci) :

%--
figure :
 id: Hierarchy
 source: hierarchy.png
 caption: |
  La hiérarchie expérimentale de l'IAT.
--%

## Bloc 2 : catégorisation des visages

Concentrons-nous d'abord sur la tâche de catégorisation des visages. Plus précisément, nous allons :

- Créer une boucle de blocs supplémentaire et une séquence d'essais
- Réutiliser tout ce que nous pouvons réutiliser de la partie précédente de l'expérience
- Ajouter de nouvelles variables et événements spécifiques à la tâche de catégorisation des visages

### Étape 4 : Créer une boucle de blocs supplémentaire

- Prenez un élément `loop` dans la `item toolbar`
- Glissez-déposez-le sur la zone d'aperçu
- Pour que le nouveau bloc apparaisse après le premier, déposez-le *sur* l'élément `words_block_loop` (voir %AppendLoopAndSequence)
- OpenSesame vous demande si vous souhaitez insérer l'élément actuel *dans* le `words_block_loop`, ou *après*. Choisissez ce dernier

<div class='info-box' markdown='1'>

__Conseil__ -- Si vous mettez par erreur le nouvel élément *dans* la boucle de bloc, vous pouvez toujours annuler cette action en appuyant sur `Ctrl+Alt+Z`).

</div>

- Donnez un nom significatif à la nouvelle boucle, par exemple *faces_block_loop*

### Étape 5 : Ajouter une nouvelle séquence d'essais

Bien que la séquence d'essais de la tâche de catégorisation des visages présente certaines similitudes avec la tâche de catégorisation des mots, elles ne sont pas identiques. Par conséquent, nous ne pouvons pas réutiliser la séquence d'essais que nous avons créée précédemment.

Pour en créer une nouvelle :

- Prenez un élément `sequence` dans la barre d'outils des éléments
- Déposez-le *dans* le *faces_block_loop*
- Cette fois-ci, choisissez "insérer dans" (voir %AppendLoopAndSequence)
- Renommez l'élément en *faces_trial_sequence*

%--
video :
 source: youtube
 id : AppendLoopAndSequence
 videoid: PVcXdAN3rjM
 width: 640
 height: 360
 caption: |
  Étape 5 et 6: Ajout du bloc 2 et de sa séquence d'essais correspondante à l'expérience.
--%


### Étape 6 : Choisissez les stimuli de visage

__Téléchargez les stimuli de visage__

Dans l'équivalent du visage de la tâche, nous avons besoin d'images de six visages jeunes et six visages vieux. Pour éviter que les biais de genre n'influencent nos résultats, il semble préférable d'utiliser un nombre égal de visages masculins et féminins par catégorie (ici : trois).

Vous pouvez télécharger un ensemble d'exemples de stimuli (au format JPG) ici :

- %static:attachments/iat/face-stimuli.zip%

Dans la plupart des navigateurs web, vous pouvez cliquer avec le bouton droit de la souris sur le lien et choisir "Enregistrer le lien sous" ou une option similaire. Après avoir téléchargé ces fichiers (dans votre dossier Téléchargements, par exemple), vous pouvez les décompresser.

__Ajoutez les fichiers JPG au fichier pool__

- Si le fichier pool n'est pas déjà visible (par défaut sur le côté droit de la fenêtre), cliquez sur le bouton "Afficher le fichier pool" dans la barre d'outils principale (raccourci : `Ctrl+P`).
- Cliquez sur le signe plus pour ajouter des fichiers
- Parcourez votre dossier Téléchargements (ou l'endroit où vous avez enregistré et décompressé le dossier *face-stimuli*) et ajoutez les 12 fichiers JPG.

Le fichier pool devrait maintenant ressembler à %FacesBlockLoop

### Étape 7 : Contenu du tableau de boucle

Tout comme dans la partie précédente de l'expérience (voir l'étape 1), nous avons besoin de trois colonnes pour définir les variables expérimentales : *stimulus*, *categorie* et *reponse_correcte*. La seule différence est que cette fois-ci, les stimuli sont les fichiers JPG que nous venons d'ajouter au fichier pool.

En ce qui concerne la réponse correcte, disons que :

- La catégorie *JEUNE* apparaît du côté gauche de l'écran, tandis que la catégorie *VIEUX* apparaît du côté droit
- La règle de réponse est la même qu'auparavant

Créez les colonnes mentionnées ci-dessus et assurez-vous que votre boucle de blocs ressemble à ceci:

%--
figure:
 id: FacesBlockLoop
 source: faces_block_loop.png
 caption: |
  Contenu du pool de fichiers et du tableau de boucles correspondant au Bloc 2 (catégorisation des visages) de l'IAT.
--%

<div class='info-box' markdown='1'>

__Astuce__ -- Les valeurs de la colonne *stimulus* doivent correspondre exactement aux noms des fichiers dans les pools de fichiers. Sinon, OpenSesame ne pourra pas trouver les JPG si nous devons nous y référer plus tard.

</div>

### Étape 8 : Modifier la séquence d'essai

Pour l'instant, notre nouvelle séquence d'essai est encore vide. Nous devons la remplir avec les événements suivants (voir %TrialSequence) :

1. Afficher un point de fixation pendant 500 ms
2. Montrer une photo d'un visage, avec les deux noms de catégories (*OLD* et *YOUNG*)
3. Collecter une réponse au clavier
4. Écrire toutes les variables dans le fichier de sortie

__Copier les éléments réutilisables__

Les événements 1, 3 et 4 sont identiques à la partie mot de l'expérience. Nous pouvons donc réutiliser les éléments correspondants en les copiant. Pour ce faire :

- Faites un clic droit sur *fixation* (dans *words_trial_sequence*) dans la zone d'aperçu
- Choisissez 'copy (linked)', car nous voulons créer une autre occurrence du même élément
- Faites un clic droit sur *faces_trial_sequence* (c'est-à-dire la nouvelle séquence)
- Choisissez 'Coller'
- Choisissez 'Insérer dans...'
- Répétez cette procédure pour les éléments *keyboard_response* et *logger* (voir %LinkedCopies)

<div class='info-box' markdown='1'>

__Astuce__ -- Si l'ordre des éléments dans la séquence est mélangé, vous pouvez le corriger en faisant glisser et déposer

__Astuce__ -- Si vous avez accidentellement déposé une copie ailleurs dans la zone d'aperçu (c'est-à-dire en dehors de la séquence d'essai que vous visiez), vous pouvez toujours annuler cette action en appuyant sur `Ctrl+Alt+Z`

</div>

%--
video:
 source: youtube
 id: LinkedCopies
 videoid: _vDGpPsSqIY
 width: 640
 height: 360
 caption: |
  Utilisation de copies liées.
--%

### Étape 9 : Créer l'affichage du visage

Enfin, nous devons créer un nouvel élément `sketchpad` pour afficher les stimuli du visage. Pour ce faire :

- Prenez un élément `sketchpad` dans la zone d'aperçu
- Déposez-le dans le *faces_trial_sequence*
- Assurez-vous qu'il apparaisse juste après le point de fixation
- Renommez l'élément en *face*

À présent, votre zone d'aperçu doit ressembler à ceci :

%--
figure:
 id: OverviewBlock1-2.png
 source: overview-area-with-face-block.png
 caption: |
  Zone d'aperçu après avoir ajouté tous les éléments dans le *faces_trial_sequence*.
--%

### Étape 10 : Configurer le contenu du sketchpad de visage

__Dessiner les noms des catégories__

- Comme auparavant, montrez les deux catégories (ici : *YOUNG* dans le quadrant supérieur gauche, et *OLD* dans le quadrant supérieur droit) en utilisant l'élément `Draw textline`
- Réglez la durée du sketchpad sur 0 ms

__Afficher le stimulus de visage__

Ensuite, nous voulons montrer une image d'un visage au centre de l'écran. Comme auparavant, le stimulus est *variable*, de sorte que le visage affiché dépend de la ligne dans la boucle de bloc qui est actuellement exécutée. Par conséquent, nous utiliserons à nouveau la `syntaxe à crochets`. Mais d'abord :

- Sélectionnez l'élément `Draw image` du sketchpad
- Cliquez sur le centre
- Sélectionnez l'un des fichiers jpg

Ensuite, nous voulons rendre le fichier jpg variable plutôt que statique. Pour ce faire, nous devons apporter une petite modification au *script* de l'élément sketchpad :

- Cliquez sur le bouton 'Select view' en haut à droite de l'onglet *face* et sélectionnez 'View script'. Vous verrez maintenant le script correspondant au sketchpad que nous venons de créer :

~~~ .python
set duration 0
set description "Displays stimuli"
draw image center=1 file="of1.jpg" scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text="YOUNG<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text=OLD x=320 y=-192 z_index=0
~~~

- La seule chose que nous devons faire est de remplacer la chaîne 'of1.jpg' par `[stimulus]`. Cela signifie qu'OpenSesame utilise la variable `[stimulus]` (qui contient tous les noms de JPG) pour déterminer quelle image doit être affichée.

~~~ .python
set duration 0
set description "Affiche les stimuli"
draw image center=1 file=[stimulus] scale=1 show_if=toujours x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=toujours text="JEUNE<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=toujours text=VIEUX x=320 y=-192 z_index=0
~~~

- Cliquez sur 'appliquer et fermer'

Ensuite, il est temps de tester si votre expérience fonctionne jusqu'à ce point.


## Les blocs mixtes

### Correspondance congruente

Le troisième bloc est un mélange des blocs 1 et 2, de sorte que les participants doivent catégoriser à la fois les mots et les visages. La correspondance est *congruente*, de sorte que les mots *POSITIFS* et les visages *JEUNES* nécessitent une réponse de la main gauche, tandis que les mots *NÉGATIFS* et les visages *VIEUX* nécessitent une réponse de la main droite (voir %Task).

### Étape 11 : Créer une troisième boucle de bloc et une séquence d'essai

Afin de créer le troisième bloc du IAT, nous devons :

- Créer une nouvelle boucle de bloc (et la renommer en *congruent_block_loop*) (cf. Étape 4)
- Créer une nouvelle séquence d'essai (à l'intérieur de la nouvelle boucle de bloc) et l'appeler *congruent_trial_sequence* (cf. Étape 5).

Votre vue d'ensemble expérimentale devrait maintenant ressembler à ceci (%OverviewWithCongruent) :

%--
figure:
 id: OverviewWithCongruent
 source: overview_with_congruent_loop.png
 caption: |
  Vue d'ensemble expérimentale après avoir inséré une troisième boucle de bloc et une séquence d'essai.
--%

### Étape 12 : Remplir la *congruent_block_loop*

Le contenu de la boucle de bloc congruent est très similaire à la boucle de bloc de mot et de visage, sauf qu'il contient maintenant les deux types de stimuli. Par conséquent :

- Copiez-collez le contenu du *word_block_loop* dans le congruent_block_loop. Cela prendra les rangées 1 à 12
- Faites de même pour le contenu du *faces_block_loop*. Cela prendra les rangées 13 à 24
- (Assurez-vous de ne pas copier les en-têtes de colonne deux fois)

### Étape 13 : Remplir la *congruent_trial_sequence*

- Comme à l'étape 8, copiez les éléments *fixation*, *keyboard_response* et *logger* dans la nouvelle séquence d'essai
- Malheureusement, nous ne pouvons pas utiliser des copies du *word* sketchpad et du *face* sketchpad, car nous voulons montrer *les deux* catégories (c'est-à-dire POSITIF vs NÉGATIF et JEUNE vs VIEUX) sur le côté gauche et droit de l'affichage
- Par conséquent, nous ajoutons un nouvel élément `sketchpad` à la congruent_trial_sequence et l'appelons *congruent_stimulus*
- Assurez-vous que le nouveau sketchpad apparaît juste après le point de fixation, et avant l'élément `keyboard_response`

Votre vue d'ensemble expérimentale devrait maintenant ressembler à ceci (%OverviewWithCongruent) :

%--
figure:
 id: OverviewWithCongruent
 source: overview_congruent_filled_in.png
 caption: |
  Vue d'ensemble expérimentale après avoir rempli la séquence d'essai du bloc congruent.
--%

### Étape 14 : Ajustez le contenu du *congruent_sketchpad*

Ouvrez l'onglet du *congruent_stimulus* sketchpad et changez sa durée à 0 au lieu de 'keypress'.

__Noms de catégorie__

- Assurez-vous que les deux noms de catégorie apparaissent en haut à gauche et à droite de l'écran (voir %Task). Utilisez le mappage suivant :
    - Les noms de catégorie *POSITIF* et *JEUNE* apparaissent sur le côté gauche
    - *NÉGATIF* et *VIEUX* apparaissent sur le côté droit

__Stimuli de mots__

Dessinez le stimulus de mot au centre de l'écran de la même manière que nous l'avons fait pour le bloc 1 (voir l'étape 3). Utilisez la syntaxe `à base de crochets`.

__Stimuli de visage__

Dessinez le stimulus de visage au centre de l'écran de la même manière que nous l'avons fait pour le bloc 2 (voir l'étape 9).Ajouter

<div class='info-box' markdown='1'>

__Conseil__ -- Ne vous inquiétez pas si votre sketchpad semble désordonné. Nous nous occuperons de cela sous peu.

</div>


## Étape 15 : Utilisation des déclarations Show-if

Dans la partie mixte de l'expérience, nous voulons qu'OpenSesame détermine s'il doit afficher un visage ou un mot. Nous pouvons le faire en utilisant des *Déclarations Show-if*. Plus précisément, nous voulons que le stimulus_sketchpad :

- Montre un mot *uniquement* lorsque le stimulus est un mot (c'est-à-dire lorsque la cellule actuelle de la colonne stimulus dans la boucle de bloc est un mot)
- Montre un visage *uniquement* lorsque le stimulus est un visage

Pour ce faire :

- Ajoutez une colonne au *congruent_block_loop* et appelez-la *stimulus_type*
- Donnez aux cellules la valeur 'word' ou 'face', en fonction du stimulus (voir %CongrLoop)

%--
figure:
 id: CongrLoop
 source: congruent_block_loop.png
 caption: |
  Contenu de la boucle de bloc de la partie congruente de l'expérience.
--%

Ensuite, pour que le contenu du sketchpad dépende des valeurs de la colonne nouvellement créée:

- Sélectionnez la flèche noire dans la barre d'outils de l'élément du sketchpad
- Cliquez sur le point d'interrogation (qui indique l'élément `Draw image` qui s'occupe de la présentation des fichiers JPG)
- Cliquez sur la case `Show if` appartenant à cet élément, qui par défaut est réglé sur 'always'
- Utilisez la syntaxe des crochets pour indiquer que cette partie du sketchpad ne doit être dessinée que si l'essai en cours contient une image de visage en tapant:

~~~ .python
[stimulus_type] = face
~~~

%--
video:
 source: youtube
 id: RunIf
 videoid: jqGFefCmn1k
 width: 640
 height: 360
 caption: |
  Utilisation d'une déclaration Run-if dans un élément `sketchpad`.
--%



- Faites de même pour l'élément `Draw text` qui contrôle la présentation des mots écrits. Cette fois, la déclaration Show-if doit être

~~~ .python
[stimulus_type] = word
~~~

Testez si les trois premiers blocs de votre expérience fonctionnent comme vous le souhaitez.

## Cartographie incongruente

## Étape 16 : Créer le bloc incongruent de l'expérience

### Devoir

Utilisez ce que vous avez appris dans les étapes précédentes pour construire la partie finale, incongruente de l'expérience.

Quelques conseils :

- Donnez des noms significatifs aux nouveaux éléments (par exemple, aux nouveaux éléments `loop` et `sequence`) (par exemple *incongruent_block_loop*, *incongruent_trial_sequence*)
- Copiez les éléments qui sont identiques pour chaque bloc (c'est-à-dire le point de fixation, la réponse_clavier et le logger)
- Vous ne pouvez pas copier le stimulus_sketchpad, car la correspondance des catégories (apparaissant en haut à gauche et à droite) doit être intervertie, de sorte que:
    - Le côté gauche montre *POSITIF* et *VIEUX*
    - Le côté droit montre *NÉGATIF* et *JEUNE* (voir %Task)
- Les valeurs dans la colonne *correct_response* doivent être modifiées en conséquence


<div class='info-box' markdown='1'>

__Astuce__ Vous pouvez utiliser une copie *non liée* du sketchpad *congruent_stimulus* pour créer le sketchpad *incongruent_stimulus* (qui est presque identique, sauf que les noms de catégorie *OLD* et *YOUNG* sont échangés).

Contrairement à une copie *liée*, une copie *non liée* aura au départ l'air identique (à l'exception de son nom), mais vous pouvez modifier l'original sans affecter la copie non liée, et vice versa.


</div>


## Devoirs supplémentaires :

### Facile : ajoutez un écran d'instruction et d'au revoir

- Les éléments `sketchpad` et `form_text_display` peuvent présenter du texte
- Les bonnes instructions sont courtes et concrètes

### Moyen : fournir un retour d'information à chaque essai

- Utilisez la variable intégrée *correct* qui a
    - la valeur 1 si le participant a répondu correctement
    - la valeur 0 si le participant a commis une erreur
- Un moyen simple de fournir un retour d'information est de présenter brièvement un point rouge après une réponse incorrecte et un point vert après une réponse correcte
- Utilisez des déclarations Show-if