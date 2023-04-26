<div class="ClassDoc YAMLDoc" markdown="1">

## Canvas(auto_prepare=True, \*\*style_args)

Eine Fabrikfunktion, die ein neues `Canvas`-Objekt erstellt. Für eine
Beschreibung möglicher Schlüsselwörter, siehe:

- %link:manual/python/canvas%


__Gibt zurück__

- Ein `Canvas`-Objekt.

__Beispiel__

~~~ .python
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~



## Experiment(osexp_path=None, log_path='defaultlog.csv', fullscreen=False, subject_nr=0, \*\*kwargs)

Eine Fabrikfunktion, die ein neues `Experiment`-Objekt erstellt. Dies ist nur
nützlich, wenn ein Experiment vollständig über ein Python-Skript implementiert wird,
anstatt über die Benutzeroberfläche.


__Parameter__

- **osexp_path**: Wenn ein Pfad zu einer `.osexp`-Datei angegeben ist, wird diese Datei geöffnet und
kann direkt durch Aufruf von `Experiment.run()` ausgeführt werden. Wenn keine Experiment-
Datei angegeben ist, wird ein leeres Experiment initialisiert.
- **log_path**: 
- **fullscreen**: 
- **subject_nr**: 
- **kwargs**: Optionale Schlüsselwort-Argumente, die als experimentelle
Variablen interpretiert werden. Der Hauptzweck besteht darin, das Backend über
das `canvas_backend` Schlüsselwort zu spezifizieren.

__Gibt zurück__

- Ein (exp, win, clock, log) Tupel, das den Experiment,
Fenstergriff (backend-spezifisch), Clock und Log Objekten entspricht.

__Beispiel__

Um ein Experiment vollständig programmatisch zu implementieren:

~~~ .python
from libopensesame.python_workspace_api import (
    Experiment, Canvas, Text, Keyboard)
exp, win, clock, log = Experiment(canvas_backend='legacy')
c = Canvas()
c += Text('Press any key')
c.show()
kb = Keyboard()
kb.get_key()
exp.end()
~~~

Um eine Experimentdatei zu laden und auszuführen:

~~~ .python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
~~~



## Form(\*args, \*\*kwargs)

Eine Fabrikfunktion, die ein neues `Form`-Objekt erstellt. Für eine
Beschreibung
möglicher Schlüsselwörter, siehe:

- %link:manual/forms/widgets%


__Gibt zurück__

- Ein `Form`-Objekt.

__Beispiel__

~~~ .python
form = Form()
label = Label(text='Beschriftung')
button = Button(text='Ok')
form.set_widget(label, (0,0))
form.set_widget(button, (0,1))
form._exec()
~~~



## Keyboard(\*\*resp_args)

Eine Fabrikfunktion, die ein neues `Keyboard`-Objekt erstellt. Für eine
Beschreibung möglicher Schlüsselwörter, siehe:

- %link:manual/python/keyboard%


__Gibt zurück__

- Ein `Keyboard`-Objekt.

__Beispiel__

~~~ .python
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key, time = my_keyboard.get_key()
~~~



## Mouse(\*\*resp_args)

Eine Fabrikfunktion, die ein neues `Mouse`-Objekt erstellt. Für eine
Beschreibung
möglicher Schlüsselwörter, siehe:

- %link:manual/python/mouse%


__Gibt zurück__

- Ein `mouse`-Objekt.

__Beispiel__

~~~ .python
my_mouse = Mouse(keylist=[1,3], timeout=5000)
button, time = my_mouse.get_button()
~~~



## Sampler(src, \*\*playback_args)

Eine Fabrikfunktion, die ein neues `Sampler`-Objekt erstellt. Für eine
Beschreibung möglicher Schlüsselwörter, siehe:

- %link:manual/python/sampler%


__Gibt zurück__

- Ein SAMPLER-Objekt.

__Beispiel__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~



## Synth(osc='sine', freq=440, length=100, attack=0, decay=5)

Eine Fabrikfunktion, die einen Klang synthetisiert und ihn als
`Sampler`-Objekt zurückgibt.


__Parameter__

