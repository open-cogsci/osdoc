## reset\_feedback()
Setzt alle Feedback-Variablen auf ihren Anfangszustand zurück.

**Beispiel**  
```js
reset_feedback()
```
<a name="set_subject_nr"></a>

## set\_subject\_nr(nr)
Legt die Teilnehmernummer und Parität (gerade/ungerade) fest. Diese Funktion wird automatisch aufgerufen, wenn ein Experiment gestartet wird. Sie müssen sie also nur selbst aufrufen, wenn Sie die Teilnehmernummer überschreiben möchten, die beim Start des Experiments angegeben wurde.

| Param | Typ | Beschreibung |
| --- | --- | --- |
| nr | <code>Number</code> | Die Teilnehmernummer |

**Beispiel**  
```js
set_subject_nr(1)
console.log('Teilnehmernr. = ' + vars.subject_nr)
console.log('Teilnehmerparität = ' + vars.subject_parity)
```
<a name="sometimes"></a>

## sometimes([p])
Gibt mit einer bestimmten Wahrscheinlichkeit true zurück. (Für fortgeschrittene Zufallsverteilungen verwenden Sie das Paket `random-ext`, das als `random` verfügbar ist.)



| Param | Typ | Default | Beschreibung |
| --- | --- | --- | --- |
| [p] | <code>Number</code> | <code>.5</code> | Die Wahrscheinlichkeit, dass true zurückgegeben wird |

**Beispiel**  
```js
if (sometimes()) {
  console.log('Manchmal gewinnt man')
} else {
  console.log('Manchmal verliert man')
}
```
<a name="xy_from_polar"></a>

## xy\_from\_polar(rho, phi, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Konvertiert Polarkoordinaten (Abstand, Winkel) in kartesische Koordinaten (x, y).


**Gibt zurück**: <code>Array.&lt;Number&gt;</code> - Ein [x, y] Array.  

| Param | Typ | Default | Beschreibung |
| --- | --- | --- | --- |
| rho | <code>Number</code> |  | Die radiale Koordinate, auch Abstand oder Exzentrizität. |
| phi | <code>Number</code> |  | Die Winkelkoordinate. Dies entspricht einer Uhrzeigersinn-Drehung in Grad (also nicht in Radiant), wobei 0 gerade nach rechts zeigt. |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Der Referenzpunkt. |

**Beispiel**  
```js
// ECMA 5.1
var xy1 = xy_from_polar(100, 45)
var xy2 = xy_from_polar(100, -45)
var c = Canvas()
c.line({sx: xy1[0], sy: xy1[1], ex: -xy1[0], ey: -xy1[1]})
c.line({sx: xy2[0], sy: xy2[1], ex: -xy2[0], ey: -xy2[1]})
c.show()
// ECMA 6
let [x1, y1] = xy_from_polar(100, 45)
let [x2, y2] = xy_from_polar(100, -45)
let c = Canvas()
c.line({sx: x1, sy: y1, ex: -x1, ey: -y1})
c.line({sx: x2, sy: y2, ex: -x2, ey: -y2})
c.show()
```
<a name="xy_to_polar"></a>

## xy\_to\_polar(x, y, [pole]) ⇒ <code>Array.&lt;Number&gt;</code>
Konvertiert kartesische Koordinaten (x, y) in Polarkoordinaten (Abstand, Winkel).

**Gibt zurück**: <code>Array.&lt;Number&gt;</code> - Ein [rho, phi] Array. Hier ist `rho` die radiale Koordinate, auch Abstand oder Exzentrizität. `phi` ist die Winkelkoordinate in Grad (also nicht in Radiant) und spiegelt eine gegen den Uhrzeigersinn gerichtete Drehung wider, wobei 0 gerade nach rechts zeigt.

| Param | Typ | Default | Beschreibung |
| --- | --- | --- | --- |
| x | <code>Number</code> |  | Die X-Koordinate. |
| y | <code>Number</code> |  | Die Y-Koordinate |
| [pole] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Der Referenzpunkt. |

**Beispiel**  
```js
// ECMA 5.1 (browser + desktop)
var rho_phi = xy_to_polar(100, 100)
var rho = rho_phi[0]
var phi = rho_phi[1]
// ECMA 6 (browser only)
let [rho, phi] = xy_to_polar(100, 100)
```
<a name="xy_distance"></a>

## xy\_distance(x1, y1, x2, y2) ⇒ <code>Number</code>
Gibt den Abstand zwischen zwei Punkten an.

**Gibt zurück**: <code>Number</code> - Der Abstand zwischen den beiden Punkten.  

