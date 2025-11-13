title: Tutoriel SigmundAI : orientation du regard
hash: d5304ea6608e83e51e1a0e01bbc9e8efc6602bc92944fcf1444d2848f9e097fe
locale: fr
language: French

[TOC]


## À propos de ce tutoriel

Dans ce tutoriel, vous construirez une expérience de psychologie en collaborant avec SigmundAI, votre copilote IA pour OpenSesame. Vous apprendrez à donner des instructions claires à Sigmund, à détecter et corriger des erreurs, et à créer des expériences plus rapidement que jamais.

Nous allons créer une expérience classique d’orientation du regard ("gaze-cuing"). C’est un paradigme amusant et intéressant, où les gens ne peuvent s’empêcher de suivre la direction du regard d’un visage.

Ce tutoriel s'appuie sur [le tutoriel pour débutants](%url:beginner%), utilisant la même expérience mais en vous montrant comment la créer avec l’aide de l'IA.


## Ce que vous allez apprendre

À la fin de ce tutoriel, vous saurez :

- ✅ Donner à Sigmund des instructions claires et efficaces
- ✅ Décomposer des tâches complexes en étapes simples
- ✅ Détecter et corriger les erreurs de Sigmund (oui, l’IA fait des erreurs !)
- ✅ Construire rapidement la structure d’une expérience
- ✅ Travailler efficacement avec un copilote IA


## Ce dont vous aurez besoin

**OpenSesame 4.1 ou version ultérieure** avec toutes les mises à jour installées. Si vous voyez une notification concernant des mises à jour disponibles, cliquez sur « Installer les mises à jour… » puis sur « Exécuter le script de mise à jour ». Redémarrez OpenSesame après la mise à jour. Vous pouvez aussi mettre à jour manuellement en saisissant la commande suivante dans la console d’OpenSesame.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**Connaissances de base d’OpenSesame.** Nouveau sur OpenSesame ? Commencez d’abord par [le tutoriel pour débutants](%url:beginner%). Comprendre les bases vous aidera à collaborer efficacement avec Sigmund. L’IA est puissante, mais elle ne remplace pas la compréhension du fonctionnement général.

