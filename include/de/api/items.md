<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __items__

Das `items`-Objekt bietet einen dict-ähnlichen Zugriff auf die Elemente. Es ist hauptsächlich
nützlich für das programmgesteuerte Ausführen von Elementen.

Ein `items`-Objekt wird automatisch erstellt, wenn das Experiment beginnt.

Zusätzlich zu den unten aufgeführten Funktionen werden die folgenden Semantiken unterstützt:

__Beispiel__

~~~ .python
# Ein Sketchpad-Element programmgesteuert vorbereiten und ausführen.
items.execute('mein_sketchpad')
# Überprüfen, ob ein Element vorhanden ist
if 'mein_sketchpad' in items:
    print('mein_sketchpad existiert')
# Ein Element löschen
del items['mein_sketchpad']
# Durch alle Elementnamen gehen
for item_name in items:
    print(item_name)
~~~

[TOC]

## execute(name)

Führt die Run- und Prepare-Phasen eines Elements aus und aktualisiert den
Element-Stack.


__Parameter__

- **name**: Ein Elementname.

__Beispiel__

~~~ .python
items.execute('ziel_sketchpad')
~~~



## new(_type, name=None, script=None, allow_rename=True)

Erstellt ein neues Element.


__Parameter__

- **_type**: Der Elementtyp.
- **name**: Der Elementname oder None, um einen eindeutigen Namen basierend auf dem Elementtyp zu wählen.
- **script**: Ein Definitionsskript oder None, um mit einem leeren Element zu beginnen.
- **allow_rename**: Gibt an, ob OpenSesame einen anderen Namen verwenden darf als den, der
als `name` angegeben ist, um doppelte Namen usw. zu vermeiden.

__Rückgabe__

- Das neu generierte Element.

__Beispiel__

~~~ .python
items.new('sketchpad', name='mein_sketchpad')
items['mein_sketchpad'].prepare()
items['mein_sketchpad'].run()
~~~



## prepare(name)

Führt die Prepare-Phase eines Elements aus und aktualisiert den Element-Stack.


__Parameter__

- **name**: Ein Elementname.

__Beispiel__

~~~ .python
items.prepare('ziel_sketchpad')
items.run('ziel_sketchpad')
~~~



## run(name)

Führt die Run-Phase eines Elements aus und aktualisiert den Element-Stack.


__Parameter__

- **name**: Ein Elementname.

__Beispiel__

~~~ .python
items.prepare('ziel_sketchpad')
items.run('ziel_sketchpad')
~~~



## valid_name(item_type, suggestion=None)

Erzeugt einen eindeutigen Namen, der gültig ist und dem gewünschten
Namen ähnelt.


__Parameter__

- **item_type**: Der Typ des Elements, für das ein Name vorgeschlagen werden soll.
- **suggestion**: Der gewünschte Name oder None, um einen Namen basierend auf dem Elementtyp zu wählen.

__Rückgabe__

- Ein eindeutiger Name.

__Beispiel__

~~~ .python
valid_name = items.valid_name('sketchpad', 'ein ungültiger Name')
~~~



</div>