title: Tutoriel débutant : orientation du regard
hash: 8b68f010d5f28f2e59818b6c6aac4308f317f2ced632ba0c36993b1e159c8432
locale: fr
language: French

## À propos d'OpenSesame

OpenSesame est un programme gratuit permettant de développer facilement des expériences comportementales en psychologie, en neurosciences, et en économie expérimentale. Pour les débutants, OpenSesame propose une interface graphique complète, basée sur le point-and-click. Pour les utilisateurs avancés, OpenSesame prend en charge le script Python (non abordé dans ce tutoriel).

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience psychologique simple mais complète à l’aide d’OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012; Mathôt & March, 2022)][references]. Vous utiliserez principalement l’interface graphique d’OpenSesame (c’est-à-dire, pas de codage inline en Python), bien que vous effectuerez quelques modifications mineures sur le script OpenSesame. Ce tutoriel prend environ une heure.

Ce tutoriel suppose que vous utilisez OpenSesame 4.1 avec toutes les dernières mises à jour appliquées. Si vous voyez une notification indiquant "Certains paquets peuvent être mis à jour (...)", cliquez sur le bouton "Installer les mises à jour ..." pour ouvrir le panneau de mise à jour, puis sur "Exécuter le script de mise à jour" pour effectuer les mises à jour. Après la mise à jour, redémarrez OpenSesame.

## L'expérience

Dans ce tutoriel, vous allez créer une expérience de guidance du regard telle qu’introduite par [Friesen et Kingstone (1998)][references]. Dans cette expérience, un visage est présenté au centre de l’écran (%FigGazeCuing). Ce visage regarde soit vers la droite soit vers la gauche. Une lettre cible (un 'F' ou un 'H') est présentée à gauche ou à droite du visage. Un stimulus distracteur (la lettre 'X') est présenté de l’autre côté du visage. La tâche consiste à indiquer le plus rapidement possible si la lettre cible est un 'F' ou un 'H'. Dans la condition congruente, le visage regarde la cible. Dans la condition incongruente, le visage regarde le distracteur. Comme vous pouvez vous y attendre, le résultat typique est que les participants répondent plus rapidement dans la condition congruente que dans la condition incongruente, même si la direction du regard ne prédit pas l’emplacement de la cible. Cela démontre que notre attention est automatiquement guidée par le regard d’autrui, même dans des situations où cela n’a pas d’utilité. (Et même lorsque le visage est un simple smiley !)

L’expérience se compose d’une phase de pratique et d’une phase expérimentale. Un feedback visuel sera présenté après chaque bloc d’essais. Un son sera joué après chaque réponse incorrecte.

La conception expérimentale :

- est *intra-sujets*, car tous les participants font toutes les conditions
- est *complètement croisée* (ou factorielle complète), car toutes les combinaisons de conditions apparaissent
- comporte trois facteurs :
    - *côté du regard* avec deux niveaux (gauche, droite)
    - *côté de la cible* avec deux niveaux (gauche, droite)
    - *lettre cible* avec deux niveaux (F, H)

Voir %DesignScreencast pour une explication de la logique et de la conception de l’expérience :

## Étape 1 : Créer la séquence principale

Lorsque vous démarrez OpenSesame, vous voyez l’onglet 'Bien démarrer !' (%FigGetStarted). Une liste de modèles s’affiche sous 'Commencer une nouvelle expérience'. Ces modèles fournissent des points de départ pratiques pour de nouvelles expériences. Après avoir enregistré une expérience pour la première fois, les expériences récemment ouvertes apparaissent sous 'Continuer avec une expérience récente'.

Cliquez sur 'Modèle par défaut' pour commencer avec un modèle expérimental minimal.

Par défaut, il existe une SEQUENCE principale, simplement appelée *experiment*. Cliquez sur *experiment* dans la zone de présentation (par défaut à gauche, voir %FigInterface) pour ouvrir ses contrôles dans la zone d’onglets. La SEQUENCE *experiment* se compose de deux items : un `notepad` appelé *getting started* et un SKETCHPAD appelé *welcome*.

<div class='info-box' markdown='1'>

__Encadré d'information__

__Noms vs types__ -- Les items dans OpenSesame ont un nom et un type. Le nom et le type peuvent être identiques, mais ce n’est généralement pas le cas. Par exemple, un item SKETCHPAD peut avoir comme nom *my_target_sketchpad*. Pour clarifier cette distinction, nous utiliserons la `monospace` pour indiquer les types d’items, et les *italiques* pour les noms.

__Astuce__ -- Le modèle 'Extended template' est un bon point de départ pour de nombreuses expériences. Il contient déjà la structure de base d'une expérience basée sur des essais.

__Astuce__ -- Vous pouvez cliquer sur les icônes d’aide en haut à droite de l’onglet d’un item pour obtenir une aide contextuelle.

__Astuce__ -- Sauvegardez (raccourci : `Ctrl+S`) fréquemment votre expérience ! En cas de perte de données (peu probable, mais possible), vous pourrez souvent récupérer votre travail à partir des sauvegardes automatiques créées toutes les 10 minutes par défaut (Menu → Outils → Ouvrir le dossier de sauvegarde).

__Astuce__ -- Sauf si vous avez utilisé 'Supprimer définitivement' (raccourci : `Shift+Del`), les items supprimés restent disponibles dans la corbeille 'Unused items', jusqu’à ce que vous choisissiez 'Permanently delete unused items' dans l’onglet 'Unused items'. Vous pouvez réintégrer un item supprimé à une SEQUENCE en le faisant glisser hors de la corbeille 'Unused items' vers l’emplacement de votre choix dans votre expérience.

__Astuce__ -- %FigExperimentStructure montre de façon schématique la structure de l’expérience que vous allez créer. Si vous êtes perdu pendant le tutoriel, vous pouvez vous référer à %FigExperimentStructure pour voir où vous en êtes.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  A schematic representation of the structure of the 'Gaze cuing' experiment. The item types are in bold face, item names in regular face.
--%

</div>


__Supprimez les items inutiles__

Nous n’avons pas besoin des deux items du modèle par défaut. Supprimez *getting_started* en faisant un clic droit dessus dans la zone de présentation et en sélectionnant « Supprimer » (raccourci : `Del`). Supprimez *welcome* de la même façon. La SEQUENCE *experiment* est maintenant vide.

__Ajoutez un item form_text_display pour afficher les instructions__

