title: Tutoriel de SigmundAI : Tâche de recherche visuelle
hash: 2662b1ce900715b74ee381b68acb991140b33a5656bfb23c5b7bee6cd4c44cec
locale: fr
language: French

[TOC]

## À propos de ce tutoriel

Ce tutoriel montre comment créer une expérience classique de recherche visuelle dans OpenSesame à l’aide de SigmundAI, le copilote IA, intégré directement dans l’interface d’OpenSesame. Au lieu de construire l’expérience entièrement à la main, vous apprendrez à collaborer avec Sigmund pour construire la structure expérimentale complète, définir des plans factoriels et implémenter une génération dynamique de stimuli grâce à une logique scriptée.


## Ce que vous apprendrez

À la fin de ce tutoriel, vous saurez comment :

- 💡 Donner à Sigmund des instructions claires et efficaces
- 💡 Décomposer des tâches complexes en étapes simples
- 💡 Repérer et corriger les erreurs de Sigmund (oui, l’IA fait des erreurs !)
- 💡 Construire rapidement des structures expérimentales
- 💡 Écrire des scripts avec Sigmund
- 💡 Travailler efficacement avec un copilote IA

## Connecter OpenSesame à Sigmund 

Sigmund est un assistant IA spécialement conçu pour OpenSesame. Contrairement aux chatbots généraux comme ChatGPT, Sigmund :

- Connaît OpenSesame sur le bout des doigts
- Fonctionne directement dans l’interface d’OpenSesame
- Peut apporter automatiquement des modifications à votre expérience

