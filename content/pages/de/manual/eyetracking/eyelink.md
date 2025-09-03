title: Eyelink
hash: 446281a464dd40eabe3f55f650572a8894359598a77c99f0c8eb20fe31cad1fc
locale: de
language: German

[TOC]

## Über EyeLink

Die EyeLink-Reihe von Eyetrackern, hergestellt von SR Research, gehören zu den am häufigsten verwendeten Eyetrackern in der psychologischen Forschung. SR Research stellt Python-Bindings für den EyeLink bereit (genannt PyLink), die von PyGaze verwendet werden. Die Lizenz von PyLink ist mit der von OpenSesame verwendeten Lizenz nicht kompatibel. Aus diesem Grund ist PyLink nicht in der Standarddistribution von OpenSesame enthalten und muss separat installiert werden.

## Windows

### Installation des EyeLink Developers Kit

Das EyeLink Developers Kit (manchmal Display Software genannt) stellt die Bibliotheken bereit, die für die Kommunikation mit dem EyeLink-PC benötigt werden. Sie finden es hier (kostenlose Registrierung erforderlich):

- <https://www.sr-research.com/support/thread-13.html>

Wenn Sie die `.zip`-Datei entpacken und dann das `.exe`-Installationsprogramm ausführen, wird die EyeLink-Display-Software in einem der folgenden Ordner installiert (je nach Ihrer Windows-Version):

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

In diesem Ordner befindet sich ein `libs`-Unterordner, den Sie zum Systempfad hinzufügen müssen (dies wurde möglicherweise schon automatisch hinzugefügt, überprüfen Sie es aber sicherheitshalber). Dies können Sie tun, indem Sie "Arbeitsplatz" öffnen, auf "Systeminformationen anzeigen" klicken, den "Erweitert"-Tab öffnen, auf "Umgebungsvariablen" klicken und `;C:\Program Files\SR Research\EyeLink\libs` oder (je nach Ihrem System) `;C:\Program Files (x86)\SR Research\EyeLink\libs` an die Variable Path (unter Systemvariablen) anhängen.

### Installation von OpenSesame mit PyLink

`pylink` ist die Python-Bibliothek für die Unterstützung von EyeLink. Zurzeit unterstützt `pylink` nur Python 3.12 und älter, während die Standardpakete von OpenSesame mit Python 3.13 gebaut wurden. Daher müssen Sie das Python 3.12 (oder älter) Paket von OpenSesame von [GitHub Releases](https://github.com/open-cogsci/OpenSesame/releases) verwenden.

Anschließend kann `pylink` aus dem SR Research PyPi-Repository mit `pip install` installiert werden:

```
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
```

Wichtig: Versuchen Sie *nicht*, `pylink` durch den Befehl `pip install pylink` zu installieren! Dadurch wird ein völlig anderes Paket installiert!

Weitere Informationen zu `pylink` finden Sie im SR Research Forum (kostenlose Registrierung erforderlich):

- <https://www.sr-research.com/support/thread-8291.html>

## Ubuntu

Die EyeLink-Display-Software kann direkt aus einem Repository installiert werden. Dadurch werden auch PyLink und verschiedene nützliche Werkzeuge wie der `edf2asc`-Konverter installiert.

```bash
sudo add-apt-repository 'deb [arch=amd64] https://apt.sr-research.com SRResearch main'
sudo apt-key adv --fetch-keys https://apt.sr-research.com/SRResearch_key
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Für weitere Informationen besuchen Sie bitte:

- <https://www.sr-support.com/thread-13.html>

## PyGaze

Nachdem Sie die EyeLink-Display-Software und PyLink gemäß obiger Anleitung installiert haben, können Sie EyeLink mit PyGaze verwenden! Siehe:

- %link:pygaze%

## SR Research eyelink plugin

SR Research bietet auch eigene EyeLink-Plug-ins für OpenSesame an. Diese ähneln (und basieren ursprünglich auf) den PyGaze-Plugins, bieten aber einige Funktionalitäten, die über PyGaze nicht verfügbar sind. Um diese Plugins zu installieren, führen Sie aus:

```
pip install opensesame-plugin-eyelink
```

Für weitere Informationen besuchen Sie bitte:

- <https://www.sr-research.com/support/thread-52.html>