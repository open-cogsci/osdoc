title: Herunterladen
hash: 02c996f07585f459badd7fcb648bad241d5c8415f54a7ceb58cd0b3f4dc465a5
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

Besser als ChatGPT für OpenSesame-Fragen. Ihr Abonnement über 9 €/Monat unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, falls Ihr Download nicht startet.
</div>


## Übersicht

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standard-Installationsoptionen

Die neueste $status$-Version ist $version$ *$codename$* ([Release Notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.13 für 64-Bit-Systeme. Die Installer- und `.zip`-Pakete sind identisch, abgesehen von der Installation. Die meisten Nutzer laden das Installer-Paket herunter (grüner Button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows, keine Installation nötig (.zip)
</a>

OpenSesame wird unter Windows 11 entwickelt und getestet. Die Funktionalität kann bei anderen Windows-Versionen abweichen.


### Mac OS

Beim ersten Start von OpenSesame wird die App vom Betriebssystem blockiert, da sie nicht von einem vertrauenswürdigen Entwickler stammt. Eine „Dennoch öffnen“-Option finden Sie unter Einstellungen > Datenschutz & Sicherheit. Diese Option erscheint, nachdem die App blockiert wurde.


<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>

OpenSesame wird unter Mac OS X Sequoia entwickelt und getestet. Die Funktionalität kann bei anderen Versionen von Mac OS X abweichen.



### Linux / Ubuntu

Kopieren Sie die folgende Zeile und fügen Sie sie in ein Terminal ein. Dadurch wird ein Installationsskript heruntergeladen und ausgeführt. Das Installationsskript benötigt curl und virtualenv. Unter Ubuntu können diese mit `sudo apt install curl python3-venv` installiert werden.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame wird unter Ubuntu 24.04 entwickelt und getestet. Die Funktionalität kann bei anderen Linux-Distributionen und anderen Ubuntu-Versionen abweichen.


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame Kern-Abhängigkeiten:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-) psycho-backend. Abhängig vom Betriebssystem und Python-Version kann es sein, dass PsychoPy nicht korrekt installiert wird. Falls dies der Fall ist, suchen Sie Unterstützung im Support-Forum oder verwenden Sie eines der vorgefertigten Pakete/Installer.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze für Eye-Tracking:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment für das xpyriment-backend

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach durch Ausführen von

```bash
opensesame
```

starten.

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

Folgen Sie anschließend den obenstehenden PyPi-Installationsanweisungen. Es werden keine dedizierten Anaconda-Pakete mehr bereitgestellt.


### Ältere Versionen

Ältere Versionen können von den GitHub-Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version soll verwendet werden?

OpenSesame wird aktuell mit Python 3.13 entwickelt und getestet. Andere Python-Versionen ab 3.10 funktionieren ebenfalls, werden aber nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Version, die ein Python-2-Paket enthielt, war 3.3.12, das weiterhin aus dem [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Führen Sie Updates während der Entwicklung und Testphase Ihres Experiments durch; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während eines laufenden Experiments, d. h. während Sie Daten erheben.
- Führen Sie ein Experiment mit derselben OpenSesame-Version durch, mit der Sie es entwickelt und getestet haben.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine reguläre Python-Umgebung, und Sie können `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame erscheint (Version endet auf 0, z. B. 3.1.0), folgen meist schnell ein oder zwei Wartungsversionen (z. B. 3.1.1 und 3.1.2), die größere Fehler beheben. Wenn Sie OpenSesame auf Systemen installieren, die Sie nicht oft aktualisieren, ist es daher am besten, bis zur zweiten oder dritten Wartungsversion (z. B. 3.0.2, 3.1.3 etc.) zu warten. So minimieren Sie das Risiko, eine Version von OpenSesame mit ernsthaften Fehlern auszurollen.
- Der Windows-Installer ermöglicht eine stille Installation von OpenSesame mit dem `/S`-Flag.