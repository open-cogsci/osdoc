title: Atelier ESCoP 2017
hash: 2218e3350fb98911efd9e3dddf712f887c598481bfa0812732c19eb030178a15
locale: fr
language: French

## À propos de l'atelier

Cet atelier OpenSesame a eu lieu en tant qu'événement pré-conférence avant ESCoP 2017.

L'atelier se composait de deux parties principales. Dans la première partie, correspondant au tutoriel ci-dessous, nous avons créé une expérience complète ensemble. Dans la deuxième partie, correspondant aux missions supplémentaires ci-dessous, les participants à l'atelier ont amélioré cette expérience par eux-mêmes, selon quelques suggestions.

Vous pouvez télécharger l'expérience complète, y compris les solutions des missions supplémentaires ici :

- <http://osf.io/jw7dr>

### Quand ?

- 3 septembre 2017
- JASP : 09:00 - 12:00
- OpenSesame : 13:00 - 16:00

### Où ?

- Université de Potsdam
- Campus III - Griebnitzsee
- Bâtiment 6 (Bâtiment de l'amphithéâtre)
- August-Bebel-Straße 89
- 14482 Potsdam
- Allemagne

### Plus d'infos

- Site de la conférence : <http://www.escop2017.org/program>
- Site JASP : <https://jasp-stats.org/>


## Screencast

%--
vidéo:
 source: youtube
 id: EscopTutorial
 videoid: ICa0vPoYrYw
 largeur: 640
 hauteur: 360
 légende: |
  Le tutoriel sous forme de vidéo.
--%


## Le tutoriel

%--
figure:
 id: FigMeowingCapybara
 source: meowing-capybara.png
 légende: |
  Ne te laisse pas berner par les capybaras qui miaulent ! ([Source][capybara_photo])
--%

[TOC]

Nous allons créer une tâche simple d'intégration multisensorielle remplie d'animaux, dans laquelle les participants voient une photo d'un chien, d'un chat ou d'un capybara. Un miaulement ou un aboiement est joué pendant que la photo est montrée. Le participant indique si un chien ou un chat est montré, en appuyant sur la touche droite ou gauche. Aucune réponse ne doit être donnée lorsqu'un capybara est montré : ce sont des essais surprises.

Pour rendre les choses plus amusantes, nous concevrons l'expérience de manière à ce que vous puissiez la réaliser sur [OSWeb](http://osweb.cogsci.nl/), un runtime en ligne pour les expériences OpenSesame (qui est encore en cours de développement, mais fonctionne pour les expériences de base).

Nous formulons deux prédictions simples :

- Les participants devraient être plus rapides pour identifier les chiens lorsqu'un aboiement est joué, et plus rapides pour identifier les chats lorsqu'un miaulement est joué. En d'autres termes, nous nous attendons à un effet de congruence multisensorielle.
- Lorsque les participants voient un capybara, ils sont plus susceptibles de signaler avoir vu un chien lorsqu'ils entendent un aboiement, et plus susceptibles de signaler avoir vu un chat lorsqu'ils entendent un miaulement. En d'autres termes, les fausses alertes sont biaisées par le son.


### Étape 1 : Téléchargez et démarrez OpenSesame

OpenSesame est disponible pour Windows, Linux, Mac OS et Android (runtime uniquement). Ce tutoriel est écrit pour OpenSesame 3.1.X, et vous pouvez utiliser la version basée sur Python 2.7 (par défaut) ou Python 3.5. Vous pouvez télécharger OpenSesame ici :

- %link:download%

Lorsque vous démarrez OpenSesame, vous aurez le choix entre des expériences modèles et (le cas échéant) une liste d'expériences récemment ouvertes (voir %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 légende: |
  La fenêtre OpenSesame au démarrage.
--%

Le *modèle étendu* offre un bon point de départ pour créer des expériences basées sur Android. Cependant, dans ce tutoriel, nous créerons l'ensemble de l'expérience à partir de zéro. Par conséquent, nous continuerons avec le "modèle par défaut", qui est déjà chargé lorsque OpenSesame est lancé (%FigDefaultTemplate). Fermez simplement les onglets "Get started!" et (si affichés) "Welcome!".

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 légende: |
  La structure du "modèle par défaut" telle que vue dans la zone de présentation.
--%

<div class='info-box' markdown='1'>

**Encadré 1 : Bases**

Les expériences OpenSesame sont des collections d'éléments. Un élément est un petit morceau de fonctionnalité qui, par exemple, peut être utilisé pour présenter des stimuli visuels (l'élément SKETCHPAD) ou pour enregistrer des pressions de touches (l'élément KEYBOARD_RESPONSE). Les éléments ont un type et un nom. Par exemple, vous pourriez avoir deux éléments du type KEYBOARD_RESPONSE avec les noms *t1_response* et *t2_response*. Pour bien distinguer les types et les noms d'éléments, nous utiliserons CE_STYLE pour les types et *ce style* pour les noms.

Pour donner une structure à votre expérience, deux types d'éléments sont particulièrement importants : la boucle (LOOP) et la séquence (SEQUENCE). Comprendre comment combiner les LOOPs et les SEQUENCEs pour construire des expériences est peut-être la partie la plus délicate du travail avec OpenSesame, alors abordons ce point en premier.

Une LOOP est l'endroit où, dans la plupart des cas, vous définissez vos variables indépendantes. Dans une LOOP, vous pouvez créer un tableau où chaque colonne correspond à une variable et chaque ligne correspond à une seule exécution de l’”élément à exécuter”. Pour rendre cela plus concret, considérons la *block_loop* suivante (sans rapport avec ce tutoriel) :

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  Un exemple de variables définies dans un tableau de boucle (LOOP). (Cet exemple n'est pas lié à l'expérience créée dans ce tutoriel.)
--%

Ce *block_loop* exécutera *trial_sequence* quatre fois. Une fois avec `soa` à 100 et `target` à 'F', une fois avec `soa` à 100 et `target` à 'H', etc. L'ordre dans lequel les lignes sont parcourues est aléatoire par défaut, mais peut aussi être défini en séquentiel en haut à droite de l'onglet.

Une SEQUENCE est composée d'une série d'éléments qui sont exécutés les uns après les autres. Une SEQUENCE prototypique est *trial_sequence*, qui correspond à une seule tentative. Par exemple, une *trial_sequence* basique pourrait contenir un SKETCHPAD, pour présenter un stimulus, un KEYBOARD_RESPONSE, pour recueillir une réponse, et un LOGGER, pour écrire les informations de l'essai dans le fichier journal.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  Un exemple d'un élément SEQUENCE utilisé comme séquence d'essai. (Cet exemple n'est pas lié à l'expérience créée dans ce tutoriel.)
--%

Vous pouvez combiner les LOOPs et les SEQUENCEs de manière hiérarchique pour créer des blocs d'essais et des phases de pratique et d'expérimentation. Par exemple, *trial_sequence* est appelée par *block_loop*. Ensemble, ils correspondent à un seul bloc d'essais. À un niveau supérieur, *block_sequence* est appelée par *practice_loop*. Ensemble, ils correspondent à la phase de pratique de l'expérience.

</div>


### Étape 2 : Ajout d'un block_loop et d'un trial_sequence

Le modèle par défaut commence avec trois éléments : un NOTEPAD appelé *getting_started*, un SKETCHPAD appelé *welcome* et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et de *welcome*, alors supprimons-les tout de suite. Pour ce faire, faites un clic droit sur ces éléments et sélectionnez "Supprimer". Ne supprimez pas *experiment* car il s'agit de l'entrée de l'expérience (c'est-à-dire le premier élément qui est appelé lorsque l'expérience démarre).

Notre expérience aura une structure très simple. Le sommet de la hiérarchie est une LOOP, que nous appellerons *block_loop*. C'est dans *block_loop* que nous définirons nos variables indépendantes (voir également l'encadré Contexte 1). Pour ajouter une LOOP à votre expérience, faites glisser l'icône LOOP de la barre d'outils des éléments sur l'élément *experiment* dans la zone d'aperçu.

