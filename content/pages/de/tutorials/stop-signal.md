title: Stop-Signal-Task (Arbeiten mit coroutines)
hash: a90dc175aa27f6f7bdfc95ae0c91f7aa1f0aacaeeac9a505a63772d5a363d5d5
locale: de
language: German

[TOC]

## Über OpenSesame

OpenSesame ist ein benutzerfreundliches Programm zur Entwicklung von Verhaltensexperimenten für Psychologie, Neurowissenschaften und experimentelle Ökonomie. Für Einsteiger bietet OpenSesame eine umfassende grafische Point-and-Click-Oberfläche. Für fortgeschrittene Nutzer unterstützt OpenSesame Python (nur Desktop) und JavaScript (Desktop und Browser).

OpenSesame ist frei verfügbar unter der [General Public License v3][gpl].

## Über dieses Tutorial

Dieses Tutorial zeigt, wie man in OpenSesame mithilfe des `coroutines`-Plugins eine stop-signal task erstellt. Das Experiment basiert auf der einfachen Reaktionszeitversion von [Logan, Cowan and Davis (1984)][references]. Das Hauptziel dieses Tutorials ist nicht nur, die Aufgabe zu erstellen, sondern auch zu verstehen, wie coroutines es ermöglichen, mehrere Ereignisse auf einer einzelnen trial timeline zu platzieren.

## Ressourcen

- __Download__ — Dieses Tutorial setzt voraus, dass Sie OpenSesame Version 4.1 oder neuer verwenden und das Experiment auf dem Desktop ausführen. Sie können die neueste Version von OpenSesame hier herunterladen:
	- <https://osdoc.cogsci.nl/4.1/download/>
- __Dokumentation__ — Eine eigene Dokumentationswebsite finden Sie unter:
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Ein Support-Forum finden Sie unter:
	- <http://forum.cogsci.nl/>
- __Sigmund__ — SigmundAI ist ein KI-Assistent mit Expertenwissen zu OpenSesame und ist hier zu finden:
	- <https://sigmundai.eu/>

## Das Experiment

In diesem Experiment reagieren die Teilnehmenden so schnell wie möglich auf Buchstaben, die auf dem Bildschirm erscheinen. In den meisten Durchgängen sollen sie die Leertaste drücken, wenn ein Buchstabe erscheint. In einigen Durchgängen wird kurz nach dem Erscheinen des Buchstabens ein Ton abgespielt, und die Teilnehmenden sollen versuchen, ihre Reaktion zurückzuhalten. Das Ziel der Aufgabe ist es, die stop-signal reaction time (SSRT) zu schätzen, ein latentes Maß für die Geschwindigkeit des inhibitorischen Prozesses. Eine zuverlässige Schätzung der SSRT erfordert, dass die Teilnehmenden in go trials schnell reagieren und nur dann versuchen, ihre Reaktion zu hemmen, wenn das stop signal präsentiert wird.

Das Experiment verwendet vier Buchstaben: `E`, `F`, `H` und `L`. Die Reaktion ist immer dieselbe, unabhängig davon, welcher Buchstabe gezeigt wird. Dadurch ist die Aufgabe eine einfache Reaktionszeitversion des stop-signal paradigm.

Jeder Durchgang hat die folgende Struktur:

- Ein Fixationspunkt wird für 500 ms gezeigt.
- Nach der Fixation wird ein Buchstabe gezeigt.
- Ein Reaktionsfenster öffnet sich, wenn der Buchstabe erscheint.
- In stop trials wird nach einer kurzen Verzögerung ein 900-Hz-Ton abgespielt.
- Auf den Buchstaben folgt eine Maske.
- Die Gesamtdauer des Durchgangs ist auf 3500 ms festgelegt.

%--
figure:
 id: Fig_paradigm
 source: stop_paradigm.png
 caption: A schematic overview of the stop-signal paradigm implemented in this tutorial.
--%

Aufgaben dieser Art zeigen im Allgemeinen, dass Teilnehmende ihre Reaktion bei einer langen stop-signal delay mit geringerer Wahrscheinlichkeit hemmen als bei einer kurzen. Teilnehmende verlangsamen sich manchmal möglicherweise strategisch, wenn sie ein stop signal erwarten. Aus diesem Grund sollten die Instruktionen betonen, dass die Teilnehmenden schnell reagieren sollen und nicht auf den Ton warten sollen.

