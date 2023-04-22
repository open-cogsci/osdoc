title: Atelier Genève 2018
hash: 8df5fba741d79f787237572f2811f29941f4ca7ab5549ef1f6ca3da382574132
locale: fr
language: French

## À propos de l'atelier

Cet atelier OpenSesame aura lieu à l'Université de Genève le 27 mars 2018.

L'atelier se composait de deux parties principales. Dans la première partie, correspondant au tutoriel ci-dessous, nous avons créé une expérience complète ensemble. Dans la deuxième partie, correspondant aux missions supplémentaires ci-dessous, les participants de l'atelier ont amélioré cette expérience par eux-mêmes, sur la base de quelques suggestions.

Vous pouvez télécharger l'expérience complète, y compris les solutions des missions supplémentaires ici :

- <http://osf.io/jw7dr>

## Le tutoriel

figure :
 id : FigMeowingCapybara
 source : meowing-capybara.png
 légende : |
   Ne vous laissez pas duper par les capybaras qui miaulent ! ([Source][capybara_photo])

Nous allons créer une simple tâche d'intégration multisensorielle remplie d'animaux, dans laquelle les participants voient une image d'un chien, d'un chat ou d'un capybara. Un miaulement ou un aboiement est joué pendant que l'image est affichée. Le participant signale si un chien ou un chat est montré, en appuyant sur la touche droite ou gauche. Aucune réponse ne doit être donnée lorsqu'un capybara est montré : il s'agit d'essais surprises.

Pour rendre les choses plus amusantes, nous allons concevoir l'expérience de manière à ce que vous puissiez la réaliser sur [OSWeb](http://osweb.cogsci.nl/), un environnement d'exécution en ligne pour les expériences OpenSesame (qui est encore en cours de développement, mais fonctionne pour les expériences basiques).

Nous faisons deux prédictions simples :

- Les participants devraient être plus rapides pour identifier les chiens lorsqu'un bruit d'aboiement est joué et plus rapides pour identifier les chats lorsqu'un bruit de miaulement est joué. En d'autres termes, nous nous attendons à un effet de congruence multisensorielle.
- Lorsque les participants voient un capybara, ils sont plus susceptibles de signaler qu'ils voient un chien lorsqu'ils entendent un aboiement et plus susceptibles de signaler qu'ils voient un chat lorsqu'ils entendent un miaulement. En d'autres termes, les fausses alertes sont biaisées par le son.

### Étape 1 : Téléchargez et démarrez OpenSesame

OpenSesame est disponible pour Windows, Linux, Mac OS et Android (exécution uniquement). Ce tutoriel est écrit pour OpenSesame 3.1.X, et vous pouvez utiliser la version basée sur Python 2.7 (par défaut) ou Python 3.5. Vous pouvez télécharger OpenSesame ici :

- %link:download%

Lorsque vous démarrez OpenSesame, vous aurez le choix entre des modèles d'expériences et, le cas échéant, une liste d'expériences récemment ouvertes (voir %FigStartUp).

figure :
 id : FigStartUp
 source : start-up.png
 légende : |
   La fenêtre OpenSesame au démarrage.

Le *modèle étendu* offre un bon point de départ pour créer des expériences basées sur Android. Cependant, dans ce tutoriel, nous créerons l'ensemble de l'expérience à partir de zéro. Par conséquent, nous continuerons avec le "modèle par défaut", qui est déjà chargé lorsque OpenSesame est lancé (%FigDefaultTemplate). Fermez simplement les onglets "Get started !" et (si affiché) "Welcome!".

figure :
 id : FigDefaultTemplate
 source : default-template.png
 légende : |
   La structure du modèle "Default template" telle qu'elle apparaît dans la zone d'aperçu.

<div class='info-box' markdown='1'>

**Encadré 1 : Les bases**

