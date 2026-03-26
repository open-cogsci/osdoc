title: Maus- und Berührungsreaktionen
hash: d6f7dcf58a399be886fd23f0ed29e9898c1beae44c3c8f6d076e26f96471d4f0
locale: de
language: German

Mausreaktionen werden mit dem MOUSE_RESPONSE-Item erfasst. Das MOUSE_RESPONSE ist in erster Linie dafür gedacht, einzelne Mausklicks zu erfassen. Auf Geräten mit Touch-Unterstützung werden Touch-Reaktionen (TOUCH_RESPONSE-Item) im Allgemeinen auf dieselbe Weise registriert wie Maus-Taste-1-Klicks an den berührten Koordinaten, sodass oft dasselbe Item und dieselbe Logik sowohl für Maus- als auch für Touch-Eingaben verwendet werden können. Wenn Sie Mauszeiger-Trajektorien erfassen möchten, werfen Sie einen Blick auf die MOUSETRAP-Plugins:

- %link:mousetracking%

[TOC]


## Reaktionsvariablen

Das MOUSE_RESPONSE setzt die Standard-Reaktionsvariablen wie hier beschrieben:

- %link:manual/variables%

Zusätzlich sind die folgenden Variablen für Maus- und Touch-Reaktionen relevant:

| Variable | Beschreibung |
|---|---|
| `response` | Die angeklickte Maustaste. Diese wird als Zahl gespeichert (`1` = linke Taste, `2` = mittlere Taste, `3` = rechte Taste, `4` = Scrollen nach oben, `5` = Scrollen nach unten). Bei einem Timeout wird `response` auf `None` gesetzt. |
| `response_time` | Die Reaktionszeit in Millisekunden oder die registrierte Timeout-Zeit, wenn keine Reaktion erfolgte. |
| `correct` | Wird automatisch anhand der Korrektheit der Taste gesetzt: `1` für eine korrekte Maustasten-Reaktion, `0` für eine inkorrekte Maustasten-Reaktion oder ein Timeout und `undefined`, wenn keine korrekte Reaktion angegeben ist. |
| `cursor_x` | Die x-Koordinate des Klicks oder der Berührung. |
| `cursor_y` | Die y-Koordinate des Klicks oder der Berührung. |
| `cursor_roi` | Eine durch Semikola getrennte Liste von Namen von sketchpad-Elementen, die die angeklickten Koordinaten enthalten. Wenn sich Elemente überlappen, können mehrere Namen aufgeführt werden. Diese Variable gibt an, wo der Klick erfolgte; sie bestimmt `correct` nicht automatisch. |


## Namen der Maustasten

Maustasten haben sowohl eine Zahl (`1` usw.) als auch einen Namen (`left_button` usw.). Beide können verwendet werden, um korrekte und erlaubte Reaktionen anzugeben, aber die Variable `response` wird auf eine Zahl gesetzt.

- `left_button` entspricht `1`
- `middle_button` entspricht `2`
- `right_button` entspricht `3`
- `scroll_up` entspricht `4`
- `scroll_down` entspricht `5`


## Korrekte Reaktion

Das Feld *Correct response* gibt an, welche Reaktion als korrekt betrachtet wird. Nach einer korrekten Reaktion wird die Variable `correct` automatisch auf 1 gesetzt; nach einer inkorrekten Reaktion oder einem Timeout (d. h. allem anderen) wird `correct` auf 0 gesetzt; wenn keine korrekte Reaktion angegeben ist, wird `correct` auf 'undefined' gesetzt.

Sie können die korrekte Reaktion auf drei Hauptarten angeben:

- *Lassen Sie das Feld leer.* Wenn Sie das Feld *Correct response* leer lassen, prüft OpenSesame automatisch, ob eine Variable namens `correct_response` definiert wurde, und verwendet diese Variable dann, falls vorhanden, als korrekte Reaktion.
- *Geben Sie einen wörtlichen Wert ein.* Sie können explizit eine Reaktion eingeben, zum Beispiel 1. Das ist nur nützlich, wenn die korrekte Reaktion fest ist.
- *Geben Sie einen Variablennamen ein.* Sie können eine Variable eingeben, zum Beispiel '{cr}'. In diesem Fall wird diese Variable als korrekte Reaktion verwendet.

Beachten Sie, dass sich die korrekte Reaktion darauf bezieht, welche Maustaste angeklickt wurde, nicht darauf, welche Region of Interest (ROI) angeklickt wurde. Wenn die Korrektheit von der angeklickten Position statt von der Maustaste abhängt, müssen Sie die Korrektheit selbst anhand von `cursor_roi` bestimmen; siehe den Abschnitt unten für weitere Informationen über ROIs.


## Erlaubte Reaktionen

Das Feld *Allowed responses* gibt eine Liste der erlaubten Reaktionen an. Alle anderen Reaktionen werden ignoriert, außer 'Escape', wodurch das Experiment pausiert wird. Die erlaubten Reaktionen sollten eine durch Semikola getrennte Liste von Reaktionen sein, z. B. '1;3', um die linke und rechte Maustaste zu erlauben. Um alle Reaktionen zu akzeptieren, lassen Sie das Feld *Allowed responses* leer.

Beachten Sie, dass sich die erlaubten Reaktionen darauf beziehen, welche Maustaste angeklickt werden kann, nicht darauf, welche Region of Interest angeklickt werden kann (ROI); siehe den Abschnitt unten für weitere Informationen über ROIs.


%--include: include/timeout.md--%

## Coordinates and regions of interest (ROIs)</notranslate>

Die Variablen `cursor_x` und `cursor_y` enthalten die Position des Mausklicks.

