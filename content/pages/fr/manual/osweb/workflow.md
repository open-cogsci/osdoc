title: Exécuter des expériences en ligne avec OSWeb
hash: d164c11575309f8213f7683999953e7c4d0eb5adf6c728cb34d716947a673fbf
locale: fr
language: French

[TOC]

## Le workflow

Pour une introduction au workflow, voir également :

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Prépublication associée (non identique au manuscrit publié)](https://doi.org/10.31234/osf.io/wnryc)</small>

### Développer votre expérience

Tout d'abord, vous développez votre expérience comme vous le feriez normalement, en utilisant l'application de bureau OpenSesame. Toutes les fonctionnalités ne sont pas disponibles dans les expériences en ligne. Notamment, vous ne pouvez pas utiliser les éléments INLINE_SCRIPT Python, mais vous devez utiliser les éléments INLINE_JAVASCRIPT JavaScript à la place. Lors du développement de votre expérience, il est donc important de vérifier que votre expérience est compatible avec OSWeb.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%
- %link:manual/osweb/questionnaires%

### Télécharger votre expérience sur JATOS

Une fois que vous avez développé votre expérience, vous l'exportez d'OpenSesame et la téléchargez sur JATOS. JATOS est un serveur web qui gère les expériences : il vous permet de générer des liens que vous pouvez distribuer aux participants, et il stocke les données qui ont été collectées.

Il n'existe pas un seul serveur JATOS. En effet, de nombreuses institutions maintiennent leur propre serveur JATOS. De plus, <https://mindprobe.eu> est un serveur JATOS gratuit, parrainé par ESCoP et OpenSesame.

- %link:jatos%

### Collecter des données

Une fois que vous avez téléchargé votre expérience sur JATOS, vous pouvez commencer à collecter des données. Vous pouvez le faire en envoyant manuellement des liens aux participants, par exemple par e-mail. Ou vous pouvez utiliser une plateforme de recrutement de participants, telle que Prolific, Mechanical Turk, ou Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%

## Tutoriels

- %link:tutorials/intermediate-javascript%
- %link:wcst%
