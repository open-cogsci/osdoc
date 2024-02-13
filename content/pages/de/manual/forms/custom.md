title: Erstellen benutzerdefinierter Formulare
hash: a7ba48cceefdfccdc42df16e4cfeb5980dcbd13a9a5b8516a328456704b5b400
locale: de
language: German

## Über Formulare, Geometrien und Widgets

Ein Formular besteht aus einer Reihe von Widgets (Knöpfen, Beschriftungen, Texteingabefeldern usw.), die in einem Raster mit einer bestimmten Geometrie angeordnet sind. Im Bild unten sehen Sie ein Beispiel für ein Formular mit 2 (Spalten) × 3 (Zeilen). Eine Formulargeometrie ist einfach und umfasst die folgenden Eigenschaften:

- *Randabstände* stellen sicher, dass die Widgets nicht die Kante des Displays berühren. Sie können unterschiedliche Randabstände für oben, rechts, unten und links haben.
- *Abstände* stellen sicher, dass die Widgets sich nicht gegenseitig berühren. Der horizontale und vertikale Abstand ist gleich.
- Es gibt eine oder mehrere *Zeilen*, möglicherweise unterschiedlicher Größe.
- Es gibt eine oder mehrere *Spalten*, möglicherweise unterschiedlicher Größe.

%--
Abbildung:
 id: FigGeometry
 source: geometry.png
 caption: Ein Schema der FORM-Geometrien.
--%

Natürlich macht ein leeres Formular keinen Spaß. Also fügen wir die folgenden Widgets hinzu, um ein einfaches Frageformular zu erstellen:

- Ein `label`, das sich über die beiden Spalten der oberen Reihe erstreckt. Wir verwenden dieses Label, um dem Formular einen Titel zu geben.
- Ein weiteres `label`, das sich über die beiden Spalten der mittleren Reihe erstreckt. Dieses Label enthält die eigentliche Frage.
- Ein `button` im unteren rechten Widget-Bereich. Dieser Knopf ermöglicht es dem Benutzer, die Antwort $0,05 zu geben.
- Ein weiterer `button` im unteren linken Widget-Bereich. Dieser Knopf ermöglicht es dem Benutzer, die Antwort $0,10 zu geben.

%--
Abbildung:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: Ein schematisches Beispiel für ein FORM.
--%

Die obigen Bilder sind schematische Beispiele. Wie dieses Formular tatsächlich in OpenSesame aussieht, hängt von Ihren Einstellungen ab (insbesondere von Ihrer Schriftart und Ihren Farben), aber es könnte so aussehen:

%--
Abbildung:
 id: FigExample1
 source: example1.png
 caption: Ein Beispiel für ein FORM.
--%

## Erstellen von benutzerdefinierten Formularen

Es gibt zwei Wege, um benutzerdefinierte Formulare zu erstellen. Sie können:

- Das FORM_BASE-Element verwenden und Ihr Formular mit OpenSesame-Script spezifizieren.
- Python in einem INLINE_SCRIPT-Element verwenden. Der Python-Weg ist etwas flexibler, aber für die meisten Zwecke können beide Wege verwendet werden.

### Formulare mit OpenSesame-Script erstellen

Wir werden das oben beschriebene Formular mit OpenSesame-Script erstellen. Ziehen Sie zuerst das FORM_BASE-Plugin in Ihr Experiment. Klicken Sie auf das neu erstellte Element, um dessen Tab zu öffnen. Klicken Sie dann auf den Button 'Skript bearbeiten' (mit dem Terminalsymbol), oben rechts im Tab-Bereich. Dadurch wird der Skripteditor geöffnet. Geben Sie das folgende Skript ein, um das oben beschriebene Formular zu erzeugen (siehe Kommentare zur Erklärung).

