title: Fehlersuche
hash: 183510524112a0f1a17d60669acd2273f06aa15f0b358eb9d3fdaac1002810c0
locale: de
language: German

Während Sie ein neues Experiment entwerfen, werden Sie unweigerlich auf Fehler stoßen. Fehler können sich als Abstürze mit Fehlermeldungen manifestieren oder als unerwartete Verhaltensweisen ohne ausdrückliche Fehlermeldung.

Das Debuggen, also die Kunst und Fähigkeit, diese Fehler und unerwarteten Verhaltensweisen zu diagnostizieren und zu beheben, ist ein entscheidender Teil des Prozesses der experimentellen Gestaltung.

[TOC]

## Debuggen in der Benutzeroberfläche

### Verwendung des Variableninspektors

Der Variableninspektor in OpenSesame bietet einen Überblick über alle Variablen, die derzeit in Ihrem Experiment aktiv sind. Dazu gehören:

- Variablen, die explizit in der Benutzeroberfläche definiert sind, typischerweise in einem LOOP-Element.
- Antwortvariablen, die durch verschiedene Antwortelemente wie das KEYBOARD_RESPONSE-Element gesetzt werden.
- Variablen, die mit Hilfe von Python INLINE_SCRIPT-Elementen definiert werden.

Während ein Experiment läuft, aktualisiert der Variableninspektor dynamisch und bietet einen ständigen Überblick über Variablen und ihre Werte. Mit dieser Funktion können Sie das Verhalten Ihres Experiments in Echtzeit beobachten und helfen, etwaige Probleme oder Fehler zu erkennen.

Wenn Sie zum Beispiel eine Variable `left_letter` definiert haben, um festzulegen, welcher Buchstabe auf der linken Seite eines SKETCHPADs erscheinen soll, stellen Sie jedoch fest, dass es während der Ausführung im Variableninspektor zu einer Übereinstimmung kommt: `left_letter` wird tatsächlich auf der rechten Seite Ihres Bildschirms angezeigt. Dies deutet auf einen Fehler hin, d.h., Sie haben die rechten und linken Buchstaben auf dem SKETCHPAD verwechselt.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: Sie können den Variableninspektor verwenden, um zu prüfen, ob Ihr Experiment so funktioniert, wie es sollte. In diesem Beispiel handelt es sich um einen Fehler, so dass der Buchstabe, der durch die Variable `left_letter` definiert ist, tatsächlich rechts erscheint und umgekehrt.
--%

Die regelmäßige Verwendung des Variableninspektors zur Überwachung von Variablen hilft sicherzustellen, dass Ihr Experiment wie erwartet funktioniert und unterstützt bei der frühzeitigen Erkennung von Problemen.

### Drucken von Fehlermeldungen auf die IPython-/Jupyter-Konsole

Die Python `print()`-Funktion ist ein einfaches und leistungsstarkes Debugging-Werkzeug, wenn es in INLINE_SCRIPT-Elementen verwendet wird, und hat einen ähnlichen Zweck wie der Variableninspektor. Beispielweise können Sie die Werte der Variablen `left_letter` und `right_letter` während der Vorbereitungsphase eines INLINE_SCRIPT am Anfang eines Versuchs ausdrucken.

Um diese Fehlermeldungen zu sehen, öffnen Sie die Jupyter/IPython-Konsole und beobachten Sie die Ausgabe während des Experiments. Damit können Sie überprüfen, ob die in der Konsole angezeigte Ausgabe mit dem tatsächlichen Verhalten des Experiments übereinstimmt.

%--
figure:
 id: FigPrintingOutput
 source: printing-output.png
 caption: Die Python `print()`-Funktion kann verwendet werden, um Fehlermeldungen an die Konsole zu senden.
--%

Im obigen Beispiel wird deutlich, dass der Buchstabe, der der Variable `left_letter` zugewiesen ist (und daher links erscheinen sollte), tatsächlich rechts erscheint und umgekehrt.

### Interpretation von Fehlermeldungen der Benutzeroberfläche

Wenn ein Fehler in Ihrem Experiment einen Absturz verursacht, zeigt OpenSesame eine Fehlermeldung an, die auch als "Ausnahme" bezeichnet wird. Eine Fehlermeldung besteht in der Regel aus den folgenden Komponenten:

- **Fehlertyp:** Gibt die allgemeine Klasse des Fehlers an. Im untenstehenden Beispiel ist dies ein `FStringError`.
- **Beschreibung:** Gibt eine spezifischere Erklärung dafür, was den Fehler ausgelöst hat. In diesem Fall: 'Fehler bei der Auswertung …'.
- **Quelle:** Gibt an, welches Element den Fehler ausgelöst hat und ob er während der Run- oder Prepare-Phase aufgetreten ist.
- **Rückverfolgung:** Eine detaillierte Python-Fehlermeldung. Diese Informationen werden nur angezeigt, wenn der Fehler beim Auswerten von benutzerdefiniertem Python-Code auftrat, was auch INLINE_SCRIPT-Elemente umfasst, aber auch bedingte Ausdrücke (z.B. Run-if-Ausdrücke) und Text mit eingebetteten Variablenreferenzen.
- **Mehr über diesen Fehler erfahren:** Ein interaktiver Button, auf den Sie klicken können, um detailliertere Informationen über die Fehlermeldung zu erhalten.

Lassen Sie uns ein Beispiel betrachten, um diese Komponenten besser zu verstehen und zu lernen, wie man einen gängigen Fehler behebt:

%--
figure:
 id: FigFStringError
 source: fstring-error.png
 caption: Ein `FStringError` weist auf ein Problem hin, wenn versucht wird, einen Textstring auszuwerten, der einen Python-Ausdruck enthält.
--%

Dies ist ein `FStringError`, was bedeutet, dass es ein Problem gab bei der Interpretation eines Textstrings, der einen Python-Ausdruck enthält. In diesem Beispiel ist der problematische Text `{right_leter}`. Alles, was in geschweiften Klammern eingeschlossen ist, wird als Python-Ausdruck interpretiert, und daher ist in diesem Fall der Python-Ausdruck `right_leter` - was einfach ein Variablenname ist. Der Versuch, den Python-Ausdruck `right_leter` auszuwerten, löste einen `NameError` aus, weil `right_leter` nicht definiert ist.

Das klingt ziemlich technisch, aber was genau ist hier in einfachen Worten schief gelaufen? Das Problem entsteht, wenn auf eine nicht existierende Variable verwiesen wird: `right_leter`. Wenn man sich den Variablennamen anschaut, scheint es wahrscheinlich, dass ein Tippfehler vorliegt: die beabsichtigte Variable ist wahrscheinlich `right_letter`, mit einem doppelten 't'.

Wo sollten wir diesen Fehler korrigieren? Die Fehlermeldung weist darauf hin, dass die Quelle des Fehlers ein Element namens *target* ist, das ein SKETCHPAD ist. Um den Fehler zu beheben, müssen wir *target* öffnen und den Text von '{right_leter}' in '{right_letter}' ändern.


### Python-Fehlermeldungen interpretieren

In Python fallen Fehler in zwei Kategorien: Syntaxfehler und Ausnahmen (oder Laufzeitfehler).


#### Python-Syntaxfehler

Ein Syntaxfehler tritt auf, wenn der Python-Interpreter keinen Code analysieren kann, weil er gegen die Syntaxregeln von Python verstößt. Dies könnte aufgrund von nicht übereinstimmenden Klammern, fehlenden Kommas, falscher Einrückung und so weiter geschehen. In OpenSesame führt dies zu einem `PythonSyntaxError`.

%--
figure:
 id: FigPythonSyntaxError
 source: python-syntax-error.png
 caption: Ein `PythonSyntaxError` wird ausgelöst, wenn der Code gegen die Syntaxregeln von Python verstößt und nicht geparst werden kann.
--%

Die oben stehende Fehlermeldung zeigt an, dass ein Syntaxfehler in Zeile 16 der Prepare-Phase eines Elements namens *constants* aufgetreten ist. Hier ist die problematische Zeile:

```python
target_orientations = [('z', 0), ('/', 90]
```

Die Meldung weist auch auf nicht übereinstimmende Klammern als potentielle Quelle des Fehlers hin. Berücksichtigt man das, können wir das Problem beheben, indem wir eine fehlende Klammer `)` vor der schließenden Klammer `]` hinzufügen:

```python
target_orientations = [('z', 0), ('/', 90)]
```


#### Python-Ausnahmen

Wenn Python-Code syntaktisch korrekt ist, aber während der Ausführung auf ein Problem stößt, wird eine Ausnahme ausgelöst. In OpenSesame führen solche Ausnahmen zu einem `PythonError`.

%--
figure:
 id: FigPythonError
 source: python-error.png
 caption: Ein `PythonError` wird ausgelöst, wenn während der Ausführung von syntaktisch korrektem Python-Code eine Ausnahme auftritt.
--%