## Versuchsdesign

Dieses Design:

- ist ein Within-Subject-Design, weil alle Teilnehmenden alle Durchgangsarten absolvieren
- umfasst go trials und stop trials
- umfasst vier stop-signal delays in stop trials:
	- `50`
	- `100`
	- `150`
	- `200`
- umfasst vier Buchstaben:
	- `E`
	- `F`
	- `H`
	- `L`

Die Schleifentabelle enthält 80 Zeilen und wird viermal wiederholt, was zu vier Blöcken mit je 80 Durchgängen führt.

Wir werden das Experiment nun Schritt für Schritt aufbauen.

## Schritt 1: Erstellen Sie die Grundstruktur des Experiments

Starten Sie OpenSesame und erstellen Sie ein neues Experiment. In diesem Tutorial heißt die main sequence `experiment` und enthält:

- `new_form_consent`
- `instructions`
- `simple_rt`

Das Element `simple_rt` ist eine loop, die die trial structure des Experiments enthält.

Der Übersichtsbereich sollte jetzt so aussehen:

%--
figure:
 id: Fig_overview
 source: stop_overview.png
 caption: The overview area of the stop-signal experiment.
--%

## Schritt 2: Ein Einwilligungsformular und einen Instruktionsbildschirm hinzufügen

Das Beispiel-Experiment beginnt mit einem Einwilligungsformular. Dies ist aus technischer Sicht optional, aber in vielen realen Experimenten ist es nützlich oder notwendig, die Teilnehmenden vor Beginn der Aufgabe um ihre informierte Einwilligung zu bitten.

Nach dem Einwilligungsformular sehen die Teilnehmenden einen Instruktionsbildschirm. Die Instruktionen erklären, dass die Teilnehmenden die Leertaste drücken sollen, sobald ein Buchstabe erscheint, aber versuchen sollen, die Reaktion zu unterdrücken, wenn sie den Stoppton hören. Die Instruktionen sollten auch betonen, dass die Teilnehmenden nicht auf den Ton warten sollen, bevor sie reagieren.

Das Instruktions-Item kann so aussehen:

%--
figure:
 id: Fig_instructions
 source: stop_instructions.png
 caption: The instruction screen shown before the experiment starts.
--%

## Schritt 3: Die trial loop erstellen

Die trial-Struktur wird in einer loop namens `simple_rt` definiert. Diese loop enthält 80 Zeilen und wird viermal wiederholt. Die Reihenfolge der trials wird innerhalb jeder Wiederholung randomisiert.

Jede Zeile definiert mindestens die folgenden Variablen:

- `letters`
- `is_stop`
- `delay`
- `correct_response`

Für go trials:

- `is_stop` ist `no`
- `delay` ist `0`
- `correct_response` ist `space`

Für stop trials:

- `is_stop` ist `yes`
- `delay` ist einer von `50`, `100`, `150` oder `200`
- `correct_response` ist `None`

Dies ist eine praktische Möglichkeit, die integrierte Bewertung des `keyboard_response`-Items zu verwenden. In go trials ist das Drücken der Leertaste korrekt. In stop trials ist das Unterdrücken der Reaktion korrekt, weil die korrekte Antwort als `None` definiert ist.

Die loop-Tabelle sollte so aussehen:

%--
figure:
 id: Fig_loop
 source: stop_loop.png
 caption: The loop table that defines go trials and stop trials.
--%

## Schritt 4: Die trial-Items erstellen

Die coroutine verwendet mehrere Items, die zunächst separat erstellt werden sollten.

### 4.1 Fixation

Fügen Sie ein neues sketchpad ein und benennen Sie es in `fixation` um. Zeichnen Sie darauf einen zentralen Fixationspunkt. Obwohl sketchpads ihre eigene Dauer-Einstellung haben, wird das Timing dieses Items später durch die coroutine gesteuert.

### 4.2 Buchstabenanzeige

Fügen Sie ein neues sketchpad ein und benennen Sie es in `letter` um. Fügen Sie ein Textelement hinzu, das den Wert der Variable `{letters}` anzeigt, sodass sich der angezeigte Buchstabe von trial zu trial ändert. Die geschweiften Klammern um `{letters}` zeigen an, dass es sich nicht um wörtlichen Text handelt, sondern um den Wert der experimentellen Variable `letters`, die in der loop-Tabelle definiert ist.

