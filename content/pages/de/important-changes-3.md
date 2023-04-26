title: Wichtige Änderungen in OpenSesame 3
hash: 5ff5aa4ddc6076985d2733031a24955084f95edb98e5b60980505b16b020ae44
locale: de
language: German

[TOC]

## Änderungen in 3.3

OpenSesame 3.3 bietet mehrere wichtige Verbesserungen, die die experimentelle Entwicklung noch einfacher gestalten. OpenSesame 3.3 ist vollständig abwärtskompatibel zu 3.2.

### Rapunzel: Ein neuer Code-Editor

Rapunzel ist ein Code-Editor, der sich auf numerisches Rechnen mit Python und R konzentriert. Technisch gesehen handelt es sich bei Rapunzel um eine Reihe von Erweiterungen für OpenSesame. Es sieht aber aus und verhält sich wie ein eigenständiges Programm. Frohes Programmieren!

- <https://rapunzel.cogsci.nl/>


### Ein neuer Inline-Script-Editor

Im Zusammenhang mit der Entwicklung von Rapuznel: Das INLINE_SCRIPT-Element verwendet jetzt eine andere Bibliothek (`PyQode`) für den Code-Editor. Dadurch unterstützt der Code-Editor jetzt viele Funktionen, die Sie von einem modernen Code-Editor erwarten, dazu gehört Code-Introspektion und statische Codeprüfung.


### Weitere Farbräume

OpenSesame unterstützt jetzt nativ die HSV-, HSL- und CIElab-Farbräume.

- %link:manual/python/canvas%


### Neues Sound-Backend auf Basis von PsychoPy

Das Standard-Backend ist jetzt *psycho*. Ein Vorteil dieses Backends besteht darin, dass die Zeitsteuerung der Tonwiedergabe besser sein sollte. Wenn Sie Stottern (klickende Tonwiedergabe) feststellen, können Sie immer noch auf das *psycho_legacy*-Backend zurückgreifen, das das alte PyGame-basierte Soundsystem verwendet.

### Unterstützung für Inline-Script-Elemente in Coroutines

Sie können jetzt `inline_script`-Elemente in `coroutines` verwenden. Dies erleichtert die Kombination von Python-Scripting und Coroutines im Vergleich zur alten Methode, bei der eine benutzerdefinierte Generatorfunktion geschrieben wurde.

- %link:coroutines%



### OpenSesame:


## Änderungen in 3.2

OpenSesame 3.2 bietet mehrere wichtige Verbesserungen, die das experimentelle Design noch einfacher gestalten. OpenSesame 3.2 ist vollständig abwärtskompatibel zu 3.1.

### Eine bessere, PEP-8-konforme Python-API

PEP-8 ist eine Stilrichtlinie für Python. Viele moderne Python-Software folgt den PEP-8-Richtlinien - OpenSesame jedoch bisher nicht. Ab Version 3.2 folgt die öffentliche API der Richtlinie, dass die Namen von Klassen (und Factory-Funktionen, die Klassen generieren) in `CamelCase`, während Namen von Objekten und Funktionen in `underscore_case` geschrieben sein sollten. Praktisch bedeutet dies, dass Sie nun `Canvas`-Objekte wie folgt erstellen:

~~~ .python
my_canvas = Canvas() # Beachten Sie das große C!
my_canvas.fixdot()
my_canvas.show())
~~~

Natürlich sind die alten `underscore_case`-Namen weiterhin als Aliase verfügbar, sodass die Abwärtskompatibilität erhalten bleibt.

Die API für Formulare wurde ebenfalls vereinfacht. Sie müssen `libopensesame.widgets` nicht mehr importieren und die ersten Argumente nicht mehr `exp` übergeben:

