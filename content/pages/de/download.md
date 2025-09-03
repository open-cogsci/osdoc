title: Herunterladen
hash: e832cf1e1be9442432bd3d542053f2fe1b63fb4c9693f37b64cda1907e87dba6
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

Ihr KI-Copilot für OpenSesame. Ihr 9 €/Monat-Abonnement unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, falls der Download nicht automatisch startet.
</div>


## Übersicht

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standard-Installationsoptionen

Die aktuelle $status$-Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows, keine Installation erforderlich (.zip)
</a>

Die meisten laden das `.exe`-Installationspaket herunter. Falls Sie keine Administratorrechte haben oder mehrere Versionen von OpenSesame parallel betreiben möchten, laden Sie stattdessen das `.zip`-Paket herunter.

Basiert auf Python 3.13 für 64-Bit-Systeme. Getestet unter Windows 11.

Manche externe Geräte wie [EyeLink](%url:eyelink%) und [Tobii](%url:tobii%) Eye-Tracker benötigen eine andere Python-Version. Weitere Informationen finden Sie auf den jeweiligen Dokumentationsseiten.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>

Bei der ersten Ausführung von OpenSesame wird die App vom Betriebssystem blockiert, da sie nicht von einem vertrauenswürdigen Entwickler stammt. Unter Einstellungen > Datenschutz & Sicherheit finden Sie danach die Option „Dennoch öffnen“. Diese erscheint, nachdem die App blockiert wurde.

Basiert auf Python 3.13 für 64-Bit-Intel-Systeme. Getestet auf Mac OS X Sequoia.

Manche externe Geräte wie [EyeLink](%url:eyelink%) und [Tobii](%url:tobii%) Eye-Tracker benötigen eine andere Python-Version. Weitere Informationen finden Sie auf den jeweiligen Dokumentationsseiten.


### Linux / Ubuntu

Kopieren Sie die folgenden Zeilen und fügen Sie sie in ein Terminal ein. Damit werden das Installationsskript heruntergeladen und ausgeführt.

```bash
# Diese Pakete müssen unter Ubuntu 24.04 installiert werden.
# Entsprechende Pakete müssen auf anderen
# Linux-Distributionen installiert werden.
sudo apt install curl python3-venv libxcb-cursor0
# Installationsskript für OpenSesame herunterladen und ausführen.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Getestet auf Ubuntu 24.04 (Python 3.12).


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi `opensesame-core` heißt.

OpenSesame-Core-Abhängigkeiten:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-)psycho-Backend. Abhängig vom Betriebssystem und der Python-Version kann es vorkommen, dass PsychoPy nicht korrekt installiert wird. In diesem Fall holen Sie sich Hilfe im Support-Forum oder nutzen Sie eines der vorgefertigten Pakete/Installationsprogramme.

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

Sobald Sie alle Pakete installiert haben, können Sie OpenSesame einfach durch Ausführen starten:

```bash
opensesame
```

Oder für Sigmund Analyst (Code-Editor):

```bash
sigmund-analyst
```


### Anaconda (plattformübergreifend)

Zuerst ein neues Python-Umfeld für OpenSesame erstellen (optional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Als Nächstes folge den obenstehenden Installationsanweisungen für PyPi. Spezielle Anaconda-Pakete werden nicht mehr bereitgestellt.


### Ältere Versionen von OpenSesame und andere Python-Versionen

Ältere Versionen von OpenSesame sowie Pakete, die mit anderen Python-Versionen (3.10, 3.11 und 3.12) erstellt wurden, sind auf GitHub Releases verfügbar:

- <https://github.com/open-cogsci/OpenSesame/releases>



### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version verwenden?

OpenSesame wird derzeit mit Python 3.13 gebaut und getestet. Andere Python-Versionen >=3.10 funktionieren ebenfalls, werden aber nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Das letzte Release, das ein Paket für Python 2 beinhaltete, war 3.3.12, das weiterhin im [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Aktualisiere während der Entwicklung und Testung deines Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisiere nicht während der Durchführung eines Experiments, also während du Daten erhebst.
- Führe ein Experiment immer mit derselben OpenSesame-Version durch, mit der du es entwickelt und getestet hast.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine gewöhnliche Python-Umgebung, und du kannst `pip install`-Befehle in der Jupyter-Konsole ausführen.


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Version, die auf 0 endet, z.B. 3.1.0), folgen in der Regel schnell ein oder zwei Wartungsversionen (z.B. 3.1.1 und 3.1.2), die wichtige Fehler beheben. Deshalb ist es ratsam, bei der Installation von OpenSesame auf selten aktualisierten Systemen bis zur zweiten oder dritten Wartungsversion zu warten (z.B. 3.0.2, 3.1.3 etc.). So minimierst du das Risiko, eine Version mit gravierenden Fehlern einzuführen.
- Der Windows-Installer ermöglicht eine stille Installation von OpenSesame mit dem `/S`-Flag.