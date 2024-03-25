title: Herunterladen
hash: c3287b768243f4d57f2068746ebea3538a3441372f6a29ed902c5fe1429fa59e
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

Besser als ChatGPT für OpenSesame Fragen. Ihr Abonnement für 9 €/Monat unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, wenn Ihr Download nicht startet.
</div>


## Übersicht

## Alle Downloadoptionen

Die neueste $status$ Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.11 für 64-Bit-Systeme. Das Installations- und `.zip`-Paket sind identisch, abgesehen von der Installation. Die meisten Leute laden das Installationspaket herunter (grüner Knopf).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installationsprogramm (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows-Paket ohne Installation (.zip)
</a>


### Mac OS

[Dieser Artikel](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) auf der Mac OS Supportseite erklärt, wie Sie die Sicherheitseinstellungen von Mac OS umgehen können, die standardmäßig verhindern, dass OpenSesame gestartet wird. Das erste Mal, wenn Sie OpenSesame starten, dauert es sehr lange, bis die Anwendung startet; bei späteren Starts geht es viel schneller.

Das untenstehende Paket ist für Intel-Prozessoren gebaut, läuft aber auch auf ARM (M1) Prozessoren.

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 für Intel x64</b> Mac OS-Paket (.dmg)
</a>

Um OpenSesame mit [Homebrew](https://brew.sh/) zu installieren, führen Sie den folgenden Befehl in einem Terminal aus:

```bash
brew install --cask opensesame
```


### Ubuntu

Pakete werden entwickelt und getestet auf Ubuntu 22.04 Jammy Jellyfish. Pakete sind nur für 22.04 und 22.10 verfügbar.

Wenn Sie OpenSesame 3.X installiert haben, deinstallieren Sie zuerst alle Pakete. Dies ist notwendig, um Paketkonflikte durch geringfügige Umbenennungen einiger Pakete in OpenSesame 4.0 zu vermeiden.

```bash
# Falls nötig: Deinstallieren Sie OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Fügen Sie anschließend die erforderlichen Repositories zu Ihren Softwarequellen hinzu und installieren Sie OpenSesame (und Rapunzel), indem Sie die folgenden Befehle in einem Terminal ausführen:

```bash
# Repository für stabile Pakete hinzufügen
sudo add-apt-repository ppa:smathot/cogscinl
# Repository für Entwicklerpakete hinzufügen
sudo add-apt-repository ppa:smathot/milgram
# Installieren Sie OpenSesame 4.X Pakete plus nützliche Erweiterungen
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Einige häufig verwendete Pakete sind nicht über das PPA erhältlich. Sie können sie über `pip` installieren:

```bash
# Installieren Sie optionale Pakete, die nur über pip verfügbar sind
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy wird am besten über pip installiert, da das Ubuntu-Paket derzeit defekt ist.

```bash
# Installieren Sie psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (plattformübergreifend)

Alle Pakete können mit pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi als `opensesame-core` bezeichnet wird.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie (nachdem Sie die richtige Umgebung aktiviert haben) Folgendes ausführen:

```bash
opensesame
```

Oder für den Rapunzel-Code-Editor:

```bash
rapunzel
```


### Anaconda (plattformübergreifend)

Erstellen Sie zuerst eine neue Python-Umgebung für OpenSesame (optional):

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Fügen Sie anschließend die relevanten Kanäle (`cogsci`) und (`conda-forge`) hinzu und installieren Sie alle relevanten Pakete. Stellen Sie sicher, dass `pyqode.core` und `pyqode.python` >= 3.2 aus dem Kanal `cogsci` und nicht die älteren Versionen aus dem Kanal `conda-forge` sind.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Einige Pakete sind nicht über conda verfügbar. Für diese können Sie `pip install` verwenden. (PsychoPy ist bekannt dafür, dass es bei einigen Systemen fehlschlägt, weshalb es unten separat installiert wird.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie (nachdem Sie die richtige Umgebung aktiviert haben) Folgendes ausführen:

```bash
opensesame
```

Oder für den Rapunzel-Code-Editor:

```bash
rapunzel
```


### Ältere Versionen

Ältere Versionen können von den GitHub-Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Version von Python verwenden?

OpenSesame wird derzeit mit Python 3.11 gebaut und getestet. Andere Versionen von Python >=3.7 funktionieren, werden aber nicht ausführlich getestet. Python 2 wird nicht mehr unterstützt. Die letzte Veröffentlichung, die ein Python-2-Paket enthielt, war 3.3.12, die noch immer im [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und des Testens Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während der Durchführung eines Experiments; das heißt, aktualisieren Sie nicht, während Sie Daten sammeln.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, die Sie zum Entwickeln und Testen verwendet haben.


### Pakete manuell aktualisieren

OpenSesame ist eine reguläre Python-Umgebung, und Sie können Pakete mit `pip` oder `conda` aktualisieren, wie hier beschrieben:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Version, die auf 0 endet, z. B. 3.1.0), folgt in der Regel schnell ein oder zwei Wartungsfreigaben (z. B. 3.1.1 und 3.1.2), die größere Fehler beheben. Wenn Sie OpenSesame also auf Systemen installieren, die Sie nicht oft aktualisieren, ist es am besten, bis zur zweiten oder dritten Wartungsfreigabe (z. B. 3.0.2, 3.1.3 usw.) zu warten. Auf diese Weise minimieren Sie das Risiko, eine Version von OpenSesame mit größeren Fehlern auszurollen.
- Das Windows-Installationsprogramm ermöglicht es Ihnen, OpenSesame still mit dem Flag `/S` zu installieren.