~~~ .python
form = Form()
button = Button(text=u'Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~

### Verbesserungen am Sketchpad und Canvas

#### Zugriff und Änderung von Canvas-Elementen

Elemente eines `Canvas` sind jetzt Objekte, die benannt, aufgerufen und geändert werden können. Das bedeutet, dass Sie nicht mehr das gesamte Canvas neu zeichnen müssen, um ein einziges Element zu ändern. Zum Beispiel können Sie einen rotierenden Arm wie folgt zeichnen:

~~~ .python
my_canvas = Canvas()
my_canvas['arm'] = Line(0, 0, 0, 0)
for x, y in xy_circle(n=100, rho=100):
	my_canvas['arm'].ex = x
	my_canvas['arm'].ey = y
	my_canvas.show()
	clock.sleep(10)
~~~

Das SKETCHPAD ermöglicht es Ihnen auch, Elemente zu benennen.

Weitere Informationen finden Sie unter:

- %link:manual/python/canvas%


#### Verbesserte Unterstützung für HTML und Nicht-Latein-Schrift

Der Text wird jetzt von Qt gerendert, das ist eine moderne Bibliothek (die auch für die grafische Benutzeroberfläche verwendet wird). Das bedeutet, dass Sie jetzt wirkliches HTML in Ihrem Text verwenden können. Dies bedeutet auch, dass Schreibrichtungen von links nach rechts und andere Nicht-Latein-Schriftarten besser gerendert werden.

#### Bilder können gedreht werden

Bilder können jetzt gedreht werden. Diese funktioniert sowohl in SKETCHPAD-Elementen als auch in `Canvas`-Objekten.

#### Arbeiten mit Polarkoordinaten

Wenn Sie mit der rechten Maustaste auf ein SKETCHPAD-Element klicken, können Sie "Polarkoordinaten angeben" auswählen. Dadurch können Sie kartesische (x, y) Koordinaten auf der Grundlage von Polarkoordinaten berechnen, was besonders nützlich ist, wenn Sie kreisförmige Konfigurationen erstellen möchten.

### Verbesserungen bei Formularen

#### Verbesserte Formularleistung

Formulare sind jetzt viel schneller bei der Verwendung der *psycho* und *xpyriment* Backends. Dies liegt daran, dass `Canvas`-Elemente jetzt einzeln aktualisiert werden können, wie oben beschrieben.

#### Überprüfung von Formulareingaben

Sie können nun die Eingabe eines Formulars überprüfen; das heißt, Sie können verhindern, dass ein Formular geschlossen wird, bis bestimmte Kriterien erfüllt sind. Darüber hinaus können Sie Zeichen als Eingabe von `TextInput`-Widgets ausschließen.

Für weitere Informationen siehe:

- %link:manual/forms/validation%

### Verbesserungen bei der Tastatur

#### Unterstützung für Tastenfreigabeereignisse

Das `Keyboard()`-Objekt verfügt jetzt über eine `get_key_release()`-Funktion, mit der Sie Tastenfreigaben erfassen können. Aufgrund von Einschränkungen der zugrunde liegenden Bibliotheken hat die Funktion zwei wichtige Einschränkungen:

- Der zurückgegebene `key` kann bei nicht-QWERTY-Tastaturbelegungen falsch sein
- Die Funktion wurde für das *psycho* Backend nicht implementiert

Für weitere Informationen siehe:

- %link:manual/response/keyboard%

### Verbesserungen bei der Maus

#### Unterstützung für Mausfreigabeereignisse

Das `Mouse()`-Objekt verfügt jetzt über eine `get_click_release()`-Funktion, mit der Sie Mausklick-Freigaben erfassen können. Diese Funktion ist derzeit für das *psycho* Backend nicht implementiert.

Für weitere Informationen siehe:

- %link:manual/response/mouse%

#### Verwenden Sie Sketchpads, um Interessenregionen zu definieren

Sie können jetzt ein verknüpftes SKETCHPAD in einem `mouse_response`-Element definieren. Wenn Sie dies tun, werden die Namen der Elemente auf dem SKETCHPAD automatisch als Interessenregionen (ROIs) für die Mausklicks verwendet.

### Erzwingen Sie das Ende Ihres Experiments

Sie können Ihr Experiment jetzt durch Klicken auf die Schaltfläche "Kill" in der Hauptwerkzeugleiste erzwingen. Dies bedeutet, dass Sie keinen Prozess-/Task-Manager mehr öffnen müssen, um außer Kontrolle geratene Experimente zu beenden!

### Verbesserte Mac OS-Unterstützung

Die Mac OS-Pakete wurden von Grund auf von %-- github: {user: dschreij} --% neu erstellt. Die Mac OS-Erfahrung sollte nun viel reibungsloser, schneller und absturzsicherer sein.

### Eine türkische Übersetzung

Eine vollständige türkische Übersetzung wurde von %-- github: {user: aytackarabay} --% beigesteuert. Dies bedeutet, dass OpenSesame jetzt vollständig in Französisch, Deutsch und Türkisch übersetzt ist. Eine teilweise Übersetzung ist in mehreren anderen Sprachen verfügbar.

## Änderungen in 3.1

OpenSesame 3.1 bringt viele Verbesserungen, die es noch einfacher machen, Experimente zu entwickeln. OpenSesame 3.1 ist vollständig abwärtskompatibel mit 3.0.

### Ein neuer Look!

OpenSesame hat ein neues Icon-Theme, basierend auf [Moka](https://snwh.org/moka) von Sam Hewitt. Darüber hinaus wurde die Benutzeroberfläche anhand konsistenter Human-Interface-Richtlinien neu gestaltet. Wir hoffen, dass Ihnen der neue Look genauso gut gefällt wie uns!

### Eine neu gestaltete Schleife

Die LOOP ist jetzt einfacher zu bedienen und ermöglicht die Einschränkung der Randomisierung; dies macht es zum Beispiel möglich, zu verhindern, dass der gleiche Reiz zweimal hintereinander auftritt.

Für weitere Informationen siehe:

- %link:loop%

### Coroutinen: Dinge parallel machen

Das COROUTINES-Plugin ist jetzt standardmäßig enthalten. COROUTINES ermöglicht es Ihnen, mehrere andere Elemente parallel auszuführen; dies macht es zum Beispiel möglich, kontinuierlich Tastendrücke zu erfassen, während eine Reihe von SKETCHPADs präsentiert wird.

Für weitere Informationen siehe:

- %link:coroutines%

### Integration des Open Science Frameworks

Sie können sich jetzt von OpenSesame aus beim [Open Science Framework](http://osf.io) (OSF) anmelden und mühelos Experimente und Daten zwischen Ihrem Computer und dem OSF synchronisieren. Vielen Dank an das [Center for Open Science](http://cos.io/) für die Unterstützung dieser Funktion!

Für weitere Informationen siehe:

- %link:osf%

### Ein Reaktionsobjekt

Es gibt ein neues standardmäßiges Python-Objekt: `responses`. Dieses Protokoll erfasst alle Antworten, die während des Experiments gesammelt wurden.

Für weitere Informationen siehe:

- %link:responses%

## Änderungen in 3.0

OpenSesame 3.0 hat viele Verbesserungen gebracht, die es noch einfacher machen, Experimente zu entwickeln. Die meisten Änderungen sind abwärtskompatibel. Das bedeutet, Sie können Dinge immer noch auf die alte Art und Weise tun. Eine Handvoll Änderungen sind jedoch nicht abwärtskompatibel, und es ist wichtig, sich dessen bewusst zu sein.

### Nicht abwärtskompatible Änderungen

#### Sampler-Eigenschaften

Das SAMPLER-Objekt hat eine Reihe von Eigenschaften, die zuvor Funktionen waren. Dies betrifft:

- `sampler.fade_in`
- `sampler.pan`
- `sampler.pitch`
- `sampler.volume`

Für weitere Informationen siehe:

- %link:sampler%

#### CSS3-kompatible Farben

Sie können nun CSS3-kompatible Farbspezifikationen verwenden, wie hier beschrieben:

- %link:manual/python/canvas%

Wenn Sie Farbnamen verwenden (z. B. 'red', 'green' usw.), kann dies zu leicht unterschiedlichen Farben führen. Zum Beispiel ist 'green' nach CSS3 `#008000` statt (wie bisher) `#00FF00`.

### Neues Dateiformat (.osexp)

OpenSesame speichert Experimente jetzt im `.osexp`-Format. Natürlich können Sie weiterhin die alten Formate öffnen (`.opensesame` und `.opensesame.tar.gz`). Für weitere Informationen siehe:

- %link:fileformat%

### Vereinfachte Python-API

#### Keine self und exp mehr

Es ist nicht mehr notwendig, `self.` oder `exp.` zu verwenden, wenn Sie häufig verwendete Funktionen aufrufen. Zum Beispiel wird dadurch die Probandennummer auf 2 gesetzt:

~~~ .python
set_subject_nr(2)
~~~

Eine Liste häufig verwendeter Funktionen finden Sie unter:

- %link:manual/python/common%

#### Das `var`-Objekt: einfaches Abrufen und Setzen von experimentellen Variablen

Die alte Methode, `self.get()` zum Abrufen und `exp.set()` zum Setzen von experimentellen Variablen zu verwenden, wurde durch eine einfachere Syntax ersetzt. Zum Beispiel zum Setzen der Variablen `condition`, so dass Sie sie als `[condition]` in SKETCHPADs usw. verwenden können:

~~~ .python
var.condition = 'easy`'
~~~

Und um eine experimentelle Variable `condition` zu erhalten, die beispielsweise in einer LOOP definiert wurde:

~~~ .python
print('Condition ist %s' % var.condition)
~~~

Für weitere Informationen siehe:

- %link:var%

#### Das `clock`-Objekt: Zeitfunktionen

Zeitfunktionen sind jetzt über das `clock`-Objekt verfügbar:

~~~ .python
print('Aktueller Zeitstempel: %s' % clock.time())
clock.sleep(1000) # Schlafen für 1 s
~~~

Für weitere Informationen siehe:

- %link:clock%

#### Das `pool`-Objekt: Zugriff auf den Datei-Pool

Der Datei-Pool ist jetzt über das `pool`-Objekt zugänglich, das eine `dict`-ähnliche Oberfläche unterstützt (aber kein echtes Python `dict` ist):

~~~ .python
path = pool['image.png']
print('Der vollständige Pfad zu image.png ist: %s' % path)
~~~

Für weitere Informationen siehe:

- %link:pool%

#### Keine "from openexp.* import *" mehr

Es ist nicht mehr notwendig, `openexp`-Klassen zu importieren und `exp` als ersten Parameter zu übergeben. Stattdessen können Sie einfach ein `canvas`-Objekt erstellen:

~~~ .python
my_canvas = canvas()
~~~

Es gibt ähnliche Factory-Funktionen (wie sie genannt werden) für `keyboard`, `mouse` und SAMPLER.

Für weitere Informationen siehe:

- %link:manual/python/common%

#### Der Synth ist jetzt ein Sampler

Der SYNTH ist keine eigene Klasse mehr. Stattdessen handelt es sich um eine Funktion, die ein SAMPLER-Objekt zurückgibt, das mit einer synthetisierten Probe gefüllt wurde.

### Verbesserungen der Benutzeroberfläche

#### Ein IPython-Debug-Fenster

IPython, ein interaktives Python-Terminal für wissenschaftliches Computing, wird jetzt für das Debug-Fenster verwendet.

#### Ein Live-Variable-Inspektor

Der Variablen-Inspektor zeigt nun die tatsächlichen Werte Ihrer Variablen während Ihr Experiment läuft und nachdem Ihr Experiment beendet ist.

#### Rückgängig machen

Sie können Aktionen endlich rückgängig machen!

#### Ein neues Farbschema

Das Standard-Farbschema ist jetzt *Monokai*. Wieder ein dunkles Farbschema, aber mit einem höheren Kontrast als das vorherige Standard, *Solarized*. Diese Erhöhung sollte die Lesbarkeit erhöhen. Und es sieht gut aus!

### Konsistente Koordinaten

Zuvor verwendete OpenSesame gemischte, inkonsistente Bildschirmkoordinaten: `0,0` war oben links auf dem Bildschirm, wenn Python-Code verwendet wurde, und in der Bildschirmmitte, wenn mit SKETCHPAD-Elementen gearbeitet wurde. Ab Version 3.0 ist die Bildschirmmitte immer `0,0`, auch im Python-Code.

Wenn Sie zur alten Verhaltensweise zurückkehren möchten, können Sie die Option "Einheitliche Koordinaten" im Allgemeinen Tab deaktivieren. Aus Gründen der Abwärtskompatibilität werden "Einheitliche Koordinaten" automatisch deaktiviert, wenn Sie ein altes Experiment öffnen.

### Verwendung von Python in Textzeichenketten

Sie können nun Python in Textzeichenketten mit der `[=...]` Syntax einbinden. Zum Beispiel wird die folgende Textzeichenkette in einem SKETCHPAD:

~~~
Zwei mal zwei ist [=2*2]
~~~

... angezeigt als:

~~~
Zwei mal zwei ist 4
~~~

Weitere Informationen finden Sie unter:

- %link:text%

### Unterstützung für Python 3

OpenSesame unterstützt jetzt Python >= 3.4. Viele Abhängigkeiten von OpenSesame, insbesondere PsychoPy und Expyriment, sind jedoch nur für Python 2 verfügbar. Daher bleibt Python 2.7 die Standardversion von Python.