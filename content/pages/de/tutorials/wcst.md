title: Wisconsin-Karten-Sortier-Test
hash: c76af36f9cc3e81cddcf0d468272405a3bebc0c73931400b287f211d586c3db3
locale: de
language: German

[TOC]

## Die grundlegenden Schritte

%--
figur:
 id: FigWCST
 quelle: wcst.png
 bildunterschrift: |
  Der Wisconsin Card Sorting Test (WCST) ist ein neuropsychologischer Test der exekutiven Funktionen.
--%


In diesem Tutorial erstellen Sie den Wisconsin Card Sorting Test (WCST) und erfahren, wie Sie diesen Test online mit OSWeb durchführen können.

Im WCST sehen Teilnehmer vier Stimuluskarten, die sich in drei Dimensionen unterscheiden: Farbe (rot, grün, blau, gelb), Form (Kreis, Stern, Dreieck, Kreuz) und Anzahl der Formen (eins, zwei, drei oder vier). Die Teilnehmer sehen auch eine einzelne Antwortkarte, die ebenfalls eine Farbe, Form und Anzahl hat.

Die Aufgabe des Teilnehmers besteht darin, die Antwortkarte der richtigen Stimuluskarte nach einer bestimmten Dimension (z. B. Farbe) oder *Übereinstimmungsregel* zuzuordnen. Der Teilnehmer weiß zunächst nicht, nach welcher Dimension er suchen soll, und seine Aufgabe besteht darin, die Übereinstimmungsregel durch Versuch und Irrtum herauszufinden.

Um die Sache schwieriger zu machen, ändert sich die Übereinstimmungsregel nach jeweils fünf richtigen Antworten. Daher muss der Teilnehmer seine Übereinstimmungsregel flexibel aktualisieren.

### Schritt 1: Laden Sie OpenSesame herunter und starten Sie es

OpenSesame ist für Windows, Linux und Mac OS verfügbar. Dieses Tutorial ist für OpenSesame 4.0 oder höher geschrieben.

Wenn Sie OpenSesame starten, erhalten Sie eine Auswahl an Vorlagen für Experimente und (falls vorhanden) eine Liste zuletzt geöffneter Experimente (siehe %FigStartUp).

%--
figur:
 id: FigStartUp
 quelle: start-up.png
 bildunterschrift: |
  Das OpenSesame-Fenster beim Start.
--%


Die *Erweiterte Vorlage* bietet einen guten Ausgangspunkt für die Erstellung vieler Experimente, die eine Block-Test-Struktur verwenden. In diesem Tutorial erstellen wir das gesamte Experiment jedoch von Grund auf neu, und wir verwenden die 'default template', die bereits geladen wird, wenn OpenSesame gestartet wird (%FigDefaultTemplate). Schließen Sie einfach die Registerkarten "Los geht's!" und (falls angezeigt) "Willkommen!".

%--
figur:
 id: FigDefaultTemplate
 quelle: default-template.png
 bildunterschrift: |
  Die Struktur des 'Default Template' im Übersichtsbereich.
--%


### Schritt 2: Einen block_loop und trial_sequence hinzufügen

Das Standardtemplate beginnt mit drei Elementen: Ein NOTEPAD namens *getting_started*, ein SKETCHPAD namens *welcome* und eine SEQUENCE namens *experiment*. Wir benötigen *getting_started* und *welcome* nicht, also entfernen wir diese gleich. Um dies zu tun, klicken Sie mit der rechten Maustaste auf diese Elemente und wählen Sie "Löschen". Entfernen Sie *experiment* nicht, da es der Einstiegspunkt für das Experiment ist (d. h. das erste Element, das beim Start des Experimentes aufgerufen wird).

Unser Experiment wird eine sehr einfache Struktur haben. Oben in der Hierarchie befindet sich eine LOOP, die wir *block_loop* nennen werden. Im *block_loop* definieren wir unsere unabhängigen Variablen. Um eine LOOP zu Ihrem Experiment hinzuzufügen, ziehen Sie das LOOP-Symbol aus der Element-Symbolleiste auf das *experiment* Element im Übersichtsbereich.

