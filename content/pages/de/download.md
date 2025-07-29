title: Herunterladen
hash: 70d7d3aa0db9c3d49b6e9a94cd6d92a1dd50ec0dc94bc9bfc9e076703ab3dd3a
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

Besser als ChatGPT für OpenSesame-Fragen. Ihr Abonnement von 9 €/Monat unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, falls Ihr Download nicht automatisch startet.
</div>


## Überblick

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Alle Download-Optionen

Die neueste $status$-Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.13 für 64-Bit-Systeme. Die Installer- und `.zip`-Pakete sind identisch, abgesehen von der Installation. Die meisten Nutzer laden das Installer-Paket herunter (grüner Button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows – Keine Installation erforderlich (.zip)
</a>


### Mac OS

Mac OS-Pakete sind für OpenSesame 4.1 noch nicht verfügbar. Der folgende Download-Link verweist daher noch auf 4.0.
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>


### Linux / Ubuntu

Kopieren Sie die folgende Zeile und fügen Sie sie in ein Terminal ein. Dies lädt ein Installationsskript herunter und führt es aus. Das Installationsskript erfordert virtualenv, das sich unter Ubuntu mit `sudo apt install python3-venv` installieren lässt.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame wird unter Ubuntu 24.04 entwickelt und getestet. Ihre Erfahrungen können auf anderen Linux-Distributionen und Ubuntu-Versionen variieren.


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame Kern-Abhängigkeiten:

```bash
# OpenSesame core dependencies
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-)psycho-Backend. Abhängig von Ihrem Betriebssystem und Ihrer Python-Version kann es bei der Installation von PsychoPy zu Problemen kommen. In diesem Fall suchen Sie bitte Hilfe im Support-Forum oder benutzen ein vorkonfiguriertes Paket/einen Installer.

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

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten durch:

```bash
opensesame
```

Oder für Sigmund Analyst (Code-Editor):

```bash
sigmund-analyst
```


### Anaconda (plattformübergreifend)

Zuerst ein neues Python-Environment für OpenSesame erstellen (optional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Folgen Sie anschließend den obigen PyPi-Installationsanweisungen. Dedizierte Anaconda-Pakete werden nicht mehr bereitgestellt.


### Ältere Versionen

Ältere Versionen können auf GitHub Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version sollte verwendet werden?

OpenSesame wird derzeit mit Python 3.13 entwickelt und getestet. Andere Python-Versionen ab 3.10 funktionieren, werden jedoch nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Version, die ein Python-2-Paket enthielt, war 3.3.12. Diese kann weiterhin aus dem [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und dem Testen Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu nutzen.
- Aktualisieren Sie nicht während eines laufenden Experiments, also während Sie Daten erheben.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, die Sie auch zur Entwicklung und zum Testen verwendet haben.


### Pakete manuell aktualisieren

OpenSesame ist eine reguläre Python-Umgebung und Sie können `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Hinweise für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Versionsnummer, die auf 0 endet, z. B. 3.1.0), folgt in der Regel schnell ein oder zwei Wartungsversionen (z. B. 3.1.1 und 3.1.2), die größere Fehler beheben. Daher ist es sinnvoll, mit der Installation von OpenSesame auf Systemen, die Sie nicht häufig aktualisieren, bis zur zweiten oder dritten Wartungsversion (z. B. 3.0.2, 3.1.3 usw.) zu warten. So minimieren Sie das Risiko, eine Version von OpenSesame mit schwerwiegenden Fehlern einzusetzen.
- Mit dem Windows-Installer können Sie OpenSesame mit dem `/S`-Flag lautlos installieren.