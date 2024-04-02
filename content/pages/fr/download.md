title: Télécharger
hash: fd00279bec39b52c5cf277e973c6f314758b571714fbc3b1fb8730ac172aa061
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

Mieux que ChatGPT pour les questions sur OpenSesame. Votre abonnement de €9/mois soutient OpenSesame.

Essayez 1 mois gratuitement avec le code promo NHVB3IXD. &#128293;

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>


## Vue d'ensemble

## Toutes les options de téléchargement

La dernière version $status$ est la $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Le package Windows est basé sur Python 3.11 pour les systèmes 64 bits. Les packages installateur et `.zip` sont identiques, à part pour l'installation. La plupart des gens téléchargent le package installateur (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Installateur Windows</b> standard (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows sans installation</b> requis (.zip)
</a>


### Mac OS

[Cet article](https://support.apple.com/fr-fr/guide/mac-help/mh40616/mac) sur le site d'assistance Mac OS explique comment contourner les paramètres de sécurité de Mac OS qui, par défaut, empêcheront OpenSesame de se lancer. La première fois que vous démarrerez OpenSesame, cela prendra beaucoup de temps avant que l'application se lance ; les lancements suivants seront beaucoup plus rapides.

Le package ci-dessous est construit pour les processeurs Intel mais fonctionne également sur les processeurs ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Package Mac OS pour Python 3 pour Intel x64</b> (.dmg)
</a>

Pour installer OpenSesame avec [Homebrew](https://brew.sh/), exécutez la commande suivante dans un terminal :

```bash
brew install --cask opensesame
```


### Ubuntu

Les packages sont développés et testés sur Ubuntu 22.04 Jammy Jellyfish. Les packages ne sont disponibles que pour les versions 22.04 et 22.10.

Si vous avez OpenSesame 3.X installé, désinstallez d'abord tous les packages. Cela est nécessaire pour éviter les conflits de package en raison du léger renommage de certains packages dans OpenSesame 4.0.

```bash
# Si nécessaire : désinstaller OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Ensuite, pour ajouter les dépôts requis à vos sources logicielles et installer OpenSesame (et Rapunzel), exécutez les commandes suivantes dans un terminal :

```bash
# Ajouter le dépôt pour les packages stables
sudo add-apt-repository ppa:smathot/cogscinl
# Ajouter le dépôt pour les packages de développement
sudo add-apt-repository ppa:smathot/milgram
# Installer les packages d'OpenSesame 4.X plus des extensions utiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Certains packages couramment utilisés ne sont pas disponibles via le PPA. Vous pouvez les installer via `pip` :

```bash
# Installer les packages optionnels disponibles uniquement via pip
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy est mieux installé par pip, car le package Ubuntu est actuellement cassé.

```bash
# Installer psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (multiplateforme)

Tous les packages peuvent être installés avec pip. Notez qu'OpenSesame est appelé `opensesame-core` sur PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Une fois que vous avez installé tous les packages, vous pouvez simplement exécuter OpenSesame en (après avoir activé l'environnement correct) lançant :

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

Ensuite, ajoutez les canaux pertinents (`cogsci`) et (`conda-forge`) et installez tous les packages nécessaires. Assurez-vous que `pyqode.core` et `pyqode.python` soient >= 3.2 depuis le canal `cogsci`, et non les versions plus anciennes du canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Certains packages ne sont pas disponibles via conda. Vous pouvez utiliser `pip install` pour ces derniers. (Il est connu que PsychoPy échoue parfois à s'installer sur certains systèmes, c'est pourquoi il est installé séparément ci-dessous.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Une fois que vous avez installé tous les packages, vous pouvez simplement exécuter OpenSesame en (après avoir activé l'environnement correct) lançant :

```bash
opensesame
```

Ou pour l'éditeur de code Rapunzel :

```bash
rapunzel
```


### Versions antérieures

Les versions antérieures peuvent être téléchargées depuis les releases GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source d'OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement construit et testé avec Python 3.11. D'autres versions de Python >= 3.7 fonctionnent mais ne sont pas testées de manière approfondie. Python 2 n'est plus pris en charge. La dernière version qui incluait un package Python 2 était la 3.3.12, qui peut encore être téléchargée depuis les [archives des releases](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour lors du développement et du test de votre expérience ; il est toujours préférable d'utiliser la dernière version d'OpenSesame.
- Ne mettez pas à jour lors du déroulement d'une expérience ; c'est-à-dire, ne mettez pas à jour pendant que vous collectez des données.
- Menez une expérience avec la même version d'OpenSesame que celle utilisée pour le développement et les tests.


### Mise à jour manuelle des packages

OpenSesame est un environnement Python régulier, et vous pouvez mettre à jour les packages avec `pip` ou `conda` comme décrit ici :

- <https://rapunzel.cogsci.nl/manual/environment/>


### Conseils pour les administrateurs système

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec une version se terminant par un 0, par exemple 3.1.0), elle est généralement rapidement suivie par une ou deux releases de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent les bugs majeurs. Donc, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour souvent, il est préférable d'attendre jusqu'à la deuxième ou troisième release de maintenance (par exemple 3.0.2, 3.1.3, etc.). De cette façon, vous minimisez le risque de déployer une version d'OpenSesame qui contient des bugs majeurs.
- L'installateur Windows vous permet d'installer OpenSesame silencieusement en utilisant le flag `/S`.