Un élément LOOP a besoin d'un autre élément pour s'exécuter; en général et dans ce cas également, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE de la barre d'outils des éléments sur l'élément *new_loop* dans la zone d'aperçu. OpenSesame vous demandera si vous souhaitez insérer la SEQUENCE dans ou après la LOOP. Sélectionnez "Insérer dans new_loop".

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est recommandé de les renommer. Les noms d'éléments doivent être constitués de caractères alphanumériques et/ou de traits de soulignement. Pour renommer un élément, double-cliquez dessus dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un essai unique. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

La zone d'aperçu de notre expérience ressemble maintenant à celle figurée dans %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%

<div class='info-box' markdown='1'>

**Encadré 3 : Éléments inutilisés**

__Astuce__ — Les éléments supprimés sont toujours disponibles dans la corbeille des éléments inutilisés, jusqu'à ce que vous sélectionniez "Supprimer définitivement les éléments inutilisés" dans l'onglet des éléments inutilisés. Vous pouvez remettre les éléments supprimés dans votre expérience en les faisant glisser depuis la corbeille des éléments inutilisés vers une SEQUENCE ou LOOP.

</div>

### Étape 3 : Importer des images et des fichiers sonores

Pour cette expérience, nous utiliserons des images de chats, de chiens et de capybaras. Nous utiliserons également des échantillons sonores de miaulements et d'aboiements. Vous pouvez télécharger tous les fichiers requis ici :

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton "Afficher le pool de fichiers" dans la barre d'outils principale (ou : Menu → Affichage → Afficher le pool de fichiers). Cela affichera le pool de fichiers, par défaut sur le côté droit de la fenêtre. La façon la plus simple d'ajouter les stimuli au pool de fichiers est de les faire glisser depuis le bureau (ou depuis l'endroit où vous avez extrait les fichiers) vers le pool de fichiers. Vous pouvez également cliquer sur le bouton '+' dans le pool de fichiers et ajouter des fichiers en utilisant la boîte de dialogue de sélection de fichiers qui apparaît. Le pool de fichiers sera automatiquement enregistré avec votre expérience.

Après avoir ajouté tous les stimuli, votre pool de fichiers ressemblera à celui de la %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Le pool de fichiers à la fin de l'étape 3.
--%

### Étape 4 : Définir les variables expérimentales dans le block_loop

Conceptuellement, notre expérience a un plan croisé complet 3x2 : nous avons trois types de stimuli visuels (chats, chiens et capybaras) qui apparaissent en combinaison avec deux types de stimuli auditifs (miaulements et aboiements). Cependant, nous avons cinq exemplaires pour chaque type de stimulus : cinq sons de miaulement, cinq photos de capybara, etc. D'un point de vue technique, il est donc logique de considérer notre expérience comme un plan 5x5x3x2, dans lequel le numéro d'image et le numéro de son sont des facteurs à cinq niveaux.

OpenSesame est très efficace pour générer des plans factoriels complets. Tout d'abord, ouvrez *block_loop* en cliquant dessus dans la zone d'aperçu. Ensuite, cliquez sur le bouton Full-Factorial Design. Cela ouvrira un assistant pour générer des plans factoriels complets, qui fonctionne de manière simple : chaque colonne correspond à une variable expérimentale (c'est-à-dire un facteur). La première ligne est le nom de la variable, les lignes ci-dessous contiennent toutes les valeurs possibles (c'est-à-dire les niveaux). Dans notre cas, nous pouvons spécifier notre plan 5×5×3×2 comme indiqué dans %FigLoopWizard.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  L'assistant de boucle génère des plans factoriels complets.
--%

Après avoir cliqué sur "Ok", vous verrez qu'il y a maintenant une table LOOP avec quatre lignes, une pour chaque variable expérimentale. Il y a 150 cycles (=5×5×3×2), ce qui signifie que nous avons 150 essais uniques. Votre table LOOP ressemble maintenant à celle de la %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La table LOOP à la fin de l'étape 4.
--%

### Étape 5 : Ajouter des éléments à la séquence d'essais

Ouvrez *trial_sequence*, qui est encore vide. Il est temps d'ajouter des éléments ! Notre *trial_sequence* de base est :

1. Un SKETCHPAD pour afficher un point de fixation central pendant 500 ms
2. Un SAMPLER pour jouer un son d'animal
3. Un SKETCHPAD pour afficher une image d'animal
4. Une KEYBOARD_RESPONSE pour collecter une réponse
5. Un LOGGER pour écrire les données dans un fichier

Pour ajouter ces éléments, faites-les simplement glisser un par un de la barre d'outils des éléments dans la *trial_sequence*. Si vous déposez accidentellement des éléments au mauvais endroit, vous pouvez simplement les réorganiser en les faisant glisser et déposer. Une fois tous les éléments dans le bon ordre, donnez-leur un nom sensé. La zone d'aperçu ressemble maintenant à celle de %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
%--

### Étape 6 : Définir le point de fixation central

Cliquez sur *fixation_dot* dans la zone d'aperçu. Cela ouvre une planche à dessin de base que vous pouvez utiliser pour concevoir vos stimuli visuels. Pour dessiner un point de fixation central, cliquez d'abord sur l'icône en forme de croix, puis sur le centre de l'affichage, c'est-à-dire à la position (0, 0).

Nous devons également préciser combien de temps le point de fixation est visible. Pour ce faire, changez la durée de 'keypress' à 495 ms, afin de spécifier une durée de 500 ms. (Voir l'encadré 4 pour une explication.)

L'élément *fixation_dot* ressemble maintenant à %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: |
  L'élément *fixation_dot* à la fin de l'étape 6.
%--

<div class='info-box' markdown='1'>

**Encadré 4 : Choisir la bonne durée**

Pourquoi choisir une durée de 495 si nous voulons une durée de 500 ms ? La raison en est que la durée réelle de présentation de l'affichage est toujours arrondie à une valeur compatible avec le taux de rafraîchissement de votre moniteur. Cela peut sembler compliqué, mais pour la plupart des besoins, les règles suivantes sont suffisantes :

1. Choisissez une durée possible étant donné le taux de rafraîchissement de votre moniteur. Par exemple, si le taux de rafraîchissement de votre moniteur est de 60 Hz, cela signifie que chaque image dure 16,7 ms (= 1000 ms/60 Hz). Par conséquent, sur un moniteur de 60 Hz, vous devez toujours choisir une durée multiple de 16,7 ms, comme 16,7, 33,3, 50, 100, etc.
2. Dans le champ de durée du SKETCHPAD, spécifiez une durée de quelques millisecondes plus courte que celle que vous visez. Ainsi, si vous voulez présenter un SKETCHPAD pendant 50 ms, choisissez une durée de 45. Si vous voulez présenter un SKETCHPAD pendant 1000 ms, choisissez une durée de 995. Etc.

Pour une discussion détaillée sur le minutage des expériences, voir :

- %link:timing%

</div>

### Étape 7 : Définir le son de l'animal

Ouvrez *animal_sound*. L'élément SAMPLER fournit un certain nombre d'options, la plus importante étant le fichier sonore à jouer. Cliquez sur le bouton de navigation pour ouvrir la boîte de dialogue de sélection du fichier, et sélectionnez l'un des fichiers sonores, tels que `bark1.ogg`.

Bien sûr, nous ne voulons pas jouer le même son encore et encore ! Au lieu de cela, nous voulons sélectionner un son en fonction des variables `sound` et `sound_nr` que nous avons définies dans la *block_loop* (étape 5). Pour ce faire, remplacez simplement la partie de la chaîne sur laquelle vous voulez que la variable dépende par le nom de cette variable entre crochets. Plus précisément, 'bark1.ogg' devient '[sound][sound_nr].ogg', car nous voulons remplacer 'bark' par la valeur de la variable `sound` et '1' par la valeur de `sound_nr`.

Nous devons également changer la durée du SAMPLER. Par défaut, la durée est 'sound', ce qui signifie que l'expérience sera interrompue pendant la lecture du son. Changez la durée à 0. Cela ne signifie pas que le son sera lu pendant seulement 0 ms, mais que l'expérience passera immédiatement à l'élément suivant, pendant que le son continue de jouer en arrière-plan. L'élément *animal_sound* ressemble maintenant à celui de %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  L'élément *animal_sound* à la fin de l'étape 7.
%--

<div class='info-box' markdown='1'>

**Encadré 5 : Variables**

Pour plus d'informations sur l'utilisation des variables, voir :

- %link:manual/variables%

</div>

### Étape 8: Définir l'image d'animal

Ouvrez *animal_picture*. Sélectionnez l'outil Image en cliquant sur le bouton avec l'icône en forme de paysage. Cliquez sur le centre (0, 0) de l'affichage. Dans la boîte de dialogue File Pool qui apparaît, sélectionnez `capybara1.png`. Le regard de côté du capybara vous fixe maintenant paresseusement depuis le centre de l'écran. Mais bien sûr, nous ne voulons pas toujours montrer le même capybara. Au lieu de cela, nous voulons que l'image dépende des variables `animal` et `pic_nr` que nous avons définies dans le *block_loop* (Étape 5).

Nous pouvons utiliser essentiellement la même astuce que celle utilisée pour *animal_sound*, bien que les choses fonctionnent légèrement différemment pour les images. Faites d'abord un clic droit sur le capybara et sélectionnez "Modifier le script". Cela vous permet de modifier la ligne suivante de script OpenSesame qui correspond à l'image du capybara :

	draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0

Maintenant, changez le nom du fichier image de 'capybara.png' à '[animal][pic_nr].png':

	draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0

Cliquez sur 'Ok' pour appliquer le changement. Le capybara a maintenant disparu, remplacé par une image de remplacement, et OpenSesame vous indique qu'un objet n'est pas affiché, car il est défini à l'aide de variables. Ne vous inquiétez pas, il sera affiché pendant l'expérience !

Pour rappeler la tâche au participant, ajoutez également deux cercles de réponse, un marqué "chien" sur le côté gauche de l'écran et un marqué "chat" sur le côté droit. Je suis sûr que vous pourrez comprendre comment faire cela avec les outils de dessin de SKETCHPAD. Mon interprétation est montrée dans %FigStep9. Notez que ces cercles de réponse sont purement visuels, et nous devons encore définir explicitement les critères de réponse (voir Étape 10).

Enfin, définissez le champ "Durée" à "0". Cela ne signifie pas que l'image est présentée pendant seulement 0 ms, mais que l'expérience passera à l'élément suivant (*response*) immédiatement. Comme *response* attend une réponse, mais ne change pas ce qui est affiché à l'écran, la cible restera visible jusqu'à ce qu'une réponse soit donnée.

%--
figure:
 id: FigStep9
 source: step9.png
 caption: |
  Le SKETCHPAD *animal_picture* à la fin de l'étape 8.
--%

<div class='info-box' markdown='1'>

**Encadré 6: Formats d'image**

__Astuce__ -- OpenSesame peut gérer une grande variété de formats d'image. Cependant, certains formats `.bmp` (non standard) sont connus pour poser des problèmes. Si vous trouvez qu'une image `.bmp` n'est pas affichée, vous pouvez envisager d'utiliser un format différent, tel que `.png`. Vous pouvez convertir facilement les images avec des outils gratuits tels que [GIMP].

</div>


### Étape 9 : Définir la réponse

Ouvrez l'élément *response*. Il s'agit d'un élément KEYBOARD_RESPONSE, qui collecte une seule pression de touche. Il y a quelques options :

- __Réponse correcte__ — passons cela pour l'instant ; nous y reviendrons à l'étape 10.
- __Réponses autorisées__ est une liste séparée par des points-virgules des touches acceptées. Définissons cela sur *left;right* pour indiquer que seules les touches fléchées gauche et droite sont acceptées. (La touche *escape* met l'expérience en pause et est toujours acceptée !)
- __Délai__ indique une durée après laquelle la réponse sera définie sur "Aucune" et l'expérience continuera. Un délai est important dans notre expérience, car les participants doivent avoir la possibilité de *ne pas* répondre lorsqu'ils voient un capybara. Réglons donc le délai d'attente à 2000.
- __Vider les touches en attente__ indique que nous devons accepter uniquement les nouvelles pressions de touches. Il est préférable de laisser cette option activée (elle l'est par défaut).

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  La KEYBOARD_RESPONSE *response* à la fin de l'étape 9.
--%


### Étape 10: Définir la réponse correcte

Jusqu'à présent, nous n'avons pas défini la réponse correcte pour chaque essai. Cela se fait en définissant une variable `correct_response`. Vous pouvez le faire en créant une colonne `correct_response` dans un tableau LOOP (ici, le *block_loop*) et en entrant manuellement les réponses correctes, ou en spécifiant la réponse correcte dans un élément PYTHON INLINE_SCRIPT, ce que nous ferons ici.

Premièrement, faites glisser un élément INLINE_SCRIPT à partir de la barre d'outils des éléments et insérez-le en haut du *trial_sequence*. (N'oubliez pas de lui donner un nom significatif!) Vous voyez maintenant un éditeur de texte avec deux onglets: un onglet *Run* et un onglet *Prepare*. Vous pouvez entrer du code Python dans les deux onglets, mais ce code est exécuté pendant différentes phases de l'expérience. La phase *Prepare* est exécutée en premier chaque fois qu'une SEQUENCE est exécutée ; cela donne à tous les éléments de la SEQUENCE la possibilité d'effectuer des opérations longues qui pourraient autrement ralentir l'expérience à des moments sensibles au temps. Ensuite, la phase *Run* est exécutée ; c'est là que se déroule l'action, comme montrer un affichage, collecter une réponse, etc.

Pour plus d'informations, consultez:

- %link:prepare-run %

Définir une réponse correcte est un exemple clair de quelque chose qui doit être fait dans la phase *Prepare*. Le script suivant fera l'affaire:

~~~ .python
if var.animal == 'chien':
	var.correct_response = 'gauche'
elif var.animal == 'chat':
	var.correct_response = 'droite'
elif var.animal == 'capybara':
	var.correct_response = None # Un délai d'attente est codé comme None !
else:
	raise ValueError('Animal invalide : %s' % var.animal)
~~~

Ce code est presque en anglais simple, mais quelques conseils peuvent être utiles:

- Dans le script Python, les variables expérimentales ne sont pas mentionnées en utilisant des crochets (`[my_variable]`), comme elles le sont ailleurs dans OpenSesame, mais en tant que propriétés de l'objet `var` (c'est-à-dire `var.my_variable`).
- Nous considérons également la possibilité que l'animal ne soit ni un chien, ni un chat, ni un capybara. Bien sûr, cela ne doit jamais arriver, mais en tenant compte de cette possibilité, nous nous protégeons contre les fautes de frappe et autres bugs. Cela s'appelle la 'programmation défensive'.


### Étape 11: Définir le journal

Nous n'avons pas besoin de configurer le LOGGER, car ses paramètres par défaut sont corrects ; mais jetons-y un coup d'œil de toute façon. Cliquez sur *logger* dans la zone d'aperçu pour l'ouvrir. Vous voyez que l'option 'Log all variables (recommended)' est sélectionnée. Cela signifie qu'OpenSesame enregistre tout, ce qui est très bien.

<div class='info-box' markdown='1'>

**Boîte d'informations 8 : Vérifiez toujours vos données !**

__Le seul conseil pour les gouverner tous__ — Vérifiez toujours si toutes les variables nécessaires sont enregistrées dans votre expérience! La meilleure façon de vérifier cela est d'exécuter l'expérience et d'examiner les fichiers de journal résultants.

</div>

### Étape 12: Ajouter un retour d'information par essai

Il est de bon ton d'informer le participant de la réponse était correcte ou non. Pour éviter de perturber le déroulement de l'expérience, ce type de rétroaction immédiate doit être aussi discret que possible. Ici, nous le ferons en montrant brièvement un point de fixation vert après une réponse correcte et un point de fixation rouge après une réponse incorrecte.

Premièrement, ajoutez deux nouveaux SKETCHPADs à la fin du *trial_sequence*. Renommez le premier en *feedback_correct* et le second en *feedback_incorrect*. Bien sûr, nous ne voulons exécuter qu'un seul de ces éléments lors d'un essai donné, en fonction de la réponse correcte ou non. Pour ce faire, nous pouvons utiliser la variable intégrée `correct`, qui a la valeur 0 après une réponse incorrecte et 1 après une réponse correcte. (À condition que nous ayons défini `correct_response`, ce que nous avons fait à l'étape 11.) Pour dire au *trial_sequence* que l'élément *feedback_correct* doit être appelé uniquement lorsque la réponse est correcte, nous utilisons la déclaration run-if suivante:

	[correct] = 1

Les crochets autour de `correct` indiquent qu'il s'agit du nom d'une variable, et non simplement de la chaîne 'correct'. De même, nous utilisons la déclaration run-if suivante pour l'élément *feedback_incorrect*:

	[correct] = 0

Nous avons encore besoin de donner du contenu aux éléments *feedback_correct* et *feedback_incorrect*. Pour ce faire, ouvrez simplement les éléments et tracez un point de fixation vert ou rouge au centre. N'oubliez pas non plus de changer les durées de 'keypress' à un intervalle bref, comme 195.

La *trial_sequence* ressemble maintenant à ce qui est montré dans %FigStep13.

%--
figure:
 id: FigStep13
 source: step13.png
 caption: |
  La *trial_sequence* à la fin de l'étape 12.
--%

<div class='info-box' markdown='1'>

**Encadré 9 : Instructions conditionnelles**

Pour plus d'informations sur les instructions conditionnelles 'if', consultez :

- %link:manual/variables%

</div>

### Étape 13 : Ajouter des instructions et des écrans d'au revoir

Une bonne expérience commence toujours par un écran d'instruction et se termine par des remerciements au participant pour le temps qu'il a consacré. La manière la plus simple de faire cela dans OpenSesame consiste à utiliser des éléments `form_text_display`.

Faites glisser deux `form_text_display` dans la séquence principale de l' *experiment*. L'un doit être placé tout au début et renommé en *form_instructions*. L'autre doit être placé à la toute fin et renommé en *form_finished*. Ajoutez maintenant un texte approprié à ces formulaires, par exemple comme indiqué dans %FigStep14.

%--
figure:
 id: FigStep14
 source: step14.png
 caption: |
  L'élément *form_instructions* à la fin de l'étape 13.
--%

<div class='info-box' markdown='1'>

**Encadré 10 : Texte**

__Astuce__ -- Les formulaires, et plus généralement le texte, prennent en charge un sous-ensemble de balises HTML pour permettre la mise en forme du texte (c'est-à-dire les couleurs, le gras, etc.). Ceci est décrit ici :

- %link:visual%

</div>

### Étape 15 : Terminé !

Votre expérience est maintenant terminée ! Cliquez sur le bouton "Exécuter en plein écran" (`Control+R`) dans la barre d'outils principale pour effectuer un test. Vous pouvez également télécharger l'expérience sur OSWeb (<http://osweb.cogsci.nl/>) et l'exécuter en ligne !

<div class='info-box' markdown='1'>

**Encadré 11 : Exécution rapide**

__Astuce__ — Une exécution de test est réalisée encore plus rapidement en cliquant sur le bouton orange "Exécuter dans une fenêtre", qui ne vous demande pas comment sauvegarder le fichier journal (et ne doit donc être utilisé qu'à des fins de test).

</div>


## Travaux pratiques supplémentaires

Les solutions à ces travaux pratiques supplémentaires se trouvent dans le [fichier de l'expérience](http://osf.io/jw7dr).

### Supplément 1 : Ajouter un écran d'instruction et d'au revoir

Conseils :

- Les éléments SKETCHPAD et FORM_TEXT_DISPLAY peuvent présenter du texte
- De bonnes instructions sont brèves et concrètes

### Supplément 2 : Analyser les données

Conseils :

- Exécutez l'expérience une fois sur vous-même
- Ouvrez le fichier de données dans Excel, LibreOffice, ou JASP

### Supplément 3 : Diviser les essais en plusieurs blocs

Conseils :

- Utilisez une instruction break-if pour interrompre la boucle après (disons) 15 essais : `([count_trial_sequence]+1) % 15 = 0`
- Ajoutez une nouvelle structure LOOP-SEQUENCE au-dessus de la *block_loop* pour répéter un bloc d'essais plusieurs fois
- Désactivez l'option "Évaluer au premier cycle" dans la *block_loop* afin que l'instruction break-if ne soit pas évaluée lorsque la variable `count_trial_sequence` n'existe pas encore
- Activez l'option "Reprendre après la pause" dans la *block_loop* pour échantillonner aléatoirement sans remplacement à partir de la table LOOP

### Supplément 4 : Ajouter un retour d'information sur la précision et le temps de réponse moyen après chaque bloc

Faites d'abord le supplément 3 !

Conseils :

- Utilisez un élément FEEDBACK pour donner un retour d'information
- Les variables `acc` et `avg_rt` contiennent la précision en cours et le temps de réaction moyen

### Supplément 5 : Contrebalancer la règle de réponse

Conseils :

- La variable `subject_parity` est 'pair' ou 'impair'
- Cela nécessite un simple script INLINE_SCRIPT
- Assurez-vous que les instructions correspondent à la règle de réponse !

## Références

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}

[OpenSesame runtime pour Android]: /getting-opensesame/android
[diapositives]: /attachments/rovereto2014-workshop-slides.pdf
[modulo]: http://fr.wikipedia.org/wiki/Opération_modulo
[pdf]: /rovereto2014/index.pdf
[gimp]: http://www.gimp.org/
[photo_de_capybara]: https://commons.wikimedia.org/wiki/File:Capybara_Hattiesburg_Zoo_(70909b-58)_2560x1600.jpg