Comme son nom l’indique, un `form_text_display` est un formulaire qui affiche du texte. Nous allons utiliser un `form_text_display` pour donner des instructions au participant au début de l'expérience.

Cliquez sur *experiment* dans la zone de présentation pour ouvrir ses contrôles dans la zone d’onglets. Vous verrez une SEQUENCE vide. Faites glisser un `form_text_display` depuis la barre d’outils des items (sous « Form », voir %FigInterface) vers la SEQUENCE *experiment* dans la zone d’onglets. Lorsque vous relâchez, un nouvel item `form_text_display` sera inséré dans la SEQUENCE. (Nous y reviendrons à l’étape 12.)

<div class='info-box' markdown='1'>

__Encadré d'information__

__Astuce__ -- Vous pouvez faire glisser des items dans la zone de présentation et dans les onglets de SEQUENCE.

__Astuce__ -- Si une action de dépôt est ambiguë, un menu contextuel apparaîtra pour vous demander ce que vous souhaitez faire.

__Astuce__ -- Un `form_text_display` affiche uniquement du texte. Si vous avez besoin d’images, etc., vous pouvez utiliser un item SKETCHPAD. Nous présenterons le SKETCHPAD à l’étape 5.

</div>

__Ajoutez un item loop, contenant un item sequence, pour la phase d’entraînement__

Nous devons ajouter un item LOOP à la SEQUENCE *experiment*. Nous utiliserons ce LOOP pour la phase d’entraînement de l’expérience. Cliquez sur la SEQUENCE *experiment* pour ouvrir ses contrôles dans la zone d’onglets.

Faites glisser l’élément LOOP depuis la barre d’outils des éléments dans la SEQUENCE, de la même manière que vous avez ajouté le `form_text_display`. Les nouveaux éléments sont insérés sous l’élément sur lequel ils sont déposés, donc si vous déposez le nouveau LOOP sur le `form_text_display` précédemment créé, il apparaîtra à l’endroit souhaité : après le `form_text_display`. Mais ne vous inquiétez pas si vous déposez un nouvel élément au mauvais endroit, car vous pourrez toujours réorganiser les éléments plus tard.

Un LOOP, à lui seul, ne fait rien. Un LOOP a toujours besoin d’un autre élément à exécuter. Par conséquent, vous devez remplir le nouvel élément LOOP avec un autre élément. (Si vous affichez l’élément loop, vous verrez également une alerte : « Aucun élément sélectionné ».) Faites glisser un élément SEQUENCE depuis la barre d’outils des éléments sur l’élément LOOP. Un menu contextuel apparaît, vous demandant si vous souhaitez insérer la SEQUENCE après ou dans l’élément LOOP. Sélectionnez « Insérer dans new_loop ». (Nous y reviendrons à l’étape 2.)

<div class='info-box' markdown='1'>

__Boîte d’information__

__Qu’est-ce qu’un élément LOOP ?__ – Un LOOP est un élément qui structure votre expérience. Il exécute de façon répétée un autre élément, généralement une SEQUENCE. C’est aussi l’endroit où vous définissez habituellement vos variables indépendantes, c’est-à-dire celles que vous manipulez dans votre expérience.

__Qu’est-ce qu’un élément SEQUENCE ?__ – Un élément SEQUENCE structure aussi votre expérience. Comme son nom l’indique, une SEQUENCE exécute plusieurs autres éléments les uns après les autres.

__La structure LOOP-SEQUENCE__ – Vous souhaitez souvent répéter une séquence d’événements. Pour cela, vous aurez besoin d’un élément LOOP contenant un élément SEQUENCE. Une SEQUENCE seule ne se répète pas : elle commence simplement par le premier élément et se termine par le dernier. En « entourant » une SEQUENCE avec un LOOP, vous pouvez répéter la SEQUENCE plusieurs fois. Par exemple, un essai unique correspond généralement à une SEQUENCE unique appelée *trial_sequence*. Un LOOP (souvent nommé *block_loop*) autour de cette *trial_sequence* constituerait alors un bloc d’essais. De même, mais à un autre niveau de l’expérience, une SEQUENCE (souvent appelée *block_sequence*) peut contenir un seul bloc d’essais, suivi d’un affichage FEEDBACK. Un LOOP *practice_phase* autour de cette SEQUENCE « bloc » constituerait alors la phase d’entraînement de l’expérience. Cela peut sembler un peu abstrait pour l’instant, mais au fur et à mesure de ce tutoriel, vous vous familiariserez avec l’utilisation des LOOP et des SEQUENCE.

__Astuce__ – Pour plus d’informations sur les SEQUENCEs et les LOOPs, voir :

- %link:loop%
- %link:sequence%

</div>

__Ajoutez un nouvel élément form_text_display pour le message de fin de phase d’entraînement__

Après la phase de pratique, nous voulons informer le participant que la vraie expérience va commencer. Pour cela, nous avons besoin d’un autre `form_text_display`. Retournez dans la SEQUENCE *experiment*, et faites glisser un `form_text_display` depuis la barre d’outils des éléments sur l’élément LOOP. Le même menu contextuel apparaîtra que précédemment. Cette fois, sélectionnez « Insérer après new_loop ». (Nous y reviendrons à l’étape 12.)

<div class='info-box' markdown='1'>

__Astuce__ – Ne vous inquiétez pas si vous avez accidentellement changé l’élément à exécuter d’un LOOP. Vous pouvez facilement annuler cela en cliquant sur le bouton « Annuler » dans la barre d’outils (`Ctrl+Maj+Z`).

</div>

__Ajoutez un nouvel élément loop, contenant la séquence précédemment créée, pour la phase expérimentale__

Nous avons besoin d’un élément LOOP pour la phase expérimentale, comme pour la phase de pratique. Faites donc glisser un LOOP depuis le menu de la barre d’outils des éléments sur *_form_text_display*.

Le LOOP nouvellement créé (appelé *new_loop_1*) est vide, et doit être rempli avec une SEQUENCE, exactement comme le LOOP que nous avons créé auparavant. Cependant, puisque les essais des phases de pratique et expérimentale sont identiques, ils peuvent utiliser la même SEQUENCE. Donc, au lieu de faire glisser une nouvelle SEQUENCE depuis la barre d’outils, vous pouvez réutiliser l’existante (c’est-à-dire créer une copie liée).

