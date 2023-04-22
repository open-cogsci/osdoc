title: Format de fichier (.osexp)
hash: 310dc6efe4055dac4dd14eda896adcf8c98e4a4f1950bb613ed0c1fd461c5ebc
locale: fr
language: French

[TOC]

## Le format .osexp

Les expériences OpenSesame sont enregistrées au format `.osexp`. Ce qu'est un fichier `.osexp` dépend de la présence ou non de fichiers inclus dans l'expérience, c'est-à-dire si la réserve de fichiers est vide ou non.

## Si la réserve de fichiers est vide

Si la réserve de fichiers est vide, l'expérience est enregistrée sous la forme d'un fichier texte brut. Ce fichier est encodé en utf-8 et utilise des fins de ligne au style Unix. Vous pouvez modifier et afficher ce fichier dans la plupart des éditeurs de texte.

La syntaxe OpenSesame-script est décrite ici :

- %link:opensesame-script%

## Si la réserve de fichiers n'est pas vide

Si des fichiers se trouvent dans la réserve de fichiers, l'expérience est enregistrée en tant que fichier `.tar.gz`, qui est un format de fichier similaire à `.zip`. Dans ce fichier, vous trouverez ce qui suit :

- `script.opensesame` est le script expérimental, dans le même format que décrit ci-dessus
- `pool/` est un dossier qui contient tous les fichiers de la réserve de fichiers. Tous les caractères non-ascii dans les noms de fichiers sont remplacés par des chaînes `U+XXXX`.

## Qu'est-il arrivé aux formats .opensesame et .opensesame.tar.gz ?

Vous pouvez toujours ouvrir les formats `.opensesame` et `.opensesame.tar.gz`, qui étaient utilisés pour OpenSesame <= 2.9.X. Cependant, vous ne pouvez plus enregistrer des expériences dans ce format.