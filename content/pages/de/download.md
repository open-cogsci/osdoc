title: Herunterladen
hash: 48b36f28d46849599cac6b02aa148d9b70d6476758c8b21e016736aed881ea59
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

Besser als ChatGPT für OpenSesame-Fragen. Ihr 9€/Monat-Abonnement unterstützt OpenSesame.

Klicken Sie <a id="click-here">hier</a>, falls Ihr Download nicht startet.
</div>


## Übersicht

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Alle Download-Optionen

Die neueste $status$ Version ist $version$ *$codename$* ([Release Notes](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.11 für 64-Bit-Systeme. Der Installer und die `.zip` Pakete sind identisch, abgesehen von der Installation. Die meisten Leute laden das Installer-Paket (grüner Knopf) herunter.

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows keine Installation erforderlich (.zip)
</a>


### Mac OS

[Dieser Artikel](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) auf der Mac OS Support-Seite erklärt, wie man die Sicherheitseinstellungen von Mac OS überschreibt, die standardmäßig verhindern, dass OpenSesame startet. Das erste Mal, wenn Sie OpenSesame starten, wird es sehr lange dauern, bis die Anwendung startet; nachfolgende Starts gehen viel schneller.

Das nachfolgende Paket ist für Intel-Prozessoren gebaut, läuft aber auch auf ARM (M1) Prozessoren.

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 für Intel x64</b> Mac OS Paket (.dmg)
</a>

Um OpenSesame mit [Homebrew](https://brew.sh/) zu installieren, führen Sie den folgenden Befehl in einem Terminal aus:

```bash
brew install --cask opensesame
```


### Ubuntu

Pakete werden auf Ubuntu 24.04 Jammy Jellyfish entwickelt und getestet. Ihre Erfahrungen können bei anderen Versionen von Ubuntu variieren.

Wenn Sie OpenSesame 3.X installiert haben, deinstallieren Sie zuerst alle Pakete. Dies ist erforderlich, um Paketkonflikte aufgrund der leichten Umbenennung einiger Pakete in OpenSesame 4.0 zu vermeiden.

```bash
# Falls erforderlich: OpenSesame 3.X deinstallieren
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Als nächstes fügen Sie die erforderlichen Repositories zu Ihren Software-Quellen hinzu und installieren OpenSesame (und Rapunzel), indem Sie die folgenden Befehle in einem Terminal ausführen:

```bash
# Repository für stabile Pakete hinzufügen
sudo add-apt-repository ppa:smathot/cogscinl
# Repository für Entwicklungspakete hinzufügen
sudo add-apt-repository ppa:smathot/milgram
# OpenSesame 4.X Pakete plus nützliche Erweiterungen installieren
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Einige häufig verwendete Pakete sind nicht über das PPA verfügbar. Sie können sie über `pip` installieren:

```bash
# Optionale Pakete installieren, die nur über pip verfügbar sind
pip install --break-system-packages --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy wird am besten über pip installiert, da das Ubuntu-Paket derzeit defekt ist.

```bash
# Zuerst installieren Sie eine benutzerdefinierte Version von wxPython, die für PsychoPy erforderlich ist
pip install --break-system-packages https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04/wxPython-4.2.2-cp312-cp312-linux_x86_64.whl
# Installieren Sie anschließend psychopy und ignorieren Sie die Anforderung für Python <=3.11, da Ubuntu 24.04 Python 3.12 verwendet
pip install --break-system-packages --ignore-requires-python psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (plattformübergreifend)

Alle Pakete können per pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi `opensesame-core` genannt wird.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Möglicherweise müssen Sie auch PyQt5 und QtWebEngine installieren, die das GUI-Toolkit bereitstellen:

```bash
pip install pyqt5 pyqtwebengine
```

Nachdem Sie alle Pakete installiert haben, können Sie OpenSesame einfach starten, indem Sie (nachdem Sie die richtige Umgebung aktiviert haben) folgendes ausführen:

```bash
opensesame
```

Oder für den Rapunzel-Code-Editor:

```bash
rapunzel
```


### Anaconda (plattformübergreifend)

Erstellen Sie zunächst eine neue Python-Umgebung für OpenSesame (optional):

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Fügen Sie dann die relevanten Kanäle (`cogsci`) und (`conda-forge`) hinzu und installieren Sie alle relevanten Pakete. Stellen Sie sicher, dass `pyqode.core` und `pyqode.python` >= 3.2 aus dem `cogsci`-Kanal stammen und nicht die älteren Versionen aus dem `conda-forge`-Kanal.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Einige Pakete sind nicht über conda verfügbar. Sie können `pip install` für diese verwenden. (Es ist bekannt, dass PsychoPy auf einigen Systemen nicht installiert werden kann, weshalb es separat unten installiert wird.)

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Sobald Sie alle Pakete installiert haben, können Sie OpenSesame einfach ausführen, indem Sie (nachdem Sie die richtige Umgebung aktiviert haben) folgendes ausführen:

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

OpenSesame wird derzeit mit Python 3.11 entwickelt und getestet. Andere Versionen von Python >=3.7 funktionieren, sind jedoch nicht umfassend getestet. Python 2 wird nicht mehr unterstützt. Die letzte Veröffentlichung, die ein Python 2-Paket enthielt, war 3.3.12, die noch aus dem [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und Testung Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während der Durchführung eines Experiments; das heißt, aktualisieren Sie nicht, während Sie Daten sammeln.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, die Sie für die Entwicklung und Testung verwendet haben.


### Manuelles Aktualisieren von Paketen

OpenSesame ist eine reguläre Python-Umgebung und Sie können Pakete mit `pip` oder `conda` wie hier beschrieben aktualisieren:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Version, die auf 0 endet, z.B. 3.1.0), folgt darauf in der Regel schnell ein oder zwei Wartungsversionen (z.B. 3.1.1 und 3.1.2), die größere Fehler beheben. Daher ist es am besten, wenn Sie OpenSesame auf Systemen installieren, die Sie nicht häufig aktualisieren, bis zur zweiten oder dritten Wartungsversion zu warten (z.B. 3.0.2, 3.1.3, usw.). Auf diese Weise minimieren Sie das Risiko, eine Version von OpenSesame auszurollen, die signifikante Fehler enthält.
- Der Windows-Installer ermöglicht es Ihnen, OpenSesame mithilfe des `/S`-Flags still zu installieren.