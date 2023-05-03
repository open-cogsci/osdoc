title: Télécharger
hash: bb4581487a399790e873f0a07ab48b9c8592ed4061874de0b12d80d523c84678
locale: fr
language: French

<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('download-started').style.display = 'block'
	document.getElementById('download-started').scrollIntoView()
}
</script>

<div class="info-box" id="download-started" markdown="1" style="display:none;">

<h3>Votre téléchargement devrait commencer sous peu !</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://www.buymeacoffee.com/cogsci">
<span class="glyphicon glyphicon-heart" aria-hidden="true"></span>
Aidez-nous à rester concentrés et offrez-nous un café !
</a>

Le café nous permet de rester éveillés pour développer des logiciels gratuits et répondre à vos questions sur le forum d'assistance !

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>


## Aperçu

%--
toc:
 exclude: [Aperçu]
 mindepth: 2
 maxdepth: 3
--%


## Toutes les options de téléchargement

La dernière version $status$ est $version$ *$codename$*, sortie le $release-date$ ([notes de version](http://osdoc.cogsci.nl/$branch$/fr/notes/$notes$)).


### Windows

Le package Windows est basé sur Python 3.11 pour les systèmes 64 bits. Les packages d'installation et `.zip` sont identiques, à l'exception de l'installation. La plupart des gens téléchargent le package d'installation (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Installateur Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows sans installation requise (.zip)
</a>


### Mac OS

Il n'y a actuellement pas de packages de pré-version d'OpenSesame 4.0 pour Mac OS. Veuillez utiliser conda ou pip.
{: .page-notification}

[Cet article](https://support.apple.com/fr-fr/guide/mac-help/mh40616/mac) sur le site d'assistance Mac OS explique comment contourner les paramètres de sécurité de Mac OS qui empêchent par défaut le lancement d'OpenSesame.

Le package ci-dessous est conçu pour les processeurs Intel mais fonctionne également sur les processeurs ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 pour Intel x64</b> Package Mac OS (.dmg)
</a>

Pour installer OpenSesame avec [Homebrew](https://brew.sh/), exécutez la commande suivante dans un terminal :

```bash
brew install --cask opensesame
```


### Ubuntu

Les packages sont développés et testés sur Ubuntu 22.04 Jammy Jellyfish. Les packages sont uniquement disponibles pour les versions 22.04 et 22.10.

Si vous avez OpenSesame 3.X installé, désinstallez d'abord tous les packages. Ceci est nécessaire pour éviter les conflits de packages dus à un léger renommage de certains packages dans OpenSesame 4.0.

```bash
# Si nécessaire : désinstaller OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Ensuite, pour ajouter les dépôts nécessaires à vos sources de logiciels et installer OpenSesame (et Rapunzel), exécutez les commandes suivantes dans un terminal :

```bash
# Ajouter le dépôt pour les packages stables
sudo add-apt-repository ppa:smathot/cogscinl
# Ajouter le dépôt pour les packages de développement
sudo add-apt-repository ppa:smathot/milgram
# Installer les packages OpenSesame 4.X ainsi que les extensions utiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Certains packages couramment utilisés ne sont pas disponibles via le PPA. Vous pouvez les installer via `pip` :

```bash
# Installer les packages optionnels qui sont uniquement disponibles via pip
pip install opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy est préférablement installé via pip, car le package Ubuntu est actuellement défectueux. 

```bash
# Installer psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (multiplateforme)

Tous les packages peuvent être installés avec pip. Notez qu'OpenSesame s'appelle `opensesame-core` sur PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Une fois que vous avez installé tous les packages, vous pouvez simplement exécuter OpenSesame en (après avoir activé le bon environnement) exécutant :

```bash
opensesame
```

Ou pour l'éditeur de code Rapunzel :

```bash
rapunzel
```


### Anaconda (multiplateforme)

D'abord, créez un nouvel environnement Python pour OpenSesame (facultatif) :

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Ensuite, ajoutez les canaux pertinents (`cogsci`) et (`conda-forge`) et installez tous les packages pertinents. Assurez-vous que `pyqode.core` et `pyqode.python` sont >= 3.2 à partir du canal `cogsci`, et non pas les anciennes versions à partir du canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze
```

Certains packages ne sont pas disponibles via conda. Vous pouvez utiliser `pip install` pour ceux-ci.

```bash
pip install soundfile pygame psychopy psychopy-sounddevice http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

Une fois que vous avez installé tous les packages, vous pouvez simplement exécuter OpenSesame en (après avoir activé le bon environnement) exécutant :

```bash
opensesame
```

Ou pour l'éditeur de code Rapunzel :

```bash
rapunzel
```


### Versions antérieures

Les versions antérieures peuvent être téléchargées à partir des versions GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source d'OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Astuces


### Quelle version de Python utiliser ?

OpenSesame est actuellement construit et testé avec Python 3.11.0. D'autres versions de Python >= 3.7 fonctionnent, mais ne sont pas testées de manière approfondie. Python 2 n'est plus pris en charge. La dernière version qui incluait un package Python 2 était la 3.3.12, qui peut toujours être téléchargée à partir de l'[archive de versions](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour pendant le développement et les tests de votre expérience ; il est toujours préférable d'utiliser la dernière version d'OpenSesame.
- Ne mettez pas à jour pendant le déroulement d'une expérience ; c'est-à-dire, ne mettez pas à jour pendant que vous collectez des données.
- Exécutez une expérience avec la même version d'OpenSesame que celle que vous avez utilisée pour la développer et la tester.


### Mise à niveau manuelle des packages

OpenSesame est un environnement Python régulier, et vous pouvez mettre à jour les packages avec `pip` ou `conda` comme décrit ici :

- <https://rapunzel.cogsci.nl/manual/environment/>


### Conseils pour les administrateurs système

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec une version se terminant par 0, par exemple 3.1.0), elle est généralement suivie rapidement par une ou deux versions de maintenance (par exemple 3.1.1 et 3.1.2) qui résolvent les problèmes majeurs. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour souvent, il est préférable d'attendre la deuxième ou la troisième version de maintenance (par exemple 3.0.2, 3.1.3, etc.). Ainsi, vous minimisez le risque de déployer une version d'OpenSesame qui contient des bogues majeurs.
- L'installateur Windows vous permet d'installer silencieusement OpenSesame en utilisant le flag `/S`.