title: Formularvariablen
hash: 5699e805a79ad2de0de21343a912e41c96c96935e89844f6af55864fcb4864cc
locale: de
language: German

[TOC]

## Über Formularvariablen

Wenn Sie ein Formular mit mehreren `checkbox`-Elementen präsentieren, möchten Sie in der Regel wissen, welche `checkbox` der Benutzer angekreuzt hat. Ebenso möchten Sie bei einem Formular mit zwei `button`-Elementen wissen, auf welchen `button` der Benutzer geklickt hat. Diese Informationen stehen durch Variablen zur Verfügung, die automatisch gesetzt werden, wenn der Benutzer mit einem Formular interagiert. Sie können selbst angeben, welche Antwortvariablen verwendet werden sollen. Wie das gemacht wird, hängt davon ab, wie Sie Ihr Formular erstellt haben.

### In vorgefertigten Formular-Plugins

Wenn Sie eines der vorgefertigten Formular-Plugins verwenden, wie zum Beispiel FORM_TEXT_INPUT, können Sie den Namen der Antwortvariable direkt in den Plugin-Controls angeben.

### In benutzerdefinierten Formularen

Mit dem Schlüsselwort `var` können Sie angeben, welche Variable verwendet werden soll. Das folgende OpenSesame-Skript, das Sie in ein FORM_BASE-Plugin eingeben können, gibt an, dass die Antwort von einem `text_input`-Widget in einer Variable namens `my_response_var` gespeichert werden soll:

```python
widget 0 0 1 1 text_input var=my_response_var
```

Der äquivalente Python-Code lautet:

~~~ .python
my_widget = TextInput(var='my_response_var)
~~~

Siehe auch:

- %link:manual/forms/widgets%

## Widget-spezifische Informationen

Jedes Widget verwendet seine Antwortvariable auf eine etwas unterschiedliche Weise.

### button

Das `button`-Widget setzt die Antwortvariable auf 'ja', wenn darauf geklickt wurde, und auf 'nein', wenn nicht.

### checkbox

Das `checkbox`-Widget setzt die Antwortvariable auf eine Semikolon-getrennte Liste des Textes aller angekreuzten Checkboxen (für diese Variable) oder auf 'nein', wenn keine `checkbox` angekreuzt wurde (für diese Variable). Das klingt ein wenig kompliziert, deshalb hier ein paar Beispiele.

```python
widget 0 0 1 1 checkbox group="1" text="A" var="my_response_var"
widget 1 0 1 1 checkbox group="1" text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
```

Hier gibt es zwei `checkbox`-Elemente mit dem Text 'A' und 'B'. Beide gehören zur selben Gruppe, genannt '1'. Beide haben dieselbe Antwortvariable, genannt `my_response_var`. Wenn 'A' angekreuzt ist, wird `my_response_var` 'A' sein. Wenn 'B' angekreuzt ist, wird `my_response_var` 'B' sein. Wenn keines angekreuzt ist, wird `my_response_var` 'nein' sein. Beachten Sie, dass in dieser Gruppe nur eine `checkbox` angekreuzt sein kann, sodass `my_response_var` in diesem Beispiel *niemals* 'A;B' ist.

Betrachten Sie nun dasselbe Skript, wobei der einzige Unterschied darin besteht, dass die beiden `checkbox`-Elemente nicht zu einer Gruppe gehören:

```python
widget 0 0 1 1 checkbox text="A" var="my_response_var"
widget 1 0 1 1 checkbox text="B" var="my_response_var"
widget 1 1 1 1 button text="Next"
```

In diesem Fall ist die Situation ähnlich wie oben beschrieben, mit der Ausnahme, dass beide `checkbox`-Elemente gleichzeitig angekreuzt sein können, und in diesem Fall wird `my_response_var` auf 'A;B' gesetzt.

Sie können dieselbe Antwortvariable nicht für `checkbox`-Elemente in verschiedenen Gruppen verwenden.

### image

Variablen sind für das `image`-Widget nicht anwendbar.

### image_button

Das `image_button`-Widget setzt die Antwortvariable auf 'ja', wenn darauf geklickt wurde, und auf 'nein', wenn nicht.

### label

Variablen sind für das `label`-Widget nicht anwendbar.

### rating_scale

Das `rating_scale`-Widget setzt die Antwortvariable auf die Nummer der Option, auf die geklickt wurde, wobei '0' die erste Option ist (nullbasierte Indexierung). Wenn keine Option ausgewählt wurde, wird die Antwortvariable auf 'None' gesetzt.

### text_input

Das `text_input`-Widget setzt die Antwortvariable auf den eingegebenen Text.