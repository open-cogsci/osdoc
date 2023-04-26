title: Aus dem Quellcode ausführen
reviewed: false
hash: 97b9ccebc7a5b8f621d7724e6cf0a8a423800dd3861b85aaa93ff679ac90ded5
locale: de
language: German

Diese Seite beschreibt, wie Sie eine vollständige Python-Umgebung auf Ihrem Computer einrichten, um OpenSesame direkt aus dem Quellcode auszuführen.

[TOC]

## Quellcode herunterladen

Laden Sie den Quellcode der neuesten stabilen Version von GitHub herunter:

- <https://github.com/smathot/OpenSesame/releases>

Sie können auch einen Entwicklungsschnappschuss des Codes herunterladen. Um einen vernünftig stabilen Schnappschuss zu erhalten, laden Sie den `master` Zweig herunter. Um den neuesten, besten und möglicherweise sehr instabilen Schnappschuss zu erhalten, laden Sie den Zweig herunter, der der Hauptversion von OpenSesane entspricht (z. B. `heisenberg` für 2.9, `ising` für 3.0).

- <https://github.com/smathot/OpenSesame/>

## Abhängigkeiten

### Symbolthema

Wenn Sie OpenSesame direkt aus der Quelle ausführen, ist das Symbolthema nicht enthalten. OpenSesame verwendet zwei Symbolthemen: [MokaSesame](https://github.com/smathot/moka-icon-theme/tree/MokaSesame), ein Fork von Moka, und [Faba](https://github.com/snwh/faba-icon-theme).

Es ist möglich, diese Symbolthemen selbst zu kompilieren, aber Sie können auch vorab kompilierte Themen von hier herunterladen:

- http://forum.cogsci.nl/uploads/editor/we/p1y3i4qm70ch.zip

Legen Sie die Ordner `Faba` und `MokaSesame` als Unterordner von `opensesame_resources/theme/default/` ab.

### Erforderlich

Die folgenden Pakete sind erforderlich, um eine minimale Version der OpenSesame GUI auszuführen, jedoch nur mit Unterstützung für das [legacy] Backend, ohne Tonunterstützung und ohne Plugin-Unterstützung.

- [Python](http://www.python.org) ist die Programmiersprache, in der OpenSesame erstellt wird. Die folgenden Python-Versionen werden unterstützt:
	- Python 2.7 (Standard)
    - OpenSesame >= 3.0.0 unterstützt Python >= 3.4
- [PyGame](http://www.pygame.org) ist eine Bibliothek, die für Grafik und Ton verwendet wird.
- [qtpy](https://github.com/goanpeca/qtpy) ist die Abstraktionsschicht über PyQt4 oder PyQt5.
	- [PyQt4](http://www.riverbankcomputing.com/software/pyqt/download) ist das Grafik-Toolkit, das für die Benutzeroberfläche verwendet wird; oder
	- [PyQt5](http://www.riverbankcomputing.com/software/pyqt/download) ist das Grafik-Toolkit, das für die Benutzeroberfläche verwendet wird.
- [QScintilla2](http://www.riverbankcomputing.com/software/pyqt/download) ist eine grundlegende Text-Editor-Komponente. In einigen Fällen ist es in `PyQt4` enthalten.
- [QProgEdit](https://github.com/smathot/QProgEdit) ist eine erweiterte Text-Editor-Komponente auf Basis von `QScintilla2`.
	- OpenSesame >= 3.1.0 erfordert QProgEdit >= 4.0.0
- [PyYAML](http://pyyaml.org/) ist eine Bibliothek, die zum Laden von `yaml`-Dateien verwendet wird.
- [WebColors](https://pypi.python.org/pypi/webcolors) ist eine Bibliothek, die zur Interpretation von Farbbeschreibungen verwendet wird.
- [python-datamatrix](https://github.com/smathot/python-datamatrix) wird vom loop item verwendet.
- [python-qdatamatrix](https://github.com/smathot/python-qdatamatrix) wird vom loop item verwendet.
- [python-pseudorandom](https://github.com/smathot/python-pseudorandom) wird vom loop item verwendet.
- [QNotifications](https://github.com/dschreij/QNotifications) wird von der Notifications-Erweiterung verwendet.

### Optional

Die folgenden Pakete sind nicht erforderlich, aber einige Funktionen fehlen, wenn sie nicht installiert sind.

- [Expyriment](http://www.expyriment.org/) wird für das [xpyriment] Backend benötigt.
    - OpenSesame >= 3.0.0 erfordert Expyriment >= 0.8.0.
- [NumPy](http://www.numpy.org/) ist eine erweiterte mathematische Bibliothek, die für verschiedene Dinge verwendet wird, wie zum Beispiel die Unterstützung von Sound.
- [PIL](http://www.pythonware.com/products/pil/) ist eine Bildbibliothek, die für verschiedene Dinge verwendet wird.
    - Sie können auch `pillow` verwenden, einen aktiv gepflegten Fork des ursprünglichen, nicht mehr gepflegten `PIL`.
- [PsychoPy](http://www.psychopy.org/) wird für das [psycho] Backend benötigt.
- [pyflakes](https://pypi.python.org/pypi/pyflakes) wird benötigt, um Ihre Python-Skripte automatisch zu validieren.
- [Pyglet](http://www.pyglet.org/) wird von PsychoPy benötigt.
- [PyOpenGL](http://pyopengl.sourceforge.net/) wird von PsychoPy und Expyriment benötigt.
- [pySerial](http://pyserial.sourceforge.net/) wird benötigt, um die Kommunikation über die serielle Schnittstelle zu ermöglichen.
- [python-markdown](https://pypi.python.org/pypi/Markdown) wird benötigt, um In-Programm-Hilfsdateien anzeigen zu können.
- [IPython](http://ipython.org/) wird , sofern verfügbar, für das Debug-Fenster verwendet.
- [python-fileinspector](https://github.com/dschreij/fileinspector) wird verwendet, um Dateityp-spezifische Symbole zu generieren.
- [shapely](https://pypi.org/project/Shapely/) wird verwendet, um die Begrenzungen von `Canvas`-Elementen zu überprüfen.

### Extra

Die folgenden Pakete werden nicht direkt von OpenSesame verwendet, können aber bei der Entwicklung Ihrer Experimente nützlich sein und sind in der offiziellen Windows-Verteilung von OpenSesame enthalten.

- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/) ist eine alternative Bibliothek zur Aufzeichnung und Wiedergabe von Ton.
- [Matplotlib](http://matplotlib.org/) ist eine Bibliothek zum Zeichnen von Diagrammen.
- [Scipy](http://www.scipy.org/) ist eine Sammlung von wissenschaftlichen Routinen.
- [pyCairo](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo) ist eine Bibliothek für Vektorgrafiken.
- [pyParallel](http://sourceforge.net/projects/pyserial/files/pyparallel) ermöglicht die Kommunikation über die parallele Schnittstelle.
- [OpenCV](http://opencv.org/) (Python-Bindungen) ist eine umfangreiche Computer-Vision-Bibliothek.
- [PyGaze](http://www.pygaze.org/) ist eine Python-Bibliothek für Eyetracking.
    - OpenSesame >= 3.0.0 benötigt PyGaze >= 0.6.0.

## Anleitung für Mac OS

Es gibt drei Möglichkeiten, die Softwareumgebung für das Ausführen von OpenSesame aus dem Quellcode auf Mac OS X vorzubereiten. Sie können entweder alle erforderlichen Pakete manuell herunterladen und installieren, oder die erforderliche Quellumgebung erstellen, indem Sie die auf Repositorys basierenden Paketmanager MacPorts oder Homebrew verwenden. Die einfachste und bevorzugte Methode, um OpenSesame zum Laufen zu bringen, ist die Verwendung von Homebrew. Dieser Paketmanager arbeitet sehr schnell, verwaltet Abhängigkeitsanforderungen sehr gut und wird sehr gut gepflegt. Der andere Paketmanager, MacPorts, ist im Grunde genommen ein großes Repository, das den Quellcode von Programmen enthält, die von Linux auf Mac OS X portiert wurden (die sehr verwandt sind, da Mac OS X ebenfalls auf Unix basiert, wie Sie vielleicht wissen). Im Vergleich zu Homebrew dauert Macports jedoch erstaunlich lange, um alle Abhängigkeiten zu kompilieren. Darüber hinaus kommt es heute bei Macports aufgrund von Abhängigkeitsproblemen häufig zu „Brüchen“. Der Nachteil von Homebrew ist, dass es „weniger vollständig“ ist als Macports und Sie viele Python-Pakete manuell installieren müssen (mit easy_install oder pip).

### Xcode herunterladen

Wenn Sie mit Homebrew oder Macports installieren möchten, müssen Sie als erstes Xcode, das Apple-Entwicklertoolkit, installieren. Sie können die neueste Version von Xcode kostenlos im App Store oder auf deren Website herunterladen (Sie müssen sich jedoch mit einem Apple-Konto anmelden).

Website: <https://developer.apple.com/xcode/>

Die Verwendung des App Stores ist vorzuziehen, da der automatische Update Ihrer Xcode-Version gewährleistet wird. Sie müssen jedoch auch die Kommandozeilen-Tools für Xcode manuell installieren (und dies jedes Mal erneut tun, nachdem sie aktualisiert wurden).

### Installation mit Homebrew

Homebrew ist eine neuere und einfachere Möglichkeit, einen Quellbaum auf Ihrem Mac zu erstellen. Es hat viele Vorteile gegenüber macports, wie zum Beispiel Geschwindigkeit, und scheint heutzutage weniger Probleme beim Kompilieren und Aktualisieren von Paketen zu haben als macports.
Sie können homebrew wie auf <http://brew.sh/> angewiesen installieren. Geben Sie dann den folgenden Befehl ein, um zu beginnen:

    brew update
    brew doctor

Beheben Sie alle Probleme, die der 'doctor'-Befehl aufwirft. Dies sollte einfach sein und in der Regel werden die Lösungen (in Form von einfachen Befehlen) bereits zusammen mit der Problemstellung angegeben.

Fügen Sie als nächstes einige andere erforderliche Repositories hinzu, indem Sie den "tap"-Befehl von homebrew verwenden:

	brew tap homebrew/python
	brew tap homebrew/headonly
	brew tap homebrew/science

Jetzt ist es an der Zeit, die eigene Python-Umgebung von homebrew zu installieren. Es ist nicht wirklich notwendig, neben der Python-Umgebung Ihres Systems eine weitere Python-Umgebung zu installieren, aber die Homebrew-Version ist in der Regel neuer und besser gepflegt, daher ist es empfehlenswert, dies zu tun.

    brew install python

Nachdem Python installiert wurde, müssen Sie es zum 'Standard'-Python von OS X machen. Das bedeutet, dass der Python-Interpreter von Homebrew verwendet wird, wenn Sie den Befehl 'python' in einem Terminal eingeben, anstelle des Standard-System-Python. Um das zu tun, geben Sie den Befehl ein

    echo export PATH="/usr/local/bin:$PATH" >> ~/.bash_profile

Dies positioniert die Referenz auf den Ordner, in dem sich all Ihre Homebrew-Dinge befinden (/usr/local/bin), vor dem Rest der PATH-Variable. Von nun an sucht OS X bei jedem Befehl, den Sie in Ihrem Terminal eingeben, zuerst in diesem Ordner nach dem auszuführenden Skript oder Programm und falls es dort nicht gefunden wird, in den anderen Ordnern der PATH-Variable. Schließen und öffnen Sie Ihr Terminal erneut oder geben Sie den Befehl ein

	source ~/.bash_profile

um die Befehle in Ihrer .bash_profile erneut auszuführen. Wenn Sie anschließend den Befehl ausführen

    which python

sollte etwas wie '/usr/local/bin/python' ausgegeben werden. Wenn es immer noch '/usr/bin/python' ausgibt, verwendet OSX immer noch das Standard-System-Python, was nicht das ist, was Sie wollen. Sie können nun fortfahren mit der Installation der restlichen notwendigen Pakete, indem Sie ausführen

	brew install qt pyqt qscintilla2 freetype portaudio numpy scipy portmidi hg pillow

Für pygame ist es vorzuziehen, zuerst die SDL-Bibliotheken und smpeg zu installieren (alle besser als die Version, die mit OS X geliefert wurde und einige wichtige Funktionen zu verpassen scheinen):

	brew install --HEAD smpeg
	brew install sdl sdl_image sdl_mixer sdl_ttf pygame

Installieren Sie die notwendigen Python-Pakete

    pip install pyopengl pyflakes markdown python-bidi pyserial billiard

Installieren Sie QProgEdit (ab OpenSesame 2.8)

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	python setup.py install
	cd ..
	rm -R QProgEdit

Installieren Sie expyriment (ab OpenSesame 0.27)

    git clone https://github.com/expyriment/expyriment.git
	cd expyriment
	python setup.py install
	cd ..
	rm -R expyriment

Installieren Sie psychopy und seine Abhängigkeit pyglet. Damit psychopy funktioniert, benötigen Sie (derzeit) die neuesten Repository-Versionen von pyglet und psychopy

Zuerst pyglet installieren:

    hg clone https://code.google.com/p/pyglet/
	cd pyglet
	python setup.py install
	cd ..
	rm -R pyglet

Dann psychopy. Installieren Sie es und führen Sie etwas Aufräumarbeiten durch:

	git clone https://github.com/psychopy/psychopy.git
	cd psychopy
	python setup.py install
	cd ..
	rm -R psychopy

Während der Installation erhalten Sie möglicherweise einen Fehler mit der Meldung "Unknown locale UTF8". Sie können diesen leicht beheben, indem Sie die Zeile "LC_ALL=en_US.UTF8" in Ihre ~/.bash_profile einfügen und dann Ihr Terminal erneut öffnen.

Sie sollten nun in der Lage sein, OpenSesame auszuführen, aber Ihnen werden einige Symbole fehlen! Sie müssen das Faenza-Symbol-Theme von <http://tiheum.deviantart.com/art/Faenza-Icons-173323228> herunterladen und es unter resources/theme/default/ ablegen. Außerdem gibt es eine Eigenart, dass die Mehrprozessorfähigkeit nicht funktioniert, wenn die Hauptdatei nicht als .py-Datei vorhanden ist, was bei opensesame der Fall ist. Um die Unterstützung für Mehrprozessorverarbeitung zu aktivieren, müssen Sie die Datei opensesame in opensesame.py umbenennen. Wenn Sie nun ein Experiment einmal ausführen, sehen Sie, dass opensesame.pyc erstellt wurde. Ab dem Moment, in dem diese Datei vorhanden ist, verwendet Python die .pyc beim Starten neuer Prozesse und Sie können opensesame.py wieder in opensesame umbenennen. Dies ist eine seltsame Lösung, um die Mehrprozessorverarbeitung zum Laufen zu bringen, aber bisher ist es die einzige, die wir kennen.

Die folgenden Pakete sind optional, aber dennoch nützlich zu installieren:

	brew install matplotlib opencv
	pip install pycairo pyparallel scikit-image

### Installation mit MacPorts

Ein anderer Weg, die notwendigen Pakete auf Mac OS zu installieren, ist die Verwendung von MacPorts, einem großen Repository von Paketen. Es dauert sehr lange (und damit meine ich viele Stunden!), alle für das Ausführen von OpenSesame erforderlichen Pakete zu installieren, da MacPorts durch Kompilieren aus Quellen arbeitet. Aber auf der positiven Seite ist es ein ziemlich unkomplizierter Prozess.

#### MacPorts herunterladen

Sie können MacPorts von seiner Website herunterladen, auf der Sie auch die notwendige Dokumentation und einen Katalog aller verfügbaren Pakete finden.

Website: <http://www.macports.org/install.php>

Sie können +universal zu Ihrer /opt/local/etc/macports/variants.conf hinzufügen, um MacPorts dazu aufzufordern, alle Ports, die Sie installieren, mit dieser Variante zu bauen (also 32-Bit- und 64-Bit-Versionen im selben Modul), ohne sich daran erinnern zu müssen, dies bei jedem Installationsbefehl einzugeben. Einige Ports wurden jedoch noch nicht als universelle Binärdateien getestet und funktionieren möglicherweise nicht ordnungsgemäß.

#### Abhängigkeiten installieren

Im Grunde können Sie nun alle erforderlichen Pakete mit einem einzigen Befehl in einem Terminal installieren:

	sudo port install py27-game py27-pyqt4 py27-scintilla py27-serial py27-pil py27-opengl py27-pyaudio opencv +python27 py27-pip

Dies dauert ewig und ist in meinem Fall einige Male mit einem Prüfsummenfehler abgestürzt. Sie können sich einfach von solchen Fehlern erholen, indem Sie den folgenden Befehl ausführen:

	sudo port clean --all [Paket_mit_dem_Fehler]

Wiederholen Sie dann den ersten Befehl und MacPorts sollte wieder auf dem richtigen Weg sein.

Installieren Sie die restlichen notwendigen Python-Pakete mit pip

    sudo pip install pyflakes markdown python-bidi pyserial billiard

Installieren Sie QProgEdit (der Standard-Code-Editor ab OpenSesame 2.8):

    git clone https://github.com/smathot/QProgEdit.git
	cd QProgEdit
	sudo python setup.py install
	cd ..
	rm -R QProgEdit

#### Expyriment und Psychopy Backends

Neben dem Legacy-Backend, das auf pygame basiert, bietet OpenSesame Ihnen auch die Möglichkeit, Expyriment oder Psychopy zu verwenden. Im Gegensatz zum Legacy-Backend sind beide Backends hardwarebeschleunigt (OpenGL) und sollten eine höhere Timing-Genauigkeit bieten.

Installieren Sie Expyriment (ab OpenSesame 0.27):

    git clone https://github.com/expyriment/expyriment.git
    cd expyriment
    sudo python setup.py install
    cd ..
    rm -R expyriment

Installieren Sie Psychopy und seine Abhängigkeit pyglet:

Installieren Sie zuerst pyglet:

    hg clone https://code.google.com/p/pyglet/
    cd pyglet
    sudo python setup.py install
    cd ..
    rm -R pyglet

Installieren Sie dann Psychopy:

    git clone https://github.com/psychopy/psychopy.git
    cd psychopy
    python setup.py install
    cd ..
    rm -R psychopy

PsychoPy weigert sich, ohne die wxPython-Bibliothek zu laufen (was seltsam ist, weil OpenSesame keines der wx-GUI-Komponenten von Psychopy verwendet). Installieren Sie daher als letzten Schritt wxPython mit:

	sudo port install py27-wxpython-dev

#### Machen Sie Python von MacPorts zum Standard-Python

Mac OS wird mit einer benutzerdefinierten Version von Python ausgeliefert, aber für unsere Zwecke (und viele andere) benötigen Sie die offizielle Python-Version. Dies ist bereits von MacPorts installiert, aber Sie müssen es noch als Standard festlegen. Sie können dies mit dem folgenden Befehl tun:

	sudo port select --set python python27

### Pakete manuell installieren

Wenn Sie alle Abhängigkeiten von Opensesame selbst installieren möchten, müssen Sie die folgenden Paketverteilungen herunterladen und installieren:

#### Installieren Sie Python

Die Python-Installation, die mit OS X geliefert wird, ist normalerweise eine ältere Version. Daher ist es besser, die neueste Version von python.org herunterzuladen:

Website: <http://www.python.org/>

Direkter Download: http://www.python.org/ftp/python/2.7.3/python-2.7.3-macosx10.6.dmg

Eine andere Möglichkeit ist die Installation der [Enthought Python Distribution (EPD)][EPD_Download]. Diese Vertriebsversion enthält Python und viele der Module, von denen OpenSesame abhängt ([anschauen][EPD_Packages] eine vollständige Liste).

#### Installieren Sie PyGame

Website: <http://www.pygame.org/>

Direkter Download (Snow Leopard): <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.6-macosx10.6.mpkg.zip><br/>
Direkter Download ((Mountain) Lion): <http://www.pygame.org/ftp/pygame-1.9.2pre-py2.7-macosx10.7.mpkg.zip>

#### Installieren Sie PyQt4

Es gibt keine offizielle Distribution (von Riverbank) von PyQt4 für Mac OS X. Es gibt jedoch einige gut gepflegte inoffizielle Distributionen:

Offizielle Website: <http://www.riverbankcomputing.co.uk/software/pyqt/intro>

Mac OS X Vertrieb (PyQtX) Webseite: <http://sourceforge.net/projects/pyqtx/> (Direkter Download: <http://sourceforge.net/projects/pyqtx/files/latest/download>)


Nachdem PyQt4 installiert ist, laden Sie das QScintilla-Modul herunter und installieren Sie es, das in OpenSesame für den Inline-Skripteditor verwendet wird:

PyQScintillaX: <http://sourceforge.net/projects/pyqtx/files/PyQScintillaX/>

#### Installieren Sie NumPy und SciPy

Die neuesten Versionen von NumPy oder SciPy können auf zwei Arten bezogen werden:

Sie können das Installationsskript verwenden, das unter <http://fonnesbeck.github.com/ScipySuperpack/> zu finden ist (Direkter Download: <https://raw.github.com/fonnesbeck/ScipySuperpack/master/install_superpack.sh>)
und die Anweisungen, wie man es benutzt. Dieses Skript findet automatisch die neuesten Versionen von numpy und scipy und installiert sie für Sie. Im Grunde genommen müssen Sie nur ausführen

	sudo sh ./install_superpack.sh

in der Konsole im Ordner, in dem Sie das Skript heruntergeladen haben.

Alternativ können Sie die Pakete von den eigenen Websites der Projekte herunterladen und installieren:

Numpy: <http://sourceforge.net/projects/numpy/files/NumPy/> (Direkter Download Version 1.7.0: <http://sourceforge.net/projects/numpy/files/NumPy/1.7.0/numpy-1.7.0-py2.7-python.org-macosx10.6.dmg/download>)
Scipy: <http://sourceforge.net/projects/scipy/files/scipy/> (Direkter Download Version 0.11.0: <http://sourceforge.net/projects/scipy/files/scipy/0.11.0/scipy-0.11.0-py2.7-python.org-macosx10.6.dmg/download>)

#### Installieren Sie PsychoPy und Expyriment(optional)

PsychoPy erfordert die Installation einer Reihe von Abhängigkeiten. Die meisten davon können mit setuptools recht einfach installiert werden.

Website: <http://pypi.python.org/pypi/setuptools>

Direkter Download: <http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea>

Wie auf der Website beschrieben, sollten folgende Schritte für die Installation erfolgen:

Laden Sie das passende Ei für Ihre Python-Version herunter (z.B. setuptools-0.6c9-py2.7.egg). Benennen Sie es NICHT um.

Führen Sie es aus, als wäre es ein Shell-Skript, z.B.

	sh setuptools-0.6c9-py2.7.egg

Setuptools wird sich selbst mit der passenden Python-Version installieren (z.B. python2.7) und das easy_install-Programm an dem Standardort für die Installation von Python-Skripten platzieren (wie in den Standard-Distutils-Konfigurationsdateien oder der Python-Installation festgelegt).
Installieren Sie danach die meisten Abhängigkeiten mit dem Befehl:

	sudo easy_install psychopy pyglet pyopengl pil expyriment

Möglicherweise müssen Sie Matplotlib und wxPython manuell installieren, da diese bei Tests nicht mit easy_install installiert wurden. Stellen Sie sicher, dass Sie die Versionen installieren, die zu Ihrer Python-Version passen.

*HINWEIS:* Das psychopy Backend scheint noch nicht zu funktionieren und stürzt ab. Der Grund dafür ist, dass PsychoPy (bzw. seine zugrundeliegende Bibliothek pyglet) noch nicht mit der 64-Bit-Cocoa-Umgebung der neueren Mac OS X-Versionen zurechtkommt. In neueren Versionen von psychopy sollte dieses Problem hoffentlich behoben sein.

#### Installieren Sie wxPython (Optional, erforderlich für das PsychoPy-Backend)

Sie können wxPython selbst herunterladen oder mit easy_install installieren (siehe "PsychoPy installieren").

Website: <http://wxpython.org/>

Direkter Download: <http://downloads.sourceforge.net/wxpython/wxPython2.9-osx-2.9.4.0-cocoa-py2.7.dmg>

#### Installieren Sie PyOpenGL (Optional, erforderlich für das opengl oder expyriment Backend)

Sie können PyOpenGL selbst herunterladen oder mit easy_install installieren (siehe "PsychoPy installieren").

Website: <http://pyopengl.sourceforge.net/>

Direkter Download: <https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-3.0.2.tar.gz#md5=77becc24ffc0a6b28030aa109ad7ff8b>

### OpenSesame ausführen

Laden Sie den Quellcode der neuesten OpenSesame-Version hier herunter. Extrahieren Sie die .tar.gz in Ihren Home-Ordner (jeder andere Ort funktioniert analog). Öffnen Sie ein Terminal und wechseln Sie zu dem Ort, an dem sich OpenSesame befindet (in diesem Beispiel wird davon ausgegangen, dass die Version 0.26 ist):

	cd /Users/[Ihr Benutzername]/opensesame-0.26

Führen Sie OpenSesame mit einem der folgenden Befehle aus:

	python opensesame
	python opensesame --debug

[winpython-basiertes Paket]: /getting-opensesame/running-with-python-portable/
[EPD_Download]: http://www.enthought.com/products/epd.php
[EPD_Packages]: http://www.enthought.com/products/epdlibraries.php
[xpyriment]: /backends/xpyriment
[legacy]: /backends/legacy
[psycho]: /backends/psycho
[cogsci.nl ppa]: https://launchpad.net/~smathot/+archive/cogscinl