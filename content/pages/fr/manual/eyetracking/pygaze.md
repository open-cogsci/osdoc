title: PyGaze (suivi du regard)
hash: 80766dbbeccf44569af795eddea4817ca3fd7e30726a50587814ffbfd94c5c8a
locale: fr
language: French

[TOC]

## À propos

PyGaze est une bibliothèque Python pour l'eye tracking. Un ensemble de plugins vous permet d'utiliser PyGaze au sein d'OpenSesame. Pour plus d'informations sur PyGaze, visitez :

- <http://www.pygaze.org/>

Veuillez citer PyGaze comme suit :

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: une boîte à outils open source et multiplateforme pour la programmation d'expériences d'eye tracking avec un effort minimal. *Behavior Research Methods*. doi:10.3758/s13428-013-0422-2
{: .reference}

## Eye trackers pris en charge

PyGaze prend en charge les eye trackers suivants:

- [EyeLink](%link:eyelink%)
- [EyeTribe](%link:eyetribe%)

Pour les eye trackers suivants, il y a un support expérimental :

- [EyeLogic](%link:eyelogic%)
- [GazePoint / OpenGaze](%link:gazepoint%)
- [SMI](%link:smi%)
- [Tobii](%link:tobii%)

Vous pouvez également effectuer un eye tracking basique dans des expériences en ligne avec WebGazer.js :

- [WebGazer.js](%link:webgazer%)

PyGaze inclut également deux eye trackers fictifs pour les tests :

- __Simple dummy__ — Ne fait rien.
- __Dummy avancé__ — Simulation de mouvements oculaires avec la souris.

## Installation de PyGaze

### Windows

Si vous utilisez le package officiel Windows d'OpenSesame, PyGaze est déjà installé.

### Ubuntu

Si vous utilisez Ubuntu, vous pouvez obtenir PyGaze à partir du PPA Cogsci.nl :

```
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install python-pygaze
```

Ou, si vous utilisez Python 3, changez la dernière commande pour :

```
sudo apt-get install python3-pygaze
```

## Installation avec pip (toutes les plates-formes)

Vous pouvez installer PyGaze avec `pip` :

```
pip install python-pygaze
```

### Anaconda (toutes les plates-formes)

```
conda install python-pygaze -c cogsci
```

## Plugins PyGaze OpenSesame

Les plugins PyGaze suivants sont disponibles :

- PYGAZE_INIT — Initialise PyGaze. Ce plugin est généralement inséré au début de l'expérience.
- PYGAZE_DRIFT_CORRECT — Implémente une procédure de correction de dérive.
- PYGAZE_START_RECORDING — Met PyGaze en mode enregistrement.
- PYGAZE_STOP_RECORDING — Sort PyGaze du mode enregistrement.
- PYGAZE_WAIT — Met en pause jusqu'à ce qu'un événement se produise, comme le début d'une saccade.
- PYGAZE_LOG — Enregistre des variables expérimentales et du texte arbitraire.

## Exemple

Pour un exemple d'utilisation des plugins PyGaze, consultez le modèle PyGaze inclus avec OpenSesame.

Ci-dessous un exemple d'utilisation de PyGaze dans un INLINE_SCRIPT Python :

~~~ .python
# Créez un clavier et un objet toile
my_keyboard = Keyboard(timeout=0)
my_canvas = Canvas()
my_canvas['dot'] = Circle(x=0, y=0, r=10, fill=True)
# Boucle ...
while True:
	# ... jusqu'à ce que l'espace soit pressé
	key, timestamp = my_keyboard.get_key()
	if key == 'space':
		break
	# Obtenez la position du regard à partir de pygaze ...
	x, y = eyetracker.sample()
	# ... et dessinez un point de fixation dépendant du regard !
	my_canvas['dot'].x = x + my_canvas.left
	my_canvas['dot'].y = y + my_canvas.top
	my_canvas.show()
~~~

## Aperçu des fonctions

Pour initialiser PyGaze dans OpenSesame, insérez le plugin PYGAZE_INIT dans votre expérience. Une fois que vous avez fait cela, un objet `eyetracker` sera disponible, qui offre les fonctions suivantes :

%-- include: include/api/eyetracker.md --%