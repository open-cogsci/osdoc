<div class="ClassDoc YAMLDoc" markdown="1">

# Klasse __Mouse__

Die `Mouse`-Klasse wird verwendet, um Maus-Eingaben zu erfassen. Im Allgemeinen erstellst du ein
`Mouse`-Objekt mit der `Mouse()`-Fabrikfunktion, wie im Abschnitt [Eine Mouse erstellen](#creating-a-mouse) beschrieben.

__Beispiel__

~~~ .python
# Zeichne einen 'Fixationspunkt-Mauszeiger', bis eine Schaltfläche angeklickt wird.
my_mouse = Mouse()
my_canvas = Canvas()
while True:
    button, position, timestamp = my_mouse.get_click(timeout=20)
    if button is not None:
        break
    (x,y), time = my_mouse.get_pos()
    my_canvas.clear()
    my_canvas.fixdot(x, y)
    my_canvas.show()
~~~

[TOC]

## Dinge, die man wissen sollte

### Eine Mouse erstellen

Im Allgemeinen erstellst du eine `Mouse` mit der `Mouse()`-Fabrikfunktion:

~~~ .python
my_mouse = Mouse()
~~~

Optional kannst du [Antwort-Schlüsselwörter](#response-keywords) an `Mouse()`
übergeben, um das Standardverhalten festzulegen:

~~~ .python
my_mouse = Mouse(timeout=2000)
~~~

### Koordinaten

- Wenn *Uniforme Koordinaten* auf 'ja' gesetzt sind, sind die Koordinaten relativ zum
  Zentrum der Anzeige. Das heißt, (0,0) ist die Mitte. Dies ist die Standardeinstellung ab
  OpenSesame 3.0.0.
- Wenn *Uniforme Koordinaten* auf 'nein' gesetzt sind, sind die Koordinaten relativ zu der
  oberen linken Ecke der Anzeige. Das heißt, (0,0) ist die obere linke Ecke. Dies war die Standardeinstellung
  in OpenSesame 2.9.X und früher.

### Tastennummern

Maus-Tasten sind wie folgt nummeriert:

1. Linke Taste
2. Mittlere Taste
3. Rechte Taste
4. Scroll hoch
5. Scroll runter

### Touchscreens

Bei der Arbeit mit einem Touchscreen wird eine Berührung als Taste 1
(linke Taste) registriert.

### Antwort-Schlüsselwörter

Funktionen, die `**resp_args` annehmen, nehmen die folgenden Schlüsselwortargumente an:

- `timeout` gibt einen Timeout-Wert in Millisekunden an oder wird auf `None` gesetzt, um den Timeout zu deaktivieren.
- `buttonlist` gibt eine Liste der akzeptierten Tasten an oder wird auf `None` gesetzt, um alle Tasten zu akzeptieren.
- `visible` zeigt an, ob der Mauszeiger sichtbar wird, wenn ein Klick erfasst wird (`True` oder `False`). Um die Cursor-Sichtbarkeit sofort zu ändern, verwenden Sie `Mouse.show_cursor()`.

~~~ .python
# Hole einen linken oder rechten Tastendruck mit einer Zeitüberschreitung von 3000 ms
my_mouse = Mouse()
button, time = my_mouse.get_click(buttonlist=[1,3], timeout=3000)
~~~

 Antwort-Schlüsselwörter beeinflussen nur den aktuellen Vorgang (außer wenn sie an `Mouse()` übergeben werden, wenn das Objekt erstellt wird). Um das Verhalten für alle anschließenden Vorgänge zu ändern, setze die Antwort-Eigenschaften direkt::

~~~ .python
# Hole zwei linke oder rechte Tastendrücke mit einer Zeitüberschreitung von 5000 ms
my_mouse = Mouse()
my_mouse.buttonlist = [1,3]
my_mouse.timeout = 5000
button1, time1 = my_mouse.get_click()
button2, time2 = my_mouse.get_click()
~~~

Oder übergebe die Antwort-Schlüsselwörter an `Mouse()`, wenn du das Objekt erstellst:

~~~ .python
# Hole zwei linke oder rechte Tastendrücke mit einer Zeitüberschreitung von 5000 ms
my_mouse = Mouse(buttonlist=[1,3], timeout=5000)
button1, time1 = my_mouse.get_click()
button2, time2 = my_mouse.get_click()
~~~

## flush(self)

Löscht alle ausstehenden Eingaben, nicht nur die der Maus.

__Returns__

- True, wenn eine Schaltfläche angeklickt wurde (d.h., wenn es etwas zu
löschen gab) und False in anderen Fällen.

__Beispiel__

~~~ .python
my_mouse = Mouse()
my_mouse.flush()
button, position, timestamp = my_mouse.get_click()
~~~



## get_click(\*arglist, \*\*kwdict)

Erfasst einen Mausklick.

__Parameter__

- **\*\*resp_args**: Optionale [Antwort-Schlüsselwörter](#response-keywords), die für diesen Aufruf von `Mouse.get_click()` verwendet werden. Dies hat keine Auswirkungen
  auf nachfolgende Vorgänge.

__Returns__

- Ein (Taste, Position, Zeitstempel)-Tupel. Die Taste und die Position sind
`None`, wenn ein Timeout auftritt. Die Position ist ein (x, y)-Tupel in Bildschirm-
Koordinaten.

__Beispiel__

~~~ .python
my_mouse = Mouse()
button, (x, y), timestamp = my_mouse.get_click(timeout=5000)
if button is None:
        print('Ein Timeout ist aufgetreten!')
~~~



## get_click_release(\*arglist, \*\*kwdict)

*Neu in v3.2.0*

Erfasst das Loslassen eines Mausklicks.

*Wichtig:* Dies
  Funktion ist derzeit nicht für das "psycho"-Backend implementiert.

__Parameter__

- **\*\*resp_args**: Optionale [Antwort-Schlüsselwörter](#response-keywords), die für diesen Aufruf von `Mouse.get_click_release()` verwendet werden. Dies hat keinen Einfluss auf nachfolgende Vorgänge.

__Gibt zurück__

- Ein (button, position, timestamp) Tupel. Der Button und die Position sind `None`, wenn ein Timeout auftritt. Die Position ist ein (x, y) Tupel in Bildschirmkoordinaten.

__Beispiel__

~~~ .python
meine_maus = Mouse()
button, (x, y), timestamp = meine_maus.get_click_release(timeout=5000)
if button is None:
        print('Ein Timeout ist aufgetreten!')
~~~

## get_pos(self)

Gibt die aktuelle Position des Mauszeigers zurück.

__Gibt zurück__

- Ein (position, timestamp) Tupel.

__Beispiel__

~~~ .python
meine_maus = Mouse()
(x, y), timestamp = meine_maus.get_pos()
print('Der Mauszeiger war bei (%d, %d)' % (x, y))
~~~

## get_pressed(self)

Gibt den aktuellen Zustand der Maustasten zurück. Ein True-Wert bedeutet, dass die Taste gerade gedrückt wird.

__Gibt zurück__

- Ein (button1, button2, button3) Tupel aus boolschen Werten.

__Beispiel__

~~~ .python
meine_maus = Mouse()
buttons = meine_maus.get_pressed()
b1, b2, b3 = buttons
print('Derzeit gedrückte Maustasten: (%d,%d,%d)' % (b1,b2,b3))
~~~

## set_pos(pos=(0, 0))

Legt die Position des Mauszeigers fest.

__Warnung:__ `set_pos()` ist
unzuverlässig und schlägt stillschweigend auf
einigen Systemen fehl.

__Parameter__

- **pos**: Ein (x, y) Tupel für die neuen Mauskoordinaten.

__Beispiel__

~~~ .python
meine_maus = Mouse()
meine_maus.set_pos(pos=(0,0))
~~~

## show_cursor(show=True)

Ändert sofort die Sichtbarkeit des Mauszeigers.

__Hinweis:__
In den meisten Fällen möchten Sie das Schlüsselwort `visible`
verwenden, welches
die Sichtbarkeit während der Erfassung von Antworten ändert,
also während
`mouse.get_click()` aufgerufen wird. Das Aufrufen von 
`show_cursor()` ändert nicht
implizit den Wert von `visible`, 
was zu dem
etwas unintuitiven Verhalten führen kann, dass der Cursor
versteckt wird, sobald
`get_click()` aufgerufen wird.

__Parameter__

- **show**: Gibt an, ob der Cursor angezeigt (True) oder ausgeblendet (False) ist.


## synonyms(button)

Gibt eine Liste von Synonymen für eine Maustaste zurück. Zum Beispiel sind 1 und
'left_button' Synonyme.

__Parameter__

- **button**: Ein Button-Wert.

__Gibt zurück__

- Eine Liste von Synonymen.


</div>