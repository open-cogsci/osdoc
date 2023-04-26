title: OpenSesame Skript
reviewed: false
hash: 73e219615747fe9d3e0d6444db9859ce306004221b08c7ff0f63e555f160cfa2
locale: de
language: German

[TOC]

## Über OpenSesame Skript

OpenSesame Skript ist eine einfache definitorische Sprache, die ein Experiment definiert. Es ist keine vollwertige Programmiersprache und enthält keine Funktionen wie `for`-Schleifen. Das OpenSesame Skript wird von einer OpenSesame Laufzeitumgebung interpretiert.

OpenSesame Skript unterscheidet sich von den Python-Skripten, die in Inline-Skript-Elementen verwendet werden. Python ist eine echte Programmiersprache mit all der Flexibilität und Komplexität, die dies mit sich bringt. Im Gegensatz dazu wird OpenSesame Skript verwendet, um Experimente auf einfache, menschenlesbare Weise zu definieren.

## Allgemeine Bemerkungen

### Schlagwörter

Einige Elemente, wie form_base und Sketchpad, akzeptieren Schlagwörter. Schlagwörter sind in der Form `Schlagwort=Wert`. Schlagwörter sind optional und sollten auf einen Standardwert zurückfallen.

### Kommentare

Zeichenketten, die mit einer Raute versehen sind, sollten als Kommentare interpretiert werden.

*Beispiel*

	# Dies ist ein Kommentar

### Anführungszeichen

Anführungszeichen sind nicht notwendig, außer bei Zeichenketten, die Leerzeichen oder andere Formen der Interpunktion enthalten. Daher sollten die folgenden Zeilen als identisch interpretiert werden:

	set my_var 'my_value'
	set my_var "my_value"
	set my_var my_value

Die folgenden Zeilen sind jedoch nicht identisch. Tatsächlich ist die erste Zeile nicht gültig, da ein unerwarteter dritter Parameter vorhanden ist.

	set my_var my value
	set my_var "my value"

### Typen

Es gibt keine Typen. Es wird kein Unterschied zwischen Zeichenketten, Ganzzahlen usw. gemacht.

### Elementspezifische Syntax

Einige Elemente haben eine spezifische Syntax. Dies wird im Abschnitt "Anwendbar auf" für jedes der unten diskutierten Schlagwörter angegeben.

### Auflösen von Pfadnamen

TODO

## *define* Anweisung

Beginnt die Definition eines Elements. Nach einer "define"-Anweisung sind alle Zeilen mit einem einzelnen Tabulator eingerückt. Das Ende der Elementdefinition ist die erste Zeichenkette, die nicht mehr eingerückt ist. Verschachtelte "define"-Anweisungen sind nicht erlaubt.

*Anwendbar auf*

Alle Elemente

*Format*

	define [Elementname] [Elementtyp]
		[Elementdefinition]

*Parameter*

|`Elementname`	|der Name des Elements	|
|`Elementtyp`	|die Art des Elements	|

*Beispiel*

	define get_key keyboard_response
		set allowed_responses "a;x"
		set description "Sammelt Tastaturantworten"
		set timeout "unendlich"
		set flush "ja"

## *draw* Anweisung

Definiert ein visuelles Element eines Sketchpad- oder Feedback-Elements.

*Anwendbar auf*

Skizzenblock, Feedback

*Format*

Das Format hängt vom Element ab.

	draw ellipse [links] [oben] [Breite] [Höhe] [Schlagwörter]
	draw circle [x] [y] [radius] [Schlagwörter]
	draw line [links] [rechts] [oben] [unten] [Schlagwörter]
	draw arrow [links] [rechts] [oben] [unten] [Schlagwörter]
	draw textline [x] [y] [text]
	draw image [x] [y] [Pfad]
	draw gabor [x] [y]
	draw noise [x] [y]
	draw fixdot [x] [y]

*Parameter*

|`links` 		|der am weitesten links liegende x-Koordinate		|
|`rechts`		|der am weitesten rechts liegende x-Koordinate	|
|`oben`			|der oberste y-Koordinate			|
|`unten`		|der unterste y-Koordinate		|
|`x` 			|die x-Koordinate				|
|`y`			|die y-Koordinate				|
|`text` 		|Textzeichenkette					|
|`Pfad` 		|der Pfad zu einer Bilddatei		|

