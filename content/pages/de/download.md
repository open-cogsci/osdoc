title: Herunterladen
hash: acf8377b52efc30d1c3f5f4f459cb00a79f09028ca118806c6cf122c7a3e9925
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

<h3>Ihr Download sollte in Kürze starten!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Abonnieren Sie SigmundAI.eu
</a>

Besser als ChatGPT für OpenSesame-Fragen. Ihr 9 €/Monat-Abonnement unterstützt OpenSesame.

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

Die neueste $status$-Version ist $version$ *$codename$* ([Release Notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.13 für 64-Bit-Systeme. Die Installer- und `.zip`-Pakete sind identisch, abgesehen von der Installation. Die meisten Benutzer laden das Installer-Paket herunter (grüner Button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows – keine Installation erforderlich (.zip)
</a>

OpenSesame wird unter Windows 11 entwickelt und getestet. Ihre Erfahrungen können auf anderen Windows-Versionen variieren.


### Mac OS

Mac OS-Pakete sind für OpenSesame 4.1 noch nicht verfügbar. Der untenstehende Download-Link verweist weiterhin auf 4.0.
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>


### Linux / Ubuntu

Kopieren Sie die folgende Zeile und fügen Sie sie in ein Terminal ein. Dadurch wird ein Installationsskript heruntergeladen und ausgeführt. Das Installationsskript benötigt curl und virtualenv. Unter Ubuntu können diese mit `sudo apt install curl python3-venv` installiert werden.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame wird unter Ubuntu 24.04 entwickelt und getestet. Ihre Erfahrungen können auf anderen Linux-Distributionen und anderen Ubuntu-Versionen variieren.


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können per pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame-Core-Abhängigkeiten:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-)psycho-Backend. Je nach Betriebssystem und Python-Version kann es sein, dass PsychoPy nicht korrekt installiert wird. Wenn dies passiert, suchen Sie Unterstützung im Support-Forum oder nutzen Sie eine der vorgefertigten Pakete/Installer.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze für Eye-Tracking:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment für das xpyriment-Backend

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Sobald Sie alle Pakete installiert haben, können Sie OpenSesame einfach mit folgendem Befehl starten:

```bash
opensesame
```

Oder für Sigmund Analyst (Code-Editor):

```bash
sigmund-analyst
```


### Anaconda (plattformübergreifend)

Erstellen Sie zunächst eine neue Python-Umgebung für OpenSesame (optional):

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Folgen Sie anschließend den obigen PyPi-Installationsanweisungen. Dedizierte Anaconda-Pakete werden nicht mehr bereitgestellt.


### Ältere Versionen

Ältere Versionen können von den GitHub-Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version soll verwendet werden?

OpenSesame wird derzeit mit Python 3.13 entwickelt und getestet. Andere Versionen von Python >=3.10 funktionieren, werden aber nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Version, die ein Python-2-Paket enthielt, war 3.3.12. Diese kann weiterhin aus dem [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und des Testens Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während eines laufenden Experiments; das heißt, nehmen Sie keine Updates vor, während Sie Daten erheben.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, mit der Sie entwickelt und getestet haben.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine reguläre Python-Umgebung und Sie können `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Versionsnummer, die auf 0 endet, z.B. 3.1.0), folgen in der Regel ein oder zwei Wartungsversionen (z.B. 3.1.1 und 3.1.2), die größere Fehler beheben. Deshalb ist es am besten, bei Installationen auf Systemen, die nicht häufig aktualisiert werden, bis zur zweiten oder dritten Wartungsversion zu warten (z.B. 3.0.2, 3.1.3 usw.). So minimieren Sie das Risiko, eine Version von OpenSesame auszurollen, die gravierende Fehler enthält.
- Der Windows-Installer ermöglicht eine stille Installation von OpenSesame mit dem `/S`-Flag.