Les expériences OpenSesame sont des collections d'éléments. Un élément est un petit morceau de fonctionnalité qui, par exemple, peut être utilisé pour présenter des stimuli visuels (l'élément SKETCHPAD) ou pour enregistrer des pressions de touches (l'élément KEYBOARD_RESPONSE). Les éléments ont un type et un nom. Par exemple, vous pouvez avoir deux éléments du type KEYBOARD_RESPONSE avec les noms *t1_response* et *t2_response*. Pour distinguer clairement les types et les noms d'éléments, nous utiliserons CE_STYLE pour les types et *ce style* pour les noms.

Pour donner une structure à votre expérience, deux types d'éléments sont particulièrement importants : la LOOP et la SEQUENCE. Comprendre comment combiner les LOOPs et les SEQUENCEs pour construire des expériences est peut-être la partie la plus délicate du travail avec OpenSesame, alors abordons ce sujet en premier.

Une LOOP est l'endroit où, dans la plupart des cas, vous définissez vos variables indépendantes. Dans une LOOP, vous pouvez créer un tableau dans lequel chaque colonne correspond à une variable et chaque ligne correspond à une seule exécution de l'élément à exécuter. Pour rendre cela plus concret, considérons le *block_loop* suivant (sans rapport avec ce tutoriel) :

%--
figure :
 id : FigLoopTable
 source : loop-table.png
 légende : |
  Exemple de variables définies dans un tableau de boucle. (Cet exemple n'est pas lié à l'expérience créée dans ce tutoriel. )
--%

Ce *block_loop* exécutera *trial_sequence* quatre fois. Une fois quand `soa` est 100 et `target` est 'F', une fois quand `soa` est 100 et `target` est 'H', etc. L'ordre dans lequel les lignes sont parcourues est aléatoire par défaut, mais peut aussi être réglé en séquence dans le coin supérieur droit de l'onglet.

Une SEQUENCE se compose d'une série d'éléments qui sont exécutés les uns après les autres. Une SEQUENCE prototypique est le *trial_sequence*, qui correspond à un seul essai. Par exemple, une *trial_sequence* basique pourrait consister en un SKETCHPAD, pour présenter un stimulus, un KEYBOARD_RESPONSE, pour recueillir une réponse, et un LOGGER, pour écrire les informations de l'essai dans le fichier journal.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  Un exemple d'un élément SEQUENCE utilisé comme séquence d'essai. (Cet exemple n'est pas lié à l'expérience créée dans ce tutoriel. )
--%

Vous pouvez combiner les LOOPs et les SEQUENCEs de manière hiérarchique, pour créer des blocs d'essais et des phases de pratique et expérimentales. Par exemple, le *trial_sequence* est appelé par le *block_loop*. Ensemble, ceux-ci correspondent à un seul bloc d'essais. Un niveau plus haut, le *block_sequence* est appelé par le *practice_loop*. Ensemble, il s'agit de la phase de pratique de l'expérience.

</div>


### Étape 2 : Ajouter un block_loop et trial_sequence

Le modèle par défaut commence avec trois éléments : un NOTEPAD appelé *getting_started*, un SKETCHPAD appelé *welcome* et une SEQUENCE appelée *experiment*. Nous n'avons pas besoin de *getting_started* et de *welcome*, alors supprimons-les tout de suite. Pour ce faire, faites un clic droit sur ces éléments et sélectionnez "Supprimer". Ne supprimez pas *experiment*, car il s'agit de l'entrée pour l'expérience (c'est-à-dire du premier élément appelé lorsque l'expérience est lancée).

Notre expérience aura une structure très simple. Au sommet de la hiérarchie se trouve une LOOP, que nous appellerons *block_loop*. La *block_loop* est l'endroit où nous définirons nos variables indépendantes (voir également l'encadré 1 sur les antécédents). Pour ajouter une LOOP à votre expérience, faites glisser l'icône LOOP de la barre d'outils des éléments sur l'élément *experiment* de la zone d'aperçu.

Un élément LOOP a besoin d'un autre élément pour fonctionner ; généralement, et dans ce cas également, il s'agit d'une SEQUENCE. Faites glisser l'élément SEQUENCE de la barre d'outils des éléments sur l'élément *new_loop* de la zone d'aperçu. OpenSesame vous demandera si vous souhaitez insérer la SEQUENCE dans ou après la LOOP. Sélectionnez "Insérer dans new_loop".

Par défaut, les éléments ont des noms tels que *new_sequence*, *new_loop*, *new_sequence_2*, etc. Ces noms ne sont pas très informatifs et il est recommandé de les renommer. Les noms des éléments doivent être composés de caractères alphanumériques et/ou de traits de soulignement. Pour renommer un élément, double-cliquez dessus dans la zone d'aperçu. Renommez *new_sequence* en *trial_sequence* pour indiquer qu'il correspondra à un seul essai. Renommez *new_loop* en *block_loop* pour indiquer qu'il correspondra à un bloc d'essais.

