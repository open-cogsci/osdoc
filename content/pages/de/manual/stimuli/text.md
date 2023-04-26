title: Text
hash: 1958b3f404645f67ec8c328c22b9b876e1507c616fa82878164f23ac0d364e92
locale: de
language: German

[TOC]

## Wie kann ich Text anzeigen?

Die gebräuchlichste Methode, um Text darzustellen, besteht darin, ein SKETCHPAD- oder FEEDBACK-Element zu verwenden. Diese ermöglichen es Ihnen, Text und andere visuelle Reize einzugeben. Um Text in einer fragebogenähnlichen Weise anzuzeigen, können Sie [Forms](%link:manual/forms/about%) verwenden.


## HTML-Formatierung

Sie können HTML-Tags verwenden, die Sie einfach in Ihren Text einfügen können. Sie können diese Tags überall verwenden: In SKETCHPAD-Elementen, in INLINE_SCRIPTs (vorausgesetzt, Sie verwenden die `Canvas`-Klasse), in Formularen usw.

Beispiel:

~~~ .html
OpenSesame unterstützt eine Teilmenge von HTML-Tags:
- <b>Fett</b>
- <i>Kursiv</i>
- <u>Unterstrichen</u>

Außerdem können Sie 'color', 'size' und 'style' als Schlüsselwörter an ein 'span'-Tag übergeben:
- <span style='color:red;'>Farbe</span>
- <span style='font-size:32px;'>Schriftgröße</span>
- <span style='font-family:serif;'>Schriftstil</span>

Schließlich können Sie mit dem 'br'-Tag Zeilenumbrüche erzwingen:
Zeile 1<br>Zeile 2
~~~


## Variablen und inline Python

Sie können Variablen in Text einbetten, indem Sie die `{...}` Syntax verwenden. Zum Beispiel ergibt Folgendes:

~~~ .python
Die Versuchspersonennummer ist {subject_nr}
~~~

.. könnte auswerten zu (für Versuchsperson 1):

~~~ .python
Die Versuchspersonennummer ist 1
~~~

Sie können auch Python-Ausdrücke einbetten. Zum Beispiel ergibt Folgendes:

~~~ .python
Der Versuchspersonennummer modulo fünf ist {subject_nr % 5}
~~~

.. könnte auswerten zu (für Versuchsperson 7):

~~~ .python
Der Versuchspersonennummer modulo fünf ist 2
~~~


## Schriftarten

### Standard-Schriftarten

Sie können eine der Standardschriftarten aus den Schriftartenauswahldialogen (%FigFontSelect) auswählen. Diese Schriftarten sind in OpenSesame enthalten und daher ist Ihr Experiment vollständig portabel, wenn Sie diese Schriftarten verwenden.

%--
Abbildung:
 ID: FigFontSelect
 Quelle: font-selection-dialog.png
 Beschriftung: "Eine Reihe von Standardschriftarten, die mit OpenSesame gebündelt sind, können über die Schriftartenauswahldialoge ausgewählt werden."
--%

Die Schriftarten wurden zur Klarstellung umbenannt, entsprechen aber den folgenden Open-Source-Schriftarten:

|__Name in OpenSesame__		|__Tatsächliche Schriftart__|
|---------------------------|---------------------------|
|`sans`					    |Droid Sans				    |
|`serif`				    |Droid Serif			    |
|`mono`					    |Droid Sans Mono		    |
|`chinese-japanese-korean`	|WenQuanYi Micro Hei	    |
|`arabic`				    |Droid Arabic Naskh		    |
|`hebrew`				    |Droid Sans Hebrew		    |
|`hindi`				    |Lohit Hindi			    |

### Auswahl einer benutzerdefinierten Schriftart über den Schriftartenauswahldialog

Wenn Sie in der Schriftartenauswahl "andere ..." auswählen, können Sie jede Schriftart auswählen, die auf Ihrem Betriebssystem verfügbar ist. Wenn Sie dies tun, ist Ihr Experiment nicht mehr vollständig portabel und erfordert, dass die ausgewählte Schriftart auf dem System installiert ist, auf dem Sie Ihr Experiment ausführen.

### Platzieren einer benutzerdefinierten Schriftart im Datei-Pool

Eine andere Möglichkeit, eine benutzerdefinierte Schriftart zu verwenden, besteht darin, eine Schriftartendatei in den Datei-Pool zu legen. Wenn Sie beispielsweise die Schriftartendatei `inconsolata.ttf` in den Datei-Pool stellen, können Sie diese Schriftart in einem SKETCHPAD-Element verwenden, wie folgt:

	draw textline 0.0 0.0 "Das wird inconsolata sein" font_family="inconsolata"

Beachten Sie, dass die Schriftartendatei eine Truetype-`.ttf`-Datei sein muss.