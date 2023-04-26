title: Über Python
hash: 99b67bfe88b7ad764c9bc1c2a5da5b4114e573e6c0e442ff7f88dc080051e6b2
locale: de
language: German

In OpenSesame können Sie komplexe Experimente nur mit der grafischen Benutzeroberfläche (GUI) erstellen. Manchmal stoßen Sie jedoch auf Situationen, in denen die Funktionalität der GUI unzureichend ist. In diesen Fällen können Sie Python-Code zu Ihrem Experiment hinzufügen.

Python wird in Online-Experimenten mit OSWeb nicht unterstützt. Wenn Sie Ihr Experiment online durchführen müssen, müssen Sie stattdessen [JavaScript](%url:manual/javascript/about%) verwenden.

[TOC]

## Python lernen

Ein grundlegendes Set an Tutorials und Übungen zum Einstieg in Python finden Sie unter <https://pythontutorials.eu/>.

## Python in der OpenSesame GUI

### Ein einzelner Python-Arbeitsbereich

Der gesamte Python-Code wird in einem einzigen Python-Arbeitsbereich ausgeführt. Das bedeutet, dass in einem INLINE_SCRIPT definierte Variablen in allen anderen INLINE_SCRIPTs sowie in Python-Ausdrücken, die in Run-if-Anweisungen und Textstrings eingebettet sind, zugänglich sind. Das Gleiche gilt für Module: Einmal `import`iert, sind sie überall verfügbar.

So können Sie zum Beispiel das `Canvas` in einem INLINE_SCRIPT erstellen...

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
~~~

... und es in einem anderen INLINE_SCRIPT anzeigen ...

~~~ .python
my_canvas.show()
~~~

### Inline_script Elemente

Um Python-Code zu verwenden, müssen Sie Ihrem Experiment ein INLINE_SCRIPT Element hinzufügen. Sie können dies tun, indem Sie das Python-Symbol (das blau/gelbe Symbol) aus der Element-Symbolleiste in die Experimentsequenz ziehen. Danach sehen Sie etwas Ähnliches wie %FigInlineScript.

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: Das INLINE_SCRIPT Element.
--%

Wie Sie sehen können, besteht das INLINE_SCRIPT Element aus zwei Registerkarten: einer für die Prepare-Phase und einer für die Run-Phase. Die Prepare-Phase wird zuerst ausgeführt, um den Elementen Zeit zu geben, sich auf die zeitkritische Run-Phase vorzubereiten. Es ist gute Praxis, `Canvas`-Objekte, `Sampler`-Objekte usw. während der Prepare-Phase zu erstellen, damit sie während der Run-Phase ohne Verzögerung präsentiert werden können. Aber das ist nur eine Konvention; Sie können während beider Phasen beliebigen Python-Code ausführen.

Für weitere Informationen zur Prepare-Run-Strategie siehe:

- %link:prepare-run%

### Bedingte ("if") Ausdrücke

Sie können einzeilige Python-Ausdrücke in bedingten Ausdrücken verwenden. Zum Beispiel können Sie das folgende Python-Skript als Run-if-Ausdruck verwenden (siehe auch %FigRunIf):

~~~ .python
correct == 1 and response_time < 1000
~~~

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: Verwendung von Python-Skripten in der Run-if-Anweisung eines SEQUENCE Elements.
--%

Weitere Informationen zu bedingten ("if") Ausdrücken finden Sie unter:

- %link:manual/variables%

### Python in Text-Strings

Sie können Python-Anweisungen in Textstrings mit der {...} Syntax einbetten. Dies funktioniert für einfache Variablenreferenzen, aber auch für einzeilige Ausdrücke. Zum Beispiel könnten Sie den folgenden Text einem SKETCHPAD hinzufügen:

```text
Die Auflösung beträgt {width} x {height} px, insgesamt {width * height} Pixel
```

Je nach Auflösung Ihres Experiments könnte dies zu folgendem Text führen:

```text
Die Auflösung beträgt 1024 x 768 px, insgesamt 786432 Pixel
```

Weitere Informationen zu Variablen und Text finden Sie unter:

- %link:manual/variables%
- %link:manual/stimuli/text%

### Die Jupyter-Konsole (Debug-Fenster)

OpenSesame leitet die Standardausgabe an die Konsole (oder: Debug-Fenster) weiter, die Sie mit Strg + D oder über das Menü aktivieren können (Menü -> Ansicht -> Debug-Fenster anzeigen; siehe %FigDebugNormal). Sie können in die Konsole mit `print()` ausgeben.

~~~ .python
print('Das erscheint im Debug-Fenster!')
~~~

