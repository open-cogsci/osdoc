<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __srbox__

Wenn Sie das srbox-Plugin zu Beginn Ihres Experiments einfügen, wird automatisch eine
Instanz von SRBOX Teil des Experiment-
Objekts und
kann innerhalb eines inline_script-Elements als SRBOX aufgerufen werden.

__Wichtiger Hinweis 1:__

Wenn Sie kein Gerät angeben, versucht das Plug-In, den
SR Box-Port automatisch zu erkennen. Auf manchen Systemen friert dies jedoch das Experiment ein, daher ist es besser, ein Gerät explizit anzugeben.

__Wichtiger Hinweis 2:__

Sie
müssen [srbox.start] aufrufen, um den SR Box in den Sendemodus zu versetzen,
bevor
Sie [srbox.get_button_press] aufrufen, um einen Tastendruck zu erfassen.

__Beispiel:__
~~~ .python
t0 = clock.time()
srbox.start()
button, t1 = srbox.get_button_press(allowed_buttons=[1, 2],
                                    require_state_change=True)
if button == 1:
    response_time = t1 - t0
print(f'Taste 1 wurde in {response_time} ms gedrückt!')
srbox.stop()
~~~
[TOC]

## get_button_press(allowed_buttons=None, timeout=None, require_state_change=False)

Erfasst einen Tastendruck von der SR-Box.


__Parameter__

- **allowed_buttons**: Eine Liste der akzeptierten Tasten oder `None`, um alle
Tasten zu akzeptieren. Gültige Tasten sind Ganzzahlen zwischen 1 und 8.
- **timeout**: Ein Zeitüberschreitungswert in Millisekunden oder `None` für keine Zeitüberschreitung.
- **require_state_change     Gibt an, ob bereits gedrückte Tasten akzeptiert werden sollten**: (False) oder ob nur eine Statusänderung von nicht gedrückt auf gedrückt
akzeptiert wird (True).

__Rückgabe__

- Ein `(button_list, timestamp)` Tupel. `button_list` ist `None`, wenn keine
Taste gedrückt wurde (d. h. eine Zeitüberschreitung aufgetreten ist).


## send(ch)

Sendet ein einzelnes Zeichen an die SR-Box. Senden Sie '`', um alle
Lichter auszuschalten, 'a' für Licht 1 ein, 'b' für Licht 2 ein,'c' für Lichter
1 und 2 ein usw.


__Parameter__

- **ch**: Das zu sendende Zeichen. Wenn ein `str` übergeben wird, wird es in
`bytes` unter Verwendung der UTF-8-Codierung kodiert.


## start(self)

Schaltet den Sendemodus ein, so dass die SR-Box beginnt, Ausgaben zu senden.
Die SR-Box muss im Sendemodus sein, wenn Sie
[srbox.get_button_press] aufrufen.




## stop(self)

Schaltet den Sendemodus aus, so dass die SR-Box aufhört, Ausgaben zu liefern.




</div>