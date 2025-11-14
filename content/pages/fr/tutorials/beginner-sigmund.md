title: Tutoriel SigmundAI : orientation du regard
hash: 80f0a9ae4381f62b46aa6b1cca4b807990e8235070ac5187f47bc98a6f028d00
locale: fr
language: French

[TOC]


## À propos de ce tutoriel

Dans ce tutoriel, vous allez construire une expérience de psychologie en travaillant avec SigmundAI, votre copilote IA pour OpenSesame. Vous apprendrez à donner des instructions claires à Sigmund, à repérer et corriger les erreurs, et à créer des expériences plus rapidement que jamais.

Nous allons créer une expérience classique d’orientation du regard. Il s'agit d'un paradigme amusant et intéressant, où les gens ne peuvent s'empêcher de suivre la direction du regard d'un visage.

Ce tutoriel fait suite au [tutoriel débutant](%url:beginner%), en utilisant la même expérience mais en vous montrant comment la réaliser avec l’aide de l’IA.


## Ce que vous allez apprendre

À la fin de ce tutoriel, vous saurez :

- 💡 Donner des instructions claires et efficaces à Sigmund
- 💡 Décomposer des tâches complexes en étapes simples
- 💡 Repérer et corriger les erreurs de Sigmund (oui, l’IA fait des erreurs !)
- 💡 Construire rapidement la structure d’une expérience
- 💡 Travailler efficacement avec un copilote IA


## Ce dont vous aurez besoin

**OpenSesame 4.1 ou version ultérieure** avec toutes les mises à jour installées. Si une notification concernant des mises à jour disponibles apparaît, cliquez sur « Installer les mises à jour… » puis sur « Lancer le script de mise à jour ». Redémarrez OpenSesame après la mise à jour. Vous pouvez également mettre à jour manuellement en exécutant la commande suivante dans la console OpenSesame.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**Notions de base sur OpenSesame.** Vous débutez sur OpenSesame ? Commencez d'abord par le [tutoriel débutant](%url:beginner%). Comprendre les bases vous aidera à collaborer efficacement avec Sigmund. L’IA est puissante, mais elle ne remplace pas la compréhension du fonctionnement des outils.

