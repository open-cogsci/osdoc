title: Eyelink
hash: 446281a464dd40eabe3f55f650572a8894359598a77c99f0c8eb20fe31cad1fc
locale: fr
language: French

[TOC]

## À propos de EyeLink

La série de trackers oculaires EyeLink, produite par SR Research, sont parmi les trackers oculaires les plus couramment utilisés en recherche psychologique. SR Research fournit des liaisons Python pour EyeLink (appelées PyLink), qui sont utilisées par PyGaze. La licence de PyLink est incompatible avec la licence utilisée par OpenSesame. Pour cette raison, PyLink n’est pas inclus dans la distribution par défaut d’OpenSesame et doit être installé séparément.


## Windows

### Installer le EyeLink Developers Kit

Le EyeLink Developers Kit (parfois appelé Display Software) fournit les bibliothèques nécessaires pour communiquer avec le PC EyeLink. Vous pouvez le trouver ici (inscription gratuite requise) :

- <https://www.sr-research.com/support/thread-13.html>

Si vous extrayez le fichier `.zip`, puis exécutez le programme d’installation `.exe`, l’affichage EyeLink sera installé dans l’un des dossiers suivants (selon votre version de Windows) :

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

Dans ce dossier, il y a un sous-dossier `libs`, que vous devez ajouter au Path du système (cela a peut-être déjà été ajouté automatiquement, mais vérifiez pour être sûr). Pour cela, ouvrez "Poste de travail", cliquez sur "Afficher les informations système", ouvrez l’onglet "Avancé", cliquez sur "Variables d’environnement" et ajoutez `;C:\Program Files\SR Research\EyeLink\libs` ou (selon votre système) `;C:\Program Files (x86)\SR Research\EyeLink\libs` à la variable Path (sous Variables système).


### Installer OpenSesame avec PyLink

`pylink` est la bibliothèque Python pour la compatibilité EyeLink. Actuellement, `pylink` ne prend en charge que Python 3.12 et les versions antérieures, tandis que les packages standards d’OpenSesame sont construits avec Python 3.13. Par conséquent, vous devez utiliser le package OpenSesame avec Python 3.12 (ou antérieur) disponible sur [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases).

Ensuite, `pylink` peut être installé à partir du dépôt PyPi de SR Research via `pip install` :

```
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
```

Important : ne tentez *pas* d’installer `pylink` en exécutant `pip install pylink`. Cela installerait un tout autre package !

Vous pouvez trouver plus d’informations sur `pylink` sur le forum SR Research (inscription gratuite requise) :

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

Le logiciel d’affichage EyeLink peut être installé directement depuis un dépôt. Cela installe également PyLink et divers outils utiles, tels que le convertisseur `edf2asc`.

```bash
sudo add-apt-repository 'deb [arch=amd64] https://apt.sr-research.com SRResearch main'
sudo apt-key adv --fetch-keys https://apt.sr-research.com/SRResearch_key
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Pour plus d’informations, veuillez consulter :

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Après avoir installé le logiciel d’affichage EyeLink et PyLink selon les instructions ci-dessus, vous pouvez utiliser EyeLink avec PyGaze ! Voir :

- %link:pygaze%


## Plugin eyelink SR Research

SR Research propose également leurs propres plug-ins EyeLink pour OpenSesame. Ceux-ci sont assez similaires (et à l’origine basés sur) les plugins PyGaze, mais offrent quelques fonctionnalités qui ne sont pas disponibles via PyGaze. Pour installer ces plug-ins, exécutez :

```
pip install opensesame-plugin-eyelink
```

Pour plus d’informations, veuillez consulter :

- <https://www.sr-research.com/support/thread-52.html>
