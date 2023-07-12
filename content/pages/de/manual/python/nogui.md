title: OpenSesame als Python-Bibliothek (keine GUI)
hash: f402b6dd5bcb95ef27e11fded05dd0fb27ec738f984dad3ea0c2ccc950ffbe1e
locale: de
language: German

Sie können Experimente auch vollständig programmatisch schreiben, indem Sie OpenSesame als Python-Modul verwenden. Dies eignet sich hauptsächlich für Leute, die Codierung gegenüber der Verwendung einer graphischen Benutzeroberfläche bevorzugen.

Die Verwendung von OpenSesame als Python-Modul funktioniert weitgehend genauso wie die Verwendung von Python `inline_script`-Elementen in der Benutzeroberfläche, mit zwei bemerkenswerten Ausnahmen:

- Funktionen und Klassen müssen explizit aus `libopensesame.python_workspace_api` importiert werden. Alle unter [Gemeinsame Funktionen](%url:manual/python/common%) beschriebenen Funktionen und Klassen sind verfügbar.
- Ein `experiment`-Objekt muss explizit mit der `Experiment()`-Fabrikfunktion erstellt werden.

Ein einfaches Hello World-Experiment sieht so aus:

```python
from libopensesame.python_workspace_api import \
  Experiment, Canvas, Keyboard, Text

# Initialisieren Sie das Experimentfenster mit dem Legacy-Backend
exp, win, clock, log = Experiment(canvas_backend='legacy')
# Bereiten Sie eine Reiz-Leinwand und eine Tastatur vor
cnv = Canvas()
cnv += Text('Hallo Welt')
kb = Keyboard()
# Zeigen Sie die Leinwand an, warten Sie auf einen Tastendruck und beenden Sie dann das Experiment
cnv.show()
kb.get_key()
exp.end()
```

Sie können auch programmatisch eine `.osexp`-Experimentdatei öffnen und ausführen:

```python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
```