| Param | Typ | Beschreibung |
| --- | --- | --- |
| x1 | <code>Number</code> | Die x-Koordinate des ersten Punkts. |
| y1 | <code>Number</code> | Die y-Koordinate des ersten Punkts. |
| x2 | <code>Number</code> | Die x-Koordinate des zweiten Punkts. |
| y2 | <code>Number</code> | Die y-Koordinate des zweiten Punkts. |

<a name="xy_circle"></a>

## xy\_circle(n, rho, [phi0], [pole]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Erstellt eine Liste von Punkten (x, y Koordinaten) in einem Kreis. Dies kann verwendet werden, um Reize in einer kreisförmigen Anordnung darzustellen.

**Rückgabe**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Ein Array aus [x,y]-Koordinatenarrays.  

| Parameter | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | Die Anzahl der zu generierenden x,y-Koordinaten. |
| rho | <code>Number</code> |  | Der radiale Koordinaten-, auch Abstands- oder Exzentrizitätswert, des ersten Punktes. |
| [phi0] | <code>Number</code> | <code>0</code> | Der Winkelkoordinatenwert für die erste Koordinate. Dies ist eine Drehung gegen den Uhrzeigersinn in Grad (d.h. nicht im Bogenmaß), wobei 0 gerade rechts ist. |
| [pol] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Der Bezugspunkt. |

**Beispiel**  
```js
// Zeichne 8 Rechtecke um einen zentralen Fixationspunkt
// ECMA 5.1 (Browser + Desktop)
var c = Canvas()
c.fixdot()
var points = xy_circle(8, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (nur Browser)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_circle(8, 100)) {
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
```
<a name="xy_grid"></a>

## xy\_grid(n, abstand, [pol]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Erzeugt eine Liste von Punkten (x,y-Koordinaten) in einem Raster. Dies kann verwendet
werden, um Reize in einer Rasteranordnung darzustellen.


**Rückgabe**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Ein Array aus [x,y]-Koordinatenarrays.  

| Parameter | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| n | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | Eine Zahl, die die Anzahl der     Spalten und Zeilen angibt, so dass `n=2` ein 2x2-Raster anzeigt, oder ein [n_col,     n_row] Array, so dass `n=[2,3]` ein 2x3-Raster anzeigt. |
| abstand | <code>Number</code> \| <code>Array.&lt;Number&gt;</code> |  | Ein numerischer Wert, der den     Abstand zwischen den Zellen angibt, oder ein [col_spacing, row_spacing]-Array. |
| [pol] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Der Bezugspunkt. |

**Beispiel**  
```js
// Zeichne ein 4x4 Raster von Rechtecken
// ECMA 5 (Desktop + Browser)
var c = Canvas()
c.fixdot()
var points = xy_grid(4, 100)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()
// ECMA 6 (nur Browser)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_grid(4, 100)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```
<a name="xy_random"></a>

## xy\_random(n, breite, höhe, [min_abstand], [pol]) ⇒ <code>Array.&lt;Array.&lt;Number&gt;&gt;</code>
Erzeugt eine Liste von zufälligen Punkten (x,y-Koordinaten) mit einem Minimum
Abstand zwischen jedem Punktepaar. Diese Funktion wirft einen Fehler aus
wenn die Koordinatenliste nicht generiert werden kann, üblicherweise, weil es zu viele Punkte gibt, der min_dist zu hoch eingestellt ist oder die Breite oder Höhe zu niedrig eingestellt sind.


**Rückgabe**: <code>Array.&lt;Array.&lt;Number&gt;&gt;</code> - Ein Array aus [x,y]-Koordinatenarrays.  

| Parameter | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| n | <code>Number</code> |  | Die Anzahl der zu generierenden Punkte. |
| breite | <code>Number</code> |  | Die Breite des Feldes mit zufälligen Punkten. |
| höhe | <code>Number</code> |  | Die Höhe des Feldes mit zufälligen Punkten. |
| [min_abstand] | <code>Number</code> | <code>0</code> | Der minimale Abstand zwischen den Punkten. |
| [pol] | <code>Array.&lt;Number&gt;</code> | <code>[0, 0]</code> | Der Bezugspunkt. |

**Beispiel**  
```js
// Zeichne 50 Rechtecke in einem Zufallsgitter
// ECMA 5 (Desktop + Browser)
var c = Canvas()
c.fixdot()
var points = xy_random(50, 500, 500, 40)
for (var i in points) {
  var x = points[i][0]
  var y = points[i][1]
  c.rect({x: x - 10, y: y - 10, w: 20, h: 20})
}
c.show()   
// ECMA 6 (nur Browser)
let c = Canvas()
c.fixdot()
for (let [x, y] of xy_random(50, 500, 500, 40)) {
  c.rect({x: x-10, y: y-10, w: 20, h: 20})
}
c.show()
```