title: Tutoriel débutant : orientation du regard
hash: b28c45b6918382f9501e7777e9058c1aafa95db4fbac25abe0b6db06f88c2a78
locale: fr
language: French

[TOC]

## À propos d'OpenSesame

OpenSesame est un programme pour faciliter le développement d'expériences comportementales en psychologie, neurosciences et économie expérimentale. Pour les débutants, OpenSesame offre une interface graphique complète et point-and-click. Pour les utilisateurs avancés, OpenSesame prend en charge les scripts Python (non couverts dans ce tutoriel).

OpenSesame est disponible gratuitement sous la [Licence publique générale v3][gpl].

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience psychologique simple mais complète en utilisant OpenSesame [(Mathôt, Schreij et Theeuwes, 2012; Mathôt & March, 2022)][references]. Vous utiliserez principalement l'interface utilisateur graphique d'OpenSesame (c'est-à-dire sans codage Python), bien que vous apportiez de petites modifications au script OpenSesame. Ce tutoriel prend environ une heure.

## Ressources

- __Téléchargement__ -- Ce tutoriel suppose que vous exécutez la version 4.0.0 d'OpenSesame ou ultérieure. Pour vérifier la version que vous utilisez, consultez le coin inférieur droit de l'onglet "Commencer" (voir %FigGetStarted). Vous pouvez télécharger la version la plus récente d'OpenSesame depuis:
	- %link:download%
- __Documentation__ -- Un site de documentation dédié est disponible à l'adresse :
	- <http://osdoc.cogsci.nl/>
- __Forum__ -- Un forum d'assistance est disponible à l'adresse :
	- <http://forum.cogsci.nl/>

## L'expérience

Dans ce tutoriel, vous allez créer une expérience de guidage du regard comme indiqué par [Friesen et Kingstone (1998)][references]. Dans cette expérience, un visage est présenté au centre de l'écran (%FigGazeCuing). Ce visage regarde soit à droite, soit à gauche. Une lettre cible (un 'F' ou un 'H') est présentée à gauche ou à droite du visage. Un stimulus distracteur (la lettre 'X') est présenté de l'autre côté du visage. La tâche consiste à indiquer le plus rapidement possible si la lettre cible est un 'F' ou un 'H'. Dans la condition congruente, le visage regarde la cible. Dans la condition incongruente, le visage regarde le distracteur. Comme vous l'avez peut-être deviné, la constatation typique est que les participants répondent plus rapidement dans la condition congruente que dans la condition incongruente, même si la direction du regard n'est pas prédictive de l'emplacement de la cible. Cela montre que notre attention est automatiquement guidée par le regard des autres, même dans des situations où cela ne sert à rien. (Et même quand le visage est juste un smiley!)

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Le paradigme de guidage du regard [(Friesen et Kingstone, 1998)][references] que vous allez mettre en œuvre dans ce tutoriel. Cet exemple représente un essai dans la condition incongruente, car le smiley regarde le distracteur ('X') et non la cible ('F').
--%

L'expérience se compose d'une phase d'entraînement et d'une phase expérimentale. Un retour visuel sera présenté après chaque bloc d'essais. Un son sera joué après chaque réponse incorrecte.

## Conception expérimentale

Cette conception :

- est *intrasujet*, car tous les participants font toutes les conditions
- est *entièrement croisée* (ou factorielle complète), car toutes les combinaisons de conditions se produisent
- a trois facteurs (ou facteurs) :
    - *côté du regard* avec deux niveaux (gauche, droite)
    - *côté cible* avec deux niveaux (gauche, droite)
    - *lettre cible* avec deux niveaux (F, H)
- a N sujets

Voir également %DesignScreencast pour une explication de la logique et de la conception de l'expérience:

%--
video:
 source: youtube
 id: DesignScreencast
 videoid: aWvibRH6D4E
 width: 640
 height: 360
 caption: |
  Une explication de la logique expérimentale et de la conception.
--%

## Étape 1 : Créer la séquence principale

Lorsque vous démarrez OpenSesame, vous voyez l'onglet 'Commencer !' (%FigGetStarted). Une liste de modèles est affichée sous "Démarrer une nouvelle expérience". Ces modèles constituent des points de départ pratiques pour les nouvelles expériences. Une fois que vous avez enregistré une expérience pour la première fois, les expériences récemment ouvertes sont affichées sous "Continuer avec une expérience récente". Au bas de la page, il y a des liens vers la documentation (qui comprend ce tutoriel), le forum de la communauté et une page avec des options de support professionnel (payant). Et bien sûr, un lien où vous pouvez nous acheter une tasse de café pour nous aider à rester éveillé pendant que nous travailons à fournir le meilleur logiciel gratuit !

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  La boîte de dialogue 'Commencer' lors du démarrage d'OpenSesame.
--%

Cliquez sur 'Modèle par défaut' pour commencer avec un modèle expérimental minimal.

Par défaut, il y a une SEQUENCE principale, simplement appelée *experiment*. Cliquez sur *experiment* dans la zone d'aperçu (par défaut sur le côté gauche, voir %FigInterface) pour ouvrir ses commandes dans la zone d'onglets. La SEQUENCE *experiment* est composée de deux éléments : un `notepad` appelé *getting started* et un SKETCHPAD appelé *welcome*.

Nous n'avons pas besoin de ces deux éléments. Supprimez *getting_started* en faisant un clic droit dessus dans la zone d'aperçu et en sélectionnant "Supprimer" (raccourci : `Del`). Supprimez *welcome* de la même manière. La SEQUENCE *experiment* est maintenant vide.

%--
figure:
 id: FigInterface
 source: interface.png
 caption: "La disposition par défaut de l'interface OpenSesame."
--%

<div class='info-box' markdown='1'>

__Encart d'information__

__Noms vs types__ -- Les éléments dans OpenSesame ont un nom et un type. Le nom et le type peuvent être les mêmes, mais ils ne le sont généralement pas. Par exemple, un élément SKETCHPAD peut avoir le nom *my_target_sketchpad*. Pour rendre cette distinction claire, nous utiliserons `monospace` pour indiquer les types d'éléments et *italique* pour indiquer les noms.

__Astuce__ -- Le "Modèle étendu" est un bon point de départ pour de nombreuses expériences. Il contient déjà la structure de base d'une expérience basée sur des essais.

__Astuce__ -- Vous pouvez cliquer sur les icônes d'aide en haut à droite d'un onglet d'élément pour obtenir de l'aide contextuelle.

__Astuce__ -- Enregistrez (raccourci : `Ctrl+S`) votre expérience souvent ! En cas de perte de données malheureuse (et improbable), vous pourrez souvent récupérer votre travail à partir des sauvegardes créées automatiquement, par défaut, toutes les 10 minutes (Menu → Outils → Ouvrir le dossier de sauvegarde).

__Astuce__ -- À moins que vous n'ayez utilisé "Supprimer définitivement" (raccourci : `Shift+Del`), les éléments supprimés sont toujours disponibles dans la corbeille "Éléments inutilisés", jusqu'à ce que vous sélectionniez "Supprimer définitivement les éléments inutilisés" dans l'onglet "Éléments inutilisés". Vous pouvez rajouter les éléments supprimés à une SEQUENCE en les faisant glisser hors de la corbeille "Éléments inutilisés" vers un endroit de votre expérience.

__Astuce__ -- %FigExperimentStructure montre schématiquement la structure de l'expérience que vous allez créer. Si vous êtes perdu pendant le tutoriel, vous pouvez vous référer à %FigExperimentStructure pour voir où vous en êtes.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  Une représentation schématique de la structure de l'expérience "Gaze cuing". Les types d'éléments sont en caractères gras, les noms d'éléments en caractères ordinaires.
--%

</div>

__Ajoutez un élément form_text_display pour l'affichage des instructions__

Comme son nom l'indique, un `form_text_display` est un formulaire qui affiche du texte. Nous allons utiliser un `form_text_display` pour donner des instructions au participant au début de l'expérience.

Cliquez sur *experiment* dans la zone d'aperçu pour ouvrir ses commandes dans la zone d'onglets. Vous verrez une SEQUENCE vide. Faites glisser un `form_text_display` depuis la barre d'outils des éléments (sous "Form", voir %FigInterface) dans la SEQUENCE *experiment* de la zone d'onglets. Lorsque vous relâchez, un nouvel élément `form_text_display` sera inséré dans la SEQUENCE. (Nous y reviendrons à l'étape 12.)

<div class='info-box' markdown='1'>

__Encart d'information__

__Conseil__ -- Vous pouvez faire glisser des éléments dans la zone d'aperçu et dans les onglets SEQUENCE.

__Conseil__ -- Si une action de largage est ambiguë, un menu contextuel vous demandera ce que vous voulez faire.

__Conseil__ -- Un `form_text_display` n'affiche que du texte. Si vous avez besoin d'images, etc., vous pouvez utiliser un élément SKETCHPAD. Nous rencontrerons le SKETCHPAD à l'étape 5.

</div>

__Ajoutez un élément de boucle, contenant un nouvel élément de séquence, pour la phase de pratique__

Nous devons ajouter un élément LOOP à la séquence *experiment*. Nous utiliserons cette boucle pour la phase de pratique de l'expérience. Cliquez sur la séquence *experiment* pour ouvrir ses contrôles dans la zone des onglets.

Faites glisser l'élément LOOP depuis la barre d'outils des éléments dans la séquence, comme vous l'avez fait pour le `form_text_display`. Les nouveaux éléments sont insérés sous l'élément sur lequel ils sont déposés. Par conséquent, si vous déposez la nouvelle boucle sur le `form_text_display` précédemment créé, elle apparaîtra là où vous le voulez : après le `form_text_display`. Mais ne vous inquiétez pas si vous déposez un nouvel élément au mauvais endroit, car vous pouvez toujours réorganiser les choses plus tard.

Un LOOP, en soi, ne fait rien. Un LOOP a toujours besoin d'un autre élément pour fonctionner. Par conséquent, vous devez remplir le nouvel élément LOOP avec un autre élément. (Si vous consultez l'élément LOOP, vous verrez également un avertissement : 'Aucun élément sélectionné'.) Faites glisser un élément SEQUENCE depuis la barre d'outils des éléments sur l'élément LOOP. Un menu contextuel apparaîtra, vous demandant si vous voulez insérer la SEQUENCE après ou dans l'élément LOOP. Sélectionnez "Insérer dans new_loop". (Nous reviendrons sur cette question à l'étape 2.)

