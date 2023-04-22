title: Son
hash: 2a7ee6fde847af9407b8719c0f7ddecc8711cf1e09f8a2c6db320088aa8d67f1
locale: fr
language: French

La méthode la plus courante pour jouer un son est d'utiliser l'élément SAMPLER, pour la lecture de fichiers audio, ou l'élément SYNTH, pour la lecture de sons simples comme des bips, etc.

[TOC]

## Le sampler

Le SAMPLER lit un seul fichier audio, généralement à partir du bassin de fichiers.

Les fichiers audio sont toujours lus à la fréquence d'échantillonnage utilisée par le backend OpenSesame sampler. Si votre échantillon semble accéléré (hauteur élevée) ou ralenti (hauteur basse), vous pouvez ajuster la fréquence d'échantillonnage de votre fichier audio dans un éditeur audio, ou modifier la fréquence d'échantillonnage utilisée par le backend OpenSesame sampler (dans "Afficher les paramètres et informations du backend" dans l'onglet Général).

Le SAMPLER a quelques options :

- *Sound file* indique le fichier à lire.
- *Volume* entre 0 (silence) et 1 (volume normal).
- *Pan* baisse le canal droit (valeurs négatives) ou gauche (valeurs positives). Pour une panoramique complète, entrez "left" ou "right".
- *Pitch* indique la vitesse de lecture, 1 correspondant à la vitesse d'origine.
- *Stop after* indique combien de temps le fichier audio doit être lu. Par exemple, une valeur de 100 ms signifie que la lecture s'arrête après 100 ms, quelle que soit la durée du fichier audio. Une valeur de 0 ms signifie que le fichier audio sera lu en entier.
- *Fade in* indique le temps de montée du volume pour le fichier audio. Par exemple, une valeur de 100 ms signifie que le fichier audio commencera en silence et atteindra la valeur maximale en 100 ms.
- *Duration* indique la durée de l'élément SAMPLER avant la présentation de l'élément suivant. Cela n'a pas besoin de correspondre à la longueur du fichier audio. Par exemple, si la durée du SAMPLER est définie à 0 ms, OpenSesame passera directement à l'élément suivant le SAMPLER (par exemple, un sketchpad), *tandis que le fichier audio continuera à être lu en arrière-plan*. En plus d'une valeur numérique, vous pouvez définir la durée à :
	- 'keypress' pour attendre un appui sur une touche
	- 'mouseclick' pour attendre un clic de souris
	- 'sound' pour attendre que le sampler ait fini de lire.

## Le synth

Le SYNTH est un synthétiseur de son basique.

Vous pouvez spécifier un certain nombre d'options :

- *Waveform* peut être réglé sur sinus, dent de scie, carré ou bruit blanc
- *Attack* est le temps nécessaire pour que le son atteigne le volume maximum (c'est-à-dire montée du volume).
- *Decay* est le temps nécessaire pour que le son s'éteigne (c'est-à-dire baisse du volume). Notez que la diminution se produit à l'intérieur de la longueur du son.
- *Volume* entre 0 et 100%
- *Pan* baisse le canal droit (valeurs négatives) ou gauche (valeurs positives). Régler la panoramique à -20 ou 20 coupe complètement le canal droit ou gauche, respectivement.
- *Length* indique la longueur du son (en millisecondes).
- *Duration* indique la durée de l'élément SYNTH avant la présentation de l'élément suivant. Cela n'a pas besoin de correspondre à la longueur du son. Par exemple, la durée du SYNTH peut être réglée sur 0 ms, afin de passer directement à l'élément suivant (par exemple, un SKETCHPAD), pendant que le son continue à être lu en arrière-plan. En plus d'une valeur numérique, vous pouvez définir la durée sur 'keypress', pour attendre un appui sur une touche de clavier, 'mouseclick', pour attendre un clic de souris, ou 'sound', pour attendre que le SYNTH ait fini de jouer.

## Lecture de sons en Python

Vous pouvez utiliser l'objet SAMPLER et la fonction SYNTH pour présenter des stimuli visuels en Python :

- %link:sampler%
- %link:manual/python/common%

## Plugins Audio Low Latency

L'objectif principal des plugins Audio Low Latency, développés par Bob Rosbag, est de jouer et d'enregistrer des sons avec des latences minimales et prévisibles pour obtenir une grande précision et une grande exactitude. Le paquet `PyAlsaAudio` qui utilise le système audio Linux ALSA a donné les meilleurs résultats dans Python. `PortAudio` et `sounddevice` sont multiplateformes et fonctionnent sur Windows et Linux.

Les plugins ne sont pas installés par défaut, mais peuvent être installés via pip :

```bash
pip install opensesame-plugin-audio-low-latency
```

Voir aussi :

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>