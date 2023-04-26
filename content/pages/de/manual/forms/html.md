title: Benutzerdefinierte HTML-Formulare
hash: 7ce4d5848c0a4e0e32e903dbfb423bd42fbcf30dea52cc43cde013192eeab9dd
locale: de
language: German

Das INLINE_HTML-Element ermöglicht es Ihnen, Formulare mit benutzerdefiniertem HTML zu erstellen.

- Das `name`-Attribut von `input`-Tags entspricht einer experimentellen Variable. Daher wird der in das Texteingabefeld von Beispiel 1 eingegebene Text als experimentelle Variable `text_response` gespeichert.
- Für `checkbox`- und `radio`-Elemente können Sie das `id`-Attribut verwenden, um einem bestimmten Wert die zugehörige experimentelle Variable zuzuweisen.
- Sie können das `required`-Attribut verwenden, um anzuzeigen, dass ein Formular nicht abgeschickt werden kann, bevor ein Feld ausgefüllt wurde.
- Das Formular wird geschlossen, wenn der Teilnehmer auf eine Eingabe des Typs submit klickt.
- Um Bilder aus dem Datei-Pool in ein benutzerdefiniertes HTML-Formular einzufügen, rufen Sie zunächst die URL zur Datei ab, weisen Sie sie einer experimentellen Variable zu und verwenden Sie dann diese Variable als Quelle für das `<img>`-Tag (siehe Beispiel 3).

Beispiel 1:

Ein sehr einfaches Texteingabeformular:

```html
<input type='text' name='text_response'>
<input type='submit' value='hier klicken zum Weitermachen'>
```

Beispiel 2:

Ein Formular mit mehreren Radiobuttons:

```html
<p>Bitte wählen Sie Ihr Alter:</p>
<input type="radio" id="age1" name="age" value="30" required>
<label for="age1">0 - 30</label><br>
<input type="radio" id="age2" name="age" value="60">
<label for="age2">31 - 60</label><br>  
<input type="radio" id="age3" name="age" value="100">
<label for="age3">61 - 100</label><br><br>
<input type="submit" value="Absenden">
```

Beispiel 3:

Sie können Variablenreferenzen verwenden (außer innerhalb von `<script>`-Tags, in denen geschweifte Klammern einfach als Teil des JavaScript-Codes interpretiert werden):

```html
<p>Ihre Altersgruppe ist {age}</p>
<input type='submit' value='ok'>
```

Beispiel 4:

Sie können JavaScript über `<script>`-Tags verwenden. Zum Beispiel können Sie ein Bild aus dem Datei-Pool erhalten und es einem anfangs leeren `<img>`-Tag wie folgt zuweisen:

```html
<img id='capybara'>
<input type='submit' value='ok'>

<script>
document.getElementById('capybara').src = pool['capybara.png'].data.src
</script>
```