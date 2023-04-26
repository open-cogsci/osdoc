<div class="ClassDoc YAMLDoc" markdown="1">

# Klasse __Keyboard__

Die `Keyboard`-Klasse wird verwendet, um Tastaturantworten zu erfassen. Normalerweise erstellen Sie
ein `Keyboard`-Objekt mit der `Keyboard()`-Fabrikfunktion, wie in dem
Abschnitt [Ein Keyboard erstellen](#creating-a-keyboard) beschrieben.

__Beispiel__

~~~ .python
# Warten auf eine 'z'- oder 'x'-Taste mit einer Zeitüberschreitung von 3000 ms
my_keyboard = Keyboard(keylist=['z', 'x'], timeout=3000)
start_time = clock.time()
key, end_time = my_keyboard.get_key()
response = key
response_time = end_time - start_time
~~~

[TOC]

## Wissenswertes

### Erstellen eines Keyboards

Erstellen Sie normalerweise ein `Keyboard` mit der `Keyboard()`-Fabrikfunktion:

~~~ .python
my_keyboard = Keyboard()
~~~

Optional können Sie [Antwort-Keywords](#response-keywords) an `Keyboard()`
übergeben, um das Standardverhalten festzulegen:

~~~ .python
my_keyboard = Keyboard(timeout=2000)
~~~

### Tastennamen

- Tastennamen können sich zwischen Backends unterscheiden.
- Tasten können entweder durch Zeichen oder Name identifiziert werden und sind nicht auf Groß- und Kleinschreibung angewiesen.
  Zum Beispiel:
  - Die Taste 'a' wird durch 'a' und 'A' dargestellt
  - Der Pfeil nach oben wird durch 'up' und 'UP' dargestellt
  - Die Taste '/' wird durch '/', 'slash' und 'SLASH' dargestellt
  - Die Leertaste wird durch 'space' und 'SPACE' dargestellt
- Um den Namen einer Taste herauszufinden, können Sie:
  - Klicken Sie auf die Schaltfläche "Verfügbare Schlüssel auflisten" des KEYBOARD_RESPONSE-Elements.
  - Erfassen Sie einen Tastendruck mit einem KEYBOARD_RESPONSE-Element und zeigen Sie den Tastennamen
    durch einen FEEDBACK-Artikel mit dem Text "Sie haben [response]" darauf gedrückt an.

### Antwort-Keywords

Funktionen, die `**resp_args` akzeptieren, nehmen die folgenden Stichwortargumente an:

- `timeout` gibt einen Timeout-Wert in Millisekunden an oder wird auf `None` gesetzt, um den Timeout zu deaktivieren.
- `keylist` gibt eine Liste der akzeptierten Tasten an oder wird auf `None`
  gesetzt, um alle Tasten zu akzeptieren.

~~~ .python
# Hole einen linken oder rechten Pfeildruck mit einer Zeitüberschreitung von 3000 ms
my_keyboard = Keyboard()
key, time = my_keyboard.get_key(keylist=[u'left', u'right'], timeout=3000)
~~~

Antwort-Keywords wirken sich nur auf die aktuelle Operation aus (außer wenn sie an
`Keyboard()` übergeben werden). Um das Verhalten für alle nachfolgenden zu ändern
Operationen, setzen Sie die Antwort-Eigenschaften direkt:

~~~ .python
# Erhalte zwei Tastendrücke A oder B mit einer Zeitüberschreitung von 5000 ms
my_keyboard = Keyboard()
my_keyboard.keylist = [u'a', u'b']
my_keyboard.timeout = 5000
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

Oder übergeben Sie die Antwortoptionen an [keyboard.__init__][__init__]:

~~~ .python
# Erhalte zwei Tastendrücke A oder B mit einer Zeitüberschreitung von 5000 ms
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

## flush(self)

Löscht alle ausstehenden Tastatureingaben, nicht nur auf die Tastatur beschränkt.

__Gibt zurück__

- True, wenn eine Taste gedrückt wurde (dh wenn es etwas zum Löschen gab), und False andernfalls.


## get_key(\*arglist, \*\*kwdict)

Sammelt einen einzelnen Tastendruck.

__Parameter__

- **\*\*resp_args**: Optionale [Antwort-Keywords](#response-keywords) (`timeout` und
  `keylist`), die für diesen Aufruf von `Keyboard.get_key()` verwendet werden.
  Dies wirkt sich nicht auf nachfolgende Operationen aus.

__Gibt zurück__

- Ein `(key, timestamp)` Tupel. `key` ist None, wenn ein Timeout auftritt.

__Beispiel__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key(timeout=5000)
if response is None:
        print(u'Es ist eine Zeitüberschreitung aufgetreten!')
~~~



## get_key_release(\*arglist, \*\*kwdict)

*Neu in v3.2.0*

Sammelt eine einzelne Tastenfreigabe.

*Wichtig:* Diese
Funktion geht derzeit von einem QWERTY-Tastaturlayout aus
(unähnlich
`Keyboard.get_key()`). Das bedeutet, dass der zurückgegebene
`key` falsch sein könnte bei
nicht-QWERTY-Tastaturlayouts. Darüber hinaus ist
diese Funktion nicht für das *psycho*-Backend implementiert.

__Parameter__

- **\*\*resp_args**: Optionale [Antwort-Keywords](#response-keywords) (`timeout` und
  `keylist`), die für diesen Aufruf von
  `Keyboard.get_key_release()` verwendet werden. Dies wirkt sich nicht auf nachfolgende
  Operationen aus.

__Gibt zurück__

- Ein `(key, timestamp)` Tupel. `key` ist None, wenn ein Timeout auftritt.

__Beispiel__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key_release(timeout=5000)
if response is None:
        print(u'Ein Timeout ist aufgetreten!')
~~~



## get_mods(self)

Gibt eine Liste der momentan gedrückten Tastatur-Moderatoren (z.B. Umschalttaste, Alt, etc.) zurück.



__Returns__

- Eine Liste der Tastatur-Moderatoren. Eine leere Liste wird zurückgegeben, wenn keine
Moderatoren gedrückt sind.

__Beispiel__

~~~ .python
my_keyboard = Keyboard()
moderators = my_keyboard.get_mods()
if u'shift' in moderators:
        print(u'Die Umschalttaste ist gedrückt!')
~~~



## show_virtual_keyboard(visible=True)

Zeigt oder verbirgt eine virtuelle Tastatur, wenn dies von der
Back-End unterstützt wird. Diese Funktion ist nur notwendig, wenn die virtuelle
Tastatur sichtbar bleiben soll, während mehrzeilige Antworten gesammelt werden.
Andernfalls wird `Keyboard.get_key()` implizit die Tastatur für eine einzelne Zeichenantwort anzeigen und
ausblenden.

Diese Funktion tut nichts für Back-Ends, die keine virtuellen Tastaturen unterstützen.

__Parameter__

- **visible**: True, wenn die Tastatur angezeigt werden soll, False sonst.

__Beispiel__

~~~ .python
my_keyboard = Keyboard()
my_keyboard.show_virtual_keyboard(True)
response1, timestamp1 = my_keyboard.get_key()
response2, timestamp2 = my_keyboard.get_key()
my_keyboard.show_virtual_keyboard(False)
~~~



## synonyms(key)

Gibt eine Liste von Synonymen für einen Tastennamen oder Tastencode zurück. Synonyme
beinhalten alle Variablen als Typen und als Unicode-Zeichenketten (falls zutreffend).



__Returns__

- Eine Liste von Synonymen


## valid_keys(self)

Versucht zu erraten, welche Tastennamen vom Back-End akzeptiert werden. Zur
internen Verwendung.



__Returns__

- Eine Liste gültiger Tastennamen.

</div>