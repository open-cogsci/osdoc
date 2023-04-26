title: Grad der Sehwinkel
hash: b9febd85c8491dfed24e738cf632d1d0051f391ed1835b760f8fbf04f7846eef
locale: de
language: German

Sie werden oft sehen, dass die Größe visueller Reize in Grad des Sehwinkels (°) ausgedrückt wird. Sehwinkel geben den Winkel zwischen den geraden Linien von den Endpunkten des Reizes bis zur Linse des Auges wieder. Daher hängt der Sehwinkel mit der Größe zusammen, die ein Reiz auf der Netzhaut einnimmt, aber nur indirekt: Es handelt sich um einen Winkel, der von der Augenlinse aus gemessen wird, wie in %FigEye dargestellt.

[TOC]

%--
figure:
 id: FigEye
 source: fig-eye.png
 caption: Eine schematische Darstellung von Grad des Sehwinkels. (Bild angepasst von [WikiMedia Commons](http://commons.wikimedia.org/wiki/File:Schematic_diagram_of_the_human_eye.svg).)
--%

Der Grund für die Verwendung dieser etwas ungewöhnlichen Größenangabe liegt darin, dass sie die wahrgenommene Größe eines Reizes widerspiegelt, die in psychologischen Experimenten oft wichtiger ist als die tatsächliche Größe. Wenn Sie beispielsweise ein Bild mit einer tatsächlichen Breite von 100 Pixeln auf dem Monitor präsentieren, kann der Sehwinkel 3° entsprechen. Wenn Sie den Monitor weiter weg bewegen, verringert sich der Sehwinkel des Bildes auf beispielsweise 2°. Der Sehwinkel zeigt somit, dass der Abstand zwischen einem Reiz und einem Beobachter wichtig ist. 

Siehe auch:

- <http://en.wikipedia.org/wiki/Visual_angle>

## Pixel in Sehwinkel umrechnen

Um Pixel in Sehwinkel umzurechnen, müssen Sie drei Dinge wissen:

- `h` ist die Höhe des Monitors in Zentimetern, die Sie mit einem Lineal messen können. (z.B. 25 cm)
- `d` ist der Abstand zwischen dem Teilnehmer und dem Monitor in Zentimetern, den Sie ebenfalls mit einem Lineal messen können. (z.B. 60cm)
- `r` ist die vertikale Auflösung des Monitors in Pixeln, die Sie in den Anzeigeeinstellungen Ihres Betriebssystems finden können (z.B., 768 px)

Sie können die Winkelausdehnung Ihres Reizes wie unten gezeigt berechnen. Sie können dieses Skript im OpenSesame Debug-Fenster ausführen. Natürlich müssen Sie alle Werte so einsetzen, dass sie Ihrem Setup entsprechen. Beachten Sie, dass einem einzelnen Sehwinkel typischerweise 30 - 60 Pixel entsprechen, abhängig von der Entfernung und Größe des Monitors. Umgekehrt entspricht ein einzelnes Pixel typischerweise 0,01 bis 0,03 Sehwinkel. Wenn Sie Werte erhalten, die weit außerhalb dieses Bereichs liegen, haben Sie wahrscheinlich einen Fehler gemacht.

```python
from math import atan2, degrees

h = 25           # Monitorhöhe in cm
d = 60           # Abstand zwischen Monitor und Teilnehmer in cm
r = 768          # Vertikale Auflösung des Monitors
size_in_px = 100 # Die Reizgröße in Pixeln
# Berechnen Sie die Anzahl der Grad, die einem einzelnen Pixel entsprechen. Dies wird
# im Allgemeinen ein sehr kleiner Wert sein, etwa 0,03.
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'{deg_per_px} Grad entsprechen einem einzelnen Pixel')
# Berechnen Sie die Größe des Reizes in Grad
size_in_deg = size_in_px * deg_per_px
print(f'Die Größe des Reizes beträgt {size_in_px} Pixel und {size_in_deg} Sehwinkel')
```

## Sehwinkel in Pixel umrechnen

Das Umrechnen von Sehwinkel in Pixel ist einfach das Umkehrverfahren der oben beschriebenen Methode und kann wie folgt durchgeführt werden:

```python
from math import atan2, degrees
h = 25           # Monitorhöhe in cm
d = 60           # Abstand zwischen Monitor und Teilnehmer in cm
r = 768          # Vertikale Auflösung des Monitors
size_in_deg = 3. # Die Reizgröße in Pixeln
# Berechnen Sie die Anzahl der Grad, die einem einzelnen Pixel entsprechen. Dies wird
# im Allgemeinen ein sehr kleiner Wert sein, etwa 0,03.
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'{deg_per_px} Grad entsprechen einem einzelnen Pixel')
# Berechnen Sie die Größe des Reizes in Grad
size_in_px = size_in_deg / deg_per_px
print(f'Die Größe des Reizes beträgt {size_in_px} Pixel und {size_in_deg} Sehwinkel')
```