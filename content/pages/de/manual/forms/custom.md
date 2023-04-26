title: Erstellen benutzerdefinierter Formulare
hash: a87d6a87fa567e6e8d52bfd533cc60fb77b7e646afa3b49d05009bbe198d852f
locale: de
language: German

[TOC]

## Über Formulare, Geometrien und Widgets

Ein Formular ist eine Gruppe von Widgets (Schaltflächen, Beschriftungen, Texteingabefeldern usw.), die in einem Rastersystem mit einer bestimmten Geometrie angeordnet sind. Im Bild unten sehen Sie ein Beispiel für ein 2 (Spalten) × 3 (Zeilen) Formular. Eine Formgeometrie ist einfach und besteht aus den folgenden Eigenschaften:

- *Ränder* stellen sicher, dass die Widgets nicht den Rand des Bildschirms berühren. Sie können unterschiedliche Ränder für oben, rechts, unten und links haben.
- *Abstände* stellen sicher, dass die Widgets nicht aneinander anstoßen. Der horizontale und vertikale Abstand ist gleich.
- Es gibt eine oder mehrere *Zeilen*, möglicherweise unterschiedlicher Größe.
- Es gibt eine oder mehrere *Spalten*, möglicherweise unterschiedlicher Größe.

%--
figure:
 id: FigGeometry
 source: geometry.png
 caption: Ein Schema von FORM-Geometrien.
--%

Natürlich ist ein leeres Formular langweilig. Fügen wir also die folgenden Widgets hinzu, um ein einfaches Frageformular zu erstellen:

- Ein `label`, das die beiden Spalten der oberen Zeile überspannt. Wir verwenden dieses Label, um dem Formular einen Titel zu geben.
- Eine weiteres `label`, das die beiden Spalten der mittleren Zeile überspannt. Dieses enthält die eigentliche Frage.
- Eine `button` im unteren rechten Widget-Bereich. Mit dieser Schaltfläche kann der Benutzer die $0,05-Antwort geben.
- Eine weitere `button` im unteren linken Widget-Bereich. Mit dieser Schaltfläche kann der Benutzer die $0,10-Antwort geben.

%--
figure:
 id: FigSchematicExample1
 source: schematic-example1.png
 caption: Ein schematisches Beispiel FORM.
--%

Die obigen Bilder sind schematische Beispiele. Wie dieses Formular in OpenSesame tatsächlich aussieht, hängt von Ihren Einstellungen ab (insbesondere Ihrer Schriftart und Farben), aber es könnte so aussehen:

%--
figure:
 id: FigExample1
 source: example1.png
 caption: Ein Beispiel FORM.
--%

## Benutzerdefinierte Formulare erstellen

Es gibt zwei Möglichkeiten, benutzerdefinierte Formulare zu erstellen. Sie können:

- Das FORM_BASE-Element verwenden und Ihr Formular mit OpenSesame-Skript angeben.
- Python in einem INLINE_SCRIPT-Element verwenden. Der Python-Weg ist etwas flexibler, aber für die meisten Zwecke können beide Wege verwendet werden.

### Formulare mit OpenSesame-Skript erstellen

Wir erstellen das oben beschriebene Formular mit OpenSesame-Skript. Ziehen Sie dazu das FORM_BASE-Plugin in Ihr Experiment. Klicken Sie auf das neu erstellte Element, um die Registerkarte zu öffnen. Klicken Sie anschließend auf die Schaltfläche 'Skript bearbeiten' (mit dem Terminalsymbol) in der oberen rechten Ecke des Registerkartenbereichs. Dadurch wird der Skripteditor geöffnet. Geben Sie das folgende Skript ein, um das oben beschriebene Formular zu generieren (siehe Kommentare für Erklärungen).

~~~
# Ränder sind definiert als "oben;rechts;unten;links". Jeder Wert entspricht einem
# Rand in Pixeln.
set margins "50;100;50;100"
# Der Abstand wird einfach als Wert in Pixeln angegeben.
set spacing "25"
# Die Größen der Zeilen sind relativ. "1;2;1" bedeutet, dass es drei Zeilen gibt,
# wobei die mittlere doppelt so groß ist wie die untere und die obere. "1;2;1"
# bedeutet also genau das Gleiche wie "3;6;3". Bitte beachten Sie, dass "3" nicht bedeutet,
# dass es drei gleich große Zeilen gibt (aber "1;1;1" tut dies).
set rows "1;2;1"
# Spalten sind auf die gleiche Weise definiert. "1;1" bedeutet einfach, dass es
# zwei gleich große Spalten gibt.
set cols "1;1"
# Widgets sind wie folgt definiert:
# widget [spalte] [zeile] [spaltenspanne] [zeilenspanne] [widget-typ] [schlüsselwörter]
#
# Die Spalten und Zeilen beginnen bei 0 zu zählen. Wenn Sie nicht möchten, dass Ihr Widget
# mehrere Spalten und Zeilen überspannt, setzen Sie einfach die Spalten- und Zeilenspanne auf 1.
widget 0 0 2 1 label text="Frage"
widget 0 1 2 1 label center="no" text="Ein Schläger und ein Baseball kosten zusammen $1,10. Der Schläger kostet einen Dollar mehr als der Ball. Wie viel kostet der Ball?"
widget 0 2 1 1 button text="$0,10"
widget 1 2 1 1 button text="$0,05"
~~~