Die oben stehende Fehlermeldung zeigt an, dass ein `NameError` in Zeile 2 der Run-Phase eines Elements namens *trial_script* ausgelöst wurde. Insbesondere wird der Bezeichner 'clock_sleep' nicht erkannt. Betrachtet man die fehlerverursachende Zeile, wird deutlich, dass wir statt einem Punkt (`.`) einen Unterstrich (`_`) verwendet haben, was fälschlicherweise impliziert, dass `clock_sleep()` eine Funktion ist.

```python
clock_sleep(495)
```

Um dies zu korrigieren, sollten wir die `sleep()` Funktion korrekt als Teil des `clock` Objekts referenzieren:

```python
clock.sleep(495)
```

## Debugging in einem Webbrowser (OSWeb)


### Ausgabe auf die Browser-Konsole drucken

Die JavaScript `console.log()` Funktion ist ein einfaches und dennoch mächtiges Debugging-Werkzeug, wenn sie innerhalb von INLINE_JAVASCRIPT Elementen verwendet wird. Sie dient einem ähnlichen Zweck wie die Python `print()` Funktion und der Variableninspektor, die beide in OSWeb nicht zur Verfügung stehen. Zum Beispiel können Sie die Werte der Variablen `left_letter` und `right_letter` während der Vorbereitungsphase eines INLINE_SCRIPT am Anfang jedes Versuchsdrucks anzeigen lassen.

Um diese Debug-Nachrichten zu sehen, müssen Sie die Browser-Konsole öffnen. So geht's in Chrome, Firefox und Edge:

- **Google Chrome:** Drücken Sie Strg + Umschalt + J (Windows / Linux) oder Befehl + Option + J (Mac).
- **Mozilla Firefox:** Drücken Sie Strg + Umschalt + K (Windows / Linux) oder Befehl + Option + K (Mac).
- **Microsoft Edge:** Drücken Sie F12, um die Entwicklertools zu öffnen, und wählen Sie dann die Registerkarte "Konsole".

Sobald die Konsole geöffnet ist, können Sie die Ausgabe während des Experiments überwachen, sodass Sie überprüfen können, ob die in der Konsole angezeigte Ausgabe mit dem tatsächlichen Verhalten des Experiments übereinstimmt.

%--
figure:
 id: FigPrintingOutputOSWeb
 source: printing-output-osweb.png
 caption: Die JavaScript `console.log()` Funktion kann verwendet werden, um Debug-Nachrichten in der Browser-Konsole auszugeben.
--%

Im obigen Beispiel wird deutlich, dass der dem `left_letter` Variable (die links erscheinen sollte) zugewiesene Buchstabe tatsächlich auf der rechten Seite erscheint und umgekehrt.


### Fehlermeldung verstehen

Wenn Ihr browserbasiertes Experiment abstürzt, zeigt OSWeb eine Fehlermeldung im Browser an. Eine Fehlermeldung besteht typischerweise aus den folgenden Komponenten:

- **Fehlertyp:** Gibt die allgemeine Fehlerklasse an. In dem folgenden Beispiel handelt es sich um einen `ReferenceError`.
- **Beschreibung:** Gibt eine genauere Erklärung darüber, was den Fehler ausgelöst hat. In diesem Fall "right_leter ist nicht definiert".
- **Quelle:** Gibt das Element an, das den Fehler ausgelöst hat und ob er während der Run- oder Prepare-Phase aufgetreten ist.
- **Ursprüngliches Skript:** Der JavaScript-Code, der den Fehler verursacht hat. Diese Information wird nur angezeigt, wenn der Fehler aufgetreten ist, während benutzerdefiniertes JavaScript ausgewertet wurde, einschließlich INLINE_JAVASCRIPT Elemente, aber auch bedingte Ausdrücke (z. B. run-if-Ausdrücke) und Text mit eingebetteten Variablenreferenzen.

Schauen wir uns ein Beispiel an, um diese Komponenten besser zu verstehen und zu lernen, wie man einen gängigen Fehler behebt:

%--
figure:
 id: FigOSWebError
 source: osweb-error.png
 caption: Ein `ReferenceError` zeigt eine Referenz auf eine nicht existente Variable oder ein anderes nicht existentes Objekt an.
--%

Dies ist ein `ReferenceError`, der darauf hinweist, dass das Experiment auf eine nicht existente Variable oder ein anderes nicht existentes Objekt verweist. In diesem Beispiel geht der Fehler von dem Text `${right_leter}` aus. Alles, was in geschweiften Klammern eingeschlossen und mit einem `$` gekennzeichnet ist, wird als JavaScript-Ausdruck interpretiert, und in diesem Fall ist der JavaScript-Ausdruck `right_leter` - was einfach ein Variablenname ist. Der Versuch, den JavaScript-Ausdruck `right_leter` auszuwerten, löste einen `ReferenceError` aus, da `right_leter` nicht definiert ist.

