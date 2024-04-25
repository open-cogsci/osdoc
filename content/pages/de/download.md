title: Herunterladen
hash: fd00279bec39b52c5cf277e973c6f314758b571714fbc3b1fb8730ac172aa061
locale: de
language: German

```html
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

Besser als ChatGPT für OpenSesame-Fragen. Ihr Abonnement für 9 €/Monat unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, wenn Ihr Download nicht startet.
</div>


## Übersicht

## Alle Download-Optionen

Die neueste $status$ Version ist $version$ *$codename$* ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.11 für 64-Bit-Systeme. Das Installationspaket und das `.zip`-Paket sind identisch, mit Ausnahme der Installation. Die meisten Leute laden das Installationspaket herunter (grüner Button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installationsprogramm (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows ohne Installation erforderlich (.zip)
</a>


### Mac OS

[Dieser Artikel](https://support.apple.com/de-de/guide/mac-help/mh40616/mac) auf der Support-Website von Mac OS erklärt, wie Sie die Sicherheitseinstellungen von Mac OS überschreiben können, die standardmäßig verhindern, dass OpenSesame gestartet wird. Das erste Mal, dass Sie OpenSesame starten, dauert es sehr lange, bis die Anwendung startet; spätere Starts sind viel schneller.

Das untenstehende Paket ist für Intel-Prozessoren gebaut, läuft aber auch auf ARM (M1) Prozessoren.

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 für Intel x64</b> Mac OS-Paket (.dmg)
</a>

Um OpenSesame mit [Homebrew](https://brew.sh/) zu installieren, führen Sie den folgenden Befehl in einem Terminal aus:

```bash
brew install --cask opensesame
```


### Ubuntu

Pakete werden für Ubuntu 22.04 Jammy Jellyfish entwickelt und getestet. Pakete sind nur für 22.04 und 22.10 verfügbar.

Wenn Sie OpenSesame 3.X installiert haben, deinstallieren Sie zuerst alle Pakete. Dies ist erforderlich, um Paketkonflikte aufgrund einer geringfügigen Umbenennung einiger Pakete in OpenSesame 4.0 zu vermeiden.

```bash
# Wenn nötig: Deinstallieren von OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Anschließend fügen Sie die erforderlichen Repositories zu Ihren Softwarequellen hinzu und installieren OpenSesame (und Rapunzel), indem Sie die folgenden Befehle in einem Terminal ausführen:

```bash
# Repository für stabile Pakete hinzufügen
sudo add-apt-repository ppa:smathot/cogscinl
# Repository für Entwicklungs-Pakete hinzufügen
sudo add-apt-repository ppa:smathot/milgram
# OpenSesame 4.X Pakete plus nützliche Erweiterungen installieren
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Einige häufig verwendete Pakete sind nicht über das PPA verfügbar. Sie können sie über `pip` installieren:

```bash
# Optionale Pakete installieren, die nur über pip verfügbar sind
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy wird am besten über pip installiert, da das Ubuntu-Paket derzeit defekt ist.

```bash
# Psychopy installieren
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (plattformübergreifend)

Alle Pakete können via pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi als `opensesame-core` bezeichnet wird.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Sobald Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie (nachdem Sie die richtige Umgebung aktiviert haben) folgendes ausführen:

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

Fügen Sie dann die relevanten Kanäle (`cogsci`) und (`conda-forge`) hinzu und installieren Sie alle relevanten Pakete. Stellen Sie sicher, dass `pyqode.core` und `pyqode.python` >= 3.2 vom `cogsci` Kanal sind und nicht die älteren Versionen vom `conda-forge` Kanal.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Einige Pakete sind nicht über conda verfügbar. Sie können diese mit `pip install` installieren. (Es ist bekannt, dass PsychoPy auf einigen Systemen nicht installiert werden kann, weshalb es unten separat installiert wird.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Sobald Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie (nachdem Sie die richtige Umgebung aktiviert haben) folgendes ausführen:

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

OpenSesame wird derzeit mit Python 3.11 gebaut und getestet. Andere Versionen von Python >=3.7 funktionieren ebenfalls, sind aber nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Veröffentlichung, die ein Python-2-Paket enthielt, war 3.3.12, welches immer noch im [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie, während Sie Ihr Experiment entwickeln und testen; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während der Durchführung eines Experiments; das heißt, aktualisieren Sie nicht, während Sie Daten sammeln.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, die Sie auch für Entwicklung und Test verwendet haben.


### Pakete manuell aktualisieren

OpenSesame ist eine reguläre Python-Umgebung, und Sie können Pakete mit `pip` oder `conda` aktualisieren, wie hier beschrieben:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Version, die auf 0 endet, z.B. 3.1.0), wird diese in der Regel schnell von ein oder zwei Wartungsversionen (z.B. 3.1.1 und 3.1.2) gefolgt, die größere Fehler beheben. Wenn Sie OpenSesame auf Systemen installieren, die Sie nicht häufig aktualisieren, ist es am besten, bis zur zweiten oder dritten Wartungsversion (z.B. 3.0.2, 3.1.3 usw.) zu warten. So minimieren Sie das Risiko, eine Version von OpenSesame auszurollen, die größere Fehler enthält.
- Der Windows-Installer ermöglicht es Ihnen, OpenSesame stillschweigend mit dem `/S`-Flag zu installieren.
