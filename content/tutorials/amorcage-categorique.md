---
layout: osdoc
title: Amorçage catégorique
group: Tutorials
permalink: /amorcage-categorique/
author: Lotje van der Linden
lang: fr
---

Ce tutoriel a été écrit pour une ancienne version d'OpenSesame.
{: .page-notification}

## Vue d'ensemble

Cette formation sera composé en trois parties. D'abord, il y aura une brève présentation générale sur la constructions des expériences. Ensuite, nous allons créer une expérience qui est à la fois simple et réaliste. Pour finir, on va affiner notre expérience en utilisant quelques astuces des programmeurs avancées.

%--
toc:
 mindepth: 2
 maxdepth: 3
 exclude: ["Vue d'ensemble"]
--%

## Introduction

Les diapositives de cette formation peut être téléchargé d'[ici][slides]

### La question de recherche

Nous allons créer une expérience catégorique amorçage. Les participants voient brièvement une chaîne de lettres et doivent décider si celle-ci est un mot ou un non-mot (i.e., une tâche de décision lexicale). Pour indiquer sa décision, le participant doit appuyer sur une touche du clavier. Notre hypothèse est que la reconnaissance d'un mot soit plus vite quand la catégorie du mot est déjà amorcée. Pour amorcer la catégorie, on montrera *un mot amorce*, indiquant la catégorie (par ex. "ANIMAL"), juste avant la présentation de la cible (par ex. 'lapin'). Comme condition de contrôle, on présentera également des mots sans avoir amorcé leur catégorie. En tel cas, la cible est précédée par une chaîne de lettres non-informative (par ex. "XXXXX").

*Attention:* On n'est donc pas principalement interessés sur la différence entre des mots et des non-mots. On varie la cible entre deux types de stimulus seulement pour donner une tâche au sujet qui nécessite une réponse manuelle.

%--
figure:
 id: hypoth1
 source: hypoth1.png
 caption: |
  La reconnaissance d'un mot est plus vite si la catégorie du mot est amorcée par une Amorce.
--%

### La séquence d'essai

Pour tester notre hypothèse, on va créer une expérience avec la séquence d'essai suivante: Chaque essai commencera avec un point de fixation (500 ms). Après, l'Amorce sera présenté brièvement (100 ms), suivi par un intervalle vide (1000 ms). Ensuite, la cible apparaît. La tâche du participant est d'indiquer aussi rapidement et précise que possible si la cible est un mot ou un non-mot.

- Si la cible est un vrai mot: il faut appuyer la touche 'm'
- Si la cible est un non-mot: il faut appuyer la touche 'q'

A la fin de chaque essai, il faut enregistrer tous les valeurs nouvelles vers un fichier de sortie.

%--
figure:
 id: trialSeq1
 source: trialSeq1.png
 caption: |
  Exemple schématique de la séquence d'essai.
--%

### Hiérarchie de l'expérience

Pour commencer, on va construire une expérience très simple, qui contient seulement 2 blocs de 12 essais. La structure hiérarchique de notre expérience peut donc être représentée comme suit:

%--
figure:
 id: hierarchy
 source: hierarchy.png
 caption: |
  Réprésentation schématique de la structure hiérarchique.
--%

## Création d'une expérience simple

### Étape 1 : Démarrer OpenSesame

Lorsque vous démarrez OpenSesame, vous recevrez un menu qui vous permet de choisir entre:

- Ouvrir une expérience qui était récemment ouverte
- Ouvrir une autre expérience déjà existante
- Créer une nouvelle expérience ...
	- complètement vide ('Default template')
	- modèle étendu, qui est déjà partiellement programmé ('Extended template')

Pour économiser du temps, on va utiliser le modèle étendu. Double-cliquez sur l'Extended template dans l'onglet 'Lancez-vous!'.

%--
figure:
 id: startup
 source: startup.png
 caption: |
  La fenêtre OpenSesame au démarrage.
--%

