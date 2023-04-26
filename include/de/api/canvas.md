<div class="ClassDoc YAMLDoc" markdown="1">

# Klasse __Canvas__

{% set arg_max_width = "Die maximale Breite des Textes in Pixeln, " +
"bevor ein Umbruch in eine neue Zeile erfolgt, oder `None`, um am Bildschirmrand umzubrechen." %}

{% set arg_bgmode = "Gibt an, ob der Hintergrund der Durchschnitt von " +
"col1 und col2 ('avg', entspricht einem typischen Gabor-Patch) oder " + 
"gleich col2 ('col2') ist, nützlich, um in den Hintergrund überzugehen. Hinweis: " +
"dieser Parameter wird von der psycho-Backend ignoriert, das eine zunehmende " +
"Transparenz für den Hintergrund verwendet." %}

{% set arg_style = "Optionale [Stil-Schlüsselwörter](#style-keywords), die " + 
"den Stil der aktuellen Zeichenoperation angeben. Dies beeinträchtigt nicht nachfolgende Zeichenoperationen." %}

{% set arg_center = "Ein bool, der angibt, ob die Koordinaten sich auf " + 
"die Mitte (`True`) oder oben links (`False`) des Textes beziehen." %}

Die `Canvas`-Klasse wird verwendet, um visuelle Stimuli darzustellen. Im Allgemeinen erstellt man ein
`Canvas`-Objekt mit der `Canvas()` Factory-Funktion, wie im Abschnitt
[Eine Canvas erstellen](#creating-a-canvas) beschrieben.

__Beispiel__:

~~~ .python
# Erstellen und Anzeigen einer Leinwand mit einem zentralen Fixationspunkt
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

__Beispiel__:

Sie können auch `Canvas`-Elemente als Objekte hinzufügen. Siehe auch den Abschnitt über [Benennen,
Zugreifen und Ändern von Elementen](#naming-accessing-and-modifying-elements).

~~~ .python
# Erstellen einer Leinwand mit einem Fixationspunkt und einem Rechteck
my_canvas = Canvas()
my_canvas['my_fixdot'] = FixDot()
my_canvas.show()
~~~

[TOC]

## Dinge, die man wissen sollte

### Eine Canvas erstellen

Normalerweise erstellen Sie eine `Canvas` mit der `Canvas()` Factory-Funktion:

~~~ .python
my_canvas = Canvas()
~~~

Optional können Sie [Stil-Schlüsselwörter](#style-keywords) an `Canvas()` übergeben, um
den Standardstil festzulegen:

~~~ .python
my_canvas = Canvas(color='green')
my_canvas.fixdot() # Wird grün sein
~~~

### Stil-Schlüsselwörter

Alle Funktionen, die `**style_args` akzeptieren, nehmen die folgenden Schlüsselwortargumente:

- `color` gibt die Vordergrundfarbe an. Für gültige Farbspezifikationen siehe
  [Farben](#colors).
- `background_color` gibt die Hintergrundfarbe an. Für gültige Farbspezifikationen siehe [Farben](#colors).
- `fill` gibt an, ob Rechtecke, Kreise, Polygone und Ellipsen gefüllt (`True`) oder als Umriss (`False`) gezeichnet werden.
- `penwidth` gibt eine Stiftbreite in Pixeln an und sollte `int` oder `float` sein.
- `html` gibt an, ob HTML-Tags interpretiert werden und sollte `True` oder `False` sein.
- `font_family` ist der Name einer Schriftfamilie, wie z.B. 'sans'.
- `font_size` ist eine Schriftgröße in Pixeln.
- `font_italic` gibt an, ob der Text kursiv sein soll und sollte `True` oder `False` sein.
- `font_bold` gibt an, ob der Text fett sein soll und sollte `True` oder `False` sein.
- `font_underline` gibt an, ob der Text unterstrichen sein soll und sollte `True` oder `False` sein.

~~~ .python
# Zeichnen eines grünen Fixationspunkts
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
~~~

Stil-Schlüsselwörter beeinflussen nur die aktuelle Zeichenoperation (außer wenn sie an
`Canvas()` während der Erstellung der `Canvas` übergeben werden). Um den Stil für alle nachfolgenden Zeichenoperationen zu ändern, setzen Sie die Stileigenschaften, wie z.B. `canvas.color`, direkt:

~~~ .python
# Zeichnen eines roten Kreuzes mit einer 2px Stiftbreite
my_canvas = Canvas()
my_canvas.color = 'red'
my_canvas.penwidth = 2
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

Oder übergeben Sie die Stileigenschaften an `Canvas()`:

~~~ .python
# Zeichnen eines roten Kreuzes mit einer 2px Stiftbreite
my_canvas = Canvas(color='red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

### Farben

Sie können Farben auf folgende Weise angeben. Dies beinhaltet CSS3-Typ-Farbspezifikationen, unterstützt aber auch zusätzliche Spezifikationen, wie den CIE l* a* b* Farbraum.

__Hinweis zur Version:__ Die Farbräume `hsv`, `hsl` und `lab` sind neu in v3.3.0.

- __Farbnamen:__ 'rot', 'schwarz', usw. Eine vollständige Liste der gültigen Farbnamen finden Sie [hier](http://www.w3.org/TR/SVG11/types.html#ColorKeywords).
- __Siebenstellige Hexadezimalzeichenfolgen:__ `#FF0000`, `#000000`, usw. Hier
  reichen die Werte von `00` bis `FF`, so dass `#FF0000` ein helles Rot ist.
- __Vierstellige Hexadezimalzeichenfolgen:__ `#F00`, `#000`, usw. Hier reichen die Werte
  von '0' bis 'F', so dass `#F00` ein helles Rot ist.
- __RGB-Zeichenfolgen:__ `rgb(255,0,0)`, `rgb(0,0,0)`, usw. Hier reichen die Werte von
  0 bis 255, so dass `rgb(255,0,0)` ein helles Rot ist.
- __RGB-Prozentzeichenfolgen:__ `rgb(100%,0%,0%)`, `rgb(0%,0%,0%)`, usw. Die Werte
  reichen hier von 0 % bis 100 %, so dass `rgb(100%,0%,0%)` ein helles Rot ist.
- __RGB-Tupel:__ `(255, 0, 0)`, `(0, 0 ,0)`, usw. Hier reichen die Werte von `0`
  bis `255`, so dass `(255,0,0)` ein helles Rot ist.
- __HSV-Zeichenfolgen:__ `hsv(120, 100%, 100%)`. Im [HSV](https://en.wikipedia.org/
  wiki/HSL_and_HSV) Farbraum ist der Farbtonparameter ein Winkel von 0 bis 359,
  und die Sättigungs- und Wertparameter sind Prozentangaben von 0% bis 100%.
- __HSL-Zeichenfolgen:__ `hsl(120, 100%, 50%)`. Im [HSL](https://en.wikipedia.org/
  wiki/HSL_and_HSV) Farbraum ist der Farbtonparameter ein Winkel von 0 bis 359,
  und die Sättigungs- und Helligkeitsparameter sind Prozentangaben von 0% bis 100%.
- __LAB-Zeichenfolgen:__ `lab(53, -20, 0)`. Im [CIELAB](https://en.wikipedia.org/
  wiki/CIELAB_color_space) Farbraum sind die Parameter Lichtwert (`l*`),
  Grün-Rot-Achse (`a*`, negativ ist grün) und Blau-Gelb-Achse (`b*`, negativ
  ist blau). Dies verwendet den D65-Weißpunkt und die sRGB-Transferfunktion, wie
  [hier](https://www.psychopy.org/_modules/psychopy/tools/
  colorspacetools.html) implementiert.
- __Leuchtdichtewerte:__ `255`, `0`, usw. Hier reichen die Werte von `0` bis `255`
  so, dass `255` weiß ist.

~~~ .python
# Verschiedene Möglichkeiten, Grün anzugeben
my_canvas.fixdot(color='green')  # Dunkelgrün
my_canvas.fixdot(color='#00ff00')
my_canvas.fixdot(color='#0f0')
my_canvas.fixdot(color='rgb(0, 255, 0)')
my_canvas.fixdot(color='rgb(0%, 100%, 0%)')
my_canvas.fixdot(color='hsl(100, 100%, 50%)')
my_canvas.fixdot(color='hsv(0, 100%, 100%)')
my_canvas.fixdot(color='lab(53, -20, 0)')  # Dunkelgrün
my_canvas.fixdot(color=(0, 255, 0))  # Leuchtdichtewert angeben (weiß)
~~~

### Benennen, Zugreifen und Modifizieren von Elementen

Ab OpenSesame 3.2 unterstützt das `Canvas` eine objektbasierte Schnittstelle, die es ermöglicht
Elemente zu benennen und auf einzelne Elemente zuzugreifen und sie zu modifizieren, ohne
dass das gesamte `Canvas` neu gezeichnet werden muss.

Zum Beispiel wird im folgenden Beispiel zuerst ein rotes `Line`-Element zu einem `Canvas`
hinzugefügt und angezeigt, dann die Farbe der Linie auf Grün geändert und es wird erneut angezeigt,
und schließlich wird die Linie gelöscht und das Canvas wieder angezeigt (das jetzt leer ist).
Der Name des Elements (`my_line`) wird verwendet, um auf das Element für alle Referenzen
Operationen.

~~~ .python
my_canvas = Canvas()
my_canvas['my_line'] = Line(-100, -100, 100, 100, color='red')
my_canvas.show()
clock.sleep(1000)
my_canvas['my_line'].color = 'green'
my_canvas.show()
clock.sleep(1000)
del my_canvas['my_line']
my_canvas.show()
~~~

Sie können auch ein Element hinzufügen, ohne explizit einen Namen dafür anzugeben. In diesem
Fall wird ein Name automatisch generiert (z. B. `stim0`).

~~~ .python
my_canvas = Canvas()
my_canvas += FixDot()
my_canvas.show()
~~~

Wenn Sie eine Liste von Elementen hinzufügen, werden diese automatisch gruppiert, und
Sie können sich auf die gesamte Gruppe unter einem Namen beziehen.

~~~ .python
my_canvas = Canvas()
my_canvas['my_cross'] = [    Line(-100, 0, 100, 0),    Line(0, -100, 0, 100)]
my_canvas.show()
~~~

Um zu prüfen, ob eine bestimmte `x, y`-Koordinate innerhalb des Begrenzungsrechtecks eines Elements liegt, können Sie `in` verwenden:

~~~ .python
my_mouse = Mouse(visible=True)
my_canvas = Canvas()
my_canvas['rect'] = Rect(-100, -100, 200, 200)
my_canvas.show()
button, (x, y), time = my_mouse.get_click()
if (x, y) in my_canvas['rect']:
    print('In Rechteck geklickt')
else:
    print('Außerhalb des Rechtecks geklickt')
~~~

Sie können auch eine Liste der Namen aller Elemente erhalten, die eine `x,y`
Koordinate enthalten, indem Sie die `Canvas.elements_at()` Funktion verwenden, die unten dokumentiert ist.

## arrow(sx, sy, ex, ey, body_length=0.8, body_width=0.5, head_width=30, \*\*style_args)

Zeichnet einen Pfeil. Ein Pfeil ist ein Polygon aus 7 Eckpunkten,
mit einer Pfeilspitze, die auf (ex, ey) zeigt.

__Parameter__

- **sx**: Die X-Koordinate der Basis des Pfeils.
- **sy**: Die Y-Koordinate der Basis des Pfeils.
- **ex**: Die X-Koordinate der Spitze des Pfeils.
- **ey**: Die Y-Koordinate der Spitze des Pfeils.
- **body_length**: Proportionale Länge des Pfeilkörpers im Verhältnis zum gesamten Pfeil
[0-1].
- **body_width**: Proportionale Breite (Dicke) des Pfeilkörpers im Verhältnis zum
vollen Pfeil [0-1].
- **head_width**: Breite (Dicke) des Pfeilkopfes in Pixeln.


## circle(x, y, r, \*\*style_args)

Zeichnet einen Kreis.


__Parameter__

- **x**: Die mittlere X-Koordinate des Kreises.
- **y**: Die mittlere Y-Koordinate des Kreises.
- **r**: Der Radius des Kreises.
- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Funktionsinterface
my_canvas.circle(100, 100, 50, fill=True, color='red')
# Elementinterface
my_canvas['my_circle'] = Circle(100, 100, 50, fill=True, color='red')
~~~



## clear(\*arglist, \*\*kwdict)

Löscht die Leinwand mit der aktuellen Hintergrundfarbe. Beachten Sie, dass es
in der Regel schneller ist, für jede experimentelle Anzeige eine andere Leinwand zu verwenden, als eine einzelne Leinwand zu verwenden und sie wiederholt zu löschen und neu zu zeichnen.

__Parameter__

- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
clock.sleep(1000)
my_canvas.clear()
my_canvas.fixdot(color='red')
my_canvas.show()
~~~



## copy(canvas)

Macht die aktuelle `Canvas` zu einer Kopie der übergebenen `Canvas`.

__Warnung:__

Das Kopieren von `Canvas`-Objekten kann zu unvorhersehbarem Verhalten führen. In vielen
Fällen ist eine bessere Lösung, mehrere `Canvas`-Objekte von Grund auf neu zu erstellen und/ oder das Element-Interface zu verwenden, um `Canvas`
Elemente einzeln zu aktualisieren.

__Parameter__

- **canvas**: Die `Canvas`, die kopiert werden soll.

__Beispiel__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(x=100, color='green')
my_copied_canvas = Canvas()
my_copied_canvas.copy(my_canvas)
my_copied_canvas.fixdot(x=200, color="blue")
my_copied_canvas.show()
~~~



## elements_at(x, y)

*Neu in v3.2.0*

Ermittelt die Namen der Elemente, die eine bestimmte `x, y`
Koordinate enthalten.

__Parameter__

- **x**: Eine X-Koordinate.
- **y**: Eine Y-Koordinate.

__Rückgabewerte__

- Eine `list` der Elementnamen, die die Koordinate `x, y` enthalten.

__Beispiel__

~~~ .python
# Erstelle und zeige eine Leinwand mit zwei teilweise überlappenden Rechtecken
my_canvas = Canvas()
my_canvas['right_rect'] = Rect(x=-200, y=-100, w=200, h=200, color='red')
my_canvas['left_rect'] = Rect(x=-100, y=-100, w=200, h=200, color='green')
my_canvas.show()
# Erfasse einen Mausklick und gib die Namen der Elemente aus, die
# den angeklickten Punkt enthalten
my_mouse = Mouse(visible=True)
button, pos, time = my_mouse.get_click()
if pos is not None:
    x, y = pos
    print('Geklickt auf Elemente: %s' % my_canvas.elements_at(x, y))
~~~



## ellipse(x, y, w, h, \*\*style_args)

Zeichnet eine Ellipse.


__Parameter__

- **x**: Die linke X-Koordinate.
- **y**: Die obere Y-Koordinate.
- **w**: Die Breite.
- **h**: Die Höhe.
- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Funktionsinterface
my_canvas.ellipse(-10, -10, 20, 20, fill=True)
# Elementinterface
my_canvas['my_ellipse'] = Ellipse(-10, -10, 20, 20, fill=True)
~~~



## fixdot(x=None, y=None, style='default', \*\*style_args)

Zeichnet einen Fixierungspunkt. Der Standardstil ist medium-open.

- 'large-filled' ist ein ausgefüllter Kreis mit einem Radius von 16px.
- 'medium-filled' ist ein
ausgefüllter Kreis mit einem Radius von 8px.
- 'small-filled' ist ein ausgefüllter Kreis
mit einem Radius von 4px.
- 'large-open' ist ein ausgefüllter Kreis mit einem Radius von 16px
und einem 2px-Loch.
- 'medium-open' ist ein ausgefüllter Kreis mit einem Radius von 8px
und einem 2px-Loch.
- 'small-open' ist ein ausgefüllter Kreis mit einem 4px Radius und
einem 2px-Loch.
- 'large-cross' ist ein 16px-Kreuz.
- 'medium-cross' ist ein 8px-
Kreuz.
- 'small-cross' ist ein 4px-Kreuz.

__Parameter__

- **x**: Die X-Koordinate des Punktmittelpunkts oder None, um einen horizontal
zentrierten Punkt zu zeichnen.
- **y**: Die Y-Koordinate des Punktmittelpunkts oder None, um einen vertikal
zentrierten Punkt zu zeichnen.
- **style**: Der Fixpunktstil. Einer der folgenden: default, large-filled,
medium-
filled, small-filled, large-open, medium-open,
small-open, large-
cross, medium-cross oder small-cross.
default entspricht medium-open.
- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.fixdot()
# Element interface
my_canvas['my_fixdot'] = FixDot()
~~~



## gabor(x, y, orient, freq, env='gaussian', size=96, stdev=12, phase=0, col1='white', col2='black', bgmode='avg')

Zeichnet einen Gabor-Patch. Hinweis: Die genaue Darstellung des Gabor-Patches
hängt vom Backend ab.


__Parameter__

- **x**: Die mittlere X-Koordinate.
- **y**: Die mittlere Y-Koordinate.
- **orient**: Orientierung in Grad [0 .. 360]. Dies bezieht sich auf eine
Drehung im Uhrzeigersinn von einer Vertikalen.
- **freq**: Frequenz in Zyklen/px der Sinuswelle.
- **env**: Die Hülle, die die Form des Patches bestimmt. Kann sein
"gaussian", "linear", "circular" oder "rectangular".
- **size**: Eine Größe in Pixeln.
- **stdev**: Standardabweichung in Pixeln der Gaußkurve. Nur anwendbar bei
gaussian Hüllen.
- **phase**: Phase der Sinuswelle [0.0 .. 1.0].
- **col1**: Eine Farbe für die Spitzen.
- **col2**: Eine Farbe für die Täler. Hinweis: Das psycho-Backend
ignoriert diesen
Parameter und verwendet immer das Inverse von
`col1` für die Täler.
- **bgmode**: {{arg_bgmode}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Function interface
my_canvas.gabor(100, 100, 45, .05)
# Element interface
my_canvas['my_gabor'] = Gabor(100, 100, 45, .05)
~~~



## image(fname, center=True, x=None, y=None, scale=None, rotation=None)

Zeichnet ein Bild aus einer Datei. Diese Funktion sucht nicht in der Datei
pool, sondern nimmt einen absoluten Pfad.


__Parameter__

- **fname**: Der Dateiname des Bildes. Bei Verwendung von Python 2 sollte dies
entweder `unicode` oder ein utf-8-kodiertes `str` sein. Bei Verwendung von Python 3,
sollte dies entweder `str` oder ein utf-8-kodiertes `bytes` sein.
- **center**: Ein bool, der angibt, ob die Koordinaten das Zentrum (True) oder
oben-links (False) anzeigen.
- **x**: Die X-Koordinate oder `None`, um ein horizontal zentriertes Bild zu zeichnen.
- **y**: Die Y-Koordinate oder `None`, um ein vertikal zentriertes Bild zu zeichnen.
- **scale**: Der Skalierungsfaktor des Bildes. `None` oder 1 zeigen die ursprüngliche
Größe an. 2,0 zeigen eine 200%ige Vergrößerung usw.
- **rotation**: Die Drehung des Bildes. `None` oder 0 zeigen die ursprüngliche
Drehung an. Positive Werte zeigen eine Drehung im Uhrzeigersinn in Grad an.

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Determine the absolute path:
path = exp.pool['image_in_pool.png']
# Function interface
my_canvas.image(path)
# Element interface
my_canvas['my_image'] = Image(path)
~~~



## line(sx, sy, ex, ey, \*\*style_args)

Zeichnet eine Linie.


__Parameter__

- **sx**: Die linke X-Koordinate.
- **sy**: Die obere Y-Koordinate.
- **ex**: Die rechte X-Koordinate.
- **ey**: Die untere Y-Koordinate.
- **\*\*style_args**: {{arg_style}}


## lower_to_bottom(element)

Senkt ein Element nach unten, so dass es zuerst gezeichnet wird; das
heißt, es wird zum Hintergrund.


__Parameter__

- **element**: Ein SKETCHPAD-Element oder dessen Name.


## noise_patch(x, y, env='gaussian', size=96, stdev=12, col1='white', col2='black', bgmode='avg')

Zeichnet einen Rausch-Patch mit einer Hülle. Die genaue Darstellung von
dem Rauschpatch hängt vom Backend ab.


__Parameter__

- **x**: Die zentrale X-Koordinate.
- **y**: Die zentrale Y-Koordinate.
- **env**: Die Hülle, die die Form des Flickens bestimmt. Kann
"gaussian", "linear", "circular" oder "rectangular" sein.
- **size**: Eine Größe in Pixel.
- **stdev**: Standardabweichung in Pixel des Gauss'schen. Nur anwendbar auf
gaussförmige Hüllen.
- **col1**: Die erste Farbe.
- **col2**: Die zweite Farbe. Hinweis: Der Psycho-Back-End ignoriert diesen
Parameter
und verwendet immer das Inverse von `col1`.
- **bgmode**: {{arg_bgmode}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Funktionsschnittstelle
my_canvas.noise_patch(100, 100, env='circular')
# Elementschnittstelle
my_canvas['my_noise_patch'] = NoisePatch(100, 100, env='circular')
~~~



## polygon(vertices, \*\*style_args)

Zeichnet ein Polygon, das durch eine Liste von Eckpunkten definiert ist. D.h. eine Form von
Punkten, die durch Linien verbunden sind.

__Parameter__

- **vertices**: Eine Liste von Tupeln, wobei jedes Tupel einem Eckpunkt entspricht. Zum
Beispiel, [(100,100), (200,100), (100,200)] zeichnet ein Dreieck.
- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
n1 = 0,0
n2 = 100, 100
n3 = 0, 100
# Funktionsschnittstelle
my_canvas.polygon([n1, n2, n3])
# Elementschnittstelle
my_canvas['my_polygon'] = Polygon([n1, n2, n3])
~~~



## prepare(self)

Beendet ausstehende Canvas-Operationen (falls vorhanden), sodass ein anschließender
Aufruf von [canvas.show] besonders schnell ist. Es ist nur notwendig, diese
Funktion aufzurufen, wenn Sie `auto_prepare` beim Initialisieren der `Canvas` deaktiviert haben.




## raise_to_top(element)

Hebt ein Element nach oben, damit es zuletzt gezeichnet wird; das heißt, es
wird in den Vordergrund gerückt.


__Parameter__

- **element**: Ein SKETCHPAD-Element oder dessen Name.


## rect(x, y, w, h, \*\*style_args)

Zeichnet ein Rechteck.


__Parameter__

- **x**: Die linke X-Koordinate.
- **y**: Die obere Y-Koordinate.
- **w**: Die Breite.
- **h**: Die Höhe.
- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Funktionsschnittstelle
my_canvas.rect(-10, -10, 20, 20, fill=True)
# Elementschnittstelle
my_canvas['my_rect'] = Rect(-10, -10, 20, 20, fill=True)
~~~



## rename_element(old_name, new_name)

Benennt ein Element um.




## show(self)

Zeigt oder "dreht" die Leinwand auf dem Bildschirm.



__Gibt zurück__

- Ein Zeitstempel der Zeit, zu der die Leinwand tatsächlich auf
dem Bildschirm erschien, oder eine beste Vermutung, wenn keine genauen Zeitinformationen verfügbar sind. Weitere Informationen zum Timing finden Sie unter </misc/timing>. Abhängig vom Back-End ist der Zeitstempel entweder ein `int` oder ein `float`.

__Beispiel__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
t = my_canvas.show()
exp.set('time_fixdot', t)
~~~



## text(text, center=True, x=None, y=None, max_width=None, \*\*style_args)

Zeichnet Text.


__Parameter__

- **text**: Ein Text-String. Bei Verwendung von Python 2 sollte dies entweder
`unicode` oder ein utf-8-kodierter `str` sein. Bei Verwendung von Python 3, dies
sollte entweder "str" oder "utf-8-kodierte" "bytes" sein.
- **center**: {{arg_center}}
- **x**: Die X-Koordinate oder None, um horizontal zentrierten Text zu zeichnen.
- **y**: Die Y-Koordinate oder None, um vertikal zentrierten Text zu zeichnen.
- **max_width**: {{arg_max_width}}
- **\*\*style_args**: {{arg_style}}

__Beispiel__

~~~ .python
my_canvas = Canvas()
# Funktionsschnittstelle
my_canvas.text('Ein Text mit <b>fettem</b> und <i>kursivem</i> Schrift')
# Elementschnittstelle
my_canvas['my_text'] = Text('Ein Text mit <b>fettem</b> und <i>kursivem</i> Schrift')
~~~



## text_size(text, center=True, max_width=None, \*\*style_args)

Bestimmt die Größe eines Text-Strings in Pixeln.


__Parameter__

- **text**: Ein Text-String.
- **center**: {{arg_center}}
- **max_width**: {{arg_max_width}}
- **\*\*style_args**: {{arg_style}}

__Gibt zurück__

- Ein (Breite, Höhe) Tupel mit den Abmessungen des Text
Strings.

__Beispiel__

~~~ .python
my_canvas = Canvas()
w, h = my_canvas.text_size('Ein Text')
~~~



</div>