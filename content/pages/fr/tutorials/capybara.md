title: Chats, chiens et capybaras
uptodate: false
hash: 66f26fecbe543127ecd03e1ed499f5e5ab9f112189ee97bc58925aeb119dddac
locale: fr
language: French

%--
figure:
 id: FigCapybara
 source: capybara.png
 caption: |
  Un capybara.
--%


[TOC]


## À propos

Nous allons créer une tâche d'intégration multisensorielle simple remplie d'animaux, dans laquelle les participants voient une photo d'un chien, d'un chat ou d'un capybara. Un miaulement ou un aboiement est joué pendant que l'image est affichée. Le participant indique si un chien ou un chat est montré, en cliquant avec la souris sur un bouton de réponse à l'écran. Aucune réponse ne doit être donnée lorsqu'un capybara est montré : ce sont des essais pièges.

Nous faisons deux prédictions simples :

- Les participants devraient être plus rapides à identifier les chiens lorsqu'un son d'aboiement est joué, et plus rapides à identifier les chats lorsqu'un son de miaulement est joué. En d'autres termes, nous nous attendons à un effet de congruence multisensorielle.
- Lorsque les participants voient un capybara, ils sont plus susceptibles de signaler qu'ils voient un chien lorsqu'ils entendent un aboiement, et plus susceptibles de signaler qu'ils voient un chat lorsqu'ils entendent un miaulement. En d'autres termes, les fausses alertes sont biaisées par le son.


## Tutoriel

### Étape 1 : Téléchargez et démarrez OpenSesame

OpenSesame est disponible pour Windows, Linux, Mac OS et Android (exécution uniquement). Ce tutoriel est rédigé pour OpenSesame 3.3.X. Vous pouvez télécharger OpenSesame à partir d'ici :

- %link:download%

Lorsque vous démarrez OpenSesame, on vous proposera de choisir parmi des expériences modèles et (le cas échéant) une liste d'expériences récemment ouvertes (voir %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La fenêtre d'OpenSesame au démarrage.
--%

Le *modèle étendu* fournit un bon point de départ pour créer des expériences basées sur des essais. Cependant, dans ce tutoriel, nous créerons l'ensemble de l'expérience à partir de zéro. Nous continuerons donc avec le "modèle par défaut", qui est déjà chargé lors du lancement d'OpenSesame (%FigDefaultTemplate). Fermez simplement les onglets "Commencer !" et (si affiché) "Bienvenue!".

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  La structure du "modèle par défaut" vue dans la zone d'aperçu.
--%

<div class='info-box' markdown='1'>

**Encadré 1 : Les bases**

