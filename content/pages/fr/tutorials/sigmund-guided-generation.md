title: Utilisez la génération guidée pour créer n’importe quelle expérience avec SigmundAI
hash: 9fd2992708f865ec29c9a7080a645de89d5d0a9619c8e543101fe468cd89d355
locale: fr
language: French

[TOC]


## À propos de ce tutoriel

Dans ce tutoriel, vous apprendrez à construire n’importe quelle expérience avec SigmundAI. Il ne s’agit pas d’un tutoriel étape par étape centré sur une expérience spécifique. Il présente plutôt un workflow général, que vous pouvez adapter selon vos besoins.

N’attendez pas de miracles ! Si vous avez une expérience complexe, Sigmund aura probablement du mal si on le laisse complètement livré à lui-même. Vous devrez souvent travailler activement avec Sigmund pour mettre en œuvre une expérience.

J’appelle cela la *génération guidée*, parce que vous guidez Sigmund tout au long du processus.

Si vous n’avez pas encore travaillé avec Sigmund, je vous recommande de commencer par suivre [le tutoriel débutant pour SigmundAI](%url:beginner-sigmund%).


## Ce que vous allez apprendre

À la fin de ce tutoriel, vous saurez comment :

- 💡 Donner à Sigmund des instructions claires et efficaces
- 💡 Décomposer le processus de création d’une expérience complète à partir de zéro en étapes gérables
- 💡 Corriger les erreurs que Sigmund peut faire lors de la construction d’une expérience.


## Quel modèle dois-je utiliser ?

La plupart des étapes ne nécessitent pas un modèle particulièrement puissant. J’utilise principalement Z.ai GLM 5.2, qui, au moment de la rédaction, offre un bon équilibre entre intelligence et coût. Cependant, l’étape finale de mise en œuvre repousse les limites de ce que la plupart des modèles d’IA peuvent faire. Par conséquent, à ce stade, vous pouvez passer à un modèle plus puissant, comme Claude Sonnet 5. Gardez à l’esprit que les modèles plus puissants sont aussi (beaucoup) plus coûteux.

En pratique, essayez différents modèles pour voir lesquels donnent les meilleurs résultats pour vos expériences spécifiques.


## Workflow

Voici ce que nous allons faire :

1. Décrire l’expérience que vous souhaitez construire en langage clair.
2. Demander à Sigmund de développer votre description en une description narrative complète qui spécifie l’expérience dans tous ses détails.
3. Relire la description complète. Si nécessaire, en discuter et l’ajuster.
4. Demander à Sigmund de développer une spécification JSON (un format technique lisible par l’humain) qui décrit la structure expérimentale.
5. Relire la spécification JSON. Si nécessaire, en discuter et l’ajuster.
6. Demander à Sigmund de construire l’expérience entière d’un seul coup.
7. Tester et peaufiner l’expérience.

Ce tutoriel porte sur la manière de communiquer efficacement avec Sigmund. Nous allons aider Sigmund à subdiviser la tâche complexe de construire une expérience en sous-tâches gérables, et fournir des instructions concrètes sur ce qu’il faut faire et à quel moment.

__Important :__ Vous devez parler à Sigmund via le panneau de chat à l’intérieur d’OpenSesame. Si vous utilisez l’interface web, Sigmund ne pourra pas contrôler OpenSesame.


## Développer une description narrative complète de l’expérience

Voici la description de l’expérience que nous utiliserons pour cet exemple :

💬 **Description :**

```text
Une tâche typique de mémoire de travail visuelle dans laquelle des cercles de différentes couleurs doivent être mémorisés. Un cercle est sondé en présentant un cercle soit de la même couleur, soit d’une couleur différente à l’emplacement d’origine du cercle. Le participant répond par un jugement same/different. La taille de l’ensemble varie.
```

Nous commençons par demander à Sigmund d’étoffer une description détaillée d’une expérience à partir de cette description. Dans votre description de l’expérience, fournissez autant de détails que possible, car cela aide Sigmund à proposer une conception qui correspond à ce que vous avez en tête. Par exemple, si vous pensez que la logique des essais doit être implémentée avec un `inline_script`, indiquez-le.

Nous incluons cette description dans un prompt qui fournit des instructions claires à Sigmund :

💬 **Prompt :**

