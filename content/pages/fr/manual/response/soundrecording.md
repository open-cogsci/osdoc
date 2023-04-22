title: Enregistrement sonore
hash: 541c85146b0c2948e62bcae0056f831ddb9cf3e2d2a3025254b3d54dac2e5f46
locale: fr
language: French

[TOC]

## Plugins Audio Low Latency

Les plugins Audio Low Latency, développés par Bob Rosbag, sont la méthode recommandée pour enregistrer des entrées sonores. L'objectif principal de cet ensemble de plugins est de lire et d'enregistrer des sons avec des latences minimales et prévisibles pour atteindre une haute précision et exactitude. Le package `PyAlsaAudio`, qui utilise le système audio Linux ALSA, a donné les meilleurs résultats au sein de Python. `PortAudio` et `sounddevice` sont multiplateformes et fonctionnent aussi bien sur Windows que sur Linux.

Les plugins ne sont pas installés par défaut, mais peuvent être installés via pip :

```bash
pip install opensesame-plugin-audio-low-latency
```

Voir aussi :

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>

## Plugins enregistreur de son

Les plugins enregistreur de son, développés par Daniel Schreij, ne sont plus en développement actif et ne sont donc plus recommandés. Vous trouverez plus d'informations sur cet ensemble de plugins dans la version précédente de cette page :

- <https://osdoc.cogsci.nl/3.2/manual/response/soundrecording/>