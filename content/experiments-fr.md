---
layout: osdoc
title: Expériences
group: General
permalink: /experiences/
---

Cette page contient une liste d'expériences rémunérées pour lesquels nous cherchons des participants.

*[View this page in english](/experiments)*

Index
-----

- [Instructions générales](#instructions)
	- [Conditions de participation](#requirements)
	- [Télécharger et exécuter une expérience](#download)
	- [Enregistrer et envoyer les fichier des données](#data)
	- [Rémunération](#payment)
- [Expériences disponibles](#experiments)
- [Résolution des problèmes](#troubleshooting)

Instructions générales {#instructions}
----------------------

### Conditions de participation {#requirements}

- Les participants doivent être des étudiants d'Aix-Marseille Université.
- Les instructions ci-dessous sont pour Windows XP / 7.
- Si vous utilisez Linux, merci d'envoyer un e-mail à <experiments@cogsci.nl> pour obtenir les instructions.
- Mac OS(X) n'est pas supporté.

### Télécharger et exécuter une expérience {#download}

- D'abord, envoyez un e-mail à <experiments@cogsci.nl> pour indiquer que vous voulez participer à une expérience. Merci d'indiquer le code d'expérience (par ex. *0043A1*) et votre numéro d'étudiant. Vous recevrez une confirmation.
- Téléchargez l'expérience (un fichier `.zip`) au moyen du lien à [Expériences disponibles](#experiments).
- Extraire le fichier `.zip` dans un dossier de votre choix.
- Ouvrez le dossier de l'expérience (par ex. `experiment-0001A1`).
- Pour démarrer une session, cliquez sur `RUN_SESSION.BAT`.
- Lisez attentivement les instructions à l'écran.
- Si l'expérience se compose de plusieurs sessions, il faut que vous exécutiez `RUN_SESSION.BAT` pour chaque session. Par exemple, si le nombre de sessions est 3, vous devrez exécuter `RUN_SESSION.BAT` trois fois.

### Enregistrer et envoyer les fichiers de données {#data}

- Lorsque vous avez terminé une session, vos données seront enregistrées sous `my_data.csv`.
- Renommez `my_data.csv` pour inclure vos nom et numéro de session (par ex. `sebastiaan_01.csv`).
- Lorsque vous avez terminé toutes les sessions, envoyez les fichiers de données à <experiments@cogsci.nl>. Si une expérience se compose de plusieurs sessions, envoyez tous les fichiers de données (`sebastiaan_01.csv`, `sebastiaan_02.csv`, etc.).

## Rémunération {#payment}

Il y a deux possibilités pour la rémunération: par virement bancaire ou sur rendez-vous. Vous recevrez la rémunération seulement si toutes les données ont été reçues avec succès, avant la date limite de l'expérience.

### Par virement bancaire (pas de rendez-vous nécessaire)

Remplissez les formulaires de consentement et de paiement et envoyez un scan de ces formulaires ou une photo de haute qualité par e-mail a <experiments@cogsci.nl> (si les formulaires ne sont pas inclus avec l'expérience, merci de demander par e-mail). Merci de inclure votre RIB. Le paiement sera viré lorsque les deux formulaires ont été bien reçus.

### Sur rendez-vous

Quand vous envoyez les données, indiquez que vous souhaitez prendre rendez-vous (dans le campus St. Charles d'Aix-Marseille Université).

Expériences disponibles {#experiments}
-----------------------

{% include experiments %}

Résolution des problèmes {#troubleshooting}
------------------------

Si vous rencontrez des problèmes, merci de contrôler [les instructions](#instructions) ci-dessus. Si vous ne réussissez pas à les résoudre, merci d'envoyer un e-mail à <experiments@cogsci.nl> avec une description précise des problèmes, y compris les messages d'erreur.

- *Problème connu :*  Il est possible que vous rencontriez l'erreur suivante `Error: 'ascii' codec can't decode byte [...] in position [...]`. Cette erreur se produit quand l'expérience est placé dans un dossier avec des caractères spéciaux ('é', 'ça', etc.). Par example, le dossier `c:\Documents and Settings\Nom avec caract*è*res speciaux\Mes documents\experiment` produit un error. Pour résoudre ce problème, placez l'expérience dans un dossier sans caractères spéciaux. Par exemple `c:\experiment`.