<div class = 'info-box' markdown = '1'>

__Boîte d'informations__

__Qu'est-ce qu'un élément LOOP?__ -- Un LOOP est un élément qui ajoute de la structure à votre expérience. Il exécute de manière répétitive un autre élément, généralement une séquence. Un LOOP est également l'endroit où vous définirez habituellement vos variables indépendantes, c'est-à-dire les variables que vous manipulez dans votre expérience.

__Qu'est-ce qu'un élément SEQUENCE?__ -- Un élément SEQUENCE ajoute également de la structure à votre expérience. Comme son nom l'indique, une SEQUENCE exécute plusieurs autres éléments les uns après les autres.

__Structure LOOP-SEQUENCE__ -- Vous voulez souvent répéter une séquence d'événements. Pour ce faire, vous aurez besoin d'un élément LOOP contenant un élément SEQUENCE. Une SEQUENCE, à elle seule, ne se répète pas. Elle commence simplement par le premier élément et se termine par le dernier. En "enveloppant" un élément LOOP autour de la SEQUENCE, vous pouvez répéter la SEQUENCE plusieurs fois. Par exemple, un essai unique correspond généralement à une SEQUENCE unique appelée *trial_sequence*. Un LOOP (souvent appelé *block_loop*) autour de cette *trial_sequence* constituerait alors un seul bloc d'essais. De même, mais à un autre niveau de l'expérience, une SEQUENCE (souvent appelée *block_sequence*) peut contenir un seul bloc d'essais, suivi d'un affichage FEEDBACK. Une boucle *practice_phase* autour de cette séquence "bloc" constituerait alors la phase de pratique de l'expérience. Cela peut sembler un peu abstrait pour l'instant, mais au fur et à mesure que vous suivrez ce tutoriel, vous vous familiariserez avec l'utilisation des LOOPs et des SEQUENCEs.

__Conseil__ -- Pour plus d'informations sur les SEQUENCEs et LOOPs, voir :

- %link:loop%
- %link:sequence%

</div>

__Ajoutez un nouvel élément form_text_display pour le message de fin de la phase de pratique__

