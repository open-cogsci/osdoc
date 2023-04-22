title: Exécution à partir du code source
reviewed: false
hash: 97b9ccebc7a5b8f621d7724e6cf0a8a423800dd3861b85aaa93ff679ac90ded5
locale: fr
language: French

Cette page décrit comment configurer un environnement Python complet sur votre ordinateur, afin de pouvoir exécuter OpenSesame directement à partir du code source.

[TOC]

## Télécharger le code source

Téléchargez le code source de la dernière version stable depuis GitHub:

- <https://github.com/smathot/OpenSesame/releases>

Vous pouvez également télécharger un instantané de développement du code. Pour obtenir un instantané raisonnablement stable, téléchargez à partir de la branche `master`. Pour obtenir le dernier instantané, le meilleur et éventuellement très instable, téléchargez à partir de la branche correspondant à la version majeure d'OpenSesane (par exemple, `heisenberg` pour 2.9, `ising` pour 3.0).

- <https://github.com/smathot/OpenSesame/>

## Dépendances

### Thème d'icônes

Si vous exécutez OpenSesame directement à partir du code source, le thème d'icônes n'est pas inclus. OpenSesame utilise deux thèmes d'icônes: [MokaSesame](https://github.com/smathot/moka-icon-theme/tree/MokaSesame), un fork de Moka, et [Faba](https://github.com/snwh/faba-icon-theme).

Il est possible de compiler ces thèmes d'icônes vous-même, mais vous pouvez également télécharger des thèmes précompilés à partir d'ici:

- http://forum.cogsci.nl/uploads/editor/we/p1y3i4qm70ch.zip

Placez les dossiers `Faba` et `MokaSesame` sous `opensesame_resources/theme/default/`.

### Requis

Les packages suivants sont requis pour exécuter une version minimale de l'interface graphique OpenSesame, avec prise en charge uniquement pour le backend [legacy], sans prise en charge du son et sans support de plugin.