Pour ce faire, faites un clic droit sur la *new_sequence* précédemment créée et sélectionnez « Copier (lié) ». Maintenant, faites un clic droit sur *new_loop_1* et sélectionnez « Coller ». Dans le menu contextuel qui apparaît, sélectionnez « Insérer dans new_loop 1 ».

<div class='info-box' markdown='1'>

__Boîte de contexte__

__Astuce__ — Il y a une distinction importante entre les copies *liées* et *non liées*. Si vous créez une copie liée d’un item, vous créez une autre occurrence du même item. Ainsi, si vous modifiez l’item d’origine, la copie liée sera également modifiée. En revanche, si vous créez une copie non liée d’un item, cette copie sera initialement identique (sauf pour le nom), mais vous pourrez modifier l’original sans affecter la copie non liée, et inversement.

</div>

__Ajoutez un nouvel item form_text_display, pour le message d’au revoir__

Lorsque l’expérience est terminée, nous devons dire au revoir au participant. Pour cela, nous avons besoin d’un autre item `form_text_display`. Retournez dans la SÉQUENCE *experiment*, et faites glisser un `form_text_display` depuis la barre d’outils des items sur *new_loop_1*. Dans le menu contextuel qui apparaît, sélectionnez « Insérer après new_loop_1 ». (Nous y reviendrons à l’étape 12.)

__Donnez des noms explicites aux nouveaux items__

Par défaut, les nouveaux items portent des noms comme *new_sequence* et *new_form_text_display_2*. Il est conseillé de nommer les items avec des noms explicites. Cela facilite grandement la compréhension de la structure de l’expérience. Si vous le souhaitez, vous pouvez également ajouter une description à chaque item. Les noms des items doivent contenir uniquement des caractères alphanumériques et/ou des tirets bas (_).

- Sélectionnez *new_form_text_display* dans la zone d’aperçu, double-cliquez sur son libellé en haut de la zone d’onglet et renommez l’item en *instructions*. (Raccourci pour la zone d’aperçu : `F2`)
- Renommez *new_loop* en *practice_loop*.
- Renommez *new_sequence* en *block_sequence*. Comme vous avez réutilisé cet item dans *new_loop_1*, le nom changera automatiquement à cet endroit aussi. (Cela illustre pourquoi il est efficace de créer des copies liées dès que possible.)
- Renommez *new_form_text_display_1* en *end_of_practice*.
- Renommez *new_loop_1* en *experimental_loop*.
- Renommez *new_form_text_display_2* en *end_of_experiment*.

__Donnez un nom explicite à toute l’expérience__

L’expérience complète possède également un titre et une description. Cliquez sur « New experiment » dans la zone d’aperçu. Vous pouvez renommer l’expérience de la même façon que vous avez renommé ses items. Le titre est actuellement « New experiment ». Renommez l’expérience en « Tutoriel : Gaze cuing ». Contrairement aux noms des items, le titre de l’expérience peut contenir des espaces, etc.

La zone d’aperçu de votre expérience ressemble désormais à %FigStep1. C’est le bon moment pour sauvegarder votre expérience (raccourci : `Ctrl+S`).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of the step 1.
--%


## Étape 2 : Créer la séquence de bloc

Cliquez sur *block_sequence* dans l’aperçu. Pour l’instant, cette SÉQUENCE est vide. Nous voulons que *block_sequence* contienne un bloc d’essais, suivi d’un affichage de FEEDBACK. Pour cela, nous devons faire ce qui suit :

__Ajoutez un item reset_feedback pour réinitialiser les variables de feedback__

Nous ne voulons pas que notre feedback soit affecté par des pressions de touches faites par les participants pendant la phase d’instructions ou lors des blocs d’essais précédents. C’est pourquoi nous commençons chaque bloc d’essais en réinitialisant les variables de feedback. Pour cela, il nous faut un item `reset_feedback`. Prenez `reset_feedback` depuis la barre d’outils des items (sous « Collecte de réponses ») et faites-le glisser sur *block_sequence*.

__Ajoutez une nouvelle boucle, contenant une nouvelle séquence, pour un bloc d’essais__

Pour un essai unique, nous avons besoin d’une SÉQUENCE. Pour un bloc d’essais, il faut répéter cette SÉQUENCE plusieurs fois. Ainsi, pour un bloc d’essais, il faut placer une BOUCLE autour d’une SÉQUENCE. Faites glisser un LOOP depuis la barre d’outils des items sur *new_reset_feedback*. Ensuite, faites glisser une SÉQUENCE depuis la barre d’outils des items sur le LOOP nouvellement créé, puis sélectionnez « Insérer dans new_loop » dans le menu contextuel qui apparaît. (Nous y reviendrons à l’étape 3.)

__Ajoutez un item feedback__

Après chaque bloc d’essais, nous voulons donner un retour au participant, afin qu’il/elle sache comment il/elle s’en sort. Pour cela, nous avons besoin d’un item FEEDBACK. Faites glisser un FEEDBACK depuis la barre d’outils des items vers *new_loop*, puis sélectionnez « Insérer après le loop » dans le menu contextuel qui apparaît. (Nous y reviendrons à l’Étape 10.)

__Donnez des noms pertinents aux nouveaux items__

Renommez : (Consultez l’Étape 1 si vous ne vous souvenez plus de la procédure.)

- *new_loop* en *block_loop*
- *new_sequence* en *trial_sequence*
- *new_reset_feedback* en *reset_feedback*
- *new_feedback* en *feedback*

L’aperçu de votre expérience ressemble maintenant à %FigStep2. N’oubliez pas d’enregistrer régulièrement votre expérience.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## Étape 3 : Remplissez le block_loop avec les variables indépendantes

Comme son nom l’indique, *block_loop* correspond à un seul bloc d’essais. À l’étape précédente, nous avons créé le *block_loop*, mais nous devons encore définir les variables indépendantes qui varieront à l’intérieur du bloc. Notre expérience comporte trois variables indépendantes :

- __gaze_cue__ peut être « left » ou « right ».
- __target_pos__ (la position de la cible) peut être « -300 » ou « 300 ». Ces valeurs correspondent à la coordonnée X de la cible en pixels (0 = centre). Utiliser directement les coordonnées, plutôt que « left » et « right », sera plus pratique lorsque nous créerons les écrans de présentation de la cible (voir Étape 5).
- __target_letter__ (la lettre cible) peut être « F » ou « H ».

