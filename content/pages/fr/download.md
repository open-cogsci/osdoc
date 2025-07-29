title: Télécharger
hash: 70d7d3aa0db9c3d49b6e9a94cd6d92a1dd50ec0dc94bc9bfc9e076703ab3dd3a
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

<h3>Votre téléchargement devrait commencer sous peu !</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Abonnez-vous à SigmundAI.eu
</a>

Mieux que ChatGPT pour les questions OpenSesame. Votre abonnement de 9 €/mois soutient OpenSesame.

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>


## Aperçu

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Toutes les options de téléchargement

La dernière version $status$ est $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Le package Windows est basé sur Python 3.13 pour les systèmes 64 bits. Les installateurs et les packages `.zip` sont identiques à l’exception de la procédure d’installation. La plupart des utilisateurs téléchargent le package installateur (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Installateur</b> Windows standard (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows standard</b> sans installation requise (.zip)
</a>


### Mac OS

Les packages Mac OS ne sont pas encore disponibles pour OpenSesame 4.1. Le lien ci-dessous pointe encore vers la version 4.0.
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Package Mac OS (.dmg)
</a>


### Linux / Ubuntu

Copiez-collez la ligne ci-dessous dans un terminal. Cela téléchargera et exécutera un script d’installation. Le script nécessite virtualenv, qui peut être installé sous Ubuntu avec `sudo apt install python3-venv`.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame est développé et testé sous Ubuntu 24.04. Le fonctionnement peut varier avec d’autres distributions Linux et versions d’Ubuntu.


### PyPi (multi-plateforme)

Tous les paquets peuvent être installés via pip. Notez que OpenSesame s’appelle `opensesame-core` sur PyPi.

Dépendances principales de OpenSesame :

```bash
# Dépendances principales d'OpenSesame
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy pour le backend psycho (par défaut). Selon votre système d’exploitation et la version de Python, installation de PsychoPy peut échouer. Dans ce cas, demandez de l’aide sur le forum de support ou utilisez un package/installeur préparé.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze pour l’oculométrie :

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment pour le backend xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Une fois tous les paquets installés, vous pouvez lancer OpenSesame en tapant :

```bash
opensesame
```

Ou pour Sigmund Analyst (éditeur de code) :

```bash
sigmund-analyst
```


### Anaconda (multi-plateforme)

D’abord, créez un nouvel environnement Python pour OpenSesame (optionnel) :

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Ensuite, suivez les instructions d’installation PyPi ci-dessus. Des paquets Anaconda spécifiques ne sont plus proposés.


### Versions précédentes

Les versions précédentes peuvent être téléchargées depuis les publications GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source d’OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement développé et testé avec Python 3.13. D'autres versions de Python >=3.10 fonctionnent mais ne sont pas testées de manière approfondie. Python 2 n'est plus pris en charge. La dernière version qui incluait un paquet Python 2 était la 3.3.12, qui peut encore être téléchargée depuis l'[archive des versions](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour pendant le développement et les tests de votre expérience ; il est toujours préférable d'utiliser la dernière version d'OpenSesame.
- Ne mettez pas à jour pendant que vous exécutez une expérience ; c'est-à-dire ne mettez pas à jour pendant la collecte des données.
- Exécutez une expérience avec la même version d'OpenSesame que celle utilisée pour le développement et les tests.


### Mise à jour manuelle des paquets

OpenSesame est un environnement Python classique, et vous pouvez exécuter des commandes `pip install` dans la console Jupyter.


### Conseils pour les administrateurs systèmes

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec un numéro se terminant par 0, par exemple 3.1.0), elle est généralement suivie rapidement d'une ou deux versions de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent des bugs importants. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour fréquemment, il est recommandé d'attendre la deuxième ou la troisième version de maintenance (par exemple 3.0.2, 3.1.3, etc.). De cette façon, vous minimisez le risque de déployer une version d'OpenSesame contenant des bugs majeurs.
- L'installeur Windows vous permet d'installer OpenSesame silencieusement grâce à l'option `/S`.