- [Python](http://www.python.org) est le langage de programmation dans lequel OpenSesame est créé. Les versions suivantes de Python sont prises en charge:
	- Python 2.7 (par défaut)
    - OpenSesame >= 3.0.0 prend en charge Python >= 3.4
- [PyGame](http://www.pygame.org) est une bibliothèque utilisée pour les graphiques et le son.
- [qtpy](https://github.com/goanpeca/qtpy) est la couche d'abstraction sur PyQt4 ou PyQt5.
	- [PyQt4](http://www.riverbankcomputing.com/software/pyqt/download) est la boîte à outils graphique utilisée pour l'interface utilisateur; ou
	- [PyQt5](http://www.riverbankcomputing.com/software/pyqt/download) est la boîte à outils graphique utilisée pour l'interface utilisateur.
- [QScintilla2](http://www.riverbankcomputing.com/software/pyqt/download) est un composant éditeur de texte de base. Dans certains cas, il est livré avec `PyQt4`.
- [QProgEdit](https://github.com/smathot/QProgEdit) est un composant éditeur de texte avancé basé sur `QScintilla2`.
	- OpenSesame >= 3.1.0 nécessite QProgEdit >= 4.0.0
- [PyYAML](http://pyyaml.org/) est une bibliothèque utilisée pour charger les fichiers `yaml`.
- [WebColors](https://pypi.python.org/pypi/webcolors) est une bibliothèque utilisée pour interpréter les descriptions de couleur.
- [python-datamatrix](https://github.com/smathot/python-datamatrix) est utilisé par l'élément de boucle.
- [python-qdatamatrix](https://github.com/smathot/python-qdatamatrix) est utilisé par l'élément de boucle.
- [python-pseudorandom](https://github.com/smathot/python-pseudorandom) est utilisé par l'élément de boucle.
- [QNotifications](https://github.com/dschreij/QNotifications) est utilisé par l'extension de notifications.

### Optionnel

Les packages suivants ne sont pas requis, mais certaines fonctionnalités seront manquantes s'ils ne sont pas installés.

- [Expyriment](http://www.expyriment.org/) est nécessaire pour le backend [xpyriment].
    - OpenSesame >= 3.0.0 nécessite Expyriment >= 0.8.0.
- [NumPy](http://www.numpy.org/) est une bibliothèque mathématique avancée utilisée pour diverses choses, telles que la prise en charge du son.
- [PIL](http://www.pythonware.com/products/pil/) est une bibliothèque d'imagerie utilisée pour diverses choses.
    - Vous pouvez également utiliser `pillow`, un fork activement maintenu de l'original, et `PIL` qui n'est plus maintenu.
- [PsychoPy](http://www.psychopy.org/) est nécessaire pour le backend [psycho].
- [pyflakes](https://pypi.python.org/pypi/pyflakes) est nécessaire pour la validation automatique de vos scripts Python.
- [Pyglet](http://www.pyglet.org/) est requis par PsychoPy.
- [PyOpenGL](http://pyopengl.sourceforge.net/) est requis par PsychoPy et Expyriment.
- [pySerial](http://pyserial.sourceforge.net/) est nécessaire pour la communication par port série.
- [python-markdown](https://pypi.python.org/pypi/Markdown) est requis pour visualiser les fichiers d'aide intégrés au programme.
- [IPython](http://ipython.org/), lorsqu'il est disponible, est utilisé pour la fenêtre de débogage.
- [python-fileinspector](https://github.com/dschreij/fileinspector) est utilisé pour générer des icônes spécifiques au type de fichier.
- [shapely](https://pypi.org/project/Shapely/) est utilisé pour vérifier les limites des éléments `Canvas`.

### Extra

Les packages suivants ne sont pas utilisés directement par OpenSesame, mais peuvent être utiles pour développer vos expériences et sont inclus dans la distribution officielle d'OpenSesame pour Windows.

- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) est une bibliothèque alternative pour l'enregistrement et la lecture de sons.
- [Matplotlib](http://matplotlib.org/) est une bibliothèque pour tracer des graphiques.
- [Scipy](http://www.scipy.org/) est un ensemble de routines scientifiques diverses.
- [pyCairo](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo) est une bibliothèque pour les graphiques vectoriels.
- [pyParallel](http://sourceforge.net/projects/pyserial/files/pyparallel) permet la communication via le port parallèle.
- [OpenCV](http://opencv.org/) (liaisons Python) est une bibliothèque étendue de vision par ordinateur.
- [PyGaze](http://www.pygaze.org/) est une bibliothèque Python pour l'eye tracking.
    - OpenSesame >= 3.0.0 nécessite PyGaze >= 0.6.0.

## Instructions pour Mac OS

Il y a trois façons de préparer l'environnement logiciel pour exécuter OpenSesame à partir du code source sur Mac OS X. Vous pouvez soit télécharger et installer tous les packages requis manuellement, soit composer l'environnement source requis à l'aide des gestionnaires de packages basés sur les dépôts MacPorts ou Homebrew. La méthode la plus facile et préférée aujourd'hui pour faire fonctionner OpenSesame est d'utiliser Homebrew. Ce gestionnaire de packages fonctionne très rapidement, gère très bien les exigences de dépendance et est très bien entretenu. L'autre gestionnaire de paquets, MacPorts, est essentiellement un grand dépôt contenant le code source de programmes qui ont été portés de Linux à Mac OS X (qui sont très liés car Mac OS X est également un système basé sur Unix, comme vous le savez peut-être). Comparé à Homebrew, Macports prend un temps incroyablement long pour compiler toutes les dépendances. De plus, même si Macports fonctionnait très bien auparavant, il connaît aujourd'hui de nombreux problèmes de dépendance. L'inconvénient de Homebrew est qu'il est "moins complet" que Macports et vous devez installer manuellement de nombreux packages Python (en utilisant easy_install ou pip).

### Télécharger Xcode

Si vous souhaitez installer avec Homebrew ou Macports, la première chose que vous devez faire est d'installer Xcode, la boîte à outils développeur d'Apple. Vous pouvez obtenir la dernière version d'Xcode gratuitement depuis l'App Store ou depuis leur site web (vous devez toutefois vous connecter avec un compte Apple).

Site web : <https://developer.apple.com/xcode/>

Utiliser l'App Store est préférable, car il maintiendra votre version de X Code automatiquement à jour. Vous devez également installer manuellement les outils de ligne de commande pour X Code (et le faire à chaque fois qu'il est mis à jour).

### Installation avec Homebrew

Homebrew est un moyen plus récent et plus simple de construire un arbre source sur votre Mac. Il présente de nombreux avantages par rapport à macports, tels que la vitesse, et semble aujourd'hui avoir moins de problèmes pour compiler et mettre à jour des packages que macports.
Vous pouvez installer homebrew comme indiqué sur <http://brew.sh/>. Ensuite, exécutez la commande suivante pour commencer:

    brew update
    brew doctor

Résolvez les problèmes que la commande 'doctor' soulève. Cela devrait être facile et généralement les solutions (sous forme de commandes simples) sont déjà données avec l'énoncé du problème.

Ensuite, ajoutez d'autres référentiels requis en utilisant la commande "tap" de homebrew:

	brew tap homebrew/python
	brew tap homebrew/headonly
	brew tap homebrew/science

Il est maintenant temps de commencer à installer l'environnement python de homebrew. Ce n'est pas vraiment nécessaire d'installer un autre environnement Python à côté du python de votre système, mais la version Homebrew est généralement plus récente et mieux maintenue, il est donc recommandé de le faire.

    brew install python

Après avoir installé python, vous devez en faire le python 'par défaut' utilisé par OS X. Cela signifie que l'interpréteur python de homebrew sera utilisé lorsque vous exécutez la commande 'python' dans un terminal au lieu du python système par défaut. Pour ce faire, tapez la commande

    echo export PATH="/usr/local/bin:$PATH" >> ~/.bash_profile

Cela placera la référence au dossier dans lequel se trouve tout votre matériel homebrew (/usr/local/bin) devant le reste de la variable PATH. Désormais, chaque fois que vous exécutez une commande dans votre terminal, OS X cherchera d'abord dans ce dossier le script ou le programme à exécuter et s'il ne le trouve pas, il continuera à chercher dans les autres dossiers de la variable PATH. Fermez et rouvrez votre terminal ou entrez la commande

	source ~/.bash_profile

pour réexécuter les commandes écrites dans votre .bash_profile. Si vous exécutez ensuite la commande

    wich python

il devrait afficher quelque chose comme '/usr/local/bin/python'. S'il affiche toujours '/usr/bin/python', OS X utilise toujours le python système par défaut, ce qui n'est pas ce que vous voulez. Vous pouvez maintenant continuer à installer le reste des packages requis en exécutant

	brew install qt pyqt qscintilla2 freetype portaudio numpy scipy portmidi hg pillow

Pour pygame, il est préférable d'installer d'abord les bibliothèques SDL et smpeg (ces versions sont toutes meilleures que celles fournies avec OS X, qui semblent manquer certaines fonctionnalités importantes):

	brew install --HEAD smpeg
	brew install sdl sdl_image sdl_mixer sdl_ttf pygame

Installez les packages python nécessaires

    pip install pyopengl pyflakes markdown python-bidi pyserial billiard

Installez QProgEdit (à partir d'OpenSesame 2.8)

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	python setup.py install
	cd ..
	rm -R QProgEdit

Installez expyriment (à partir d'OpenSesame 0.27)

    git clone https://github.com/expyriment/expyriment.git
	cd expyriment
	python setup.py install
	cd ..
	rm -R expyriment

Installez psychopy et sa dépendance pyglet. Pour que psychopy fonctionne, vous devez (actuellement) installer les dernières versions des dépôts pyglet et psychopy

Tout d'abord, installez pyglet:

    hg clone https://code.google.com/p/pyglet/
	cd pyglet
	python setup.py install
	cd ..
	rm -R pyglet

Ensuite, psychopy. Installez-le et effectuez un nettoyage avec:

	git clone https://github.com/psychopy/psychopy.git
	cd psychopy
	python setup.py install
	cd ..
	rm -R psychopy

Lors de l'installation, vous pouvez recevoir une erreur avec le message "Unknown locale UTF8". Vous pouvez facilement résoudre ce problème en plaçant la ligne "LC_ALL=en_US.UTF8" dans votre ~/.bash_profile puis rouvrez votre terminal.

Vous devriez maintenant être en mesure d'exécuter OpenSesame, mais vous remarquerez qu'il vous manque certaines icônes! Vous devez télécharger le thème d'icônes Faenza à partir de <http://tiheum.deviantart.com/art/Faenza-Icons-173323228> et le placer dans resources/theme/default/. De plus, il y a une particularité selon laquelle le multiprocessing ne fonctionne pas lorsque le fichier principal n'est pas présent en tant que fichier .py, ce qui est le cas pour opensesame. Pour activer la prise en charge du multiprocessing, vous devez renommer le fichier opensesame en opensesame.py, puis si vous exécutez une expérience maintenant, vous verrez que opensesame.pyc aura été créé. Dès que ce fichier est présent, Python utilisera le .pyc lors de la création de nouveaux processus et vous pourrez maintenant renommer à nouveau opensesame.py en opensesame. C'est une solution étrange pour que le multiprocessing fonctionne, mais pour l'instant c'est la seule que nous connaissons.

Les packages suivants sont optionnels, mais il peut être utile de les installer néanmoins :

	brew install matplotlib opencv
	pip install pycairo pyparallel scikit-image

### Installation avec MacPorts

Une autre manière d'installer les paquets nécessaires sur Mac OS est en utilisant MacPorts, un grand dépôt de paquets. Cela prend beaucoup de temps (et par là, je veux dire plusieurs heures!) pour installer tous les paquets nécessaires à l'exécution d'OpenSesame, car MacPorts fonctionne en compilant à partir des sources. Mais pour être positif, c'est un processus assez simple.

#### Télécharger MacPorts

Vous pouvez télécharger macports depuis son site web sur lequel vous pouvez également trouver la documentation nécessaire et un catalogue de tous les paquets disponibles.

Site web : <http://www.macports.org/install.php>

Vous pouvez ajouter +universal à votre /opt/local/etc/macports/variants.conf pour demander à MacPorts de construire tous les ports que vous installez avec cette variante (donc les versions 32 bits et 64 bits empaquetées dans le même module), sans avoir à vous souvenir de le taper à chaque commande d'installation. Cependant, certains ports n'ont pas encore été testés en tant que binaires universels et peuvent ne pas se construire correctement.

#### Installer les dépendances

Essentiellement, vous pouvez maintenant installer tous les paquets requis en exécutant une seule commande dans un terminal :

	sudo port install py27-game py27-pyqt4 py27-scintilla py27-serial py27-pil py27-opengl py27-pyaudio opencv +python27 py27-pip

Cela prend énormément de temps et, dans mon cas, a échoué plusieurs fois avec une erreur de somme de contrôle. Vous pouvez simplement récupérer de telles erreurs en exécutant la commande suivante :

	sudo port clean --all [paquet_qui_a_causé_l'erreur]

Ensuite, vous répétez la première commande et MacPorts devrait être de nouveau en route.

Installez les autres paquets python nécessaires en utilisant pip

    sudo pip install pyflakes markdown python-bidi pyserial billiard

Installer QProgEdit (l'éditeur de code par défaut d'OpenSesame 2.8 et suivants)

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	sudo python setup.py install
	cd ..
	rm -R QProgEdit

#### Backend Expyriment et Psychopy

En plus du backend legacy, qui est basé sur pygame, OpenSesame vous offre également la possibilité d'utiliser expyriment ou psychopy. Contrairement au backend legacy, ces deux backend sont accélérés matériellement (OpenGL) et devraient avoir une meilleure précision de temporisation.

Installez expyriment (à partir d'OpenSesame 0.27)

    git clone https://github.com/expyriment/expyriment.git
    cd expyriment
    sudo python setup.py install
    cd ..
    rm -R expyriment

Installer psychopy et sa dépendance pyglet :

Installez d'abord pyglet :

    hg clone https://code.google.com/p/pyglet/
    cd pyglet
    sudo python setup.py install
    cd ..
    rm -R pyglet

Ensuite, installez psychopy :

    git clone https://github.com/psychopy/psychopy.git
    cd psychopy
    python setup.py install
    cd ..
    rm -R psychopy

PsychoPy refuse de fonctionner sans la bibliothèque wxPython installée (ce qui est étrange, car OpenSesame n'utilise aucun des composants wx GUI de psychopy), installez donc wxPython en dernier avec :

	sudo port install py27-wxpython-dev

#### Faites de MacPorts Python le Python par défaut

Mac OS est livré avec une version personnalisée de Python, mais pour notre objectif (et de nombreux objectifs), vous avez besoin de la version officielle de Python. Cela a déjà été installé par MacPorts, mais vous devez toujours en faire la version par défaut. Vous pouvez le faire avec la commande suivante :

	sudo port select --set python python27

### Installation des packages manuellement

Si vous souhaitez installer toutes les dépendances d'Opensesame vous-même, vous devez télécharger et installer les distributions des packages suivants :

#### Installer Python

L'installation de python qui vient avec OS X est généralement d'une version plus ancienne. Il est donc préférable d'installer la dernière version à partir de python.org :

Site web : <http://www.python.org/>

Téléchargement direct : http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg

Une autre option est d'installer la [Enthought Python Distribution (EPD)][EPD_Download] à la place. Cette distribution inclut Python et plusieurs modules dont OpenSesame dépend ([voir][EPD_Packages] la liste complète).

#### Installer PyGame

Site web : <http://www.pygame.org/>

Téléchargement direct (Snow Leopard) : <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.6-macosx10.6.mpkg.zip><br/>
Téléchargement direct ((Mountain) Lion) : <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.7-macosx10.7.mpkg.zip>

#### Installer PyQt4

Il n'y a pas de distribution officielle (de Riverbank) disponible de PyQt4 pour Mac OS X. Cependant, il existe quelques distributions non officielles bien entretenues :

Site officiel : <http://www.riverbankcomputing.co.uk/software/pyqt/intro>

Site web de la distribution Mac OS X (PyQtX) : <http://sourceforge.net/projects/pyqtx/> (Téléchargement direct : <http://sourceforge.net/projects/pyqtx/files/latest/download>)

Après avoir installé PyQt4, téléchargez et installez le module QScintilla, qui est utilisé pour l'éditeur de script en ligne dans OpenSesame :

PyQScintillaX : <http://sourceforge.net/projects/pyqtx/files/PyQScintillaX/>

#### Installer NumPy et SciPy

Pour obtenir les dernières versions de NumPy ou SciPy, vous pouvez procéder de deux manières :

Vous pouvez utiliser le script d'installation qui se trouve à l'adresse <http://fonnesbeck.github.com/ScipySuperpack/> (Téléchargement direct : <https://raw.github.com/fonnesbeck/ScipySuperpack/master/install_superpack.sh>)
ainsi que les instructions sur la façon de l'utiliser. Ce script trouvera automatiquement les dernières versions de numpy et scipy et les installera pour vous. Fondamentalement, il suffit de lancer

	sudo sh ./install_superpack.sh

dans la console du dossier où vous avez téléchargé le script.

Alternativement, vous pouvez télécharger et installer les packages depuis les sites web des projets eux-mêmes :

Numpy : <http://sourceforge.net/projects/numpy/files/NumPy/> (Téléchargement direct version 1.7.0 : <http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/numpy-1.7.0-py2.7-python.org-macosx10.6.dmg/download>)
Scipy : <http://sourceforge.net/projects/scipy/files/scipy/> (Téléchargement direct version 0.11.0 : <http://sourceforge.net/projects/scipy/files/scipy/0.11.0/scipy-0.11.0-py2.7-python.org-macosx10.6.dmg/download>)

#### Installer PsychoPy et Expyriment (optionnel)

PsychoPy nécessite l'installation d'un certain nombre de dépendances. La plupart d'entre elles peuvent être installées assez facilement à l'aide de setuptools.

Site web : <http://pypi.python.org/pypi/setuptools>

Téléchargement direct : <http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea>

Comme décrit sur le site web, l'installation doit se dérouler selon les étapes suivantes :

Téléchargez l'œuf approprié pour votre version de Python (par exemple setuptools-0.6c9-py2.7.egg). Ne le renommez PAS.

Exécutez-le comme s'il s'agissait d'un script shell, par exemple

	sh setuptools-0.6c9-py2.7.egg

Setuptools s'installera en utilisant la version correspondante de Python (par exemple python2.7) et placera l'exécutable easy_install à l'emplacement par défaut pour l'installation des scripts Python (tel que déterminé par les fichiers de configuration distutils standard, ou par l'installation de Python).
Ensuite, installez la plupart des dépendances avec la commande :

	sudo easy_install psychopy pyglet pyopengl pil expyriment

Vous devrez peut-être installer manuellement Matplotlib, wxPython car (au moment des tests) ceux-ci ne se sont pas installés en utilisant easy_install. Assurez-vous d'installer les versions correspondant à votre version de Python.

*NOTE :* Le backend psychopy ne semble pas encore fonctionner et plante. La raison est que PsychoPy (ou plutôt sa bibliothèque sous-jacente pyglet) ne peut pas gérer l'environnement 64 bits cocoa des nouvelles versions de Mac OS X. Dans les nouvelles versions de psychopy, ce problème est, espérons-le, résolu.

#### Installer wxPython (facultatif, requis pour le backend PsychoPy)

Vous pouvez télécharger wxPython vous-même ou l'installer en utilisant easy_install (voir "installer PsychoPy").

Site Web : <http://wxpython.org/>

Téléchargement direct : <http://downloads.sourceforge.net/wxpython/wxPython2.9-osx-2.9.4.0-cocoa-py2.7.dmg>

#### Installer PyOpenGL (facultatif, requis pour le backend opengl ou expyriment)

Vous pouvez télécharger PyOpenGL vous-même ou l'installer en utilisant easy_install (voir "installer PsychoPy").

Site Web : <http://pyopengl.sourceforge.net/>

Téléchargement direct : <https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.0.2.tar.gz#md5=77becc24ffc0a6b28030aa109ad7ff8b>

### Exécuter OpenSesame

Téléchargez le code source de la dernière version d'OpenSesame ici. Extrayez le .tar.gz dans votre dossier personnel (toute autre localisation fonctionne de manière analogue). Ouvrez un terminal et passez à l'emplacement d'OpenSesame (cet exemple suppose que la version est 0.26) :

	cd /Users/[votre nom d'utilisateur]/opensesame-0.26

Exécutez OpenSesame avec l'une des commandes suivantes :

	python opensesame
	python opensesame --debug

[winpython-based package] : /getting-opensesame/running-with-python-portable/
[EPD_Download] : http://www.enthought.com/products/epd.php
[EPD_Packages] : http://www.enthought.com/products/epdlibraries.php
[xpyriment] : /backends/xpyriment
[legacy] : /backends/legacy
[psycho] : /backends/psycho
[cogsci.nl ppa] : https://launchpad.net/~smathot/+archive/cogscinl