Ein LOOP-element benötigt ein weiteres Element zum Ausführen; normalerweise und auch in diesem Fall handelt es sich um eine SEQUENCE. Ziehen Sie das SEQUENCE-Element aus der Element-Symbolleiste auf das *new_loop*-Element im Übersichtsbereich. OpenSesame fragt dann, ob Sie die SEQUENCE in oder nach der LOOP einfügen möchten. Wählen Sie "In new_loop einfügen".

Standardmäßig haben Elemente Namen wie *new_sequence*, *new_loop*, *new_sequence_2* usw. Diese Namen sind nicht sehr informativ und es ist ratsam, sie umzubenennen. Elementnamen dürfen nur aus alphanumerischen Zeichen und / oder Unterstrichen bestehen. Um ein Element umzubenennen, doppelklicken Sie auf das Element im Übersichtsbereich. Benennen Sie *new_sequence* in *trial_sequence* um, um anzuzeigen, dass es einer einzelnen Testsequenz entsprechen wird. Benennen Sie *new_loop* in *block_loop* um, um anzuzeigen, dass es einem Block von Testsequenzen entsprechen wird.

Klicken Sie abschließend auf "Neues Experiment", um die Registerkarte "Allgemeine Eigenschaften" zu öffnen. Klicken Sie auf den Titel des Experiments und benennen Sie es in "Wisconsin Card Sorting Test" um.

Der Übersichtsbereich unseres Experiments sieht nun wie in %FigBasicStructure aus.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  Der Überblicksbereich am Ende von Schritt 2.
--%


### Schritt 3: Bilder und Sounddateien importieren

Für dieses Experiment verwenden wir Bilder für die Spielkarten. Sie können diese von hier herunterladen:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Laden Sie `stimuli.zip` herunter und extrahieren Sie es irgendwohin (zum Beispiel auf Ihren Desktop). Klicken Sie anschließend in OpenSesame auf die Schaltfläche "Datei-Pool anzeigen" in der Haupt-Toolbar (oder: Menü → Ansicht → Datei-Pool anzeigen). Standardmäßig wird der Datei-Pool auf der rechten Seite des Fensters angezeigt. Die einfachste Methode, um die Reize in den Datei-Pool hinzuzufügen, besteht darin, sie vom Desktop (oder von dem Ort, an dem sie extrahiert wurden) in den Datei-Pool zu ziehen. Alternativ können Sie auch auf die Schaltfläche "+" im Datei-Pool klicken und Dateien über den Dateiauswahldialog hinzufügen, der daraufhin erscheint. Der Datei-Pool wird automatisch mit Ihrem Experiment gespeichert.

Nachdem Sie alle Reize hinzugefügt haben, sieht Ihr Datei-Pool aus wie in %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Der Datei-Pool mit den Reizen.
--%


### Schritt 4: Eine statische Kartendarstellung erstellen

Zunächst erstellen wir eine Anzeige mit vier Reizkarten und einer Antwortkarte. Welche Karten jedoch angezeigt werden, hängt zunächst nicht von Variablen ab, dh wir erstellen eine *statische* Anzeige.

Ziehen Sie ein SKETCHPAD in *trial_sequence* und benennen Sie es in *card_display* um. Verwenden Sie das Bildwerkzeug, um vier Karten in einer horizontalen Reihe irgendwo oben auf der Anzeige zu zeichnen; dies werden die Reizkarten sein. Zeichnen Sie eine einzelne Karte in der Nähe des unteren Teils der Anzeige; dies wird die Antwortkarte sein. Fügen Sie auch Text hinzu, um dem Teilnehmer anzuzeigen, was er oder sie tun soll, nämlich `a`, `b`, `c` oder `d` drücken, um anzuzeigen, welche der Reizkarten mit der Antwortkarte übereinstimmt. Der genaue Text, das Layout und die Karten liegen bei Ihnen! Tipps: Mit der Option *scale* können Sie die Größe der Karten anpassen; Sie können die Hintergrundfarbe im Tab Allgemeine Eigenschaften ändern, den Sie öffnen können, indem Sie auf das oberste Element des Experiments klicken.

Bei mir sieht das Ergebnis so aus:

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Ein SKETCHPAD mit statisch definierten Karten.
--%


### Schritt 5: Machen Sie die Antwortkarte variabel

