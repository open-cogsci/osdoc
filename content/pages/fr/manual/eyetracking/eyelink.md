title: Eyelink
hash: 795cf5b31d90084e4fe773cb7002ad511f76aa023cfef172927e5544fd44ed44
locale: fr
language: French

[TOC]

## A propos d'EyeLink

La série des eye-trackers EyeLink, produite par SR Research, est l'une des plus couramment utilisées dans la recherche en psychologie. SR Research fournit des liaisons Python pour l'EyeLink (appelé PyLink), qui sont utilisées par PyGaze. La licence de PyLink est incompatible avec la licence utilisée par OpenSesame. Pour cette raison, PyLink n'est pas inclus dans la distribution par défaut d'OpenSesame et doit être installé séparément.

## Windows

### Installation du kit de développement EyeLink

Le kit de développement EyeLink (parfois appelé logiciel d'affichage) fournit les bibliothèques nécessaires pour communiquer avec le PC EyeLink. Vous pouvez le trouver ici (inscription gratuite requise) :

- <https://www.sr-research.com/support/thread-13.html>

Si vous extrayez le fichier `.zip`, puis exécutez l'installateur `.exe`, l'affichage EyeLink sera installé dans l'un des dossiers suivants (selon votre version de Windows) :

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

Dans ce dossier, il y a un sous-dossier `libs`, que vous devez ajouter au chemin d'accès système (cela a peut-être été ajouté au chemin d'accès automatiquement, mais vérifiez pour vous en assurer). Vous pouvez le faire en ouvrant "Mon Ordinateur", en cliquant sur "Voir les informations système", en ouvrant l'onglet "Avancé", en cliquant sur "Variables d'environnement" et en ajoutant `;C:\Program Files\SR Research\EyeLink\libs` ou (selon votre système) `;C:\Program Files (x86)\SR Research\EyeLink\libs` à la variable Path (sous Variables système).

### Installation d'OpenSesame avec PyLink

PyLink est la bibliothèque Python pour le support EyeLink. En juillet 2023, PyLink prend en charge les versions Python jusqu'à 3.10, tandis qu'OpenSesame utilise par défaut Python 3.11. Par conséquent, jusqu'à ce que Pylink soit mis à jour pour Python 3.11, le moyen le plus simple d'installer OpenSesame avec Pylink est de créer un environnement Python 3.10 via Anaconda.

Cela peut sembler compliqué, mais ça ne l'est vraiment pas. Pour ce faire, commencez par lire la procédure générale pour installer OpenSesame via Anaconda comme décrit sur la page Téléchargements :

- %link:download%

Ensuite, une fois que vous comprenez la procédure générale, commencez par créer un environnement Python 3.10, continuez avec les instructions de la page Téléchargements, puis installez PyLink :

```
# Commencez par créer un environnement Python 3.10
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Suivez maintenant les instructions de la page de téléchargement
# ...
# Puis installez PyLink depuis l'entrepôt PyPi de SR Research
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
# Et maintenant lancez OpenSesame !
opensesame
```

Vous pouvez trouver plus d'informations sur PyLink sur le forum de SR Research (inscription gratuite requise) :

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

Le logiciel d'affichage EyeLink peut être installé directement à partir d'un dépôt. Ceci installe également PyLink et divers outils pratiques comme le convertisseur `edf2asc`.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Pour plus d'informations, veuillez visiter :

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Une fois que vous avez installé le logiciel d'affichage EyeLink et PyLink selon les instructions ci-dessus, vous pouvez utiliser l'EyeLink avec PyGaze ! Voir :

- %link:pygaze%