*Schlagwörter*

TODO

*Beispiel*

	draw fixdot 0 0

## *log* Anweisung

Zeigt an, dass eine Variable in die Log-Datei geschrieben werden soll.

*Anwendbar auf*

Logger

*Format*

	log [Variablenname]

*Parameter*

|`Variablenname`		|der Name einer Variable	|

*Beispiel*

	log response_time

## *run* Anweisung

Zeigt an, dass ein Element ausgeführt werden soll. Im Falle der Sequenz bestimmt die Reihenfolge der "run"-Anweisungen die Reihenfolge, in der die Elemente aufgerufen werden. Im Falle des Coroutines-Plugins werden alle Elemente gleichzeitig aufgerufen.

*Anwendbar auf*

Sequenz

*Format*

	run [Elementname] [optional: Bedingung] [optional: deaktiviert]

*Parameter*

|`Elementname`			|der Name des auszuführenden Elements	|
|`Bedingung` (optional)	|die bedingte Anweisung, die bestimmt, ob das Element tatsächlich aufgerufen wird. Wenn keine Bedingung angegeben ist, wird das Element immer aufgerufen.|

*Beispiel*

	run correct_feedback '[correct] = 1'

## *set* Anweisung

Definiert Einzeilige Variablen.

*Anwendbar auf*

Alle Elemente

*Format*

	set [Variablenname] [Wert]

*Parameter*

|`Variablenname`	|der Variablenname	|
|`Wert`			|der Variablenwert	|

*Beispiel*

	set timeout 1000

*Anmerkungen*

Mehrzeilige Variablen werden mit der `__[Variablenname]__`-Notation definiert. Dies ist hauptsächlich für Elemente nützlich, die große Textblöcke erfordern. Innerhalb einer Elementdefinition wird jeder Zeile ein einzelner Tabulator vorangestellt, der nicht als Teil des Textes interpretiert werden sollte. `__end__` zeigt das Ende der Variable an.

*Zum Beispiel:*

	__meine_variable__
	Dies ist die erste Zeile.
	Dies ist die zweite Zeile.
	__end__

## *setcycle* Anweisung

Ähnlich wie bei der regulären "set"-Anweisung, setzt jedoch eine Variable nur während eines bestimmten Zyklus einer Schleife. Dies entspricht dem Skriptäquivalent der Loop-Tabelle.

*Anwendbar auf*

Schleife

*Format*

	setcycle [Zyklus #] [Variablenname] [Variablenwert]

*Parameter*

|`Zyklus #`			|die Nummer des Zyklus, wobei 0 der erste ist	|
|`Variablenname` 	|der Variablenname								|
|`Wert`				|der Variablenwert								|

*Beispiel*

	setcycle 0 cue valid

## *widget* Anweisung

Fügt einem Formular ein Widget (Schaltflächen, Beschriftungen usw.) hinzu. Gültige Schlüsselwörter hängen vom Typ des Widgets ab. Die Widget-Anweisung gehört nicht strikt zum Kern der OpenSesame-Syntax, wird aber vom form_base-Plugin verwendet.

*Anwendbar auf*

form_base (Plugin)

*Format*

	widget [Spalte] [Zeile] [Spaltenbreite] [Zeilenhöhe] [Widget-Typ] [Schlüsselwörter]

*Parameter*

|`Spalte`		|die Spaltenposition des Widgets im Formular, wobei 0 am weitesten links ist							|
|`Zeile`		|die Zeilenposition des Widgets im Formular, wobei 0 oben ist										|
|`Spaltenbreite`	|die Anzahl der Spalten, die das Widget einnimmt												|
|`Zeilenhöhe`		|die Anzahl der Zeilen, die das Widget einnimmt												|
|`Widget-Typ`	|'button', 'checkbox', 'image', 'image_button', 'label', 'rating_scale' oder 'text_input'		|

*Schlüsselwörter*

TODO

*Beispiel*

	widget 0 0 1 1 label text='Dies ist eine Beschriftung'