Par conséquent, notre expérience comporte 2 x 2 x 2 = 8 conditions. Bien que 8 conditions ne soient pas beaucoup (la plupart des expériences en auront plus), nous n’avons pas besoin de saisir toutes les combinaisons possibles à la main. Cliquez sur *block_loop* dans l’aperçu pour ouvrir son onglet. Cliquez ensuite sur le bouton « Plan factoriel complet ». Dans l’assistant de variables, il vous suffit de définir toutes les variables en tapant le nom dans la première ligne et les niveaux dans les lignes en dessous du nom (voir %FigVariableWizard). Si vous sélectionnez « Ok », vous verrez que *block_loop* a été rempli avec toutes les 8 combinaisons possibles.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  The loop variable wizard in Step 3.
--%

Dans le tableau du loop obtenu, chaque ligne correspond à une exécution de *trial_sequence*. Dans notre cas, une exécution de *trial_sequence* correspond à un essai, chaque ligne du tableau de loop représente donc un essai. Chaque colonne correspond à une variable, qui peut prendre une valeur différente à chaque essai.

Mais ce n’est pas tout. Nous devons ajouter trois variables supplémentaires : la position du distracteur, la réponse correcte et la congruence.

- __dist_pos__ -- Sur la première ligne de la première colonne vide, entrez « dist_pos ». Cela ajoute automatiquement une nouvelle variable expérimentale nommée « dist_pos ». Dans les lignes en dessous, saisissez « 300 » partout où « target_pos » vaut -300, et « -300 » partout où « target_pos » vaut 300. En d’autres termes, la cible et le distracteur doivent être placés de manière opposée.
- __correct_response__ -- Créez une autre variable, dans une nouvelle colonne vide, avec le nom « correct_response ». Attribuez « z » à « correct_response » là où « target_letter » est « F », et « m » là où « target_letter » est « H ». Cela signifie que le participant doit appuyer sur la touche « z » s’il voit un « F » et sur la touche « m » s’il voit un « H ». (N’hésitez pas à choisir d’autres touches si « z » et « m » ne sont pas pratiques sur votre clavier ; par exemple, « w » et « n » sont de meilleures options sur un clavier AZERTY.)
- __congruency__ -- Créez une autre variable appelée « congruency ». Attribuez « congruent » à « congruency » lorsque « target_pos » vaut « -300 » et « gaze_cue » vaut « left », et lorsque « target_pos » vaut « 300 » et « gaze_cue » vaut « right ». En d’autres termes, un essai est congruent si le visage regarde la cible. Attribuez « incongruent » pour les essais où le visage regarde le distracteur. La variable « congruency » n’est pas nécessaire pour faire fonctionner l’expérience ; cependant, elle sera utile lors de l’analyse ultérieure des données.

Nous devons faire une dernière chose. ‘Repeat’ est actuellement réglé sur ‘1.00’. Cela signifie que chaque cycle sera exécuté une fois. Donc, le bloc consiste maintenant en 8 essais, ce qui est un peu court. Une longueur raisonnable pour un bloc d'essais est de 24, donc réglez ‘Repeat’ sur 3.00 (3 répétitions x 8 cycles = 24 essais). Il n’est pas nécessaire de modifier ‘Order’, car ‘random’ est exactement ce que nous souhaitons.

Le *block_loop* ressemble maintenant à %FigStep3. Pensez à enregistrer régulièrement votre expérience.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

__Boîte de contexte__

__Astuce__ -- Vous pouvez préparer votre table de boucle dans votre programme de tableur préféré et la copier-coller dans la table des variables de LOOP.

__Astuce__ -- Vous pouvez spécifier votre table de boucle dans un fichier séparé (au format `.xlsx` ou `.csv`), et utiliser ce fichier directement. Pour cela, sélectionnez ‘file’ dans ‘Source’.

__Astuce__ -- Vous pouvez définir ‘Repeat’ sur une valeur non entière. Par exemple, en réglant ‘Repeat’ sur ‘0.5’, seule la moitié des essais (sélectionnés aléatoirement) seront exécutés.

</div>

## Étape 4 : Ajouter des images et des fichiers sonores à la réserve de fichiers

Pour nos stimuli, nous utiliserons des images depuis un fichier. De plus, nous diffuserons un son si le participant fait une erreur. Pour cela, nous avons besoin d’un fichier son.

Vous pouvez télécharger les fichiers nécessaires ici (dans la plupart des navigateurs, vous pouvez faire un clic droit sur les liens et choisir « Enregistrer le lien sous » ou une option similaire) :

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Après avoir téléchargé ces fichiers (par exemple sur votre bureau), vous pouvez les ajouter à la réserve de fichiers. Si la réserve de fichiers n’est pas déjà visible (par défaut, sur le côté droit de la fenêtre), cliquez sur le bouton « Afficher la réserve de fichiers » dans la barre d’outils principale (raccourci : `Ctrl+P`). Le moyen le plus simple d’ajouter les quatre fichiers à la réserve de fichiers est de les glisser-déposer depuis le bureau (ou l’endroit où vous les avez téléchargés) dans la réserve de fichiers. Vous pouvez également cliquer sur le bouton ‘+’ dans la réserve de fichiers pour ajouter des fichiers à l’aide de la boîte de dialogue qui s’ouvre. La réserve de fichiers sera automatiquement enregistrée avec votre expérience.

Votre réserve de fichiers ressemble maintenant à %FigStep4. Pensez à enregistrer régulièrement votre expérience.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

## Étape 5 : Remplir la séquence d’essai avec des items

Un essai dans notre expérience se présente comme suit :

1. __Point de fixation__ — 750 ms, SKETCHPAD item
2. __Regard neutre__ — 750 ms, SKETCHPAD item
3. __Indice de regard__ — 500 ms, SKETCHPAD item
4. __Cible__  — 0 ms, SKETCHPAD item
5. __Collecte de la réponse__ — KEYBOARD_RESPONSE item
6. __Jouer un son si la réponse est incorrecte__ —  SAMPLER item
7. __Enregistrer la réponse dans un fichier__ — LOGGER item

Cliquez sur *trial_sequence* dans l’aperçu pour ouvrir l’onglet *trial_sequence*. Prenez un SKETCHPAD depuis la barre d’outils des items et faites-le glisser dans le *trial_sequence*. Répétez cela trois fois encore, pour que *trial_sequence* contienne quatre SKETCHPADs. Ensuite, sélectionnez et ajoutez un item KEYBOARD_RESPONSE, un item SAMPLER, et un item LOGGER.

