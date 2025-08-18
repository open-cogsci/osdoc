title: Herunterladen
hash: 9beb2ebf584b530f7411227d288486a4076872b885ede71e4a690dd50ad929c9
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

<h3>Ihr Download sollte in Kürze beginnen!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Abonnieren Sie SigmundAI.eu
</a>

Ihr KI-Co-Pilot für OpenSesame. Ihr Abonnement für 9 €/Monat unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, falls Ihr Download nicht startet.
</div>


## Überblick

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standard-Installationsoptionen

Die neueste $status$ Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows, keine Installation erforderlich (.zip)
</a>

Die meisten Leute laden das `.exe`-Installer-Paket herunter. Wenn Sie keine Administratorrechte besitzen oder mehrere Versionen von OpenSesame parallel ausführen müssen, laden Sie stattdessen das `.zip`-Paket herunter.

Basierend auf Python 3.13 für 64-Bit-Systeme. Getestet unter Windows 11.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>

Beim ersten Starten von OpenSesame wird die App durch das Betriebssystem blockiert, da sie nicht von einem vertrauenswürdigen Entwickler stammt. Unter Einstellungen > Datenschutz & Sicherheit finden Sie eine Option „Dennoch öffnen“. Diese Option erscheint, nachdem die App blockiert wurde.

Basierend auf Python 3.13 für 64-Bit-Intel-Systeme. Getestet unter Mac OS X Sequoia.


### Linux / Ubuntu

Kopieren Sie die folgenden Zeilen und fügen Sie sie in ein Terminal ein. Dies lädt ein Installationsskript herunter und führt es aus.

```bash
# Diese Pakete müssen unter Ubuntu 24.04 installiert werden.
# Gleichwertige Pakete müssen auf anderen
# Linux-Distributionen installiert werden.
sudo apt install curl python3-venv libxcb-cursor0
# OpenSesame-Installationsskript herunterladen und ausführen.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Getestet unter Ubuntu 24.04 (Python 3.12).


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame Kernabhängigkeiten:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-) psycho Backend. Je nach Betriebssystem und Python-Version könnte sich PsychoPy möglicherweise nicht ordnungsgemäß installieren lassen. Sollte dies passieren, holen Sie sich Hilfe im Supportforum oder verwenden Sie eines der vorkonfigurierten Pakete/Installationsprogramme.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze für Eye-Tracking:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment für das xpyriment Backend

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie ausführen:

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

Folgen Sie danach den obigen PyPi-Installationsanweisungen. Eigene Anaconda-Pakete werden nicht länger bereitgestellt.


### Ältere Versionen

Ältere Versionen können von den GitHub-Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version sollte verwendet werden?

OpenSesame wird aktuell mit Python 3.13 entwickelt und getestet. Andere Python-Versionen ab 3.10 funktionieren ebenfalls, sind jedoch nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Das letzte Release, das ein Python-2-Paket enthielt, war 3.3.12; dieses kann weiterhin vom [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und des Testens Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während der Durchführung eines Experiments, also während der Datenerhebung.
- Führen Sie ein Experiment immer mit derselben Version von OpenSesame durch, mit der Sie auch entwickelt und getestet haben.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine reguläre Python-Umgebung, und Sie können `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (Versionsnummer endet auf 0, z. B. 3.1.0), folgen in der Regel schnell ein oder zwei Wartungsversionen (z. B. 3.1.1 und 3.1.2), die wesentliche Fehler beheben. Daher ist es am besten, bei der Installation von OpenSesame auf Systemen, die Sie nicht häufig aktualisieren, bis zur zweiten oder dritten Wartungsversion zu warten (z. B. 3.0.2, 3.1.3 usw.). So minimieren Sie das Risiko, eine Version mit schwerwiegenden Fehlern auszurollen.
- Der Windows-Installer ermöglicht eine stille Installation von OpenSesame mit dem `/S`-Parameter.