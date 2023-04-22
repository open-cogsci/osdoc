title: Boîte SR
hash: 4071d0970094db9727787578d613e899ded69a490b5c9c3e902816836096ee9a
locale: fr
language: French

[TOC]

## À propos du plugin srbox

La boîte de réponse série (SR) est une boîte à boutons, spécifiquement conçue pour la collecte de réponses dans les expériences psychologiques. La version originale, développée par Psychology Software Tools, dispose de 5 boutons, 5 lumières et est connectée au PC via le port série. Il existe également des dispositifs compatibles avec la boîte SR Box fabriqués par d'autres fabricants, qui peuvent différer par le nombre de boutons et de lumières et utilisent souvent une connexion USB qui émule un port série.

Le plugin SRBOX pour OpenSesame vous permet d'utiliser la boîte SR Box ou un dispositif compatible dans vos expériences OpenSesame.

## Capture d'écran

%--
figure:
  source: srbox.png
  id: FigSrbox
  caption: Le plugin srbox dans OpenSesame.
--%

## Définition du nom du périphérique

Par défaut, le plugin essaie de détecter automatiquement votre SR Box. Si cela fonctionne, vous n'avez pas besoin de le changer. Si votre expérience se bloque, OpenSesame a choisi le mauvais port série et vous devez entrer manuellement le nom du périphérique. Sous Windows, le périphérique est probablement appelé quelque chose comme

```text
COM4
```

Sous Linux, le périphérique est probablement appelé quelque chose comme

```text
/dev/tty0
```

## Exigences

Une boîte de boutons SR Box ou compatible. Toutes les boîtes de boutons ne sont pas compatibles, voir :

- %link:buttonbox%

## Utiliser la SR Box depuis du code Python en ligne

L'objet `srbox` n'existe *pas* lorsque le plug-in est en mode factice.

%-- include: include/api/srbox.md --%