Das klingt ziemlich technisch, aber was genau ist hier in einfachen Worten schief gelaufen? Das Problem entsteht durch die Bezugnahme auf eine nicht existente Variable: `right_leter`. Bei Betrachtung des Variablennamens scheint es wahrscheinlich, dass es sich um einen Tippfehler handelt: die beabsichtigte Variable ist wahrscheinlich `right_letter`, mit einem Doppel-'t'.

Wo sollten wir diesen Fehler korrigieren? Die Fehlermeldung weist darauf hin, dass die Quelle des Fehlers ein Element namens *target* ist, welches ein SKETCHPAD ist. Um den Fehler zu beheben, müssen wir *target* öffnen und den Text von '{right_leter}' zu '{right_letter}' ändern. 


### Verwendung der `debugger` Anweisung in INLINE_JAVASCRIPT Elementen

Die JavaScript `debugger` Anweisung ist ein mächtiges Werkzeug zum Debuggen von `INLINE_JAVASCRIPT` Elementen in OpenSesame/OSWeb Experimenten. Sie ermöglicht es Ihnen, Haltepunkte in Ihrem Code einzufügen, wodurch die JavaScript-Ausführung des Browsers an dieser Stelle pausiert. Dies ermöglicht es Ihnen, den aktuellen Zustand des JavaScript-Arbeitsbereichs zu inspizieren.

Die Verwendung der `debugger` Anweisung ist unkompliziert. Fügen Sie einfach die Anweisung `debugger` in die Zeile ein, an der Sie die Ausführung anhalten möchten. Zum Beispiel:

```javascript
console.log(`left_letter = ${left_letter}`)
console.log(`right_letter = ${right_letter}`)
debugger // Ausführung wird hier pausiert
```

Nachdem Sie die `debugger` Anweisung in Ihren Code eingefügt haben, müssen Sie die Browser-Konsole öffnen, wie oben erklärt. Nachdem Sie die Browser-Konsole geöffnet haben, führen Sie Ihr Experiment durch. Wenn der JavaScript-Interpreter die `debugger` Anweisung erreicht, wird er die Ausführung pausieren und die Entwicklertools wechseln zum "Sources" (Chrome/Edge) oder "Debugger" (Firefox) Tab und heben die Zeile mit dem Haltepunkt hervor.

%--
figure:
 id: FigJavaScriptDebugger
 source: javascript-debugger.png
 caption: When the JavaScript interpreter reaches the `debugger` statement, it will pause execution and allow you to inspect the JavaScript workspace. The `debugger` statement only works when the browser console is open.
--%

Während die Ausführung pausiert ist, können Sie Variablenwerte inspizieren, den Code Zeile für Zeile durchgehen und den Call-Stack untersuchen, um den Zustand Ihres Programms am Haltepunkt besser zu verstehen.

Vergessen Sie nicht, die `debugger` Anweisungen zu entfernen oder auszukommentieren, wenn Sie mit dem Debuggen fertig sind, da sie sonst den normalen Betrieb Ihres Experiments stören können.

## Umgang mit ExperimentProcessDied Fehlern

Gelegentlich könnten Sie während eines Experiments auf einen `ExperimentProcessDied` Fehler stoßen.

%--
figure:
 id: FigExperimentProcessDied
 source: experiment-process-died.png
 caption: The `ExperimentProcessDied` error generally indicates an issue with the underlying Python process or associated libraries, not your experiment's code.
--%

Dieser Fehler deutet darauf hin, dass der Python-Prozess, in dem das Experiment lief, unerwartet beendet wurde. Es weist normalerweise nicht auf einen Fehler in Ihrem Experiment hin, sondern deutet auf ein Problem in einer der Low-Level-Bibliotheken, die von OpenSesame verwendet werden, oder sogar auf einen Fehler in Python selbst hin.

Die genaue Ursache dieses Fehlers zu bestimmen, kann herausfordernd sein und das Beheben sogar noch mehr. Es gibt jedoch einige Ausweichlösungen, die Sie ausprobieren können, um das Problem zu mildern:

- **Ändern Sie das Backend:** Wählen Sie unter 'Run Experiment' in den Experimenteigenschaften ein anderes Backend aus. Dies könnte das Problem beheben, da verschiedene Backends unterschiedliche Sets von Low-Level-Bibliotheken verwenden.
- **Aktualisierung von OpenSesame und relevanten Paketen:** Eine regelmäßige Aktualisierung von OpenSesame und allen zugehörigen Paketen kann dieses Problem möglicherweise beheben, da in neuen Versionen routinemäßig Fehler behoben werden.