Après la phase de pratique, nous voulons informer le participant que la véritable expérience commencera. Pour cela, nous avons besoin d'un autre `form_text_display`. Revenez à la séquence *experiment* et faites glisser un` form_text_display` depuis la barre d'outils des éléments sur l'élément LOOP. Le même menu contextuel apparaîtra qu'auparavant. Cette fois-ci, sélectionnez "Insérer après new_loop". (Nous reviendrons sur cette question à l'étape 12.)

<div class = 'info-box' markdown = '1'>

__Conseil__ -- Ne vous inquiétez pas si vous avez accidentellement changé l'élément à exécuter d'une boucle. Vous pouvez facilement annuler cela en cliquant sur le bouton "Annuler" dans la barre d'outils (`Ctrl+Shift+Z`).

</div>

__Ajoutez un nouvel élément de boucle, contenant la séquence précédemment créée, pour la phase expérimentale__

Nous avons besoin d'un élément LOOP pour la phase expérimentale, tout comme pour la phase de pratique. Par conséquent, faites glisser un LOOP depuis le menu de la barre d'outils des éléments sur * _ form_text_display *.

La nouvelle BOUCLE (appelée *new_loop_1*) est vide et doit être remplie avec une SÉQUENCE, tout comme la BOUCLE que nous avons créée précédemment. Cependant, comme les essais de la phase de pratique et expérimentale sont identiques, ils peuvent utiliser la même SÉQUENCE. Par conséquent, au lieu de faire glisser une nouvelle SEQUENCE à partir de la barre d'outils, vous pouvez réutiliser celle *existante* (c'est-à-dire créer une copie liée).

Pour ce faire, faites un clic droit sur la *new_sequence* précédemment créée et sélectionnez "Copier (lié)". Maintenant, faites un clic droit sur *new_loop_1* et sélectionnez "Coller". Dans le menu contextuel qui apparaît, sélectionnez "Insérer dans new_loop_1".

<div class='info-box' markdown='1'>

__Boîte d'arrière-plan__

__Astuce__ : Il existe une distinction importante entre les copies *liées* et *non liées*. Si vous créez une copie liée d'un élément, vous créez une autre occurrence du même élément. Par conséquent, si vous modifiez l'élément original, la copie liée changera également. En revanche, si vous créez une copie non liée d'un élément, la copie sera initialement identique (sauf pour son nom), mais vous pouvez modifier l'original sans affecter la copie non liée, et vice versa.

</div>

__Ajoutez un nouvel élément form_text_display pour le message d'au revoir__

Lorsque l'expérience est terminée, nous devons dire au revoir au participant. Pour cela, nous avons besoin d'un autre élément `form_text_display`. Revenez à la SÉQUENCE *expérimentale* et faites glisser un `form_text_display` depuis la barre d'outils sur *new_loop_1*. Dans le menu contextuel qui apparaît, sélectionnez "Insérer après new_loop_1" (nous reviendrons à cela à l'étape 12).

__Donnez aux nouveaux éléments des noms significatifs__

Par défaut, les nouveaux éléments ont des noms tels que *new_sequence* et *new_form_text_display_2*. Il est recommandé de donner des noms significatifs aux éléments. Cela facilite grandement la compréhension de la structure de l'expérience. Si vous le souhaitez, vous pouvez également ajouter une description à chaque élément. Les noms des éléments doivent être composés de caractères alphanumériques et/ou de tirets bas.