Im Moment zeigen wir immer dieselbe Antwortkarte (im obigen Beispiel ein einzelnes blaues Dreieck). Natürlich möchten wir jedoch auf jeder Testversion eine andere Antwortkarte zeigen. Um dies zu tun, müssen wir zuerst die Variablen definieren, die bestimmen, welche Antwortkarte wir anzeigen werden. Wir werden dies im *block_loop* tun.

Öffnen Sie den *block_loop*. Die LOOP-Tabelle ist jetzt leer. Um die Farbe, Form und Anzahl der Antwortkarte zu bestimmen, könnten wir manuell drei Spalten (`response_color`, `response_shape` und `response_number`) und 64 Zeilen für alle möglichen Kombinationen von Farben, Formen und Zahlen erstellen. Das wäre jedoch viel Arbeit. Stattdessen verwenden wir den Vollfaktoriellen-Design-Assistenten, den Sie öffnen können, indem Sie auf die Schaltfläche "Vollfaktorielles Design" klicken. (Ein vollfaktorielles Design ist ein Design, bei dem alle möglichen Kombinationen der Variablenniveaus auftreten.) In diesem Assistenten erstellen Sie für jede der drei Variablen eine Spalte und geben in den darunter liegenden Zellen die möglichen Werte für diese Variable ein (siehe %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  Mit dem Vollfaktorielles-Design-Assistenten können Sie problemlos große LOOP-Tabellen generieren, die vollfaktoriellen Designs entsprechen.
--%


Klicken Sie anschließend auf die Schaltfläche OK. Der *block_loop* enthält nun alle 64 Kombinationen von Farben, Zahlen und Formen (siehe %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  Der *block_loop* am Ende von Schritt 5.
--%

Kehren Sie jetzt zum *card_display* zurück. Jedes Element in OpenSesame wird durch ein Skript definiert. Dieses Skript wird automatisch durch die Benutzeroberfläche generiert. Manchmal kann es praktisch (oder sogar notwendig) sein, dieses Skript direkt zu bearbeiten. Der häufigste Grund für die Bearbeitung des Skripts eines Elements besteht darin, Variablen zum Skript hinzuzufügen, was wir auch jetzt tun werden!

Um das Skript anzuzeigen, klicken Sie auf die Schaltfläche "Anzeigen" und wählen Sie "Skript anzeigen". (Die Schaltfläche "Anzeigen" befindet sich in der Mitte der Elementsteuerungen oben rechts.) Dies öffnet einen Skripteditor.

Das Skript für *card_display* besteht hauptsächlich aus `draw`-Befehlen, die jede der fünf Karten und auch die verschiedenen Textelemente definieren. Suchen Sie die Zeile, die der Antwortkarte entspricht. Sie können diese finden, indem Sie sich die Y-Koordinate ansehen, die positiv sein sollte (d. h. im unteren Teil der Anzeige) oder durch Betrachten des Namens der Bilddatei.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

In meinem Beispiel ist die Bilddatei für die Antwortkarte derzeit immer `"1-blue-triangle.png"`. Aber natürlich wollen wir nicht immer ein einziges blaues Dreieck zeigen. Stattdessen möchten wir, dass die Bilddatei von den Variablen abhängt, die wir im *block_loop* definiert haben. Um dies zu tun, ersetzen Sie die Zahl durch `{response_number}`, die Farbe durch `{response_color}` und die Form durch `{response_shape}`: (Die geschwungenen Klammern geben an, dass diese sich auf Variablennamen beziehen.)

```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Klicken Sie auf Übernehmen, um die Änderungen am Skript zu akzeptieren. Die Antwortkarte wurde nun durch ein Fragezeichen-Symbol ersetzt. Das liegt daran, dass OpenSesame nicht weiß, wie man eine Vorschau eines Bildes anzeigen kann, das mit Variablen definiert wurde. Aber keine Sorge: Das Bild wird angezeigt, wenn Sie das Experiment ausführen!

### Schritt 6: Machen Sie die Stimulus-Karten variabel

Die Stimulus-Karten sollten mehr oder weniger zufällig ausgewählt werden, aber jede Farbe, Form und Nummer sollte nur einmal vorkommen; das heißt, es sollte niemals zwei rote Karten oder zwei Karten mit Dreiecken geben. (Wenn es welche gäbe, würde das Matching-Verfahren mehrdeutig sein.) Um dies zu erreichen, können wir *horizontales Mischen* verwenden, eine leistungsstarke, aber ungewöhnliche Funktion des LOOP-Elements.

- %link:loop%

Öffnen Sie zunächst den *block_loop* und erstellen Sie 12(!) neue Spalten, um die Stimulus-Karten zu definieren: `color1`, für die Farbe der ersten Karte, `color2`,`color3`,`color4`, und `shape1` ... `shape4`, und `number1` ... `number4`. Jede Spalte hat denselben Wert in jeder Zeile (siehe %FigLoopTable2).

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  Der *block_loop* während Schritt 6.
--%

Aber noch sind wir nicht fertig! Derzeit ist die erste Stimulus-Karte immer ein einzelner roter Kreis, die zweite zwei blaue Dreiecke usw. Um das zu randomisieren, sagen wir OpenSesame, die Werte der vier Farbvariablen, der vier Formvariablen und der vier Anzahlvariablen zufällig zu tauschen (horizontal zu mischen). Öffnen Sie dazu das Skript für den *block_loop*. Fügen Sie in der vorletzten Zeile (direkt vor `run trial_sequence`) die folgenden Befehle hinzu:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Klicken Sie auf Übernehmen, um das Skript zu akzeptieren. Um zu sehen, ob dies funktioniert hat, klicken Sie auf die Schaltfläche "Vorschau". Dadurch wird eine Vorschau angezeigt, wie die LOOP-Tabelle während des Experiments randomisiert wird. Sieht das gut aus?

Kehren Sie jetzt zum *card_display* zurück und lassen Sie das Bild der ersten Stimulus-Karte von der Variablen `color1`, `shape1` und `number1` abhängen, und analog dazu für die anderen Stimulus-Karten. (Wenn Sie nicht sicher sind, wie das geht, überprüfen Sie Schritt 5.)

### Schritt 7: Bestimmen Sie die korrekte Antwort (für eine Übereinstimmungsregel)

Fürs Erste gehen wir davon aus, dass die Teilnehmer immer nach Form abgleichen. (Eine der Zusatzaufgaben besteht darin, dies zu verbessern.)

Momentan ist die Dauer von *card_display* auf 'keypress' eingestellt. Das bedeutet, dass das *card_display* angezeigt wird, bis eine Taste gedrückt wird, aber es bietet keine Kontrolle darüber, wie dieser Tastendruck behandelt wird. Ändere daher die Dauer auf 0 und füge direkt nach *card_display* eine KEYBOARD_RESPONSE ein. Benenne die KEYBOARD_RESPONSE in *press_a* um und gib an, dass die korrekte Antwort 'a' und die erlaubten Antworten 'a; b; c; d' sind.

%--
figur:
 id: FigPressA
 quelle: press-a.png
 untertitel: |
  Eines der KEYBOARD_RESPONSE-Elemente, die in Schritt 7 definiert sind.
--%

Aber das ist noch nicht genug! Momentan gibt es ein einzelnes Antwortelement, das davon ausgeht, dass die korrekte Antwort immer 'a' ist. Wir haben noch nicht angegeben, *wann* die richtige Antwort 'a' ist, noch haben wir Versuche in Betracht gezogen, bei denen die richtige Antwort 'b', 'c' oder 'd' ist.

Um dies zu erreichen, erstelle zuerst drei weitere KEYBOARD_RESPONSE-Elemente: *press_b*, *press_c* und *press_d*. Diese sind alle gleich, außer der korrekten Antwort, die für jedes von ihnen separat definiert ist und jeweils 'b', 'c' und 'd' sein sollte.

Schließlich verwende in der *trial_sequence* Run If-Anweisungen, um zu entscheiden, unter welcher Bedingung jedes der vier KEYBOARD_RESPONSE-Elemente ausgeführt werden soll (wodurch entschieden wird, was die korrekte Antwort ist). Für *press_a* ist die Bedingung, dass `shape1` gleich `response_shape` sein sollte. Warum? Nun, weil das bedeutet, dass die Form der ersten Stimulus-Karte gleich der Form der Antwortkarte ist, und in diesem Fall ist die richtige Antwort 'a'. Diese Bedingung entspricht der folgenden Run-If-Anweisung: `shape1 = response_shape`. Die Run-if-Anweisungen für die anderen KEYBOARD_RESPONSE-Elemente sind analog (siehe %FigTrialSequence1).

%--
figur:
 id: FigTrialSequence1
 quelle: trial-sequence-1.png
 untertitel: |
  Die *trial_sequence* am Ende von Schritt 7.
--%

### Schritt 8: Gib dem Teilnehmer Rückmeldung

OpenSesame verfolgt automatisch, ob eine Antwort korrekt war oder nicht, indem die Variable `correct` auf jeweils 1 oder 0 gesetzt wird. (Vorausgesetzt natürlich, dass Sie die korrekte Antwort angegeben haben, wie wir es in Schritt 7 getan haben.) Wir können dies nutzen, um dem Teilnehmer Feedback darüber zu geben, ob er korrekt geantwortet hat oder nicht.

Dazu füge zwei neue SKETCHPADs zur *trial_sequence* hinzu und nennt sie *correct_feedback* und *incorrect_feedback*. Gib dann an, welches der beiden mit einer Run-If-Anweisung ausgeführt werden soll (siehe %FigTrialSequence2).

%--
figur:
 id: FigTrialSequence2
 quelle: trial-sequence-2.png
 untertitel: |
  Die *trial_sequence* am Ende von Schritt 8.
--%

Füge beiden SKETCHPADs schließlich nützliche Inhalte hinzu. Zum Beispiel könntest du für *correct_feedback* einen grünen Fixationspunkt und für *incorrect_feedback* einen roten Fixationspunkt verwenden, in beiden Fällen für 500 ms angezeigt (d.h. die SKETCHPAD-Dauer auf 500 einstellen). Farbige Punkte sind eine schöne, unaufdringliche Möglichkeit, Feedback zu geben.

### Schritt 9: Teste das Experiment

Du hast jetzt eine grundlegende (aber unvollständige!) Implementierung des Wisconsin Card Sorting Test erstellt. (Du wirst die Implementierung als Teil der Extra-Aufgaben unten vervollständigen.)

Um das Experiment zu testen, klicke entweder auf die Schnellstart-Taste (die blauen Doppelpfeile) oder die Taste "Im Vollbildmodus ausführen" (der grüne Pfeil).

## Zusatzaufgaben

### Extra 1 (einfach): Füge einen Logger hinzu

OpenSesame protokolliert nicht automatisch Daten. Stattdessen musst du deinem Experiment explizit einen `logger` hinzufügen. In einem versuchsbasierten Experiment ist ein `logger` normalerweise das letzte Element der *trial_sequence*, sodass alle Daten, die während des Versuchs gesammelt wurden, gespeichert werden.

Momentan protokolliert unser WCST keine Daten. Zeit, das zu beheben!

### Extra 2 (einfach): Überprüfe die Datendatei

*Voraussetzung dafür ist, dass Sie Extra 1 abgeschlossen haben*.

Führe das Experiment kurz aus. Überprüfe nun die Protokolldatei in einem Programm wie Excel, LibreOffice Calc oder JASP. Identifiziere die relevanten Variablen und überlege, wie du die Ergebnisse analysieren könntest.

__Pro-Tipp:__ Setzen Sie den Wiederholungswert der *block_loop* auf 0,1, um die Anzahl der Versuche während des Tests zu reduzieren.

### Extra 3 (einfach): Anweisungen und Abschiedsbildschirm hinzufügen

Ein gutes Experiment kommt mit klaren Anweisungen. Und ein höfliches Experiment verabschiedet sich von den Teilnehmern, wenn sie fertig sind. Sie können dazu ein SKETCHPAD oder ein FORM_TEXT_DISPLAY verwenden.

### Extra 4 (mittel): Die richtige Antwort und Matching-Regel durch JavaScript festlegen

Um Skripterstellung in OSWeb einzubinden, können Sie den INLINE_JAVASCRIPT-Artikel verwenden, der JavaScript unterstützt. (Es bietet jedoch nicht derzeit alle Funktionen, die mit dem regulären Python INLINE_SCRIPT angeboten werden!). Siehe
[hier](https://osdoc.cogsci.nl/4.0/manual/javascript/about/) für Details.

Bisher ist die Anpassungsregel immer die Anpassung an die Form. Um dies zu ändern, fügen Sie dem Start des Experiments einen INLINE_JAVASCRIPT-Artikel hinzu und verwenden Sie das folgende Skript (in der *prepare*-Phase), um die Variable `matching_rule` zufällig auf "shape", "number" oder "color" zu setzen.

```javascript
function choice(choices) {
    // JavaScript hat keine eingebaute choice-Funktion, also definieren wir
    // es hier.
    // use let to introduce a temporary new variable
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}


// use var to introduce a global new variable
var matching_rule = choice(['shape', 'number', 'color'])
```

Fügen Sie nun einen weiteren INLINE_JAVASCRIPT-Artikel zum Start der *trial_sequence* hinzu. In der *prepare*-Phase fügen Sie ein Skript hinzu, um die Variable `correct_response` auf "a", "b", "c" oder "d" zu setzen. Dazu benötigen Sie eine Reihe von `if`-Anweisungen, die zunächst die Anpassungsregel betrachten und dann untersuchen, welche Form der Antwortform entspricht (für die Form-Anpassungsregel) oder welche Farbe der Antwortfarbe entspricht (für die Farb-Anpassungsregel) usw.

Um Ihnen den Einstieg zu erleichtern, finden Sie hier einen Teil der Lösung (aber es muss noch vervollständigt werden!):

```javascript
if (matching_rule === 'shape') {
    if (shape1 === response_shape) correct_response = 'a'
    // Not done yet
} // Not done yet

// Let's print some info to the debug window
console.log('matching_rule = ' + matching_rule)
console.log('correct_response = ' + correct_response)
```

### Extra 5 (schwierig): Änderung der Anpassungsregel in regelmäßigen Abständen

Bisher wird die Anpassungsregel zu Beginn des Experiments zufällig festgelegt, aber dann bleibt sie während des gesamten Experiments konstant. Bei einem echten WCST ändert sich die Anpassungsregel jedoch in regelmäßigen Abständen, normalerweise nachdem der Teilnehmer eine feste Anzahl korrekter Antworten gegeben hat.

Um dies zu implementieren, benötigen Sie einen weiteren INLINE_JAVASCRIPT. Hier sind einige Tipps zum Einstieg:

- Verwenden Sie eine Zählvariable, die nach einer korrekten Antwort um 1 erhöht wird und nach einer falschen Antwort auf 0 zurückgesetzt wird.
- Achten Sie beim Ändern der Anpassungsregel darauf, dass sie nicht zufällig wieder auf dieselbe Anpassungsregel gesetzt wird.

### Extra 6 (wirklich schwierig): Reaktionskarte einschränken

Im Moment kann die Antwortkarte auf mehreren Dimensionen mit einer Stimuluskarte übereinstimmen. Wenn zum Beispiel eine der Stimuluskarten ein einzelner blauer Kreis ist, könnte die Antwortkarte zwei blaue Kreise sein und sich damit sowohl in Farbe als auch in Form überschneiden. Bei einem echten WCST sollte die Antwortkarte jedoch in höchstens einer Dimension mit jeder Stimuluskarte übereinstimmen.

Diesmal liegt es an Ihnen. Keine Tipps!

### Extra 7 (einfach): Das Experiment online mit JATOS durchführen

Unser WCST ist mit OSWeb kompatibel, das bedeutet, dass Sie es in einem Browser ausführen können. Um zu testen, ob das noch funktioniert, können Sie das OSWeb Backend in der Registerkarte Allgemeine Eigenschaften des Experiment-Artikels auswählen. Sobald es ausgewählt ist, können Sie einfach auf die grüne Schaltfläche klicken und das Experiment wird in Ihrem Standardbrowser gestartet.

Um jedoch tatsächliche Daten für eine Ihrer Studien zu erfassen, möchten Sie das Experiment in JATOS importieren und JATOS verwenden, um einen Link zu generieren, den Sie an Ihre Teilnehmer verteilen können. Das ist viel einfacher als es klingt! Für weitere Informationen siehe:

- %link:manual/osweb/workflow%

Sie können das vollständige Experiment, einschließlich der Lösungen für die zusätzlichen Aufgaben, hier herunterladen:

- <https://osf.io/f5er2/>