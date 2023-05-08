title: Schleifen und unabhängige Variablen
hash: f52d2b6f370a4abedc40605527622cea0ff9e57163ef51e6d8d4e39ff35789ec
locale: de
language: German

Das LOOP-Element hat zwei wichtige Funktionen:

- Es führt ein anderes Element mehrmals aus.
- Hier definieren Sie normalerweise Ihre unabhängigen Variablen, d. h. die Variablen, die Sie in Ihrem Experiment manipulieren.

[TOC]

## Das auszuführende Element

Ein LOOP ist immer mit einem anderen Element verbunden: dem auszuführenden Element. Sie wählen das auszuführende Element im Feld "Ausführen". In den meisten Fällen handelt es sich dabei um eine SEQUENCE, die mehrere Elemente nacheinander ausführt.

Zwei häufige SEQUENCE-LOOP-Strukturen sind:

- Wenn eine SEQUENCE einer einzelnen Testphase entspricht (üblicherweise *trial_sequence* genannt), entspricht ein LOOP, der mit dieser Sequenz verbunden ist, mehreren Testphasen oder einem Block (üblicherweise *block_loop* genannt).
- Wenn eine SEQUENCE einem Block von Testphasen gefolgt von einer Feedback-Anzeige entspricht (üblicherweise *block_sequence* genannt), entspricht ein LOOP, der mit dieser Sequenz verbunden ist, mehreren Blöcken oder einer vollständigen experimentellen Sitzung (üblicherweise *experimental_loop* genannt).

## Unabhängige Variablen definieren

Die LOOP-Tabelle ist eine leistungsstarke und dennoch einfache Möglichkeit, unabhängige Variablen zu definieren. Jede Spalte in der Tabelle entspricht einer Variable; jede Zeile entspricht einem Zyklus, d. h. einer Stufe der Variable. Zum Beispiel sieht eine einfache Schleife mit einer Variable (`animal`) und zwei Zyklen ("cat" und "dog") so aus:

animal |
------ |
cat    |
dog    |

Die Schleife hat einige wichtige Optionen:

*Wiederholen* gibt an, wie oft jeder Zyklus ausgeführt werden soll. Im obigen Beispiel ist die Wiederholung auf 2 gesetzt, was bedeutet, dass *trial_sequence* zweimal aufgerufen wird, während die Variable `animal` den Wert "cat" und zweimal den Wert "dog" hat (insgesamt also viermal).

*Reihenfolge* gibt an, ob die Zyklen sequenziell oder in zufälliger Reihenfolge ausgeführt werden sollen. Die Randomisierung ist vollständig, in dem Sinne, dass die gesamte Liste der Anzahl der Zyklen × Wiederholungen randomisiert wird.

## Unabhängige Variablen aus einer Datei lesen

Wenn Sie unabhängige Variablen aus einer Datei lesen möchten, anstatt sie in die LOOP-Tabelle einzugeben, können Sie dies wie folgt tun:

- Setzen Sie *Quelle* auf *Datei*.
- Wählen Sie eine Excel-(`.xlsx`) oder CSV-(`.csv`) Datei im *Datei*-Eingabefeld.

Die Quelldatei folgt den gleichen Konventionen wie die LOOP-Tabelle; d. h. jede Spalte entspricht einer Variable, und jede Zeile entspricht einem Zyklus.

CSV-Dateien sollten im folgenden Format vorliegen:

- Nur-Text
- kommagetrennt
- doppelte Anführungszeichen (wörtliche doppelte Anführungszeichen werden mit umgekehrten Schrägstrichen ausgewichen)
- UTF-8-kodiert

## Die Schleife unterbrechen

Wenn Sie die Schleife beenden möchten, bevor alle Zyklen ausgeführt wurden, können Sie eine "break-if"-Ausdruck angeben. Dieser "break-if"-Ausdruck folgt der gleichen Syntax wie andere bedingte Ausdrücke, wie in:

- %link:manual/variables%

Zum Beispiel würde der folgende "break-if"-Ausdruck die Schleife unterbrechen, sobald eine korrekte Antwort gegeben wird:

