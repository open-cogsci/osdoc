---
layout: osdoc
title: Formation AMU Part 2
group: General
permalink: /aix2014-part2/
menuclass: external
ext_url: /aix2014-part2
show: True
authors: Lotje van der Linden
---

## Vue d'ensemble

%--
toc:
 mindepth: 2
 maxdepth: 3
 exclude: ["Vue d'ensemble"]
--%	

## Introduction

Vous allez apprendre à créer une expérience psychologique simple mais complet. On va utiliser principalement l'interface, combiné avec un petit peu de codage.
Les diapositives de cette formation peut être téléchargé d'[ici][slides]

### La question de recherche

On va créer une expérience 'gaze cuieing'. Un smiley est présenté au centre de l'écran. Les yeux du smiley régardent soit à droite, soit à gauche. La cible (la lettre "F" ou "H") est présenté soit à gauche, soit à droite. Un distractor (toujours la lettre "X") est présenté sur l'autre coté. La tâche du sujet est d'indiquer dés que possible, si la cible est la lettre "F" ou "H" en tapant cette lettre sur le clavier.

Les variables indépendantes principales sont: 
	
- La direction du regard (droite ou gauche)
- La position de la cible (droite ou gauche)

Ces deux facteurs sont croisés par un plan factoriel. Ce plan factoriel donne lieu à une nouvelle variable, *Congruence*, qui obtient la valeur 'congruent' si le smiley regarde à la direction de la cible, et la valeur 'non-congruente' si le smiley regarde à la direction du distractor.

%--
figure:
 id: crossed
 source: crossed.png
 caption: |
  Le plan factoriel 
--%

Notre dernières 2 variables indépendante sont:
	
- La lettre de la cible: H ou F
- La position de la distractor (droit ou gauche, toujours à la position opposé de la cible)

L'hypothèse est que le sujet va identifier la cible plus rapidement dans la condition congruente par rapport au condition incongruente. Cela montrera que notre attention visuelle est automatiquement guidé par le regard des autres, même dans les situations où cela ne sert pas un but (parce que le regard du smiley ne prédit pas la position de la cible).

%--
figure:
 id: hypothesis
 source: hypothesis.png
 caption: |
  L'hypothèse
--%


### La séquence d'essai

Pour tester notre hypothèse, on va créer une expérience avec la séquence d'essai suivante: 

%--
figure:
 id: trialSeq
 source: trialSeq.png
 caption: |
  La séquence d'essai
--%
	
### Hiérarchie de l'expérience

La structure de la séance experimentale est comme suit:
	
- Une phase d'entrainement (2 blocs de 8 essais)
- Une phase expérimentale (8 blocs de 8 essais)

%--
figure:
 id: hierarchy
 source: hierarchy.png
 caption: |
  La structure hierarchique
--%

## Création d'une expérience simple

### Étape 1 : Démarrer OpenSesame

Pour économiser du temps, on va utiliser le modèle étendu. Double-cliquez sur l'Extended template dans l'onglet 'Lancez-vous!'.

%--
figure:
 id: startup
 source: startup.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

La vue d'ensemble montre la structure hiérarchique de l'Extended template.  

%--
figure:
 id: vue
 source: vue.png
 caption: |
  La vue d'ensemble.
--%

La structure hiérarchique de la vue d'ensemble ressemble déjà beaucoup la structure schématique qui est représentée par %hierarchy. Cette ressemblance montre que c'est souvent utile de commencer par l'Extended template.

- Registrez votre nouvelle expérience en cliquant l'icône 'Enregistrer' de la barre d'outils principale.

### Étape 2 : Definir les variables indépendantes

#### La position de la cible en pixels

On commence par 'traduire' les valeurs de la variable 'Position de la Cible' vers des coordonnées *x*, par rapport au centre de l'écran, en pixels:
	
- Si la position de la cible apparait à gauche, sa coordonnée *x* est 300 px
- Si la position de la cible apparait à droit, sa coordonnée *x* est -300 px
	
#### Le plan factoriel

On a trois variables indépendantes qui doivent être croisées les uns avec les autres:

- La direction du regard (droite ou gauche)
- La position de la cible (300 ou -300 px)
- La lettre de la cible (H ou F)

