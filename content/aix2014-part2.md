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

TODO

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

On va créer une expérience 'gaze cuieing'. Un visage est présenté au centre de l'écran. Les yeux du visage régardent soit à droite, soit à gauche. La cible (la lettre "F" ou "H") est présenté soit à gauche, soit à droite. Un distracteur (toujours la lettre "X") est présenté sur l'autre coté.

La tâche du sujet est d'indiquer dés que possible, si la cible est la lettre "F" ou "H". 

Les variables indépendantes sont: 
	
- La direction du regard (droit ou gauche)
- La position de la cible (droit ou gauche)

Ces deux facteurs sont croisées avec un plan factoriel. Ça donne une autre variable: Congruence. La variable Congruent a deux niveaux: la condition congruente (ou le regard est dirigé vers la cible) vs la condition non-congruente (le regard est dirigé vers le distracteur).

Notre dernières 2 variables indépendante sont:
	
- La lettre de la cible: H ou F
- La position de la distractor (droit ou gauche, toujours à la position opposé de la cible)

L'hypothèse est que le sujet va identifier la cible plus rapidement dans la condition congruente par rapport au condition incongruente. Cela montrera que notre attention visuelle est automatiquement guidé par le regard des autres, même dans les situations où cela ne sert pas un but (parce que le regard du smiley ne prédit pas la position de la cible).

### La séquence d'essai

Pour tester notre hypothèse, on va créer une expérience avec la séquence d'essai suivante: 

- Point de fixation (750 ms)
- Neutral gaze (750)
- Gaze cue (500 ms)
- Target (0 ms)
- Response collection
- Feedback
- Log
	
- Si la cible est une H:
- Si la cible est une F:

### Hiérarchie de l'expérience

La structure de la séance experimentale est comme suit:
	
- Un bloc d'entrainement (seulement 10 essais)
- Un block expérimentale


## Création d'une expérience simple

### Étape 1 : Démarrer OpenSesame

Lorsque vous démarrez OpenSesame, vous recevrez un menu qui vous permet de choisir entre:
	
- Ouvrir une expérience qui était récemment ouverte
- Ouvrir une autre expérience déjà existante
- Créer une nouvelle expérience ...
	- complètement vide ('Default template')
	- modèle étendu, qui est déjà partiellement programmé ('Extended template')

Pour économiser du temps, on va utiliser le modèle étendu. Double-cliquez sur l'Extended template dans l'onglet 'Lancez-vous!'.

La vue d'ensemble montre la structure hiérarchique de l'Extended template.  
La structure hiérarchique de la vue d'ensemble ressemble déjà beaucoup la structure schématique qui est représentée par %hierarchy. Cette ressemblance montre que c'est souvent utile de commencer par l'Extended template.

Ensuite, on enregistre notre nouvelle expérience 

- En cliquant l'icône 'Enregistrer' de la barre d'outils principale.

### Étape 2 : Definir les variables indépendantes

Comme dit, nous avons deux variables indépendantes:

- Lettre: H ou F
- Direction du regard: droit et gauche
- Position de la cible: droit et gauche

On commence par 'traduire' les valeurs de la deuxième variable, Position de la cible, vers un coordinate x, par rapport au centre de l'écran, en pixels:

- Si la position de la cible apparait à gauche, sa coordinate X est 300 px par rapport au centre de l'écran
- Si la position de la cible apparait à droit, sa coordinate X est -300 px par rapport au centre de l'écran

En total, ça donne 2 * 2 * 2 = 8 combinaisons différentes. Ces 8 conditions constituent la liste d'essais d'un bloc (voyez %hierarchy). Cette liste doit être rempli dans l'élément *block_loop*.  
On n'a pas besoin de taper toutes ces 8 combinaisons manuellement. Au lieu de cela, nous utilisons l'*Assistant de variables*, qui va nous générer un *plan factoriel*.

Pour exécuter cette opération:

- Sélectionnez l'élément *block_loop* de la vue d'ensemble
- Cliquez sur le bouton *Assistant de variables* dans l'onglet du *block_loop*
- Tapez les noms de variables sur la première ligne de l'Assistant de variables
- Remplissez les deux colonnes en tapant chaque niveau de la variable. 
- Cliquez 'Ok'