La zone d'aperçu de notre expérience ressemble maintenant à celle de %FigStep3.

%--
figure :
 id : FigStep3
 source : step3.png
 légende : |
  La zone d'aperçu à la fin de l'étape 2.
--%

<div class='info-box' markdown='1'>

**Encadré 3 : Éléments inutilisés**

__Tip__ — Les éléments supprimés sont toujours disponibles dans la corbeille des éléments inutilisés, jusqu'à ce que vous sélectionnez "Supprimer définitivement les éléments inutilisés" dans l'onglet des éléments inutilisés. Vous pouvez réajouter les éléments supprimés à votre expérience en les faisant glisser hors de la corbeille des éléments inutilisés dans une SEQUENCE ou une LOOP.

</div>

### Étape 3 : Importer des images et des fichiers audio

Pour cette expérience, nous utiliserons des images de chats, de chiens et de capybaras. Nous utiliserons également des échantillons sonores de miaulements et d'aboiements. Vous pouvez télécharger tous les fichiers nécessaires ici :

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

Téléchargez `stimuli.zip` et extrayez-le quelque part (sur votre bureau, par exemple). Ensuite, dans OpenSesame, cliquez sur le bouton "Afficher le répertoire de fichiers" dans la barre d'outils principale (ou : Menu → Vue → Afficher le répertoire de fichiers). Cela affichera la banque de fichiers, par défaut sur le côté droit de la fenêtre. La manière la plus simple d'ajouter les stimuli à la banque de fichiers est de les faire glisser depuis le bureau (ou l'endroit où vous avez extrait les fichiers) dans la banque de fichiers. Sinon, vous pouvez cliquer sur le bouton '+' dans la banque de fichiers et ajouter des fichiers à l'aide de la boîte de dialogue de sélection de fichiers qui apparaît. La banque de fichiers sera automatiquement enregistrée avec votre expérience.

Une fois que vous avez ajouté tous les stimuli, votre banque de fichiers ressemble à celle de %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  La banque de fichiers à la fin de l'étape 3.
--%

### Étape 4 : Définir les variables expérimentales dans le block_loop

Conceptuellement, notre expérience a un plan croisé complet 3x2 : nous avons trois types de stimuli visuels (chats, chiens et capybaras) qui se produisent en combinaison avec deux types de stimuli auditifs (miaulements et aboiements). Cependant, nous avons cinq exemplaires pour chaque type de stimulus : cinq sons de miaulement, cinq images de capybara, etc. D'un point de vue technique, il est donc logique de traiter notre expérience comme un plan 5×5×3×2, dans lequel le numéro de l'image et le numéro du son sont des facteurs avec cinq niveaux.

OpenSesame est très bon pour générer des plans factoriels complets. Tout d'abord, ouvrez le *block_loop* en cliquant dessus dans la zone d'aperçu. Ensuite, cliquez sur le bouton Design factoriel complet. Cela ouvrira un assistant pour générer des plans factoriels complets, qui fonctionne de manière simple : chaque colonne correspond à une variable expérimentale (c'est-à-dire un facteur). La première ligne est le nom de la variable, les lignes ci-dessous contiennent toutes les valeurs possibles (c'est-à-dire les niveaux). Dans notre cas, nous pouvons spécifier notre plan 5×5×3×2 comme indiqué dans %FigLoopWizard.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  L'assistant de boucle génère des plans factoriels complets.
--%

Après avoir cliqué sur "Ok", vous verrez qu'il y a maintenant une table LOOP avec quatre lignes, une pour chaque variable expérimentale. Il y a 150 cycles (=5×5×3×2), ce qui signifie que nous avons 150 essais uniques. Votre table LOOP ressemble maintenant à celle de %FigStep5.

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
4. Une KEYBOARD_RESPONSE pour recueillir une réponse
5. Un LOGGER pour enregistrer les données dans un fichier

Pour ajouter ces éléments, faites-les simplement glisser un par un depuis la barre d'outils des éléments vers la *trial_sequence*. Si vous déposez accidentellement des éléments au mauvais endroit, vous pouvez simplement les réorganiser en les faisant glisser et en les déposant. Une fois que tous les éléments sont dans le bon ordre, donnez à chacun d'entre eux un nom pertinent. La zone d'aperçu ressemble maintenant à celle de %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  La zone d'aperçu à la fin de l'étape 5.
--%

### Étape 6 : Définir le point de fixation central

Cliquez sur *fixation_dot* dans la zone d'aperçu. Cela ouvre un tableau de dessin de base que vous pouvez utiliser pour concevoir vos stimuli visuels. Pour dessiner un point de fixation central, cliquez d'abord sur l'icône en forme de croix, puis cliquez au centre de l'affichage, c'est-à-dire à la position (0, 0).

Nous devons également préciser combien de temps le point de fixation est visible. Pour ce faire, changez la durée de "keypress" à 495 ms, afin de spécifier une durée de 500 ms. (Voir Background box 4 pour une explication.)

L'élément *fixation_dot* apparaît maintenant comme dans %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: |
  L'élément *fixation_dot* à la fin de l'étape 6.
--%

<div class='info-box' markdown='1'>

**Encadré 4 : Choisir la bonne durée**

Pourquoi spécifier une durée de 495 si nous voulons une durée de 500 ms ? La raison est que la durée réelle de présentation de l'affichage est toujours arrondie à une valeur compatible avec le taux de rafraîchissement de votre écran. Cela peut sembler compliqué, mais pour la plupart des applications, les règles de base suivantes sont suffisantes :

1. Choisissez une durée possible compte tenu du taux de rafraîchissement de votre écran. Par exemple, si le taux de rafraîchissement de votre écran est de 60 Hz, cela signifie que chaque image dure 16,7 ms (=1000 ms/60 Hz). Par conséquent, sur un écran de 60 Hz, vous devez toujours choisir une durée qui est un multiple de 16,7 ms, comme 16,7, 33,3, 50, 100, etc.
2. Dans le champ de durée du SKETCHPAD, spécifiez une durée de quelques millisecondes plus courte que celle que vous visez. Ainsi, si vous voulez présenter un SKETCHPAD pendant 50 ms, choisissez une durée de 45. Si vous voulez présenter un SKETCHPAD pendant 1000 ms, choisissez une durée de 995. Etc.

Pour une discussion détaillée sur le chronométrage expérimental, voir :

- %link:timing%

</div>

### Étape 7 : Définir le son de l'animal

Ouvrez *animal_sound*. L'élément SAMPLER offre un certain nombre d'options, la plus importante étant le fichier son à jouer. Cliquez sur le bouton de navigation pour ouvrir le sélecteur de fichiers et sélectionnez l'un des fichiers audio, comme `bark1.ogg`.

Bien évidemment, nous ne voulons pas jouer le même son encore et encore! Au lieu de cela, nous souhaitons sélectionner un son en fonction des variables `sound` et `sound_nr` que nous avons définies dans le *block_loop* (étape 5). Pour ce faire, remplacez simplement la partie de la chaîne de caractères que vous souhaitez dépendre d'une variable par le nom de cette variable entre crochets. Plus précisément, 'bark1.ogg' devient '[sound][sound_nr].ogg', car nous voulons remplacer 'bark' par la valeur de la variable `sound` et '1' par la valeur de `sound_nr`.

Nous devons également changer la durée de l'échantillonneur. Par défaut, la durée est 'sound', ce qui signifie que l'expérience est en pause pendant la lecture du son. Modifiez la durée pour 0. Cela ne signifie pas que le son sera joué pendant seulement 0 ms, mais que l'expérience passera immédiatement à l'élément suivant, pendant que le son continue de jouer en arrière-plan. L'élément *animal_sound* ressemble maintenant à celui présenté dans %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  L'élément *animal_sound* à la fin de l'étape 7.
--%

<div class='info-box' markdown='1'>

**Encadré 5 : Variables**

Pour plus d'informations sur l'utilisation des variables, consultez :

- %link:manual/variables%

</div>

### Étape 8 : Définir l'image de l'animal

Ouvrez *animal_picture*. Sélectionnez l'outil image en cliquant sur le bouton avec l'icône de paysage. Cliquez au centre (0, 0) de l'affichage. Dans la boîte de dialogue File Pool qui apparaît, sélectionnez `capybara1.png`. Le regard de côté du capybara vous observera paresseusement au centre de l'affichage. Mais bien sûr, nous ne voulons pas toujours montrer le même capybara. Au lieu de cela, nous voulons que l'image dépende des variables `animal` et `pic_nr` que nous avons définies dans le *block_loop* (étape 5).

Nous pouvons utiliser essentiellement la même astuce que pour *animal_sound*, bien que les choses fonctionnement légèrement différemment pour les images. Tout d'abord, faites un clic droit sur le capybara et sélectionnez "Modifier le script". Cela vous permet de modifier la ligne de script OpenSesame correspondant à l'image du capybara :

	draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0

Maintenant, changez le nom du fichier image de 'capybara.png' en '[animal][pic_nr].png' :

	draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0

Cliquez sur "Ok" pour appliquer le changement. Le capybara a disparu, remplacé par une image fantôme, et OpenSesame vous indique qu'un objet n'est pas affiché car il est défini à l'aide de variables. Ne vous inquiétez pas, il sera affiché pendant l'expérience !

Pour rappeler la tâche au participant, ajoutez également deux cercles de réponse, un marqué "chien" sur le côté gauche de l'écran et un marqué "chat" sur le côté droit. Je suis sûr que vous saurez comment faire cela avec les outils de dessin SKETCHPAD. Ma version est présentée dans %FigStep9. Notez que ces cercles de réponse sont purement visuels, et que nous devons encore définir explicitement les critères de réponse (voir l'étape 10).

