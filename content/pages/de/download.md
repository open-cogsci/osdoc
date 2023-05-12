title: Herunterladen
hash: bb4581487a399790e873f0a07ab48b9c8592ed4061874de0b12d80d523c84678
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

<a role="button" class="btn btn-success btn-align-left" href="https://www.buymeacoffee.com/cogsci">
<span class="glyphicon glyphicon-heart" aria-hidden="true"></span>
Helfen Sie uns, konzentriert zu bleiben und kaufen Sie uns einen Kaffee!
</a>

Kaffee hält uns wach, damit wir kostenlose Software entwickeln und Ihre Fragen im Support-Forum beantworten können!

Klicken Sie <a id="click-here">hier</a>, wenn Ihr Download nicht startet.
</div>


## Übersicht

%--
toc:
 exclude: [Übersicht]
 mindepth: 2
 maxdepth: 3
--%


## Alle Downloadoptionen

Die aktuelle $status$ Version ist $version$ *$codename$*, veröffentlicht am $release-date$ ([Versionshinweise](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

Das Windows-Paket basiert auf Python 3.11 für 64-Bit-Systeme. Das Installations- und `.zip`-Paket sind identisch, mit Ausnahme der Installation. Die meisten Leute laden das Installationspaket herunter (grüner Button).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Standard</b> Windows-Installer (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Standard</b> Windows ohne Installation erforderlich (.zip)
</a>


### Mac OS

Derzeit gibt es keine Vorabversionen von OpenSesame 4.0 für Mac OS. Bitte verwenden Sie conda oder pip.
{: .page-notification}

[Dieser Artikel](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) auf der Mac OS-Support-Website erklärt, wie man die Sicherheitseinstellungen von Mac OS übersteuert, die standardmäßig verhindern, dass OpenSesame gestartet wird.

Das untenstehende Paket ist für Intel-Prozessoren entwickelt, läuft aber auch auf ARM (M1)-Prozessoren.

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 für Intel x64</b> Mac OS-Paket (.dmg)
</a>

Um OpenSesame mit [Homebrew](https://brew.sh/) zu installieren, führen Sie den folgenden Befehl in einem Terminal aus:

```bash
brew install --cask opensesame
```


### Ubuntu

Pakete werden auf Ubuntu 22.04 Jammy Jellyfish entwickelt und getestet. Pakete sind nur für 22.04 und 22.10 verfügbar.

Wenn Sie OpenSesame 3.X installiert haben, deinstallieren Sie zuerst alle Pakete. Dies ist erforderlich, um Paketkonflikte aufgrund von leichten Umbenennungen einiger Pakete in OpenSesame 4.0 zu vermeiden.

```bash
# Falls erforderlich: Deinstallieren Sie OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Fügen Sie anschließend die erforderlichen Repositories zu Ihren Softwarequellen hinzu und installieren Sie OpenSesame (und Rapunzel), indem Sie die folgenden Befehle in einem Terminal ausführen:

```bash
# Repository für stabile Pakete hinzufügen
sudo add-apt-repository ppa:smathot/cogscinl
# Repository für Entwicklerpakete hinzufügen
sudo add-apt-repository ppa:smathot/milgram
# Installieren Sie OpenSesame 4.X-Pakete sowie nützliche Erweiterungen
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Einige häufig verwendete Pakete sind nicht über das PPA verfügbar. Sie können sie über `pip` installieren:

```bash
# Installieren Sie optionale Pakete, die nur über pip verfügbar sind
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy wird am besten über pip installiert, da das Ubuntu-Paket derzeit defekt ist.

```bash
# Installieren Sie PsychoPy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (plattformübergreifend)

Alle Pakete können über pip installiert werden. Beachten Sie, dass OpenSesame auf PyPi unter `opensesame-core` aufgeführt ist.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Nachdem alle Pakete installiert wurden, können Sie OpenSesame einfach ausführen, indem Sie (nachdem die korrekte Umgebung aktiviert wurde) folgendes eingeben:

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

Fügen Sie dann die relevanten Kanäle (`cogsci`) und (`conda-forge`) hinzu und installieren Sie alle relevanten Pakete. Stellen Sie sicher, dass `pyqode.core` und `pyqode.python` vom `cogsci`-Kanal stammen und >= 3.2 sind, und nicht die älteren Versionen vom `conda-forge`-Kanal.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Einige Pakete sind nicht über conda verfügbar. Sie können `pip install` für diese Pakete verwenden.

```bash
pip install soundfile pygame psychopy psychopy-sounddevice http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

Nachdem alle Pakete installiert wurden, können Sie OpenSesame einfach ausführen, indem Sie (nachdem die korrekte Umgebung aktiviert wurde) folgendes eingeben:

```bash
opensesame
```

Oder für den Rapunzel-Code-Editor:

```bash
rapunzel
```


### Ältere Versionen

Ältere Versionen können von GitHub-Releases heruntergeladen werden:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Quellcode

Der Quellcode von OpenSesame ist auf [GitHub](https://github.com/open-cogsci/OpenSesame) verfügbar.


## Tipps


### Welche Python-Version verwenden?

OpenSesame wird derzeit mit Python 3.11.0 erstellt und getestet. Andere Python-Versionen >=3.7 funktionieren, werden jedoch nicht ausführlich getestet. Python 2 wird nicht mehr unterstützt. Die letzte Veröffentlichung, die ein Python 2-Paket enthielt, war 3.3.12, das im [Release-Archiv](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12) noch heruntergeladen werden kann.


### Wann (nicht) aktualisieren?

- Aktualisieren Sie während der Entwicklung und Tests Ihres Experiments; es ist immer am besten, die neueste Version von OpenSesame zu verwenden.
- Aktualisieren Sie nicht während der Durchführung eines Experiments; das heißt, aktualisieren Sie nicht, während Sie Daten erfassen.
- Führen Sie ein Experiment mit derselben Version von OpenSesame durch, die Sie für die Entwicklung und Tests verwendet haben.


### Manuelle Aktualisierung von Paketen

OpenSesame ist eine reguläre Python-Umgebung, und Sie können Pakete mit `pip` oder `conda` aktualisieren, wie hier beschrieben:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Tipps für Systemadministratoren

- Wenn eine neue Hauptversion von OpenSesame veröffentlicht wird (mit einer Versionsnummer, die auf 0 endet, z.B. 3.1.0), wird sie in der Regel schnell von ein oder zwei Wartungsreleases (z.B. 3.1.1 und 3.1.2) gefolgt, die größere Fehler beheben. Wenn Sie OpenSesame also auf Systemen installieren, die Sie nicht oft aktualisieren, ist es am besten, bis zum zweiten oder dritten Wartungsrelease (z.B. 3.0.2, 3.1.3 usw.) zu warten. Auf diese Weise minimieren Sie das Risiko, eine Version von OpenSesame mit größeren Fehlern auszurollen.
- Der Windows-Installer ermöglicht eine stille Installation von OpenSesame mit der `/S`-Option.