~~~
# Die Randabstände sind als "oben;rechts;unten;links" definiert. Jeder Wert entspricht
# einem Randabstand in Pixeln.
set margins "50;100;50;100"
# Der Abstand ist einfach ein Wert in Pixeln.
set spacing "25"
# Die Größen der Zeilen sind relativ. "1;2;1" bedeutet, dass es drei Zeilen gibt,
# wobei die mittlere doppelt so groß ist wie die untere und die obere. Also bedeutet
# "1;2;1" genau das Gleiche wie "3;6;3". Bitte beachten Sie, dass "3" nicht bedeutet,
# dass es drei gleich große Zeilen gibt (aber "1;1;1" tut das).
set rows "1;2;1"
# Spalten werden auf die gleiche Weise definiert. "1;1" bedeutet einfach, dass es
# zwei gleich große Spalten gibt.
set cols "1;1"
# Widgets werden wie folgt definiert:
# widget [spalte] [zeile] [spaltenbreite] [zeilenhöhe] [widget-typ] [schlüsselwörter]
#
# Die Spalten und Zeilen werden bei 0 beginnend gezählt. Wenn Sie nicht möchten, dass Ihr Widget
# mehrere Spalten und Zeilen umfasst, setzen Sie einfach die Spaltenbreite und Zeilenhöhe auf 1.
widget 0 0 2 1 label text="Frage"
widget 0 1 2 1 label center="no" text="Eine Fledermaus und ein Baseball kosten zusammen $1,10. Der Schläger kostet einen Dollar mehr als der Ball. Wie viel kostet der Ball?"
widget 0 2 1 1 button text="$0,10"
widget 1 2 1 1 button text="$0,05"
~~~

Wenn Sie möchten, dass ein bestimmtes Widget den Fokus erhält, wenn das Formular ausgeführt wird, können Sie das Schlüsselwort `focus=yes` auf eines der Widgets anwenden:

```
widget 0 0 1 1 text_input text="Initialer Text" frame=yes center=no stub="Hier tippen …" return_accepts=yes var=response focus=yes
```

### Formulare mit Python Inline-Skript erstellen

Das exakt gleiche Formular kann mit einem INLINE_SCRIPT und etwas Python-Code erstellt werden. Sie werden bemerken, dass der Python-Code dem oben gezeigten OpenSesame-Skript etwas ähnelt. Das ist kein Wunder: Das FORM_BASE-Plugin übersetzt das OpenSesame-Skript im Wesentlichen in Python-Code.

Zuerst ziehen Sie ein INLINE_SCRIPT in Ihr Experiment. Wählen Sie den neu erstellten Eintrag aus, um seinen Tab zu öffnen, und fügen Sie das folgende Skript in die Run-Phase des INLINE_SCRIPT-Eintrags ein (siehe die Kommentare für Erklärungen).

~~~ .python
# Ein Formular erstellen
form = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# Vier Widgets erstellen
labelTitle = Label(text='Frage')
labelQuestion = Label(
    text='Eine Fledermaus und ein Baseball kosten zusammen $1,10. Der Schläger kostet einen Dollar mehr als der Ball. Wie viel kostet der Ball?',
    center=False
)
button5cts = Button(text='$0,05')
button10cts = Button(text='$0,10')
# Die Widgets zum Formular hinzufügen. Die Position im Formular wird als
# (Spalte, Reihe)-Tupel angegeben.
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))
# Das Formular ausführen! In diesem Fall wird das Formular den Text des Buttons zurückgeben,
# der geklickt wurde. Dies ist eine Möglichkeit, einen Rückgabewert aus dem Formular zu erhalten.
# Eine andere Möglichkeit ist die Verwendung des 'var'-Schlüsselworts, das von einigen Widgets unterstützt wird.
button_clicked = form._exec()
~~~

Wenn Sie möchten, dass ein bestimmtes Widget den Fokus erhält, wenn das Formular ausgeführt wird, können Sie das Schlüsselwort `focus_widget` verwenden:

~~~ .python
button_clicked = form._exec(focus_widget=button5cts)
~~~

### Nicht-interaktive Formulare