La vue d'ensemble montre la structure hiérarchique de l'Extended template.  
Pour simplifier des choses, on commence par supprimer le *practice_loop*, qui représente un bloc d'entraînement pour le participant. Pour exécuter cette suppression:

- Clic droit sur 'practice_loop' dans la vue d'ensemble
- Choisissez 'Supprimer'
- Répétez cette opération pour également supprimer l'élément *end_of_practice*

Maintenant, la structure hiérarchique de la vue d'ensemble ressemble déjà beaucoup la structure schématique qui est représentée par %hierarchy. Cette ressemblance montre que c'est souvent utile de commencer par l'Extended template.

%--
figure:
 id: overview
 source: overview.png
 caption: |
  L'Extended template comme on le voit dans la vue d'ensemble avant et après avoir supprimé le *practice_loop*.
--%

Ensuite, on enregistre notre nouvelle expérience

- En cliquant l'icône 'Enregistrer' de la barre d'outils principale.

%--
figure:
 id: save
 source: save.png
 caption: |
  N'oubliez pas de sauvegarder votre expérience.
--%

### Étape 2 : Definir les variables indépendantes

Pour commencer, nous nous limitons à deux variables indépendantes: *Cible* et *Amorce*. La variable *Cible* contient les mots d'une certaine catégorie qui le participant doit identifier.  

- Des vrais mots: 'chien', 'chat', 'lapin'
- Des non-mots: 'chiun', 'chot', 'lapon'

La variable *Amorce* contient le stimulus qu'on utilise pour amorcer la catégorie du mot:

- Pour les essais expérimentaux: 'ANIMAL'
- Pour les essais de contrôle: 'XXXXXX'

En total, ça donne 12 Cible * Amorce combinaisons différentes. Ces 12 conditions constituent la liste d'essais d'un bloc (voyez %hierarchy). Cette liste doit être rempli dans l'élément *block_loop*.  
Heureusement, on n'a pas besoin de taper toutes ces 12 combinaisons manuellement. Au lieu de cela, nous utilisons l'*Assistant de variables*, qui va nous générer un *plan factoriel*.

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

%--
figure:
 id: blockloop
 source: blockloop.png
 caption: |
  Le *block_loop* après que vous avez ajouté le plan factoriel et la variable correct_response.
--%

### Étape 3 : Ajouter des éléments à la séquence d'essai

Comme montre la %trialSeq1, l'objectif est de construire une séquence d'essai comme suit:

1. Présenter le point de fixation
2. Présenter l'Amorce
3. Présenter un écran vide (intervalle entre Amorce et Cible)
4. Présenter la Cible
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
  Glisser-déposer des éléments (ici: des `sketchpad`s) de la barre d'outils vers la vue d'ensemble.
--%

Par défaut, OpenSesame attribue des noms tels que "__sketchpad" aux éléments nouvellement crées. Ces noms ne sont pas très informative. Il est donc forcement recommandé de les changer.

Pour réaliser ça:

- Clic droit sur un élément dans la vue d'ensemble
- Choisissez 'Renommer'
- Changez le nom
- Appelez les éléments `sketchpad` *fixation*, *amorce*, *intervalle* et *cible*, respectivement.

%--
figure:
 id: renamed
 source: renamed.png
 caption: |
  La *trial_sequence* après on a ajouté et renommé trois nouveux éléments `sketchpad`.
--%

Les derniers deux événements de la séquence d'essai, (collecter la réponse et enregistrer les données) sont sont déjà répresentés par les éléments `keyboard_response` et `logger`, respectivement.

### Étape 4 : Créer les éléments *fixation*, *amorce*, *intervalle* et *cible*

#### fixation

Maintenant, on va créer le content des éléments `sketchpad` grâce aux 'drawing tools' (des outils de dessin) de ces éléments. On commence avec le `sketchpad` *fixation*.

- Ouvrez l'onglet *fixation* en cliquant sur cet élément dans la vue d'ensemble.
- Comme vous voyez, grâce à l'Extended template, le point de fixation est déjà dessiné.