Encore une fois, nous allons renommer les nouveaux items pour que le *trial_sequence* soit facile à comprendre. Renommez :

- *new_sketchpad* en *fixation_dot*
- *new_sketchpad_1* en *neutral_gaze*
- *new_sketchpad_2* en *gaze_cue*
- *new_sketchpad_3* en *target*
- *new_keyboard_response* en *keyboard_response*
- *new_sampler* en *incorrect_sound*
- *new_logger* en *logger*

Par défaut, les items sont toujours exécutés, ce qui est indiqué par l'expression run-if `True`. Cependant, nous souhaitons changer cela pour l’item *incorrect_sound*, qui ne doit être exécuté que si une erreur a été commise. Pour ce faire, nous devons modifier l’expression « Run if » en `correct == 0` dans l’onglet *trial_sequence*. Cela fonctionne car l’item *keyboard_response* crée automatiquement une variable `correct`, qui prend la valeur `1` (correct), `0` (incorrect) ou `undefined` (cela dépend de la variable `correct_response` définie à l’étape 3). Le signe égal double correspond à la syntaxe Python et indique que l’on veut vérifier si les deux éléments sont égaux, en l’occurrence si la variable `correct` est égale à 0. Pour modifier une expression run-if, double-cliquez dessus (raccourci : `F3`).

La *trial_sequence* ressemble maintenant à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%

<div class='info-box' markdown='1'>

__Boîte d'arrière-plan__

__Qu’est-ce qu’un item SKETCHPAD ?__ -- Un SKETCHPAD est utilisé pour présenter des stimuli visuels : texte, formes géométriques, points de fixation, patchs de Gabor, etc. Vous pouvez dessiner sur le SKETCHPAD à l’aide des outils de dessin intégrés.

__Qu’est-ce qu’un item KEYBOARD_RESPONSE ?__ -- Un item KEYBOARD_RESPONSE collecte la réponse d’un participant au clavier.

__Qu’est-ce qu’un item SAMPLER ?__ -- Un item SAMPLER joue un son à partir d’un fichier sonore.

__Qu’est-ce qu’un item LOGGER ?__ -- Un item LOGGER enregistre les données dans le fichier log. C’est très important : si vous oubliez d’inclure un item LOGGER, aucune donnée ne sera enregistrée pendant l’expérience !

__Astuce__ -- Les variables et les expressions conditionnelles « if » sont très puissantes ! Pour en savoir plus à leur sujet, consultez :

- %link:manual/variables%

</div>

## Étape 6 : Dessiner les items sketchpad

Les items SKETCHPAD que nous avons créés à l’étape 5 sont encore vides. Il est temps de dessiner !

__Définir la couleur de fond sur blanc__

Cliquez sur *fixation_dot* dans la zone d’aperçu pour ouvrir son onglet. Le SKETCHPAD est encore gris foncé, alors que les images que nous avons téléchargées ont un fond blanc. Oups, nous avons oublié de définir la couleur de fond de l’expérience sur blanc (elle est grise foncée par défaut) ! Cliquez sur « Tutorial: Gaze cuing » dans la zone d’aperçu pour ouvrir l’onglet « General properties ». Changez « Foreground » en « black » et « Background » en « white ».

<div class='info-box' markdown='1'>

__Boîte d'arrière-plan__

__Astuce__ -- Pour un contrôle plus précis des couleurs, vous pouvez aussi utiliser l’écriture RGB hexadécimale (par exemple, `#FF000` pour le rouge), utiliser différents espaces couleur, ou l’outil sélecteur de couleurs. Voir aussi :

- %link:manual/python/canvas%

</div>

__Dessiner le point de fixation__

Revenez à *fixation_dot* en cliquant sur *fixation_dot* dans l’aperçu. Sélectionnez maintenant l’outil point de fixation en cliquant sur le bouton en forme de mire. Si vous déplacez votre curseur sur le sketchpad, vous pouvez voir les coordonnées de l’écran en haut à droite. Définissez la couleur (avant-plan) sur « black ». Cliquez au centre de l’écran (0, 0) pour dessiner un point de fixation central.

Enfin, changez le champ ‘Duration’ de ‘keypress’ à ‘745’, car nous voulons que le point de fixation soit présenté pendant 750 ms. Attendez… *pourquoi n’avons-nous pas simplement indiqué 750 ms ?* La raison est que la durée réelle d’affichage est toujours arrondie vers la valeur compatible avec la fréquence de rafraîchissement de votre moniteur. Cela peut sembler compliqué, mais pour la plupart des cas, les règles suivantes suffisent :

1. Choisissez une durée compatible avec le taux de rafraîchissement de votre écran. Par exemple, si le taux de rafraîchissement de votre écran est de 60 Hz, cela signifie que chaque image dure 16,7 ms (= 1000 ms/60 Hz). Par conséquent, sur un écran à 60 Hz, vous devriez toujours sélectionner une durée qui est un multiple de 16,7 ms, comme 16,7, 33,3, 50, 100, etc.
2. Dans le champ de durée du SKETCHPAD, spécifiez une durée qui est inférieure de quelques millisecondes à celle que vous visez. Donc, si vous souhaitez présenter un SKETCHPAD pendant 50 ms, choisissez une durée de 45. Si vous souhaitez présenter un SKETCHPAD pendant 1000 ms, choisissez une durée de 995. Etc.

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Pour une discussion détaillée sur la synchronisation expérimentale, consultez :

- %link:timing%

__Astuce__ -- La durée d'un SKETCHPAD peut être une valeur en millisecondes, mais vous pouvez également entrer 'keypress' ou 'mouseclick' pour enregistrer respectivement une pression de touche ou un clic de souris. Dans ce cas, un SKETCHPAD fonctionnera presque de la même manière qu'un item KEYBOARD_RESPONSE (mais avec moins d’options).

__Astuce__ -- Assurez-vous que la couleur (avant-plan) est définie sur noir. Sinon, vous dessinerez en blanc sur fond blanc et vous ne verrez rien !

</div>

__Dessiner le regard neutre__