Vous voyez que OpenSesame a généré notre entière liste d'essais.

Il est souvent pratique de dire OpenSesame quelle est la bonne réponse par essai en définissant la variable 'correct_response'. Ça permet OpenSesame de suivre les variables de la performance, comme 'acc' ('accuracy' ou pourcentage correct).  
Pour dire OpenSesame quelle est la bonne réponse sur chaque essai:
	
- Cliquez sur le bouton 'Ajouter une variable'
- Ecrivez 'correct_response' (avec une 's'!) et appuyez sur 'Enter'
- Maintenant, on a créé un colonne vide pour la nouvelle variable. Il faut donc le remplir. 
	- Pour chaque ligne contenant un vrai mot, mettez 'm' comme bonne réponse. 
	- Pour chaque ligne contenant un non-mot, mettez 'q'.
	
Il nous reste une variable a ajouter: la position du distractor. Comme on a dit, le distracteur apparait toujours à la position opposé de la cible. Donc, sa coordinate x, en pixels, et l'inverse de la coordinate x de la cible. Pour ajouter cette information vers le *block_loop*:
	
- Cliquez sur le bouton 'Ajouter une variable'
- Ecrivez 'x_distractor' et appuyez sur 'Enter'
- Maintenant, on a créé un colonne vide pour la nouvelle variable. Il faut donc le remplir. 
	- Pour chaque ligne ou la position de la cible est 300 -> mettez 'x_distractor' vers -300
	- Pour chaque ligne ou la position de la cible est -300 -> mettez 'x_distractor' vers 300

### Étape 3 : Ajouter des éléments à la séquence d'essai

Comme montre la %trialSeq1, l'objectif est de construire une séquence d'essai comme suit:
	
1. Présenter le point de fixation
2. Présenter Neutral gaze
3. Présenter Gaze cue
4. Présenter la Cible
5. Collecter une réponse sur le clavier
6. Feedback
7. Enregistrer toutes les valeurs dans un fichier de sortie

On s'appelle ces 6 étapes *des événements*. On va réaliser ces 6 événements en ajoutant des *éléments* vers le *trial_sequence* de notre expérience.  

Pour les premiers 4 événements, on utilisera des éléments `sketchpad`. Cependant, pour l'instant, notre *trial_sequence* ne contient qu'un seul élément `sketchpad`. Il faut donc en ajouter encore 3.

Pour ajouter ces 3 éléments `sketchpad`:

- Regardez la barre d'outils à l'extrème gauche de l'écran OpenSesame
- Choisissez l'élément `sketchpad`
- Faites glisser l'élément vers la *trial_sequence* dans la vue d'ensemble.
- *Attention:* Pour faire apparaitre un élément *au dessous* d'un autre élément, déposez-le *sur* cet autre élément.
- Répétez la procédure glisser-déposer jusqu'à ce que vous avez 4 éléments `sketchad` dans votre *trial_sequence*. 

Par défaut, OpenSesame attribue des noms tels que "__sketchpad" aux éléments nouvellement crées. Ces noms ne sont pas très informative. Il est donc forcement recommandé de les changer. 

Pour réaliser ça:
	
- Clic droit sur un élément dans la vue d'ensemble
- Choisissez 'Renommer'
- Changez le nom
- Appelez les éléments `sketchpad` *fixation*, *amorce*, *intervalle* et *cible*, respectivement.

Les derniers deux événements de la séquence d'essai, (collecter la réponse et enregistrer les données) sont sont déjà répresentés par les éléments `keyboard_response` et `logger`, respectivement.


SAY THAT IT ALSO CHANGES IN PRACTICE LOOP!

### Étape 4 : Créer les éléments *fixation*, *amorce*, *intervalle* et *cible*

#### fixation

Maintenant, on va créer le content des éléments `sketchpad` grâce aux 'drawing tools' (des outils de dessin) de ces éléments. On commence avec le `sketchpad` *fixation*.

