title: Visuelle Reize
hash: 88ce873464207508e0ba22cecad7bdf4c51299ae1bf089ba96618c35389e13c2
locale: de
language: German

Die gebräuchlichste Art, visuelle Reize zu präsentieren, ist die Verwendung des SKETCHPAD-Elements oder, für nicht zeitkritische Reize, des FEEDBACK-Elements.

[TOC]


## Verwendung der sketchpad und feedback Elemente

Die SKETCHPAD- und FEEDBACK-Elemente bieten einfache "What-you-see-is-what-you-get"-Zeichenwerkzeuge (%FigSketchpad).

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: Das SKETCHPAD bietet integrierte Zeichenwerkzeuge.
--%


## Verwendung von show-if Ausdrücken

Sie können show-if Ausdrücke verwenden, um zu bestimmen, ob ein bestimmtes Element angezeigt werden soll oder nicht. Wenn Sie zum Beispiel ein Bild von einem glücklichen Gesicht haben, das nur angezeigt werden soll, wenn die Variable `valence` den Wert 'positive' hat, dann können Sie den show-if Ausdruck für das entsprechende Bildelement festlegen auf:

```python
valence == 'positive'
```

Wenn Sie einen show-if Ausdruck leer lassen oder `True` eingeben, wird das Element immer angezeigt. Show-if Ausdrücke verwenden die gleiche Syntax wie andere bedingte Ausdrücke. Für weitere Informationen siehe:

- %link:manual/variables%

Show-if Ausdrücke werden in dem Moment ausgewertet, in dem die Anzeige vorbereitet wird. Das bedeutet, dass sie für SKETCHPAD-Elemente während der Vorbereitungsphase ausgewertet werden, während sie für FEEDBACK-Elemente während der Ausführungsphase ausgewertet werden (siehe auch den Abschnitt unten).


## Der Unterschied zwischen sketchpad und feedback Elementen

Die SKETCHPAD- und FEEDBACK-Elemente sind in den meisten Punkten identisch, mit zwei wichtigen Unterschieden.


### Sketchpad Elemente werden im Voraus vorbereitet, feedback Elemente nicht

Der Inhalt eines SKETCHPAD wird während der Vorbereitungsphase der SEQUENCE vorbereitet, zu der es gehört. Dies ist notwendig, um eine genaue Timing zu gewährleisten: Es ermöglicht das sofortige Anzeigen des SKETCHPAD während der Ausführungsphase, ohne Verzögerungen durch die Stimulusvorbereitung. Der Nachteil dabei ist jedoch, dass der Inhalt eines SKETCHPAD nicht davon abhängen kann, was während der SEQUENCE passiert, zu der es gehört. Zum Beispiel können Sie keinen SKETCHPAD zur sofortigen Rückmeldung über die durch ein KEYBOARD_RESPONSE Element erfasste Reaktionszeit verwenden (angenommen, das SKETCHPAD und KEYBOARD_RESPONSE sind Teil derselben Sequence.)

Im Gegensatz dazu wird der Inhalt eines FEEDBACK-Elements nur vorbereitet, wenn es tatsächlich angezeigt wird, d.h., während der Ausführungsphase der SEQUENCE, zu der es gehört. Dies ermöglicht eine Rückmeldung über Dinge, die gerade passiert sind - daher der Name. Die FEEDBACK-Element sollte jedoch nicht verwendet werden, um zeitkritische Reize zu präsentieren, da sie Verzögerungen durch die Stimulusvorbereitung aufweist.

Für weitere Informationen zur prepare-run Strategie siehe:

- %link:prepare-run%


### Feedback Variablen werden (standardmäßig) durch feedback Elemente zurückgesetzt

Das FEEDBACK-Element hat eine Option 'Reset feedback variables'. Wenn diese Option aktiviert ist (standardmäßig ist sie aktiviert), werden feedback-Variablen zurückgesetzt, wenn das FEEDBACK-Element angezeigt wird.

Für weitere Informationen über feedback Variablen siehe:

- %link:manual/variables%


## Visuelle Reize in Python Inline-Skript präsentieren

### Zugriff auf ein SKETCHPAD in Python

Sie können auf das `Canvas`-Objekt für ein SKETCHPAD als die Eigenschaft `canvas` der Items zugreifen. Angenommen, Ihr SKETCHPAD heißt *my_sketchpad* und enthält Bildelemente mit dem Namen 'my_image'. Sie könnten dieses Bild dann mit dem folgenden Skript rotieren lassen:

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~


### Erstellung eines Canvas in Python

Sie können das `Canvas`-Objekt verwenden, um visuelle Reize in Python zu präsentieren:

- %link:manual/python/canvas%