Cependant, il faut qu'on fasse un petit changement sur cet élément. Actuellement, la durée de ce `sketchpad` est mis sur '0'. Ça veut dire que le point de fixation sera présenté pendant 0 millisecondes. Bien sur, ce n'est pas ce qu'on veut. On veut que le point de fixation sera présenté par 500 ms (voyez %trialSeq1), et que, aprés, l'expérience avance automatiquement.  
Pour réaliser ça, il faut changer la durée vers '500'.

%--
figure:
 id: fixation
 source: fixation.png
 caption: |
  Le `sketchpad` *fixation*, avec une durée de 500 ms.
--%

#### amorce

Pour le point de fixation, on a créé un `sketchpad` *invariable*. Un `sketchpad` invariable montre la même chose (ici: un point de fixation pendant 500 ms) sur chaque essai.

On peut également créer des `sketchpad`s *variables*. Ça veut dire que le contient du `sketchpad` est défini par une variable indépendente. Grâce aux `sketchpad`s variables, on ne doit pas créer deux `sketchpad`s différents pour chaque niveau de la variable Amorce ('ANIMAL et 'XXXXX'). Au lieu de ça, on en crée qu'un, et on laisse décider OpenSesame quel Amorce sera présenté sur chaque essai, au base des valeurs dans la liste *block_loop*.

Pour indiquer à OpenSesame qu'il s'agit d'un `sketchpad` variable, on utilise la méthode *entre-crochets*. La méthode entre-crochets fonctionne comme suit:

- Ouvrez l'onglet *amorce* en cliquant sur cet élément dans la vue d'ensemble
- Cliquez sur l'icone "A" pour sélectionner l'outil texte
- Cliquez sur le centre de l'écran
- Cela ouvrira une boîte de dialogue vous demandant de spécifier un texte
- Au lieu de taper l'Amorce (par ex. 'ANIMAL') directement, on tape *le nom de la variable indépendante* ('amorce') entre crochets
- Enfin, mettez la durée du `sketchpad` sur 100 ms

%--
figure:
 id: amorce
 source: amorce.png
 caption: |
  Le `sketchpad` *amorce* aprés avoir sélectionné l'outil texte, tapé le nom de la variable, et mis la durée sur 100 ms.
--%

Les crochets indique que nous avons affaire à une texte variable. Donc, au lieu de présenter '[amorce]' sur l'écran, OpenSesame présentera la valeur de la variable (i.e. 'XXXXXX' ou 'ANIMAL') comme tirée de la liste *block_loop*.

%--
figure:
 id: squarebrackets1
 source: squarebrackets1.png
 caption: |
  Réprésentation de la méthode 'entre crochets'. Les crochets indiquent que 'amorce' doit être interprété comme un nom de variable, et que OpenSesame doit lire les valeurs de cette variable de la liste *block_loop*.
--%

#### intervalle

Le `sketchpad` *intervalle* est *invariable*. Il est facile de créer, parce qu'il s'agit de rien de plus qu'un écran vide avec une durée de 1000 ms.

#### cible

Le `sketchpad` *cible* est un sketchpad *variable*; pareil que le sketchpad *amorce*. Donc, on utilise encore une fois la méthode entre-crochets. La seule différence est que, cette fois, on met le nom de notre autre variable indépendente, 'cible', entre crochets.

Ensuite, on met la durée du `sketchpad` *cible* sur 0 ms. Ça peut vous sembler contre-intuitif, mais ça veut juste dire que OpenSesame va initialiser la prochaine élément (ici, *keyboard_response*) tout de suite. L'élément *keyboard_response* lui même ne change pas ce qui est actuellement montrer au sujet sur l'écran.

Donc, en somme, le stimulus reste sur l'écran jusqu'à le sujet a appuyé sur une touche.

%--
figure:
 id: cible
 source: cible.png
 caption: |
  Les crochets indiquent que 'cible' doit être interprété comme un nom de variable, et que OpenSesame doit lire les valeurs de cette variable de la liste *block_loop*.
--%

### Étape 5 : La séquence de bloc

Jusqu'a maintenant, on a travaillé sur le niveau le plus bas de notre structure hierarchique (%hierarchy): la séquence d'essai. Cependant, il faut également créer la séquence de bloc et la séquence de la session entière.

Pour avoir une meilleure vue sur la bloc de séquence, on commence par cacher temporairement la séquence d'essai de la vue d'ensemble. Pour réaliser ça:

- Cliquez le signe '-' dans la vue d'ensemble à gauche de l'élément *trial_sequence*.

%--
figure:
 id: blockSeq
 source: blockSeq.png
 caption: |
  La séquence de bloc.
--%

On voit que, actuellement, la bloc de séquence se compose de trois éléments:

1. reset_feedback
2. block_loop
3. feedback

Cette séquence de bloc est déjà parfait pour notre expérience.

- Avec l'élément *feedback*, on peut montrer au sujet, après chaque bloc, son pourcentage de réponses correctes, et son temps de réaction moyen
- L'élément *reset_feedback* assure que ces moyens sont réinitialisés au début de chaque bloc
- Comme on a vu, l'élément *block_loop* fait 12 fois tourner la séquence d'essai (une fois pour chaque combinaison)

### Étape 6 : La séquence de session

Le niveau le plus haut de notre structure hierarchique répresente la sequence de la session experimentale entière. Pour voir mieux cette séquence, on cache temporairement la séquence de bloc.

%--
figure:
 id: sessSeq
 source: sessSeq.png
 caption: |
  La séquence de la session expérimentale entière.
--%

On voit que la séquence de la session expérimentale entière se compose de 3 éléments:

1. instructions
2. experimental_loop (qui fait tourner 1 séquence de bloc, qui, à sa tour, fait tourner 12 essais)
3. end_of_experiment

Même si cette séquence de session est déjà presque parfait, on va régler des petites choses dans chacun de ces éléments.

#### instructions

Le `sketchpad` *instructions* donne une explication de la tâche pour le participant. Pour l'instant, les instructions ne sont pas suffisamment précises.

Changez les comme suit:

- Supprimez le texte qui est actuellement montré:
	- Sélectionnez la flêche de la barre d'outils
	- Cliquez sur le texte au centre du `sketchpad`
	- Appuyez la touche 'delete' du clavier
- Ajoutez un nouveau text:
	- Cliquez sur l'icone 'A' pour sélectionner l'outil texte
	- Cliquez quelque part sur le `sketchpad`
	- Écrivez une petite texte qui informe le sujet de sa tâche de décision lexical

#### experimental_loop

Actuellement, notre expérience consiste juste d'un seul bloc expérimental. Chaque bloc, à son tour, est constitué d'un petit nombre d'essai (les 12 conditions sont montrés au sujet qu'une fois). Normalement, un tel nombre d'observations ne suffit pas pour faire des bonnes analyses statistiques. Pour augmenter le nombre de répétitions, on va changer le nombre de blocs expérimentaux comme suit:

- Ouvrez l'onglet *experimental_loop* en cliquant sur cet élément dans la vue d'ensemble
- Changer le nombre de répétitions dans la boite *Répéter*. Mettez-le vers '2'. Par conséquence, le bloc expérimental entier va être répété 2 fois.

%--
figure:
 id: increaseRep
 source: increaseRep.png
 caption: |
  Le *block_loop* va être répété 2 fois.
--%

#### end_of_experiment

Cet élément `sketchpad` informe le participant que l'expérience est terminé.

- Mettez ce message en français en utilisant l'outil texte.

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

## Perfectionner l'expérience

### Étape 8 : Donner du feedback après chaque essai

On va étendre la séquence d'essai avec un événement en plus : un élément `sketchpad` qui informe le participant, après chaque réponse, si sa réponse était juste ou faux. En réalisant ça, on va apprendre deux astuces un peu plus avancés :

- Utiliser des *variables dépendantes* en ligne
- Utiliser des déclarations *exécuter-si* (run-if statements)

Pendant chaque essai, la précision du réponse du participant est enregistrée comme la variable *correct*:

- Si le participant répond correctement, la variable 'correct' obtient la valeur 1
- Si le participant répond mal, la variable 'correct' obtient la valeur 0

On va utiliser cette variable *en ligne*, pour déterminer si le participant doit être informé que sa réponse était juste (en lui montant un point de fixation vert) ou faux (en lui montant un point de fixation rouge).

