title: OSWeb
hash: d0eed8ce85e569f15d774ecf9cc4dff90b02dffd12470987bae00484d0c05865
locale: de
language: German

[TOC]


## Über OSWeb

OSWeb ist eine Online-Laufzeitumgebung für OpenSesame-Experimente. Es handelt sich um eine JavaScript-Bibliothek, die OpenSesame-Experimente in einem Browser ausführt. Um OSWeb zu verwenden, benötigen Sie das `opensesame-extension-osweb`-Paket, das bereits in den OpenSesame-Distributionen für Windows und macOS vorinstalliert ist.


## Durchführung eines Experiments in einem Web-Browser

Um ein Experiment in einem Web-Browser mit OSWeb durchzuführen, folgen Sie diesen Schritten:

1. Öffnen Sie die Eigenschaften des Experiments und wählen Sie 'In einem Browser mit OSWeb (osweb)' im Abschnitt 'Experiment durchführen' aus.
2. Klicken Sie auf eine der 'Start'-Schaltflächen, um das Experiment zu starten.
3. Wenn das Experiment nicht mit OSWeb kompatibel ist, erscheint eine Fehlermeldung, die die Kompatibilitätsprobleme erläutert. (Weitere Details finden Sie im Abschnitt 'Unterstützte Funktionen'.)
4. Wenn es keine Kompatibilitätsprobleme gibt, wird das Experiment in einem neuen Browserfenster geöffnet. Beachten Sie, dass das Experiment, obwohl es in einem Webbrowser läuft, immer noch lokal auf Ihrem eigenen Computer ausgeführt wird. Um das Experiment online zu hosten, müssen Sie es auf [JATOS](%url:jatos%) veröffentlichen.
5. Wenn das Experiment abgeschlossen ist, werden die Daten im `.json`-Format heruntergeladen. Diese Datendatei kann dann [in das `.xlsx` oder `.csv` Format konvertiert](%url:manual/osweb/data%) werden für weitere Analysen.


%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: Open the Experiment Properties and select 'In a browser with OSWeb (osweb)' under 'Run experiment'.
--%


## OSWeb Kontrollpanel

Für mehr Kontrolle über OSWeb-Experimente, können Sie das OSWeb und JATOS Kontrollpanel aus dem Tools-Menü aufrufen. Dieses Panel bietet eine Reihe von Konfigurationsoptionen:

- **Mögliche Teilnehmernummern:** Wenn Sie ein Experiment innerhalb von JATOS durchführen, wird eine Teilnehmernummer zufällig aus dieser Liste ausgewählt. Sie können einzelne Nummern mit Kommas angeben (z.B. '1,2,3') oder Nummernbereiche (z.B. '1-10'). Wenn Sie ein Experiment innerhalb von OpenSesame durchführen, gilt diese Option nicht, da die Teilnehmernummer beim Start des Experiments festgelegt wird.
- **Browser im Vollbildmodus öffnen:** Diese Option bestimmt, ob der Browser in den Vollbildmodus wechseln soll, wenn ein Experiment innerhalb von JATOS beginnt. Wenn Sie ein Experiment direkt aus OpenSesame starten, wird diese Option ignoriert; stattdessen können Sie das Experiment im Vollbildmodus durch Drücken der regulären Start-Schaltfläche durchführen, während die Quick-Start-Schaltfläche den Vollbildmodus nicht aktiviert.
- **OSWeb-Begrüßungsbildschirm anzeigen:** Dieser Umschalter steuert, ob Teilnehmer einen Begrüßungsbildschirm vor dem Start des Experiments sehen. Der Begrüßungsbildschirm kann den Teilnehmern wichtige Informationen vermitteln. Darüber hinaus hat er einen technischen Zweck—aufgrund von Browser-Sicherheitsrichtlinien ist die Wiedergabe von Medien und bestimmte Funktionen nur verfügbar, wenn das Experiment durch eine Benutzeraktion initiiert wird. Daher ist es generell empfehlenswert, diese Option aktiviert zu lassen.
- **Kompatibilitätsprüfung umgehen:** Wenn Sie diese Option aktivieren, können Sie das Experiment durchführen, auch wenn die OSWeb-Kompatibilitätsprüfung fehlschlägt. Beachten Sie, dass dies Kompatibilitätsprobleme nicht automatisch löst!
- **Begrüßungstext:** In diesem Feld können Sie die Begrüßungsnachricht anpassen, die den Teilnehmern auf dem Begrüßungsbildschirm angezeigt wird.
- **Externe Bibliotheken:** In diesem Feld können Sie externe Bibliotheken angeben, die mit Ihrem Experiment geladen werden sollten. Die Verwendung von externen Bibliotheken wird im folgenden Abschnitt genauer erklärt.


