title: Télécharger
hash: 48b36f28d46849599cac6b02aa148d9b70d6476758c8b21e016736aed881ea59
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

<h3>Votre téléchargement devrait démarrer sous peu !</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Abonnez-vous à SigmundAI.eu
</a>

Mieux que ChatGPT pour les questions OpenSesame. Votre abonnement à 9€/mois soutient OpenSesame.

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>


## Vue d'ensemble

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Toutes les options de téléchargement

La dernière version $status$ est $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Le package Windows est basé sur Python 3.11 pour les systèmes 64 bits. Le programme d'installation et les packages `.zip` sont identiques, sauf pour l'installation. La plupart des gens téléchargent le package d'installation (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> installateur Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows sans installation requise (.zip)
</a>


### Mac OS

[Cet article](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) sur le site d'assistance Mac OS explique comment outrepasser les paramètres de sécurité de Mac OS qui empêcheront par défaut OpenSesame de se lancer. La première fois que vous démarrez OpenSesame, cela prendra beaucoup de temps avant que l'application ne se lance; les lancements suivants seront beaucoup plus rapides.

Le package ci-dessous est construit pour les processeurs Intel mais fonctionne également sur les processeurs ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 pour Intel x64</b> package Mac OS (.dmg)
</a>

Pour installer OpenSesame avec [Homebrew](https://brew.sh/), exécutez la commande suivante dans un terminal :

```bash
brew install --cask opensesame
```


### Ubuntu

Les packages sont développés et testés sur Ubuntu 24.04 Jammy Jellyfish. Votre expérience peut varier sur d'autres versions d'Ubuntu.

Si vous avez installé OpenSesame 3.X, désinstallez d'abord tous les packages. Ceci est nécessaire pour éviter les conflits de packages dus à un léger changement de nom de certains packages dans OpenSesame 4.0.

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
# Installer les packages OpenSesame 4.X plus les extensions utiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Certains packages couramment utilisés ne sont pas disponibles via le PPA. Vous pouvez les installer via `pip` :

```bash
# Installer des packages optionnels uniquement disponibles via pip
pip install --break-system-packages --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy est préférable à installer via pip, car le package Ubuntu est actuellement défectueux.

```bash
# D'abord, installez une version personnalisée de wxPython, requise pour PsychoPy
pip install --break-system-packages https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04/wxPython-4.2.2-cp312-cp312-linux_x86_64.whl
# Ensuite, installez psychopy et ignorez la condition requise pour Python <=3.11, car Ubuntu 24.04 utilise Python 3.12
pip install --break-system-packages --ignore-requires-python psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (multiplateforme)

Tous les packages peuvent être installés avec pip. Notez que OpenSesame est appelé `opensesame-core` sur PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Il est également possible que vous deviez installer PyQt5 et QtWebEngine, qui fournissent la boîte à outils GUI :

```bash
pip install pyqt5 pyqtwebengine
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

Tout d'abord, créez un nouvel environnement Python pour OpenSesame (optionnel) :

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Ensuite, ajoutez les canaux pertinents (`cogsci`) et (`conda-forge`) et installez tous les packages pertinents. Assurez-vous que `pyqode.core` et `pyqode.python` sont >= 3.2 du canal `cogsci`, et non les versions plus anciennes du canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Certains packages ne sont pas disponibles via conda. Vous pouvez utiliser `pip install` pour ceux-ci. (PsychoPy est connu pour échouer à l'installation sur certains systèmes, c'est pourquoi il est installé séparément ci-dessous.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
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

Les versions antérieures peuvent être téléchargées depuis les releases GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source de OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement construit et testé avec Python 3.11 D'autres versions de Python >=3.7 fonctionnent mais ne sont pas testées de manière extensive. Python 2 n'est plus supporté. La dernière version qui incluait un package Python 2 était 3.3.12, qui peut encore être téléchargée depuis l'[archive de release](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour pendant le développement et le test de votre expérience ; il est toujours préférable d'utiliser la dernière version de OpenSesame.
- Ne mettez pas à jour pendant l'exécution d'une expérience ; c'est-à-dire, ne mettez pas à jour pendant que vous collectez des données.
- Exécutez une expérience avec la même version de OpenSesame que vous avez utilisée pour le développement et le test.


### Mise à niveau manuelle des packages

OpenSesame est un environnement Python ordinaire, et vous pouvez mettre à niveau des packages avec `pip` ou `conda` comme décrit ici :

- <https://rapunzel.cogsci.nl/manual/environment/>


### Conseils pour les administrateurs système

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec une version se terminant par 0, par exemple 3.1.0), elle est généralement rapidement suivie par une ou deux versions de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent des bogues majeurs. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas souvent à jour, il est préférable d'attendre la deuxième ou la troisième version de maintenance (par exemple 3.0.2, 3.1.3, etc.). De cette façon, vous minimisez le risque de déployer une version d'OpenSesame contenant des bogues majeurs.
- Le programme d'installation pour Windows vous permet d'installer OpenSesame en mode silencieux en utilisant le flag `/S`.