Das Buchstaben-sketchpad sollte so aussehen:

%--
figure:
 id: Fig_letter
 source: stop_letter.png
 caption: The letter sketchpad, which shows the value of the variable `letters`.
--%

### 4.3 Maske

Fügen Sie ein neues sketchpad ein und benennen Sie es in `mask` um. Im aktuellen Experiment ist dieses sketchpad leer und fungiert daher hauptsächlich als Platzhalter in der trial-Timeline. Wie bei den anderen sketchpads wird sein effektives Timing später durch die coroutine bestimmt.

### 4.4 Reaktions-Item

Fügen Sie ein neues `keyboard_response`-Item ein und benennen Sie es in `resp_simple_rt` um. Setzen Sie die erlaubte Antwort auf `space`. Wenn dieses Item innerhalb der coroutine verwendet wird, wird das Reaktionsfenster durch die coroutine-Timeline statt durch die eigene Timeout-Einstellung des Items gesteuert.

Die keyboard_response-Einstellungen sollten so aussehen:

%--
figure:
 id: Fig_keyboard
 source: stop_keyboard.png
 caption: The keyboard response item configured to collect a spacebar response.
--%

### 4.5 Stoppsignal

Fügen Sie ein neues `synth`-Item ein und benennen Sie es in `stop_signal` um. Setzen Sie:

- waveform auf `sine`
- frequency auf `900`
- length auf `500`
- duration auf `0`

Eine duration von `0` stellt sicher, dass der Ton startet und die coroutine sofort fortgesetzt wird, anstatt darauf zu warten, dass der Ton zu Ende abgespielt wird.

%--
figure:
 id: Fig_synth
 source: stop_synth.png
 caption: The synth item configured to produce a 900-Hz tone lasting 500 ms.
--%

### 4.6 Logger

Fügen Sie ein neues `logger`-Item ein und benennen Sie es in `logger` um. Schalten Sie das automatische Logging aus und protokollieren Sie die kritischen Variablen manuell. Stellen Sie insbesondere sicher, dass Variablen wie `letters`, `is_stop`, `delay`, `response`, `response_time` und `correct` enthalten sind.

Die logger-Einstellungen sollten wie folgt aussehen:

%--
figure:
 id: Fig_logger
 source: stop_logger.png
 caption: The logger item configured to log the critical stop-signal variables.
--%

## Schritt 5: Das coroutines-Item hinzufügen

Fügen Sie nun ein `coroutines`-Item ein und benennen Sie es in `coroutines` um. Dieses Item definiert das Timing jedes Durchgangs auf einer gemeinsamen Zeitachse.

Setzen Sie die gesamte coroutine-Dauer auf `3500` und fügen Sie die trial-Items so hinzu, dass sie auf derselben trial-Zeitachse platziert werden.

In diesem Stadium ist es wichtig, im Hinterkopf zu behalten, dass nicht jedes OpenSesame-Item innerhalb einer coroutine verwendet werden kann. Unterstützte Items umfassen mindestens:

- `feedback`
- `inline_script`
- `keyboard_response`
- `logger`
- `mouse_response`
- `sampler`
- `synth`
- `sketchpad`

Wenn ein Item coroutines nicht unterstützt, kann es nicht auf der gemeinsamen coroutine-Zeitachse platziert werden.

## Schritt 6: Das coroutines-Item konfigurieren

Das `coroutines`-Item ist der zeitliche Kern des Experiments. Es ermöglicht, mehrere trial-Ereignisse auf einer einzigen Zeitachse zu koordinieren, sodass Präsentation, Reaktionserfassung und Sound-Planung sich zeitlich überlappen können.

Dies ist besonders nützlich für die Stop-Signal-Aufgabe. Die Fixationsanzeige erscheint zuerst, der Buchstabe erscheint später, die Versuchsperson kann reagieren, während der Durchgang weiterläuft, und der Stoppton wird nur in einigen Durchgängen und nur nach einer variablen Verzögerung präsentiert. Ein normales sequence-Item eignet sich für diese Art zeitlicher Überlappung nicht besonders gut, wohingegen eine coroutine genau für diesen Zweck ausgelegt ist.