Die Konsole ist außerdem ein interaktiver Python-Interpreter, der von [Jupyter Project](https://jupyter.org) unterstützt wird.

## Dinge, die Sie wissen sollten

### Gängige Funktionen

Viele gängige Funktionen sind direkt in einem INLINE_SCRIPT-Element verfügbar, ohne dass etwas importiert werden muss. Zum Beispiel:

~~~ .python
# `Canvas()` ist eine Fabrikfunktion, die ein `Canvas`-Objekt zurückgibt
fixdot_canvas = Canvas()
if sometimes(): # Manchmal ist der Fixpunkt grün
    fixdot_canvas.fixdot(color='green')
else: # Manchmal ist er rot
    fixdot_canvas.fixdot(color='red')
fixdot_canvas.show()
~~~

Eine Liste der häufig verwendeten Funktionen finden Sie unter:

- %link:manual/python/common%


### Das `var`-Objekt: Zugang zu experimentellen Variablen

__Hinweis zur Version__ Ab OpenSesame 4.0 sind alle experimentellen Variablen als globale Variablen verfügbar. Das bedeutet, dass Sie das `var`-Objekt nicht mehr benötigen.
{:.page-notification}

Sie können auf experimentelle Variablen über das `var`-Objekt zugreifen:

~~~ .python
# Eine experimentelle Variable abrufen
print('my_variable ist: %s' % var.my_variable)
# Eine experimentelle Variable setzen
var.my_variable = 'my_value'
~~~

Eine vollständige Übersicht über das `var`-Objekt finden Sie hier:

- %link:manual/python/var%


### Das `clock`-Objekt: Zeitfunktionen

Grundlegende Zeitfunktionen sind über das `clock`-Objekt verfügbar:

~~~ .python
# Den aktuellen Zeitstempel abrufen
t = clock.time()
# 1 s warten
clock.sleep(1000)
~~~

Eine vollständige Übersicht über das `clock`-Objekt finden Sie hier:

- %link:manual/python/clock%


### Das `log`-Objekt: Datenaufzeichnung

Die Datenaufzeichnung ist über das `log`-Objekt verfügbar:

~~~ .python
# Eine Zeile Text schreiben
log.write('Meine benutzerdefinierte Log-Nachricht')
# Alle Variablen schreiben
log.write_vars()
~~~

Eine vollständige Übersicht über das `log`-Objekt finden Sie hier:

- %link:manual/python/log%


### Das `pool`-Objekt: Zugang zum Datei-Pool

Den vollständigen Pfad zu einer Datei im Datei-Pool erhalten Sie über das `pool`-Objekt:

~~~ .python
# Ein Bild aus dem Datei-Pool anzeigen
path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(path)
my_canvas.show()
~~~

Eine vollständige Übersicht über das `pool`-Objekt finden Sie hier:

- %link:manual/python/pool%


### Das `responses`-Objekt: Zugang zu Teilnehmerantworten

Das `responses`-Objekt speichert alle Teilnehmerantworten, die während des Experiments erfasst wurden. Um beispielsweise die Korrektheit aller bisher erfassten Antworten aufzulisten:

~~~ .python
for response in responses:
    print(response.correct)
~~~

Eine vollständige Übersicht über das `responses`-Objekt finden Sie hier:

- %link:manual/python/responses%


### Die `Canvas`-Klasse: Präsentation visueller Reize

Die `Canvas`-Klasse wird verwendet, um visuelle Reize darzustellen. Um beispielsweise einen Fixationspunkt anzuzeigen:

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

Eine vollständige Übersicht über die "Canvas"-Klasse finden Sie hier:

- %link:manual/python/canvas%


### Die `Keyboard`-Klasse: Tastendrucke sammeln

Die `Keyboard`-Klasse wird verwendet, um Tastendrucke zu erfassen. Um beispielsweise einen Tastendruck mit einer Timeout von 1000 ms zu erfassen:

~~~ .python
my_keyboard = Keyboard(timeout=1000)
key, time = my_keyboard.get_key()
~~~

Eine vollständige Übersicht über die `Keyboard`-Klasse finden Sie hier:

- %link:manual/python/keyboard%


### Die `Mouse`-Klasse: Mausklicks und Bildschirmberührungen sammeln

Die `Mouse`-Klasse wird verwendet, um Mausklicks und Bildschirmberührungen zu erfassen. (OpenSesame macht keinen Unterschied zwischen den beiden.) Um beispielsweise einen Mausklick mit einer Timeout von 1000 ms zu erfassen:

~~~ .python
my_mouse = Mouse(timeout=1000)
button, position, time = my_mouse.get_click()
~~~

Eine vollständige Übersicht über die `Mouse`-Klasse finden Sie hier:

- %link:manual/python/mouse%


### Die `Sampler`-Klasse: Soundwiedergabe

Die `Sampler`-Klasse wird verwendet, um Tonbeispiele abzuspielen. Um beispielsweise einen einfachen Piepton wiederzugeben:

~~~ .python
my_sampler = Sampler()
my_sampler.play()
~~~

Eine vollständige Übersicht über die `Sampler`-Klasse finden Sie hier:

- %link:manual/python/sampler%


## Alternative Module für die Darstellung von Anzeigen, Sammeln von Antworten usw.


### `psychopy`

Wenn Sie das *psycho*-Backend verwenden, können Sie die verschiedenen [PsychoPy]-Module direkt verwenden. Weitere Informationen finden Sie unter:

- %link:backends%


### `expyriment`

Wenn Sie das *xpyriment*-Backend verwenden, können Sie die verschiedenen [Expyriment]-Module direkt verwenden. Weitere Informationen finden Sie unter:

- %link:backends%

### `pygame`

Wenn Sie das *legacy*, *droid* oder *xpyriment* Backend verwenden (nur mit "Use OpenGL" auf "no" eingestellt), können Sie die verschiedenen [PyGame] Module direkt verwenden. Weitere Informationen finden Sie unter:

- %link:backends%


[python]: http://www.python.org/
[backends]: /backends/about-backends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org/
[pygame]: http://www.pygame.org/