- Sélectionnez *new_form_text_display* dans la zone d'aperçu, double-cliquez sur son étiquette en haut de la zone des onglets et renommez l'élément *instructions*. (Raccourci zone d'aperçu : `F2`)
- Renommez *new_loop* en *practice_loop*.
- Renommez *new_sequence* en *block_sequence*. Comme vous avez réutilisé cet élément dans *new_loop_1*, le nom change automatiquement là aussi. (Cela illustre pourquoi il est efficace de créer des copies liées chaque fois que cela est possible.)
- Renommez *new_form_text_display_1* en *end_of_practice*.
- Renommez *new_loop_1* en *experimental_loop*.
- Renommez *new_form_text_display_2* en *end_of_experiment*.

__Donnez à toute l'expérience un nom significatif__

L'expérience dans son ensemble a également un titre et une description. Cliquez sur "Nouvelle expérience" dans la zone d'aperçu. Vous pouvez renommer l'expérience de la même manière que vous avez renommé ses éléments. Le titre actuel est "Nouvelle expérience". Renommez l'expérience en "Tutoriel : Gaze cuing". Contrairement aux noms des éléments, le titre de l'expérience peut contenir des espaces, etc.

La zone d'aperçu de votre expérience ressemble maintenant à %FigStep1. Ce serait un bon moment pour sauvegarder votre expérience (raccourci : `Ctrl+S`).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  La zone d'aperçu à la fin de l'étape 1.
--%


## Étape 2 : Créer la séquence de bloc

Cliquez sur *block_sequence* dans l'aperçu. Pour l'instant, cette SEQUENCE est vide. Nous voulons que *block_sequence* se compose d'un bloc d'essais, suivi d'un affichage FEEDBACK. Pour cela, nous devons faire ce qui suit : 

__Ajoutez un élément reset_feedback pour réinitialiser les variables de retour__

Nous ne voulons pas que notre retour soit biaisé par les touches que les participants ont appuyées pendant la phase d'instruction ou les blocs d'essais précédents. Par conséquent, nous commençons chaque bloc d'essais en réinitialisant les variables de retour. Pour ce faire, il nous faut un élément `reset_feedback`. Prenez `reset_feedback` dans la barre d'outils (sous "Collecte de réponses") et faites-le glisser sur *block_sequence*.

__Ajoutez une nouvelle boucle, contenant une nouvelle séquence, pour un bloc d'essais__

Pour une seule essai, nous avons besoin d'une SÉQUENCE. Pour un bloc d'essais, nous devons répéter cette SÉQUENCE plusieurs fois. Par conséquent, pour un bloc d'essais, nous devons entourer une BOUCLE autour d'une SÉQUENCE. Faites glisser une BOUCLE depuis la barre d'outils des éléments sur *new_reset_feedback*. Ensuite, faites glisser une SÉQUENCE depuis la barre d'outils des éléments sur la BOUCLE nouvellement créée, et sélectionnez 'Insérer dans new_loop' dans le menu contextuel qui apparaît. (Nous reviendrons sur ce point à l'étape 3.)

__Ajoutez un élément de feedback__

Après chaque bloc d'essais, nous voulons donner un retour d'information au participant, afin qu'il sache comment il/elle se débrouille. Pour cela, nous avons besoin d'un élément FEEDBACK. Faites glisser un FEEDBACK depuis la barre d'outils des éléments sur *new_loop*, et sélectionnez 'Insérer après la boucle' dans le menu contextuel qui apparaît. (Nous reviendrons sur ce point à l'étape 10.)

__Donnez des noms logiques aux nouveaux éléments__

Renommez : (Voir l'étape 1 si vous ne vous souvenez pas comment faire.)

- *new_loop* en *block_loop*
- *new_sequence* en *trial_sequence*
- *new_reset_feedback* en *reset_feedback*
- *new_feedback* en *feedback*

L'aperçu de votre expérience ressemble maintenant à %FigStep2. N'oubliez pas d'enregistrer régulièrement votre expérience.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  La zone d'aperçu à la fin de l'étape 2.
--%

## Étape 3 : Remplir la boucle de blocs avec des variables indépendantes

Comme son nom l'indique, *block_loop* correspond à un seul bloc d'essais. Dans l'étape précédente, nous avons créé le *block_loop*, mais nous devons encore définir les variables indépendantes qui seront modifiées à l'intérieur du bloc. Notre expérience a trois variables indépendantes :

- __gaze_cue__ peut être 'gauche' ou 'droite'.
- __target_pos__ (la position de la cible) peut être '-300' ou '300'. Ces valeurs reflètent l'abscisse X de la cible en pixels (0 = centre). Utiliser les coordonnées directement, plutôt que 'gauche' et 'droite', sera pratique lorsque nous créerons les affichages cibles (voir étape 5).
- __target_letter__ (la lettre cible) peut être 'F' ou 'H'.

Par conséquent, notre expérience a 2 x 2 x 2 = 8 niveaux. Bien que 8 niveaux ne soit pas si élevé (la plupart des expériences en auront plus), nous n'avons pas besoin de saisir toutes les combinaisons possibles manuellement. Cliquez sur *block_loop* dans l'aperçu pour ouvrir son onglet. Cliquez maintenant sur le bouton 'Plan factoriel complet'. Dans l'assistant des variables, vous définissez simplement toutes les variables en tapant le nom dans la première rangée et les niveaux dans les rangées sous le nom (voir %FigVariableWizard). Si vous sélectionnez 'Ok', vous verrez que *block_loop* a été rempli avec les 8 combinaisons possibles.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  L'assistant des variables de boucle à l'étape 3.
--%

Dans le tableau des boucles résultant, chaque ligne correspond à une exécution de *trial_sequence*. Comme, dans notre cas, une exécution de *trial_sequence* correspond à un essai, chaque ligne de notre tableau de boucle correspond à un essai. Chaque colonne correspond à une variable, qui peut avoir une valeur différente à chaque essai.

Mais nous n'avons pas encore terminé. Nous devons ajouter trois autres variables : l'emplacement du distractor, la réponse correcte et la congruence.

- __dist_pos__ -- Sur la première ligne de la première colonne vide, saisissez 'dist_pos'. Cela ajoute automatiquement une nouvelle variable expérimentale nommée 'dist_pos'. Dans les lignes ci-dessous, saisissez '300' lorsque 'target_pos' est -300, et '-300' lorsque 'target_pos' est 300. En d'autres termes, la cible et le distracteur doivent être positionnés à l'opposé l'un de l'autre.
- __correct_response__ -- Créez une autre variable, dans une autre colonne vide, avec le nom 'correct_response'. Définissez 'correct_response' sur 'z' lorsque 'target_letter' est 'F', et sur 'm' lorsque 'target_letter' est 'H'. Cela signifie que le participant doit appuyer sur la touche 'z' s'il voit un 'F' et sur la touche 'm' s'il voit un 'H'. (N'hésitez pas à choisir d'autres touches si 'z' et 'm' sont gênantes sur la disposition de votre clavier; par exemple, 'w' et 'n' sont meilleures sur les claviers AZERTY.)
- __congruency__ -- Créez une autre variable avec le nom 'congruency'. Définissez 'congruency' sur 'congruent' lorsque 'target_pos' est '-300' et 'gaze_cue' est 'left', et lorsque 'target_pos' est '300' et 'gaze_cue' est 'right'. En d'autres termes, un essai est congruent si le visage regarde la cible. Définissez 'congruency' sur 'incronguent' pour les essais où le visage regarde le distracteur. La variable 'congruency' n'est pas nécessaire pour exécuter l'expérience; cependant, elle est utile pour analyser les données ultérieurement.

Nous devons faire encore une dernière chose. 'Repeat' est actuellement défini sur '1.00'. Cela signifie que chaque cycle sera exécuté une fois. Le bloc est donc composé de 8 essais, ce qui est un peu court. Une longueur raisonnable pour un bloc d'essais est de 24, donc définissez 'Repeat' sur 3.00 (3 répétitions x 8 cycles = 24 essais). Vous n'avez pas besoin de changer 'Order', car 'random' est exactement ce que nous voulons.

Le *block_loop* ressemble maintenant à %FigStep3. N'oubliez pas d'enregistrer régulièrement votre expérience.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "Le *block_loop* à la fin de l'étape 3."
--%

<div class='info-box' markdown='1'>

__Encadré__

__Astuce__ -- Vous pouvez préparer votre tableau de boucle dans votre programme de tableur préféré et le copier-coller dans le tableau des variables LOOP.

__Astuce__ -- Vous pouvez spécifier votre tableau de boucle dans un fichier séparé (au format `.xlsx` ou `.csv`) et utiliser ce fichier directement. Pour ce faire, sélectionnez 'file' sous 'Source'.

__Astuce__ -- Vous pouvez définir 'Repeat' avec un nombre non entier. Par exemple, en définissant 'Repeat' sur '0.5', seuls la moitié des essais (sélectionnés au hasard) sont exécutés.

</div>

## Étape 4 : Ajoutez des images et des fichiers sonores à la pool de fichiers

Pour nos stimuli, nous utiliserons des images provenant de fichiers. De plus, nous jouerons un son si le participant commet une erreur. Pour cela, nous avons besoin d'un fichier sonore.

Vous pouvez télécharger les fichiers requis ici (dans la plupart des navigateurs, vous pouvez cliquer avec le bouton droit sur les liens et choisir 'Enregistrer le lien sous' ou une option similaire) :

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Une fois que vous avez téléchargé ces fichiers (sur votre bureau, par exemple), vous pouvez les ajouter à la pool de fichiers. Si la pool de fichiers n'est pas déjà visible (par défaut à droite de la fenêtre), cliquez sur le bouton 'Afficher la pool de fichiers' dans la barre d'outils principale (raccourci : `Ctrl+P`). La manière la plus simple d'ajouter les quatre fichiers à la pool de fichiers est de les faire glisser du bureau (ou de l'endroit où vous les avez téléchargés) dans la pool de fichiers. Vous pouvez également cliquer sur le bouton '+' dans la pool de fichiers et ajouter des fichiers en utilisant la boîte de dialogue de sélection de fichiers qui apparaît. La pool de fichiers sera enregistrée automatiquement avec votre expérience.

Votre pool de fichiers ressemble maintenant à %FigStep4. N'oubliez pas d'enregistrer régulièrement votre expérience.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "La pool de fichiers à la fin de l'étape 4."
--%

## Étape 5 : Remplissez la séquence d'essai avec des éléments

Un essai dans notre expérience se présente comme suit :

1. __Point de fixation__ -- 750 ms, élément SKETCHPAD
2. __Regard neutre__ -- 750 ms, élément SKETCHPAD
3. __Indice de regard__ -- 500 ms, élément SKETCHPAD
4. __Cible__ -- 0 ms, élément SKETCHPAD
5. __Collecte de réponse__ -- élément KEYBOARD_RESPONSE
6. __Jouer un son si la réponse est incorrecte__ -- élément SAMPLER
7. __Enregistrer la réponse dans un fichier__ -- élément LOGGER

Cliquez sur *trial_sequence* dans l'aperçu pour ouvrir l'onglet *trial_sequence*. Prenez un SKETCHPAD dans la barre d'outils des éléments et faites-le glisser dans le *trial_sequence*. Répétez cette opération trois fois de plus, de sorte que *trial_sequence* contienne quatre SKETCHPADs. Ensuite, sélectionnez et ajoutez un élément KEYBOARD_RESPONSE, un élément SAMPLER et un élément LOGGER.

De nouveau, nous allons renommer les nouveaux éléments, pour nous assurer que le *trial_sequence* est facile à comprendre. Renommez :

- *new_sketchpad* en *fixation_dot*
- *new_sketchpad_1* en *neutral_gaze*
- *new_sketchpad_2* en *gaze_cue*
- *new_sketchpad_3* en *target*
- *new_keyboard_response* en *keyboard_response*
- *new_sampler* en *incorrect_sound*
- *new_logger* en *logger*

Par défaut, les éléments sont toujours exécutés, ce qui est indiqué par l'expression run-if `True`. Cependant, nous voulons changer cela pour l'élément *incorrect_sound*, qui ne doit être exécuté que si une erreur a été commise. Pour ce faire, il faut modifier l'expression "Run if" en `correct == 0` dans l'onglet *trial_sequence*. Ceci fonctionne, car l'élément *keyboard_response* crée automatiquement une variable `correct`, qui est définie à `1` (correct), `0` (incorrect) ou `undefined` (cela repose sur la variable `correct_response` définie à l'étape 3). Le double signe égal est la syntaxe Python et indique que vous voulez comparer si les deux choses sont égales entre elles, dans ce cas si la variable `correct` est égale à 0. Pour modifier une expression run-if, double-cliquez dessus (raccourci : `F3`).

