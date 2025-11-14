title: Tutoriel débutant : orientation du regard
hash: 1bc0db6f02f63201f3d90855479f82e8a246736a8141fb744439c06fe8783002
locale: fr
language: French

## À propos d'OpenSesame

OpenSesame est un programme gratuit pour le développement rapide d’expériences comportementales en psychologie, neurosciences cognitives et économie expérimentale. Pour les débutants, OpenSesame propose une interface graphique complète basée sur le « pointer-cliquer ». Pour les utilisateurs avancés, OpenSesame prend en charge le script Python et JavaScript (non abordé dans ce tutoriel).

## À propos de ce tutoriel

Nous allons créer une expérience classique d'orientation du regard (« gaze-cuing »). Il s'agit d'un paradigme amusant et intéressant, où il est difficile de ne pas regarder là où fixe un visage.

Nous utiliserons uniquement l’interface graphique. Nous *n’utiliserons pas* de code Python ou JavaScript (ce contenu est traité dans les tutoriels intermédiaires). Ce tutoriel dure environ une heure.

## Ce que vous allez apprendre

À la fin de ce tutoriel, vous saurez :

- 💡 Construire la structure d’une expérience avec des items SEQUENCE et LOOP
- 💡 Définir un plan factoriel complet avec des variables indépendantes dans une table LOOP
- 💡 Créer des stimuli visuels avec des items SKETCHPAD
- 💡 Recueillir des réponses avec des items KEYBOARD_RESPONSE
- 💡 Fournir un feedback aux participants avec des items FEEDBACK
- 💡 Afficher du texte à l'aide des items FORM_TEXT_DISPLAY
- 💡 Utiliser des variables pour définir vos stimuli
- 💡 Utiliser des expressions conditionnelles (run-if) pour contrôler le déroulement de l’expérience
- 💡 Organiser les fichiers de stimuli dans le file pool
- 💡 Enregistrer des données (log)

## Ce dont vous aurez besoin

**OpenSesame 4.1 ou version ultérieure** avec toutes les mises à jour installées. Si une notification de mises à jour disponibles apparaît, cliquez sur « Installer les mises à jour... » puis sur « Exécuter le script de mise à jour ». Redémarrez OpenSesame après la mise à jour. Vous pouvez également mettre à jour manuellement en exécutant la commande suivante dans la console OpenSesame.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

## L'expérience

Comme mentionné précédemment, nous allons créer une expérience d’orientation du regard, initialement développée par [Friesen et Kingstone (1998)][references]. Voici le déroulement :

1. Un visage apparaît au centre de l'écran
2. Le visage regarde à gauche ou à droite
3. Une lettre cible ('F' ou 'H') apparaît d’un côté
4. Une lettre distractrice ('X') apparaît de l’autre côté
5. Les participants identifient la lettre cible aussi vite que possible

L'expérience comprend une phase d’entraînement et une phase expérimentale. Vous montrerez un feedback après chaque bloc. Un son sera joué après une réponse incorrecte.

Le résultat intéressant ? Les gens sont plus rapides lorsque le visage regarde vers la cible, même si la direction du regard ne prédit pas l'emplacement de la cible. Cela montre que les humains suivent automatiquement le regard des autres.

## Étape 1 : Créer la séquence principale

🎯 __But :__ Dans cette étape, nous allons créer la structure de base de notre expérience : une phase d’entraînement, durant laquelle les participants s’exercent à la tâche ; une phase expérimentale, durant laquelle nous collecterons les données pour l’analyse ; et des écrans d’information avant et après ces phases. Nous allons uniquement mettre en place la structure. Les détails seront implémentés plus tard.

Lorsque vous lancez OpenSesame, l’onglet « Bien démarrer ! » apparaît (%FigGetStarted). Choisissez « Modèle par défaut ».

Open the main SEQUENCE named *experiment*. Il contient deux items par défaut : un notepad (*getting_started*) et un SKETCHPAD (*welcome*).

<details class='info-box' markdown='1'>

<summary markdown='1'>Astuces utiles pour ce tutoriel</summary>