Ouvrez le SKETCHPAD *neutral_gaze*. Sélectionnez maintenant l’outil image en cliquant sur le bouton avec l’icône représentant un paysage de montagne. Cliquez au centre de l’écran (0, 0). La boîte de dialogue 'Sélectionner un fichier du pool' apparaîtra. Sélectionnez le fichier `gaze_neutral.png` et cliquez sur le bouton 'Sélectionner'. L’image de regard neutre apparaîtra alors au centre de l’écran ! Enfin, comme précédemment, changez le champ 'Duration' de 'keypress' à '745'. (Et notez encore une fois que cela correspond à une durée de 750 ms sur la plupart des écrans !)

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- OpenSesame peut gérer une grande variété de formats d’image. Toutefois, certains formats `.bmp` (non standards) sont connus pour poser problème. Si vous constatez qu’une image `.bmp` n'est pas affichée, vous pouvez la convertir dans un autre format, comme `.png`. Vous pouvez facilement convertir des images avec des outils gratuits tels que [GIMP].
</div>

__Dessiner l’indice directionnel du regard__

Ouvrez le SKETCHPAD *gaze_cue*, et sélectionnez à nouveau l’outil image. Cliquez au centre de l’écran (0, 0) et sélectionnez le fichier `gaze_left.png`.

Mais nous n’avons pas encore terminé ! Car l’indice directionnel du regard ne devrait pas toujours être 'left', mais dépendre de la variable `gaze_cue`, que nous avons définie à l’étape 3. Cependant, en dessinant l’image `gaze_left.png` sur le SKETCHPAD, nous avons généré un script qui ne nécessite qu’une très petite modification pour s’assurer que la bonne image sera affichée. Cliquez sur le bouton 'Select view' en haut à droite de l’onglet *gaze_cue* et sélectionnez 'View script'. Vous verrez maintenant le script correspondant au sketchpad que nous venons de créer :

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

La seule chose à faire est de remplacer `gaze_left.png` par `gaze_{gaze_cue}.png`. Cela signifie qu’OpenSesame utilise la variable `gaze_cue` (qui prend les valeurs `left` et `right`) pour déterminer quelle image doit être affichée.

Pendant que nous y sommes, changeons aussi la durée à '495' (arrondi à 500 !). Le script ressemble maintenant à ceci :

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Cliquez sur le bouton 'Apply' en haut à droite pour appliquer vos modifications au script et revenir aux commandes classiques de l’item. OpenSesame vous avertira que l’image ne peut pas être affichée car elle est définie à l’aide de variables, et une image de remplacement sera affichée à la place. Ne vous inquiétez pas, l’image correcte sera affichée pendant l’expérience !

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuces__ -- L’inspecteur de variables (raccourci : `Ctrl+I`) est un moyen puissant de découvrir quelles variables ont été définies dans votre expérience, et quelles valeurs elles possèdent (voir %FigVariableInspector). Lorsque votre expérience n’est pas en cours d’exécution, la plupart des variables n’ont pas encore de valeur. Mais lorsque vous exécutez votre expérience dans une fenêtre, tout en gardant l’inspecteur de variables visible, vous pouvez voir les variables changer en temps réel. Cela est très utile pour déboguer votre expérience.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "L’inspecteur de variables est un moyen pratique d’obtenir un aperçu des variables présentes dans votre expérience."
--%

</div>

__Dessiner la cible__

Nous voulons que trois objets fassent partie de l’affichage de la cible : la lettre cible, la lettre distractrice et l’indice de regard (voir %FigGazeCuing). Comme précédemment, nous allons commencer par créer un affichage statique en utilisant l’éditeur SKETCHPAD. Ensuite, il ne sera nécessaire de faire que des modifications mineures du script pour que l’affichage exact dépende des variables.

Cliquez sur *target* dans la vue d’ensemble pour ouvrir l’onglet de la cible et, comme précédemment, dessinez l’image `gaze_left.png` au centre de l’écran. Sélectionnez ensuite l’outil Texte en cliquant sur le bouton avec l’icône ‘A’. Changez la couleur du texte en ‘noir’ (si ce n’est pas déjà le cas). La taille de police par défaut est de 18 px, ce qui est un peu petit pour notre objectif, donc changez la taille de la police à 32 px. Cliquez ensuite sur (-320, 0) dans le SKETCHPAD (la coordonnée X n’a pas besoin d’être exactement 320, car nous la changerons de toute façon par une variable). Entrez "{target_letter}" dans la boite de dialogue qui apparaît, pour dessiner la lettre cible (lors du dessin de texte, vous pouvez utiliser directement des variables). De la même manière, cliquez sur (320, 0) et dessinez un ‘X’ (le distracteur est toujours un ‘X’).

Ouvrez maintenant l’éditeur de script en cliquant sur le bouton ‘Select view’ en haut à droite de l’onglet, puis en sélectionnant ‘View script’. Le script ressemble à ceci :

~~~ .python
set duration keypress
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

Comme précédemment, changez `gaze_left.png` par `gaze_{gaze_cue}.png`. Nous devons aussi faire en sorte que la position de la cible et du distracteur dépende respectivement des variables `target_pos` et `dist_pos`. Pour cela, changez simplement `-320` en `{target_pos}` et `320` en `{dist_pos}`. Assurez-vous de laisser le `0`, qui correspond à la coordonnée Y. Le script ressemble maintenant à ceci :

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

Cliquez sur le bouton 'Apply' pour appliquer le script et revenir aux contrôles réguliers de l’item.

Enfin, définissez le champ ‘Duration’ sur ‘0’. Cela ne veut pas dire que la cible est présentée pendant seulement 0 ms, mais que l’expérience va passer à l’item suivant (*keyboard_response*) immédiatement. Puisque *keyboard_response* attend une réponse sans changer ce qui est affiché à l’écran, la cible restera visible jusqu’à ce qu’une réponse soit donnée.

N’oubliez pas d’enregistrer régulièrement votre expérience.

<div class='info-box' markdown='1'>

__Boîte de fond__

__Astuce__ -- Chaque élément d'un SKETCHPAD possède une option 'Afficher si', qui spécifie à quel moment l'élément doit être affiché. Vous pouvez utiliser cela pour masquer/afficher des éléments d'un SKETCHPAD en fonction de certaines variables, de la même manière que les instructions run-if dans une SEQUENCE.

__Astuce__ -- Assurez-vous que la couleur (avant-plan) est définie sur noir. Sinon, vous dessinerez en blanc sur blanc et vous ne verrez rien !

