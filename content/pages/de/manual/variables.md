title: Variablen
hash: 87f8069d56f529c53b29b95555f8d096d7d742f9b355ff6689a0d6e7cb2b8654
locale: de
language: German

[TOC]

## Was ist eine experimentelle Variable in OpenSesame?

Experimentelle Variablen in OpenSesame sind solche Variablen, die:

- Im Benutzerinterface mit der '{variable_name}'-Syntax referenziert werden können.
- Als globale Variablen in einem Python INLINE_SCRIPT verfügbar sind.
- Als globale Variablen in einem JavaScript INLINE_JAVASCRIPT verfügbar sind.
- Dinge enthalten wie:
	- Die Variablen, die Sie in einem LOOP-Element definiert haben.
	- Die gesammelten Antworten.
	- Verschiedene Eigenschaften des Experiments.
	- Usw.

## Der Variableninspektor

Der Variableninspektor (`Ctrl+I`) bietet einen Überblick über verfügbare Variablen (%FigVariableInspector). Wenn das Experiment nicht läuft, basiert dieser Überblick auf einer besten Schätzung, welche Variablen während des Experiments verfügbar werden. Wenn das Experiment jedoch läuft, zeigt der Variableninspektor eine Live-Übersicht der Variablen und deren Werte. Dies ist nützlich zur Fehlersuche in Ihrem Experiment.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: Der Variableninspektor bietet einen Überblick über alle Variablen, die OpenSesame kennt.
--%

## Variablen definieren

Der einfachste Weg, eine Variable zu definieren, ist über das LOOP-Element. Zum Beispiel zeigt %FigLoop, wie man eine Variable namens `gaze_cue` definiert. In diesem Beispiel wird das *trial_sequence*-Element viermal aufgerufen, während `gaze_cue` 'left' ist und eine weitere viermal, während 'gaze_cue' 'right' ist.

%--
figure:
 id: FigLoop
 source: defining-variables-in-a-loop.png
 caption: Der häufigste Weg, unabhängige Variablen zu definieren, ist die Verwendung der LOOP-Tabelle.
--%

## Integrierte Variablen

Die folgenden Variablen sind immer verfügbar:

### Experimentvariablen

|Variablenname			|Beschreibung|
|-----------------------|-----------|
|`title`				|Der Titel des Experiments|
|`description`			|Die Beschreibung des Experiments|
|`foreground`			|Die standardmäßige Vordergrundfarbe. Z.B. 'white' oder '#FFFFFF'.|
|`background`			|Die standardmäßige Hintergrundfarbe. Z.B. 'black' oder '#000000'.|
|`height`				|Der Höhenanteil der Bildschirmauflösung. Z.B. '768'|
|`width`				|Der Breitenanteil der Bildschirmauflösung. Z.B. '1024'|
|`subject_nr`			|Die Versuchspersonennummer, die beim Start des Experiments abgefragt wird.|
|`subject_parity`		|Ist 'odd', wenn `subject_nr` ungerade ist und 'even', wenn `subject_nr` gerade ist. Nützlich für das Gegengleichgewicht.|
|`experiment_path`		|Der Ordner des aktuellen Experiments, ohne den Dateinamen des Experiments selbst. Wenn das Experiment nicht gespeichert ist, hat es den Wert `None`.|
|`pool_folder`			|Der Ordner, in dem der Inhalt des Dateipools extrahiert wurde. Dies ist in der Regel ein temporärer Ordner.|
|`logfile`				|Der Pfad zur Logdatei.|

### Elementvariablen

Es gibt auch Variablen, die alle Elemente des Experiments verfolgen.

|Variablenname			|Beschreibung|
|-----------------------|-----------|
|`time_[item_name]`		|Enthält einen Zeitstempel, wann das Element zuletzt ausgeführt wurde. Für SKETCHPAD-Elemente kann dies verwendet werden, um das Timing der Bildschirmpräsentation zu überprüfen.|
|`count_[item_name]`	|Entspricht der Anzahl der Aufrufe minus eins (beginnend bei 0, mit anderen Worten), die ein Element aufgerufen wurde. Dies kann, zum Beispiel, als Trial- oder Blockzähler verwendet werden.|

### Antwortvariablen

Wenn Sie die standardmäßigen Antwortelemente verwenden, wie KEYBOARD_RESPONSE und MOUSE_RESPONSE, werden eine Reihe von Variablen aufgrund der Reaktion des Teilnehmers festgelegt.