- Cliquez sur l’icône Aide dans l’onglet de n’importe quel item pour afficher l’aide contextuelle.
- Sauvegardez fréquemment (Ctrl+S). Des sauvegardes sont créées automatiquement (Outils → Ouvrir le dossier de sauvegarde).
- Les items supprimés peuvent être récupérés depuis “Éléments inutilisés” sauf s’ils ont été définitivement supprimés (Shift+Del).
- Consultez la figure ci-dessous pour la structure que nous allons construire.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  Structure of the gaze-cuing experiment. Item types in bold, item names regular.
--%

</details>

Supprimez les items par défaut :

- Clic droit sur *getting_started* → Supprimer
- Clic droit sur *welcome* → Supprimer

La SEQUENCE *experiment* est maintenant vide. Ajoutez un formulaire pour les instructions :

- Faites glisser un FORM_TEXT_DISPLAY depuis la barre d’outils (Form) dans *experiment*. Celui-ci affichera les instructions au début (nous définirons le texte des instructions à l’étape 12).

Ajoutez une LOOP avec une SEQUENCE pour la phase d’entraînement :

- Faites glisser une LOOP dans *experiment* (placez-la après le formulaire d’instructions).
- Faites glisser une SEQUENCE dans la LOOP et choisissez “Insérer dans [nom de la loop]”.

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur la structure LOOP/ SEQUENCE</summary>

Vous répétez souvent une séquence d’événements, comme un essai. Cela se fait généralement en combinant une LOOP, qui répète un seul item, et une SEQUENCE, qui exécute plusieurs items dans l’ordre.

Exemple : Un *block_loop* contient une *trial_sequence*, qui elle-même contient plusieurs items correspondant à un essai. Ensemble, cette structure LOOP/ SEQUENCE correspond à un bloc unique comprenant plusieurs essais.

</details>

Ajoutez un formulaire à la fin de l’entraînement

- Dans *experiment*, faites glisser un autre FORM_TEXT_DISPLAY et choisissez “Insérer après [nom de la loop d’entraînement]”. Ceci affichera un message de “fin d'entraînement” (Étape 12).

Ajoutez une LOOP pour la phase expérimentale, en réutilisant une copie liée de la même SEQUENCE que vous avez utilisée pour la LOOP d’entraînement :

- Faites glisser une LOOP et insérez-la après le formulaire de fin d’entraînement.
- Réutilisez la SEQUENCE que vous avez créée pour la LOOP d’entraînement :
  - Clic droit sur la SEQUENCE existante > Copier (lié).
  - Clic droit sur la nouvelle LOOP expérimentale > Coller > “Insérer dans [loop expérimentale]”.

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur les copies liées et non liées</summary>

Lorsque exactement le même item apparaît à plusieurs endroits, ce sont des copies liées. Les copies liées sont pratiques, car ainsi toute modification de l’item n’a à être effectuée qu’une seule fois.

Les copies non liées sont indépendantes les unes des autres, vous pouvez donc en modifier une sans affecter les autres.

Il est recommandé d’utiliser des copies liées autant que possible !

</details>

Ajoutez un formulaire d’au revoir :

- Faites glisser un FORM_TEXT_DISPLAY et insérez-le après la loop expérimentale.

Renommez les items pour plus de clarté :

- new_form_text_display → *instructions*
- new_loop → *practice_loop*
- new_sequence → *block_sequence* (les copies liées sont mises à jour automatiquement)
- new_form_text_display_1 → *end_of_practice*
- new_loop_1 → *experimental_loop*
- new_form_text_display_2 → *end_of_experiment*

Renommez l’expérience :

- Cliquez sur New experiment dans l’aperçu. Renommez en “Tutoriel : Gaze cuing”. Puis sauvegardez (Ctrl+S).

%--
figure:
 id: FigStep_1
 source: step1.png
 caption: |
  Overview at the end of Step 1.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur les différents types d’items</summary>

