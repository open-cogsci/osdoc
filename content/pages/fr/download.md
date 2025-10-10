title: Télécharger
hash: 0057d1f73dae2a2590e1f0e03dfe7d984bdf6d67622188a9eb35e2cb08646b28
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

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; S’abonner à SigmundAI.eu
</a>

Votre copilote IA pour OpenSesame. Votre abonnement à 9 €/mois soutient OpenSesame.

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>


## Aperçu

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Options d'installation standard

La dernière version $status$ est $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Installateur</b> Windows standard (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows standard</b> sans installation requise (.zip)
</a>

La plupart des utilisateurs téléchargent le package d'installation `.exe`. Si vous n'avez pas de droits administrateur, ou si vous souhaitez exécuter plusieurs versions de OpenSesame côte à côte, téléchargez plutôt le package `.zip`.

Basé sur Python 3.13 pour systèmes 64 bits. Testé sur Windows 11.

Certains appareils externes, tels que les eye trackers [EyeLink](%url:eyelink%) et [Tobii](%url:tobii%), nécessitent une autre version de Python. Consultez les pages de documentation respectives pour plus d'informations.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquet Mac OS (.dmg)
</a>

Lorsque vous lancez OpenSesame pour la première fois, il est bloqué par le système d’exploitation car l’application ne provient pas d’un développeur identifié. Vous trouverez une option « Ouvrir quand même » dans Réglages > Confidentialité et sécurité. Cette option apparaît après le blocage de l’application.

Basé sur Python 3.13 pour systèmes intel 64 bits. Testé sur Mac OS X Sequoia.

Certains appareils externes, tels que les eye trackers [EyeLink](%url:eyelink%) et [Tobii](%url:tobii%), nécessitent une autre version de Python. Consultez les pages de documentation respectives pour plus d'informations.


### Linux / Ubuntu

Copiez-collez les lignes ci-dessous dans un terminal. Cela téléchargera et exécutera un script d'installation.

```bash
# Ces paquets doivent être installés sur Ubuntu 24.04.
# Des paquets équivalents doivent être installés sur les autres
# distributions Linux.
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# Téléchargez et lancez le script d'installation d'OpenSesame.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Testé sur Ubuntu 24.04 (Python 3.12).


## Options d'installation avancées


### PyPi (multiplateforme)

Tous les paquets peuvent être installés avec pip. À noter que OpenSesame s'appelle `opensesame-core` sur PyPi.

Dépendances principales d’OpenSesame :

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy pour l’arrière-plan (backend) psycho (par défaut). Selon votre système d’exploitation et la version de Python, PsychoPy peut ne pas s’installer correctement. En cas de problème, demandez de l’aide sur le forum de support ou utilisez un des installateurs ou paquets préfabriqués.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze pour le suivi oculaire :

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment pour l’arrière-plan xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Une fois tous les paquets installés, vous pouvez simplement lancer OpenSesame en exécutant :

```bash
opensesame
```

Ou pour Sigmund Analyst (éditeur de code) :

```bash
sigmund-analyst
```


### Anaconda (multi-plateforme)

D'abord, créez un nouvel environnement Python pour OpenSesame (optionnel)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Ensuite, suivez les instructions d'installation PyPi ci-dessus. Des paquets dédiés à Anaconda ne sont plus fournis.


### Anciennes versions d'OpenSesame et autres versions de Python

Des anciennes versions d'OpenSesame ainsi que des paquets construits avec différentes versions de Python (3.10, 3.11, et 3.12) sont disponibles sur les releases GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>



### Code source

Le code source d'OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement construit et testé avec Python 3.13. D'autres versions de Python >=3.10 fonctionnent mais ne sont pas testées de façon exhaustive. Python 2 n'est plus pris en charge. La dernière version incluant un paquet Python 2 était la 3.3.12, qui peut encore être téléchargée depuis [l'archive des releases](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour pendant la phase de développement et de test de votre expérience ; il est toujours préférable d’utiliser la dernière version d'OpenSesame.
- Ne mettez pas à jour pendant la collecte des données, c’est-à-dire lorsque vous êtes en train de faire passer l’expérience.
- Faites passer une expérience avec la même version d’OpenSesame que celle utilisée pour le développement et les tests.


### Mettre à jour manuellement les paquets

OpenSesame est un environnement Python classique, et vous pouvez exécuter les commandes `pip install` dans la console Jupyter.


### Conseils pour les administrateurs système

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec un numéro de version se terminant par 0, par ex. 3.1.0), elle est généralement suivie rapidement par une ou deux mises à jour correctives (par ex. 3.1.1 et 3.1.2) qui corrigent des bogues critiques. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour fréquemment, il est préférable d'attendre la deuxième ou troisième version corrective (par ex. 3.0.2, 3.1.3, etc.). Ainsi, vous minimisez le risque de déployer une version d'OpenSesame contenant des bogues majeurs.
- L'installateur Windows permet d'installer OpenSesame silencieusement en utilisant le paramètre `/S`.