Le *trial_sequence* ressemble maintenant à %FigStep5.

%--
figure :
 id: FigStep5
 source: step5.png
 caption: "Le *trial_sequence* à la fin de l'étape 5."
--%

<div class='info-box' markdown='1'>

__Encadré__

__Qu'est-ce qu'un élément SKETCHPAD ?__ -- Un SKETCHPAD est utilisé pour présenter des stimuli visuels : texte, formes géométriques, points de fixation, patchs Gabor, etc. Vous pouvez dessiner sur le SKETCHPAD en utilisant les outils de dessin intégrés.

__Qu'est-ce qu'un élément KEYBOARD_RESPONSE ?__ -- Un élément KEYBOARD_RESPONSE recueille une seule réponse du participant à partir du clavier.

__Qu'est-ce qu'un élément SAMPLER ?__ -- Un élément SAMPLER lit un son à partir d'un fichier son.

__Qu'est-ce qu'un élément LOGGER ?__ -- Un élément LOGGER écrit des données dans le fichier de journalisation. C'est très important : si vous oubliez d'inclure un élément LOGGER, aucune donnée ne sera enregistrée pendant l'expérience !

__Astuce__ -- Les variables et les expressions conditionnelles "if" sont très puissantes ! Pour en savoir plus sur elles, consultez:

- %link:manual/variables%

</div>

## Étape 6 : Dessiner les éléments sketchpad

Les éléments SKETCHPAD que nous avons créés à l'étape 5 sont toujours vides. Il est temps de faire quelques dessins !

__Définir la couleur d'arrière-plan en blanc__

Cliquez sur *fixation_dot* dans la zone d'aperçu pour ouvrir son onglet. Le SKETCHPAD est toujours gris foncé, alors que les images que nous avons téléchargées ont un fond blanc. Oups, nous avons oublié de définir la couleur d'arrière-plan de l'expérience en blanc (elle est gris foncé par défaut) ! Cliquez sur 'Tutoriel : Gaze cuing' dans la zone d'aperçu pour ouvrir l'onglet 'Propriétés générales'. Changez 'Avant-plan' en 'noir' et 'Arrière-plan' en 'blanc'.

<div class='info-box' markdown='1'>

__Encadré__

__Astuce__ -- Pour un contrôle plus précis des couleurs, vous pouvez également utiliser la notation hexadécimale RVB (par exemple, `#FF000` pour le rouge), utiliser différents espaces colorimétriques ou utiliser l'outil sélecteur de couleurs. Voir aussi :

- %link:manual/python/canvas%

</div>

__Dessinez le point de fixation__

Revenez au *fixation_dot* en cliquant sur *fixation_dot* dans l'aperçu. Sélectionnez maintenant l'élément du point de fixation en cliquant sur le bouton avec la croix. Si vous déplacez votre curseur sur le sketchpad, vous pouvez voir les coordonnées de l'écran en haut à droite. Définissez la couleur (de premier plan) sur 'noir'. Cliquez au centre de l'écran (0, 0) pour dessiner un point de fixation central.

Enfin, changez le champ 'Durée' de 'keypress' à '745', car nous voulons que le point de fixation soit présenté pendant 750 ms. Attendez... *pourquoi n'avons-nous pas simplement spécifié une durée de 750 ms?* La raison en est que la durée réelle de présentation de l'affichage est toujours arrondie à une valeur compatible avec le taux de rafraîchissement de votre écran. Cela peut paraître compliqué, mais pour la plupart des utilisations, les règles de base suivantes sont suffisantes:

1. Choisissez une durée qui est possible étant donné le taux de rafraîchissement de votre écran. Par exemple, si le taux de rafraîchissement de votre écran est de 60 Hz, cela signifie que chaque image dure 16,7 ms (= 1000 ms / 60 Hz). Par conséquent, sur un écran de 60 Hz, vous devez toujours choisir une durée qui est un multiple de 16,7 ms, comme 16,7, 33,3, 50, 100, etc.
2. Dans le champ de durée du SKETCHPAD, indiquez une durée de quelques millisecondes de moins que ce que vous visez. Ainsi, si vous souhaitez présenter un SKETCHPAD pendant 50 ms, choisissez une durée de 45. Si vous voulez présenter un SKETCHPAD pendant 1000 ms, choisissez une durée de 995. Etc.

<div class='info-box' markdown='1'>

__Boîte d'informations__

__Astuce__ - Pour une discussion détaillée sur le chronométrage expérimental, consultez:

- %link:timing%