**Un abonnement SigmundAI.** Vous aurez besoin d’un abonnement actif sur [sigmundai.eu](https://sigmundai.eu/).


## Connecter OpenSesame à Sigmund

Sigmund est un assistant IA spécifiquement conçu pour OpenSesame. Contrairement aux chatbots généralistes comme ChatGPT, Sigmund :

- Connaît OpenSesame parfaitement
- Fonctionne directement dans l’interface d’OpenSesame
- Peut modifier automatiquement votre expérience

Pour vous connecter, connectez-vous simplement sur [sigmundai.eu](https://sigmundai.eu). Le panneau Sigmund dans OpenSesame se connectera automatiquement :

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>


## L'expérience

Comme mentionné, nous allons créer une expérience d’orientation du regard, initialement développée par [Friesen et Kingstone (1998)][references]. Voici comment cela fonctionne :

1. Un visage apparaît au centre de l’écran
2. Le visage regarde vers la gauche ou la droite
3. Une lettre cible (« F » ou « H ») apparaît d’un côté
4. Une lettre distractrice (« X ») apparaît de l’autre côté
5. Les participants identifient la lettre cible le plus rapidement possible

La découverte intéressante ? Les gens sont plus rapides lorsque le visage regarde vers la cible, même si la direction du regard ne prédit pas l’endroit où la cible apparaîtra. Cela montre que les humains suivent automatiquement le regard des autres.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Le paradigme d’orientation du regard [(Friesen et Kingstone, 1998)][references]. Cet exemple montre un essai **incongru**, car le visage regarde vers le distracteur (« X ») au lieu de la cible (« F »).
--%


## Étape 1 : Créer la séquence principale

Commençons par construire la structure de base. L’expérience comporte deux phases : la phase d’entraînement et la phase expérimentale. Chaque phase nécessite des instructions avant et un message après. Partir d’une structure claire aide à garder l’organisation, pour vous comme pour Sigmund.

Lorsque vous parlez à Sigmund, soyez précis ! Dites à Sigmund exactement ce que vous voulez, mais aussi ce que vous ne voulez *pas* encore. Cela évite que Sigmund n’en fasse trop d’un coup.

💬 **Prompt :**

```text
Salut Sigmund ! J’aimerais construire une expérience d’orientation du regard ensemble. Commençons par la structure de base :

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

Nous avons besoin de quelques fichiers pour nos stimuli :

- Images d’un visage regardant de façon neutre, à gauche et à droite
- Un son à jouer lorsque les participants font une erreur

Sigmund ne peut pas télécharger de fichiers pour vous, donc vous devrez faire cette partie manuellement. Téléchargez les fichiers ci-dessous et glissez-les dans votre pool de fichiers :

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Le pool de fichiers devrait ressembler à %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## Étape 5 : Construire la séquence d’essai

Il est temps de créer la structure d’un essai. Voici ce qui se passe à chaque essai :

1. Afficher un point de fixation (préparez-vous !)
2. Afficher le visage neutre (le visage arrive)
3. Afficher l’indice de regard (le visage regarde à gauche ou à droite)
4. Afficher la cible et le distracteur (il est temps de répondre !)
5. Recueillir la réponse au clavier
6. Jouer le son d’erreur (seulement si la réponse était fausse)
7. Logger les données

Le son d’erreur ne doit être joué que sur les essais incorrects. Cela utilise une expression run-if : une condition qui détermine quand un item s’exécute.

💬 **Message :**

```text
Ajoutons des items à la trial_sequence :

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — ne joue qu’après une réponse incorrecte
- logger (logger)

Crée simplement les items pour l’instant, n’ajoute pas encore de contenu. Peux-tu faire cela ?
```

Cette tâche nécessite de nombreuses actions et Sigmund se trompe parfois. Vérifie bien son travail.

**Erreurs courantes de Sigmund ici :**

- Oublier de créer certains items
- Oublier d’ajouter une expression de run-if pour *incorrect_sound*

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%

Si Sigmund a fait une erreur (comme oublier le logger ou l’expression run-if), donne-lui un rappel gentil avec des instructions spécifiques :

💬 **Message** (à adapter selon l’oubli) :

```text
Je remarque que le logger manque. Peux-tu l’ajouter s’il te plaît ? 

Ensuite, peux-tu sélectionner la trial_sequence et ajouter une expression run-if pour le sampler incorrect_sound ? Rappelle-toi, les expressions run-if se définissent dans la séquence qui contient l’item, pas dans l’item lui-même.
```

Pourquoi Sigmund fait-il des erreurs ? L’IA est imprévisible, ce qui veut dire que des erreurs peuvent survenir à n’importe quelle étape. Cependant, Sigmund a particulièrement du mal avec les tâches en plusieurs étapes. La tâche ci-dessus requérait 9 actions différentes ! Lorsque tu demandes des tâches complexes, vérifie toujours les résultats.

Ta *trial_sequence* devrait ressembler à %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## Étape 6 : Dessiner le contenu visuel

Passons maintenant à la partie amusante : créer ce que les participants verront ! Nous allons travailler sur chaque écran un par un.

D’abord, définissons les couleurs et dessinons le point de fixation de départ. Nos stimuli de regard utilisent un fond blanc, alors il nous faut un fond blanc avec des éléments noirs.

💬 **Message :**

```text
Peux-tu changer les paramètres de l’expérience pour utiliser des stimuli noirs sur fond blanc ? Puis ajoute un point de fixation dans l’item fixation_dot et règle sa durée à 745 ms.
```

Ensuite, l’écran avec le visage neutre :

💬 **Message :**

```text
Super ! Maintenant ajoute l’image du regard neutre. La durée doit être de 745 ms.
```

Sigmund devrait avoir compris qu’il fallait utiliser le fichier *gaze_neutral.png* du pool de fichiers. Vérifie le sketchpad pour t’en assurer !

Maintenant l’indice de regard (où le visage regarde) :

💬 **Message :**

```text
Parfait ! Maintenant ajoute l’écran d’indice de regard. Il doit être affiché pendant 495 ms.
```

Sigmund doit utiliser la variable `gaze_cue` pour afficher soit *gaze_left.png* soit *gaze_right.png*.

Enfin, l’affichage de la cible (le plus complexe) :

💬 **Message :**

```text
Excellent ! Maintenant, créez l'affichage de la cible. Il doit montrer :

- L'indice de regard (visage toujours orienté)
- La lettre cible à gauche ou à droite (selon target_pos)
- Un 'X' du côté opposé
```

La durée doit être 0 parce que l’item *keyboard_response* vient ensuite et attendra une réponse. Vérifiez que Sigmund a bien fait cela !


## Étape 7 : Configurer la réponse clavier

Nous devons maintenant recueillir les réponses des participants.

💬 **Invite :**

```text
Veuillez configurer keyboard_response avec un délai d’attente de 2000 ms. N’acceptez que les touches de réponse correctes (z et m).
```


## Étape 8 : Configurer le son d’erreur

Quand les participants font des erreurs, ils doivent entendre un retour sonore.

💬 **Invite :**

```text
Configurez maintenant incorrect_sound sampler pour jouer le fichier sonore d’erreur.
```


## Étape 9 : Créer l’écran de feedback

Après chaque bloc, les participants doivent voir leurs résultats.

💬 **Invite :**

```text
Ajoutez un feedback à l’item feedback affichant la précision moyenne et le temps de réponse du bloc.
```


## Étape 10 : Définir la répétition des blocs

Nous devons maintenant spécifier combien de fois répéter chaque bloc.

💬 **Invite :**

```text
Réglez la phase de pratique sur 2 blocs et la phase expérimentale sur 8 blocs. Créez également une variable 'practice' (oui ou non) pour distinguer les essais de pratique des essais expérimentaux dans nos données.
```


## Étape 11 : Rédiger les écrans d’instructions

Les participants doivent savoir ce qu’ils doivent faire ! Demandons à Sigmund d’écrire des instructions claires.

💬 **Invite :**

```text
Veuillez écrire des instructions claires et concises pour l’expérience, plus des messages utiles à la fin de la pratique et à la fin de l’expérience. Utilisez votre jugement pour le contenu !
```

Lisez les instructions. Sont-elles compréhensibles ? Sont-elles claires ? N’hésitez pas à demander à Sigmund de les revoir si besoin !


## Étape 12 : Test et débogage !

Le moment de vérité est arrivé. Exécutez l’expérience ! Appuyez sur le bouton quick-run bleu et voyez ce qu’il se passe. Vous pourriez obtenir une erreur ! C’est tout à fait normal. Voici une erreur possible :

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "Une erreur apparaît. Pas de panique !"
--%

Quel est le problème ? L’item de fin de pratique essaie d’afficher la variable `acc` avant qu’elle n’existe. Cela arrive à cause des phases de préparation et d’exécution d’OpenSesame : les items sont préparés à l’avance, et parfois les variables ne sont pas encore définies à ce moment-là.

Sigmund peut généralement corriger ce genre de problème. Il suffit de cliquer sur "Ask Sigmund to fix this" lorsque l’erreur apparaît. Une fois l’erreur corrigée, essayez de relancer l’expérience. Recommencez si nécessaire.

C’est fait ! Félicitations. Vous avez construit une expérience complète avec Sigmund !

💬 **Invite finale :**

```text
Merci Sigmund ! Excellent travail !
```


## À retenir

Vous avez appris à travailler efficacement avec un copilote IA ! Voici les principales leçons :

1. **Soyez précis et clair** dans vos instructions.
2. **Divisez les tâches complexes en étapes simples**. N’en demandez pas trop à la fois.
3. **Vérifiez toujours le travail de Sigmund**. L’IA peut faire des erreurs !
4. **Posez des questions complémentaires** lorsqu’il y a un problème.
5. **Soyez patient**. Le débogage fait partie du processus.

Avec de la pratique, vous et Sigmund formerez une excellente équipe ! 🤝


## Références

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references