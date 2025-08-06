title: Herunterladen
hash: 4c609d80d00e5704f1e59d0daf4820641810168b01ec87f556a20c226969d520
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
 &#128150; Abonniere SigmundAI.eu
</a>

Besser als ChatGPT für OpenSesame-Fragen. Dein 9€/Monat-Abonnement unterstützt OpenSesame.

Klicke <a id="click-here">hier</a>, falls dein Download nicht startet.
</div>


## Übersicht

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standard-Installationsoptionen

Die neueste $status$ Version ist $version$ *$codename$* ([Release Notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows – keine Installation erforderlich (.zip)
</a>

Die meisten laden das `.exe`-Installationspaket herunter. Falls du keine Administratorrechte hast oder mehrere Versionen von OpenSesame parallel nutzen möchtest, lade stattdessen das `.zip`-Paket herunter.

Basierend auf Python 3.13 für 64-Bit-Systeme. Getestet unter Windows 11.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>

Wenn du OpenSesame das erste Mal startest, wird es vom Betriebssystem blockiert, da die App nicht von einem vertrauenswürdigen Entwickler stammt. Unter Einstellungen > Datenschutz & Sicherheit findest du die Option "Dennoch öffnen". Diese Option erscheint, nachdem die App blockiert wurde.

Basierend auf Python 3.13 für 64-Bit-Intel-Systeme. Getestet unter Mac OS X Sequoia.


### Linux / Ubuntu

Kopiere die folgende Zeile und füge sie in ein Terminal ein. Dadurch wird ein Installationsskript heruntergeladen und ausgeführt. Das Installationsskript benötigt curl und virtualenv. Unter Ubuntu können diese mit `sudo apt install curl python3-venv` installiert werden.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Getestet unter Ubuntu 24.04 (Python 3.12).


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können über pip installiert werden. Beachte, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame Core-Abhängigkeiten:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-) psycho Backend. Je nach Betriebssystem und Python-Version kann es sein, dass PsychoPy nicht korrekt installiert wird. In diesem Fall hole dir Unterstützung im Support-Forum oder verwende eines der vorkonfigurierten Pakete bzw. Installationsprogramme.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze für Eyetracking:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment für das xpyriment Backend

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Nachdem du alle Pakete installiert hast, kannst du OpenSesame einfach ausführen mit:

```bash
opensesame
```

Oder für Sigmund Analyst (Code-Editor):

```bash
sigmund-analyst
```


### Anaconda (plattformübergreifend)

Lege zunächst ein neues Python-Umfeld für OpenSesame an (optional):

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Folge anschließend den obigen PyPi-Installationsanweisungen. Spezielle Anaconda-Pakete werden nicht mehr bereitgestellt.


### Ältere Versionen

Ältere Versionen können von den GitHub-Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version soll verwendet werden?

OpenSesame wird derzeit mit Python 3.13 entwickelt und getestet. Andere Python-Versionen ab 3.10 funktionieren ebenfalls, werden aber nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Version, die ein Python-2-Paket enthielt, war 3.3.12, die weiterhin im [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und Testung Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während eines laufenden Experiments; das heißt, aktualisieren Sie nicht, während Sie Daten erheben.
- Führen Sie ein Experiment mit derselben OpenSesame-Version durch, mit der Sie es entwickelt und getestet haben.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine reguläre Python-Umgebung, und Sie können `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Tipps für Systemadministrator:innen

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Versionsnummer, die auf 0 endet, z.B. 3.1.0), folgt in der Regel schnell ein oder zwei Wartungsversionen (z.B. 3.1.1 und 3.1.2), die größere Fehler beheben. Wenn Sie OpenSesame daher auf Systemen installieren, die Sie nicht oft aktualisieren, empfiehlt es sich, bis zur zweiten oder dritten Wartungsversion zu warten (z.B. 3.0.2, 3.1.3 usw.). So minimieren Sie das Risiko, eine Version von OpenSesame auszurollen, die schwerwiegende Fehler enthält.
- Der Windows-Installer ermöglicht die stille Installation von OpenSesame mit dem `/S`-Flag.