__Astuce__ - La durée d'un SKETCHPAD peut être une valeur en millisecondes, mais vous pouvez également saisir 'keypress' ou 'mouseclick' pour collecter une pression sur une touche ou un clic de souris respectivement. Dans ce cas, un SKETCHPAD fonctionnera de manière très similaire à un élément KEYBOARD_RESPONSE (mais avec moins d'options).

__Astuce__ - Assurez-vous que la couleur (de premier plan) est réglée sur noir. Sinon, vous dessinerez en blanc sur blanc et vous ne verrez rien !

</div>

__Dessinez le regard neutre__

Ouvrez le SKETCHPAD *neutral_gaze*. Sélectionnez maintenant l'outil image en cliquant sur le bouton avec l'icône de paysage montagneux. Cliquez au centre de l'écran (0, 0). La boîte de dialogue 'Sélectionner un fichier dans la base' apparaîtra. Sélectionnez le fichier `gaze_neutral.png` et cliquez sur le bouton 'Sélectionner'. L'image du regard neutre vous fixera maintenant depuis le centre de l'écran ! Enfin, comme précédemment, changez le champ 'Durée' de 'keypress' à '745'. (Et notez à nouveau que cela signifie une durée de 750 ms sur la plupart des écrans!)

<div class='info-box' markdown='1'>

__Boîte d'informations__

__Astuce__ - OpenSesame peut gérer une grande variété de formats d'image. Cependant, certains formats `.bmp` (non standard) sont connus pour causer des problèmes. Si vous constatez qu'une image `.bmp` n'est pas affichée, vous pouvez la convertir en un format différent, tel que `.png`. Vous pouvez facilement convertir des images avec des outils gratuits tels que [GIMP].
</div>

__Dessinez le repère du regard__

Ouvrez le SKETCHPAD *gaze_cue* et sélectionnez à nouveau l'outil image. Cliquez au centre de l'écran (0, 0) et sélectionnez le fichier `gaze_left.png`.

Mais nous n'avons pas encore terminé! Parce que le repère du regard ne doit pas toujours être 'à gauche', mais doit dépendre de la variable `gaze_cue`, que nous avons définie à l'étape 3. Cependant, en dessinant l'image `gaze_left.png` sur le SKETCHPAD, nous avons généré un script qui nécessite seulement une petite modification pour s'assurer que l'image appropriée est affichée. Cliquez sur le bouton 'Sélectionner la vue' en haut à droite de l'onglet *gaze_cue* et sélectionnez 'Voir le script'. Vous verrez maintenant le script qui correspond au sketchpad que nous venons de créer:

~~~ .python
set duration keypress
set description "Affiche les stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

La seule chose que nous devons faire est de remplacer `gaze_left.png` par `gaze_{gaze_cue}.png`. Cela signifie qu'OpenSesame utilise la variable `gaze_cue` (qui a les valeurs `left` et `right`) pour déterminer quelle image doit être affichée.

Tant qu'à faire, nous pourrions aussi changer la durée à '495' (arrondi à 500 !). Le script ressemble maintenant à ceci :

~~~ .python
set duration 495
set description "Affiche les stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Cliquez sur le bouton 'Appliquer' en haut à droite pour appliquer vos modifications au script et revenir aux contrôles d'éléments normaux. OpenSesame vous avertira que l'image ne peut être affichée, car elle est définie à l'aide de variables, et une image substitut sera affichée à la place. Ne vous inquiétez pas, l'image correcte sera affichée pendant l'expérience !

<div class='info-box' markdown='1'>

__Boîte d'informations__

__Astuce__ -- L'inspecteur de variables (raccourci : `Ctrl+I`) est un moyen puissant de découvrir quelles variables ont été définies dans votre expérience et quelles valeurs elles ont (voir %FigVariableInspector). Lorsque votre expérience ne fonctionne pas, la plupart des variables n'ont pas encore de valeur. Mais lorsque vous exécutez votre expérience dans une fenêtre, tout en ayant l'inspecteur de variables visible, vous pouvez voir les variables changer en temps réel. Cela est très utile pour déboguer votre expérience.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "L'inspecteur de variables est un moyen pratique d'avoir un aperçu des variables qui existent dans votre expérience."
--%

</div>

__Dessiner la cible__

Nous voulons que trois objets fassent partie de l'affichage de la cible : la lettre cible, la lettre distractrice et l'indice de regard (voir %FigGazeCuing). Comme auparavant, nous commencerons par créer un affichage statique à l'aide de l'éditeur SKETCHPAD. Ensuite, nous n'aurons besoin d'apporter que de légères modifications au script pour que l'affichage exact dépende des variables.