### 6.1 Die coroutine-Zeitachse

In diesem Experiment:

- `fixation` beginnt bei `0`
- `letter` beginnt bei `500`
- `resp_simple_rt` beginnt bei `500`
- `mask` beginnt bei `1000`
- `stop_signal` beginnt bei `{delay + 500}` nur in stop-Durchgängen
- `logger` läuft am Ende des Durchgangs

Der Wert von `delay` stammt aus der loop-Tabelle. Da der Buchstabe bei `500` ms erscheint, plant der Ausdruck `{delay + 500}` das Stoppsignal relativ zum Buchstabenbeginn statt relativ zum Beginn des gesamten Durchgangs.

### 6.2 Wie `start`, `end` und `run_if` funktionieren

Jede Zeile in einer coroutine gibt an, wann ein Item ausgeführt werden soll und in manchen Fällen, wann es gestoppt werden soll.

- `start` gibt an, wann das Item beginnt, in Millisekunden nach dem Start der coroutine.
- `end` gibt an, wann das Item endet, falls das Item über ein Intervall hinweg aktiv bleibt.
- `run_if` gibt an, ob das Item überhaupt ausgeführt werden soll.

Das bedeutet, dass die coroutine mehr tut, als einfach nur Items aufzulisten. Sie definiert eine Zeitachse und platziert jedes Item auf dieser Zeitachse.

Zum Beispiel:

- `letter` beginnt bei `500`, was bedeutet, dass der Buchstabe 500 ms nach Beginn des Durchgangs erscheint.
- `resp_simple_rt` beginnt ebenfalls bei `500`, was bedeutet, dass die Reaktionserfassung beginnt, wenn der Buchstabe erscheint.
- `stop_signal` verwendet eine `run_if`-Bedingung, sodass es nur in stop-Durchgängen abgespielt wird.

Ein typischer `run_if`-Ausdruck für das Stoppsignal ist:

`is_stop == "yes"`

Dieser Ausdruck wird für jeden Durchgang ausgewertet. In stop-Durchgängen wird das synth-Item ausgeführt. In go-Durchgängen wird es übersprungen.

### 6.3 Wann `end` anwendbar ist

Nicht jedes Item in einer coroutine verwendet `end` auf dieselbe Weise.

Einige Items sind effektiv one-shot-Items. Ein sketchpad zum Beispiel bereitet eine Anzeige vor und zeigt sie an, wenn es gestartet wird. In der Praxis ist für ein solches Item normalerweise die `start`-Zeit die wichtige Einstellung. Der Anzeigewechsel erfolgt in diesem Moment, und das sketchpad selbst muss nicht in derselben Weise aktiv bleiben wie ein response-Item oder sound-Item.

Andere items bleiben über einen gewissen Zeitraum aktiv. Eine `keyboard_response` kann zum Beispiel während eines response window aktiv bleiben, und ein Sound-item kann aktiv bleiben, während Audio abgespielt wird. Für diese items ist `end` aussagekräftig, weil es bestimmt, wann das item auf der coroutine-Zeitleiste aufhört, aktiv zu sein.

Also, im Allgemeinen:

- `start` ist für alle items relevant
- `end` ist hauptsächlich für items relevant, die über ein Intervall hinweg aktiv bleiben
- `run_if` ist relevant, wenn ein item nur unter bestimmten Bedingungen ausgeführt werden soll

### 6.4 Wie sich dies auf die Stop-Signal-Aufgabe auswirkt

Im vorliegenden Experiment:

- `fixation`, `letter` und `mask` werden hauptsächlich verwendet, um die Anzeige zu bestimmten Zeitpunkten zu aktualisieren
- `resp_simple_rt` bleibt während des response window aktiv
- `stop_signal` wird nur gestartet, wenn `is_stop == "yes"`
- `logger` wird am Ende des trial ausgeführt

Das bedeutet, dass die sketchpads sich hauptsächlich auf ihre `start`-Zeitpunkte verlassen, während das response-item und das stop-signal-item besser als items verstanden werden, die während eines Teils der trial-Zeitleiste aktiv sind.

### 6.5 Wie die item-Dauer mit dem coroutine-Timing zusammenhängt