- SEQUENCE : Exécute les items dans l’ordre.
- LOOP : Répète un autre item, souvent une SEQUENCE, et définit les variables indépendantes.
- SKETCHPAD : Présente des stimuli visuels. Est préparé à l’avance, et convient donc aux stimuli nécessitant une synchronisation précise.
- FEEDBACK : Présente des stimuli visuels. N’est pas préparé à l’avance, et convient donc à la présentation de contenus actualisés, comme le retour sur les réponses d’un participant.
- KEYBOARD_RESPONSE : Récupère une réponse par pression d’une touche.
- SAMPLER : Joue un son à partir d’un fichier.
- LOGGER : Écrit des données dans un fichier.
- RESET_FEEDBACK : Réinitialise les variables de feedback au début d’un bloc.
- FORM_TEXT_DISPLAY : Affiche du texte en utilisant une disposition de formulaire.

</details>

## Étape 2 : Créer la séquence de blocs

🎯 __Objectif :__ Dans cette étape, nous allons à nouveau structurer notre expérience. Cette fois, nous allons implémenter la structure pour un seul bloc d’essais, qui correspond à *block_sequence*. Nous mettrons seulement en place la structure. Les détails seront implémentés ultérieurement.

Ouvrez *block_sequence* et ajoutez les items suivants dans l’ordre :

- RESET_FEEDBACK (pour réinitialiser les variables de feedback au début du bloc)
- LOOP avec une nouvelle SEQUENCE insérée (pour gérer la boucle effective et la logique des essais)
- FEEDBACK (pour fournir un feedback au participant à la fin du bloc)

Renommez

- new_reset_feedback → *reset_feedback*
- new_loop → *block_loop*
- new_sequence → *trial_sequence*
- new_feedback → *feedback*

%--
figure:
 id: FigStep_2
 source: step2.png
 caption: |
  Vue d’ensemble à la fin de l’étape 2.
--%


## Étape 3 : Remplir la boucle de bloc avec les variables indépendantes
 
🎯 __Objectif :__ Dans cette étape, nous allons définir les variables indépendantes (conditions) de notre expérience. Notre expérience est un exemple de plan complètement randomisé, ce qui signifie que les variables indépendantes varient d’un essai à l’autre.

Ouvrez *block_loop*. Cliquez sur Full-factorial design. Définissez :

- `gaze_cue` : left, right
- `target_pos` : -300, 300 (coordonnée x en pixels ; 0 = centre ; négatif = gauche)
- `target_letter` : F, H

Cela crée 2×2×2 = 8 combinaisons. Nous devons aussi définir plusieurs variables qui sont dérivées des variables ci-dessus. Pour cela, ajoutez manuellement une colonne pour chaque variable et saisissez les valeurs correctes dans chaque cellule.

- `dist_pos` : Pour chaque ligne, mettez 300 si `target_pos` vaut -300, et -300 si `target_pos` vaut 300
- `correct_response` : z pour F, m pour H
- `congruency` : congruent si le regard indique la direction de la cible, et incongruent sinon

Vérifiez que la table de la boucle comporte 8 lignes. Réglez ensuite Repeat sur 3 afin d’obtenir 3 × 8 = 24 essais par bloc.

%--
figure:
 id: FigStep_3
 source: step3.png
 caption: |
  La *block_loop* à la fin de l’étape 3.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur la table LOOP</summary>

- Vous pouvez copier-coller une table à partir d’un tableur, ou charger un fichier .csv/.xlsx en réglant Source sur file.
- Repeat peut être fractionnaire. Par exemple, en réglant repeat à 0.5, seule la moitié des lignes seront exécutées, sélectionnées de façon aléatoire.

</details>


## Étape 4 : Ajouter des images et fichiers audio à la banque de fichiers

🎯 __Objectif :__ Dans cette étape, nous allons utiliser la banque de fichiers pour intégrer les fichiers de stimuli (images et un son) à l’expérience.

Téléchargez les fichiers ci-dessous :

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Ouvrez la banque de fichiers (Ctrl+P) et glissez-y les fichiers. Ou bien utilisez le bouton + pour les ajouter. La banque de fichiers est automatiquement intégrée à votre expérience.

%--
figure:
 id: FigStep_4
 source: step4.png
 caption: |
  Banque de fichiers à la fin de l’étape 4.
--%

## Étape 5 : Remplir la séquence d’essai avec des items

🎯 __Objectif :__ Dans cette étape, nous allons définir la séquence d’un essai. Pour l’instant, nous allons seulement ajouter les items nécessaires sans les définir en détail. Nous ferons cela plus tard.