|Variablenname					|Beschreibung|
|-------------------------------|-----------|
|`response`						|Enthält die zuletzt abgegebene Antwort.|
|`response_[item_name]`			|Enthält die letzte Antwort für ein bestimmtes Antwort-Element. Dies ist nützlich, wenn es mehrere Antwort-Elemente gibt.|
|`response_time`				|Enthält das Intervall in Millisekunden zwischen dem Start des Antwortintervalls und der letzten Antwort.|
|`response_time_[item_name]`	|Enthält die Antwortzeit für ein bestimmtes Antwort-Element.|
|`correct`						|Wird auf '1' gesetzt, wenn die letzte `response` der Variablen `correct_response` entspricht, auf '0' wenn nicht und auf 'undefined', wenn die Variable `correct_response` nicht gesetzt wurde.|
|`correct_[item_name]`			|Wie `correct`, aber für ein bestimmtes Antwort-Element.|

### Feedback Variablen

Feedback-Variablen führen einen gleitenden Durchschnitt von Genauigkeit und Antwortzeiten.

|Variablenname					|Beschreibung|
|-------------------------------|-----------|
|`average_response_time`		|Die durchschnittliche Antwortzeit. Diese Variable ist nützlich, um dem Teilnehmer Feedback zu präsentieren.|
|`avg_rt`						|Synonym für `average_response_time`|
|`accuracy`						|Der durchschnittliche Prozentsatz der richtigen Antworten. Diese Variable ist nützlich, um dem Teilnehmer Feedback zu präsentieren.|
|`acc`							|Synonym für `accuracy`|

## Verwendung von Variablen in der Benutzeroberfläche

Überall dort, wo Sie in der Benutzeroberfläche einen Wert sehen, können Sie diesen Wert durch eine Variable ersetzen, indem Sie die '{variable_name}'-Notation verwenden. Wenn Sie beispielsweise in einem LOOP-Element eine Variable `soa` definiert haben, können Sie diese Variable für die Dauer eines Sketchpad verwenden, wie in %FigSketchpad gezeigt.

%--
figure:
 id: FigSketchpad
 source: variable-duration.png
 caption: Die Dauer "{soa}" zeigt, dass die Dauer des SKETCHPAD von der Variable `soa` abhängt.
--%

Dies funktioniert in der gesamten Benutzeroberfläche. Wenn Sie beispielsweise die Variable `my_freq` definiert haben, können Sie diese Variable als Frequenz in einem SYNTH-Element verwenden, wie in %FigSynth gezeigt.

%--
figure:
 id: FigSynth
 source: variable-frequency.png
 caption: Die Frequenz "{my_freq}" zeigt, dass die Frequenz des SYNTH von der Variable `my_freq` abhängt.
--%

Manchmal können Sie in der Benutzeroberfläche keinen beliebigen Text eingeben. Zum Beispiel sind die Elemente eines SKETCHPAD visuell dargestellt, und Sie können eine X-Koordinate nicht direkt in eine Variable ändern. Sie können jedoch auf den *Select view → View script*-Button oben rechts klicken und das Script direkt bearbeiten.

Zum Beispiel können Sie die Position eines Fixationspunkts von der Mitte ändern:

```text
draw fixdot x=0 y=0
```

… zu einer Position, die durch die Variablen `xpos` und `ypos` definiert wird:

```text
draw fixdot x={xpos} y={ypos}
```


## Verwendung von Python-Ausdrücken in der Benutzeroberfläche

