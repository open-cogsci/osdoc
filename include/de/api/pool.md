<div class="ClassDoc YAMLDoc" markdown="1">

# Instanz __pool__

Das `pool`-Objekt bietet dict-ähnlichen Zugriff auf den Datei-Pool. Beim
Überprüfen, ob sich eine Datei im Datei-Pool befindet, werden
mehrere Ordner durchsucht.
Weitere Informationen finden Sie unter `pool.ordner()`.

Ein `pool`-Objekt wird
automatisch erstellt, wenn das Experiment startet.

Zusätzlich zu den unten aufgeführten Funktionen
werden die folgenden Semantiken unterstützt:

__Beispiele__

Grundlegende Verwendung:

~~~ .python
# Erhalte den vollständigen Pfad zu einer Datei im Datei-Pool
print(f'Der vollständige Pfad zu img.png ist {pool["img.png"]}')
# Überprüfe, ob sich eine Datei im Datei-Pool befindet
if 'img.png' in pool:
    print('img.png ist im Datei-Pool')
# Lösche eine Datei aus dem Datei-Pool
del pool['img.png']
# Gehe durch alle Dateien im Datei-Pool. Dabei werden die vollständigen Pfade abgerufen.
for path in pool:
    print(path)
# Überprüfe die Anzahl der Dateien im Datei-Pool
print(f'Es gibt {len(pool)} Dateien im Datei-Pool')
~~~

Hole ein Bild aus dem Datei-Pool und verwende ein `Canvas` um es anzuzeigen.

~~~ .python
image_path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(image_path)
my_canvas.show()
~~~

[TOC]

## hinzufügen(Pfad, neuer_Name=None)

Kopiert eine Datei in den Datei-Pool.

__Parameter__

- **Pfad**: Der vollständige Pfad zur Datei auf der Festplatte.
- **neuer_Name**: Ein neuer Name für die Datei im Pool, oder None, um den ursprünglichen Namen der Datei zu verwenden.

__Beispiel__

~~~ .python
pool.add('/home/username/Pictures/my_ing.png')
~~~

## bereinigen(self)

Entfernt den Pool-Ordner.



## ausweich_ordner(self)

Der vollständige Pfad zum Ausweich-Pool-Ordner, der sich im
`__pool__` Unterordner des aktuellen Experimentordners befindet, oder
`None`, wenn dieser Ordner nicht existiert. Der Reserve-Pool-
Ordner ist hauptsächlich nützlich in Kombination mit einer Versionsverwaltung,
wie git, da dadurch das Experiment als Klartextdatei gespeichert werden kann, auch wenn sich Dateien im Datei-Pool befinden.



__Gibt zurück__

- 

__Beispiel__

~~~ .python
if pool.ausweich_ordner() is not None:
    print('Es gibt einen Ausweich-Pool-Ordner!')
~~~

## dateien(self)

Gibt alle Dateien im Datei-Pool zurück.



__Gibt zurück__

- Eine Liste der vollständigen Pfade.

__Beispiel__

~~~ .python
for path in pool.dateien():
    print(path)
# Äquivalent zu:
for path in pool:
    print(path)
~~~

## ordner(self)

Gibt den vollständigen Pfad zum (Haupt-)Pool-Ordner zurück. Dies ist normalerweise ein
temporärer Ordner, der gelöscht wird, wenn das Experiment beendet ist.



__Gibt zurück__

- Der vollständige Pfad zum Haupt-Pool-Ordner.

__Beispiel__

~~~ .python
print(f'Der Pool-Ordner befindet sich hier: {pool.ordner()}')
~~~

## ordner(inklusive_ausweich_ordner=True, inklusive_experimentpfad=False)

Gibt eine Liste aller Ordner zurück, die durchsucht werden, wenn der
vollständige Pfad zu einer Datei abgerufen wird. Dies sind (in
der Reihenfolge):

1. Der Datei-Pool-Ordner
selbst, wie von `pool.ordner()` zurückgegeben.
2. Der Ordner des aktuellen
Experiments (sofern vorhanden)
3. Der Ausweich-Pool-Ordner, wie von
`pool.ausweich_ordner()` zurückgegeben (sofern vorhanden)

__Parameter__

- **inklusive_ausweich_ordner**: Gibt an, ob der Ausweich-Pool-Ordner einbezogen werden soll, falls
vorhanden.
- **inklusive_experimentpfad**: Gibt an, ob der Experiment-Ordner einbezogen werden soll, falls
vorhanden.

__Gibt zurück__

- Eine Liste aller Ordner.

__Beispiel__

~~~ .python
print('Die folgenden Ordner werden nach Dateien durchsucht:')
for folder in pool.ordner():
    print(folder)
~~~

## in_ordner(Pfad)

Überprüft, ob sich der Pfad im Pool-Ordner befindet. Das unterscheidet sich von
der `Pfad in Pool` Syntax, da es nur den Haupt-Pool-Ordner überprüft,
und nicht den Ausweich-Pool-Ordner und Experiment-Ordner.

__Parameter__

- **Pfad**: Ein Datei-Basename zum Überprüfen.

__Gibt zurück__

- 

__Beispiel__

~~~ .python
print(pool.in_ordner('cue.png'))
~~~

## umbenennen(alter_Pfad, neuer_Pfad)

Benennt eine Datei im Pool-Ordner um.

__Parameter__

- **alter_Pfad**: Der alte Dateiname.
- **neuer_Pfad**: Der neue Dateiname.

__Beispiel__

~~~ .python
pool.umbenennen('my_old_img.png', 'my_new_img.png')
~~~

## Größe(self)

Ermittelt die kombinierte Größe in Bytes aller Dateien im Datei-Pool.



__Gibt zurück__

- 

__Beispiel__

~~~ .python
print(f'Die Größe des Datei-Pools beträgt {pool.size()} Bytes')
~~~



</div>