Un essai consiste en :

1. Point de fixation — 750 ms — SKETCHPAD  
2. Regard neutre — 750 ms — SKETCHPAD  
3. Indice de regard — 500 ms — SKETCHPAD  
4. Cible — 0 ms — SKETCHPAD (la durée de 0 ms permet à l'expérience de passer immédiatement à la collecte de la réponse)  
5. Collecte de la réponse — KEYBOARD_RESPONSE  
6. Son incorrect — SAMPLER (exécuté uniquement si la réponse est incorrecte)  
7. Log — LOGGER  

Ouvrez *trial_sequence*, ainsi que les items dans l'ordre indiqué ci-dessus. Une fois terminé, renommez-les :

- *new_sketchpad* → *fixation_dot*
- *new_sketchpad_1* → *neutral_gaze*
- *new_sketchpad_2* → *gaze_cue*
- *new_sketchpad_3* → *target*
- *new_keyboard_response* → *keyboard_response*
- *new_sampler* → *incorrect_sound*
- *new_logger* → *logger*

Dans *trial_sequence*, réglez "run-if" pour *incorrect_sound* sur : `correct == 0`. Il est important d'utiliser un double signe égal (`==`), qui vérifie si deux valeurs sont identiques, dans ce cas si `correct` est égal à 0. (Si vous utilisez accidentellement un seul signe égal, `correct = 1`, vous obtiendrez une `SyntaxError` lors de l'exécution de l'expérience.)

%--
figure:
 id: FigStep_5
 source: step5.png
 caption: |
  *trial_sequence* à la fin de l'étape 5.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur les variables et les expressions run-if</summary>

Les variables et les expressions conditionnelles (run-if) sont puissantes ! Voir %link:manual/variables%

</details>

## Étape 6 : Dessiner les items SKETCHPAD

🎯 __Objectif :__ Dans cette étape, nous allons définir les quatre items SKETCHPAD de la séquence d'essai : le point de fixation, le regard neutre (regarde droit devant), l'indice de regard (regarde à gauche ou à droite), et l'affichage de la cible (deux lettres de chaque côté de l'indice de regard, qui regarde encore à gauche ou à droite).

Définissez la couleur de fond de l'expérience sur blanc et la couleur de premier plan sur noir :

- Cliquez sur le titre de l'expérience pour ouvrir les propriétés générales
- Modifiez Background en 'white' et Foreground en 'black'

Définir le point de fixation :

- Ouvrez *fixation_dot*
- Sélectionnez l'élément fixdot. Il s'agit de l'icône du point de fixation dans la barre d'outils verticale à gauche du canevas.
- Tracez un point de fixation au centre de l'écran (0, 0)
- Définissez la durée à 745 ms. Celle-ci sera arrondie à la durée souhaitée de 750 ms.

<details class='info-box' markdown='1'>

<summary markdown='1'>Pourquoi spécifier une durée de 745 ms alors que vous souhaitez afficher un écran pendant 750 ms&nbsp;?</summary>

Les écrans se rafraîchissent périodiquement. Sur un moniteur 60 Hz, un cycle de rafraîchissement dure 1000 / 60 = 16,67 ms. Cela signifie que, sur un moniteur 60 Hz, la durée d'un affichage sera nécessairement un multiple de 16,67.

745 n'est *pas* un multiple de 16,67. Par conséquent, la durée sera arrondie au multiple supérieur le plus proche, c'est-à-dire 750.

Pour plus d'informations, voir :

- %link:timing%

</details>

Définir l'affichage du regard neutre :

- Ouvrez *neutral_gaze*
- Sélectionnez l'élément image
- Placez une image au centre de l'écran, et choisissez `gaze_neutral.png` dans la boîte de dialogue de la bibliothèque de fichiers qui s'affiche
- Définissez la durée à 745 ms

Définir l'affichage de l'indice de regard :

- Ouvrez *gaze_cue*
- Placez `gaze_left.png` au centre de l'écran