Bei der Arbeit mit coroutines ist es wichtig, sich daran zu erinnern, dass die coroutine steuert, wann items aktiv sind. Mit anderen Worten: Das effektive Timing wird durch die `start`-, `end`- und `run_if`-Einstellungen der coroutine bestimmt, nicht in erster Linie durch die duration- oder timeout-Einstellungen innerhalb der einzelnen items.

Deshalb benötigen die sketchpads in diesem Experiment keine eigenen Dauern, um die trial-Struktur festzulegen. Ihre Rolle in der Zeitleiste wird durch die coroutine bestimmt. Dieselbe Logik gilt für die `keyboard_response`: Selbst wenn das item eine eigene timeout-Einstellung hat, wird das response window effektiv durch die coroutine-Zeitleiste definiert.

Der `stop_signal`-synth veranschaulicht dies deutlich. Seine Sound-Eigenschaften, wie waveform und length, werden im synth-item selbst definiert, aber der Zeitpunkt, zu dem er startet, wird durch die coroutine festgelegt.

### 6.6 Warum der `stop_signal`-synth `duration = 0` verwendet

Das `stop_signal`-item hat eine Sound-Länge von 500 ms und eine duration von `0`. Das ist wichtig, weil es bedeutet, dass der Sound startet und die coroutine sofort weiterläuft, anstatt zu warten, bis der Sound zu Ende ist.

Dadurch kann der Ton abgespielt werden, während der Rest der coroutine-Zeitleiste weiterläuft. Genau das wird in einer Stop-Signal-Aufgabe benötigt: Das Signal muss zu einem präzisen Zeitpunkt auftreten, darf aber weder die response-Erfassung noch den Rest des trial pausieren.

Die coroutine-Einstellungen sollten so aussehen:

%--
figure:
 id: Fig_coroutines
 source: stop_coroutines.png
 caption: The coroutine item that controls the shared trial timeline.
--%

### 6.7 Warum der logger bei `3400` platziert ist

Im Beispiel-Experiment beträgt die Gesamtdauer der coroutine `3500` ms, aber sowohl `resp_simple_rt` als auch `logger` sind auf `3400` gesetzt. Das bedeutet, dass das response window bei `3400` ms geschlossen wird und der trial am selben Punkt protokolliert wird, statt ganz am Ende der coroutine.

Das ist nützlich, weil es sicherstellt, dass die response-Erfassung nicht über den Zeitpunkt hinaus fortgesetzt wird, an dem der trial protokolliert wird. Gleichzeitig bleiben die letzten `100` ms der coroutine als kleine Sicherheitsmarge ungenutzt, bevor die coroutine selbst endet.

In der Praxis bedeutet das, dass beim Ausführen des logger die relevanten response-Variablen, wie `response`, `response_time` und `correct`, bereits gesetzt wurden.

## Schritt 7: Testen Sie das Experiment

Wenn die Experimentstruktur vollständig ist, führen Sie einen Testlauf durch und überprüfen Sie, dass:

- der Fixationspunkt zuerst erscheint
- der Buchstabe nach 500 ms erscheint
- das response window mit dem Einsetzen des Buchstabens geöffnet wird
- der Stop-Ton nur in stop-trials abgespielt wird
- das Timing des Stop-Tons von `delay` abhängt
- die trial-Dauer immer 3500 ms beträgt

Es ist auch nützlich, die Logdatei zu prüfen, um zu kontrollieren, dass `letters`, `is_stop`, `delay`, `response`, `response_time` und `correct` korrekt gespeichert werden.

## Fertig

Glückwunsch, das Experiment ist abgeschlossen. Sie können jetzt einen Testlauf durchführen, indem Sie auf die blaue Doppelpfeil-Schaltfläche drücken (Tastenkürzel: `Ctrl+W`).

Unten sehen Sie eine Demonstration einer verkürzten Version des Experiments, die für Tutorial-Zwecke erstellt wurde.

<video controls width ="100%"> 
    <source src="/video/stop_demo.mp4" type="video/mp4">
</video>
<p align="center"><em>Video 1. Demonstration der abgeschlossenen Stop-Signal-Aufgabe.</em></p>

## Literatur

Logan, G. D., Cowan, W. B., & Davis, K. A. (1984). On the ability to inhibit simple and choice reaction time responses: A model and a method. *Journal of Experimental Psychology: Human Perception and Performance*, *10*(2), 276–291.

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324.

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html