```text
J’ai une tâche difficile pour toi ! Nous allons mettre en œuvre une expérience OpenSesame à partir de zéro. Nous allons décomposer le processus en quelques étapes pour que cela reste gérable. À l’étape actuelle, ta tâche consiste à développer la description de la tâche expérimentale afin qu’elle contienne tous les détails dont nous avons besoin pour l’implémenter.

Voici quelques éléments à prendre en compte pour la structure des essais :

- La manière dont les participants répondent
- Le timing des stimuli
- L’apparence des stimuli
- La disposition des stimuli
- Si un feedback au participant est fourni et, si oui, comment
- Tout stimulus qui n’est pas explicitement mentionné mais qui devrait être inclus
- Les affichages vides ou de fixation entre les stimuli (s’il y a un point de fixation, il est généralement affiché pendant tout l’essai)

Voici quelques éléments à prendre en compte pour la structure de l’expérience :

- Les variables indépendantes et dépendantes
- La présence ou non d’une phase de pratique
- Le fait que les essais soient ou non subdivisés en blocs d’essais
- Le nombre d’essais et de blocs (le cas échéant)
- Les écrans de bienvenue, d’instructions et d’au revoir

Veuillez également inclure toute information supplémentaire que vous jugez pertinente.

<experimental_task_description>
Une tâche typique de mémoire de travail visuelle dans laquelle des cercles de différentes couleurs doivent être mémorisés. Un cercle est testé en présentant un cercle soit de la même couleur, soit d’une couleur différente à l’emplacement du cercle d’origine. Le participant répond par un jugement same/different. La taille de l’ensemble varie.
</experimental_task_description>

Veuillez répondre avec une description complète. Ne l’enregistrez pas encore comme note, car nous allons d’abord la revoir.
```

Sigmund répondra avec une description détaillée de l’expérience. Passez-la en revue et apportez des corrections si nécessaire. Si cela vous convient, demandez à Sigmund d’en faire une note.


💬 **Prompt :**

```text
Super ! Veuillez enregistrer la description complète comme note persistante afin de ne pas l’oublier. Ne la résumez pas, mais enregistrez-la intégralement.
```


## Élaboration d’une spécification JSON pour la structure expérimentale

Nous allons maintenant demander à Sigmund de concevoir la structure expérimentale. Cela spécifie quels items composent l’expérience et comment ils sont connectés.

Le deuxième point du prompt mentionne quels types d’items peuvent être utilisés. Pour aider Sigmund, supprimez les types d’items dont vous savez qu’ils ne seront pas nécessaires. Par exemple, si les participants n’utiliseront pas la souris pour répondre, vous pouvez supprimer le type d’item `mouse_response`.


💬 **Prompt :**

```text
On continue ! Voici votre prochaine tâche :

- Rédigez une spécification JSON basée sur la description narrative de l’expérience que vous venez d’enregistrer comme note.
- Chaque dict dans le JSON doit correspondre à un seul item OpenSesame. Vous pouvez utiliser les items suivants : [loop, sequence, sketchpad, feedback, synth, sampler, keyboard_response, mouse_response, logger, inline_script, inline_javascript, form_multiple_choice, form_text_display, form_text_input, reset_feedback]
- Les items sketchpad sont préparés à l’avance et ne peuvent donc pas prendre en compte des variables qui sont définies après leur phase de préparation. Par conséquent, pour afficher des écrans avec un contenu variable, vous voudrez souvent utiliser plutôt des items feedback, mais uniquement pour des affichages qui ne sont pas critiques en termes de temps.
- N’utilisez pas plusieurs items logger non liés, car cela produira des fichiers journaux désordonnés. Utilisez plutôt des copies liées du même logger.
- Ne placez pas d’items reset_feedback dans la séquence principale de l’expérience, car cela n’est pas compatible avec OSWeb.
- N’incluez aucun détail d’implémentation pour les items. Nous y reviendrons plus tard. Pour l’instant, fournissez simplement une description, un nom et un type. Pour les items qui font partie d’une séquence, vous pouvez aussi fournir une expression run-if.
- Les items qui sont des copies liées d’items apparaissant ailleurs ne doivent être détaillés que lors de leur première occurrence ; pour les occurrences suivantes, fournissez uniquement le nom (les items portant le même nom sont des copies liées).
- Les items qui ont des items enfants ont un champ supplémentaire `items`. Un loop a toujours une seule séquence comme item enfant. Une séquence a généralement plusieurs items enfants de différents types.
- Veuillez utiliser des copies liées des items chaque fois que possible. Pour indiquer qu’un item est une copie liée d’un autre, réutilisez simplement le même nom et ajoutez un champ `linked` défini sur `true`.
- L’exemple de spécification JSON ci-dessous montre l’idée générale, mais il est fortement simplifié. Votre spécification JSON sera probablement beaucoup plus élaborée.

<json_example>
{
  "name": "experiment",
  "type": "sequence",
  "description": "Une description de la tâche en une ligne",
  "items": [
    {
      "name": "task_description",
      "type": "notepad",
      "description": "La description narrative complète de la tâche va ici."
    },
    {
      "name": "welcome",
      "type": "sketchpad",
      "description": "Bref message de bienvenue"
    },
    {
      "name": "block_loop",
      "type": "loop",
      "description": "Un bloc d’essais. Les variables indépendantes sont également définies ici.",
      "items": [
        {
          "name": "trial_sequence",
          "type": "sequence",
          "description": "Séquence pour un seul essai",
          "items": [
            {
              "name": "fixation",
              "type": "sketchpad",
              "description": "Affiche une croix de fixation noire (+) pendant 500 ms"
            },
            {
              "name": "target_display",
              "type": "sketchpad",
              "description": "Affiche le stimulus cible tandis que la croix de fixation reste visible"
            },
            {
              "name": "keyboard_response",
              "type": "keyboard_response",
              "description": "Recueille la réponse du participant au stimulus cible"
            },
            {
              "name": "correct_feedback",
              "type": "sketchpad",
              "description": "Affiche un point de fixation vert pendant 500 ms après une réponse correcte",
              "run_if": "correct == 1"
            },
            {
              "name": "fixation",
              "linked": true
            },
            {
              "name": "logger",
              "type": "logger",
              "description": "Enregistre toutes les données d’essai"
            }
          ]
        }
      ]
    }
  ]
}
</json_example>

Veuillez répondre avec la spécification JSON pour la description narrative de l’expérience. N’enregistrez pas encore la spécification JSON comme note, car nous allons d’abord la passer en revue.
```