Bien entendu, nous ne souhaitons pas toujours afficher `gaze_left.png`. Nous voulons afficher `gaze_left.png` lorsque la variable `gaze_cue` vaut "left", et `gaze_right.png` lorsque la variable `gaze_cue` vaut "right". Autrement dit, nous voulons afficher `gaze_{gaze_cue}.png`, où les accolades indiquent qu'une variable doit être insérée.

Nous pouvons spécifier cela dans le script de l'item. Cliquez sur Select view (l'icône du milieu en haut à droite) → View script. Cela affiche le script OpenSesame qui définit l'item (ce n'est pas du Python ni du JavaScript !). Modifiez la commande `draw image` comme indiqué ci-dessous. Profitez-en également pour spécifier la durée (rappelez-vous que 495 ms sera arrondi à 500 ms, comme expliqué ci-dessus).

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Cliquez sur Appliquer. L’affichage revient maintenant à la vue des contrôles graphiques. L’image apparaît maintenant sous forme de point d’interrogation. Pas d’inquiétude ! L’image correcte sera affichée pendant l’expérience.

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur les variables existantes dans votre expérience</summary>

Ouvrez l’inspecteur de variables (Ctrl+I) pour voir quelles variables existent dans votre expérience. Lorsque l’expérience tourne, vous verrez même leurs valeurs changer en temps réel !

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: |
  L’inspecteur de variables.
--%

</details>

Définir l’affichage cible :

- Ouvrez *target*
- Dessinez `gaze_left.png` au centre de l’écran.
- Sélectionnez l’élément textline.
- Placez "{target_letter}" quelque part sur le côté gauche de l’écran. Les coordonnées exactes importent peu, car nous utiliserons ensuite une variable à cet emplacement. Comme précédemment, les accolades indiquent que la variable `target_letter` doit être insérée.
- Placez "X" quelque part sur le côté droit de l’écran.

Éditez le script de l’item (Sélectionnez Affichage → Afficher le script). Comme précédemment, l’indice de regard ("gaze cue") doit dépendre de la variable `gaze_cue`. De plus, la coordonnée X de la lettre cible doit dépendre de la variable `target_pos`, et la coordonnée X du "X" doit dépendre de la variable `dist_pos`.

Il est important de définir la durée à 0. Cela ne signifie pas que la cible est affichée pendant 0 ms. Cela signifie plutôt que l’expérience passe immédiatement à l’item suivant, qui est un KEYBOARD_RESPONSE. Autrement dit, la collecte de réponse commence dès que la cible est affichée !

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x="{target_pos}" y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="X" x="{dist_pos}" y=0 z_index=0
~~~

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur l’utilisation d’expressions de variables complexes dans le script OpenSesame</summary>

Dans le script OpenSesame, vous pouvez inclure des expressions complexes à l’aide des accolades. Par exemple, au lieu de spécifier `x="{dist_pos}"` pour le "X", nous aurions pu écrire `x="{-1 * target_pos}"`. Cela utilise les [littéraux de chaînes formatées en Python](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).

</details>


## Étape 7 : Configurer l’item keyboard_response

🎯 __Objectif :__ Dans cette étape, nous allons configurer les touches que les participants peuvent utiliser pour répondre, ainsi que la durée dont disposent les participants pour répondre.

Ouvrez *keyboard_response* :

- Laissez Réponse correcte vide. La variable `correct_response` (de l’étape 3) sera utilisée par défaut.
- Définissez Réponses autorisées sur `z;m`
- Définissez le Timeout à `2000` ms
- Laissez Type d’événement sur keypress

%--
figure:
 id: FigStep_7
 source: step7.png
 caption: |
  KEYBOARD_RESPONSE à la fin de l’étape 7.
--%


## Étape 8 : Configurer l’item sampler

🎯 __Objectif :__ Dans cette étape, nous allons spécifier quel son doit être joué après une mauvaise réponse.

Ouvrez *incorrect_sound*. Cliquez sur Parcourir et sélectionnez `incorrect.ogg` depuis la banque de fichiers.

%--
figure:
 id: FigStep_8
 source: step8.png
 caption: |
  *incorrect_sound* à la fin de l’étape 8.
--%


## Étape 9 : Configurer le logger

