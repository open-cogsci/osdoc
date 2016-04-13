---
layout: osdoc
title: Amorçage catégorique
group: Tutorials
permalink: /amorcage-categorique/
author: Lotje van der Linden
lang: fr
---

## Vue d'ensemble

%--
toc:
 mindepth: 2
 maxdepth: 3
 exclude: ["Vue d'ensemble"]
--%

## Introduction

Cette formation sera composée en trois parties. D'abord, il y aura une brève présentation générale sur la construction des expériences. Ensuite, nous allons créer une expérience qui est à la fois simple et réaliste. Pour finir, on va affiner notre expérience en utilisant quelques astuces des programmeurs avancées.

### La question de recherche

Nous allons créer une expérience d'amorçage catégorique. Les participants voient brièvement une chaîne de lettres et doivent décider si celles-ci forment un mot ou un non-mot (i.e., une tâche de décision lexicale). Pour indiquer sa décision, le participant doit appuyer sur une touche du clavier (« m » pour des mots, et « q » pour des non-mots). Notre hypothèse est que la reconnaissance d'un mot soit plus rapide quand la catégorie du mot est déjà amorcée. Pour amorcer la catégorie, on montrera *un mot amorce*, indiquant la catégorie (par ex. « ANIMAL »), juste avant la présentation de la cible (par ex. « lapin »). Comme condition de contrôle, on présentera également des mots sans avoir amorcé leur catégorie. En tel cas, la cible est précédée par une chaîne de lettres non-informative (par ex. « XXXXX »).

On n'est donc pas principalement intéressés par la différence entre des mots et des non-mots. On varie la cible entre deux types de stimulus seulement pour donner une tâche au sujet qui nécessite une réponse manuelle.

%--
figure:
 id: hypoth1
 source: hypoth1.png
 caption: |
  La reconnaissance d'un mot est plus vite si la catégorie du mot est amorcée par une Amorce.
--%

### La séquence d'essai

Pour tester notre hypothèse, on va créer une expérience avec la séquence d'essai suivante: Chaque essai commencera avec un point de fixation (500 ms). Après, l'Amorce sera présentée brièvement (100 ms), suivi par un intervalle vide (1000 ms). Ensuite, la cible apparaît. La tâche du participant est d'indiquer aussi rapidement et précisement que possible si la cible est un mot ou un non-mot.

- Si la cible est un vrai mot : il faut appuyer la touche « m ».
- Si la cible est un non-mot : il faut appuyer la touche « q ».

À la fin de chaque essai, on sauvegarde toutes les variables (la réponse, la catégorie, etc.) sur un fichier des données.

%--
figure:
 id: trialSeq1
 source: trialSeq1.png
 caption: |
  Exemple schématique de la séquence d'essai.
--%

### Hiérarchie de l'expérience

Notre expérience aura une structure assez simple, avec 2 blocs de 12 essais. La structure hiérarchique de notre expérience peut donc être représentée comme ci-dessous :

%--
figure:
 id: hierarchy
 source: hierarchy.png
 caption: |
  Représentation schématique de la structure hiérarchique.
--%

## Créer l'expérience

### Étape 1 : Démarrer OpenSesame

Lorsque vous démarrez OpenSesame, vous pouvez choisir entre :

- Créer une nouvelle expérience à partir d'un ...
	- modèle par défaut, qui est très simple (« Default template »)
	- modèle étendu, qui est déjà partiellement programmé (« Extended template »)
- Ouvrir une expérience qui était récemment ouverte
- Ouvrir une autre expérience déjà existante

Pour économiser du temps, on va utiliser le modèle étendu. Double-cliquez sur « Extended template » dans l'onglet « Lancez-vous ! ».

%--
figure:
 id: startup
 source: startup.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

La vue d'ensemble montre la structure hiérarchique de l'Extended template.  
Pour simplifier la structure, on commence par supprimer le *practice_loop*, qui représente un bloc d'entraînement pour le participant. (Il n'y a pas de phase d'entraînement dans notre expérience.) Pour le supprimer :