Pour vous connecter, il vous suffit de vous connecter à [sigmundai.eu](https://sigmundai.eu). Le panneau Sigmund dans OpenSesame se connectera automatiquement :

<video controls width ="100%"> 
    <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>
<p align="center"><em>Vidéo 1. Connexion d’OpenSesame à Sigmund.</em></p>


## L’expérience 

Dans ce tutoriel, vous créerez une expérience de base de recherche visuelle. L’expérience ressemble aux études classiques de recherche visuelle de [Treisman and Gelade (1980)][references], mais elle n’est pas identique.

Dans cette expérience, les participants recherchent un objet cible, qui peut être un carré jaune, un cercle jaune, un carré bleu ou un cercle bleu ; l’identité de la cible varie d’un bloc d’essais à l’autre. Les participants indiquent si la cible est présente ou non en appuyant sur la touche flèche droite (présente) ou flèche gauche (absente).

En plus de la cible, zéro ou plusieurs objets distracteurs sont présentés. Il y a trois conditions, et la condition détermine le type de distracteurs présents :

- Dans la condition *Conjunction*, les distracteurs peuvent avoir n’importe quelle forme et n’importe quelle couleur, avec pour seule contrainte qu’ils ne peuvent pas être identiques à la cible. Ainsi, par exemple, si la cible est un carré jaune, alors les distracteurs sont des cercles jaunes, des cercles bleus et des carrés bleus.

- Dans la condition *Shape Feature*, les distracteurs ont une forme différente de celle de la cible, mais peuvent avoir n’importe quelle couleur. Ainsi, par exemple, si la cible est un carré jaune, alors les distracteurs sont des cercles jaunes et des cercles bleus.

- Dans la condition *Color Feature*, les distracteurs peuvent avoir n’importe quelle forme, mais ont une couleur différente de celle de la cible. Ainsi, par exemple, si la cible est un carré jaune, alors les distracteurs sont des carrés bleus et des cercles bleus.

Un feedback immédiat est présenté après chaque essai : un point vert après une réponse correcte, et un point rouge après une réponse incorrecte. Un feedback détaillé sur les temps de réponse moyens et la précision est présenté après chaque bloc d’essais.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg.png
 caption: The visual-search experiment that you will implement in this tutorial.
--%


Des expériences comme celle-ci montrent deux résultats typiques :

- Il faut plus de temps pour trouver la cible dans la condition Conjunction que dans les deux conditions Feature.
- Dans la condition Conjunction, les temps de réponse augmentent à mesure que le nombre de distracteurs augmente. Cela suggère que les personnes recherchent la cible un élément à la fois ; cela s’appelle une *recherche sérielle*.
- Dans les conditions Feature (forme et couleur), les temps de réponse n’augmentent pas, ou presque pas, à mesure que le nombre de distracteurs augmente. Cela suggère que les personnes traitent l’ensemble de l’affichage d’un seul coup ; cela s’appelle une *recherche parallèle*.

Selon la théorie de l’intégration des caractéristiques de Treisman et Gelade, ces résultats reflètent le fait que la condition Conjunction exige que vous combiniez, ou *associiez*, la couleur et la forme de chaque objet. Cette association nécessite de l’attention, et vous devez donc déplacer votre attention d’un objet à l’autre ; cela est lent, et explique pourquoi les temps de réponse dépendent du nombre d’objets présents. En revanche, dans les conditions Feature, la couleur et la forme n’ont pas besoin d’être associées, et l’ensemble de l’affichage peut donc être traité en un seul balayage sans que l’attention soit dirigée vers chacun des objets.

## Étape 1 : Construire la structure principale  

Avant de commencer à construire une expérience, il est utile de comprendre comment les expériences sont organisées dans OpenSesame. 
Dans OpenSesame, une expérience est composée d’items qui contrôlent ce qui se passe et dans quel ordre. 
Nous voulons d’abord définir cette structure afin que Sigmund puisse s’appuyer dessus. 

Le cadre de base de notre expérience comprend :

1. La séquence expérimentale principale – Elle contient toute l’expérience
2. Un emplacement pour les instructions générales – Les participants auront besoin d’instructions avant le début de l’expérience.
3. Une loop qui définit les différents blocs expérimentaux – Une loop répète une partie de l’expérience plusieurs fois. Dans notre cas, chaque répétition correspondra à un bloc expérimental.
4. Une sequence qui définit ce qui se passe à l’intérieur de chaque bloc – Cette sequence contiendra plus tard les essais et la logique spécifique au bloc.
5. Et un écran de fin – Pour que les participants sachent quand l’expérience est terminée.

L’utilisation d’une structure claire comme celle-ci permet à Sigmund comme à nous de rester organisés. Si nous essayons de faire construire tout en une seule fois par Sigmund, Sigmund aura davantage de chances de faire des erreurs et il nous sera plus difficile de repérer les problèmes et de les corriger. 

Commençons donc par créer le cadre, et nous remplirons les détails plus tard !


💬 **Prompt :**

```text
Hi Sigmund! I’d like to build a visual search experiment. Please create this structure without adding content yet:

- experiment (sequence)
  - instructions (sketchpad)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_message (sketchpad)
```

Quand Sigmund aura terminé, la vue d’ensemble devrait ressembler à %FigStep1 : 

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area after creating the main structure.
--%


Avant de continuer, nous devrions demander à Sigmund de donner à notre expérience un nom approprié et de supprimer tous les items par défaut inutiles : 


💬 **Prompt :**
```text
Please remove unnecessary default items and give the experiment a clear title.
```

%--
figure:
 id: FigStep1b
 source: step1b.png
 caption: |
  The overview area at the end of Step 1.
--%


## Étape 2 : Construire la block_sequence 

L’expérience de recherche visuelle est hiérarchique. Cela signifie que l’expérience contient des blocs et que les blocs eux-mêmes contiennent des essais. Dans chaque bloc, les participants effectueront plusieurs essais en recherchant la même cible. Il est important de ne pas confondre ces niveaux, sinon les cibles pourraient varier d’un essai à l’autre ! 


L’étape suivante consiste à construire la structure d’un bloc unique. Chaque bloc doit comporter : 

1. Des instructions qui indiquent au participant quelle est la cible
2. Une loop qui exécute tous les essais pour ce bloc 
3. Un écran de feedback du bloc

💬 **Prompt :**

```text
Now create the block_sequence contents. It should look like this:

- block_sequence (sequence)
  - block_instructions (sketchpad)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)
  
Just build the structure for now.
```

Votre vue d’ensemble devrait maintenant ressembler à %FigStep2.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%


## Étape 3 : Définir les variables inter-blocs

Les cibles ont deux caractéristiques, la forme et la couleur, qui changent entre les blocs. Par conséquent, Sigmund doit les définir dans la boucle externe (experimental_loop).  
Si nous définissons ces variables à l’intérieur de la boucle d’essai à la place, la cible change à chaque essai au lieu de changer à chaque bloc.

Nous demandons maintenant à Sigmund de définir des variables dans experimental_loop pour créer toutes les combinaisons de circle/square et blue/yellow.


💬 **Prompt :**

```text
Please define the variables in experimental_loop so that all combinations of:

  1. target_shape (circle/square)
  2. target_color (blue/yellow)

occur equally often across blocks.
```

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The table of experimental_loop at the end of step 3."
--%


## Étape 4 : Définir les conditions d’essai

À l’intérieur de chaque bloc, trois facteurs varient d’un essai à l’autre :

1. La condition (conjunction / shape / color)
2. Le nombre de stimuli (1 / 5 / 15)
3. La présence ou non de la cible.

Nous voulons que Sigmund crée des conditions d’essai pour toutes les combinaisons, c’est-à-dire un plan factoriel complet.
3 conditions x 3 tailles d’ensemble x 2 niveaux de présence = 18 types d’essais

💬 **Prompt :**

```text
Now define the block_loop variables. This should be a full factorial design with:

- condition: conjunction, feature_shape, feature_color
- set_size: 1, 5, 15
- target_present: present, absent

Please create all combinations.
```

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The table of block_loop at the end of step 4."
--%


## Étape 5 : Construire la séquence d’essai

Nous devons maintenant définir ce qui se passe pendant un seul essai. Commençons d’abord par créer les items ; nous ajouterons leur contenu dans les étapes suivantes.
Pendant un seul essai, nous :

1. Affichons un point de fixation  
2. Affichons l’écran principal de recherche (cela nécessite un inline_script)
3. Recueillons la réponse du participant  
4. Enregistrons les données dont nous avons besoin  
5. Donnons un feedback au participant


💬 **Prompt :**

```text
Please add items to trial_sequence in this order:

- fixation (sketchpad)
- search_display_script (inline_script)
- keyboard_response (keyboard_response)
- logger (logger)
- green_feedback (sketchpad)
- red_feedback (sketchpad)

Only create the items for now, don’t add content yet.
```

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The trial_sequence at the end of Step 5."
--%


## Étape 6 : Écran de fixation

Commençons à ajouter du contenu ! Demandez à Sigmund de dessiner un point de fixation sur le sketchpad : 

💬 **Prompt :**

```text
Please draw a central fixation dot in the fixation item and set its duration to 500 ms.
```

%--
figure:
 id: FigStep6
 source: step6.png
 caption: "The fixation display"
--%


## Étape 7 : Générer l’affichage de recherche visuelle

La génération de l’affichage de recherche visuelle dépasse ce que l’interface graphique d’OpenSesame peut faire. Nous avons besoin d’une génération dynamique des stimuli, d’un placement aléatoire et d’une logique conditionnelle. OpenSesame permet de faire cela en utilisant Python (`inline_script`) ou JavaScript (`inline_javscript`). Dans notre cas, nous utiliserons Python. Nous avons déjà ajouté un script en ligne (vide) à la trial_sequence à l’Étape 5.

Mais que faire si nous ne pouvons pas ou ne voulons pas écrire un script nous-mêmes ? Sigmund peut le faire pour nous ! Dites à Sigmund d’écrire le script dont nous avons besoin : 

💬 **Prompt :**

```text
Now implement the search display using the inline script. It should:

- create a canvas
- generate random non-overlapping positions
- draw the target if present
- draw distractors based on the condition:
  - conjunction: any shape/color except target combination
  - feature_shape: shape must differ from target
  - feature_color: color must differ from target
- use the set_size variable for the number of items
- raise an error if invalid values occur

The script should show the canvas.
```

Comme cette tâche est un peu plus complexe, Sigmund fait parfois des erreurs. Cependant, Sigmund peut parfois les corriger lui-même ! Essayez d’exécuter l’expérience et, si une erreur apparaît, demandez à Sigmund de la corriger.

Un exemple d’erreur fréquente est que Sigmund oublie parfois d’importer une bibliothèque Python, comme `random`. Si vous le remarquez, vous pouvez le signaler et demander à Sigmund de le corriger !

💬 **Prompt :**

```text
It looks like you forgot to import random. Please fix it!
```

Si tout s’est bien passé, vous pouvez maintenant exécuter l’expérience (même si elle est encore incomplète) et elle affichera un écran comme celui-ci :

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "A visual search display."
--%


## Étape 8 : Définir la réponse correcte 

L’item keyboard_response que Sigmund a ajouté plus tôt vérifie les réponses par rapport à une variable appelée correct_response. Nous devons donc définir la bonne réponse avant que la réponse ne soit recueillie. Nous pouvons demander à Sigmund de le faire avec un inline script : 

💬 **Prompt :**

```text
Add logic so the experiment knows the correct response.

- If target_present is present → correct_response is right arrow key.
- If target_present is absent → correct_response is left arrow key.

Please implement this using a new inline script placed before the keyboard response item.
```

## Étape 9 : Configurer le keyboard_response 

Seules les touches flèche gauche et flèche droite sont des réponses valides, nous limitons donc les participants à celles-ci. Nous pouvons aussi demander à Sigmund de passer automatiquement à l’essai suivant après un délai fixe si le participant ne répond pas dans un temps raisonnable (c.-à-d. un timeout).

💬 **Prompt :**

```text
Please configure the keyboard response so that:

- timeout is 3000 ms
- only left and right arrow keys are allowed
```

## Étape 10 : Créer les écrans de feedback 

Ensuite, nous voulons donner aux participants un feedback indiquant s’ils ont correctement identifié la présence de la cible lors d’un essai. Dites à Sigmund de définir dynamiquement l’affichage du feedback :

💬 **Prompt :**

```text
Now configure the feedback sketchpads:

- green_feedback should show a green fixation dot for 500 ms
- red_feedback should show a red fixation dot for 500 ms

Show green only after correct responses and red only after incorrect responses.
```

## Étape 11 : Instructions de bloc 

Les participants doivent savoir ce qu’ils cherchent ! Demandez à Sigmund de créer l’écran d’instructions et d’afficher une représentation de la cible actuelle : 

💬 **Prompt :**

```
Please add instructions to block_instructions that tell participants which target to search for, based on the current block’s target shape and color. Visually show what the target looks like.
```

%--
figure:
 id: FigStep11
 source: step11.png
 caption: "The instruction display."
--%


## Étape 12 : Feedback de bloc 

Après chaque bloc, nous donnons aux participants un feedback sur leurs performances en fonction de leur précision et de leur temps de réponse. Laissez Sigmund créer l’écran pour nous :

💬 **Prompt :**

```text
Configure the feedback item so it shows average accuracy and response time for the block.
```

%--
figure:
 id: FigStep12
 source: step12.png
 caption: "The block feedback display."
--%


## Étape 13 : Message de fin

Enfin, nous ajoutons un message de fin.

💬 **Prompt :**

```text
Set an end of experiment message in end_message.
```

## Terminé

Félicitations, l’expérience est terminée ! Vous pouvez l’essayer en cliquant sur le bouton bleu à double flèche (raccourci : Ctrl+W).

Voici à quoi ressemble un bloc de recherche visuelle terminé :

<video controls width="100%">
  <source src="/video/visual-search-demo.mp4" type="video/mp4">
</video>

<p align="center"><em>Vidéo 2. Démonstration d’un bloc de recherche visuelle terminé.</em></p>

Pour vous assurer que l’expérience fonctionne bien, vérifiez si vous reconnaissez les éléments suivants :

1. Chaque bloc commence par des instructions montrant la forme et la couleur de la cible actuelle
2. Chaque essai comporte un point de fixation et le bon feedback est affiché immédiatement après chaque essai 
3. D’un essai à l’autre, la taille des ensembles et la présence de la cible varient 
4. Après chaque bloc, un résumé des performances est affiché

Si vous remarquez de petits bugs ou des erreurs, ne vous inquiétez pas. Sigmund peut souvent les corriger tout seul. Essayez d’exécuter l’expérience et, si une erreur apparaît, décrivez simplement le problème à Sigmund et demandez-lui de le corriger. Par exemple, Sigmund peut généralement corriger des imports manquants, des noms de variables incorrects ou de petites erreurs de logique lorsque vous les lui signalez. Apprendre à tester votre expérience et à demander de manière itérative à Sigmund des corrections ciblées est une partie importante d’un travail efficace avec un copilote IA.

## Références

<div class='reference' markdown='1'>
Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, *12*(1), 97–136. doi:10.1016/0010-0285(80)90005-5
</div>

[references]: #references