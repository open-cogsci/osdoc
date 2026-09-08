title: Herunterladen
hash: 43af7638374babac965b68a0a316b0487bd9a9f780ffb4e0674e0c7e015f026e
locale: de
language: German

<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('download-started').style.display = 'block'
	document.getElementById('download-started').scrollIntoView()
}
</script>

<div class="info-box" id="download-started" markdown="1" style="display:none;">

<h3>Dein Download sollte in Kürze starten!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; SigmundAI.eu abonnieren
</a>

Dein KI-Copilot für OpenSesame. Dein Abonnement für 9 € pro Monat unterstützt OpenSesame.

Klicke <a id="click-here">hier</a>, wenn dein Download nicht startet.
</div>


## Overview

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standardinstallationsoptionen

Die neueste $status$-Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b>-Windows-Installationsprogramm (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b>-Windows, keine Installation erforderlich (.zip)
</a>

Die meisten Menschen laden das Installationspaket `.exe` herunter. Wenn du keine Administratorrechte hast oder mehrere Versionen von OpenSesame parallel ausführen musst, lade stattdessen das Paket `.zip` herunter.

Basierend auf Python 3.13 für 64-Bit-Systeme. Getestet unter Windows 11.

Einige externe Geräte, wie [Tobii](%url:tobii%)-Eye-Tracker, benötigen eine andere Python-Version. Weitere Informationen findest du auf den jeweiligen Dokumentationsseiten.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac-OS-Paket (.dmg)
</a>

Wenn du OpenSesame zum ersten Mal startest, wird es vom Betriebssystem blockiert, weil die App nicht von einem vertrauenswürdigen Entwickler stammt. Unter Einstellungen > Datenschutz & Sicherheit findest du die Option „Trotzdem öffnen“. Diese Option erscheint, nachdem die App blockiert wurde.

Basierend auf Python 3.13 für 64-Bit-Intel-Systeme. Getestet unter Mac OS X Sequoia.

Einige externe Geräte, wie [Tobii](%url:tobii%)-Eye-Tracker, benötigen eine andere Python-Version. Weitere Informationen findest du auf den jeweiligen Dokumentationsseiten.


### Linux / Ubuntu

Kopiere die folgenden Zeilen in ein Terminal und füge sie dort ein. Dadurch wird ein Installationsskript heruntergeladen und ausgeführt.

```bash
# These packages need to be installed on Ubuntu 24.04.
# Equivalent packages need to be installed on other
# Linux distributions.
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# Download and run the OpenSesame installation script.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/nightingale/linux-installer.sh) --install
```

Getestet unter Ubuntu 24.04 (Python 3.12).


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachte, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame-Kernabhängigkeiten:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (standardmäßige) psycho backend. Abhängig von deinem Betriebssystem und deiner Python-Version lässt sich PsychoPy möglicherweise nicht korrekt installieren. Wenn dies passiert, suche im Supportforum Hilfe oder verwende eines der vorgefertigten Pakete/Installationsprogramme.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze für Eye-Tracking:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment für das xpyriment backend

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Sobald du alle Pakete installiert hast, kannst du OpenSesame einfach durch Ausführen von Folgendem starten:

```bash
opensesame
```

Oder für Sigmund Analyst (Code-Editor):

```bash
sigmund-analyst
```


### Anaconda (plattformübergreifend)

Erstellen Sie zunächst eine neue Python-Umgebung für OpenSesame (optional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Folgen Sie anschließend den obigen PyPi-Installationsanweisungen. Separate Anaconda-Pakete werden nicht mehr bereitgestellt.


### Ältere Versionen von OpenSesame und andere Python-Versionen

Ältere Versionen von OpenSesame sowie Pakete, die mit anderen Versionen von Python (3.10, 3.11 und 3.12) erstellt wurden, sind in den GitHub-Releases verfügbar:

- <https://github.com/open-cogsci/OpenSesame/releases>



### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version sollte verwendet werden?

OpenSesame wird derzeit mit Python 3.13 erstellt und getestet. Andere Python-Versionen >=3.10 funktionieren, werden jedoch nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Version, die ein Python-2-Paket enthielt, war 3.3.12, die weiterhin aus dem [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann sollte (nicht) aktualisiert werden?

- Aktualisieren Sie während der Entwicklung und des Testens Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während der Durchführung eines Experiments; das heißt, aktualisieren Sie nicht, während Sie Daten erheben.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, die Sie für die Entwicklung und das Testen verwendet haben.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine reguläre Python-Umgebung, und Sie können `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Versionsnummer, die auf 0 endet, z. B. 3.1.0), folgen in der Regel schnell ein oder zwei Wartungsreleases (z. B. 3.1.1 und 3.1.2), die schwerwiegende Fehler beheben. Wenn Sie OpenSesame daher auf Systemen installieren, die Sie nicht häufig aktualisieren, ist es am besten, bis zum zweiten oder dritten Wartungsrelease zu warten (z. B. 3.0.2, 3.1.3 usw.). Auf diese Weise minimieren Sie das Risiko, eine Version von OpenSesame bereitzustellen, die schwerwiegende Fehler enthält.
- Das Windows-Installationsprogramm ermöglicht die unbeaufsichtigte Installation von OpenSesame mit dem Flag `/S`.