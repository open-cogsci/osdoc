title: Télécharger
hash: acf8377b52efc30d1c3f5f4f459cb00a79f09028ca118806c6cf122c7a3e9925
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

Mieux que ChatGPT pour les questions sur OpenSesame. Votre abonnement à 9&nbsp;€/mois soutient OpenSesame.

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

Le paquet Windows est basé sur Python 3.13 pour les systèmes 64 bits. Les paquets installeur et `.zip` sont identiques, sauf pour l'installation. La plupart des utilisateurs téléchargent le paquet installeur (bouton vert).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Installateur standard</b> Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Version standard</b> Windows sans installation requise (.zip)
</a>

OpenSesame est développé et testé sur Windows 11. Les résultats peuvent varier sur d’autres versions de Windows.


### Mac OS

Les paquets Mac OS ne sont pas encore disponibles pour OpenSesame 4.1. Le lien de téléchargement ci-dessous pointe encore vers la version 4.0.
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquet Mac OS (.dmg)
</a>


### Linux / Ubuntu

Copiez-collez la ligne ci-dessous dans un terminal. Ceci téléchargera et exécutera un script d'installation. Le script d'installation nécessite curl et virtualenv. Sur Ubuntu, ceux-ci peuvent être installés avec `sudo apt install curl python3-venv`.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame est développé et testé sur Ubuntu 24.04. Les résultats peuvent varier sur d’autres distributions Linux et versions d’Ubuntu.


## Options d'installation avancées


### PyPi (multiplateforme)

Tous les paquets peuvent être installés avec pip. Notez que OpenSesame s'appelle `opensesame-core` sur PyPi.

Dépendances principales d’OpenSesame :

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy pour le backend (par défaut) psycho. Selon votre système d'exploitation et la version de Python, PsychoPy peut ne pas s'installer correctement. Si cela se produit, demandez de l’aide sur le forum de support ou utilisez l’un des paquets/installateurs préfabriqués.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze pour le suivi oculaire :

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment pour le backend xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Une fois que tous les paquets sont installés, vous pouvez simplement lancer OpenSesame en exécutant&nbsp;:

```bash
opensesame
```

Ou pour Sigmund Analyst (éditeur de code)&nbsp;:

```bash
sigmund-analyst
```


### Anaconda (multiplateforme)

D'abord, créez un nouvel environnement Python pour OpenSesame (optionnel) :

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Ensuite, suivez les instructions d'installation PyPi ci-dessus. Des paquets Anaconda dédiés ne sont plus proposés.


### Versions précédentes

Les versions précédentes peuvent être téléchargées depuis les releases GitHub :

- <https://github.com/open-cogsci/OpenSesame/releases>


### Code source

Le code source d'OpenSesame est disponible sur [GitHub](https://github.com/open-cogsci/OpenSesame).


## Conseils


### Quelle version de Python utiliser ?

OpenSesame est actuellement développé et testé avec Python 3.13. D’autres versions de Python >=3.10 fonctionnent mais ne sont pas testées de manière approfondie. Python 2 n’est plus pris en charge. La dernière version incluant un package Python 2 était la 3.3.12, toujours disponible dans l’[archive des versions](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### Quand (ne pas) mettre à jour ?

- Mettez à jour pendant le développement et les tests de votre expérience ; il est toujours préférable d’utiliser la dernière version d’OpenSesame.
- Ne mettez pas à jour pendant que vous exécutez une expérience ; c’est-à-dire, ne mettez pas à jour pendant la collecte de données.
- Exécutez une expérience avec la même version d’OpenSesame que celle utilisée pour le développement et les tests.


### Mise à niveau manuelle des packages

OpenSesame est un environnement Python classique, et vous pouvez exécuter des commandes `pip install` dans la console Jupyter.


### Conseils pour les administrateurs système

- Lorsqu’une nouvelle version majeure d’OpenSesame est publiée (avec un numéro de version se terminant par 0, par exemple 3.1.0), elle est généralement suivie rapidement d’une ou deux versions de maintenance (par exemple 3.1.1 et 3.1.2) qui corrigent des bugs majeurs. Par conséquent, si vous installez OpenSesame sur des systèmes que vous ne mettez pas à jour fréquemment, il est préférable d’attendre la deuxième ou troisième version de maintenance (par exemple 3.0.2, 3.1.3, etc.). Ainsi, vous minimisez le risque de déployer une version d’OpenSesame contenant des bugs majeurs.
- L’installateur Windows permet d’installer OpenSesame silencieusement à l’aide du paramètre `/S`.