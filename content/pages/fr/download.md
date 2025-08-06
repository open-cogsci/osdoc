title: Télécharger
hash: 4c609d80d00e5704f1e59d0daf4820641810168b01ec87f556a20c226969d520
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

<h3>Votre téléchargement devrait commencer sous peu&nbsp;!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Abonnez-vous à SigmundAI.eu
</a>

Mieux que ChatGPT pour les questions OpenSesame. Votre abonnement à 9&nbsp;€/mois soutient OpenSesame.

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
	<b>Installateur</b> Windows Standard (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows sans installation requise (.zip)
</a>

La plupart des utilisateurs téléchargent le package installateur `.exe`. Si vous n’avez pas de droits d'administrateur ou si vous devez exécuter plusieurs versions d’OpenSesame côte à côte, téléchargez plutôt le package `.zip`.

Basé sur Python 3.13 pour les systèmes 64 bits. Testé sur Windows 11.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Package Mac OS (.dmg)
</a>

Lorsque vous lancez OpenSesame pour la première fois, il est bloqué par le système d’exploitation car l’application ne provient pas d'un développeur de confiance. Vous trouverez une option «&nbsp;Ouvrir quand même&nbsp;» dans Réglages&nbsp;> Confidentialité et sécurité. Cette option s'affiche après le blocage de l'application.

Basé sur Python 3.13 pour les systèmes intel 64 bits. Testé sur Mac OS X Sequoia.


### Linux / Ubuntu

Copiez et collez la ligne ci-dessous dans un terminal. Cela téléchargera et exécutera un script d'installation. Le script d'installation requiert curl et virtualenv. Sur Ubuntu, ceux-ci peuvent être installés avec `sudo apt install curl python3-venv`.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Testé sur Ubuntu 24.04 (Python 3.12).


## Options d'installation avancées


### PyPi (multiplateforme)

Tous les paquets peuvent être installés via pip. Notez qu’OpenSesame se nomme `opensesame-core` sur PyPi.

Dépendances principales d’OpenSesame&nbsp;:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy pour le backend psycho (par défaut). Selon votre système d’exploitation et votre version de Python, PsychoPy peut ne pas s’installer correctement. Si c’est le cas, demandez de l’aide sur le forum de support ou utilisez l’un des paquets/installateurs préassemblés.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze pour l’eye-tracking&nbsp;:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment pour le backend xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Une fois tous les paquets installés, vous pouvez simplement lancer OpenSesame en exécutant&nbsp;:

```bash
opensesame
```

Ou pour Sigmund Analyst (éditeur de code)&nbsp;:

```bash
sigmund-analyst
```


### Anaconda (multiplateforme)

D'abord, créez un nouvel environnement Python pour OpenSesame (optionnel)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Ensuite, suivez les instructions d'installation PyPi ci-dessus. Les paquets Anaconda dédiés ne sont plus fournis.


### Versions précédentes

Les versions précédentes peuvent être téléchargées depuis les releases GitHub&nbsp;:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source d’OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement construit et testé avec Python 3.13. D’autres versions de Python >=3.10 fonctionnent mais ne sont pas testées de manière approfondie. Python 2 n’est plus pris en charge. La dernière version incluant un paquet Python 2 était la 3.3.12, qui peut encore être téléchargée depuis [l’archive des versions](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour lors du développement et des tests de votre expérience ; il est toujours préférable d’utiliser la dernière version d’OpenSesame.
- Ne mettez pas à jour pendant l’exécution d’une expérience ; c’est-à-dire, ne faites pas de mise à jour pendant la collecte de données.
- Exécutez une expérience avec la même version d’OpenSesame que celle utilisée pour le développement et les tests.


### Mise à niveau manuelle des paquets

OpenSesame est un environnement Python standard, et vous pouvez exécuter des commandes `pip install` dans la console Jupyter.


### Conseils pour les administrateurs système

- Lorsqu’une nouvelle version majeure d’OpenSesame est publiée (avec un numéro de version se terminant par 0, par exemple 3.1.0), elle est généralement rapidement suivie d’une ou deux versions de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent des bogues majeurs. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour fréquemment, il est préférable d’attendre la deuxième ou la troisième version de maintenance (par exemple 3.0.2, 3.1.3, etc.). Ainsi, vous minimisez le risque de déployer une version d’OpenSesame contenant des bogues majeurs.
- L’installateur Windows vous permet d’installer OpenSesame silencieusement en utilisant l’option `/S`.