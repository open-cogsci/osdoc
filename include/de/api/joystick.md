<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __joystick__

Wenn Sie das JOYSTICK-Plugin am Anfang Ihres Experiments einfügen, wird ein
JOYSTICK-Objekt automatisch Teil des Experiment-Objekts
und kann innerhalb eines INLINE_SCRIPT-Elements als `joystick` verwendet werden.

{% set arg_joybuttonlist = "Eine Liste von Buttons, die akzeptiert werden oder " +
"`None`, um alle Buttons zu akzeptieren." %}
{% set arg_timeout = "Ein Zeitlimit in Millisekunden oder `None` für kein " +
"Zeitlimit." %}

[TOC]

## flush(self)

Löscht alle ausstehenden Eingaben, nicht nur auf den Joystick bezogen.



__Gibt zurück__

- True, wenn Joystick-Eingaben ausstehend waren (d.h., wenn etwas zu
löschen war) und False andernfalls.


## get_joyaxes(timeout=None)

Wartet auf Joystick-Achsenbewegungen.


__Parameter__

- **timeout**: Ein Zeitlimit in Millisekunden oder `None`, um das Standard-Zeitlimit zu verwenden.

__Gibt zurück__

- Ein `(position, timestamp)` Tupel. `position` ist `None`, wenn ein Timeout
auftritt. Andernfalls ist `position` ein `(x, y, z)` Tupel.


## get_joyballs(timeout=None)

Wartet auf Joystick-Trackball-Bewegungen.


__Parameter__

- **timeout**: Ein Zeitlimit in Millisekunden oder `None`, um das Standard-Zeitlimit zu verwenden.

__Gibt zurück__

- Ein `(position, timestamp)` Tupel. Die Position ist `None`, wenn ein
Timeout auftritt.


## get_joybutton(joybuttonlist=None, timeout=None)

Sammelt Joystick-Tasteneingaben.


__Parameter__

- **joybuttonlist**: Eine Liste von Buttons, die akzeptiert werden oder `None`, um die Standard-Buttonliste 
zu verwenden.
- **timeout**: Ein Zeitlimit in Millisekunden oder `None`, um das Standard-Zeitlimit zu verwenden.

__Gibt zurück__

- Ein (joybutton, timestamp) Tupel. Der joybutton ist `None`, wenn ein
Timeout auftritt.


## get_joyhats(timeout=None)

Wartet auf Joystick-Hut-Bewegungen.


__Parameter__

- **timeout**: Ein Zeitlimit in Millisekunden oder `None`, um das Standard-Zeitlimit zu verwenden.

__Gibt zurück__

- Ein `(position, timestamp)` Tupel. `position` ist `None`, wenn ein Timeout
auftritt. Andernfalls ist `position` ein `(x, y)` Tupel.


## get_joyinput(joybuttonlist=None, timeout=None)

Wartet auf jegliche Joystick-Eingaben (Tasten, Achsen, Hüte oder Trackballs).


__Parameter__

- **joybuttonlist**: Eine Liste von Buttons, die akzeptiert werden oder `None`, um die Standard-Buttonliste 
zu verwenden.
- **timeout**: Ein Zeitlimit in Millisekunden oder `None`, um das Standard-Zeitlimit zu verwenden.

__Gibt zurück__

- Ein (event, value, timestamp) Tupel. Der Wert ist `None`, wenn ein Timeout
auftritt. `event` ist eines von `None`, 'joybuttonpress',
'joyballmotion', 'joyaxismotion' oder 'joyhatmotion'


## input_options(self)

Erstellt eine Liste mit der Anzahl der verfügbaren Tasten, Achsen, Trackballs
und Hüte.



__Gibt zurück__

- Eine Liste mit der Anzahl der Eingaben als: [Tasten, Achsen, Trackballs,
Hüte].


## set_joybuttonlist(joybuttonlist=None)

Legt eine Liste der akzeptierten Tasten fest.


__Parameter__

- **joybuttonlist**: {{arg_joybuttonlist}}


## set_timeout(timeout=None)

Legt ein Zeitlimit fest.


__Parameter__

- **timeout**: {{arg_timeout}}


</div>