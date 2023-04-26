title: Gegenbalancierung
hash: f746c6dcc8ded61b700e84340fafff7a9ab6a1c217365d1ff9b97ab344438cd2
locale: de
language: German

Das Gegenbalancieren ist eine Möglichkeit, Störvariablen aus einem Experiment zu entfernen, indem man leicht unterschiedliche Aufgaben für verschiedene Gruppen von Teilnehmern anbietet. Dies klingt abstrakt, daher betrachten wir zwei Beispiele.

[TOC]

### Beispiel 1: Gegenbalancieren der Antwortregel

Stellen Sie sich ein lexikalisches Entscheidungsexperiment vor, in dem die Teilnehmer Wörter als Verben klassifizieren, indem sie mit ihrer linken Hand 'z' drücken, oder als Substantive, indem sie mit ihrer rechten Hand 'm' drücken. Dieses Design hat ein Problem: Wenn Sie feststellen, dass Teilnehmer schneller auf Substantive als auf Verben reagieren, könnte dies daran liegen, dass Substantive schneller verarbeitet werden als Verben oder weil Teilnehmer schneller mit ihrer rechten Hand als mit ihrer linken Hand reagieren. Sie können dieses Problem beheben, indem Sie die Antwortregel gegenbalancieren.

Für gerade Teilnehmernummern:

- Verb → z
- Substantiv → m

Für ungerade Teilnehmernummern:

- Verb → m
- Substantiv → z

### Beispiel 2: Rotierende Stimulusbedingungen

Nehmen Sie ein maskiertes Priming-Experiment, bei dem die Teilnehmer Zielwörter laut vorlesen. In jedem Durchgang wird das Zielwort von einer von drei Arten von Priming-Wörtern vorangestellt:

- Ein nicht verwandtes Prime, z.B. Priming mit 'Beere' für das Ziel 'Haus'.
- Ein orthografisch verwandtes Prime, z.B. Priming mit 'Maus' für das Ziel 'Haus'
- Ein semantisch verwandtes Prime, z.B. Priming mit 'Garten' für das Ziel 'Haus'

Um Wiederholungseffekte zu vermeiden, möchten Sie Zielwörter nur einmal pro Teilnehmer anzeigen. Daher erstellen Sie drei verschiedene Sets von Zielwörtern, eines für jeden Prime-Typ. Dies ist ein Between-Word-Design, das eine geringere statistische Aussagekraft hat als ein Within-Word-Design, bei dem jedes Zielwort in jeder Bedingung vorkommt. (Aus demselben Grund sind between-subject-Designs weniger leistungsstark als within-subject-Designs.)

Sie können das Gegenbalancieren verwenden, um dieses Experiment in ein Within-Word-Design umzuwandeln, indem Sie die Bedingung, in der jedes Wort bei den Teilnehmern vorkommt, 'rotieren'. Wir haben drei Bedingungen und daher auch drei Gruppen von Teilnehmern:

- Teilnehmer 1, 4, 7 usw.
    - Wort A in Bedingung 1
    - Wort B in Bedingung 2
    - Wort C in Bedingung 3
- Teilnehmer 2, 5, 8 usw.
    - Wort A in Bedingung 2
    - Wort B in Bedingung 3
    - Wort C in Bedingung 1
- Teilnehmer 3, 6, 9 usw.
    - Wort A in Bedingung 3
    - Wort B in Bedingung 1
    - Wort C in Bedingung 2

## Gegenbalancieren implementieren

### Verwendung der Teilnehmernummer

Wenn Sie ein Experiment in OpenSesame auf dem Desktop ausführen, werden Sie nach einer Teilnehmernummer gefragt. Wenn Sie ein Experiment online ausführen, wird eine Teilnehmernummer zufällig aus der Liste der möglichen Teilnehmernummern ausgewählt, die Sie in der [OSWeb-Erweiterung](%url:osweb) angegeben haben. (Das bedeutet, dass Sie für Online-Experimente nicht sicherstellen können, dass die Teilnehmerzahl für die verschiedenen Bedingungen, die Sie gegenbalancieren möchten, genau gleich ist, zumindest nicht, wenn Sie sich auf die Teilnehmernummer verlassen.)

Diese Teilnehmernummer ist als experimentelle Variable `subject_nr` verfügbar. Zusätzlich hat die experimentelle Variable `subject_parity` den Wert 'odd' oder 'even', abhängig davon, ob die Teilnehmernummer ungerade oder gerade ist. Angenommen, Sie möchten die Antwortregel wie in Beispiel 1 gegenbalancieren, könnten Sie das folgende INLINE_SCRIPT zu Beginn des Experiments hinzufügen.

```python
if subject_parity == 'odd':
    verb_response = 'z'
    noun_response = 'm'
else:
    verb_response = 'm'
    noun_response = 'z'
```