🎯 __Objectif :__ Dans cette étape, nous allons revoir la méthodologie de l’enregistrement des données.

Ouvrez *logger*. Par défaut, « Enregistrer automatiquement toutes les variables » est activé. C’est une bonne pratique, il n’est donc pas nécessaire de changer quoi que ce soit ici !

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur l’enregistrement de données personnalisé</summary>

Vous pouvez également exclure des variables spécifiques que vous ne souhaitez pas enregistrer. Vous pouvez aussi désactiver complètement l’enregistrement automatique et sélectionner manuellement les variables à enregistrer. Cela peut aider à garder les fichiers journaux clairs. Cependant, vérifiez toujours attentivement que toutes les variables requises sont enregistrées !

</details>

## Étape 10 : Dessiner l’item de feedback

🎯 __Objectif :__ Dans cette étape, nous allons définir le feedback que les participants recevront sur leurs performances à la fin de chaque bloc.

Ouvrez *feedback*. Laissez la durée sur 'keypress'. Ajoutez le texte suivant pour le feedback :

```text
Fin du bloc

Votre temps de réponse moyen était de {avg_rt} ms
Votre précision était de {acc} %

Appuyez sur une touche pour continuer
```

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: |
  *feedback* à la fin de l’étape 10.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur les variables de feedback</summary>

OpenSesame suit automatiquement les variables de feedback :

- `response` est la valeur de la dernière réponse. Exemples : "z", "left", etc.
- `correct` vaut 1 après une réponse correcte, et 0 après une réponse incorrecte
- `response_time` est le temps de réponse (en millisecondes) de la dernière réponse
- `acc` est le pourcentage de réponses correctes depuis la dernière réinitialisation des variables de feedback, ici par l’item RESET_FEEDBACK au début du bloc
- `avg_rt` est le temps de réponse moyen depuis la dernière réinitialisation des variables de feedback

Voir aussi :

- %link:manual/variables%

</details>

## Étape 11 : Régler le nombre de blocs pour la phase d’entraînement et la phase expérimentale

🎯 __Objectif :__ Dans cette étape, nous allons spécifier le nombre de blocs d’essais dans les phases d’entraînement et expérimentale.

Ouvrez *practice_loop* et réglez Répéter sur 2, afin d’avoir deux blocs d’entraînement. Ajoutez également une variable practice à la table de boucle, et mettez-la à 'yes'. Cela est pratique, car cela nous permettra d’identifier facilement les essais qui faisaient partie de la phase d’entraînement lors de l’analyse des données.

Ouvrez *experimental_loop* et réglez Répéter sur 8. Ajoutez à nouveau une variable practice mais cette fois, réglez-la sur 'no'.

## Étape 12 : Écrire les formulaires d’instructions, *end_of_practice* et *end_of_experiment*

🎯 __Objectif :__ Dans cette étape, nous allons ajouter des messages d’instructions informatifs tout au long de l’expérience.

Ouvrez les trois items FORM_TEXT_DISPLAY et saisissez des instructions brèves et claires. De bonnes instructions sont simples, complètes et spécifiques !

## Étape 13 : Lancer l’expérience !

🎯 __Objectif :__ Dans cette étape, nous allons effectuer un premier test de l’expérience !

La double flèche bleue dans la barre d’outils est le bouton Exécution rapide (Ctrl+Shift+W). Cela lance l’expérience dans une fenêtre en utilisant un numéro de sujet fictif et un emplacement de fichier journal temporaire. Ceci est principalement utile pendant le développement.

La simple flèche verte est le bouton Lancer en plein écran (Ctrl+R). Il demande d’abord un numéro de sujet et un fichier journal, et vous demande si vous voulez exécuter l’expérience en plein écran ou dans une fenêtre. Ceci est principalement utile lors de la collecte de données.

Appuyez sur un des deux boutons pour effectuer un test de l’expérience !

🏁 Si l’expérience fonctionne, vous avez terminé ! Mais avant de partir, examinons deux derniers points importants, liés au débogage et au choix du backend :

## Un débogage efficace et la compréhension des erreurs

Les erreurs sont normales lors de la construction d’expériences. Lisez les messages d’erreur attentivement, et essayez de comprendre ce qu’ils signifient. C’est la seule véritable voie vers un débogage efficace !

