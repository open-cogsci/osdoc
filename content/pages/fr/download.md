title: Télécharger
hash: 02c996f07585f459badd7fcb648bad241d5c8415f54a7ceb58cd0b3f4dc465a5
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

Mieux que ChatGPT pour les questions OpenSesame. Votre abonnement à 9 €/mois soutient OpenSesame.

Cliquez <a id="click-here">ici</a> si votre téléchargement ne démarre pas.
</div>


## Aperçu

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Options d’installation standard

La dernière version $status$ est $version$ *$codename$* ([notes de version](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Le package Windows est basé sur Python 3.13 pour les systèmes 64 bits. Les installeurs et les packages `.zip` sont identiques, à l’exception du mode d’installation. La plupart des gens téléchargent le package installeur (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> installeur Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows, aucune installation requise (.zip)
</a>

OpenSesame est développé et testé sur Windows 11. Les résultats peuvent varier avec d'autres versions de Windows.


### Mac OS

Lorsque vous ouvrez OpenSesame pour la première fois, il sera bloqué par le système car l’application ne provient pas d’un développeur approuvé. Une option «&nbsp;Ouvrir quand même&nbsp;» apparaît dans Réglages &gt; Confidentialité &amp; Sécurité. Cette option apparaît après le blocage de l’application.


<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Package Mac OS (.dmg)
</a>

OpenSesame est développé et testé sur Mac OS X Sequoia. Les résultats peuvent varier avec d'autres versions de Mac OS X.



### Linux / Ubuntu

Copiez-collez la ligne ci-dessous dans un terminal. Cela téléchargera et exécutera un script d’installation. Ce script nécessite curl et virtualenv. Sous Ubuntu, ceux-ci peuvent être installés avec `sudo apt install curl python3-venv`.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame est développé et testé sur Ubuntu 24.04. Les résultats peuvent varier avec d'autres distributions Linux ou versions d'Ubuntu.


## Options d’installation avancées


### PyPi (multiplateforme)

Tous les packages peuvent être installés via pip. Notez qu’OpenSesame s’appelle `opensesame-core` sur PyPi.

Dépendances principales d’OpenSesame :

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy pour le backend psycho (par défaut). Selon votre système d’exploitation et votre version de Python, PsychoPy peut ne pas s’installer correctement. Si besoin, demandez de l’aide sur le forum de support ou utilisez un des packages/installateurs préfabriqués.

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

Une fois tous les packages installés, vous pouvez simplement lancer OpenSesame avec&nbsp;:

```bash
opensesame
```

Ou pour Sigmund Analyst (éditeur de code) :

```bash
sigmund-analyst
```


### Anaconda (multiplateforme)

Commencez par créer un nouvel environnement Python pour OpenSesame (facultatif)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Ensuite, suivez les instructions d'installation PyPi ci-dessus. Des paquets Anaconda dédiés ne sont plus fournis.

### Versions précédentes

Les versions précédentes peuvent être téléchargées depuis les releases GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>

### Code source

Le code source d'OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).

## Conseils

### Quelle version de Python utiliser ?

OpenSesame est actuellement développé et testé avec Python 3.13. D'autres versions de Python >=3.10 fonctionnent mais n'ont pas été testées de manière exhaustive. Python 2 n'est plus supporté. La dernière version incluant un paquet Python 2 était la 3.3.12, qui peut encore être téléchargée depuis [l’archive des releases](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).

### Quand (ne pas) mettre à jour ?

- Effectuez les mises à jour pendant le développement et les tests de votre expérience ; il est toujours préférable d'utiliser la dernière version d'OpenSesame.
- Ne mettez pas à jour durant la passation d'une expérience ; c'est-à-dire, ne mettez pas à jour pendant la collecte des données.
- Faites tourner une expérience avec la même version d'OpenSesame que celle utilisée pour le développement et les tests.

### Mise à niveau manuelle des paquets

OpenSesame est un environnement Python classique et vous pouvez exécuter des commandes `pip install` dans la console Jupyter.

### Conseils pour les administrateurs système

- Lorsqu'une nouvelle version majeure d'OpenSesame est publiée (avec un numéro de version se terminant par 0, par exemple 3.1.0), elle est généralement suivie rapidement d'une ou deux versions de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent des bugs majeurs. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas souvent à jour, il est préférable d'attendre la deuxième ou troisième version de maintenance (par exemple 3.0.2, 3.1.3, etc.). De cette manière, vous minimisez le risque de déployer une version d'OpenSesame avec des bugs majeurs.
- L’installateur Windows permet d’installer OpenSesame silencieusement en utilisant le paramètre `/S`.