- Ouvrez l'onglet *fixation* en cliquant sur cet élément dans la vue d'ensemble.
- Comme vous voyez, grâce à l'Extended template, le point de fixation est déjà dessiné. 

Cependant, il faut qu'on fasse un petit changement sur cet élément. Actuellement, la durée de ce `sketchpad` est mis sur '0'. Ça veut dire que le point de fixation sera présenté pendant 0 millisecondes. Bien sur, ce n'est pas ce qu'on veut. On veut que le point de fixation sera présenté par 750 ms (voyez %trialSeq1), et que, aprés, l'expérience avance automatiquement.  
Pour réaliser ça, il faut changer la durée vers '7'.

#### neutral



#### gaze cue

Pour le point de fixation, on a créé un `sketchpad` *invariable*. Un `sketchpad` invariable montre la même chose (ici: un point de fixation pendant 750 ms) sur chaque essai.

On peut également créer des `sketchpad`s *variables*. Ça veut dire que le contient du `sketchpad` est défini par une variable indépendente. Grâce aux `sketchpad`s variables, on ne doit pas créer beaucoup des `sketchpad`s différents pour chaque essai. Au lieu de ça, on en crée qu'un, et on laisse décider OpenSesame quel condition (ex. regard droit ou regard gauche) sera présenté sur chaque essai, au base des valeurs dans la liste *block_loop*.

Pour indiquer à OpenSesame qu'il s'agit d'un `sketchpad` variable, on utilise la méthode *entre-crochets*. La méthode entre-crochets fonctionne comme suit:
	
- Ouvrez l'onglet *TODO* en cliquant sur cet élément dans la vue d'ensemble

TODO

- Enfin, mettez la durée du `sketchpad` sur 500 ms

Les crochets indique que nous avons affaire à une texte variable. Donc, au lieu de présenter '[amorce]' sur l'écran, OpenSesame présentera la valeur de la variable (i.e. 'XXXXXX' ou 'ANIMAL') comme tirée de la liste *block_loop*.


#### cible

Le `sketchpad` *cible* est également un sketchpad *variable*. Donc, on utilise encore une fois la méthode entre-crochets. La seule différence est que, cette fois, on va mettre la coordinate x entre crochets, dans le script!!

Ensuite, on met la durée du `sketchpad` *cible* sur 0 ms. Ça peut vous sembler contre-intuitif, mais ça veut juste dire que OpenSesame va initialiser la prochaine élément (ici, *keyboard_response*) tout de suite. L'élément *keyboard_response* lui même ne change pas ce qui est actuellement montrer au sujet sur l'écran.

Donc, en somme, le stimulus reste sur l'écran jusqu'à le sujet a appuyé sur une touche.

#### keyboard_response

Cliquez sur `keyboad_response` dans la vue d'ensemble, pour ouvrir son onglet. Vous voyez 3 options, Correct response, Allowed responses, et Timeout.

- Correct response: on a déjà indiqué la variable *correct_response* dans le block_loop, donc on n'a pas besoin de le mettre ici. Si nous le faisons, nous allons tout simplement annuler la réponse correcte précédemment défini, qui est certainement pas ce que nous voulons.
- Allowed responses (réponses authorisées): Entrez 'z; m' dans le champ-réponses autorisées. Le point-virgule est utilisé pour des réponses distinctes. Le keyboard_response accepte maintenant seulement les touches 'm' 'z' et. Tous les autres touches sont ignorés, à l'exception de'esc', ce qui interrompt l'expérience.
- Timeout (délai): Nous voulons également définir un délai, qui est l'intervalle maximal que la keyboard_response attend avant de décider que la réponse était incorrecte. «2000» (ms) est une bonne valeur. Si un 'Timeout' arrive:
	- La variable dépendante "correct" obtient le valeur 0
	- La variable "réponse" obtient le valeur 'timeout'
	
	TODO: in output file

### Étape 5 : La séquence de bloc

Jusqu'a maintenant, on a travaillé sur le niveau le plus bas de notre structure hierarchique (%hierarchy): la séquence d'essai. Cependant, il faut également créer la séquence du bloc d'entrainement et du bloc expérimental.

