title: JATOS
hash: b885bbb21d5bc5d8ffa13b6adf7ce306d93ad1253011bddf7529f22af3b5eb59
locale: fr
language: French

[TOC]


## Introduction à JATOS

[JATOS](https://www.jatos.org/) est un système de gestion d'expériences en ligne. Il vous permet de créer des comptes pour les expérimentateurs, de télécharger des expériences et de générer des liens que vous pouvez distribuer aux participants. OpenSesame s'intègre étroitement à JATOS.

Pour accéder à un serveur JATOS, vous avez trois options principales:

- Demandez un compte gratuit sur [MindProbe](https://mindprobe.eu/), un serveur JATOS public parrainé par ESCoP et OpenSesame.
- Utilisez un serveur JATOS fourni par votre institution.
- Téléchargez JATOS et installez-le sur votre propre serveur.

## Lier OpenSesame à JATOS/MindProbe

OpenSesame nécessite un jeton API pour accéder à votre compte sur un serveur JATOS tel que MindProbe. Suivez ces étapes pour générer un jeton API :

1. **Connectez-vous à JATOS.**
2. **Ouvrez votre profil utilisateur** en cliquant sur votre nom situé dans le coin supérieur droit de la page.
3. **Créez un jeton API** en cliquant sur 'jetons d'API' pour voir tous vos jetons actuels, puis cliquez sur 'Nouveau jeton'.
4. **Attribuez un nom à votre jeton**. Ce nom sert de descripteur indiquant son utilisation prévue, comme par exemple 'Intégration OpenSesame'.
5. **Définissez une date d'expiration pour votre jeton**. Par défaut, les jetons expirent après 30 jours, nécessitant de générer un nouveau jeton chaque mois. Vous pouvez sélectionner 'Pas d'expiration' pour plus de commodité, mais sachez que c'est moins sûr. Si quelqu'un accède à un jeton non expiré, il peut l'utiliser indéfiniment, ou jusqu'à ce que vous révoquiez le jeton.

%--
figure:
 id: FigAPIToken
 source: api-token.png
 caption: Les jetons API peuvent être générés dans votre profil utilisateur JATOS.
--%

Note : un jeton API commence toujours par `jap_`, suivi d'une série de caractères et de chiffres. Gardez votre jeton en sécurité!

Une fois que vous avez votre jeton API, ouvrez le panneau de contrôle OSWeb et JATOS dans OpenSesame. Saisissez votre jeton API dans le champ correspondant et ajustez l'URL du serveur JATOS, si nécessaire.

%--
figure:
 id: FigJATOSControlPanel
 source: jatos-control-panel.png
 caption: Spécifiez le serveur JATOS et votre jeton API dans le panneau de contrôle OSWeb et JATOS.
--%


## Publier des expériences sur, et télécharger à partir de, JATOS/MindProbe

Après avoir connecté avec succès OpenSesame à JATOS, comme expliqué ci-dessus, vous pouvez publier votre expérience sur JATOS. Pour ce faire, sélectionnez l'option 'Publier sur JATOS/MindProbe' dans le menu Fichier. Lors de la première publication, votre expérience se verra attribuer un identifiant unique (UUID) qui la lie à une étude sur JATOS.

Vous pouvez ensuite visiter votre serveur JATOS et constater que l'expérience récemment publiée a été ajoutée à votre liste d'études.

A partir de ce moment, chaque fois que vous publiez l'expérience, l'étude JATOS existante sera mise à jour avec la nouvelle version. Si vous souhaitez publier l'expérience en tant qu'étude totalement nouvelle sur JATOS, vous devrez réinitialiser l'UUID JATOS via le panneau de contrôle OSWeb et JATOS.

Pour télécharger une expérience à partir de JATOS, sélectionnez l'option 'Ouvrir à partir de JATOS/MindProbe' dans le menu Fichier. Veuillez noter que cette fonction n'est applicable que si l'étude JATOS correspondante est compatible avec OSWeb 2.