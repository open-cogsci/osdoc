title: Mausreaktionen
hash: 047288a3fddc3e00aa932fe2d7d9f62628bd9d8e5e6d54ceac2b7b5a836e6f0f
locale: de
language: German

Mausklicks werden mit dem MOUSE_RESPONSE-Element aufgenommen. MOUSE_RESPONSE ist in erster Linie dafür vorgesehen, einzelne Mausklicks zu sammeln. Wenn Sie die Trajektorien des Mauszeigers erfassen möchten, schauen Sie sich die MOUSETRAP-Plugins an:

- %link:mousetracking%

[TOC]

## Antwortvariablen

Das MOUSE_RESPONSE-Element definiert die Standardantwortvariablen, wie hier beschrieben:

- %link:manual/variables%

## Maustastennamen

Maustasten haben eine Nummer (`1`, usw.) sowie einen Namen (`left_button`, usw.). Beide können verwendet werden, um korrekte und erlaubte Antworten anzugeben, aber die Variable `response` wird auf eine Nummer gesetzt.

- `left_button` entspricht `1`
- `middle_button` entspricht `2`
- `right_button` entspricht `3`
- `scroll_up` entspricht `4`
- `scroll_down` entspricht `5`

## Korrekte Antwort

Das Feld *Korrekte Antwort* gibt an, welche Antwort als korrekt betrachtet wird. Nach einer korrekten Antwort wird die Variable `correct` automatisch auf 1 gesetzt; nach einer falschen Antwort oder einem Timeout (d.h. alles andere) wird `correct` auf 0 gesetzt; wenn keine korrekte Antwort angegeben ist, wird `correct` auf 'undefined' gesetzt.

Sie können die korrekte Antwort auf drei Hauptwegen angeben:

- *Das Feld leer lassen.* Wenn Sie das Feld *Korrekte Antwort* leer lassen, überprüft OpenSesame automatisch, ob eine Variable namens `correct_response` definiert wurde und wenn ja, verwendet diese Variable für die korrekte Antwort.
- *Einen Literalwert eingeben.* Sie können eine Antwort explizit eingeben, wie zum Beispiel 1. Dies ist nur nützlich, wenn die korrekte Antwort festgelegt ist.
- *Einen Variablennamen eingeben.* Sie können eine Variable eingeben, wie `{cr}`. In diesem Fall wird diese Variable für die korrekte Antwort verwendet.

Beachten Sie, dass die korrekte Antwort sich darauf bezieht, welche Maustaste geklickt wurde, und nicht darauf, welche Region von Interesse (ROI) geklickt wurde; siehe untenstehender Abschnitt für weitere Informationen über ROIs.

## Erlaubte Antworten

Das Feld *Erlaubte Antworten* gibt eine Liste von erlaubten Antworten an. Alle anderen Antworten werden ignoriert, außer 'Escape', was das Experiment pausiert. Die erlaubten Antworten sollten eine Semikolon-getrennte Liste von Antworten sein, wie '1;3', um die linke und rechte Maustaste zu erlauben. Um alle Antworten zu akzeptieren, lassen Sie das Feld *Erlaubte Antworten* leer.

Beachten Sie, dass die erlaubten Antworten sich darauf beziehen, welche Maustaste geklickt werden kann, und nicht darauf, welche Region von Interesse (ROI) geklickt werden kann; siehe untenstehender Abschnitt für weitere Informationen über ROIs.

%--include: include/timeout.md--%</notranslate>

## Koordinaten und Regionen von Interesse (ROIs)

Die Variablen `cursor_x` und `cursor_y` halten die Position des Mausklicks.

Wenn Sie ein verlinktes SKETCHPAD angeben, wird die Variable `cursor_roi` eine durch Kommas getrennte Liste von Namen von Elementen enthalten, die die geklickten Koordinaten enthalten. Mit anderen Worten, Elemente auf dem SKETCHPAD dienen automatisch als Regionen von Interesse für den Mausklick.

Wenn die Korrektheit einer Antwort davon abhängt, welche ROI geklickt wurde, können Sie dafür nicht die Variable `correct_response` verwenden, da diese derzeit nur darauf verweist, welche Maustaste geklickt wurde. Stattdessen müssen Sie ein einfaches Skript verwenden.

In einem Python INLINE_SCRIPT können Sie dies folgendermaßen tun:

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('korrekt!')
    correct = 1
else:
    print('falsch!')
    correct = 0
```

Mit OSWeb unter Verwendung eines INLINE_JAVASCRIPT können Sie dies folgendermaßen tun:

```js
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('korrekt!')
    correct = 1
} else {
    console.log('falsch!')
    correct = 0
}
```

%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Sammeln von Mausklicks und verwenden von Regionen von Interesse.
--%

## Mausantworten in Python sammeln

Sie können das `mouse`-Objekt verwenden, um Mausantworten in Python zu sammeln:

- %link:manual/python/mouse%