#### Créer les éléments `sketchpad`

- Ajoutez deux éléments `sketchpad` à la séquence d'essai.
- Placez-les après l'élément *keyboard_response*.
- Donnez-les des noms informatives, par ex. *juste* et *faux*.
- Mettez leurs durées vers 500 ms
- Ouvrez le sketchpad *juste* et dessinez un croix de fixation vert sur le centre du `sketchpad`. Pour effectuer cette opération :
	- Cliquez sur l'icône du point de fixation pour sélectionner cet outil.
	- Changez son couleur du blanc vers vert, en tapant "green" dans la boite couleur.
	- Cliquez sur le centre du sketchpad.
- Ouvrez le sketchpad 'feedback_incorrect' et répétez cette procédure. Assurez-vous que, pour l'*évaluation_incorrect*, le couleur du point de fixation soit rouge ('red').

%--
figure:
 id: correct
 source: correct.png
 caption: |
  Créez un point de fixation vert qui va être montré au participant si sa réponse était juste.
--%

#### Utiliser des déclarations "Run-if" (exécuter-si)

Cliquez sur l'élément *trial_sequence* dans la vue d'ensemble'. Un onglet s'ouvre, qui donne une vue d'ensemble de chaque événement de la séquence. À droite, on voit les déclarations 'Run-if'. Ils indiquent dans quelles circonstances OpenSesame exécutera chaque élément. Maintenant, ils sont tous exécutés 'always' ('toujours'). Ce valeur est correct pour tous nos éléments, sauf les éléments *juste* et *faux*. Effectivement, à la fin de chaque essai, il faut seulement exécuter un des deux en fonction du précision de la réponse (juste ou faux). Pour programmer ça, il faut changer leurs déclarations 'Run-if' vers :

- [correct] = 1
- [correct] = 0  

pour les éléments *juste* et *faux*, respectivement

Par conséquence, le sujet verra le point de fixation vert si sa réponse était juste, et le point de fixation rouge si sa réponse était faux.

%--
figure:
 id: ifStat
 source: ifStat.png
 caption: |
  On utilise des déclarations 'Run-if' pour réaliser qu'une partie de la séquence d'essai dépend des variables collectées en ligne.
--%

### Étape 9 : Varier un variable indépendante entre *blocs*

Imaginez que nous ne soyons pas seulement intéressés sur l'effet de l'Amorce, mais qu'on veule examiner si l'effet de l'Amorce interagit avec l'effet de la durée de l'intervalle entre Amorce et Cible. Par exemple, on peut élargir la question de recherche vers:

*La reconnaissance d'un mot, est-elle plus vite quand la catégorie du mot est amorcée très récemment, mais non quand l'intervalle entre Amorce et Cible est assez longue ?*

%--
figure:
 id: hypoth2
 source: hypoth2.png
 caption: |
  Notre hypothèse est qu'il y aura un effet d'interaction entre Amorce et Intervalle.
--%

Pour répondre à cette question, il faut un deuxième variable indépendente: durée de l'intervalle. On va le donner deux valeurs différentes: 1000 ms vs. 3000 ms.

Pour ajouter cette variable à notre expérience, on a deux possibilités :

- On peut ajouter une variable supplémentaire dans notre liste du *block_loop*.
	- Par conséquence, l'intervalle sera varié entre chaque essai
- On peut ajouter une variable dans notre liste de l'*experimental_loop*.
	- Par conséquence, l'intervalle sera varié seulement entre blocs : on aura un bloc entier avec un intervalle de 1000 ms, et un autre avec un intervalle de 4000 ms.