%FigErrorMessage montre un exemple de message d’erreur :

- Le type d’erreur est `FStringError`
- La description indique : « Échec lors de l’évaluation de l’expression f-string dans le texte suivant : `gaze_{gaze_ceu}.png` »
- L’erreur s’est produite dans la phase de préparation des items *gaze_cue*
- Le traceback est un message d’erreur Python. C’est une version plus technique de la description ci-dessus.

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: |
  Un message d’erreur dans OpenSesame.
--%

Une fois que vous avez compris d’où vient l’erreur, vous pouvez essayer de la corriger. Dans cet exemple, l’erreur provient d'une faute de frappe lors de la définition de l'item *gaze_cue* à l’étape 6. `gaze_{gaze_ceu}.png` devrait être `gaze_{gaze_cue}.png`. Facile à corriger !


<details class='info-box' markdown='1'>

<summary markdown='1'>En savoir plus sur le débogage efficace</summary>

Un débogage efficace est une compétence importante. L’apprendre vous fera gagner beaucoup de temps et vous évitera bien des frustrations ! Consultez le lien ci-dessous pour des conseils :

- %link:manual/debugging%

</details>


## Chronométrage et sélection du backend

Dans l’onglet ‘Propriétés générales’ de l’expérience (l’onglet que vous ouvrez en cliquant sur le nom de l’expérience), vous pouvez sélectionner un backend. Le backend est la couche logicielle qui contrôle l’affichage, les périphériques d’entrée, le son, etc. La plupart des expériences fonctionnent avec tous les backends, mais il existe des raisons de préférer l’un à l’autre, principalement liées au chronométrage. Il existe actuellement quatre backends :

- __psycho__ est le choix par défaut. Il est basé sur PsychoPy et fournit un excellent chronométrage [(Peirce, 2007)][references].
- xpyriment — est basé sur Expyriment et offre également un excellent chronométrage [(Krause & Lindemann, 2013)][references]
- legacy — est une option de secours qui fonctionne sur plus de systèmes mais offre un chronométrage moins précis
- osweb — exécute les expériences dans un navigateur [(Mathôt & March, 2022)][references]

Voir aussi :

- %link:backends%
- %link:timing%

## Points clés à retenir

Vous avez appris à construire une expérience simple mais complète !

- ✅ La structure d’une expérience est généralement construite en combinant des items SEQUENCE et LOOP
- ✅ Les variables sont généralement définies dans le tableau LOOP
- ✅ Les stimuli visuels sensibles au temps sont généralement présentés avec un SKETCHPAD
- ✅ Les retours aux participants sont généralement présentés avec des items FEEDBACK
- ✅ Le FORM_TEXT_DISPLAY est pratique pour la présentation de texte
- ✅ Les variables et expressions peuvent être insérées avec des accolades. Exemple : `{gaze_cue}`
- ✅ Les expressions Run-if sont définies dans une SEQUENCE et déterminent quels items sont effectivement exécutés : Exemple : `correct == 0`
- ✅ Vérifiez toujours le chronométrage et les fichiers journaux avec un test complet avant la collecte de données


## Prochaines étapes

Vous avez maintenant une compréhension de base d’OpenSesame. Cela suffit pour créer de nombreuses expériences simples. Cependant, vous pourriez avoir besoin ou envie d’en savoir encore plus ! Voici quelques prochaines étapes judicieuses :

- [Apprenez à construire des expériences avec SigmundAI](%url:beginner-sigmund%)
- [Apprenez à utiliser du code Python dans vos expériences](%url:intermediate%)
- [Apprenez à utiliser du code JavaScript dans vos expériences en ligne](%url:intermediate-javascript%)

## Références

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. Social Science Computer Review. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? Behavior Research Methods, 42, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. Psychonomic Bulletin & Review, 5, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. Behavior Research Methods. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. Behavior Research Methods, 44(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. Language Learning. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Résolution temporelle des horloges : Effets sur la mesure du temps de réaction—De bonnes nouvelles pour les mauvaises horloges. British Journal of Mathematical and Statistical Psychology, 42(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about