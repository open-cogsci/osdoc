title: Mausreaktionen
hash: 9e348c65c44cf1d0e1e152976c013b0a235f432d16ceeb3fff09001f8c9d0e7b
locale: de
language: German

Mausantworten werden mit dem MOUSE_RESPONSE-Element erfasst. Das MOUSE_RESPONSE dient hauptsächlich zur Erfassung einzelner Mausklicks. Wenn Sie die Bewegung des Mauszeigers erfassen möchten, sehen Sie sich die MOUSETRAP-Plugins an:

- %link:mousetracking%

[TOC]

## Antwortvariablen

Die MOUSE_RESPONSE setzt die Standard-Antwortvariablen, wie hier beschrieben:

- %link:manual/variables%

## Namen der Maustasten

Mausknöpfe haben sowohl eine Nummer (z.B. `1`) als auch einen Namen (z.B. `left_button`). Beides kann verwendet werden, um korrekte und erlaubte Antworten anzugeben, aber die `response`-Variable wird auf eine Nummer eingestellt:

- `left_button` entspricht `1`
- `middle_button` entspricht `2`
- `right_button` entspricht `3`
- `scroll_up` entspricht `4`
- `scroll_down` entspricht `5`

## Korrekte Antwort

Das Feld *Korrekte Antwort* gibt an, welche Antwort als korrekt angesehen wird. Nach einer korrekten Antwort wird die Variable `correct` automatisch auf 1 gesetzt; nach einer falschen Antwort oder einem Timeout (also allem anderen) wird `correct` auf 0 gesetzt; wenn keine korrekte Antwort angegeben ist, wird `correct` auf "undefined" gesetzt.

Sie können die korrekte Antwort auf drei Hauptweisen angeben:

- *Lassen Sie das Feld leer.* Wenn Sie das Feld "Korrekte Antwort" leer lassen, überprüft OpenSesame automatisch, ob eine Variable mit dem Namen `correct_response` definiert wurde, und verwendet diese Variable, wenn ja, für die korrekte Antwort.
- *Geben Sie einen Literalwert ein.* Sie können eine Antwort explizit eingeben, wie z.B. 1. Dies ist nur sinnvoll, wenn die korrekte Antwort festgelegt ist.
- *Geben Sie einen Variablennamen ein.* Sie können eine Variable eingeben, wie z.B. '{cr}'. In diesem Fall wird diese Variable für die korrekte Antwort verwendet.

## Erlaubte Antworten

Das Feld *Erlaubte Antworten* gibt eine Liste der erlaubten Antworten an. Alle anderen Antworten werden ignoriert, außer "Escape", das das Experiment unterbricht. Die erlaubten Antworten sollten eine semikolongetrennte Liste von Antworten sein, wie z.B. "1;3", um die linke und rechte Maustaste zuzulassen. Um alle Antworten zu akzeptieren, lassen Sie das Feld *Erlaubte Antworten* leer.

%--include: include/timeout.md--%

## Koordinaten und Interessensbereiche (ROIs)

Die Variablen `cursor_x` und `cursor_y` enthalten die Position des Mausklicks.

Wenn Sie einen verknüpften SKETCHPAD angeben, enthält die Variable `cursor_roi` eine kommaseparierte Liste von Namen der Elemente, die die angeklickte Koordinate enthalten. Mit anderen Worten: Elemente auf dem SKETCHPAD dienen automatisch als Interessensbereiche für den Mausklick.

%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Mausklicks sammeln und Interessensbereiche verwenden.
--%

## Mausantworten in Python sammeln

Sie können das `mouse`-Objekt verwenden, um Mausantworten in Python zu erfassen:

- %link:manual/python/mouse%