Sigmund va maintenant fournir une spécification JSON détaillée, qui est essentiellement une vue technique de la zone d’aperçu dans OpenSesame. Examinez la spécification et fournissez un retour si nécessaire. Si tout vous convient, demandez à Sigmund d’en prendre note.

💬 **Prompt :**

```text
Beautiful, well done Sigmund! Please save this as another persistent note so you don't forget. Do not summarize it, but save it in full.
```


## Implémentation de l’expérience

Nous sommes maintenant prêts à commencer ! Cette dernière étape repousse les limites de ce que la plupart des modèles d’IA peuvent faire. Si vous constatez que Sigmund échoue systématiquement, essayez de passer à un modèle plus puissant. J’ai obtenu de bons résultats avec Claude Sonnet 5.

💬 **Prompt :**

```text
We're now ready to implement the experiment. A few pointers:

- Save these instructions as a persistent note so you don't forget.
- Do *not* inspect items of the current experiment. They're not relevant, because we're going to completely overwrite the current experiment.
- Do *not* inspect the general script of the current experiment for the same reason.
- Before writing the experiment script, call `opensesame_get_syntax_documentation` with `save_as="note"` to get all relevant documentation.
- Finally, write the new experiment as a single complete general script and pass it to `opensesame_update_general_script`.

This is a challenging task, but I know you can do it. Let's go!
```

Sigmund parvient à implémenter avec succès l’expérience de mémoire de travail visuelle utilisée comme exemple. Cependant, toutes les expériences ne se dérouleront pas forcément aussi bien.

Si Sigmund remarque qu’il a fait une erreur de syntaxe en générant l’expérience, il essaiera de la corriger. Sigmund peut se retrouver bloqué dans une boucle infinie en essayant de faire fonctionner les choses. Lorsque cela se produit, interrompez la conversation.

Si l’expérience est générée avec succès, elle peut malgré tout contenir des erreurs ou des imperfections. Testez-la soigneusement et peaufinez-la !


## Exemples d’expériences créées avec génération guidée

Pour tous les exemples ci-dessous, les étapes initiales ont été effectuées avec Z.ai GLM 5.2, et l’étape finale d’implémentation a été réalisée avec Claude Sonnet 5. Je n’ai fourni aucun retour sur la description complète ni sur la spécification JSON. Cependant, j’ai peaufiné l’expérience finale comme décrit dans les notes ci-dessous.


### Mémoire de travail visuelle

💬 **Description :**

```text
A typical visual-working-memory task where circles of different colors need to be remembered. One circle is probed by presenting a circle of either the same or a different color at the original circle's location. The participant responds with a same/different judgment. Set size is varied.
```

Notes :

- Sigmund a utilisé la syntaxe obsolète `[square_brackets_syntax]` pour faire référence aux variables dans les éléments SKETCHPAD. Cela fonctionne, mais je l’ai remplacée par la syntaxe préférée `{curly_brackets_syntax}`.
- Sigmund a utilisé Python INLINE_SCRIPT pour cette expérience. Par conséquent, elle ne peut pas être exécutée dans un navigateur.

Essayez l’expérience :

- %static:attachments/sigmund/sigmund-visual-working-memory.osexp%


### Posner cuing

💬 **Description :**

```text
A Posner cuing paradigm with a central cue and a letter-discrimination task.
```

Notes :

- Sigmund a utilisé des marqueurs unicode (par ex. `\u2190`) pour les indices fléchés. Ils ne sont pas affichés par OpenSesame et ont dû être remplacés par les caractères réels (par ex. '←').
- Sigmund a utilisé la syntaxe obsolète `[square_brackets_syntax]` pour faire référence aux variables dans les éléments SKETCHPAD. Cela fonctionne, mais je l’ai remplacée par la syntaxe préférée `{curly_brackets_syntax}`.

Essayez l’expérience :

- %static:attachments/sigmund/sigmund-posner-cuing.osexp%
- [Exécuter dans le navigateur](https://jatos.mindprobe.eu/publix/QgymMCSRYzL)


### AX continuous performance

💬 **Description :**

```text
An AX continuous performance task.
```

Notes :

- Sigmund a oublié de définir quels éléments exécuter dans les différents éléments `sequence`. Cela a dû être corrigé manuellement.

Essayez l’expérience :

- %static:attachments/sigmund/sigmund-axcpt.osexp%
- [Exécuter dans le navigateur](https://jatos.mindprobe.eu/publix/5s8TbGLx0bZ)