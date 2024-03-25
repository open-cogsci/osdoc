title: Télécharger
hash: c3287b768243f4d57f2068746ebea3538a3441372f6a29ed902c5fe1429fa59e
locale: fr
language: French

```html
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

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Abonnez-vous à SigmundAI.eu
</a>

Mieux que ChatGPT pour les questions sur OpenSesame. Votre abonnement à 9 €/mois soutient OpenSesame.

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>

## Vue d'ensemble


## Toutes les options de téléchargement

La dernière version $status$ est $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).

### Windows

Le paquet Windows est basé sur Python 3.11 pour les systèmes 64 bits. Les paquets d'installation et `.zip` sont identiques, sauf pour l'installation. La plupart des gens téléchargent le paquet d'installation (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Installeur</b> Windows standard (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows standard</b> sans installation requise (.zip)
</a>


### Mac OS

[Cet article](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) sur le site de support Mac OS explique comment contourner les paramètres de sécurité de Mac OS qui, par défaut, empêcheront le lancement d'OpenSesame. La première fois que vous lancez OpenSesame, il faut beaucoup de temps avant que l'application démarre ; les lancements suivants sont beaucoup plus rapides.

Le paquet ci-dessous est construit pour les processeurs Intel mais fonctionne également sur les processeurs ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Paquet Mac OS</b> pour Python 3 pour Intel x64 (.dmg)
</a>

Pour installer OpenSesame avec [Homebrew](https://brew.sh/), exécutez la commande suivante dans un terminal :

```bash
brew install --cask opensesame
```

### Ubuntu

Les paquets sont développés et testés sur Ubuntu 22.04 Jammy Jellyfish. Les paquets sont disponibles uniquement pour les versions 22.04 et 22.10.

Si vous avez OpenSesame 3.X installé, désinstallez d'abord tous les paquets. Ceci est nécessaire pour éviter des conflits de paquets en raison du léger renommage de certains paquets dans OpenSesame 4.0.

```bash
# Si nécessaire : désinstaller OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Ensuite, pour ajouter les dépôts requis à vos sources de logiciels et installer OpenSesame (et Rapunzel), exécutez les commandes suivantes dans un terminal :

```bash
# Ajouter le dépôt pour les paquets stables
sudo add-apt-repository ppa:smathot/cogscinl
# Ajouter le dépôt pour les paquets de développement
sudo add-apt-repository ppa:smathot/milgram
# Installer les paquets OpenSesame 4.X ainsi que des extensions utiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Certains paquets couramment utilisés ne sont pas disponibles via le PPA. Vous pouvez les installer via `pip` :

```bash
# Installer des paquets optionnels disponibles uniquement via pip
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy est mieux installé via pip, car le paquet Ubuntu est actuellement cassé.

```bash
# Installer psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```

### PyPi (multiplateforme)

Tous les paquets peuvent être installés avec pip. Notez que OpenSesame est appelé `opensesame-core` sur PyPi.
```

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Une fois que vous avez installé tous les paquets, vous pouvez simplement exécuter OpenSesame en (après avoir activé l'environnement correct) exécutant :

```bash
opensesame
```

Ou pour l'éditeur de code Rapunzel :

```bash
rapunzel
```


### Anaconda (multiplateforme)

Premièrement, créez un nouvel environnement Python pour OpenSesame (optionnel) :

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Ensuite, ajoutez les canaux pertinents (`cogsci`) et (`conda-forge`) et installez tous les paquets pertinents. Assurez-vous que `pyqode.core` et `pyqode.python` sont >= 3.2 depuis le canal `cogsci`, et non les anciennes versions du canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Certains paquets ne sont pas disponibles via conda. Vous pouvez utiliser `pip install` pour ceux-ci. (Il est connu que l'installation de PsychoPy échoue sur certains systèmes, c'est pourquoi elle est installée séparément ci-dessous.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Une fois que vous avez installé tous les paquets, vous pouvez simplement exécuter OpenSesame en (après avoir activé l'environnement correct) exécutant :

```bash
opensesame
```

Ou pour l'éditeur de code Rapunzel :

```bash
rapunzel
```


### Anciennes versions

Les anciennes versions peuvent être téléchargées depuis les releases GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source d'OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement construit et testé avec Python 3.11 D'autres versions de Python >=3.7 fonctionnent mais ne sont pas testées de manière approfondie. Python 2 n'est plus pris en charge. La dernière version qui comprenait un paquet Python 2 était la 3.3.12, qui peut toujours être téléchargée depuis les [archives des releases](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour lors du développement et du test de votre expérience ; il est toujours préférable d'utiliser la dernière version d'OpenSesame.
- Ne mettez pas à jour pendant l'exécution d'une expérience ; c'est-à-dire, ne mettez pas à jour pendant que vous collectez des données.
- Exécutez une expérience avec la même version d'OpenSesame que celle que vous avez utilisée pour le développement et les tests.


### Mise à niveau manuelle des paquets

OpenSesame est un environnement Python régulier, et vous pouvez mettre à niveau les paquets avec `pip` ou `conda` comme décrit ici :

- <https://rapunzel.cogsci.nl/manual/environment/>


### Conseils pour les administrateurs système

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec une version se terminant par 0, par exemple 3.1.0), elle est généralement rapidement suivie par une ou deux releases de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent les bugs majeurs. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour souvent, il est préférable d'attendre jusqu'à la deuxième ou troisième release de maintenance (par exemple 3.0.2, 3.1.3, etc.). Ainsi, vous minimisez le risque de déployer une version d'OpenSesame contenant des bugs majeurs.
- L'installateur Windows vous permet d'installer OpenSesame en silence en utilisant le drapeau `/S`.