### Formulare erstellen mit Python Inline-Skript

Das exakt gleiche Formular kann mit einem INLINE_SCRIPT und etwas Python-Code erstellt werden. Ihnen wird auffallen, dass der Python-Code dem oben gezeigten OpenSesame-Skript etwas ähnelt. Das ist kein Wunder: Das FORM_BASE-Plugin übersetzt das OpenSesame-Skript im Wesentlichen in Python-Code.

Zuerst ziehe ein INLINE_SCRIPT in dein Experiment. Wähle das neu erstellte Element, um seinen Tab zu öffnen, und füge das folgende Skript in die Laufphase des INLINE_SCRIPT Elements ein (siehe Kommentare für Erklärungen).

~~~ .python
# Erstelle ein Formular
form = Form(
    cols=[1,1], rows=[1,2,1],
    margins=(50,100,50,100), spacing=25
)
# Erstelle vier Widgets
labelTitle = Label(text='Frage')
labelQuestion = Label(
    text='Ein Schläger und ein Baseball kosten zusammen 1,10 $. Der Schläger kostet einen Dollar mehr als der Ball. Wie viel kostet der Ball?',
    center=False
)
button5cts = Button(text='0,05 $')
button10cts = Button(text='0,10 $')
# Füge die Widgets zum Formular hinzu. Die Position im Formular wird als
# (Spalte, Zeile) Tupel angezeigt.
form.set_widget(labelTitle, (0,0), colspan=2)
form.set_widget(labelQuestion, (0,1), colspan=2)
form.set_widget(button5cts, (0,2))
form.set_widget(button10cts, (1,2))
# Führe das Formular aus! In diesem Fall gibt das Formular den Text der Schaltfläche zurück, die
# angeklickt wurde. Dies ist eine Möglichkeit, einen Rückgabewert aus dem Formular zu erhalten. Eine weitere Möglichkeit
# ist die Verwendung des 'var'-Schlüsselworts, das einige der Widgets unterstützt.
button_clicked = form._exec()
~~~

Wenn du möchtest, dass ein bestimmtes Widget den Fokus erhält, wenn das Formular ausgeführt wird, verwende das `focus_widget` Schlüsselwort:

~~~ .python
button_clicked = form._exec(focus_widget=button5cts)
~~~

### Nicht-interaktive Formulare

Normalerweise hat ein Formular ein Eingabefeld, eine Schaltfläche oder ein anderes interaktives Element. Du kannst jedoch auch Formulare ohne interaktive Elemente verwenden. Um dies im OpenSesame-Skript zu tun, setze `only_render` auf "yes":

```python
set only_render yes
```

Um dies in einem Python INLINE_SCRIPT zu tun, rufe `form.render()` auf, anstelle von `form._exec()`.

### Themes

Formulare unterstützen das Themeing. Derzeit sind zwei Themes verfügbar: 'gray' und 'plain'. Das 'gray' Theme ist das Standard-Theme. Obwohl das 'gray' Theme bereits recht schlicht ist, ist das 'plain' Theme noch einfacher. Du kannst in OpenSesame script ein Theme so auswählen:

```python
set theme plain
```

Und durch Verwendung des `theme` Schlüsselworts im Python-inline-Skript:

~~~ .python
form = Form(theme='plain')
~~~

### Verfügbare Widgets und Schlüsselwörter

Eine Liste der verfügbaren Widgets und Schlüsselwörter findest du unter:

- %link:manual/forms/widgets%

### Eingabe validieren

Um zu sehen, wie du die Eingabe eines Formulars validieren kannst, siehe:

- %link:manual/forms/validation%

## Ein weiteres Beispiel

Das folgende OpenSesame-Skript (in einem FORM_BASE-Plugin) erzeugt einen Fragebogen mit drei Bewertungsskalen und einer Weiter-Schaltfläche:

```python
set rows "1;1;1;1;1"
set cols "1;1"
widget 0 0 2 1 label text="Geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen"
widget 0 1 1 1 label center="no" text="Formulare sind einfach"
widget 1 1 1 1 rating_scale var="question1" nodes="Stimme zu;Weiß nicht;Stimme nicht zu"
widget 0 2 1 1 label center="no" text="Ich mag Daten"
widget 1 2 1 1 rating_scale var="question2" nodes="Stimme zu;Weiß nicht;Stimme nicht zu"
widget 0 3 1 1 label center="no" text="Ich mag Fragebögen"
widget 1 3 1 1 rating_scale var="question3" nodes="Stimme zu;Weiß nicht;Stimme nicht zu"
widget 0 4 2 1 button text="Weiter"
```

Das folgende Python-inline-Skript erzeugt den gleichen Fragebogen.

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