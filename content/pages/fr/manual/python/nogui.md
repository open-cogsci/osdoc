title: OpenSesame en tant que bibliothèque Python (pas d'interface graphique)
hash: f402b6dd5bcb95ef27e11fded05dd0fb27ec738f984dad3ea0c2ccc950ffbe1e
locale: fr
language: French

Vous pouvez également rédiger des expériences entièrement de manière programmatique en utilisant OpenSesame comme un module Python. C'est principalement adapté pour les personnes qui préfèrent coder plutôt que d'utiliser une interface utilisateur graphique.

Utiliser OpenSesame comme un module Python fonctionne de la même manière que l'utilisation d'éléments Python `inline_script` dans l'interface utilisateur, avec deux exceptions notables :

- Les fonctions et les classes doivent être explicitement importées de `libopensesame.python_workspace_api`. Toutes les fonctions et classes décrites dans [Fonctions communes](%url:manual/python/common%) sont disponibles.
- Un objet `experiment` doit être explicitement créé en utilisant la fonction factory `Experiment()`.

Une simple expérience Hello World ressemble à cela :

```python
from libopensesame.python_workspace_api import \
  Experiment, Canvas, Keyboard, Text

# Initialiser la fenêtre d'expérience en utilisant le backend obsolète
exp, win, clock, log = Experiment(canvas_backend='legacy')
# Préparer un canevas de stimulus et un clavier
cnv = Canvas()
cnv += Text('Bonjour le monde')
kb = Keyboard()
# Afficher le canevas, attendre une pression de touche, puis terminer l'expérience
cnv.show()
kb.get_key()
exp.end()
```

Vous pouvez aussi ouvrir et exécuter de manière programmatique un fichier d'expérience `.osexp` :

```python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
```