Normalerweise hat ein Formular ein Eingabefeld, einen Button oder ein anderes interaktives Element. Sie können jedoch auch Formulare nutzen, ohne irgendwelche interaktiven Elemente zu haben. Um dies in einem OpenSesame-Skript zu tun, setzen Sie `only_render` auf "yes":

```python
set only_render yes
```

Um dies in einem Python INLINE_SCRIPT zu tun, rufen Sie `form.render()` auf, anstelle von `form._exec()`.

### Themes

Formulare unterstützen Themes. Derzeit sind zwei Themes verfügbar: 'gray' und 'plain'. Das 'gray' Theme ist das Standard-Theme. Obwohl das 'gray' Theme bereits ziemlich schlicht ist, ist das 'plain' Theme noch grundlegender. Sie können ein Theme auf diese Weise in OpenSesame-Skript wählen:

```python
set theme plain
```

Und indem Sie das Schlüsselwort `theme` im Python Inline-Skript verwenden:

~~~ .python
form = Form(theme='plain')
~~~

### Verfügbare Widgets und Schlüsselwörter

Für eine Liste verfügbarer Widgets und Schlüsselwörter siehe:

- %link:manual/forms/widgets%

### Eingabevalidierung

Um zu sehen, wie Sie die Eingabe in einem Formular validieren können, siehe:

- %link:manual/forms/validation%

## Ein weiteres Beispiel

Das folgende OpenSesame-Skript (in einem FORM_BASE-Plugin) wird einen Fragebogen mit drei Bewertungsskalen plus einem Weiter-Button erzeugen:

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="Geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen"
widget 0 1 1 1 label center="no" text="Formulare sind einfach"
widget 1 1 1 1 rating_scale var="question1" nodes="Zustimmen;Weiß nicht;Ablehnen"
widget 0 2 1 1 label center="no" text="Ich mag Daten"
widget 1 2 1 1 rating_scale var="question2" nodes="Zustimmen;Weiß nicht;Ablehnen"
widget 0 3 1 1 label center="no" text="Ich mag Fragebögen"
widget 1 3 1 1 rating_scale var="question3" nodes="Zustimmen;Weiß nicht;Ablehnen"
widget 0 4 2 1 button text="Weiter"
```

Das folgende Python INLINE_SCRIPT wird denselben Fragebogen erzeugen.

``` .python
form = Form(cols=[1,1], rows=[1,1,1,1,1])
title = Label(
    text='Geben Sie an, inwieweit Sie der folgenden Aussage zustimmen'
)
question1 = Label(text='Formulare sind einfach', center=False)
question2 = Label(text='Ich mag Daten', center=False)
question3 = Label(text='Ich mag Fragebögen', center=False)
ratingScale1 = RatingScale(
    var='question1',
    nodes=['Zustimmen', u"Weiß nicht", 'Ablehnen']
)
ratingScale2 = RatingScale(
    var='question2',
    nodes=['Zustimmen', u"Weiß nicht", 'Ablehnen']
)
ratingScale3 = RatingScale(var='question3',
    nodes=['Zustimmen', u"Weiß nicht", 'Ablehnen'])
nextButton = Button(text='Weiter')
form.set_widget(title, (0, 0), colspan=2)
form.set_widget(question1, (0, 1))
form.set_widget(question2, (0, 2))
form.set_widget(question3, (0, 3))
form.set_widget(ratingScale1, (1, 1))
form.set_widget(ratingScale2, (1, 2))
form.set_widget(ratingScale3, (1, 3))
form.set_widget(nextButton, (0, 4), colspan=2)
form._exec()
```

Das resultierende Formular sieht in etwa so aus. (Das genaue Erscheinungsbild hängt von Ihrer Schriftart, Farben usw. ab.)

%--
Abbildung:
 ID: FigExample2
 Quelle: example2.png
 Bildunterschrift: Ein weiteres Beispiel FORMULAR.
--%