```python
correct == 1
```

Die Option *Bei erstem Zyklus auswerten* gibt an, ob der "break-if"-Ausdruck vor dem ersten Zyklus ausgewertet werden sollte, in welchem Fall möglicherweise kein Zyklus ausgeführt wird, oder nur vor dem zweiten Zyklus, bei dem immer mindestens ein Zyklus ausgeführt wird. In einigen Fällen wird der "break-if"-Ausdruck auf eine Variable verweisen, die erst nach dem ersten Zyklus definiert ist. In diesem Fall sollten Sie die Option "Bei erstem Zyklus auswerten" deaktivieren, um einen "Variable existiert nicht"-Fehler zu vermeiden.

## Erstellung eines vollfaktoriellen Designs

Wenn Sie auf *Vollfaktorielles Design* klicken, öffnen Sie einen Assistenten, mit dem Sie einfach ein vollfaktorielles Design erstellen können, d. h. ein Design, bei dem jede Kombination von Faktoren auftritt.

## Pseudorandomisierung

Sie können Einschränkungen für die Pseudorandomisierung zum Skript des LOOP-Elements hinzufügen. Dies mischt die Zeilen, selbst wenn die Reihenfolge auf sequenziell eingestellt ist. (Derzeit ist dies nicht über die GUI möglich.)

Beispiel: Stellen Sie sicher, dass Wiederholungen desselben Worts (gegeben durch die Variable `word`) durch mindestens 4 Zyklen getrennt sind:

```python
constrain word mindist=4
```

Beispiel: Stellen Sie sicher, dass das gleiche Wort nicht wiederholt wird:

```python
constrain word maxrep=1
```

`constrain` Befehle müssen *nach* `setcycle` Befehlen stehen.

## Erweiterte Schleifenoperationen

Befehle für erweiterte Schleifenoperationen müssen *nach* `constrain` und `setcycle` Befehlen stehen.

### fullfactorial

Die `fullfactorial` Anweisung behandelt die Schleifentabelle als Eingabe für ein vollfaktorielles Design. Zum Beispiel würde die folgende Schleifentabelle:

cue   | duration
----- | --------
left  | 0
right | 100
      | 200

Zu diesem Ergebnis führen:

cue   | duration
----- | --------
left  | 0
left  | 100
left  | 200
right | 0
right | 100
right | 200

### shuffle

`shuffle` ohne Argument mischt die gesamte Tabelle. Wenn ein Spaltenname angegeben ist (`shuffle cue`), wird nur diese Spalte gemischt.

### shuffle_horiz

`shuffle_horiz` mischt alle Spalten horizontal. Wenn mehrere Spalten angegeben sind, werden nur diese Spalten horizontal gemischt.

Zum Beispiel, wenn `shuffle_horiz word1 word2` auf die folgende Tabelle angewendet wird:

word1 | word2 | word3
----- | ----- | -----
cat   | dog   | bunny
cat   | dog   | bunny
cat   | dog   | bunny

Das Ergebnis könnte sein (d.h. Werte werden zufällig zwischen `word1` und `word2` getauscht, aber nicht `word3`):

word1 | word2 | word3
----- | ----- | -----
dog   | cat   | bunny
dog   | cat   | bunny
cat   | dog   | bunny

### slice

`slice [from] [to]` wählt einen Ausschnitt aus der Schleife. Es erfordert einen Start- und einen Endindex, wobei 0 die erste Zeile ist und negative Werte von hinten nach vorne gezählt werden. (Genau wie das Zerteilen von Listen in Python, mit anderen Worten.)

Zum Beispiel, wenn `slice 1 -1` auf die folgende Tabelle angewendet wird:

word  |
----- |
cat   |
dog   |
bunny |
horse |

Das Ergebnis wäre:

word  |
----- |
dog   |
bunny |

### sort

`sort [column]` sortiert eine einzelne Spalte, ohne die anderen Spalten zu ändern.

### sortby

`sortby [column]` sortiert die gesamte Tabelle nach einer einzelnen Spalte.

### reverse

