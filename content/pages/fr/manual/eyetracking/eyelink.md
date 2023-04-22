title: Eyelink
hash: c9635275665d7dc2d7c42f6f480e386381284e31750ff4cd7cbaab5fb4522ee5
locale: fr
language: French

[TOC]

## À propos d'EyeLink

La série d'eye-trackers EyeLink, produite par SR Research, est l'une des plus couramment utilisées dans la recherche en psychologie. SR Research fournit des liaisons Python pour l'EyeLink (appelées PyLink), qui sont utilisées par PyGaze. La licence de PyLink est incompatible avec celle utilisée par OpenSesame, c'est pourquoi PyLink n'est pas inclus dans la distribution par défaut d'OpenSesame et doit être installé séparément.


## Forum SR Research

Vous devrez télécharger certains logiciels depuis le forum SR Research. Ce forum est un forum fermé, mais vous pouvez vous inscrire gratuitement.

- <https://www.sr-support.com/>

## Windows

### Installer le Kit de développement EyeLink

Le Kit de développement EyeLink (parfois appelé Display Software) fournit les bibliothèques nécessaires pour communiquer avec le PC EyeLink. Vous pouvez le trouver ici :

- <https://www.sr-support.com/thread-13.html>

Si vous extrayez le .zip, puis exécutez l'installateur .exe, le display EyeLink sera installé dans l'un des dossiers suivants (selon votre version de Windows) :

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

Dans ce dossier, il y a un sous-dossier `libs`, que vous devez ajouter au chemin système (cela a peut-être été ajouté automatiquement, mais vérifiez pour vous assurer). Vous pouvez le faire en ouvrant "Mon ordinateur", en cliquant sur "Afficher les informations système", en ouvrant l'onglet "Avancé", en cliquant sur "Variables d'environnement" et en ajoutant `;C:\Program Files\SR Research\EyeLink\libs` ou (selon votre système) `;C:\Program Files (x86)\SR Research\EyeLink\libs` à la variable Path (sous Variables système).

### Installer PyLink

PyLink est la bibliothèque Python pour le support EyeLink. PyLink est inclus dans les versions récentes du logiciel d'affichage EyeLink (décrit ci-dessus) et vous pouvez le trouver dans l'un des dossiers suivants (selon votre version de Windows) :

```
C:\Program Files\SR Research\EyeLink\SampleExperiments\Python
C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python
```

Sinon, vous pouvez télécharger Pylink ici :

- <https://www.sr-support.com/thread-13.html>

Pour installer PyLink dans OpenSesame, il suffit de copier le dossier avec le PyLink dans le dossier du programme OpenSesame ou dans le sous-dossier `Lib\site-packages`. Dans certains cas, le dossier `pylink` porte un nom tel que `pylink27-amd64`, auquel cas vous devez le renommer simplement `pylink`.

__Important :__ La version Python de PyLink doit correspondre à la version Python de votre installation OpenSesame. Dans la plupart des cas, cela signifie que vous avez besoin de PyLink pour Python 3.7.


## Ubuntu

Le logiciel d'affichage EyeLink peut être installé directement à partir d'un référentiel. Cela installe également PyLink et divers outils pratiques, tels que le convertisseur `edf2asc`.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Pour plus d'informations, veuillez visiter :

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Après avoir installé le logiciel d'affichage EyeLink et PyLink comme indiqué ci-dessus, vous pouvez utiliser EyeLink avec PyGaze ! Voir :

- %link:pygaze%