- Cliquez-droit sur *practice_loop* dans la vue d'ensemble ;
- Choissisez « Supprimer » ; et
- Répétez l'opération précédente pour aussi supprimer l'item *end_of_practice*.

Maintenant, la structure hiérarchique montrée dans la vue d'ensemble ressemble déjà beaucoup à la structure montrée par %hierarchy. Cela montre que c'est souvent utile de commencer par l'Extended template.

%--
figure:
 id: overview
 source: overview.png
 caption: |
  L'Extended template comme on le voit dans la vue d'ensemble après avoir supprimé le *practice_loop*.
--%

Ensuite, on enregistre notre nouvelle expérience en cliquant l'icône « Enregistrer » dans la barre d'outils principale.

%--
figure:
 id: save
 source: save.png
 caption: |
  N'oubliez pas de sauvegarder votre expérience.
--%

### Étape 2 : Définir les variables indépendantes

Les variables indépendantes (VI) sont les variables que nous manipulons dans notre expérience. Pour commencer, nous nous limitons à deux VI : *Cible* et *Amorce*. *Cible* correspond aux mots que le participant doit identifier. On utilise les mots suivants :

- Des vrais mots : « chien », « chat », « lapin »
- Des non-mots : « chiun », « chot », « lapon »

*Amorce* correspond aux stimuli qu'on utilise pour amorcer la catégorie du mot. On utilise les amorces suivants :

- Pour les essais expérimentaux : « ANIMAL »
- Pour les essais de contrôle : « XXXXXX »

En total, il y a 12 *Cible* × *Amorce* combinaisons différentes. Ces 12 conditions constituent la liste d'essais d'un bloc (voir %hierarchy). Cette liste doit être saissie dans l'item *block_loop*.  

Heureusement, on n'a pas besoin de saissir toutes ces 12 combinaisons manuellement. L'*Assistant de variables* nous permet de générer un *plan factoriel* facilement.

Pour exécuter cette opération :

- Sélectionnez l'item *block_loop* de la vue d'ensemble ;
- Cliquez sur le bouton *Assistant de variables* dans l'onglet du *block_loop* ;
- Tapez les noms de variables sur la première ligne de l'Assistant de variables ;
- Remplissez les deux colonnes en tapant chaque niveau de la variable ; et
- Cliquez « Ok ».

Vous voyez que OpenSesame a généré notre entière liste d'essais.

Il est pratique d'indiquer la bonne réponse pour chaque essai en définissant la variable `correct_response` (en anglais, donc avec un « s » !). Ça permet OpenSesame de suivre les variables de la performance, comme `acc` (« accuracy » ou pourcentage correct).

Pour indiquer la bonne réponse pour chaque essai :

- Cliquez sur le bouton « Ajouter une variable » ;
- Saisissez « correct_response » et appuyez sur « Enter » ; et
- Maintenant, on a créé un colonne vide pour la nouvelle variable. Il faut donc le remplir :
	- Pour chaque ligne contenant un vrai mot, mettez « m » comme bonne réponse ; et
	- Pour chaque ligne contenant un non-mot, mettez « q ».

%--
figure:
 id: blockloop
 source: blockloop.png
 caption: |
  Le *block_loop* après que vous avez ajouté le plan factoriel et la variable correct_response.
--%

### Étape 3 : Ajouter des items à la séquence d'essai

Comme montre la %trialSeq1, l'objectif est de construire une séquence d'essai comme suit :

1. Présenter le point de fixation
2. Présenter l'Amorce
3. Présenter un écran vide (intervalle entre Amorce et Cible)
4. Présenter la Cible
5. Collecter une réponse sur le clavier
6. Sauvegarder toutes les valeurs sur un fichier de données

On appelle ces 6 étapes *des événements*. On va réaliser ces 6 événements en ajoutant des *items* au *trial_sequence*.

Pour les premiers 4 événements, on utilise des items `sketchpad`. Cependant, pour l'instant, notre *trial_sequence* ne contient qu'un seul item `sketchpad`. Il faut donc en ajouter encore 3.

Pour ajouter ces 3 items `sketchpad` :

