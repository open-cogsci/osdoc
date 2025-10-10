title: Herunterladen
hash: 0057d1f73dae2a2590e1f0e03dfe7d984bdf6d67622188a9eb35e2cb08646b28
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

Ihr KI-Copilot für OpenSesame. Ihr Abonnement für 9 €/Monat unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, falls Ihr Download nicht automatisch startet.
</div>


## Überblick

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Standard-Installationsoptionen

Die aktuellste $status$ Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows, keine Installation erforderlich (.zip)
</a>

Die meisten Nutzer laden das `.exe`-Installationspaket herunter. Wenn Sie keine Administratorrechte haben oder mehrere Versionen von OpenSesame nebeneinander ausführen müssen, laden Sie stattdessen das `.zip`-Paket herunter.

Basierend auf Python 3.13 für 64-Bit-Systeme. Getestet unter Windows 11.

Einige externe Geräte, wie [EyeLink](%url:eyelink%) und [Tobii](%url:tobii%) Eye-Tracker, erfordern eine andere Python-Version. Weitere Informationen finden Sie auf den jeweiligen Dokumentationsseiten.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Mac OS-Paket (.dmg)
</a>

Wenn Sie OpenSesame zum ersten Mal starten, wird es vom Betriebssystem blockiert, da die App nicht von einem vertrauenswürdigen Entwickler stammt. Unter Einstellungen > Datenschutz & Sicherheit finden Sie die Option "Dennoch öffnen". Diese Option erscheint, nachdem die App blockiert wurde.

Basierend auf Python 3.13 für 64-Bit-Intel-Systeme. Getestet unter Mac OS X Sequoia.

Einige externe Geräte, wie [EyeLink](%url:eyelink%) und [Tobii](%url:tobii%) Eye-Tracker, erfordern eine andere Python-Version. Weitere Informationen finden Sie auf den jeweiligen Dokumentationsseiten.


### Linux / Ubuntu

Kopieren Sie die folgenden Zeilen in ein Terminal. Dadurch wird ein Installationsskript heruntergeladen und ausgeführt.

```bash
# Diese Pakete müssen unter Ubuntu 24.04 installiert sein.
# Entsprechende Pakete müssen unter anderen
# Linux-Distributionen installiert werden.
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# Installationsskript für OpenSesame herunterladen und ausführen
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Getestet unter Ubuntu 24.04 (Python 3.12).


## Erweiterte Installationsoptionen


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachten Sie, dass OpenSesame bei PyPi `opensesame-core` genannt wird.

OpenSesame Kerndependencies:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy für das (Standard-)Psycho-Backend. Je nach Betriebssystem und Python-Version kann es passieren, dass PsychoPy nicht korrekt installiert wird. In diesem Fall suchen Sie Hilfe im Support-Forum oder verwenden Sie eine der vorgefertigten Paketdateien bzw. Installer.

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

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie:

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