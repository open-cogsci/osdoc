title: PyGaze (Eye-Tracking)
hash: 80766dbbeccf44569af795eddea4817ca3fd7e30726a50587814ffbfd94c5c8a
locale: de
language: German

[TOC]

## Über

PyGaze ist eine Python-Bibliothek für Eye Tracking. Ein Satz von Plugins ermöglicht Ihnen, PyGaze innerhalb von OpenSesame zu verwenden. Für weitere Informationen über PyGaze, besuchen Sie:

- <http://www.pygaze.org/>

Bitte zitieren Sie PyGaze wie folgt:

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: An open-source, cross-platform toolbox for minimal-effort programming of eyetracking experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0422-2
{: .reference}

## Unterstützte Eye Tracker

PyGaze unterstützt die folgenden Eye Tracker:

- [EyeLink](%link:eyelink%)
- [EyeTribe](%link:eyetribe%)

Für die folgenden Eye Tracker gibt es experimentelle Unterstützung:

- [EyeLogic](%link:eyelogic%)
- [GazePoint / OpenGaze](%link:gazepoint%)
- [SMI](%link:smi%)
- [Tobii](%link:tobii%)

Mit WebGazer.js können Sie auch grundlegendes Eye Tracking für Online-Experimente durchführen:

- [WebGazer.js](%link:webgazer%)

PyGaze enthält auch zwei Dummy-Eye Tracker für Testzwecke:

- __Einfacher Dummy__ — Tut nichts.
- __Erweiterter Dummy__ — Maus-Simulation von Augenbewegungen.

## PyGaze installieren

### Windows

Wenn Sie das offizielle Windows-Paket von OpenSesame verwenden, ist PyGaze bereits installiert.

### Ubuntu

Wenn Sie Ubuntu verwenden, können Sie PyGaze aus dem Cogsci.nl PPA beziehen:

```
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install python-pygaze
```

Oder, wenn Sie Python 3 verwenden, ändern Sie den letzten Kommentar in:

```
sudo apt-get install python3-pygaze
```

## pip install (alle Plattformen)

Sie können PyGaze mit `pip` installieren:

```
pip install python-pygaze
```

### Anaconda (alle Plattformen)

```
conda install python-pygaze -c cogsci
```

## PyGaze OpenSesame Plugins

Die folgenden PyGaze Plugins sind verfügbar:

- PYGAZE_INIT — Initialisiert PyGaze. Dieses Plugin wird im Allgemeinen am Anfang des Experiments eingefügt.
- PYGAZE_DRIFT_CORRECT — Implementiert ein Driftkorrekturverfahren.
- PYGAZE_START_RECORDING — Setzt PyGaze in den Aufnahmemodus.
- PYGAZE_STOP_RECORDING — Setzt PyGaze aus dem Aufnahmemodus zurück.
- PYGAZE_WAIT — Pausiert bis ein Ereignis eintritt, wie z.B. der Beginn einer Sakkade.
- PYGAZE_LOG — Protokolliert experimentelle Variablen und beliebigen Text.

## Beispiel

Ein Beispiel, wie die PyGaze Plugins verwendet werden, finden Sie in der PyGaze Vorlage, die mit OpenSesame enthalten ist.

Im Folgenden finden Sie ein Beispiel, wie PyGaze in einem Python INLINE_SCRIPT verwendet wird:

~~~ .python
# Erstellen Sie ein Tastatur- und ein Canvas-Objekt
my_keyboard = Keyboard(timeout=0)
my_canvas = Canvas()
my_canvas['dot'] = Circle(x=0, y=0, r=10, fill=True)
# Schleife ...
while True:
	# ... bis die Leertaste gedrückt wird
	key, timestamp = my_keyboard.get_key()
	if key == 'space':
		break
	# Holen Sie die Blickposition von pygaze ...
	x, y = eyetracker.sample()
	# ... und zeichnen Sie einen blickkontingenten Fixationspunkt!
	my_canvas['dot'].x = x + my_canvas.left
	my_canvas['dot'].y = y + my_canvas.top
	my_canvas.show()
~~~

## Funktionsübersicht

Um PyGaze in OpenSesame zu initialisieren, fügen Sie das PYGAZE_INIT Plugin in Ihr Experiment ein. Sobald Sie dies getan haben, steht Ihnen ein `eyetracker` Objekt zur Verfügung, das die folgenden Funktionen bietet:

%-- include: include/api/eyetracker.md --%