- Regardez la barre d'items (à la gauche).
- Choisissez l'item `sketchpad`.
- Faites glisser l'item vers la *trial_sequence* dans la vue d'ensemble.
- *Attention:* Pour faire apparaître un item *au dessous* d'un autre item, déposez-le *sur* cet autre item.
- Répétez la procédure glisser-déposer jusqu'à ce que vous ayez 4 items `sketchpad` dans votre *trial_sequence*.

%--
figure:
 id: dragdrop
 source: dragdrop.png
 caption: |
  Glisser-déposer des items (ici: des `sketchpad`s) de la barre d'outils vers la vue d'ensemble.
--%

Par défaut, OpenSesame attribue des noms tels que *__sketchpad* ou *new_sketchpad_2* (selon la version d'OpenSesame) aux items nouvellement crées. Ces noms ne sont pas très informatifs. Il est donc fortement recommandé de les renommer.

Pour réaliser ça :

- Cliquez-droit sur un item dans la vue d'ensemble ;
- Choisissez « Renommer » ; et
- Changez le nom.
- Appelez les items `sketchpad` *fixation*, *amorce*, *intervalle* et *cible*, respectivement.

%--
figure:
 id: renamed
 source: renamed.png
 caption: |
  La *trial_sequence* après on a ajouté et renommé trois nouveaux items `sketchpad`.
--%

Les derniers deux événements de la séquence d'essai (collecter la réponse et enregistrer les données) sont déjà répresentés par les items `keyboard_response` et `logger`, respectivement.

### Étape 4 : Créer les items *fixation*, *amorce*, *intervalle* et *cible*

#### fixation

Maintenant, on va créer les contenus des items `sketchpad`. On commence avec le `sketchpad` *fixation*.

- Ouvrez l'onglet *fixation* en cliquant sur cet item dans la vue d'ensemble.
- Comme vous voyez, grâce à l'Extended template, le point de fixation est déjà dessiné.

Cependant, il faut qu'on fasse un petit changement sur cet item. Actuellement, la durée de ce `sketchpad` est mis sur 0. Ça veut dire que le point de fixation sera présenté pendant 0 millisecondes. Bien sur, ce n'est pas ce que l'on veut. On veut que le point de fixation soit présenté pendant 500 ms (voir %trialSeq1), et que, après, l'expérience avance automatiquement.

Pour réaliser ça, il faut changer la durée vers 500.

%--
figure:
 id: fixation
 source: fixation.png
 caption: |
  Le `sketchpad` *fixation*, avec une durée de 500 ms.
--%

#### amorce

Pour le point de fixation, on a créé un `sketchpad` *invariable*. Un `sketchpad` invariable montre la même chose (ici : un point de fixation pendant 500 ms) sur chaque essai.

On peut également créer des `sketchpad`s *variables*. Ça veut dire que le contenu du `sketchpad` est défini par une variable indépendante. Grâce aux `sketchpad`s variables, on ne doit pas créer deux `sketchpad`s différents pour chaque niveau de la variable Amorce (« ANIMAL » et « XXXXX »). Au lieu de ça, on en crée qu'un seul, et on laisse décider OpenSesame quel Amorce sera présentée sur chaque essai, sur la base des valeurs de la liste *block_loop*.

Pour indiquer à OpenSesame qu'il s'agit d'un `sketchpad` variable, on utilise la méthode *entre-crochets*. La méthode entre-crochets fonctionne comme expliqué ci-dessous :

- Ouvrez l'onglet *amorce* en cliquant sur cet item dans la vue d'ensemble
- Cliquez sur l'icone « A » pour sélectionner l'outil texte
- Cliquez sur le centre de l'écran
- Cela ouvrira une boîte de dialogue pour entrer du texte
- Au lieu de taper l'Amorce (par ex. « ANIMAL ») directement, on tape *le nom de la variable indépendante* ('amorce') entre crochets
- Enfin, mettez la durée du `sketchpad` sur 100 ms

%--
figure:
 id: amorce
 source: amorce.png
 caption: |
  Le `sketchpad` *amorce* après avoir sélectionné l'outil texte, saissi le nom de la variable, et mis la durée sur 100 ms.
--%

Les crochets indiquent que nous avons affaire à une texte variable. Donc, au lieu de présenter « amorce » sur l'écran, OpenSesame présentera la valeur de la variable (i.e. « XXXXXX » ou « ANIMAL ») comme tirée de la liste *block_loop*.

%--
figure:
 id: squarebrackets1
 source: squarebrackets1.png
 caption: |
  Représentation de la méthode entre crochets. Les crochets indiquent que « amorce » doit être interprété comme un nom de variable, et que OpenSesame doit lire les valeurs de cette variable de la liste *block_loop*.
--%

#### intervalle

Le `sketchpad` *intervalle* est *invariable*. Il est facile de le créer, car il ne s'agit de rien de plus que d'un écran vide avec une durée de 1000 ms.

#### cible

Le `sketchpad` *cible* est un sketchpad *variable*, pareil que le sketchpad *amorce*. Donc, on utilise encore une fois la méthode entre-crochets. La seule différence est que, cette fois, on met le nom de notre autre variable indépendante, « cible », entre crochets.

Ensuite, on met la durée du `sketchpad` *cible* sur 0 ms. Ça peut vous sembler contre-intuitif, mais ça veut juste dire que OpenSesame va initialiser le prochain item (ici, *keyboard_response*) tout de suite. L'item *keyboard_response* lui même ne change pas ce qui est actuellement montrer au sujet sur l'écran.

Donc, en somme, le stimulus reste sur l'écran jusqu'à-ce que le sujet ait appuyé sur une touche.

%--
figure:
 id: cible
 source: cible.png
 caption: |
  Les crochets indiquent que « cible » doit être interprété comme un nom de variable, et que OpenSesame doit lire les valeurs de cette variable de la liste *block_loop*.
--%

### Étape 5 : La séquence de bloc

Jusqu'à maintenant, on a travaillé sur le niveau le plus bas de notre structure hiérarchique (%hierarchy) : la séquence d'essai. Cependant, il faut également créer la séquence de bloc (un bloc contient plusieurs essais) et la séquence de la session entière (une session contient plusieurs blocs).

Pour avoir une meilleure vue sur le bloc de séquence, on commence par cacher temporairement la séquence d'essai de la vue d'ensemble. Pour réaliser ça:

- Cliquez sur le signe à gauche de l'item *trial_sequence* dans la vue d'ensemble.

%--
figure:
 id: blockSeq
 source: blockSeq.png
 caption: |
  La séquence de bloc.
--%

On voit que, actuellement, le bloc de séquence se compose de trois items :

1. reset_feedback
2. block_loop
3. feedback

Cette séquence de bloc est déjà parfaite pour notre expérience.

- Avec l'item *feedback*, on peut montrer au sujet, après chaque bloc, son pourcentage de réponses correctes, et son temps de réaction moyen.
- L'item *reset_feedback* assure que ces moyens sont ré-initialisés au début de chaque bloc.
- Comme on a vu, l'item *block_loop* fait 12 fois tourner la séquence d'essai (une fois pour chaque combinaison).

### Étape 6 : La séquence de session

Le niveau le plus haut de notre structure hiérarchique représente la séquence de la session expérimentale entière. Pour mieux voir cette séquence, on cache temporairement la séquence de bloc.

%--
figure:
 id: sessSeq
 source: sessSeq.png
 caption: |
  La séquence de la session expérimentale entière.
--%

On voit que la séquence de la session expérimentale entière se compose de 3 éléments :

1. instructions
2. experimental_loop ; cela fait tourner 1 séquence de bloc, qui, à son tour, fait tourner 12 essais.
3. end_of_experiment

Même si cette séquence de session est déjà presque parfaite, on va régler des petites choses dans chacun de ces éléments.

#### instructions

Le `sketchpad` *instructions* explique la tâche au participant. Pour l'instant, les instructions ne sont pas suffisamment précises.

Changez les instructions comme ci-dessous :

- Supprimez le texte qui est actuellement montré :
	- Sélectionnez la flèche de la barre d'outils ; 
	- Cliquez-droit sur le texte au centre du `sketchpad` ; et
	- Sélectionnez « Supprimer » pour le supprimer.
- Ajoutez un nouveau texte :
	- Cliquez sur l'icone « A » pour sélectionner l'outil texte ;
	- Cliquez quelque part sur le `sketchpad` ; et
	- Saisissez un petit texte qui informe le sujet de ce qu'il faut faire dans cette expérience. Une bonne instruction est à la fois brève et claire.

#### experimental_loop

Actuellement, notre expérience est composée d'un seul bloc expérimental. Chaque bloc, à son tour, est composé d'un petit nombre d'essai (les 12 conditions sont montrées au sujet une seule fois). D'une manière générale, un tel nombre d'observations ne suffit pas pour faire des bonnes analyses statistiques. Pour augmenter le nombre de répétitions, on va changer le nombre de blocs expérimentaux comme expliqué ci-dessous :

- Ouvrez l'onglet *experimental_loop* en cliquant sur cet item dans la vue d'ensemble ; et
- Changez le nombre de répétitions dans la boite *Répéter*. Mettez-le sur 2. Par conséquence, le bloc expérimental entier va être répété 2 fois.

%--
figure:
 id: increaseRep
 source: increaseRep.png
 caption: |
  Le *block_loop* va être répété 2 fois.
--%

#### end_of_experiment

Cet élément `sketchpad` informe le participant que l'expérience est terminée.

- Mettez ce message en français en utilisant l'outil texte.

### Étape 7 : Tester l'expérience

Félicitations ! Vous avez construit une expérience complète !
Maintenant, il faut la tester. Pour exécuter votre expérience :

- Cliquez sur une des flèches vertes ; et
- Saisissez un numéro de sujet (par ex. 1).
- Une fenêtre s'ouvre qui indique le nom de défaut du fichier de sortie. Si vous n'aimez pas ce nom, vous pouvez le changer.
- Cliquez sur Enregistrer.
- L'expérience sera lancée.

Si vous n'avez pas envie de dérouler l'expérience entière (2 fois 12 essais) vous pouvez arrêter l'expérience en appuyant la touche « Esc » (ou « Echap ») sur le clavier.

Après d'avoir exécuté (une part de) votre expérience, vous pouvez voir si vos variables sont sauvegardées correctement dans le fichier de données.

## Perfectionner l'expérience

### Étape 8 : Donner du feedback après chaque essai

On va étendre la séquence d'essai avec un item en plus : un `sketchpad` qui informe le participant, après chaque réponse, si sa réponse était juste ou fausse. En réalisant ça, on va apprendre deux astuces plus avancées :

- Comment utiliser des *variables dépendantes* en ligne ; et
- Comment utiliser des déclarations *exécuter-si* (run-if statements).

Pendant chaque essai, la précision du réponse du participant est enregistrée comme la variable *correct* :

- Si le participant répond correctement, `correct` à la valeur 1
- Si le participant répond faux, `correct` à la valeur 0

On va utiliser cette variable *en ligne*, pour déterminer si le participant doit être informé que sa réponse était juste (en lui montant un point de fixation vert) ou fausse (en lui montant un point de fixation rouge).

#### Créer les éléments `sketchpad`

- Ajoutez deux items `sketchpad` à la séquence d'essai.
- Placez-les après l'item *keyboard_response*.
- Donnez-leurs des noms informatifs, par ex. *juste* et *faux*.
- Mettez leurs durées vers 500 ms.
- Ouvrez le sketchpad *juste* et dessinez un croix de fixation vert sur le centre du `sketchpad`. Pour effectuer cette opération :
	- Cliquez sur l'icône du point de fixation pour sélectionner cet outil.
	- Changez sa couleur du blanc au vert, en tapant « green » dans la boite couleur.
	- Cliquez sur le centre du sketchpad.
- Ouvrez le sketchpad *feedback_incorrect* et répétez cette procédure. Assurez-vous que, pour l'item *faux*, le couleur du point de fixation soit rouge (« red »).

%--
figure:
 id: correct
 source: correct.png
 caption: |
  Un point de fixation vert va être montré au participant si sa réponse était juste.
--%

#### Utiliser des déclarations « exécuter-si » (run-if statements)

Cliquez sur l'item *trial_sequence* dans la vue d'ensemble. Un onglet s'ouvre, et donne une vue d'ensemble de chaque événement de la séquence. À droite, on voit les déclarations « exécuter-si » (en anglais : *run-if*). Ils indiquent dans quelles circonstances chaque item est exécuté. Maintenant, ils sont tous exécutés « always » (« toujours »). Ce valeur est correct pour tous nos items, sauf pour les items *juste* et *faux* : à la fin de chaque essai, il faut seulement exécuter un des deux en fonction de la précision de la réponse (juste ou faux). Pour programmer ça, il faut changer leurs déclarations « exécuter-si » vers :

- [correct] = 1
- [correct] = 0  

… pour les éléments *juste* et *faux*, respectivement. Par conséquence, le sujet verra le point de fixation vert si sa réponse était juste, et le point de fixation rouge si sa réponse était fausse.

%--
figure:
 id: ifStat
 source: ifStat.png
 caption: |
  On utilise des déclarations « exécuter-si » pour réaliser qu'une partie de la séquence d'essai dépend des variables collectées en ligne.
--%

### Étape 9 : Varier un variable indépendante entre *blocs*

Imaginez que nous ne soyons pas seulement intéressés par l'effet de l'Amorce, mais que l'on veuille également examiner si l'effet de l'Amorce interagit avec l'effet de la durée de l'intervalle entre Amorce et Cible. Par exemple, on peut élargir la question de recherche vers :

> La reconnaissance d'un mot, est-elle plus rapide quand la catégorie du mot est amorcée très récemment, mais non quand l'intervalle entre Amorce et Cible est assez longue ?

%--
figure:
 id: hypoth2
 source: hypoth2.png
 caption: |
  Notre hypothèse est qu'il y aura un effet d'interaction entre Amorce et Intervalle.
--%

Pour répondre à cette question, il faut une deuxième variable indépendante : durée de l'intervalle. On va lui donner deux valeurs différentes : 1000 et 3000 ms.

Pour ajouter cette variable à notre expérience, on a deux possibilités :

- On peut ajouter une variable supplémentaire dans notre liste du *block_loop*.
	- Par conséquence, l'intervalle sera différent à chaque essai.
- On peut ajouter une variable dans notre liste de l'*experimental_loop*.
	- Par conséquence, l'intervalle sera différent seulement entre blocs : on aura un bloc entier avec une intervalle de 1000 ms, et un autre avec une intervalle de 4000 ms.

Pour ce tutoriel, on choisit option 2. Pour réaliser cette opération :

- Ouvrez l'item *experimental_loop* ;
- Mettez le nombre de cycles sur « 2 », dans la boite « Cycles » ; et
- Ajoutez une variable `intervalle`. Donnez-lui les valeurs 1000 et 4000.

%--
figure:
 id: exploop
 source: exploop.png
 caption: |
  Ajoutez une variable indépendante, qui va être varié entre blocs.
--%

- Ouvrez le `sketchpad` *intervalle*.
- Changez la durée sur « [intervalle] », indiquant que la durée de cet item dépend à la valeur de la variable `intervalle`.

%--
figure:
 id: squarebrackets3
 source: squarebrackets3.png
 caption: |
  Utilisez la méthode entre-crochets pour indiquer que « intervalle » doit être interprété comme un nom de variable, et que OpenSesame doit lire les valeurs de cette variable de la liste *experimental_loop*.
--%


### Étape 10 : Fini !

Votre expérience est maintenant terminée. Exécutez-la, pour la tester.

## Extra

S'il vous reste encore du temps, vous pouvez essayer de faire une expérience extra. L'expérience extra est une variante de l'expérience 'amorcage catégorique' que vous venez de construire. Sauvegardez donc cette expérience sous un autre nom. Ensuite, vous pouvez modifier le copie de l'expérience originale.

*Attention :* Assurez-vous que vous avez fait un copie (sauvegarder-sous) de l'expérience originale. Sinon, vous allez l'écraser.

Pour l'expérience originale, tous les stimuli (l'amorce et la cible) était des textes. Pour l'expérience extra, on va changer le protocole de telle sorte que l'amorce et la cible soient des images. Pour réaliser ça, il faut d'abord changer les niveaux des deux variables indépendantes : Amorce et Cible.