Les expériences OpenSesame sont des collections d' *items*. Un item est un petit morceau de fonctionnalité qui, par exemple, peut être utilisé pour présenter des stimuli visuels (l'item SKETCHPAD) ou pour enregistrer des pressions de touches (l'item KEYBOARD_RESPONSE). Les items ont un type et un nom. Par exemple, vous pourriez avoir deux items du type KEYBOARD_RESPONSE avec les noms *t1_response* et *t2_response*. Pour bien distinguer les types et les noms d'items, nous utiliserons CE_STYLE pour les types et *ce style* pour les noms.

Pour donner une structure à votre expérience, deux types d'items sont particulièrement importants : la LOOP et la SEQUENCE. Comprendre comment vous pouvez combiner des LOOPs et des SEQUENCEs pour construire des expériences est peut-être la partie la plus délicate du travail avec OpenSesame, alors abordons ce point en premier.

Une LOOP est l'endroit où, dans la plupart des cas, vous définissez vos variables indépendantes. Dans une LOOP, vous pouvez créer un tableau dans lequel chaque colonne correspond à une variable et chaque ligne correspond à une seule exécution de l' "item à exécuter". Pour rendre cela plus concret, considérons la *block_loop* suivante (sans rapport avec ce tutoriel) :

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  Un exemple de variables définies dans un tableau de boucle. (Cet exemple n'est pas lié à l'expérience créée dans ce tutoriel.)
--%

Cette *block_loop* exécutera *trial_sequence* quatre fois. Une fois avec `soa` à 100 et `target` à 'F', une fois avec `soa` à 100 et `target` à 'H', etc. L'ordre dans lequel les lignes sont parcourues est aléatoire par défaut, mais peut également être réglé sur séquentiel dans le coin supérieur droit de l'onglet.

Une SEQUENCE est composée d'une série d'éléments exécutés les uns après les autres. Une SEQUENCE prototype est la *trial_sequence*, qui correspond à un essai unique. Par exemple, une *trial_sequence* de base pourrait être composée d'un SKETCHPAD, pour présenter un stimulus, d'une KEYBOARD_RESPONSE, pour recueillir une réponse, et d'un LOGGER, pour écrire les informations de l'essai dans le fichier journal.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  Un exemple d'un élément SEQUENCE utilisé comme séquence d'essai. (Cet exemple n'est pas lié à l'expérience créée dans ce tutoriel.)
--%

Vous pouvez combiner les LOOPs et les SEQUENCEs de manière hiérarchique pour créer des blocs d'essais, ainsi que des phases de pratique et d'expérimentation. Par exemple, la *trial_sequence* est appelée par la *block_loop*. Ensemble, ils correspondent à un bloc unique d'essais. Un niveau plus haut, la *block_sequence* est appelée par la *practice_loop*. Ensemble, ils correspondent à la phase de pratique de l'expérience.

</div>


### Étape 2 : Ajouter une block_loop et une trial_sequence

Le modèle par défaut commence avec trois éléments : un NOTEPAD appelé *getting_started*, un SKETCHPAD appelé *welcome* et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et *welcome*, alors supprimons-les tout de suite. Pour ce faire, faites un clic droit sur ces éléments et sélectionnez 'Supprimer'. Ne supprimez pas *experiment*, car c'est l'entrée de l'expérience (c'est-à-dire le premier élément appelé lorsque l'expérience commence).

Notre expérience aura une structure très simple. Au sommet de la hiérarchie se trouve une LOOP, que nous appellerons *block_loop*. Le *block_loop* est l'endroit où nous définirons nos variables indépendantes (voir aussi l'encadré 1 en arrière-plan). Pour ajouter une LOOP à votre expérience, faites glisser l'icône LOOP de la barre d'outils des éléments sur l'élément *experiment* dans la zone d'aperçu.

Un élément LOOP a besoin d'un autre élément pour fonctionner ; généralement, et dans ce cas également, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE de la barre d'outils des éléments sur l'élément *new_loop* dans la zone d'aperçu. OpenSesame vous demandera si vous voulez insérer la SEQUENCE dans ou après la LOOP. Sélectionnez 'Insérer dans new_loop'.

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est recommandé de les renommer. Les noms des éléments doivent être composés de caractères alphanumériques et/ou de traits de soulignement. Pour renommer un élément, double-cliquez sur l'élément dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un essai unique. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

La zone d'aperçu de notre expérience ressemble maintenant à celle présentée en %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%

<div class='info-box' markdown='1'>

**Encadré 3 : Éléments inutilisés**

__Astuce__ — Les éléments supprimés sont toujours disponibles dans la corbeille des éléments inutilisés, jusqu'à ce que vous sélectionniez 'Supprimer définitivement les éléments inutilisés' dans l'onglet Éléments inutilisés. Vous pouvez réajouter des éléments supprimés à votre expérience en les faisant glisser hors de la corbeille des éléments inutilisés dans une SEQUENCE ou LOOP.

</div>

### Étape 3 : Importer des images et des fichiers sonores

