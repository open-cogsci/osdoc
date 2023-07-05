title: Exécution d'expériences en ligne avec OSWeb
hash: f0cc1f57958c34a65409a874ee511e03fee4f8ee35bc0bef55d0af11ac74f56e
locale: fr
language: French

[TOC]


## Le workflow

Pour une introduction au workflow, voir également :

Mathôt, S., & March, J. (2022). Réaliser des expériences linguistiques en ligne avec OpenSesame et OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Preprint associé (non identique au manuscrit publié)](https://doi.org/10.31234/osf.io/wnryc)</small>


### Développement de votre expérience

Premièrement, vous développez votre expérience comme vous le feriez habituellement, en utilisant l'application de bureau OpenSesame. Toutes les fonctionnalités ne sont pas disponibles dans les expériences en ligne. Notamment, vous ne pouvez pas utiliser les éléments Python INLINE_SCRIPT, mais devez opter pour les éléments JavaScript INLINE_JAVASCRIPT à la place. Lors du développement de votre expérience, il est donc important de vérifier que votre expérience est compatible avec OSWeb.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%


### Téléchargement de votre expérience sur JATOS

Une fois que vous avez développé votre expérience, vous la publiez sur JATOS. JATOS est un serveur web qui gère les expériences : il vous permet de générer des liens que vous pouvez distribuer aux participants, et il stocke les données qui ont été collectées.

Il n'y a pas un seul serveur JATOS. De nombreuses institutions maintiennent leur propre serveur JATOS. De plus, <https://mindprobe.eu> est un serveur JATOS gratuit, parrainé par ESCoP et OpenSesame.

- %link:jatos%


### Collecte des données

Une fois que vous avez publié votre expérience sur JATOS, vous pouvez commencer à collecter les données. Vous pouvez le faire en envoyant manuellement des liens aux participants, par exemple par email. Ou vous pouvez utiliser une plateforme de recrutement de participants, telle que Prolific, Mechanical Turk, ou Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%


### Analyse des données

Une fois la collecte de données terminée, vous pouvez télécharger les données de JATOS et les convertir en format `.xlsx` ou `.csv` pour une analyse plus approfondie :

- %link:manual/osweb/data%


## Tutoriels

- %link:tutorials/intermediate-javascript%
- %link:wcst%