Wenn Sie ein verknüpftes SKETCHPAD angeben, enthält die Variable `cursor_roi` eine durch Semikola getrennte Liste der Namen von Elementen, die die angeklickte Koordinate enthalten. Mit anderen Worten: Elemente auf dem SKETCHPAD dienen automatisch als regions of interest für den Mausklick.

Die Variable `cursor_roi` gibt an, wo der Klick erfolgt ist, während `response` angibt, welche Maustaste geklickt wurde. Wenn sich mehrere benannte Elemente an der angeklickten Position überlappen, kann `cursor_roi` mehrere Elementnamen enthalten.

Wenn die Korrektheit einer Antwort davon abhängt, welches ROI angeklickt wurde, können Sie dafür nicht die Variable `correct_response` verwenden, da sich diese nur darauf bezieht, welche Maustaste geklickt wurde. Stattdessen müssen Sie ein einfaches Skript verwenden, um die Korrektheit auf Grundlage von `cursor_roi` zu bestimmen, und bei Bedarf `correct` überschreiben.

In einem Python INLINE_SCRIPT können Sie dies wie folgt tun:

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('correct!')
    correct = 1
else:
    print('incorrect!')
    correct = 0
```

Mit OSWeb unter Verwendung eines INLINE_JAVASCRIPT können Sie dies wie folgt tun:

```javascript
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('correct!')
    correct = 1
} else {
    console.log('incorrect!')
    correct = 0
}
```

Hier ist `'my_roi'` einfach ein Beispielname eines sketchpad-Elements. Ersetzen Sie ihn in einem realen Experiment durch den Namen des ROI, das als korrekt gelten soll. Um Mehrdeutigkeiten zu vermeiden, sollten benannte Elemente innerhalb eines sketchpad eindeutig sein.


## Touch-Antworten

Auf Geräten mit Touch-Unterstützung wird jedes Tippen im Allgemeinen als mouse-button-1-Antwort an den berührten Koordinaten registriert. Das bedeutet, dass das MOUSE_RESPONSE-Item häufig sowohl für Mausklicks als auch für Touch-Eingaben ohne weitere Anpassung verwendet werden kann.

In der Praxis bedeutet dies, dass sich eine Touch-Antwort wie folgt verhält:

- Die Taste wird typischerweise als `1` registriert
- Die Position der Berührung wird in `cursor_x` und `cursor_y` gespeichert
- Wenn ein sketchpad verknüpft ist, können berührte Elemente über `cursor_roi` identifiziert werden

Dies kann für Experimente nützlich sein, die sowohl auf Desktop- als auch auf Touchscreen-Geräten laufen sollen.

### Beispiel: Touch-Antworten mit MOUSE_RESPONSE

Betrachten Sie zum Beispiel eine einfache Auswahlaufgabe, bei der zwei große sketchpad-Elemente auf der linken und rechten Seite des Bildschirms angezeigt werden. Wenn der Teilnehmer auf einem Touchscreen auf das linke Element tippt:

- wird `response` typischerweise auf `1` gesetzt
- enthalten `cursor_x` und `cursor_y` die Touch-Koordinaten
- kann `cursor_roi` den Namen des berührten Elements enthalten, zum Beispiel `left_option`

Das bedeutet, dass Touch-Eingaben auf die gleiche Weise behandelt werden können wie Maus-Eingaben. Wenn die Korrektheit vom berührten Element statt von der Taste abhängt, können Sie dieselbe oben beschriebene `cursor_roi`-Logik verwenden.

### Beispiel: Verwendung des `touch_response`-Plug-ins

Für Experimente, bei denen Sie den Bildschirm in diskrete Antwortbereiche unterteilen möchten (z. B. ein Raster aus Schaltflächen), bietet das `touch_response`-Plug-in einen einfacheren und bequemeren Ansatz als die Arbeit mit Rohkoordinaten. Es unterteilt die Anzeige in ein Raster aus Zeilen und Spalten und kodiert jede Antwort als einzelne Zahl, von links nach rechts und von oben nach unten gezählt.

Bei 2 Spalten und 3 Zeilen wird die Anzeige zum Beispiel wie folgt unterteilt:

| | Spalte 1 | Spalte 2 |
|---|---|---|
| **Zeile 1** | 1 | 2 |
| **Zeile 2** | 3 | 4 |
| **Zeile 3** | 5 | 6 |

Wenn Sie also 2 Spalten und 1 Zeile angeben, wird die Anzeige in zwei Antwortbereiche unterteilt:

| Linke Hälfte | Rechte Hälfte |
|---|---|
| `1` | `2` |

In einer einfachen Ja/Nein-Aufgabe könnten Sie Folgendes zuweisen:

- `1` = Ja
- `2` = Nein

Wenn die richtige Antwort Ja ist, setzen Sie das Feld *Correct response* auf `1`. OpenSesame setzt dann automatisch `correct` auf 1, wenn der Teilnehmer auf die linke Hälfte des Bildschirms tippt.

> [!NOTE]
> Das Plug-in `touch_response` verwendet keine benannten sketchpad-Elemente oder `cursor_roi`. Antworten werden nur als Gitterpositionen kodiert.

> [!NOTE]
> Das genaue Verhalten der Touch-Eingabe kann von der Plattform und dem Backend abhängen, die zum Ausführen des Experiments verwendet werden.

> [!NOTE]
> Das Element MOUSE_RESPONSE erfasst nur eine einzelne Touch-Antwort. Wenn mehrere Finger gleichzeitig den Bildschirm berühren, wird nur eine Antwort registriert.


%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Collecting mouse clicks and using regions of interest.
--%

## Erfassen von Mausantworten in Python

Sie können das Objekt `mouse` verwenden, um Mausantworten in Python zu erfassen:

- %link:manual/python/mouse%