`reverse` kehrt die Reihenfolge der gesamten Tabelle um. Wenn ein Spaltenname angegeben ist (z. B. `reverse word`), wird nur diese Spalte umgekehrt, ohne die anderen Spalten zu ändern.

### roll

`roll [value]` rollt die gesamte Tabelle nach vorne (für positive Werte) oder nach hinten (für negative Werte). Wenn ein Spaltenname angegeben ist (z. B. `roll 1 word`), wird nur diese Spalte gerollt, ohne die anderen Spalten zu ändern.

Zum Beispiel, wenn `roll 1` auf die folgende Tabelle angewendet wird:

word  |
----- |
cat   |
dog   |
bunny |
horse |

Das Ergebnis wäre:

word  |
----- |
horse |
cat   |
dog   |
bunny |

### weight

`weight [column]` wiederholt jede Zeile entsprechend einem Gewichtungswert, der in einer Spalte angegeben ist.

Zum Beispiel, wenn `weight w` auf die folgende Tabelle angewendet wird:

word  | w
----- | -
cat   | 0
dog   | 0
bunny | 2
horse | 1

Das Ergebnis wäre:

word  | w
----- | -
bunny | 2
bunny | 2
horse | 1

## Vorschau der Schleife

Wenn Sie Einschränkungen angegeben haben oder erweiterte Schleifenoperationen verwendet haben, ist es ratsam zu prüfen, ob das Ergebnis wie erwartet ist. Dazu können Sie eine Vorschau der Schleifentabelle erstellen, wie sie beim Ausführen des Experiments sein wird (oder sein könnte, im Falle von Zufallsprinzip).

Um eine Vorschau zu erstellen, klicken Sie auf die Schaltfläche *Vorschau*.

## Zugriff auf die Schleifentabelle in Python Inline-Skript

Die ursprüngliche LOOP-Tabelle, wie Sie sie in der OpenSesame-Benutzeroberfläche sehen, ist ein [`DataMatrix`](http://datamatrix.cogsci.nl/) Objekt namens `dm` und ist Eigenschaft des LOOP-Elements.

Diese ursprüngliche LOOP-Tabelle wird normalerweise auf verschiedene Weise transformiert; zum Beispiel kann die Reihenfolge der Zeilen zufällig sein und Zeilen können mehrere Male wiederholt werden. Die transformierte LOOP ist ebenfalls ein `DataMatrix` Objekt und heißt `live_dm`. `live_dm` wird erstellt, kurz bevor die Schleife ausgeführt wird und wird auf `None` gesetzt, wenn die Schleife abgeschlossen ist; das heißt, `live_dm` ist nur während der *Lauf*-Phase der LOOP verfügbar.

Schließlich wird der Index der aktuellen Zeile als experimentelle Variable `live_row` gespeichert. Das heißt, `live_row` zeigt die derzeit aktive Zeile von `live_dm` an.

Also stellen wir uns vor, dass wir eine LOOP namens *block_loop* haben. Wir könnten dann auf die LOOP-Tabelle in einem Python Inline-Script wie folgt zugreifen:

~~~ .python
print('Die ursprüngliche Loop-Tabelle:')
print(items['block_loop'].dm)

print('Die transformierte Loop-Tabelle:')
print(items['block_loop'].live_dm)

print('Die aktuelle Zeile:')
print(items['block_loop'].live_dm[var.live_row])
~~~

Sie können sogar die LOOP-Tabelle programmatisch definieren. Sie müssen dies in der Prepare-Phase eines INLINE_SCRIPT tun, das dem LOOP vorausgeht.

```python
from datamatrix import DataMatrix

items['block_loop'].dm = DataMatrix(length=4)
items['block_loop'].dm.cue_side = 'links', 'rechts', 'links', 'rechts'
items['block_loop'].dm.cue_validity = 'gültig', 'gültig', 'ungültig', 'ungültig'
```

`DataMatrix`-Objekte sind leistungsfähige Strukturen, um mit Tabellendaten zu arbeiten. Weitere Informationen finden Sie unter:

- <https://pydatamatrix.eu/>