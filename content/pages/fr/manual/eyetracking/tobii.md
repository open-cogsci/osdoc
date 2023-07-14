title: Tobii
hash: a383da57d44200882bf0aa52f84f681e06fecc7982e5a785150b5372d2d75259
locale: fr
language: French

PyGaze offre un support *expérimental* pour les eye-trackers Tobii.

`tobii-research` est la bibliothèque Python pour le support Tobii. En juillet 2023, `tobii-research` nécessite Python 3.10, alors qu'OpenSesame utilise par défaut Python 3.11. Par conséquent, jusqu'à ce que `tobii-research` soit mis à jour pour Python 3.11, la façon la plus simple d'installer OpenSesame avec le support Tobii est de construire un environnement Python 3.10 via Anaconda.

Cela semble compliqué, mais ce ne l'est pas vraiment. Pour ce faire, commencez par lire la procédure générale pour installer OpenSesame via Anaconda, comme décrit sur la page Téléchargements :

- %link:download%

Ensuite, une fois que vous avez compris la procédure générale, commencez par créer un environnement Python 3.10, continuez avec les instructions de la page Téléchargements, puis installez `tobii-research` :

```
# Commencez par créer un environnement Python 3.10
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Suivez maintenant les instructions de la page de téléchargements
# ...
# Ensuite installez le support Tobii
pip install tobii-research
# Et maintenant lancez OpenSesame !
opensesame
```

Pour plus d'informations, voir :

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>