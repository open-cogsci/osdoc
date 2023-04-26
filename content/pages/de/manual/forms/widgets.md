title: Formular-Widgets und Schlüsselwörter
hash: a4f02ea6550b00af4807cff9e990f6b79be4e00837de3d2ed8f8c3d34f77a19e
locale: de
language: German


[TOC]


## Screenshot

%--
figure:
 id: FigWidgets
 source: widgets.png
 caption: Eine Liste der verfügbaren FORM Widgets.
--%


## Widgets und Schlüsselwörter

Alle Schlüsselwörter sind optional, außer anders angegeben.

### Formular

Die Schlüsselwörter `cols` und `rows` können entweder einzelne `int` Werte sein, in diesem Fall geben sie die Anzahl der gleichgroßen Spalten und Zeilen an, oder Listen von `int`, in diesem Fall geben sie die relativen Größen jeder Spalte und Zeile an. Weitere Informationen zur Formgeometrie finden Sie unter:

- %link:manual/forms/custom%

Das Schlüsselwort `validator` kann verwendet werden, um die Eingabe im Formular zu validieren. Weitere Informationen finden Sie unter:

- %link:manual/forms/validation%

(In OpenSesame Skript muss ein Formular nicht explizit erstellt werden.)

Python-Skript:

~~~ .python
form = Form(
    cols=2, rows=2, spacing=10, margins=(100, 100, 100, 100), theme='gray',
    timeout=None, clicks=False, validator=None
)
button = Button(text='Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### button / Button

OpenSesame Skript:

~~~python
widget 0 0 1 1 button text="Klick mich!" center=yes frame=yes var=response
~~~

Python-Skript:

~~~ .python
form = Form()
button = Button(text='Klick mich!', frame=True, center=True, var='response')
form.set_widget(button, (0, 0))
form._exec()
~~~


### checkbox / Checkbox

Wenn eine Gruppe angegeben ist, wird das Ankreuzen einer Checkbox aus dieser Gruppe alle anderen Checkboxen aus dieser Gruppe deaktivieren. Checkboxen, die Teil einer Gruppe sind, können nicht deaktiviert werden, es sei denn, indem man auf eine andere Checkbox in der Gruppe klickt.

Das Schlüsselwort `group` hat auch Auswirkungen darauf, wie Variablen gespeichert werden, wie hier beschrieben:

- %link:manual/forms/variables%

OpenSesame Skript:

~~~python
widget 0 0 1 1 checkbox group=group text="Option 1"
widget 0 1 1 1 checkbox group=group text="Option 2"
~~~

Python-Skript:

~~~ .python
form = Form()
checkbox1 = Checkbox(text='Option 1', group='group')
checkbox2 = Checkbox(text='Option 2', group='group')
form.set_widget(checkbox1, (0, 0))
form.set_widget(checkbox2, (0, 1))
form._exec()
~~~


### image / ImageWidget

Das Python-Objekt heißt `ImageWidget`, um es vom `Image` Canvas-Element zu unterscheiden.

OpenSesame Skript:

~~~python
# Nur path ist ein erforderliches Schlüsselwort
widget 0 0 1 1 image path="my_image.png" adjust=yes frame=no
~~~

Python-Skript:

~~~ .python
# Nur path ist ein erforderliches Schlüsselwort
form = Form()
image = ImageWidget(path=pool['my_image.png'], adjust=True, frame=False)
form.set_widget(image, (0, 0))
form._exec()
~~~


### image_button / ImageButton

Das Schlüsselwort `image_id` wird verwendet, um das Bild-Button beim Klicken zu identifizieren. Wenn keine `image_id` angegeben ist, wird der Pfad zum Bild als ID verwendet.

OpenSesame Skript:

~~~python
# Nur path ist ein erforderliches Schlüsselwort
widget 0 0 1 1 image_button path="my_image.png" adjust=yes frame=no image_id=my_image var=response
~~~

Python-Skript:

~~~ .python
# Nur path ist ein erforderliches Schlüsselwort
form = Form()
image_button = ImageButton(
    path=pool['my_image.png'], adjust=True, frame=False,
    image_id='my_image', var='response'
)
form.set_widget(image_button, (0, 0))
form._exec()
~~~


### label / Label

OpenSesame Skript:

~~~python
widget 0 0 1 1 label text="Mein Text" frame=no center=yes
~~~

Python-Skript:

~~~ .python
form = Form()
label = Label(text='Mein Text', frame=False, center=True)
form.set_widget(label, (0,0))
form._exec()
~~~


### rating_scale / RatingScale

Das Schlüsselwort `nodes` kann ein `int` oder eine durch Semikolon getrennte Liste von Bezeichnungen sein. Wenn `nodes` ein `int` ist, gibt es die Anzahl der (nicht beschrifteten) Knoten an.

Das Schlüsselwort `default` zeigt an, welche Knotennummer standardmäßig ausgewählt ist, wobei der erste Knoten 0 ist.

OpenSesame Skript:

~~~python
widget 0 1 1 1 rating_scale var=response nodes="Zustimmen;Weiß nicht;Ablehnen" click_accepts=no orientation=horizontal var=response default=0
~~~

Python-Skript:

~~~ .python
form = Form()
rating_scale = RatingScale(
    nodes=['Zustimmen', u"Weiß nicht", 'Ablehnen'], click_accepts=False,
    orientation='horizontal', var='antwort', default=0
)
form.set_widget(rating_scale, (0, 0))
form._exec()
~~~


### text_input / TextInput

Das `stub` Stichwort gibt den Platzhaltertext an, der angezeigt wird, wenn noch kein Text eingegeben wurde. Das `key_filter` Stichwort, das nur in Python verfügbar ist, gibt eine Funktion an, um Tastenanschläge zu filtern. Dies wird unter folgendem Link ausführlicher beschrieben:

- %link:manual/forms/validation%

OpenSesame Skript:

~~~python
widget 0 0 1 1 text_input text="Anfangstext" frame=yes center=no stub="Hier tippen …" return_accepts=yes var=antwort
~~~

Python Skript:

~~~ .python
form = Form()
text_input = TextInput(
    text='Anfangstext', frame=True, center=False, stub='Hier tippen …',
    return_accepts=True, var='antwort', key_filter=my_filter_function
)
form.set_widget(text_input, (0, 0))
form._exec()
~~~