</div>

## Étape 7 : Configurer l'élément keyboard_response

Cliquez sur *keyboard_response* dans l'aperçu pour ouvrir son onglet. Vous voyez trois options : Réponse correcte, Réponses autorisées, Temps d'attente (Timeout), et Type d'événement.

Nous avons déjà défini la variable `correct_response` à l'étape 3. À moins de spécifier explicitement une réponse correcte, OpenSesame utilise automatiquement la variable `correct_response` si elle est disponible. Par conséquent, nous n'avons pas besoin de modifier le champ 'Réponse correcte' ici.

Nous devons en revanche spécifier les réponses autorisées. Entrez 'z;m' dans le champ des réponses autorisées (ou d'autres touches si vous avez choisi des touches différentes). Le point-virgule sépare les réponses. Le KEYBOARD_RESPONSE n'accepte maintenant que les touches 'z' et 'm'. Toutes les autres frappes sont ignorées, à l'exception de 'escape', qui met l'expérience en pause.

Nous voulons également définir un temps d'attente, c'est-à-dire l'intervalle maximal pendant lequel le KEYBOARD_RESPONSE attend avant de décider que la réponse est incorrecte et de définir la variable 'response' sur 'None'. '2000' (ms) est une bonne valeur.

Nous ne devons pas changer le type d'événement, car nous voulons que le participant réponde en appuyant sur une touche (keypress, valeur par défaut) et non en relâchant une touche (keyrelease).

Le KEYBOARD_RESPONSE ressemble maintenant à %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "Le KEYBOARD_RESPONSE à la fin de l'étape 7."
--%

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Par défaut, le KEYBOARD_RESPONSE utilisera la variable `correct_response` pour déterminer si une réponse est correcte. Mais vous pouvez aussi utiliser une autre variable. Pour cela, saisissez un nom de variable entre accolades (`{my_variable}`) dans le champ réponse correcte.

__Astuce__ -- Si 'vider les frappes en attente' est activé (c'est le cas par défaut), toutes les frappes de touche en attente sont ignorées lorsque l'élément KEYBOARD_RESPONSE est appelé. Cela évite les effets de report, qui pourraient sinon survenir si le participant appuie accidentellement sur une touche lors d'une phase sans réponse de l'essai.

__Astuce__ -- Pour utiliser des touches spéciales, telles que '/' ou la flèche vers le haut, vous pouvez utiliser le nom des touches (ex : 'up' et 'space') ou les caractères correspondants (ex : '/' et ']'). Le bouton 'Lister les touches disponibles' fournit un aperçu de tous les noms de touches valides.

</div>

## Étape 8 : Configurer l'élément incorrect (sampler)

L'élément *incorrect_sound* ne nécessite pas beaucoup de configuration : il suffit de sélectionner le son à jouer. Cliquez sur *incorrect_sound* dans l'aperçu pour ouvrir son onglet. Cliquez sur le bouton 'Parcourir' et sélectionnez `incorrect.ogg` depuis la bibliothèque de fichiers.

Le sampler ressemble maintenant à %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "L'élément *incorrect_sound* à la fin de l'étape 8."
--%

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Vous pouvez utiliser des variables pour spécifier quel son doit être joué en utilisant un nom de variable entre accolades comme (partie du) nom de fichier. Par exemple : `{a_word}.ogg`

__Astuce__ -- Le SAMPLER gère les fichiers aux formats `.ogg`, `.mp3`, et `.wav`. Si vous avez des fichiers audio dans un autre format, [Audacity] est un excellent outil gratuit pour convertir des fichiers audio (et bien plus).

</div>

## Étape 9 : Configurer le variable logger

En réalité, nous n'avons pas besoin de configurer le LOGGER de variables, mais regardons-le tout de même. Cliquez sur *logger* dans l'aperçu pour ouvrir son onglet. Vous verrez que l'option 'Consigner automatiquement toutes les variables' est sélectionnée. Cela signifie qu'OpenSesame enregistre tout, ce qui est très bien.

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Si vous souhaitez garder vos fichiers de log propres, vous pouvez désactiver l’option « Enregistrer automatiquement toutes les variables » et sélectionner manuellement les variables, soit en saisissant leurs noms (« Ajouter une variable personnalisée »), soit en faisant glisser les variables depuis l’inspecteur de variables vers le tableau LOGGER. Vous pouvez également laisser l’option « Enregistrer automatiquement toutes les variables » activée et exclure les variables qui ne vous intéressent pas.

__L’astuce ultime__ -- Vérifiez toujours trois fois si toutes les variables nécessaires sont bien enregistrées dans votre expérience ! La meilleure façon de vérifier est d’exécuter l’expérience et d’inspecter les fichiers de log générés.

</div>

## Étape 10 : Dessiner l’élément feedback

Après chaque bloc d’essais, nous souhaitons présenter un retour au participant afin de lui indiquer ses performances. Pour cette raison, à l’étape 2, nous avons ajouté un élément FEEDBACK, simplement nommé *feedback*, à la fin de *block_sequence*.

Cliquez sur *feedback* dans l’aperçu pour ouvrir son onglet, sélectionnez l’outil texte, changez la couleur du premier plan en « noir » (si ce n’est pas déjà le cas), et cliquez à (0, 0). Saisissez alors le texte suivant :

```text
Fin du bloc

Votre temps de réponse moyen était de {avg_rt} ms
Votre précision était de {acc} %

Appuyez sur une touche pour continuer
```

Comme nous voulons que l’élément feedback reste affiché aussi longtemps que le participant le souhaite (jusqu’à ce qu’il appuie sur une touche), nous laissons le champ « Durée » à « keypress ».

L’élément feedback ressemble maintenant à %FigStep_10.

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "The feedback item at the end of Step 10."
--%

<div class='info-box' markdown='1'>

__Boîte de contexte__

__Qu’est-ce qu’un élément feedback ?__ -- Un élément FEEDBACK est presque identique à un élément SKETCHPAD. La seule différence est qu’un élément FEEDBACK n’est pas préparé à l’avance. Cela signifie que vous pouvez l’utiliser pour présenter des retours, qui nécessitent des informations à jour sur la réponse du participant. Vous ne devez pas utiliser les éléments FEEDBACK pour présenter des affichages critiques en termes de temps, car le fait qu’ils ne soient pas préparés à l’avance signifie que leurs propriétés temporelles ne sont pas aussi bonnes que celles de l’élément SKETCHPAD. Voir aussi :

- %link:visual%

__Feedback et variables__ -- Les éléments de réponse suivent automatiquement la précision et le temps de réponse moyen du participant dans les variables 'acc' (synonyme : 'accuracy') et 'avg_rt' (synonyme : 'average_response_time'). Voir aussi :

- %link:manual/variables%

__Astuce__ -- Vérifiez que la couleur (de premier plan) est bien réglée sur noir. Sinon, vous écrirez en blanc sur blanc et ne verrez rien !

</div>

## Étape 11 : Définir la longueur des phases d’entraînement et expérimentale

Nous avons déjà créé les éléments *practice_loop* et *experiment_loop*, qui appellent tous les deux *block_sequence* (c’est-à-dire un bloc d’essais). Cependant, actuellement, ils appellent *block_sequence* une seule fois, ce qui signifie que la phase d’entraînement et la phase expérimentale ne comprennent qu’un seul bloc d’essais.

Cliquez sur *practice_loop* pour ouvrir son onglet et réglez « Répéter » sur « 2,00 ». Cela signifie que la phase d’entraînement comprend deux blocs.

Cliquez sur *experimental_loop* pour ouvrir son onglet et réglez « Répéter » sur « 8,00 ». Cela signifie que la phase expérimentale comprend huit blocs.

<div class='info-box' markdown='1'>

__Boîte de contexte__

__Astuce__ -- Vous pouvez créer une variable `practice` dans *practice_loop* et *experimental_loop* et la définir respectivement sur « yes » et « no ». C’est un moyen simple de garder une trace des essais faisant partie de la phase d’entraînement.

</div>

## Étape 12 : Rédiger les formulaires instruction, end_of_practice et end_of_experiment

Je pense que vous pouvez gérer cette étape tout seul ! Ouvrez simplement les éléments appropriés et ajoutez du texte pour présenter les instructions, un message de fin de phase d’entraînement, et un message de fin d’expérience.

<div class='info-box' markdown='1'>

__Boîte de contexte__

__Astuce__ -- Vous pouvez utiliser un sous-ensemble de balises HTML pour formater votre texte. Par exemple, *&lt;b&gt;ceci sera en gras&lt;b&gt;* et *&lt;span color='red'&gt;ceci sera en rouge&lt;span&gt;*. Pour plus d’informations, voir :

- %link:text%

</div>

## Étape 13 : Exécutez l'expérience !

C'est terminé ! Cliquez sur les boutons 'Exécuter dans une fenêtre' (raccourci : `Ctrl+W`) ou 'Exécuter en plein écran' (raccourci : `Ctrl+R`) dans la barre d'outils pour lancer votre expérience.

<div class='info-box' markdown='1'>

__Boîte d'information__

__Astuce__ -- Un essai rapide est encore plus rapide en cliquant sur le bouton orange 'Exécuter dans une fenêtre' (raccourci : `Ctrl+Shift+W`), qui ne vous demande pas comment sauvegarder le fichier journal (et ne doit donc être utilisé qu'à des fins de test).

</div>


## Comprendre les erreurs

Savoir comprendre les messages d'erreur est une compétence cruciale lorsqu'on travaille avec OpenSesame. Après tout, une expérience nouvellement créée démarre rarement sans aucune erreur !

Supposons que nous ayons commis une erreur lors d'une des étapes ci-dessus. En essayant d'exécuter l'expérience, nous obtenons le message d'erreur suivant (%FigErrorMessage) :

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "Un message d'erreur dans OpenSesame."
--%

Le message d’erreur commence par un nom, dans ce cas `FStringError`, qui indique le type général d’erreur. Ceci est suivi d’un court texte explicatif, ici 'Failed to evaluate f-string expression in the following text: gaze_{gaze_ceu}.png`. Même sans comprendre ce qu'est une f-string (c'est une chaîne qui contient du code Python entre des accolades), il est clair qu'il y a quelque chose qui cloche avec le texte '{gaze_ceu}.png'.

Le message d’erreur indique aussi que l’erreur provient de la phase de préparation de l’item *gaze_cue*.

Enfin, le message d’erreur précise ce qui, précisément, a échoué lors de l’évaluation du texte 'gaze_{gaze_ceu}.png' : le nom 'gaze_ceu' n’est pas défini.

En lisant attentivement le message d’erreur, la cause et la solution vous viennent probablement déjà à l’esprit : nous avons fait une simple faute de frappe dans l’item *gaze_cue*, en écrivant '{gaze_ceu}' au lieu de '{gaze_cue}' ! Cela a donc généré une erreur car il n’existe pas de variable nommée `gaze_ceu`. Ceci peut être facilement corrigé en ouvrant le script de l’item *gaze_cue* et en corrigeant la faute de frappe.


## Enfin : Quelques considérations générales concernant le timing et la sélection du backend

Dans l’onglet 'Propriétés générales' de l’expérience (l’onglet que vous ouvrez en cliquant sur le nom de l’expérience), vous pouvez sélectionner un backend. Le backend est la couche logicielle qui contrôle l’affichage, les dispositifs d’entrée, le son, etc. La plupart des expériences fonctionnent avec tous les backends, mais il y a des raisons de préférer un backend à un autre, principalement liées au timing. Il existe actuellement quatre backends (selon votre système, tous ne seront peut-être pas disponibles) :

- __psycho__ -- un backend accéléré matériellement basé sur PsychoPy [(Peirce, 2007)][references]. C’est celui par défaut.
- __xpyriment__ -- un backend accéléré matériellement basé sur Expyriment [(Krause & Lindeman, 2013)][references]
- __legacy__ -- un backend "sûr" basé sur PyGame. Il offre des performances fiables sur la plupart des plateformes, mais, faute d’accélération matérielle, ses propriétés temporelles ne sont pas aussi bonnes que celles des autres backends.
- __osweb__ -- exécute les expériences dans un navigateur [(Mathôt & March, 2022)][references].

Voir aussi :

- %link:backends%
- %link:timing%


## Références

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame : Un outil open-source et graphique pour créer des expériences en sciences sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Réaliser des expériences linguistiques en ligne avec OpenSesame et OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy : Un logiciel de psychophysique en Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Résolution temporelle des horloges : Effets sur la mesure du temps de réaction—De bonnes nouvelles pour les mauvaises horloges. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about