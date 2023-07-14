title: Eyelink
hash: 795cf5b31d90084e4fe773cb7002ad511f76aa023cfef172927e5544fd44ed44
locale: de
language: German

[TOC]

## Über EyeLink

Die Eyelink-Reihe von Eye-Trackern, produziert von SR Research, gehört zu den am häufigsten verwendeten Eye-Trackern in der psychologischen Forschung. SR Research stellt Python-Bindings für den Eyelink zur Verfügung (genannt PyLink), die von PyGaze verwendet werden. Die Lizenz von PyLink ist nicht mit der Lizenz von OpenSesame kompatibel. Aus diesem Grund ist PyLink nicht in der Standardverteilung von OpenSesame enthalten und muss separat installiert werden.


## Windows

### Installation des EyeLink Developers Kit

Das EyeLink Developers Kit (manchmal Display Software genannt) stellt die Bibliotheken zur Verfügung, die zum Kommunizieren mit dem EyeLink PC erforderlich sind. Sie finden es hier (kostenlose Registrierung erforderlich):

- <https://www.sr-research.com/support/thread-13.html>

Wenn Sie die `.zip`-Datei entpacken und dann den `.exe`-Installer ausführen, wird das EyeLink-Display in einem der folgenden Ordner installiert (abhängig von Ihrer Windows-Version:

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

In diesem Ordner gibt es einen `libs`-Unterordner, den Sie zum Systempfad hinzufügen müssen (dieser wurde möglicherweise automatisch hinzugefügt, aber prüfen Sie dies sicherheitshalber). Sie können dies tun, indem Sie „Mein Computer“ öffnen, auf „Systeminformationen anzeigen“ klicken, den Reiter „Erweitert“ öffnen, auf „Umgebungsvariablen“ klicken und `;C:\Program Files\SR Research\EyeLink\libs` oder (abhängig von Ihrem System) `;C:\Program Files (x86)\SR Research\EyeLink\libs` zur Path-Variable (unter Systemvariablen) hinzufügen.


### Installation von OpenSesame mit PyLink

PyLink ist die Python-Bibliothek für EyeLink-Unterstützung. Stand Juli 2023 unterstützt PyLink Python-Versionen bis 3.10, während OpenSesame standardmäßig Python 3.11 verwendet. Daher ist der einfachste Weg, OpenSesame mit PyLink zu installieren, bis Pylink für Python 3.11 aktualisiert wird, die Erstellung einer Python 3.10-Umgebung durch Anaconda.

Das klingt kompliziert, ist es aber wirklich nicht. Lesen Sie dazu zunächst das allgemeine Verfahren zur Installation von OpenSesame über Anaconda auf der Download-Seite:

- %link:download%

Fahren Sie dann, sobald Sie das allgemeine Verfahren verstanden haben, mit der Erstellung einer Python 3.10-Umgebung fort, folgen Sie den Anweisungen auf der Download-Seite und installieren Sie dann PyLink:

```
# Beginnen Sie mit der Erstellung einer Python 3.10-Umgebung
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Befolgen Sie nun die Anweisungen von der Download-Seite
# ...
# Installieren Sie dann PyLink aus dem SR Research PyPi-Repository
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
# Und starten Sie jetzt OpenSesame!
opensesame
```

Weitere Informationen zu PyLink finden Sie im SR Research-Forum (kostenlose Registrierung erforderlich):

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

Die EyeLink-Display-Software kann direkt aus einem Repository installiert werden. Dies installiert auch PyLink und verschiedene bequeme Tools, wie den `edf2asc`-Konverter.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Für weitere Informationen besuchen Sie bitte:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Nachdem Sie die EyeLink-Display-Software und PyLink gemäß den obigen Anweisungen installiert haben, können Sie den EyeLink mit PyGaze verwenden! Siehe:

- %link:pygaze%