### Amorce

L'amorce va être soit un animal (par ex. un oiseau), soit pas un animal (par ex. un accordéon). L'idée est que l'image de l'oiseau va amorcer la catégorie sémantique « animal », lorsque l'image de l'accordéon ne le fera pas. L'amorce non-animal fonctionne donc comme notre condition contrôle.

### Cible

Ensuite, la cible va être soit un chien, soit un chat. Si la cible est un chien, le sujet doit appuyer sur la touche « m ». Si la cible est un chat, le sujet doit appuyer sur la touche « q ». Les cibles sont donc toutes des animaux (au lieu des mots et des non-mots dans notre protocole original).

%--
figure:
 id: trialSeq2
 source: trialSeq2.png
 caption: |
  Exercice extra : Une expérience de l'amorçage catégorique avec des images.
--%

### L'hypothèse

L'hypothèse est que le sujet va identifier la cible (toujours un animal) plus rapidement si la catégorie sémantique « animal » est déjà amorcée, par rapport à la condition contrôle.

*Attention :* On n'est donc pas principalement intéressés par la différence entre des images chats et des images chiens. On varie la cible entre deux types d'animaux seulement pour donner une tâche au sujet qui nécessite une réponse manuelle.

%--
figure:
 id: hypoth3
 source: hypoth3.png
 caption: |
  Exercice extra : L'hypothèse.