Cliquez sur *target* dans l'aperçu pour ouvrir l'onglet cible et, comme avant, dessinez l'image `gaze_left.png` au centre de l'écran. Sélectionnez maintenant l'outil de dessin de texte en cliquant sur le bouton avec l'icône 'A'. Changez la couleur de premier plan en 'noir' (si ce n'est pas déjà le cas). La taille de la police par défaut est de 18 px, ce qui est un peu petit pour notre objectif, alors changez la taille de la police à 32 px. Maintenant, cliquez sur (-320, 0) dans le SKETCHPAD (la coordonnée X n'a pas besoin d'être exactement 320, puisque nous la changerons de toute façon en variable). Entrez "{target_letter}" dans la boîte de dialogue qui apparaît, pour dessiner la lettre cible (lorsque vous dessinez du texte, vous pouvez utiliser directement les variables). De même, cliquez sur (320, 0) et dessinez un 'X' (le distracteur est toujours un 'X').

Ouvrez maintenant l'éditeur de script en cliquant sur le bouton "Sélectionner la vue" en haut à droite de l'onglet et en sélectionnant "Voir le script". Le script ressemble à ceci :

~~~ .python
set duration keypress
set duration keypress
set description "Affiche les stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

Comme précédemment, changez `gaze_left.png` en `gaze_{gaze_cue}.png`. Nous devons également faire en sorte que la position de la cible et du distracteur dépende des variables `target_pos` et `dist_pos` respectivement. Pour ce faire, changez simplement `-320` en `{target_pos}` et `320` en `{dist_pos}`. Assurez-vous de laisser le `0`, qui est la coordonnée Y. Le script ressemble maintenant à ceci :

~~~ .python
set duration keypress
set description "Affiche les stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

Cliquez sur le bouton "Appliquer" pour appliquer le script et revenir aux contrôles d'éléments normaux.

Enfin, réglez le champ 'Duration' sur '0'. Cela ne signifie pas que la cible est présentée pour seulement 0 ms, mais que l'expérience passera à l'élément suivant (le *keyboard_response*) immédiatement. Comme le *keyboard_response* attend une réponse, mais ne change pas ce qui est affiché à l'écran, la cible restera visible jusqu'à ce qu'une réponse soit donnée.

N'oubliez pas d'enregistrer régulièrement votre expérience.

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Chaque élément d'un SKETCHPAD a une option 'Show if', qui spécifie quand l'élément doit être affiché. Vous pouvez utiliser cela pour masquer / afficher des éléments d'un SKETCHPAD en fonction de certaines variables, de manière similaire aux déclarations run-if dans une SEQUENCE.

__Astuce__ -- Assurez-vous que la couleur (de premier plan) est réglée sur noir. Sinon, vous dessinerez en blanc sur blanc et vous ne verrez rien!

</div>

## Étape 7: Configurer l'élément de réponse au clavier

Cliquez sur *keyboard_response* dans l'aperçu pour ouvrir son onglet. Vous voyez trois options: Correct response, Allowed responses, Timeout et Event type.

Nous avons déjà défini la variable `correct_response` à l'étape 3. Sauf si nous spécifions explicitement une réponse correcte, OpenSesame utilise automatiquement la variable `correct_response` si elle est disponible. Par conséquent, nous n'avons pas besoin de modifier le champ 'Correct response' ici.

Nous devons définir les réponses autorisées. Entrez 'z;m' dans le champ allowed-responses (ou d'autres touches si vous avez choisi des touches de réponse différentes). Le point-virgule est utilisé pour séparer les réponses. Le KEYBOARD_RESPONSE n'accepte désormais que les touches 'z' et 'm'. Toutes les autres pressions de touches sont ignorées, à l'exception de 'échap', qui met l'expérience en pause.

Nous voulons également définir un délai d'attente, qui est l'intervalle maximum que le KEYBOARD_RESPONSE attend avant de décider que la réponse est incorrecte et de régler la variable 'response' sur 'Aucune'. '2000' (ms) est une bonne valeur.

Nous n'avons pas besoin de modifier le type d'événement, car nous voulons que le participant réponde en appuyant sur une touche (keypress, par défaut) et non en relâchant une touche (keyrelease).

Le KEYBOARD_RESPONSE ressemble maintenant à %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "Le KEYBOARD_RESPONSE à la fin de l'étape 7."
--%

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Par défaut, le KEYBOARD_RESPONSE utilise la variable `correct_response` pour déterminer si une réponse était correcte. Mais vous pouvez utiliser une variable différente également. Pour ce faire, entrez un nom de variable entre crochets (`{my_variable}`) dans le champ correct response.

__Astuce__ -- Si 'flush pending key presses' est activé (c'est le cas par défaut), toutes les pressions de touches en attente sont supprimées lorsque l'élément KEYBOARD_RESPONSE est appelé. Cela évite les effets de report, qui pourraient sinon se produire si le participant appuie accidentellement sur une touche pendant une partie non responsive du procès.

__Astuce__ -- Pour utiliser des touches spéciales, comme '/' ou la touche flèche vers le haut, vous pouvez utiliser des noms de touches (par exemple 'up' et 'space') ou des caractères associés (par exemple '/' et ']'). Le bouton 'List available keys' fournit un aperçu de tous les noms de touches valides.

</div>

## Étape 8: Configurer l'élément incorrect (sampler)

L'élément *incorrect_sound* ne nécessite pas beaucoup de travail: nous devons seulement sélectionner le son qui doit être joué. Cliquez sur *incorrect_sound* dans l'aperçu pour ouvrir son onglet. Cliquez sur le bouton 'Parcourir' et sélectionnez `incorrect.ogg` dans le fichier pool.

Le sampler ressemble maintenant à %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "L'élément *incorrect_sound* à la fin de l'étape 8."
--%

<div class='info-box' markdown='1'>

__ Boîte d'information__

__Astuce__ -- Vous pouvez utiliser des variables pour spécifier quel son doit être joué en utilisant un nom de variable entre crochets en tant que (partie de) nom de fichier. Par exemple: `{a_word}.ogg`

__Astuce__ -- Le SAMPLER gère les fichiers aux formats `.ogg`, `.mp3` et `.wav`. Si vous avez des fichiers audio dans un autre format, [Audacity] est un excellent outil gratuit pour convertir les fichiers audio (et bien plus).

</div>

## Étape 9 : Configurer le variable LOGGER

En réalité, nous n'avons pas besoin de configurer le LOGGER variable, mais jetons-y un coup d'œil quand même. Cliquez sur *logger* dans l'aperçu pour ouvrir son onglet. Vous voyez que l'option "Enregistrer automatiquement toutes les variables" est sélectionnée. Cela signifie qu'OpenSesame enregistre tout, ce qui est très bien.

<div class='info-box' markdown='1'>

__Background box__

__Conseil__ - Si vous aimez avoir des fichiers de journalisation propres, vous pouvez désactiver l'option "Enregistrer automatiquement toutes les variables" et sélectionner manuellement les variables, soit en entrant manuellement les noms des variables ("Ajouter une variable personnalisée"), soit en faisant glisser les variables à partir de l'inspecteur de variables dans le tableau LOGGER. Vous pouvez également laisser l'option "Enregistrer automatiquement toutes les variables" activée et exclure les variables qui ne vous intéressent pas.

__The one tip to rule them all__ -- Vérifiez toujours trois fois si toutes les variables nécessaires sont enregistrées dans votre expérience ! La meilleure façon de vérifier cela est de lancer l'expérience et d'analyser les fichiers de journalisation résultants.

</div>

## Étape 10 : Dessiner l'élément de feedback

Après chaque bloc d'essais, nous voulons présenter un feedback au participant pour le/la informer de sa performance. C'est pourquoi, à l'étape 2, nous avons ajouté un élément FEEDBACK, simplement nommé *feedback* à la fin de *block_sequence*.

Cliquez sur *feedback* dans l'aperçu pour ouvrir son onglet, sélectionnez l'outil de dessin de texte, changez la couleur d'avant-plan en 'noir' (si ce n'est pas déjà fait), et cliquez à (0, 0). Entrez maintenant le texte suivant :

```text
Fin du bloc

Votre temps de réponse moyen était de {avg_rt} ms
Votre précision était de {acc} %

Appuyez sur n'importe quelle touche pour continuer
```

Puisque nous voulons que l'élément de feedback reste visible aussi longtemps que le participant le souhaite (c'est-à-dire jusqu'à ce qu'il/elle appuie sur une touche), nous laissons le champ "Durée" défini sur "touche enfoncée".

L'élément de feedback ressemble maintenant à %FigStep_10.

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "L'élément de feedback à la fin de l'étape 10."
--%

<div class='info-box' markdown='1'>

__Background box__

__Qu'est-ce qu'un élément de feedback ?__ - Un élément FEEDBACK est presque identique à un élément SKETCHPAD. La seule différence est qu'un élément FEEDBACK n'est pas préparé à l'avance. Cela signifie que vous pouvez l'utiliser pour présenter un feedback, qui nécessite des informations à jour sur la réponse d'un participant. Vous ne devez pas utiliser d'éléments FEEDBACK pour présenter des affichages sensibles au temps, car le fait qu'ils ne soient pas préparés à l'avance signifie que leurs propriétés de synchronisation ne sont pas aussi bonnes que celles de l'élément SKETCHPAD. Voir aussi:

- %link:visual%

__Feedback et variables__ - Les éléments de réponse suivent automatiquement la précision et le temps de réponse moyen du participant dans les variables 'acc' (synonyme : 'accuracy') et 'avg_rt' (synonyme : 'average_response_time') respectivement. Voir aussi :

- %link:manual/variables%

__Conseil__ - Assurez-vous que la couleur (de premier plan) est réglée sur noir. Sinon, vous dessinerez du blanc sur du blanc et vous ne verrez rien !

</div>

## Étape 11 : Définir la durée de la phase de pratique et de la phase expérimentale

Nous avons précédemment créé les éléments *practice_loop* et *experiment_loop*, qui appellent tous deux *block_sequence* (c'est-à-dire un bloc d'essais). Cependant, pour l'instant, ils n'appellent *block_sequence* qu'une seule fois, ce qui signifie que la phase de pratique et la phase expérimentale ne comportent qu'un seul bloc d'essais chacune.

Cliquez sur *practice_loop* pour ouvrir son onglet et définissez "Répéter" sur "2.00". Cela signifie que la phase de pratique se compose de deux blocs.

Cliquez sur *experimental_loop* pour ouvrir son onglet et définissez "Répéter" sur "8.00". Cela signifie que la phase expérimentale se compose de huit blocs.

<div class='info-box' markdown='1'>

__Background box__

__Conseil__ -- Vous pouvez créer une variable `practice` dans *practice_loop* et *experimental_loop* et la définir respectivement sur 'yes' et 'no'. C'est un moyen facile de garder une trace des essais qui faisaient partie de la phase de pratique.

</div>

## Étape 12 : Rédiger les formulaires d'instruction, de fin de pratique et de fin d'expérience

Je pense que vous pouvez gérer cette étape vous-même ! Ouvrez simplement les éléments appropriés et ajoutez du texte pour présenter les instructions, un message de fin de pratique et un message de fin d'expérience.

<div class='info-box' markdown='1'>

__Boîte d'arrière-plan__

__Astuce__ -- Vous pouvez utiliser un sous-ensemble de balises HTML pour formater votre texte. Par exemple, *&lt;b&gt;ceci sera en gras&lt;b&gt;* et *&lt;span color='red'&gt;ceci sera en rouge&lt;span&gt;*. Pour plus d'informations, consultez :

- %link:text%

</div>

## Étape 13 : Exécuter l'expérience !

C'est terminé ! Cliquez sur les boutons 'Exécuter dans une fenêtre' (raccourci : `Ctrl+W`) ou 'Exécuter en plein écran' (raccourci : `Ctrl+R`) dans la barre d'outils pour lancer votre expérience.

<div class='info-box' markdown='1'>

__Boîte d'arrière-plan__

__Astuce__ -- Un test est exécuté encore plus rapidement en cliquant sur le bouton orange 'Exécuter dans une fenêtre' (raccourci : `Ctrl+Shift+W`), qui ne vous demande pas comment enregistrer le fichier journal (et doit donc être utilisé uniquement à des fins de test).

</div>


## Comprendre les erreurs

Être capable de comprendre les messages d'erreur est une compétence essentielle lorsqu'on travaille avec OpenSeame. Après tout, une expérience nouvellement construite fonctionne rarement immédiatement sans erreur !

Supposons que nous ayons fait une erreur lors de l'une des étapes ci-dessus. Lorsque nous essayons d'exécuter l'expérience, nous obtenons le message d'erreur suivant (%FigErrorMessage) :

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "Un message d'erreur dans OpenSesame."
--%

Le message d'erreur commence par un nom, dans ce cas `FStringError`, qui indique le type général d'erreur. Il est suivi d'un court texte explicatif, dans ce cas "Échec de l'évaluation de l'expression f-string dans le texte suivant : gaze_{gaze_ceu}.png". Même sans comprendre ce qu'est une f-string (c'est une chaîne de caractères qui contient du code Python entre accolades), il est clair qu'il y a un problème avec le texte '{gaze_ceu}.png'.

Le message d'erreur indique également que l'erreur provient de la phase de préparation de l'élément *gaze_cue*.

Enfin, le message d'erreur indique ce qui s'est mal passé lors de l'évaluation du texte 'gaze_{gaze_ceu}.png' : le nom 'gaze_ceu' n'est pas défini.

En lisant attentivement le message d'erreur, la cause et la solution vous sont probablement déjà venues à l'esprit : nous avons fait une simple faute de frappe dans l'élément *gaze_cue*, en écrivant '{gaze_ceu}' au lieu de '{gaze_cue}' ! Et cela a entraîné une erreur car il n'y a pas de variable avec le nom `gaze_ceu`. Il suffit d'ouvrir le script de l'élément *gaze_cue* et de corriger la faute de frappe.


## Enfin : Quelques considérations générales concernant le timing et la sélection du backend

Dans l'onglet 'Propriétés générales' de l'expérience (l'onglet que vous ouvrez en cliquant sur le nom de l'expérience), vous pouvez sélectionner un backend. Le backend est la couche logicielle qui contrôle l'affichage, les périphériques d'entrée, le son, etc. La plupart des expériences fonctionnent avec tous les backends, mais il y a des raisons de préférer un backend à un autre, principalement liées au timing. Actuellement, il existe quatre backends (selon votre système, les trois ne sont peut-être pas disponibles) :

- __psycho__ -- un backend accéléré matériellement basé sur PsychoPy [(Peirce, 2007)][references]. C'est le choix par défaut.
- __xpyriment__ -- un backend accéléré matériellement basé sur Expyriment [(Krause & Lindeman, 2013)][references]
- __legacy__ -- un backend 'sûr', basé sur PyGame. Il offre des performances fiables sur la plupart des plates-formes, mais, en raison de l'absence d'accélération matérielle, ses propriétés de temporisation ne sont pas aussi bonnes que celles des autres backends.
- __osweb__ -- exécute des expériences dans un navigateur [(Mathôt & March, 2022)][references].

Voir aussi :

- %link:backends%
- %link:timing%


## Références

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Time resolution of clocks: Effects on reaction time measurement—Good news for bad clocks. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.fr.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about