- **osc**: Oszillator, kann "sine", "saw", "square" oder "white_noise" sein.
- **freq**: Frequenz, entweder ein ganzzahliger Wert (Wert in Hertz) oder eine Zeichenkette ("A1",
"eb2", etc.).
- **length**: Die Länge des Klangs in Millisekunden.
- **attack**: Die Angriffszeit (Fade-In) in Millisekunden.
- **decay**: Die Abklingzeit (Fade-Out) in Millisekunden.

__Gibt zurück__

- Ein SAMPLER-Objekt.

__Beispiel__

~~~ .python
my_sampler = Synth(freq=u'b2', length=500)
~~~



## copy_sketchpad(name)

Gibt eine Kopie der Leinwand eines `sketchpad` zurück.


__Parameter__

- **name**: Der Name des `sketchpad`.

__Gibt zurück__

- Eine Kopie der Leinwand des `sketchpad`.

__Beispiel__

~~~ .python
my_canvas = copy_sketchpad('my_sketchpad')
my_canvas.show()
~~~

## pause()

Pausiert das Experiment.



## register_cleanup_function(fnc)

Registriert eine Aufraumfunktion, die ausgeführt wird, wenn das Experiment
endet. Aufraumfunktionen werden ganz am Ende ausgeführt, nachdem die Anzeige,
die Soundvorrichtung und die Log-Datei geschlossen wurden. Aufraumfunktionen werden auch
ausgeführt, wenn das Experiment abstürzt.



__Beispiel__

~~~ .python
def my_cleanup_function():
        print(u'Das Experiment ist abgeschlossen!')
register_cleanup_function(my_cleanup_function)
~~~



## reset_feedback()

Setzt alle Feedback-Variablen auf ihren ursprünglichen Zustand zurück.



__Beispiel__

~~~ .python
reset_feedback()
~~~



## set_subject_nr(nr)

Legt die Versuchspersonennummer und Parität fest (gerade/ ungerade). Diese Funktion wird automatisch aufgerufen
wenn ein Experiment gestartet wird. Sie müssen es nur selbst aufrufen, wenn Sie die 
Versuchspersonennummer überschreiben, die beim Start des Experiments angegeben wurde.


__Parameter__

- **nr**: Die Versuchspersonennummer.


__Beispiel__

~~~ .python
set_subject_nr(1)
print('Versuchspersonennummer = %d' % var.subject_nr)
print('Versuchspersonenparität = %s' % var.subject_parity)
~~~



## sometimes(p=0.5)

Gibt True mit einer bestimmten Wahrscheinlichkeit zurück. (Für fortgeschritteneres
Zufallsprinzip, verwenden Sie das Python `random`-Modul.)


__Parameter__

- **p**: Die Wahrscheinlichkeit, dass True zurückgegeben wird.

__Rückgabe__

- True oder False

__Beispiel__

~~~ .python
if sometimes():
        print('Manchmal gewinnt man')
else:
        print('Manchmal verliert man')
~~~



## xy_circle(n, rho, phi0=0, pole=(0, 0))

Generiert eine Liste von Punkten (x,y-Koordinaten) im Kreis. Dies kann verwendet werden
um Reize in einer kreisförmigen Anordnung darzustellen.


__Parameter__

- **n**: Die Anzahl der x,y-Koordinaten, die generiert werden sollen.
- **rho**: Der radiale Koordinatenwert, auch Abstand oder Exzentrizität des ersten
Punkten.
- **phi0**: Die Winkelkoordinate für die erste Koordinate. Dies ist eine
gegenuhrzeigersinnige Drehung in Grad (d.h. nicht in Radiant), wobei 0
gerade nach rechts zeigt.
- **pole**: Der Bezugspunkt.

__Rückgabe__

- Eine Liste von (x,y) Koordinatentupeln.

__Beispiel__

