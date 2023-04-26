title: Die Prepare-Run-Strategie
hash: e91e8e57fbac78eb05547ef89cd9bbb3ae1f177e7d96e295fb31c6e7da95965d
locale: de
language: German

[TOC]

## Über

Experimente bestehen in der Regel aus kurzen Intervallen ('Versuche'), während denen Teilnehmer Stimuli wahrnehmen und eine Aufgabe ausführen. Die Zeitsteuerung sollte während eines Versuchs kontrolliert werden, aber einige unvorhersehbare Variation in der Dauer des Intervalls zwischen den Versuchen ist akzeptabel. Daher ist es eine gute Strategie, zeitintensive Aufgaben vor einem Versuch durchzuführen und die während eines Versuchs ausgeführten Operationen auf ein Minimum zu reduzieren.

OpenSesame macht dies, indem jedes Element aus einem SEQUENCE-Element zweimal aufgerufen wird. Dies ist die *Prepare-Run-Strategie*:

- Während der Prepare-Phase haben die Elemente die Möglichkeit, sich vorzubereiten. Zum Beispiel erzeugt ein SYNTH einen Ton (spielt ihn aber nicht ab); und ein SKETCHPAD zeichnet eine Leinwand (zeigt sie aber nicht an).
- Während der Run-Phase tun die Elemente so wenig wie möglich. Zum Beispiel spielt ein SYNTH eine zuvor vorbereitete Ton ab; und ein SKETCHPAD zeigt eine zuvor vorbereitete Leinwand an.

Dies reduziert das Risiko von Timing-Fehlern. Die Prepare-Run-Strategie ist auf der Ebene von SEQUENCE-Elementen implementiert, die in der Regel die zeitkritischen Teile eines Experiments enthalten. Das bedeutet, dass vor dem Start einer SEQUENCE eine unvorhersehbare zeitliche Streuung vorhanden ist.

## Elementspezifische Hinweise

### Loop-Elemente

Ein LOOP-Element wird nicht im Voraus vorbereitet. Es ist wichtig, dies zu berücksichtigen, wenn Sie eine Schleife verwenden, um zeitkritische Teile zu implementieren. Zum Beispiel könnten Sie versucht sein, einen RSVP-Stream mit einem LOOP-Element wie folgt zu implementieren:

~~~text
rsvp_loop-Element (4 Zyklen)
- stimulus_element
~~~

In dieser Konstruktion wird *stimulus_element* abwechselnd viermal vorbereitet und ausgeführt, wie folgt:

~~~text
stimulus_element vorbereiten
stimulus_element ausführen
stimulus_element vorbereiten
stimulus_element ausführen
stimulus_element vorbereiten
stimulus_element ausführen
stimulus_element vorbereiten
stimulus_element ausführen
~~~

Daher müssen Sie überprüfen, ob die Vorbereitung von *stimulus_element* keine Timing-Fehler verursacht.

### Sequence-Elemente

Alle Elemente, die Teil einer SEQUENCE sind, werden im Voraus vorbereitet. Daher wird die folgende Konstruktion ...

~~~text
trial_sequence
- fixation_sketchpad
- target_sketchpad
- keyboard_response
- logger
~~~

... wie folgt ausgeführt ...

~~~text
fixation_sketchpad vorbereiten
target_sketchpad vorbereiten
keyboard_response vorbereiten
logger vorbereiten
fixation_sketchpad ausführen
target_sketchpad ausführen
keyboard_response ausführen
logger ausführen
~~~

### Sketchpad- und Feedback-Elemente

SKETCHPAD- und FEEDBACK-Elemente unterscheiden sich darin, wann sie vorbereitet werden. Für SKETCHPADs erfolgt die Vorbereitung während der Prepare-Phase; für FEEDBACK-Elemente erfolgt die Vorbereitung erst während der Run-Phase.

Weitere Informationen finden Sie unter:

- %link:manual/stimuli/visual%

### Synth- und Sampler-Elemente

Bei SYNTH- und SAMPLER-Elementen wird der Ton während der Prepare-Phase erzeugt und vorab geladen.

### Inline_script-Elemente

In einem INLINE_SCRIPT-Element können Sie wählen, wie Sie die Run- und Prepare-Strategie implementieren möchten. Im Allgemeinen ist es ratsam, die folgenden Richtlinien einzuhalten:

- Zeitintensive, vorbereitende Funktionen erfolgen in der Prepare-Phase. Zum Beispiel das Erstellen von Leinwandobjekten und das Erzeugen von Tönen.
- Eine minimale Menge an Code wird in der Run-Phase verwendet. Zum Beispiel nur das Anzeigen einer zuvor vorbereiteten Leinwand.

### Andere Elemente und Plugins

Im Allgemeinen sollten Elemente dem Prinzip folgen, möglichst viel zeitintensive Vorbereitung während der Prepare-Phase durchzuführen und die Run-Phase zu minimieren. Jedes Plugin ist jedoch unterschiedlich implementiert. Wenn Sie sich in einem speziellen Fall unsicher sind, stellen Sie bitte eine Anfrage im Forum.

## Bedingte Ausdrücke (run if, show if, break if usw.)

In SEQUENCE-Elementen wird der 'Run if'-Zustand im letzten Moment, während der Run-Phase, ausgewertet. Daher können Sie eine Bedingung wie `correct == 0` verwenden, die von den Ergebnissen eines KEYBOARD_RESPONSE-Elements abhängt, das direkt davor aufgerufen wurde. Es ist wichtig zu beachten, dass der 'Run if'-Ausdruck *nur* für die Run-Phase eines Elements gilt – die Prepare-Phase wird *immer* ausgeführt.

In COROUTINES-Elementen wird die 'Ausführen, wenn'-Bedingung während der Prepare-Phase ausgewertet. Daher können die Bedingungen nicht von Ereignissen abhängen, die während der Ausführung der COROUTINES auftreten.

In SKETCHPAD-Elementen wird die 'Anzeigen, wenn'-Bedingung während der Prepare-Phase ausgewertet, wenn die Leinwand erstellt wird. In FEEDBACK-Elementen wird die 'Anzeigen, wenn'-Bedingung während der Run-Phase ausgewertet (weil die Leinwand nur in der Run-Phase erstellt wird).