Enfin, définissez le champ 'Durée' sur '0'. Cela ne signifie pas que l'image est présentée pendant seulement 0 ms, mais que l'expérience passera à l'objet suivant (*réponse*) immédiatement. Comme *réponse* attend une réponse, mais ne change pas ce qui est affiché à l'écran, la cible restera visible jusqu'à ce qu'une réponse soit donnée.

%--
figure:
 id: FigStep9
 source : step9.png
 caption : |
  Le SKETCHPAD *animal_picture* à la fin de l'étape 8.
--%

<div class='info-box' markdown='1'>

**Background box 6: Formats d'image**

__Astuce__ -- OpenSesame peut gérer une grande variété de formats d'image. Cependant, certains formats `.bmp` (non standard) sont connus pour poser problème. Si vous constatez qu'une image `.bmp` n'est pas affichée, vous pouvez envisager d'utiliser un format différent, tel que `.png`. Vous pouvez convertir les images facilement avec des outils gratuits tels que [GIMP].

</div>


### Étape 9: Définir la réponse

Ouvrez l'objet *réponse*. Il s'agit d'un élément KEYBOARD_RESPONSE, qui collecte une seule pression de touche. Il y a quelques options :

- __Réponse correcte__ — passons cela pour le moment ; nous y reviendrons à l'étape 10.
- __Réponses autorisées__ est une liste de touches séparées par des points-virgules qui sont acceptées. Définissons-le sur *left;right* pour indiquer que seules les touches fléchées gauche et droite sont acceptées. (La touche *escape* met en pause l'expérience et est toujours acceptée !)
- __Durée__ indique une durée après laquelle la réponse sera définie sur 'Aucune', et l'expérience se poursuivra. Une durée est importante dans notre expérience, car les participants doivent avoir la possibilité de *ne pas* répondre lorsqu'ils voient un capybara. Fixons donc la durée à 2000.
- __Vider les pressions de touches en attente__ indique que nous devrions seulement accepter les nouvelles pressions de touches. Il est préférable de le laisser activé (il l'est par défaut).

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  Le KEYBOARD_RESPONSE *réponse* à la fin de l'étape 9.
--%


### Étape 10: Définir la réponse correcte

Jusqu'à présent, nous n'avons pas défini de réponse correcte pour chaque essai. Cela se fait en définissant une variable `correct_response`. Vous pouvez le faire soit en créant une colonne `correct_response` dans un tableau LOOP (ici le *block_loop*) et en entrant les réponses correctes manuellement, soit en spécifiant la réponse correcte dans un élément INLINE_SCRIPT Python, ce que nous ferons ici.

Tout d'abord, faites glisser un élément INLINE_SCRIPT depuis la barre d'outils des éléments et insérez-le au début de la *trial_sequence*. (N'oubliez pas de lui donner un nom significatif!) Vous voyez maintenant un éditeur de texte avec deux onglets : un onglet *Run* et un onglet *Prepare*. Vous pouvez saisir du code Python dans les deux onglets, mais ce code est exécuté à différentes phases de l'expérience. La phase *Prepare* est exécutée en premier chaque fois qu'une SEQUENCE est exécutée ; cela donne à tous les éléments de la SEQUENCE la possibilité d'effectuer des opérations longues qui pourraient sinon ralentir l'expérience lors de moments sensibles au temps. Ensuite, la phase *Run* est exécutée ; c'est là que se passe l'action, comme montrer un affichage, collecter une réponse, etc.

Pour plus d'informations, voir :

- %link:prepare-run %

Définir une réponse correcte est un exemple clair de quelque chose qui doit être fait lors de la phase *Prepare*. Le script suivant fera l'affaire:

~~~ .python
if var.animal == 'chien':
	var.correct_response = 'gauche'
elif var.animal == 'chat':
	var.correct_response = 'droite'
elif var.animal == 'capybara':
	var.correct_response = None # Un délai d'attente est codé comme None!
else:
	raise ValueError('Animal invalide : %s' % var.animal)
~~~

Ce code est presque en anglais courant, mais quelques conseils peuvent être utiles :

- Dans le script Python, les variables expérimentales ne sont pas référencées en utilisant des crochets (`[my_variable]`), comme elles le sont ailleurs dans OpenSesame, mais en tant que propriétés de l'objet `var` (c'est-à-dire `var.my_variable`).
- Nous prenons également en compte la possibilité que l'animal ne soit ni un chien, ni un chat, ni un capybara. Bien sûr, cela ne devrait jamais arriver, mais en prenant cette possibilité en compte, nous nous protégeons contre les fautes de frappe et autres bugs. Ceci s'appelle la 'programmation défensive'.


### Étape 11 : Définir le logger

Nous n'avons pas besoin de configurer le LOGGER, car ses paramètres par défaut conviennent; mais regardons-le quand même. Cliquez sur *logger* dans la zone d'aperçu pour l'ouvrir. Vous voyez que l'option 'Log all variables (recommended)' est sélectionnée. Cela signifie qu'OpenSesame enregistre tout, ce qui est bien.

<div class='info-box' markdown='1'>

**Encadré 8 : Vérifiez toujours vos données !**

__Le conseil ultime__ — Vérifiez toujours et encore si toutes les variables nécessaires sont enregistrées dans votre expérience! Le meilleur moyen de vérifier cela est de lancer l'expérience et d'examiner les fichiers journaux résultants.

</div>

### Étape 12: Ajouter un retour d'information par essai

Il est bon de prévenir le participant si la réponse était correcte ou non. Pour éviter de perturber le déroulement de l'expérience, ce type de retour d'information immédiat doit être aussi discret que possible. Ici, nous le ferons en affichant brièvement un point de fixation vert après une réponse correcte, et un point de fixation rouge après une réponse incorrecte.

Tout d'abord, ajoutez deux nouveaux SKETCHPADs à la fin de la *trial_sequence*. Renommez le premier en *feedback_correct* et le second en *feedback_incorrect*. Bien sûr, nous voulons exécuter seulement l'un de ces éléments lors d'un essai donné, en fonction de la réponse correcte ou non. Pour ce faire, nous pouvons utiliser la variable intégrée `correct`, qui a la valeur 0 après une réponse incorrecte et 1 après une réponse correcte. (À condition d'avoir défini `correct_response`, ce que nous avons fait à l'étape 11.) Pour indiquer à la *trial_sequence* que l'élément *feedback_correct* doit être appelé uniquement lorsque la réponse est correcte, nous utilisons la déclaration run-if suivante :

	[correct] = 1

Les crochets autour de `correct` indiquent qu'il s'agit du nom d'une variable, et non simplement de la chaîne 'correct'. De manière analogue, nous utilisons la déclaration run-if suivante pour l'élément *feedback_incorrect*:

	[correct] = 0

Il nous reste à donner du contenu aux éléments *feedback_correct* et *feedback_incorrect*. Pour ce faire, ouvrez simplement les éléments et dessinez un point de fixation vert ou rouge au centre. N'oubliez pas non plus de changer les durées de 'keypress' à un intervalle court, comme 195.

Le *trial_sequence* apparaît maintenant comme indiqué dans %FigStep13.

%--
figure:
 id: FigStep13
 source: step13.png
 caption: |
  Le *trial_sequence* à la fin de l'étape 12.
--%

<div class='info-box' markdown='1'>

**Encadré 9 : Déclarations conditionnelles**

Pour plus d'informations sur les déclarations conditionnelles 'if', voir :

- %link:manual/variables%

</div>

### Étape 13: Ajouter des instructions et des écrans d'au revoir

Une bonne expérience commence toujours par un écran d'instructions et se termine en remerciant le participant pour le temps qu'il a consacré. La manière la plus simple de le faire dans OpenSesame est avec des éléments `form_text_display`.

Faites glisser deux `form_text_display`s dans la SEQUENCE principale *experiment*. L'un doit être au tout début, et renommé en *form_instructions*. L'autre doit être à la toute fin, et renommé en *form_finished*. Maintenant, ajoutez simplement du texte approprié à ces formulaires, par exemple comme indiqué dans %FigStep14.

%--
figure:
 id: FigStep14
 source: step14.png
 caption: |
  L'élément *form_instructions* à la fin de l'étape 13.
--%

<div class='info-box' markdown='1'>

**Encadré 10 : Texte**

__Astuce__ -- Les formulaires et le texte en général, supportent un sous-ensemble de balises HTML pour permettre la mise en forme du texte (c'est-à-dire les couleurs, le gras, etc.). Ceci est décrit ici :

- %link:visual%

</div>

### Étape 15 : Terminé !

Votre expérience est maintenant terminée ! Cliquez sur le bouton "Lancer en plein écran" (`Control+R`) dans la barre d'outils principale pour faire un essai.

<div class='info-box' markdown='1'>

**Encadré 11 : Lancement rapide**

__Astuce__ — Un essai est exécuté encore plus rapidement en cliquant sur le bouton orange "Lancer dans une fenêtre", qui ne vous demande pas comment enregistrer le fichier journal (et ne doit donc être utilisé qu'à des fins de test).

</div>


## Travaux pratiques supplémentaires

Les solutions de ces travaux pratiques supplémentaires se trouvent dans le [fichier d'expérience](http://osf.io/jw7dr).

### Supplément 1 : Ajouter un écran d'instruction et d'au revoir

Conseils :

- SKETCHPAD et FORM_TEXT_DISPLAY peuvent présenter du texte
- Les bonnes instructions sont brèves et concrètes

### Supplément 2 : Analyser les données et vérifier le timing

Conseils :

- Lancez l'expérience une fois sur vous-même
- Ouvrez le fichier de données dans Excel, LibreOffice, ou JASP
- Vous pouvez vérifier le temps de présentation des `sketchpad`s grâce aux variables `time_[nom de l'élément]`.

### Supplément 3 : Diviser les essais en plusieurs blocs

Conseils :

- Utilisez une instruction break-if pour interrompre la boucle après (disons) 15 essais : `([count_trial_sequence]+1) % 15 = 0`
- Ajoutez une nouvelle structure LOOP-SEQUENCE au-dessus de la *block_loop* pour répéter un bloc d'essais plusieurs fois
- Désactivez l'option "Évaluer lors du premier cycle" dans la *block_loop* afin que l'instruction break-if ne soit pas évaluée lorsque la variable `count_trial_sequence` n'existe pas encore
- Activez l'option "Reprendre après la pause" dans la *block_loop* pour échantillonner aléatoirement sans remplacement dans la table LOOP

### Supplément 4 : Ajouter un retour d'information sur la précision et le temps de réponse moyen après chaque bloc

Faites d'abord le supplément 3 !

Conseils :

- Utilisez un élément FEEDBACK pour fournir des informations
- Les variables `acc` et `avg_rt` contiennent la précision et le temps de réaction moyen en cours

### Supplément 5 : Contrebalancer la règle de réponse

Conseils :

- La variable `subject_parity` est 'even' ou 'odd'
- Ceci nécessite un simple INLINE_SCRIPT
- Assurez-vous que les instructions correspondent à la règle de réponse !

## Références

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}

[OpenSesame runtime pour Android]: /getting-opensesame/android
[diapositives]: /attachments/rovereto2014-workshop-slides.pdf
[modulo]: http://fr.wikipedia.org/wiki/Opération_modulo
[pdf]: /rovereto2014/index.pdf
[gimp]: http://www.gimp.org/
[capybara_photo]: https://commons.wikimedia.org/wiki/File:Capybara_Hattiesburg_Zoo_(70909b-58)_2560x1600.jpg