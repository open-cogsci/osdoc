title: Dinge parallel ausführen
hash: 355690924feb930d7fef825b28269bb20c28adb8e20b8c2a86de761222d40d95
locale: de
language: German

Coroutinen führen mehrere Elemente parallel aus - oder genauer gesagt, sie führen Elemente in schneller Abfolge auf eine Weise aus, die parallel aussieht. Nicht alle Elemente unterstützen Coroutinen.

[TOC]

## Coroutinen verwenden

Sie können Coroutinen über das COROUTINES-Plugin verwenden (siehe %FigCoroutinesInterface).

%--
figure:
 source: FigCoroutinesInterface.png
 caption: Die Benutzeroberfläche des Coroutines-Plugins.
 id: FigCoroutinesInterface
--%

Wie Sie sehen können, sieht das COROUTINES-Plugin ähnlich wie das SEQUENCE-Element aus, verfügt jedoch über einige zusätzliche Optionen:

- *Duration* gibt die Gesamtdauer der Coroutinen an.
- *End after item (optional)* gibt an, dass die Coroutinen enden sollen, wenn ein bestimmtes Element beendet ist. Dadurch können Sie beispielsweise angeben, dass die Coroutinen enden sollen, wenn eine Tastendruck-Aktion erfasst wurde. Dafür wählen Sie hier ein KEYBOARD_RESPONSE-Element aus.
- Jedes Element hat eine *Startzeit*. Die meisten Elemente haben auch eine *Endzeit*. Die Endzeit gilt nicht für einmalige Elemente. Beispielsweise zeigen SKETCHPADs eine Anzeige an und werden sofort beendet. Daher haben sie keine Endzeit.

Insbesondere führt das Beispiel aus %FigCoroutinesInterface (aus dem Stop-Signal-Task-Beispiel) Folgendes aus:

- Es zeigt sofort eine Zielanzeige an.
- Wenn die Variable `stop_after` nicht leer ist, zeigt es die Stop_Signal-Anzeige nach einem Intervall an, das durch die Variable `stop_after` angegeben wird.
- Während des gesamten (2000 ms) Intervalls wird eine Tastaturantwort erfasst.

Der zeitliche Ablauf wird durch das COROUTINES-Plugin gesteuert. Daher werden die in den Elementen angegebenen Timeout- und Dauerwerte nicht verwendet. Zum Beispiel läuft in %FigCoroutinesInterface die KEYBOARD_RESPONSE 2000 ms lang, unabhängig von dem in dem Element angegebenen Timeout.


## Unterstützte Elemente

Derzeit werden die folgenden Elemente unterstützt (diese Liste ist möglicherweise nicht vollständig):

- FEEDBACK
- INLINE_SCRIPT
- KEYBOARD_RESPONSE
- LOGGER
- MOUSE_RESPONSE
- SAMPLER
- SYNTH
- SKETCHPAD

## Verwendung von inline_script-Elementen in Coroutinen

Wenn Sie ein INLINE_SCRIPT-Element in einer COROUTINE verwenden, funktioniert die Run-Phase etwas anders als Sie es gewohnt sind. Insbesondere wird die Run-Phase bei jeder Iteration der COROUTINES ausgeführt. Darüber hinaus sollte die Run-Phase nur Code enthalten, der sehr wenig Zeit zum Ausführen benötigt. Dies liegt daran, dass zeitintensive Vorgänge die COROUTINES blockieren und somit die Zeitsteuerung anderer Elemente in den COROUTINES beeinträchtigen. Um die COROUTINES zu beenden, können Sie eine `AbortCoroutines()` Ausnahme auslösen.

Angenommen, Sie haben eine COROUTINES-Struktur mit zwei KEYBOARD_RESPONSE-Elementen, *kb1* und *kb2*, und möchten die COROUTINES ausführen, bis zwei Tastendrucks erfasst wurden, mit einem Timeout von 5000 ms. Dann könnten Sie die folgende COROUTINES-Struktur erstellen:

%--
figure:
 source: FigCoroutinesTwoResponses.png
 caption: Eine Coroutine, die zwei Tastendruck-Antworten sammelt.
 id: FigCoroutinesTwoResponses
--%

Das *check_responses* INLINE_SCRIPT würde dann im Prepare-Phase zuerst beide Antwort-Variablen auf einen leeren String setzen:

```python
# Das wird zu Beginn der Coroutinen ausgeführt
response_kb1 = ''
response_kb2 = ''
```

und dann in der Run-Phase überprüfen, ob beide Variablen gesetzt wurden, und die Coroutinen abbrechen, wenn dies der Fall ist:

```python
# Werte, die kein Leerzeichen sind, sind für Python True
# Dieser Code wird viele Male ausgeführt!
if response_kb1 and response_kb2:
    raise AbortCoroutines()
```

## Run-if-Ausdrücke

Das Verhalten von Run-if-Ausdrücken in COROUTINES unterscheidet sich etwas von dem in SEQUENCE-Elementen. Insbesondere werden Run-if-Ausdrücke in COROUTINES während der Prepare-Phase ausgewertet. Weitere Informationen finden Sie unter:

- %link:prepare-run%