Oder, wenn Sie ein OSWeb-Experiment erstellen, fügen Sie das folgende INLINE_JAVASCRIPT zu Beginn des Experiments hinzu:

```javascript
if (subject_parity === 'odd') {
    verb_response = 'z'
    noun_response = 'm'
} else {
    verb_response = 'm'
    noun_response = 'z'
}
```

Jetzt setzen Sie in Ihrer *block_loop* `correct_response` anstelle eines festen Wertes auf eine Variable: `{verb_response}` oder `{noun_response}`. Sie können sich das *lexikalische Entscheidungsaufgabe*-Beispiel ansehen, um zu sehen, wie das funktioniert (Menü -> Tools -> Beispiel-Experimente).

### Verwendung von Batch Session Data (nur JATOS und OSWeb)

Beim Ausführen eines OSWeb-Experiments, das auf JATOS gehostet wird, können Sie [Batch Session Data](https://www.jatos.org/jatos.js-Reference.html#functions-to-access-the-batch-session) verwenden. Dabei handelt es sich um Daten, die zwischen allen experimentellen Sitzungen geteilt werden, die Teil desselben Worker-Batches sind. Daher können Sie diese Daten verwenden, um eine Liste von Bedingungen zu definieren, die auf die Teilnehmer verteilt werden sollen. Zu Beginn jeder experimentellen Sitzung wird eine Bedingung aus dieser Liste entfernt und für die aktuelle Sitzung verwendet. Dies ist der fortschrittlichste Weg, um das Gegengewicht (Counterbalancing) für OSWeb-Experimente, die auf JATOS gehostet werden, zu implementieren.

Sie können hier ein Vorlagen-Experiment herunterladen:

- %static:attachments/counterbalancing-osweb-jatos.osexp%

Beim Ausführen von JATOS ruft das Experiment eine einzelne Bedingung aus den Batch Session Data ab (siehe unten) und registriert diese als die experimentelle Variable `condition`. Bei einem Testdurchlauf wird `condition` auf einen Standardwert eingestellt, der am Ende von *init_condition* festgelegt ist.

Das Experiment selbst sollte in der *experiment* SEQUENCE implementiert werden, die in der Vorlage nur das *show_condition* SKETCHPAD enthält (siehe %FigCounterbalancingOSWebJATOS).

%--
figure:
    source: counterbalancing-osweb-jatos.png
    id: FigCounterbalancingOSWebJATOS
    caption: |
        Der Übersichtsbereich des template Experiments zur Implementierung von Counterbalancing mit JATOS Batch Session Data.
--%

Beim Importieren des Experiments in JATOS sollten alle Bedingungen in den Batch Session Data als `pending` Liste (unter Worker & Batch Manager; siehe %FigBatchSessionData) angegeben werden. Jede Bedingung von `pending` entspricht einer einzigen experimentellen Sitzung; wenn also Bedingung `a` für zwei experimentelle Sitzungen verwendet werden soll, dann muss `a` zweimal in der `pending` Liste vorkommen. Die Bedingungen werden in der Reihenfolge verwendet, in der sie definiert sind.

%--
figure:
    source: batch-session-data.png
    id: FigBatchSessionData
    caption: |
        Die Bedingungen sollten in den Batch Session Data in JATOS angegeben werden.
--%

Zu Beginn einer experimentellen Sitzung wird eine einzelne Bedingung von `pending` nach `started` verschoben. (Wenn die Liste `pending` leer ist, wird der Teilnehmer darüber informiert, dass er/sie nicht mehr an dem Experiment teilnehmen kann.) Am Ende der experimentellen Sitzung wird die Bedingung der Liste `finished` angehängt.

Um dies zu verdeutlichen, nehmen wir an, dass Sie die Batch Session Data wie in %FigBatchSessionData gezeigt definiert haben. Dann werden vier experimentelle Sitzungen gestartet, aber die zweite experimentelle Sitzung mit Bedingung `a` wird nie beendet, zum Beispiel weil der Teilnehmer den Browser während des Experiments schließt. Die Batch Session Data sehen dann so aus wie in %FigBatchSessionAfter:

%--
figure:
    source: batch-session-data-after.png
    id: FigBatchSessionAfter
    caption: |
        Die Batch Session Data, nachdem alle Bedingungen verbraucht wurden. Eine Sitzung mit Bedingung `a` wurde nie beendet.
--%

Aus den Batch Session Data geht hervor, dass eine experimentelle Sitzung mit Bedingung `a` begonnen, aber nie beendet wurde. Um dennoch eine experimentelle Sitzung mit dieser Bedingung zu sammeln, müssen Sie manuell ein neues `a` zur `pending` Liste hinzufügen und eine neue Sitzung erfassen.