~~~ .python
# Zeichne 8 Rechtecke um einen zentralen Fixpunkt
c = Canvas()
c.fixdot()
for x, y in xy_circle(8, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_distance(x1, y1, x2, y2)

Gibt den Abstand zwischen zwei Punkten an.


__Parameter__

- **x1**: Die x-Koordinate des ersten Punktes.
- **y1**: Die y-Koordinate des ersten Punktes.
- **x2**: Die x-Koordinate des zweiten Punktes.
- **y2**: Die y-Koordinate des zweiten Punktes.

__Rückgabe__

- Der Abstand zwischen den beiden Punkten.


## xy_from_polar(rho, phi, pole=(0, 0))

Konvertiert polare Koordinaten (Abstand, Winkel) in kartesische Koordinaten
(x, y).


__Parameter__

- **rho**: Die radiale Koordinate, auch Abstand oder Exzentrizität.
- **phi**: Die Winkelkoordinate. Dies zeigt eine drehung im Uhrzeigersinn in Grad
(d.h. nicht Radiant), wobei 0 gerade nach rechts zeigt.
- **pole**: Der Bezugspunkt.

__Rückgabe__

- Ein (x, y) Koordinatentupel.

__Beispiel__

~~~ .python
# Zeichne ein Kreuz
x1, y1 = xy_from_polar(100, 45)
x2, y2 = xy_from_polar(100, -45)
c = Canvas()
c.line(x1, y1, -x1, -y1)
c.line(x2, y2, -x2, -y2)
c.show()
~~~



## xy_grid(n, spacing, pole=(0, 0))

Generiert eine Liste von Punkten (x,y-Koordinaten) in einem Raster. Dies kann verwendet werden
um Reize in einer Rasteranordnung darzustellen.


__Parameter__

- **n**: Eine `int`, die die Anzahl der Spalten und Zeilen angibt, sodass `n=2`
einen 2x2-Grid angibt, oder ein (n_col, n_row) `tuple`, sodass `n=(2,3)`
einen 2x3-Grid angibt.
- **spacing**: Ein numerischer Wert, der den Abstand zwischen den Zellen angibt, oder ein
(col_spacing, row_spacing) Tupel.
- **pole**: Der Bezugspunkt.

__Rückgabe__

- Eine Liste von (x,y) Koordinatentupeln.

__Beispiel__

~~~ .python
# Zeichne ein 4x4 Raster von Rechtecken
c = Canvas()
c.fixdot()
for x, y in xy_grid(4, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_random(n, width, height, min_dist=0, pole=(0, 0))

Erzeugt eine Liste von zufälligen Punkten (x, y-Koordinaten) mit einem Minimum
Abstand zwischen jedem Paar von Punkten. Diese Funktion wird eine
Ausnahme auslösen, wenn die Koordinatenliste nicht generiert werden kann, normalerweise weil
es gibt zu viele Punkte, der min_dist ist zu hoch eingestellt, oder die Breite oder Höhe sind zu niedrig eingestellt.


__Parameter__

- **n**: Die Anzahl der zu generierenden Punkte.
- **width**: Die Breite des Feldes mit zufälligen Punkten.
- **height**: Die Höhe des Feldes mit zufälligen Punkten.
- **min_dist**: Der minimale Abstand zwischen jedem Punkt.
- **pole**: Der Referenzpunkt.

__Gibt zurück__

- Eine Liste von (x,y) Koordinaten-Tupeln.

__Beispiel__

~~~ .python
# Zeichne 50 Rechtecke in einem zufälligen Gitter
c = Canvas()
c.fixdot()
for x, y in xy_random(50, 500, 500, min_dist=40):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~



## xy_to_polar(x, y, pole=(0, 0))

Konvertiert kartesische Koordinaten (x, y) in Polarkoordinaten (Distanz,
Winkel).


__Parameter__

- **x**: Die X-Koordinate.
- **y**: Die Y-Koordinate.
- **pole**: Der Referenzpunkt.

__Gibt zurück__

- Ein (rho, phi) Koordinaten-Tupel. Hier ist `rho` die radiale Koordinate,
auch Distanz oder Exzentrizität. `phi` ist die Winkelkoordinate in
Grad (d. h. nicht Bogenmaß) und widerspiegelt eine gegen den Uhrzeigersinn in Drehung,
0 ist gerade rechts.

__Beispiel__

~~~ .python
rho, phi = xy_to_polar(100, 100)
~~~



</div>