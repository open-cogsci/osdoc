title: Son
hash: abc659dc7f36f6c760c6f029cd4e89ea9f3cf46e33e009701bc55bafd4f59b01
locale: fr
language: French

La manière la plus courante de jouer un son consiste à utiliser l’item SAMPLER, pour la lecture de fichiers audio, ou l’item SYNTH, pour la lecture de bips simples, etc.

[TOC]

## Le sampler

Le SAMPLER lit un seul fichier son, généralement à partir du pool de fichiers.

Les fichiers son sont toujours lus à la fréquence d’échantillonnage utilisée par le backend sampler d’OpenSesame. Si votre échantillon semble accéléré (hauteur élevée) ou ralenti (hauteur basse), vous pouvez ajuster la fréquence d’échantillonnage de votre fichier son dans un éditeur audio, ou modifier la fréquence d’échantillonnage utilisée par le backend sampler d’OpenSesame (sous « Show backend settings and info » dans l’onglet General).

Le SAMPLER a quelques options :

- *Fichier son* indique le fichier à lire.
- *Volume* entre 0 (silence) et 1 (volume normal).
- *Pan* atténue le canal droit (valeurs négatives) ou gauche (valeurs positives). Pour un panoramique complet, saisissez « left » ou « right »,
- *Pitch* indique la vitesse de lecture, où 1 correspond à la vitesse d’origine.
- *Stop after* indique pendant combien de temps le fichier son doit être lu. Par exemple, une valeur de 100 ms signifie que la lecture sera arrêtée après 100 ms, quelle que soit la durée du fichier son. Une valeur de 0 ms signifie que le fichier son sera lu en entier.
- *Fade in* indique le temps de fondu d’entrée du fichier son. Par exemple, une valeur de 100 ms signifie que le fichier son commencera en silence et augmentera jusqu’à sa valeur maximale en 100 ms.
- *Duration* indique la durée de l’item sampler, avant que l’item suivant ne soit présenté. Cela ne doit pas nécessairement correspondre à la durée du fichier son. Par exemple, si la durée du sampler est définie sur 0 ms, OpenSesame passera directement à l’item qui suit le SAMPLER (p. ex. un sketchpad), *pendant que le fichier son continue à être lu en arrière-plan*. En plus d’une valeur numérique, vous pouvez définir duration sur :
	- « keypress » pour attendre un appui sur une touche
	- « mouseclick » pour attendre un clic de souris
	- « sound » pour attendre que le sampler ait terminé la lecture.

## Le synth

Le SYNTH est un synthétiseur sonore de base.

Vous pouvez spécifier un
certain nombre d’options :

- *Waveform* peut être défini sur sine, sawtooth, square ou white noise
- *Attack* est le temps nécessaire pour que le son atteigne son volume maximal (c.-à-d. fondu d’entrée).
- *Decay* est le temps nécessaire pour que le son s’éteigne (c.-à-d. fondu de sortie). Notez que le decay se produit dans la durée du son.
- *Volume* entre 0 et 100 %
- *Pan* atténue le canal droit (valeurs négatives) ou gauche (valeurs positives). Définir pan sur -20 ou 20 coupe complètement le canal droit ou gauche, respectivement.
- *Length* indique la durée du son (en millisecondes).
- *Duration* indique la durée de l’item SYNTH, avant que l’item suivant ne soit présenté. Cela ne doit pas nécessairement correspondre à la durée du son. Par exemple, la durée du SYNTH peut être définie sur 0 ms, afin de passer directement à l’item suivant (p. ex. un SKETCHPAD), tandis que le son continue à être lu en arrière-plan. En plus d’une valeur numérique, vous pouvez définir la durée sur « keypress », pour attendre un appui sur une touche du clavier, « mouseclick », pour attendre un clic de souris, ou « sound », pour attendre que le SYNTH ait terminé la lecture.

## Timing sonore dans sampler et synth

Jouer un son dans OpenSesame implique deux contrôles indépendants : l’un détermine combien de temps le son lui-même est lu, et l’autre détermine combien de temps l’expérience attend sur l’item actuel avant de passer au suivant. Comprendre la différence entre ces deux contrôles est essentiel pour un timing précis des stimuli.

### Deux contrôles indépendants

#### Durée du son

| Item | Paramètre | Description |
|---|---|---|
| **Sampler** | **Stop after** | Coupe le fichier audio avant sa fin après le nombre de ms indiqué. Définissez sur `0` pour lire le fichier jusqu’à sa fin naturelle. |
| **Synth** | **Length** | Définit directement la durée de la tonalité générée (en ms). Il n’y a pas de fin naturelle au-delà de la valeur spécifiée. |

#### Timing de l’item

SAMPLER et SYNTH partagent tous deux le paramètre *Duration*, qui contrôle combien de temps l’expérience reste sur l’item avant de passer au suivant. Il n’affecte pas directement le son lui-même.

| Valeur de Duration | Comportement |
|---|---|
| `0` | Passer immédiatement à la suite |
| *nombre* (ms) | Attendre le nombre de ms indiqué, puis passer à la suite |
| `sound` | Attendre que le son ait fini d’être joué |


### Règle générale

Que *longueur du son* désigne :
- *Stop after* pour SAMPLER, ou la longueur naturelle du fichier si *Stop after* vaut `0`
- *Length* pour SYNTH

Alors, ce qui suit s’applique :

| Condition | Résultat |
|---|---|
| *Duration* **<** longueur du son | L’item se termine avant le son, donc le son continue dans l’item suivant |
| *Duration* = `sound` | L’expérience attend jusqu’à ce que le son se termine |
| *Duration* **≥** longueur du son | L’item dure plus longtemps que le son, donc la lecture est terminée avant le début de l’item suivant |

### Remarques

- Pour SAMPLER, la durée de lecture réelle correspond à la longueur naturelle du fichier, sauf si *Stop after* est supérieur à `0`, auquel cas la lecture s’arrête après la durée indiquée.
- Pour SYNTH, la durée de lecture réelle est toujours égale à *Length*.
- Lorsque *Duration* = `sound`, l’expérience attend la durée de lecture réelle, en tenant compte de *Stop after* pour SAMPLER.

### Son qui continue dans l’item suivant

Un son peut continuer à être lu après la fin de l’item actuel si *Duration* est plus court que la durée de lecture réelle. Cela peut être intentionnel, par exemple lorsque vous voulez qu’un son tourne en arrière-plan pendant que l’item suivant est affiché. Mais cela peut aussi se produire involontairement si *Duration* est plus court que prévu, auquel cas le son peut déborder sur l’élément d’essai suivant.

## Lecture sonore en Python

Vous pouvez utiliser l’objet SAMPLER et la fonction SYNTH pour présenter des stimuli visuels en Python :

- %link:sampler%
- %link:manual/python/common%


## Plugins Audio Low Latency

L’objectif principal des plugins Audio Low Latency, développés par Bob Rosbag, est de lire et d’enregistrer l’audio avec des latences minimales et prévisibles afin d’atteindre une grande exactitude et précision. Le paquet `PyAlsaAudio`, qui utilise le système audio ALSA de Linux, a fourni les meilleurs résultats dans Python. `PortAudio` et `sounddevice` sont multiplateformes et fonctionnent aussi bien sous Windows que sous Linux.

Les plugins ne sont pas installés par défaut, mais peuvent être installés via pip :

```bash
pip install opensesame-plugin-audio-low-latency
```

Voir aussi :

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>