title: EyeLink
hash: 37419c41f2ba79dc8903d36fe35edc800de2791247978b58d7a4c3ee07121ff1
locale: fr
language: French

[TOC]

## À propos d’EyeLink

Les oculomètres EyeLink, produits par SR Research, comptent parmi les oculomètres les plus couramment utilisés dans la recherche en psychologie. SR Research fournit des liaisons Python permettant de communiquer avec l’EyeLink (appelées PyLink), qui sont utilisées par PyGaze et par leur propre plugin EyeLink.


## Installation de PyLink

La bibliothèque Python destinée à l’intégration d’EyeLink est disponible sur PyPI sous le nom `sr-research-pylink`. Elle prend entièrement en charge Windows, macOS et Linux pour les versions de Python allant de 2.7 à 3.14 ; elle peut donc être installée dans les installations récentes d’OpenSesame.

Vous pouvez l’installer directement depuis le terminal :

```
pip install sr-research-pylink
```

**Important :** N’essayez *pas* d’installer `pylink` en exécutant `pip install pylink`. Cela installerait un package complètement différent et sans rapport !

Vous trouverez davantage d’informations sur `sr-research-pylink` sur le forum SR Research (inscription gratuite requise) :

- <https://www.sr-research.com/support/> 
- <https://www.sr-research.com/support/thread-48.html>
	
## PyGaze

Après avoir installé PyLink en suivant les instructions ci-dessus, vous pouvez utiliser l’EyeLink avec PyGaze ! Voir :

- %link:pygaze%

## Plugin EyeLink de SR Research

SR Research fournit également son propre ensemble de plugins EyeLink pour OpenSesame. Ce plugin offre des fonctionnalités supplémentaires d’intégration d’EyeLink qui ne sont pas disponibles via PyGaze, telles qu’un gaze trigger, le transfert EDF lorsqu’une tâche est interrompue, et une prise en charge complète lors du transfert de la caméra pour les modèles EyeLink récents. Pour installer leur plugin, exécutez :

```
pip install opensesame-plugin-eyelink
```

Pour plus d’informations, veuillez consulter :

- <https://www.sr-research.com/support/thread-52.html>

## Facultatif : EyeLink Developers Kit

Bien qu’il ne soit plus nécessaire pour exécuter PyLink dans OpenSesame, l’EyeLink Developers Kit (parfois appelé EyeLink Display Software) fournit des outils supplémentaires utiles, tels que le convertisseur `edf2asc`, de la documentation et des fichiers d’installation hors ligne de `sr-research-pylink` (.whl).

Si vous avez besoin de ces utilitaires, vous trouverez les programmes d’installation pour Windows et macOS, ainsi que les dépôts Ubuntu, sur le site de support de SR Research :

- <https://www.sr-research.com/support/forum-9.html>