%--
figure:
 id: FigOSWebControlPanel
 source: osweb-control-panel.png
 caption: The OSWeb and JATOS control panel offers a range of configuration options for your OSWeb experiments.
--%


## Unterstützte Funktionen

Wenn Sie das Experiment innerhalb von OpenSesame durchführen, wird automatisch eine Kompatibilitätsprüfung durchgeführt. Diese Prüfung ist jedoch recht oberflächlich. Eine vollständigere Übersicht der unterstützten Funktionen finden Sie unten.

- `advanced_delay`
- `feedback`
    - Siehe `sketchpad`
- `form_consent` (unterstützt >= v1.4)
- `form_text_display` (unterstützt >= 1.4)
- `form_text_input` (unterstützt >= 1.4)
    - Nicht unterstützt: Vollbildmodus
- `form_multiple_choice` (unterstützt >= 1.4)
- `inline_html` (unterstützt >= 1.4)
- `inline_javascript`
- `keyboard`
    - Nicht unterstützt: Tastenfreigabe
    - Nicht unterstützt: HSV, HSL und CIELab Farbräume
- `logger`
- `loop`
    - Nicht unterstützt: Fortsetzen nach Pause
    - Nicht unterstützt: Deaktivierung der Evaluierung im ersten Zyklus
    - Nicht unterstützt: Einschränkungen (Pseudorandomisierung)
    - Unterstützt >= 1.4: Dateiquelle
- `mouse`
    - Nicht unterstützt: Mausfreigabe
    - Nicht unterstützt: verknüpftes Skizzenpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Unterstützt >= 1.4.12: Panning, Tonhöhe und Einblenden
    - Unterstützt >= 1.4.12: Sound-Wiedergabe auf Safari auf Mac OS oder jedem Browser auf iOS
    - Nicht unterstützt: nach stoppen
- `sequence`
- `sketchpad`
    - Nicht unterstützt: benannte Elemente
    - Unterstützt >= 1.4: Bildrotation
    - Nicht unterstützt: HSV, HSL und CIELab Farbräume
- `touch_response`

Die Kompatibilitätsprüfung kann auch Fehler des folgenden Typs anzeigen:

> Die Vorbereitungsphase für das Element new_logger wird mehrmals hintereinander aufgerufen

Dieser Fehler resultiert aus der Struktur des Experiments und insbesondere aus der Verwendung von verlinkten Kopien. Es ist nicht immer einfach zu verstehen, woher dieser Fehler kommt, aber Sie können mehr über die Prepare-Run-Strategie in [diesem Artikel](%url:prepare-run%) lesen. Als Workaround können Sie die problematischen Elemente in eine Dummy-Schleife setzen, das heißt, eine Schleife, die das Element einfach einmal aufruft.

## Einbeziehung externer JavaScript-Pakete

Sie können externe JavaScript-Pakete einbeziehen, indem Sie URLs zu diesen Paketen (eine URL pro Zeile) in das Eingabefeld mit der Bezeichnung 'Externe JavaScript-Bibliotheken' eingeben. Diese Pakete werden dann mit `<script>`-Tags im Kopfteil des HTML eingebunden.

Zum Beispiel können Sie [WebGazer](%url:webgazer%) für den Aufruf im Browser einbinden, indem Sie den folgenden Link eingeben:

```
https://webgazer.cs.brown.edu/webgazer.js
```

## Debugging

Siehe:

- %link:debugging%