On voit que, actuellement, la śequence de bloc se compose de trois éléments:
	
1. reset_feedback
2. block_loop
3. feedback

Cette séquence de bloc est déjà parfait pour notre expérience. 

- Avec l'élément *feedback*, on peut montrer au sujet, après chaque bloc, son pourcentage de réponses correctes, et son temps de réaction moyen
- L'élément *reset_feedback* assure que ces moyens sont réinitialisés au début de chaque bloc
- Comme on a vu, l'élément *block_loop* fait 8 fois tourner la séquence d'essai (une fois pour chaque combinaison)

### Étape 6 : La séquence de session

Le niveau le plus haut de notre structure hierarchique répresente la sequence de la session experimentale entière. C'est sur ce niveau qu'on va réglar la longeur de la phase d'entrainement et la longeur de la phase experimentalle. Evidemment, la phase d'entrainement doit durer plus courte (ex. que 16 essais) que la phase expermentale.

Cependant, maintenant, practice_loop et experimental_loop déroulent la séquence de bloc une seule fois. Donc il faut changer ça:
	
- Cliquez sur 'practice_loop' pour ouvrir son onglet.
- Mettez 'Répéter' vers 2. Cela signifie que la phase d'entrainement se compose de deux blocs
- Cliquez sur 'experimental_loop' pour ouvrir son onglet
- Mettez 'Répéter' vers 8. Cela signifie que la phase d'entrainement se compose de huit blocs

### Les consignes

Change the instructions.


### Étape 7 : Tester l'expérience

Félicitations!! Vous avez construit une expérience entièrement fonctionnel !
Donc, c'est le temps pour la tester. Pour exécuter votre expérience :
	
- Cliquez une des flèches vertes
- Entrez un numéro de sujet (par ex. '1')
- Une fênetre s'ouvre qui indique le nom de défaut du fichier de sortie. Si vous n'aimez pas ce nom, vous pouvez le changer
- Cliquez 'save'
- L'expérience sera lancé. Vous pouvez prétendre que vous avez un participant, pour vérifier si l'expérience fonctionne comme on le souhaite

Si vous n'avez pas envie de dérouler l'expérience entière (2 fois 12 essais) vous pouvez aborter l'expérience en appuyant la touche 'Esc' sur le clavier. Ça interrompt immédiatement l'exécution de l'expérience, de sorte que vous pouvez continuer de la programmer.

Après d'avoir exécuté (un part de) votre expérience, vous pouvez voir si vos variables sont enrégistrées correctement dans le fichier de sortie. 

#### Étappe 8 : Regardez le fichier de sortie

TODO

## Perfectionner l'expérience

### Étape 8 : Donner du feedback après chaque essai

On va donner le sujet du feedback sur son performance apres chaque essai. On va 

Selectionner un item sound, glisser vers la vue d'ensembe, juste aprés le `keyboard_response`. Renommez-le vers 'incorrect_sound'.

Pendant chaque essai, la précision du réponse du participant est enregistrée comme la variable *correct*:
	
- Si le participant répond correctement, la variable 'correct' obtient la valeur 1
- Si le participant répond mal, la variable 'correct' obtient la valeur 0

L'élément `incorrect_sound` ne doit être executée que si la réponse du sujet était faux. Cliquez sur l'élément *trial_sequence* dans la vue d'ensemble'. Un onglet s'ouvre, qui donne une vue d'ensemble de chaque événement de la séquence. À droite, on voit les déclarations 'Run-if'. Ils indiquent dans quelles circonstances OpenSesame exécutera chaque élément. Maintenant, ils sont tous exécutés 'always' ('toujours'). Ce valeur est correct pour tous nos éléments, sauf l'élément `incorrect_sound`. Effectivement, cette élément doit être executée seulememt si la réponse du sujet était faux. Pour programmer ça, il faut changer sa déclaration 'Run-if' vers :

- [correct] = 0  
	
Par conséquence, le sujet entendra le bip seulement si il a fait un erreur.

### Étape 9 : Contrebalancer


### Étape 10 : Fini !

Votre expérience est maintenant terminée. Exécutez-la, pour la tester.

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