Pour cette expérience, nous utiliserons des images de chats, de chiens et de capybaras. Nous utiliserons également des échantillons sonores de miaulements et d'aboiements. Vous pouvez télécharger tous les fichiers requis à partir d'ici :

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton 'Afficher le pool de fichiers' dans la barre d'outils principale (ou : Menu → Affichage → Afficher le pool de fichiers). Ceci affichera le pool de fichiers, par défaut sur le côté droit de la fenêtre. La manière la plus simple d'ajouter les stimuli au pool de fichiers est de les faire glisser depuis le bureau (ou l'endroit où vous avez extrait les fichiers) dans le pool de fichiers. Sinon, vous pouvez cliquer sur le bouton '+' dans le pool de fichiers et ajouter des fichiers en utilisant la boîte de dialogue de sélection de fichiers qui apparaît. Le pool de fichiers sera automatiquement sauvegardé avec votre expérience.

Après avoir ajouté tous les stimuli, votre pool de fichiers ressemble à celui de %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Le pool de fichiers à la fin de l'étape 3.
--%

### Étape 4 : Définir les variables expérimentales dans le bloc_loop

Conceptuellement, notre expérience a un design entièrement croisé 3×2 : Nous avons trois types de stimuli visuels (chats, chiens et capybaras) qui se produisent en combinaison avec deux types de stimuli auditifs (miaulements et aboiements). Cependant, nous avons cinq exemples pour chaque type de stimulus : cinq sons de miaulement, cinq images de capybara, etc. D'un point de vue technique, il est donc logique de traiter notre expérience comme un design 5×5×3×2, dans lequel le numéro de l'image et le numéro du son sont des facteurs avec cinq niveaux.

OpenSesame est très bon pour générer des designs factoriels complets. Tout d'abord, ouvrez *block_loop* en cliquant dessus dans la zone d'aperçu. Ensuite, cliquez sur le bouton Design factoriel complet. Ceci ouvrira un assistant pour générer des designs factoriels complets, qui fonctionne de manière simple : Chaque colonne correspond à une variable expérimentale (c.-à-d. un facteur). La première ligne est le nom de la variable, les lignes ci-dessous contiennent toutes les valeurs possibles (c.-à-d. les niveaux). Dans notre cas, nous pouvons spécifier notre design 5×5×3×2 comme indiqué dans %FigLoopWizard.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  L'assistant de boucle génère des designs factoriels complets.
--%

Après avoir cliqué sur 'Ok', vous verrez qu'il y a maintenant une table LOOP avec quatre rangées, une pour chaque variable expérimentale. Il y a 150 cycles (=5×5×3×2), ce qui signifie que nous avons 150 essais uniques. Votre table LOOP ressemble maintenant à celle de %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La table LOOP à la fin de l'étape 4.
--%

### Étape 5 : Ajouter des éléments à la séquence d'essais

Ouvrez *trial_sequence*, qui est toujours vide. Il est temps d'ajouter des éléments ! Notre *trial_sequence* de base est :

1. Un SKETCHPAD pour afficher un point de fixation central pendant 500 ms
2. Un SAMPLER pour jouer un son d'animal
3. Un SKETCHPAD pour afficher une image d'animal
4. Un MOUSE_RESPONSE pour recueillir une réponse
5. Un LOGGER pour écrire les données dans un fichier

Pour ajouter ces éléments, faites-les glisser un par un depuis la barre d'outils des éléments dans la *trial_sequence*. Si vous déposez accidentellement des éléments au mauvais endroit, vous pouvez simplement les réorganiser en les faisant glisser et en les déposant. Une fois que tous les éléments sont dans le bon ordre, donnez à chacun d'eux un nom sensé. La zone d'aperçu ressemble maintenant à celle de %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
--%

### Étape 6 : Définir le point de fixation central

Cliquez sur *fixation_dot* dans la zone d'aperçu. Cela ouvre un tableau de dessin de base que vous pouvez utiliser pour concevoir vos stimuli visuels. Pour dessiner un point de fixation central, cliquez d'abord sur l'icône de la croix, puis cliquez sur le centre de l'affichage, c'est-à-dire à la position (0, 0).

Nous devons également spécifier combien de temps le point de fixation est visible. Pour ce faire, changez la durée de 'keypress' à 495 ms, afin de spécifier une durée de 500 ms. (Voir le cadre d'information 4 pour une explication.)

L'élément *fixation_dot* ressemble désormais à celui de %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: |
  L'élément *fixation_dot* à la fin de l'étape 6.
--%

<div class='info-box' markdown='1'>

**Encadré d'information 4 : Sélectionner la bonne durée**

Pourquoi spécifier une durée de 495 si nous voulons une durée de 500 ms ? La raison en est que la durée réelle de présentation de l'affichage est toujours arrondie à une valeur compatible avec la fréquence de rafraîchissement de votre moniteur. Cela peut sembler compliqué, mais pour la plupart des besoins, les règles générales suivantes sont suffisantes :

1. Choisissez une durée qui est possible compte tenu de la fréquence de rafraîchissement de votre moniteur. Par exemple, si la fréquence de rafraîchissement de votre moniteur est de 60 Hz, cela signifie que chaque image dure 16,7 ms (= 1000 ms/60 Hz). Par conséquent, sur un moniteur de 60 Hz, vous devez toujours sélectionner une durée qui est un multiple de 16,7 ms, comme 16,7, 33,3, 50, 100, etc.
2. Dans le champ de durée du SKETCHPAD, spécifiez une durée qui est de quelques millisecondes plus courte que ce que vous visez. Donc, si vous voulez présenter un SKETCHPAD pendant 50 ms, choisissez une durée de 45. Si vous voulez présenter un SKETCHPAD pendant 1000 ms, choisissez une durée de 995. Etc.

Pour une discussion détaillée sur le temps expérimental, voir :

- %link:timing%

</div>


### Étape 7 : Définir le son de l'animal

Ouvrez *animal_sound*. L'élément SAMPLER offre un certain nombre d'options, la plus importante étant le fichier son qui doit être joué. Cliquez sur le bouton parcourir pour ouvrir la boîte de dialogue de sélection de la file-pool, et sélectionnez l'un des fichiers son, comme `bark1.ogg`.

Bien sûr, nous ne voulons pas toujours jouer le même son ! Au lieu de cela, nous voulons sélectionner un son en fonction des variables `sound` et `sound_nr` que nous avons définies dans la boucle *block_loop* (étape 5). Pour ce faire, il suffit de remplacer la partie de la chaîne que vous voulez dépendre d'une variable par le nom de cette variable entre crochets. Plus précisément, 'bark1.ogg' devient '[sound][sound_nr].ogg', car nous voulons remplacer 'bark' par la valeur de la variable `sound` et '1' par la valeur de `sound_nr`.

Nous devons également changer la durée du SAMPLER. Par défaut, la durée est 'sound', ce qui signifie que l'expérience sera en pause pendant la lecture du son. Changez la durée à 0. Cela ne signifie pas que le son sera joué pendant seulement 0 ms, mais que l'expérience passera tout de suite à l'élément suivant, pendant que le son continue de jouer en arrière-plan. L'élément *animal_sound* ressemble maintenant à ce qui est montré dans %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  L'élément *animal_sound* à la fin de l'étape 7.
--%

<div class='info-box' markdown='1'>

**Encadré 5 : Variables**

Pour plus d'informations sur l'utilisation des variables, voir :

- %link:manual/variables%

</div>

### Étape 8 : Définir l'image de l'animal

Ouvrez *animal_picture*. Sélectionnez l'outil image en cliquant sur le bouton avec l'icône de paysage. Cliquez sur le centre (0, 0) de l'affichage. Dans la boîte de dialogue File Pool qui apparaît, sélectionnez `capybara1.png`. Le regard latéral du capybara vous fixera paresseusement depuis le centre de l'affichage. Mais bien sûr, nous ne voulons pas toujours montrer le même capybara. Au lieu de cela, nous voulons que l'image dépende des variables `animal` et `pic_nr` que nous avons définies dans la boucle *block_loop* (étape 4).

Nous pouvons utiliser essentiellement la même astuce que nous avons fait pour *animal_sound*, bien que les choses fonctionnent légèrement différemment pour les images. Tout d'abord, faites un clic droit sur le capybara et sélectionnez "Modifier le script". Cela vous permet de modifier la ligne de script OpenSesame suivante correspondant à l'image du capybara :

```python
draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0
```

Maintenant, changez le nom du fichier image de 'capybara.png' en '[animal][pic_nr].png' :

```python
draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0
```

Cliquez sur "Ok" pour appliquer le changement. Le capybara a maintenant disparu, remplacé par une image réservée, et OpenSesame vous dit qu'un objet n'est pas affiché, car il est défini à l'aide de variables. Ne vous inquiétez pas, il sera affiché pendant l'expérience !

Nous ajoutons également deux cercles de réponse :

- Un cercle avec le nom 'chien' sur le côté gauche de l'écran. (Pour rappeler au participant la règle de réponse, vous pouvez ajouter un élément de texte avec le texte 'chien' au cercle. C'est purement visuel.)
- Un cercle avec le nom 'chat' sur le côté droit de l'écran. (Pour rappeler au participant la règle de réponse, vous pouvez ajouter un élément de texte avec le texte 'chat' au cercle.)

Nous allons utiliser ces cercles comme *régions d'intérêt* pour nos réponses à la souris. Plus précisément, parce que nous avons donné un nom aux cercles, notre élément *mouse_response* pourra vérifier si le clic de la souris se situe à l'intérieur de l'un de ces cercles. Nous y reviendrons dans l'étape 9.

Enfin, réglez le champ 'Durée' sur '0'. Cela ne signifie pas que l'image est présentée pendant seulement 0 ms, mais que l'expérience passera à l'élément suivant (*response*) immédiatement après. Comme *response* attend une réponse, mais ne change pas ce qui est affiché à l'écran, la cible restera visible jusqu'à ce qu'une réponse soit donnée.

%--
figure:
 id: FigStep9
 source: step9.png
 caption: |
  Le SKETCHPAD *animal_picture* à la fin de l'étape 8.
--%

<div class='info-box' markdown='1'>

**Encadré 6 : Formats d'images**

__Astuce__ -- OpenSesame peut gérer une grande variété de formats d'images. Cependant, certains formats `.bmp` (non standard) sont connus pour causer des problèmes. Si vous constatez qu'une image `.bmp` n'est pas affichée, vous pouvez envisager d'utiliser un format différent, comme `.png`. Vous pouvez facilement convertir des images avec des outils gratuits tels que [GIMP].

</div>


### Étape 9 : Définir la réponse

Ouvrez l'élément *mouse_response*. Il s'agit d'un élément MOUSE_RESPONSE, qui collecte un seul clic de souris (ou relâchement). Il y a quelques options :

- __Correct response__ — c'est ici que vous pouvez indiquer quel bouton de la souris est la bonne réponse. Cependant, nous déterminerons si une réponse est correcte en fonction de l'endroit où le participant clique, et non en fonction du bouton sur lequel il clique, donc nous pouvons laisser ce champ vide.
- __Allowed responses__ est une liste de boutons de souris séparés par des points-virgules qui sont acceptés. Réglons-le sur 'left_button'.
- __Timeout__ indique une durée après laquelle la réponse sera définie sur 'Aucune', et l'expérience continuera. Un délai d'expiration est important dans notre expérience, car les participants doivent avoir la possibilité de *ne pas* répondre lorsqu'ils voient un capybara. Réglons donc le délai d'expiration sur 2000.
- __Linked sketchpad__ indique un SKETCHPAD dont les éléments doivent être utilisés comme régions d'intérêt. Nous sélectionnerons *animal_picture*. Maintenant, si nous cliquons sur l'élément avec le nom 'chat', la variable `cursor_roi` sera automatiquement définie sur 'chat'.
- __Visible mouse cursor__ - Indique que le curseur de la souris doit être affiché pendant la collecte de la réponse. Nous devons activer cela, afin que les participants puissent voir où ils cliquent.
- __Flush pending mouse clicks__ indique que nous ne devrions accepter que les nouveaux clics de souris. Il est préférable de laisser cette option activée (c'est le cas par défaut).

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  Le MOUSE_RESPONSE *mouse_response* à la fin de l'étape 9.
--%


### Étape 10 : Définir le logger

Nous n'avons pas besoin de configurer le LOGGER, car ses paramètres par défaut sont corrects ; mais jetons-y un coup d'œil quand même. Cliquez sur *logger* dans la zone de vue d'ensemble pour l'ouvrir. Vous voyez que l'option "Log all variables (recommended)" est sélectionnée. Cela signifie qu'OpenSesame enregistre tout, ce qui est bien.

<div class='info-box' markdown='1'>

**Encadré 8 : Vérifiez toujours vos données !**

__Le conseil ultime__ — Vérifiez toujours trois fois si toutes les variables nécessaires sont consignées dans votre expérience ! La meilleure façon de vérifier cela est de lancer l'expérience et d'examiner les fichiers journaux résultants.

</div>

### Étape 11 : Terminé ! (En quelque sorte …)

Vous devriez maintenant être en mesure d'exécuter votre expérience. Il y a encore beaucoup de place pour l'amélioration, et vous travaillerez sur le polissage de l'expérience dans le cadre des Missions supplémentaires ci-dessous. Mais la structure de base est là !

Cliquez sur le bouton "Exécuter en plein écran" (`Control+R`) dans la barre d'outils principale pour faire un essai.

<div class='info-box' markdown='1'>

**Boîte contextuelle 11 : Exécution rapide**

__Astuce__ — Un test est exécuté encore plus rapidement en cliquant sur le bouton orange "Exécuter dans la fenêtre", qui ne vous demande pas comment enregistrer le fichier de journal (et ne doit donc être utilisé qu'à des fins de test).

</div>


## Travaux pratiques supplémentaires

Les travaux pratiques supplémentaires ci-dessous sont à résoudre par vos soins. Les solutions de ces travaux peuvent être trouvées dans le [fichier d'expérience](https://osf.io/2gr3a/). Mais la meilleure façon d'apprendre est de les résoudre vous-même !

### Facile : Ajouter un écran d'instruction et d'au revoir

- Les éléments SKETCHPAD et FORM_TEXT_DISPLAY peuvent présenter du texte
- Les bonnes instructions sont courtes et concrètes

### Facile : Inspecter les données

- Exécutez l'expérience une fois sur vous-même. Vous pouvez réduire le nombre d'essais en définissant la valeur Répéter du *block_loop* à moins de un.
- Ouvrez le fichier de données dans Excel, LibreOffice ou JASP

### Moyen : Fournir un retour d'information à chaque essai

- Pour ce faire, vous devez avoir déjà défini une réponse correcte ! (voir ci-dessous).
- Une bonne façon discrète de fournir un retour d'information est de présenter brièvement un point rouge après une réponse incorrecte et un point vert après une réponse correcte
- Utilisez des instructions Run If !

### Moyen : Contrebalancer la règle de réponse

- La variable `subject_parity` est 'even' ou 'odd'
- Utilisez deux éléments SKETCHPAD et MOUSE_RESPONSE différents pour les participants pairs et impairs

### Moyen : Ne pas répéter la même image d'animal

- Vous pouvez spécifier des contraintes de randomisation sous forme d'opérations de boucle avancées

### Difficile : Déterminer si la réponse était correcte

- Ceci nécessite un INLINE_SCRIPT
- Définissez la variable `correct` à 0 pour une réponse incorrecte et à 1 pour une réponse correcte
- Si un délai d'attente se produit, la variable `response` est la chaîne 'None'
- Sinon, la variable `cursor_roi` contient une liste séparée par des points-virgules de tous les noms d'éléments (du SKETCHPAD lié) qui ont été cliqués. Il est possible de cliquer sur plus d'un élément, par exemple si l'image de l'animal et le cercle de réponse se chevauchent

### Difficile : Diviser les essais en plusieurs blocs

- Ajoutez un SKETCHPAD à la fin de la séquence d'essais qui invite les participants à faire une courte pause
- Utilisez une instruction Run If pour exécuter ce SKETCHPAD seulement après tous les 15 essais
- Vous aurez besoin de l'opérateur modulo (`%`) pour faire cela, ainsi que de la variable `count_trial_sequence`

### Difficile : Adapter l'expérience pour la réalisation en ligne

- Ceci nécessite un INLINE_JAVASCRIPT
- Actuellement, OSWeb ne prend pas en charge la liaison d'un MOUSE_RESPONSE à un SKETCHPAD. Cela signifie que vous devez utiliser la variable `cursor_x` pour déterminer où le participant a cliqué et si la réponse était correcte.
- OSWeb ne prend pas en charge les éléments INLINE_SCRIPT

## Références

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un générateur d'expériences graphiques open-source pour les sciences sociales. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}