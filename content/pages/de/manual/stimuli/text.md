title: Text
hash: 2c5f78c24fe19088d9f96d120232def3d4ca9bb4bc48409ae868d353c7ebc4ed
locale: de
language: German

## Wie kann ich Text präsentieren?

Die gebräuchlichste Methode, Text anzuzeigen, ist die Verwendung eines SKETCHPAD oder eines FEEDBACK-Elements. Diese ermöglichen es Ihnen, Text und andere visuelle Reize einzugeben. Für eine fragebogenähnliche Darstellung von Text können Sie [Formulare](%link:manual/forms/about%) verwenden.

## HTML-Formatierung

Sie können HTML-Tags verwenden, die Sie einfach in Ihren Text einfügen können. Sie können diese Tags überall verwenden: In SKETCHPAD-Elementen, in INLINE_SCRIPTs (vorausgesetzt, Sie verwenden die `Canvas`-Klasse), in Formularen usw.

Beispiel:

~~~ .html
OpenSesame unterstützt eine Untergruppe von HTML-Tags:
- <b>Fettgedruckt</b>
- <i>Kursiv</i>
- <u>Unterstrichen</u>

Zusätzlich können Sie 'color', 'size' und 'style' als Schlüsselwörter zu einem 'span'-Tag hinzufügen:
- <span style='color:red;'>Farbe</span>
- <span style='font-size:32px;'>Schriftgröße</span>
- <span style='font-family:serif;'>Schriftart</span>

Schließlich können Sie Zeilenumbrüche mit dem 'br'-Tag erzwingen:
Zeile 1<br>Zeile 2
~~~

## Variablen und inline Python

Sie können Variablen im Text einbetten, indem Sie die `{...}`-Syntax verwenden. Zum Beispiel könnte folgendes:

~~~ .python
Die Probandennummer ist {subject_nr}
~~~

... ausgewertet werden als (für Probanden 1):

~~~ .python
Die Probandennummer ist 1
~~~

Sie können auch Python-Ausdrücke einbetten. Zum Beispiel könnte folgendes:

~~~ .python
Die Probandennummer modulo fünf ist {subject_nr % 5}
~~~

... ausgewertet werden als (für Proband 7):

~~~ .python
Die Probandennummer modulo fünf ist 2
~~~

## Schriftarten

### Standard-Schriftarten

Sie können eine der Standard-Schriftarten aus den Schriftart-Auswahldialogen (%FigFontSelect) wählen. Diese Schriftarten sind in OpenSesame enthalten, und Ihr Experiment ist daher vollständig portabel, wenn Sie sie verwenden.

%--
Abbildung:
 id: FigFontSelect
 Quelle: font-selection-dialog.png
 Beschriftung: "Eine Auswahl von Standard-Schriftarten, die mit OpenSesame gebündelt sind, kann über die Schriftart-Auswahldialoge ausgewählt werden."
--%

Die Schriftarten wurden zur besseren Verständlichkeit umbenannt, entsprechen aber den folgenden Open-Source-Schriftarten:

|__Name in OpenSesame__		|__Tatsächliche Schriftart__	|
|---------------------------|-------------------------------|
|`sans`						|Droid Sans					|
|`serif`					|Droid Serif					|
|`mono`						|Droid Sans Mono			|
|`chinesisch-japanisch-koreanisch`	|WenQuanYi Micro Hei	|
|`arabisch`					|Droid Arabic Naskh			|
|`hebräisch`				|Droid Sans Hebrew			|
|`hindi`					|Lohit Hindi				|

### Auswahl einer benutzerdefinierten Schriftart über den Schriftart-Auswahldialog

Wenn Sie 'andere ...' im Schriftart-Auswahldialog wählen, können Sie jede Schriftart auswählen, die auf Ihrem Betriebssystem verfügbar ist. Wenn Sie dies tun, ist Ihr Experiment nicht länger voll portabel und erfordert, dass die ausgewählte Schriftart auf dem System installiert ist, auf dem Ihr Experiment ausgeführt wird.

Dies funktioniert nur für OpenSesame auf dem Desktop, nicht für Online-OSWeb-Experimente.

### Platzieren einer benutzerdefinierten Schriftart im Dateipool (OpenSesame Desktop)

Wenn Sie Ihr Experiment auf dem Desktop ausführen, ist eine weitere Möglichkeit, eine benutzerdefinierte Schriftart zu verwenden, eine Schriftartdatei im Dateipool abzulegen. Wenn Sie zum Beispiel die Schriftartdatei `inconsolata.ttf` im Dateipool platzieren, können Sie diese Schriftart in einem SKETCHPAD-Element verwenden, wie folgt:

	draw textline 0.0 0.0 "This will be inconsolata" font_family="inconsolata"

Die Schriftartdatei muss eine Truetype-`.ttf`-Datei sein. Dies funktioniert nur für OpenSesame auf dem Desktop, nicht für Online-OSWeb-Experimente.

### Verwendung einer benutzerdefinierten Schriftart von Google Fonts (OSWeb)

Wenn Sie Ihr Experiment in einem Browser mit OSWeb ausführen, können Sie Schriftarten von Google Fonts verwenden. Dazu bearbeiten Sie einfach das Skript eines Textelements und geben den Namen der Schriftart unter `font_family` an:

```
draw textline x=0 y=0 font_family="Jacquard 12 Charted" text="This is shown in a funny font"
```

Dies funktioniert nur für Online-OSWeb-Experimente, nicht für OpenSesame auf dem Desktop.