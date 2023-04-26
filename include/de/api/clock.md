<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __clock__

Das `clock`-Objekt bietet grundlegende Zeitfunktionen. Ein `clock`-Objekt wird automatisch erstellt, wenn das Experiment beginnt.

__Beispiel__

~~~ .python
# Zeitstempel vor und nach dem Schlafen für 1000 ms erhalten
t0 = clock.time()
clock.sleep(1000)
t1 = clock.time()
vergangene_zeit = t1 - t0
print(f'Das sollte 1000 sein: {vergangene_zeit}')
~~~

[TOC]

## loop_for(ms, throttle=None, t0=None)

*Neu in v3.2.0*

Ein Iterator, der für eine feste Zeit läuft.

__Parameter__

- **ms**: Die Anzahl der Millisekunden, für die die Schleife ausgeführt werden soll.
- **throttle**: Eine Schlafperiode zwischen jeder Iteration.
- **t0**: Eine Startzeit. Wenn `None`, ist die Startzeit der Moment, in dem die Iteration beginnt.

__Rückgabe__

- 

__Beispiel__

~~~ .python
for ms in clock.loop_for(100, throttle=10):
    print(ms)
~~~



## once_in_a_while(ms=1000)

*Neu in v3.2.0*

Gibt periodisch `True` zurück. Dies ist hauptsächlich nützlich
für die Ausführung 
von Code (z. B. innerhalb einer `for`-Schleife), der nur gelegentlich 
ausgeführt werden soll.

__Parameter__

- **ms**: Die minimale Wartezeit.

__Rückgabe__

- `True` nach (mindestens) der minimalen Wartezeit 
seit dem letzten Aufruf von `Clock.once_in_a_while()`, oder
`False` andernfalls.

__Beispiel__

~~~ .python
for i in range(1000000):
    if clock.once_in_a_while(ms=50):
        # Führen Sie diesen Code nur alle 50 ms aus
        print(clock.time())
~~~



## sleep(ms)

Schläft (pausiert) für einen bestimmten Zeitraum.

__Parameter__

- **ms**: Die Anzahl der Millisekunden, für die geschlafen werden soll.

__Beispiel__

~~~ .python
# Erstellen Sie zwei Canvas-Objekte ...
my_canvas1 = Canvas()
my_canvas1.text('1')
my_canvas2 = Canvas()
my_canvas2.text('2')
# ... und zeigen Sie sie mit 1 s dazwischen an
my_canvas1.show()
clock.sleep(1000)
my_canvas2.show()
~~~



## time()

Gibt einen aktuellen Zeitstempel in Millisekunden zurück. Die absolute Bedeutung des Zeitstempels (d. h. wann er 0 war) hängt vom Backend ab.



__Rückgabe__

- Ein Zeitstempel.

__Beispiel__

~~~ .python
t = clock.time()
print(f'Die aktuelle Zeit ist {t}')
~~~



</div>