En total, ça donne 2 * 2 * 2 = 8 combinaisons différentes. Ces 8 conditions constituent la liste d'essais d'un bloc (voyez %hierarchy). Cette liste doit être rempli dans l'élément *block_loop*.  
On n'a pas besoin de taper toutes ces 8 combinaisons manuellement. Au lieu de cela, nous utilisons l'*Assistant de variables*, qui va nous générer un *plan factoriel*.

Pour exécuter cette opération:

- Sélectionnez l'élément *block_loop* de la vue d'ensemble
- Cliquez sur le bouton *Assistant de variables* dans l'onglet du *block_loop*
- Tapez les noms de variables sur la première ligne de l'Assistant de variables
- Remplissez les deux colonnes en tapant chaque niveau de la variable. 
- Cliquez 'Ok'

Vous voyez que OpenSesame a généré notre entière liste d'essais.

%--
figure:
 id: blockloop1
 source: blockloop1.png
 caption: |
  La liste des essais après avoir rempli le plan factoriel dans l'Assistant de variables.
--%

*Attention:* Le *practice_loop* (phase d'entrainement) et l'*experimental_loop* déroulent la même *block_sequence*. Par conséquence, tous les changements que nous faisons dans la *block_sequence* ou des niveaus au dessous, sont automatiquement appliqué à ses deux parties de l'expérience.

#### La bonne réponse

Il est souvent pratique de dire OpenSesame quelle est la bonne réponse par essai en définissant la variable 'correct_response'. Ça permet OpenSesame de suivre les variables de la performance, comme 'acc' ('accuracy' ou pourcentage correct).  
Pour dire OpenSesame quelle est la bonne réponse sur chaque essai:
	
- Cliquez sur le bouton 'Ajouter une variable'
- Ecrivez 'correct_response' (avec une 's'!) et appuyez sur 'Enter'
- Maintenant, on a créé un colonne vide pour la nouvelle variable. Il faut donc le remplir. 
	- Pour chaque ligne contenant un vrai mot, mettez 'm' comme bonne réponse. 
	- Pour chaque ligne contenant un non-mot, mettez 'q'.
	
#### La position du distractor

Il nous reste une dernière variable a ajouter: la position du distractor en pixels. Comme dit, le distractor apparait toujours à la position opposé de la cible. Donc, sa coordinate x, en pixels, et l'inverse de la coordinate x de la cible (%cross). Pour ajouter cette information vers le *block_loop*:
	
- Cliquez sur le bouton 'Ajouter une variable'
- Ecrivez 'x_distractor' et appuyez sur 'Enter'
- Maintenant, on a créé un colonne vide pour la nouvelle variable. Il faut donc le remplir. 
	- Pour chaque ligne ou la position de la cible est 300 -> mettez 'x_distractor' vers -300
	- Pour chaque ligne ou la position de la cible est -300 -> mettez 'x_distractor' vers 300

%--
figure:
 id: blockloop2
 source: blockloop2.png
 caption: |
  Le résultat après avoir ajouté les dernières deux variables, correct_response et x_distractor, vers la liste d'essais.
--%

### Étape 3 : Ajouter des éléments à la séquence d'essai

Comme montre la %trialSeq, l'objectif est de construire une séquence d'essai comme suit:
	
1. Présenter une point de fixation (750 ms)
2. Présenter un smiley neutre (750)
3. Présenter l'indice (500 ms)
4. Présenter la cible et le distractor
5. Collecter une réponse sur le clavier
6. Enregistrer toutes les valeurs dans un fichier de sortie

On s'appelle ces 6 étapes *des événements*. On va réaliser ces 6 événements en ajoutant des *éléments* vers le *trial_sequence* de notre expérience.  

Pour les premiers 4 événements, on utilisera des éléments `sketchpad`. Cependant, pour l'instant, notre *trial_sequence* ne contient qu'un seul élément `sketchpad`. Il faut donc en ajouter encore 3.  
Pour ajouter ces 3 éléments `sketchpad`:

- Regardez la barre d'outils à l'extrème gauche de l'écran OpenSesame
- Choisissez l'élément `sketchpad`
- Faites glisser l'élément vers la *trial_sequence* dans la vue d'ensemble.
- *Attention:* Pour faire apparaitre un élément *au dessous* d'un autre élément, déposez-le *sur* cet autre élément.
- Répétez la procédure glisser-déposer jusqu'à ce que vous avez 4 éléments `sketchad` dans votre *trial_sequence*. 

%--
figure:
 id: dragdrop
 source: dragdrop.png
 caption: |
  Glisser-déposer des éléments (ici: des `sketchpads`) de la barre d'outils vers la vue d'ensemble.
--%

Par défaut, OpenSesame attribue des noms tels que "__sketchpad" aux éléments nouvellement crées. Ces noms ne sont pas très informative. Il est donc forcement recommandé de les changer.  
Pour réaliser ça:
	
- Clic droit sur un élément dans la vue d'ensemble
- Choisissez 'Renommer'
- Changez le nom
- Appelez les éléments `sketchpad` *fixation*, *regard_neutre*, *regard_direction* et *cible*, respectivement.

%--
figure:
 id: renamed
 source: renamed.png
 caption: |
  La vue d'ensemble avant et après avoir renommé des éléments `sketchpad`
--%

Les derniers deux événements de la séquence d'essai(collecter la réponse et enregistrer les données) sont sont déjà répresentés par les éléments `keyboard_response` et `logger`, respectivement.

### Étape 4: Préparer le groupe de fichiers:

Pour notre expérience, on aura besoin de trois images: un smiley neutre, un smiley qui regarde à droite et un smiley qui regarde à gauche. 
Vous pouvez télécharger ces trois images d'ici:
	
- [gaze_neutral.png](/attachments/gaze-cuing/gaze_neutral.png)
- [gaze_left.png](/attachments/gaze-cuing/gaze_left.png)
- [gaze_right.png](/attachments/gaze-cuing/gaze_right.png)

Après avoir téléchargé les images, on va les ajouter vers le groupe de fichiers de notre expérience: 
	
- Cliquez sur le bouton 'Montrer le groupe de fichiers'
- Dans la fenêtre 'Groupe de fichiers', cliquez sur le signe '+'
- Choisissez les fichiers que vous voulez ajouter

%--
figure:
 id: filepool
 source: filepool.png
 caption: |
  Le groupe de fichiers après avoir ajouté des images.
--%

### Étape 5: Créer les éléments de la séquence d'essai

On va créer les `sketchpad`s grâce aux 'drawing tools' (des outils de dessin) de ces éléments. 

#### fixation

Le `sketchpad` fixation est un `sketchpad` *invariable*. Ça veut dire que cette partie de la séquence d'essai ne change pas d'un essai à l'autre.

- Ouvrez l'onglet *fixation* en cliquant sur cet élément dans la vue d'ensemble.
- Comme vous voyez, grâce à l'Extended template, le point de fixation est déjà dessiné. 

Cependant, il faut qu'on fasse un petit changement sur cet élément. Actuellement, la durée de ce `sketchpad` est mis sur '0'. Ça veut dire que le point de fixation sera présenté pendant 0 millisecondes. Bien sur, ce n'est pas ce qu'on veut. On veut que le point de fixation sera présenté par 750 ms (voyez %trialSeq), et que, aprés, l'expérience avance automatiquement.  
Pour réaliser ça:
	
- Changez la durée vers '750'.

%--
figure:
 id: fixation
 source: fixation.png
 caption: |
  Le sketchpad `fixation`
--%

#### regard_neutre

Le `sketchpad_neutre` est également un `sketchpad` *invariable*.

- Ouvrez l'onglet *fixation* en cliquant sur cet élément dans la vue d'ensemble.
- Sélectionnez l'outil Image (%neutral)
- Cliquez sur le centre du `sketchpad`
- Choisissez l'image 'regard_neutre.png' pour y insérer
- Mettez la durée vers 750

%--
figure:
 id: neutral
 source: neutral.png
 caption: |
  Le sketchpad `fixation`
--%

#### regard_direction

Contrairement aux dernières deux `sketchpad`s, le `sketchpad` *regard_direction* est *variable*. Ça veut dire que ses propriétés sont *variés* entre essais, et qu'elles *dépendent* des valeurs dans la liste de bloc (*block_loop*). Pour indiquer à OpenSesame qu'il s'agit d'un `sketchpad` variable, on utilise la méthode *entre-crochets*. Après, on laisse décider OpenSesame quelle condition (ex. regard droit ou regard gauche) sera présentée sur chaque essai, au base des valeurs dans la liste *block_loop*.

- Ouvrez l'onglet *regard_direction* en cliquant sur cet élément dans la vue d'ensemble
- Sélectionnez l'outil Image (%cue)
- Cliquez sur le centre du `sketchpad`
- Choisissez l'image 'regard_gauche.png'
- Affichez le code du `sketchpad` en cliquant l'icone 'Select view'. 

%--
figure:
 id: cue
 source: cue.png
 caption: |
  Affichez le code du `sketchpad en cliquant l'icone 'Select view'. 
--%

Le code a besoin d'un petit modification, en utlisant la méthode *entre-crochets*.

Au début, le code du `sketchpad` *regard_direction* ressemble à:
	
{% highlight python %}
set duration "500"
draw image 0 0 "regard_gauche.png" scale=1 center=1 z_index=0 show_if="always"
{% endhighlight %}

La seule chose que nous avons à faire, est de remplacer '_gauche' vers '[direction_regard]'. Cela signifie que OpenSesame utilise la variable 'direction_regard' (qui a les valeurs 'droite' et 'gauche') pour déterminer quelle image doit être montrée:

{% highlight python %}
set duration "500"
draw image 0 0 "regard_[direction_regard].png" scale=1 center=1 z_index=0 show_if="always"
{% endhighlight %}

- Faites ce changement au code du `sketchad`
- Cliquez sur 'Appliquer et fermer' pour appliquer les modifications
- Mettez la durée vers 750

*Attention:* Parce que les propriétés du `sketchpad` *regard_direction* changent pour chaque essai, le `sketchpad` ne montre plus l'image qu'on avait initialement insérée. Mais ne vous inquietez pas. Elle sera bien montrée pendant l'exécution de l'expérience.

#### cible

Le `sketchpad` *cible* est également un sketchpad *variable*. Donc, on utilise encore une fois la méthode entre-crochets. Dans ce `sketchpad`, on a même 3 variables qui sont variées:
	
1. La lettre de la cible (F ou H)
2. La coordonnée x de la cible (-300 ou 300)
3. La coordonnée x du distractor (-300 ou 300)

Pour commencer, il faut repétez toutes les étappes du sketchpad *regard_direction* pour assurer que le smiley indice reste sur l'écran.

Ensuite, il faut montrer la cible et le distractor:
	
- Sélectionnez l'outit Texte
- Cliquez quelquepart à gauche du centre et taper 'F'
- Cliquez quelquepart à gauche du centre et taper 'X'
- Affichez le code en cliquant 'select view'

%--
figure:
 id: cible
 source: cible.png
 caption: |
  Ajoutez la cible est le distractor en utilisant l'outil Texte (l'icone A). 
--%

On va encore une fois faire quelques modifications du code. Au début, votre code devrait ressemble à:

{% highlight python %}
set duration "keypress"
draw image 0 0 "regard_[direction_regard].png" scale=1 center=1 z_index=0 show_if="always"
draw textline -256 0 "F" center=1 color="white" font_family="mono" font_size=18 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
draw textline 288 0 "X" center=1 color="white" font_family="mono" font_size=18 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
{% endhighlight %}

Pour varier la lettre de la cible, et les coordonnées x de la cible et du distractor sur la base de la liste d'essai:
	
- changez la lettre "F" vers [lettre_cible]
- changez la coordonnée x de la cible vers [x_cible]
- changez la coordonnée x du distractor vers [x_distractor]

Par conséquence, votre code devrait ressemble à:
	
{% highlight python %}
set duration "keypress"
draw image 0 0 "regard_[direction_regard].png" scale=1 center=1 z_index=0 show_if="always"
draw textline "[x_cible]" 0 "[lettre_cible]" center=1 color="white" font_family="mono" font_size=18 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
draw textline "[x_distractor]" 0 "X" center=1 color="white" font_family="mono" font_size=18 font_bold="no" font_italic="no" html="yes" z_index=0 show_if="always"
{% endhighlight %}
	
Finalement, on met la durée du `sketchpad` *cible* sur 0 ms. Ça peut vous sembler contre-intuitif, mais ça veut juste dire que OpenSesame va initialiser la prochaine élément (ici, *keyboard_response*) tout de suite. L'élément *keyboard_response* lui même ne change pas ce qui est actuellement montrer au sujet sur l'écran. Donc, en somme, le dernier `sketchpad` reste sur l'écran jusqu'à le sujet a appuyé sur une touche.

#### keyboard_response

Cliquez sur `keyboad_response` dans la vue d'ensemble, pour ouvrir son onglet. Vous voyez 3 options, Correct response, Allowed responses, et Timeout.

- Correct response: on a déjà indiqué la variable *correct_response* dans le block_loop, donc on n'a pas besoin de le mettre ici. Si nous le faisons, nous allons tout simplement annuler la réponse correcte précédemment défini, qui est certainement pas ce que nous voulons.
- Allowed responses (réponses authorisées): Entrez 'z; m' dans le champ-réponses autorisées. Le point-virgule est utilisé pour des réponses distinctes. Le keyboard_response accepte maintenant seulement les touches 'm' 'z' et. Tous les autres touches sont ignorés, à l'exception de'esc', ce qui interrompt l'expérience.
- Timeout (délai): Nous voulons également définir un délai, qui est l'intervalle maximal que la keyboard_response attend avant de décider que la réponse était incorrecte. «2000» (ms) est une bonne valeur. Si un 'Timeout' arrive:
	- La variable dépendante "correct" obtient le valeur 0
	- La variable "réponse" obtient le valeur 'timeout'

%--
figure:
 id: keyboard_response
 source: keyboard_response.png
 caption: |
  L'élément *keyboard_response*.
--%

### Étape 6 : La séquence de session

Le niveau le plus haut de notre structure hierarchique répresente la sequence de la session experimentale entière (%hierarchy). C'est sur ce niveau qu'on va régler la longeur de la phase d'entrainement et la longeur de la phase experimentalle. On veut que la phase d'entrainement dure que 2 blocs, et que la phase expérimentale dure 8 blocs.

Cependant, maintenant, *practice_loop* et *experimental_loop* déroulent la séquence de bloc qu'une seule fois. Pour changer ça:
	
- Cliquez sur 'practice_loop' pour ouvrir son onglet.
- Mettez 'Répéter' vers 2. Cela signifie que la phase d'entrainement se compose de deux blocs
- Cliquez sur 'experimental_loop' pour ouvrir son onglet
- Mettez 'Répéter' vers 8. Cela signifie que la phase d'entrainement se compose de huit blocs

%--
figure:
 id: practice_loop
 source: practice_loop.png
 caption: |
  L'élément *practice_loop* après avoir mis le nombre de répétitions vers 2.
--%

#### Les consignes

Pour l'instant, les consignes ne sont pas très informative pour le sujet. Ouvrez l'onglet 'instructions' et changez la texte vers des instructions qui sont plus clairs pour le sujet. Mettez également la texte dans les éléments *end_of_practice* et *end_of_experiment* en français.

### Étape 7 : Tester l'expérience

Félicitations!! Vous avez construit une expérience entièrement fonctionnel !
Donc, c'est le temps pour la tester. Pour exécuter votre expérience :
	
- Cliquez une des flèches vertes
- Entrez un numéro de sujet (par ex. '1')
- Une fênetre s'ouvre qui indique le nom de défaut du fichier de sortie. Si vous n'aimez pas ce nom, vous pouvez le changer
- Cliquez 'save'
- L'expérience sera lancé. Vous pouvez prétendre que vous êtes un participant, pour vérifier si l'expérience fonctionne comme on le souhaite

Si vous n'avez pas envie de dérouler l'expérience entière (2 fois 12 essais) vous pouvez aborter l'expérience en appuyant la touche 'Esc' sur le clavier. Ça interrompt immédiatement l'exécution de l'expérience, de sorte que vous pouvez continuer de la programmer.

Après d'avoir exécuté (un part de) votre expérience, vous pouvez voir si vos variables sont enrégistrées correctement dans le fichier de sortie.

%--
figure:
 id: run
 source: run.png
 caption: |
  Exécutez l'expérience.
--%

### Étape 8 : Donner du feedback après chaque essai

On va donner le sujet du feedback sur son performance apres chaque essai. Plus précisement, on va jouer un petit son si le sujet fait un erreur. Si sa répond est juste, il ne va entendre rien.

#### Ajouter le son vers le groupe de fichiers

#### Créer un élément `sampler`

- Selectionner un élément sampler et glisser le vers la vue d'ensembe, juste aprés le `keyboard_response`. 
- Renommez-le vers 'incorrect'.

#### Indiquer le fichier de son

Vous pouvez télécharger le fichier de son d'ici:
	
- [incorrect.ogg](/attachments/gaze-cuing/incorrect.ogg)
	
Après avoir téléchargé les images, on va les ajouter vers le groupe de fichiers de notre expérience: 

%--
figure:
 id: filepool_with_sound
 source: filepool_with_sound.png
 caption: |
  Le groupe de fichiers après avoir ajouté des images..
--%

Ensuite:
	
- Ouvrez l'onglet de l'élément *incorret*:
- Cliquez sur 'Naviguer'
- Sélectionnez le fichier 'incorrect.ogg'
	
%--
figure:
 id: sound
 source: sound.png
 caption: |
  L'élément *incorrect*
--%

#### Utilisez une déclaration 'run-if'

Pendant chaque essai, la précision du réponse du participant est enregistrée comme la variable *correct*:
	
- Si le participant répond correctement, la variable 'correct' obtient la valeur 1
- Si le participant répond mal, la variable 'correct' obtient la valeur 0

L'élément `incorrect_sound` ne doit être executée que si la réponse du sujet était faux. Cliquez sur l'élément *trial_sequence* dans la vue d'ensemble'. Un onglet s'ouvre, qui donne une vue d'ensemble de chaque événement de la séquence. À droite, on voit les déclarations 'Run-if'. Ils indiquent dans quelles circonstances OpenSesame exécutera chaque élément. Maintenant, ils sont tous exécutés 'always' ('toujours'). Ce valeur est correct pour tous nos éléments, sauf l'élément `incorrect_sound`. Effectivement, cette élément doit être executée seulememt si la réponse du sujet était faux. Pour programmer ça, il faut changer sa déclaration 'Run-if' vers :

- [correct] = 0  
	
Par conséquence, le sujet entendra le bip seulement si il a fait un erreur.

%--
figure:
 id: runif
 source: runif.png
 caption: |
  On utilise des déclarations 'Run-if' pour réaliser qu'une partie de la séquence d'essai dépend des variables collectées en ligne.
--%

### Étape 9 : Add a questionnaire


### Étape 10 : Fini !

Votre expérience est maintenant terminée. Exécutez-la, pour la tester.

## Extra

## Références

Math&ocirc;t, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social science. *Behavior Research Methods*, *44*(2), 313-324. doi:10.3758/s13428-011-0168-7
{: .reference}

[download]: /getting-opensesame/download/
[feedback]: /usage/feedback/
[forms]: /forms/about/
[forms-opensesame]: /forms/custom-forms/#opensesame-script
[forms-performance]: /forms/performance-issues-and-troubleshooting/
[forms-python]: /forms/custom-forms/#python
[slides]: /attachments/Formation_OpenSesame_Aix_2014.pdf
[variables]: /usage/variables-and-conditional-statements/#using-variables
[responses]: /usage/collecting-responses/
[tutorial]: /usage/step-by-step-tutorial/
[html-subset]: /usage/text-formatting/
[aps-page]: http://aps.psychologicalscience.org/convention/program_2013/search/viewProgram.cfm?Abstract_ID=26153
[smep]: http://www.smep.org/
[pdf]: /aps2013/index.pdf
[prepare-run]: /usage/prepare-run/#sketchpad-feedback