--%

### Astuces

Vous pouvez télécharger les stimuli pour cette expérience ici [(Rossion & Pourtois, 2004)](#references)

- [accordeon.png](/attachments/amorcage-categorique/accordeon.png)
- [chat.png](/attachments/amorcage-categorique/chat.png)
- [chien.png](/attachments/amorcage-categorique/chien.png)
- [oiseau.png](/attachments/amorcage-categorique/oiseau.png)

Ensuite :

- Ajoutez ces stimuli vers le *groupe de fichiers* [(voir ici)][workshop-part2].
- Utilisez la méthode *entre-crochets* dans le code d'un sketchpad, pour indiquer quelles images sont montrées pendant chaque essai [(voir ici)][workshop-part2].

## Références

Math&ocirc;t, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social science. *Behavior Research Methods*, *44*(2), 313-324. doi:10.3758/s13428-011-0168-7
{: .reference}

Rossion, B., & Pourtois, G. (2004). Revisiting Snodgrass and Vanderwart’s object pictorial set: The role of surface detail in basic-level object recognition. *Perception*, *33*(2), 217–236.
{: .reference}

[download]: /getting-opensesame/download/
[feedback]: /usage/feedback/
[forms]: /forms/about/
[forms-opensesame]: /forms/custom-forms/#opensesame-script
[forms-performance]: /forms/performance-issues-and-troubleshooting/
[forms-python]: /forms/custom-forms/#python
[slides]: /attachments/amorcage-categorique/Workshop_OpenSesame_Part1.pdf
[variables]: /usage/variables-and-conditional-statements/#using-variables
[responses]: /usage/collecting-responses/
[tutorial]: /usage/step-by-step-tutorial/
[html-subset]: /usage/text-formatting/
[aps-page]: http://aps.psychologicalscience.org/convention/program_2013/search/viewProgram.cfm?Abstract_ID=26153
[smep]: http://www.smep.org/
[pdf]: /aps2013/index.pdf
[prepare-run]: /usage/prepare-run/#sketchpad-feedback
[workshop-part2]: http://osdoc.cogsci.nl/tutorials/direction-du-regard/

