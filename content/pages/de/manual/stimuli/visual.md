title: Visuelle Reize
hash: 4ead1768298a015dc8af358675db670a71ea61876c2803a8998223c3509860c5
locale: de
language: German

Der häufigste Weg, visuelle Reize zu präsentieren, ist die Verwendung des SKETCHPAD-Elements oder, für nicht zeitkritische Reize, des FEEDBACK-Elements.

[TOC]

## Verwendung der Sketchpad- und Feedback-Elemente

Die SKETCHPAD- und FEEDBACK-Elemente bieten grundlegende Zeichenwerkzeuge, die das zeigen, was Sie sehen (%FigSketchpad).

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: Das SKETCHPAD bietet integrierte Zeichenwerkzeuge.
--%

## Der Unterschied zwischen Sketchpad- und Feedback-Elementen

Die SKETCHPAD- und FEEDBACK-Elemente sind in den meisten Bereichen identisch, abgesehen von zwei wichtigen Unterschieden.

### Sketchpad-Elemente werden im Voraus vorbereitet, Feedback-Elemente nicht

Der Inhalt eines SKETCHPAD wird während der Vorbereitungsphase der SEQUENCE, zu der es gehört, vorbereitet. Dies ist notwendig, um eine genaue Zeitnahme zu gewährleisten: Es ermöglicht, dass das SKETCHPAD während der Laufphase sofort angezeigt wird, ohne Verzögerungen aufgrund der Reizvorbereitung. Der Nachteil dabei ist jedoch, dass der Inhalt des SKETCHPAD nicht von dem abhängen kann, was während der SEQUENCE, zu der es gehört, geschieht. Zum Beispiel können Sie kein SKETCHPAD verwenden, um sofortiges Feedback zur Reaktionszeit zu geben, die von einem KEYBOARD_RESPONSE-Element erfasst wird (vorausgesetzt, das SKETCHPAD und KEYBOARD_RESPONSE sind Teil derselben Sequenz.)

Im Gegensatz dazu werden die Inhalte eines FEEDBACK-Elements erst vorbereitet, wenn sie tatsächlich angezeigt werden, also während der Laufphase der SEQUENCE, zu der sie gehören. Dies ermöglicht es, Feedback zu Dingen zu geben, die gerade passiert sind - daher der Name. Das FEEDBACK-Element sollte jedoch nicht verwendet werden, um zeitkritische Reize zu präsentieren, da es unter Verzögerungen aufgrund der Reizvorbereitung leidet.

Für weitere Informationen zur Prepare-Run-Strategie siehe:

- %link:prepare-run%

### Feedback-Variablen werden (standardmäßig) von Feedback-Elementen zurückgesetzt

Das FEEDBACK-Element hat eine Option "Feedback-Variablen zurücksetzen". Wenn diese Option aktiviert ist (standardmäßig ist dies der Fall), werden die Feedback-Variablen zurückgesetzt, wenn das FEEDBACK-Element angezeigt wird.

Für weitere Informationen über Feedback-Variablen, siehe:

- %link:manual/variables%

## Visuelle Reize in Python Inline-Script präsentieren

### Zugriff auf ein SKETCHPAD in Python

Das `Canvas`-Objekt für ein SKETCHPAD kann als Eigenschaft `canvas` des Elements abgerufen werden. Angenommen, Ihr SKETCHPAD heißt *my_sketchpad* und enthält ein Bildelement mit dem Namen "my_image". Sie könnten dann das Bild mit dem folgenden Skript drehen lassen:

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~

### Erstellung eines Canvas in Python

Das `Canvas`-Objekt kann zur Präsentation visueller Reize in Python verwendet werden:

- %link:manual/python/canvas%