Pour ce tutoriel, on choisit option 2. Pour réaliser cette opération :

- Ouvrez l'élément 'experimental_loop'
- Mettez le nombre de cycles sur '2', dans la boite 'Cycles'
- Ajoutez un variable 'intervalle'. Donnez-le ses 2 valeurs

%--
figure:
 id: exploop
 source: exploop.png
 caption: |
  Ajoutez une variable indépendante, qui va être varié entre blocs.
--%

- Changez le `sketchpad` *intervalle* d'un `sketchpad` *invariable* vers un `sketchpad` *variable*
- Utilisez la méthode 'entre crochets' dans la boîte 'Durée'

%--
figure:
 id: squarebrackets3
 source: squarebrackets3.png
 caption: |
  Utilisez la méthode entre-crochetspour indiquer que 'interval' doit être interprété comme un nom de variable, et que OpenSesame doit lire les valeurs de cette variable de la liste *experimental_loop*
--%


### Étape 10 : Fini !

Votre expérience est maintenant terminée. Exécutez-la, pour la tester.

## Extra:

S'il vous reste encore du temps, vous pouvez essayer de faire une expérience extra. L'expérience extra est une variation sur l'expérience 'amorcage catégorique' que vous venez de construire. Sauvegardez donc cette expérience sous un autre nom. Ensuite, vous pouvez modifier le copie de l'expérience originale.

*Attention:* Assurez-vous que vous avez fait un copie (sauvegarder-sous) de l'expérience originale. Sinon, vous allez l'écraser.

Pour l'expérience originale, tous les stimuli (l'amorce et la cible) était des textes. Pour l'expérience extra, on va changer le protocole de telle sorte que l'amorce et la cible sont des images. Pour réaliser ça, il faut d'abord changer les niveaux des deux variables indépendantes; Amorce et Cible:

### Amorce:

L'amorce va être soit un animal (e.g. un oiseau), soit non un animal (e.g. un accordéon). L'idée est que l'image de l'oiseau va amorcer la catégorie sémantique "animal", lorsque l'image de l'accordéon ne le fera pas. L'amorce non-animal fonctions donc comme notre condition contrôle.

### Cible:

Ensuite, la cible va être soit un chien, soit un chat. Si la cible est un chien, le sujet doit appuyer sur la touche 'm'. Si la cible est un chat, le sujet doit appuyer sur la touche 'q'. Les cibles sont donc toutes des animals (au lieu des mots et des non-mots dans notre protocole original).

%--
figure:
 id: trialSeq2
 source: trialSeq2.png
 caption: |
  Exercice extra: Une expérience de l'amorçage catégorique avec des images.
--%

### L'hypothèse

L'hypothèse est que le sujet va identifier la cible (toujours un animal) plus rapidement si la catégorie sémantique "animal" est déjà amorcée, par rapport à la condition contrôle.

*Attention:* On n'est donc pas principalement interessés sur la différence entre des images chats et des images chiens. On varie la cible entre deux types d'animal seulement pour donner une tâche au sujet qui nécessite une réponse manuelle.

%--
figure:
 id: hypoth3
 source: hypoth3.png
 caption: |
  Exercice extra: L'hypothèse.
--%

### Astuces:

Vous pouvez télécharger les stimuli pour cette expérience ici [(Rossion & Pourtois, 2004)](#references)

- [accordeon.png](/attachments/amorcage-categorique/accordeon.png)
- [chat.png](/attachments/amorcage-categorique/chat.png)
- [chien.png](/attachments/amorcage-categorique/chien.png)
- [oiseau.png](/attachments/amorcage-categorique/oiseau.png)

Ensuite:

- Ajoutez ces stimuli vers le *groupe de fichiers* [voyez aussi][workshop-part2]
- Utilisez la méthode *entre-crochets* dans le code d'un sketchpad, pour laisser OpenSesame décider quel image a montrer pendant chaque essai [voyez aussi][workshop-part2]

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