Wenn Sie auf Variablen mit der `{my_var}`-Notation verweisen, verwenden Sie tatsächlich einen sogenannten [f-String](https://peps.python.org/pep-0498/), der eine Möglichkeit ist, Python-Code in Textzeichenketten einzubetten. Sie können f-Strings auch verwenden, um beliebigen Python-Code auszuwerten. Zum Beispiel können Sie die Variablen `width` und `height` multiplizieren und das Ergebnis in einem SKETCHPAD einschließen, wie folgt:

%--
figure:
 id: FigFString
 source: fstrings.png
 caption: Sie können Python-Ausdrücke mit f-Strings einbetten.
--%

f-Strings sind Python-Code und werden daher nur auf dem Desktop unterstützt. Für Browser-Experimente gibt es jedoch eine JavaScript-Alternative.


## Verwendung von JavaScript-Ausdrücken in der Benutzeroberfläche

Bei der Verwendung von OSWeb werden Ausdrücke, die zwischen geschweiften Klammern eingeschlossen sind, als [Template-Literale](https://developer.mozilla.org/de/docs/Web/JavaScript/Reference/template_literals) interpretiert. Dies ist sehr ähnlich wie f-Strings in Python, mit dem wichtigen Unterschied, dass es JavaScript verwendet.

In normalem JavaScript werden Ausdrücke innerhalb von Template-Literale mit einem `$` vorangestellt, so: `${expression}`. Dies ist in OpenSesame erlaubt, aber nicht notwendig: Das Präfix wird automatisch hinzugefügt, um die Kompatibilität zwischen Browser- und Desktop-Experimenten zu verbessern. In den meisten Fällen, wie in der Abbildung unten, ist derselbe Ausdruck sowohl als Python f-String auf dem Desktop als auch als JavaScript-Template-Literal im Browser gültig.

%--
figure:
 id: FigTempalteLiteral
 source: template-literals.png
 caption: Sie können JavaScript-Ausdrücke mit Template-Literalen einbetten.
--%

## Verwenden von Variablen in Python

In einem INLINE_SCRIPT stehen experimentelle Variablen als globale Variablen zur Verfügung. Wenn Sie zum Beispiel in einer LOOP die `example_variable` definiert haben, wird der folgende Code den Wert von `example_variable` im Debug-Fenster anzeigen:

~~~ .python
print(example_variable)
~~~

Sie können die experimentelle Variable `example_variable` wie folgt auf den Wert 'some value' setzen:

~~~ .python
example_variable = 'some value'
~~~

## Verwenden von Variablen in JavaScript

In einem INLINE_JAVASCRIPT stehen experimentelle Variablen als globale Variablen zur Verfügung. Bei der Definition von `example_variable` in einer LOOP wird der folgende Code den Wert von `example_variable` in der Browser-Konsole anzeigen:

```js
console.log(example_variable)
```

Sie können die experimentelle Variable `example_variable` wie folgt auf den Wert 'some value' setzen:

```js
example_variable = 'some value'
```

## Verwenden von bedingten ("if") Anweisungen

Bedingte Anweisungen oder 'if-Anweisungen' bieten eine Möglichkeit, anzugeben, dass etwas nur unter bestimmten Umständen geschehen soll, z. B. wenn eine Variable einen bestimmten Wert hat. Bedingte Anweisungen sind reguläre Python-Ausdrücke.

Die am häufigsten verwendete if-Anweisung in OpenSesame ist die run-if-Anweisung der SEQUENCE, mit der Sie die Bedingungen angeben können, unter denen ein bestimmtes Element ausgeführt wird. Wenn Sie ein SEQUENCE-Element öffnen, sehen Sie, dass jedes Element aus der Sequenz eine 'Run if …''-Option hat. Der Standardwert ist 'always', was bedeutet, dass das Element immer ausgeführt wird; aber Sie können hier auch eine Bedingung eingeben. Wenn Sie zum Beispiel nach einer korrekten Antwort einen grünen Fixationspunkt und nach einer falschen Antwort einen roten Fixationspunkt anzeigen möchten, können Sie eine SEQUENCE erstellen wie folgt (dies macht sich zunutze, dass ein KEYBOARD_RESPONSE-Element automatisch die Variable `correct` setzt, wie oben besprochen) wie in %FigRunIf gezeigt.

*Wichtig:* Die "Run if"-Anweisungen gelten nur für die Run-Phase von Elementen. Die Prepare-Phase wird immer ausgeführt. Siehe auch [diese Seite](%link:prepare-run%).

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: |
  'Run if'-Anweisungen können verwendet werden, um anzugeben, dass bestimmte Elemente einer SEQUENCE nur unter bestimmten Umständen ausgeführt werden sollen.
--%

Sie können auch komplexere Bedingungen verwenden. Hier sind einige Beispiele:

```python
correct == 1 and response_time > 2000
correct != 1 or response_time > max_response_time or response_time < min_response_time
```

Dasselbe Prinzip gilt für die 'Show if'-Felder in SKETCHPAD-Elementen. Wenn Sie zum Beispiel einen rechts aufwärts gerichteten Pfeil zeichnen möchten, aber nur, wenn die Variable `quadrant` auf 'upper right' gesetzt wurde, geben Sie einfach die entsprechende Bedingung in das Feld 'Show if ...' ein und zeichnen Sie den Pfeil, wie in %FigShowIf gezeigt. Stellen Sie sicher, dass Sie den Pfeil zeichnen, nachdem Sie die Bedingung festgelegt haben.

%--
figure:
 id: FigShowIf
 source: show-if.png
 caption: "'Show if'-Anweisungen können verwendet werden, um anzugeben, dass bestimmte Elemente eines SKETCHPAD- oder FEEDBACK-Elements nur unter bestimmten Umständen angezeigt werden sollen."
--%

Wichtig: Der Zeitpunkt, zu dem eine bedingte Anweisung ausgewertet wird, kann sich auf die Funktionsweise Ihres Experiments auswirken. Dies hängt mit der Prepare-Run-Strategie zusammen, die von OpenSesame verwendet wird und hier erklärt wird:

- %link:prepare-run%