**Un abonnement SigmundAI.** Il vous faudra un abonnement actif via [sigmundai.eu](https://sigmundai.eu/).


## Connecter OpenSesame à Sigmund

Sigmund est un assistant IA spécifiquement conçu pour OpenSesame. Contrairement à des chatbots génériques comme ChatGPT, Sigmund :

- Connaît OpenSesame sur le bout des doigts
- Fonctionne directement dans l’interface OpenSesame
- Peut apporter automatiquement des modifications à votre expérience

Pour vous connecter, il suffit de vous connecter sur [sigmundai.eu](https://sigmundai.eu/). Le panneau Sigmund dans OpenSesame se connectera automatiquement :

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>


## L’expérience

Comme indiqué, nous allons créer une expérience d’orientation du regard, développée à l'origine par [Friesen et Kingstone (1998)][references]. Voici comment cela fonctionne :

1. Un visage apparaît au centre de l'écran
2. Le visage regarde à gauche ou à droite
3. Une lettre cible (« F » ou « H ») apparaît d'un côté
4. Une lettre distractrice (« X ») apparaît de l’autre côté
5. Les participants identifient la lettre cible le plus rapidement possible

Le résultat intéressant ? Les personnes sont plus rapides lorsque le visage regarde vers la cible, même si la direction du regard ne prédit pas l’endroit où la cible apparaîtra. Cela montre que les humains suivent automatiquement la direction du regard des autres.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Le paradigme d’orientation du regard [(Friesen et Kingstone, 1998)][references]. Cet exemple montre un essai **incongru**, car le visage regarde vers le distracteur (« X ») au lieu de la cible (« F »).
--%


## Étape 1 : Créer la séquence principale

Commençons par construire la structure de base. L’expérience comporte deux phases : entraînement et expérimentation. Chaque phase doit comporter des instructions avant et un message après. Commencer par une structure claire aide à garder de l'organisation pour vous et pour Sigmund.

Lorsque vous vous adressez à Sigmund, soyez précis ! Indiquez exactement ce que vous souhaitez, et ce que vous *ne* souhaitez pas encore. Cela évite que Sigmund n’en fasse trop à la fois.

💬 **Invite :**

```text
Bonjour Sigmund ! J’aimerais construire ensemble une expérience d’orientation du regard. Commençons par la structure de base :

- experiment (sequence)
  - instructions (form_text_display)
  - practice_loop (loop)
    - block_sequence (sequence)
  - end_of_practice (form_text_display)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_of_experiment (form_text_display)
```

Veuillez créer cette structure sans ajouter de contenu aux éléments pour l’instant. Nous ferons cela étape par étape !
```

Après que Sigmund ait créé cette structure, nettoyons un peu les choses. Demandez-le dans une invite séparée pour ne pas submerger Sigmund avec trop de tâches à la fois.

💬 **Invite :**

```text
Parfait ! Maintenant, veuillez supprimer tous les éléments dont nous n’avons pas besoin, et donnez un titre clair à l’expérience.
```

Votre zone d’aperçu devrait ressembler à %FigStep1. (Le titre de votre expérience peut être légèrement différent. Ce n’est pas grave !)

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of Step 1.
--%


<div class='info-box' markdown='1'>

**💡 Gardez Sigmund sous contrôle !**

En bas du panneau Sigmund, vous pouvez choisir de revoir les actions de Sigmund avant qu’elles ne se produisent. Lorsqu'elle est activée, vous approuvez chaque modification que Sigmund propose.

- **Pour apprendre :** Laissez cette option ACTIVÉE. Vous comprendrez ce que fait Sigmund.
- **Pour aller vite :** Désactivez-la lorsque vous êtes à l’aise.

Rappelez-vous que Sigmund fait des erreurs ! Vérifiez toujours les résultats, surtout au début.

</div>


## Étape 2 : Créer la séquence de blocs

Construisons à présent le déroulé de chaque bloc d’essais. Chaque bloc suit ce schéma :

1. Réinitialiser le feedback (afin que la performance sur les blocs précédents n’affecte pas le feedback du bloc actuel)
2. Lancer une boucle d’essais
3. Afficher le feedback de performance

Les phases d’exercice et expérimentale utilisent le même item *block_sequence*. Ceci s’appelle une copie liée. Lorsque vous modifiez l’un, l’autre change aussi. Utiliser des copies liées est pratique quand une même fonctionnalité (comme un bloc d’essais) apparaît à plusieurs endroits de votre expérience.

💬 **Invite :**

```text
Parfait ! Ajoutons maintenant du contenu à block_sequence. Il doit être partagé entre les phases de pratique et expérimentale (copie liée). Structurez-le ainsi :

- block_sequence (sequence)
  - reset_feedback (reset_feedback)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)

Encore une fois, créez seulement la structure. Nous ajouterons le contenu plus tard. Prêt ? Allons-y !
```

Votre aperçu doit maintenant ressembler à %FigStep2.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%


## Étape 3 : Définir les conditions des essais

Chaque expérience comporte des variables indépendantes. Ce sont celles que vous manipulez. Dans notre expérience, nous faisons varier :

- La direction du regard du visage (gauche ou droite)
- L’endroit où apparaît la cible (gauche à -300, ou droite à 300)
- La lettre cible (F ou H)

Nous devons aussi calculer :

- Où va le distracteur (le côté opposé à la cible)
- Quelle est la touche de réponse correcte (z pour F, m pour H)

Cela crée un plan 2 × 2 × 2 = 8 types d’essais différents.

En expliquant le plan à Sigmund, nous aidons Sigmund à bien comprendre la logique et à créer toutes les combinaisons correctes.

💬 **Invite :**

```text
Définissons maintenant les variables dans block_loop. Il s’agit d’un plan 2 × 2 × 2 (8 lignes en tout) :

- gaze_cue : gauche ou droite
- target_pos : -300 ou 300 (coordonnée x, négatif = gauche, 0 = centre)
- target_letter : F ou H
- dist_pos : opposé à target_pos
- correct_response : z quand target_letter vaut F, m quand target_letter vaut H

Pouvez-vous faire cela ? Merci !
```

Votre *block_loop* doit maintenant ressembler à %FigStep3, avec 8 lignes affichant toutes les combinaisons possibles.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%


<div class='info-box' markdown='1'>

**🤖 Choisissez un modèle d’IA qui vous convient !**

Sigmund n’est pas une unique IA. C’est un chatbot qui peut utiliser différents modèles d’IA. Sur [sigmundai.eu](https://sigmundai.eu), vous pouvez choisir parmi plusieurs modèles.

Ce tutoriel a été testé avec **Claude Sonnet 4.5** et **GPT-5**, tous deux en mode conversation.

Astuces :

- Différents modèles ont des forces différentes. Expérimentez pour trouver votre préféré.
- Les modèles de résolution de problèmes sont plus lents et ne sont pas toujours meilleurs pour les tâches simples.

</div>


## Étape 4 : Ajouter des images et sons à la banque de fichiers

Nous avons besoin de certains fichiers pour nos stimuli :

- Images d’un visage regardant de façon neutre, à gauche et à droite
- Un son à jouer lorsque les participants font une erreur

Sigmund ne peut pas télécharger les fichiers pour vous, donc vous devrez effectuer cette partie manuellement. Téléchargez les fichiers ci-dessous et faites-les glisser dans votre file pool :

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Le file pool devrait ressembler à %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## Étape 5 : Construire la séquence d’essai

Il est temps de créer la structure d’un essai unique. Voici ce qui se passe à chaque essai :

1. Afficher un point de fixation (préparez-vous !)
2. Afficher le visage neutre (voici le visage)
3. Afficher l’indice de regard (le visage regarde à gauche ou à droite)
4. Afficher la cible et le distracteur (il est temps de répondre !)
5. Recueillir la réponse au clavier
6. Jouer le son d’erreur (uniquement si la réponse était incorrecte)
7. Enregistrer les données

Le son d’erreur ne doit être joué que lors des essais incorrects. Cela utilise une expression run-if : une condition qui détermine quand un item s’exécute.

💬 **Invite :**

```text
Ajoutons des items à la trial_sequence :

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — à jouer uniquement après une réponse incorrecte
- logger (logger)

Créez simplement les items pour l’instant, ne les remplissez pas encore. Pouvez-vous faire cela ?
```

Cette tâche requiert de nombreuses actions, et Sigmund se trompe parfois. Vérifiez bien son travail.

Erreurs courantes de Sigmund ici :

- Oublier de créer certains items
- Oublier d’ajouter l’expression run-if pour *incorrect_sound*

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oups ! Sigmund a oublié d’ajouter un logger et de définir une expression run-if pour incorrect_sound."
--%

Si Sigmund a fait une erreur (comme oublier le logger ou l’expression run-if), donnez-lui un rappel doux avec des instructions spécifiques :

💬 **Invite** (à ajuster selon ce qui manque) :

```text
Je remarque que le logger est manquant. Pourriez-vous l’ajouter s’il vous plaît ?

Ensuite, pourriez-vous sélectionner la trial_sequence et ajouter une expression run-if pour le sampler incorrect_sound ? Rappelez-vous que les expressions run-if sont définies dans la séquence qui contient l’item, pas dans l’item lui-même.
```

Pourquoi Sigmund fait-il des erreurs ? L’IA est imprévisible, donc des erreurs peuvent arriver pour toute tâche. Cependant, Sigmund a particulièrement du mal avec les tâches multi-étapes. Celle-ci demandait 9 actions distinctes ! Lorsque vous demandez des tâches complexes, vérifiez toujours attentivement le résultat.

Votre *trial_sequence* devrait ressembler à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "La *trial_sequence* à la fin de l’étape 5."
--%


## Étape 6 : Dessiner les items d’affichage

Passons à la partie amusante : créer ce que les participants vont voir ! Nous allons travailler chaque écran un par un.

Tout d’abord, configurons les couleurs et dessinons le point de fixation initial. Nos stimuli de regard utilisent un fond blanc, donc nous avons besoin d’un fond blanc avec des éléments noirs.

💬 **Invite :**

```text
Pourriez-vous changer les paramètres de l’expérience pour utiliser des stimuli noirs sur un fond blanc ? Puis ajoutez un point de fixation à l’item fixation_dot et définissez sa durée à 745 ms.
```

Ensuite, l’affichage du visage neutre :

💬 **Invite :**

```text
Super ! Maintenant, ajoutez l’image du regard neutre. La durée doit être de 745 ms.
```

Sigmund devrait avoir compris qu’il faut utiliser le fichier *gaze_neutral.png* du file pool. Regardez le sketchpad pour vérifier !

Maintenant l’indice de regard (où le visage regarde) :

💬 **Invite :**

```text
Parfait ! Ajoutez maintenant l’affiche du regard indicateur. Elle doit être affichée pendant 495 ms.
```

Sigmund devrait utiliser la variable `gaze_cue` pour afficher soit *gaze_left.png* soit *gaze_right.png*.

Enfin, l’affichage de la cible (le plus complexe) :

💬 **Invite :**

```text
Excellent ! Maintenant, créez l'affichage cible. Il doit afficher :

- L’indice du regard (visage toujours orienté)
- La lettre cible à gauche ou à droite (en fonction de target_pos)
- Un « X » du côté opposé
```

La durée doit être de 0 parce que l’élément *keyboard_response* vient ensuite et attendra une réponse. Vérifiez que Sigmund a bien fait cela !

## Étape 7 : Configurez la réponse clavier

Nous devons maintenant recueillir les réponses des participants.

💬 **Invite :**

```text
Veuillez configurer la réponse clavier avec un délai d’attente de 2000 ms. N’acceptez que les touches de réponse correctes (z et m).
```

## Étape 8 : Configurez le son d’erreur

Lorsque les participants se trompent, ils doivent entendre un signal sonore.

💬 **Invite :**

```text
Configurez maintenant le sampler incorrect_sound pour jouer le fichier sonore d’erreur.
```

## Étape 9 : Créez l’écran de feedback

Après chaque bloc, les participants doivent voir comment ils s’en sortent.

💬 **Invite :**

```text
Ajoutez un feedback à l’élément feedback affichant la précision moyenne et le temps de réponse moyen pour le bloc.
```

## Étape 10 : Définir les répétitions de blocs

Nous devons maintenant spécifier combien de fois chaque bloc doit être répété.

💬 **Invite :**

```text
Définissez la phase d’entraînement à 2 blocs et la phase expérimentale à 8 blocs. Créez également une variable « practice » (oui ou non) afin que nous puissions distinguer les essais d’entraînement des essais expérimentaux dans nos données.
```

## Étape 11 : Rédiger les écrans d’instructions

Les participants doivent savoir quoi faire ! Demandons à Sigmund de rédiger des instructions claires.

💬 **Invite :**

```text
Veuillez rédiger des instructions claires et concises pour l’expérience, ainsi que des messages utiles à la fin de la phase d’entraînement et à la fin de l’expérience. Utilisez votre jugement pour le contenu !
```

Lisez attentivement les instructions. Sont-elles claires ? Sont-elles compréhensibles ? N’hésitez pas à demander à Sigmund de les réviser si besoin !

## Étape 12 : Testez et déboguez !

Le moment de vérité est arrivé. Lancez l’expérience ! Appuyez sur le bouton bleu d’exécution rapide et voyez ce qui se passe. Vous pourriez obtenir une erreur ! C’est tout à fait normal. Voici une erreur possible :

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "An error appears. Don't panic!"
--%

Que se passe-t-il ? L’élément de fin de pratique essaie d’afficher la variable `acc` avant qu’elle n’existe. Cela arrive à cause des phases prepare-run d’OpenSesame : les éléments sont préparés à l’avance et, parfois, certaines variables ne sont pas encore définies à ce moment-là.

Sigmund peut généralement corriger de tels problèmes. Cliquez simplement sur « Demander à Sigmund de corriger cela » lorsque l’erreur apparaît. Une fois l’erreur corrigée, essayez de relancer l’expérience. Répétez si nécessaire.

Terminé ! Félicitations. Vous avez construit une expérience complète avec Sigmund !

💬 **Invite finale :**

```text
Merci Sigmund ! Excellent travail !
```

## Points clés à retenir

Vous avez appris à travailler efficacement avec un copilote IA ! Voici les principales leçons :

- ✅ **Soyez précis et clair** dans vos instructions.
- ✅ **Divisez les tâches complexes en étapes simples**. N’en demandez pas trop d’un coup.
- ✅ **Vérifiez toujours le travail de Sigmund**. L’IA peut faire des erreurs !
- ✅ **Posez des questions de suivi** si quelque chose ne vous paraît pas correct.
- ✅ **Soyez patient**. Le débogage fait partie du processus.

Avec de la pratique, vous et Sigmund formerez une excellente équipe ! 🤝

## Références

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references