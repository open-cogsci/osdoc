title: Wisconsin-Karten-Sortier-Test
uptodate: false
hash: de605121ce6b894d920b49eb8caa88e9c60f258f6f573d69ce0a995939cbaf10
locale: de
language: German


[TOC]


## Die grundlegenden Schritte


%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  Der Wisconsin Card Sorting Test (WCST) ist ein neuropsychologischer Test der exekutiven Funktionen.
--%


In diesem Tutorial implementieren Sie den Wisconsin Card Sorting Test (WCST) und erfahren, wie Sie diesen Test online mit OSWeb durchführen können.

Im WCST sehen die Teilnehmer vier Karten, die sich in drei Dimensionen unterscheiden: Farbe (rot, grün, blau, gelb), Form (Kreis, Stern, Dreieck, Kreuz) und Anzahl der Formen (eins, zwei, drei oder vier). Die Teilnehmer sehen auch eine einzelne Antwortkarte, die ebenfalls eine Farbe, Form und Anzahl hat.

Die Aufgabe des Teilnehmers besteht darin, die Antwortkarte der richtigen Karte zuzuordnen, und zwar auf der Grundlage einer bestimmten Dimension (z. B. Farbe) oder *Matching-Regel*. Der Teilnehmer weiß zunächst nicht, in welcher Dimension er abgleichen soll, und seine Aufgabe besteht darin, die Matching-Regel durch Versuch und Irrtum herauszufinden.

Um die Sache schwieriger zu machen, ändert sich die Matching-Regel nach jeweils fünf korrekten Antworten. Daher muss der Teilnehmer seine Matching-Regel flexibel anpassen.


### Schritt 1: Laden Sie OpenSesame herunter und starten Sie es

OpenSesame ist für Windows, Linux und Mac OS verfügbar. Dieses Tutorial ist für OpenSesame 3.2 oder höher geschrieben.

Wenn Sie OpenSesame starten, haben Sie die Auswahl zwischen Vorlagen-Experimenten und (falls vorhanden) einer Liste kürzlich geöffneter Experimente (siehe %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  Das OpenSesame-Fenster beim Start.
--%

Die *erweiterte Vorlage* bietet einen guten Ausgangspunkt für die Erstellung vieler Experimente, die eine Block-Trial-Struktur verwenden. In diesem Tutorial werden wir jedoch das gesamte Experiment von Grund auf erstellen, und wir werden die 'Standardvorlage' verwenden, die bereits geladen ist, wenn OpenSesame gestartet wird (%FigDefaultTemplate). Schließen Sie einfach die Registerkarten 'Los geht's!' und (falls angezeigt) 'Willkommen!'.

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  Die Struktur der 'Standardvorlage' im Übersichtsbereich.
--%


### Schritt 2: Fügen Sie eine block_loop und trial_sequence hinzu

Die Standardvorlage beginnt mit drei Elementen: Einem NOTIZBLOCK namens *getting_started*, einem ZEICHENFELD namens *welcome* und einer SEQUENZ namens *experiment*. Wir benötigen *getting_started* und *welcome* nicht, also entfernen wir diese gleich. Klicken Sie mit der rechten Maustaste auf diese Elemente und wählen Sie 'Löschen'. Entfernen Sie nicht *experiment*, weil es der Einstiegspunkt für das Experiment ist (d. h. das erste Element, das aufgerufen wird, wenn das Experiment gestartet wird).

Unser Experiment hat eine sehr einfache Struktur. Eine SCHLEIFE, die wir *block_loop* nennen, steht oben in der Hierarchie. An dieser Stelle werden wir unsere unabhängigen Variablen definieren. Um eine SCHLEIFE Ihrem Experiment hinzuzufügen, ziehen Sie das SCHLEIFENsymbol aus der Elementleiste auf das Element *experiment* im Übersichtsbereich.

Ein SCHLEIFEN-Element benötigt ein weiteres Element zum Ausführen; normalerweise handelt es sich dabei – und auch in diesem Fall – um eine SEQUENZ. Ziehen Sie das SEQUENZ-Element aus der Elementleiste auf das Element *new_loop* im Übersichtsbereich. OpenSesame fragt, ob Sie die SEQUENZ in die SCHLEIFE oder nach der SCHLEIFE einfügen möchten. Wählen Sie 'In new_loop einfügen'.

Elemente haben standardmäßig Namen wie *new_sequence*, *new_loop*, *new_sequence_2* usw. Diese Namen sind nicht sehr aussagekräftig, und es ist ratsam, sie umzubenennen. Elementnamen müssen aus alphanumerischen Zeichen und/oder Unterstrichen bestehen. Um den Namen eines Elements zu ändern, doppelklicken Sie auf das Element im Übersichtsbereich. Benennen Sie *new_sequence* in *trial_sequence* um, um darauf hinzuweisen, dass es einer einzigen Durchführung entspricht. Benennen Sie *new_loop* in *block_loop* um, um darauf hinzuweisen, dass es einem Block von Durchführungen entspricht.

Klicken Sie abschließend auf "New experiment", um die Registerkarte Allgemeine Eigenschaften zu öffnen. Klicken Sie auf den Titel des Experiments und benennen Sie ihn um in 'Wisconsin Card Sorting Test'.

Der Übersichtsbereich unseres Experiments sieht nun aus wie in %FigBasicStructure.

%--
Abbildung:
 ID: FigBasicStructure
 Quelle: basic-structure.png
 Beschriftung: |
  Der Übersichtsbereich am Ende von Schritt 2.
--%


### Schritt 3: Bilder und Audiodateien importieren

Für dieses Experiment werden wir Bilder für die Spielkarten verwenden. Sie können diese von hier herunterladen:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Laden Sie `stimuli.zip` herunter und extrahieren Sie es irgendwo (zum Beispiel auf Ihrem Desktop). Klicken Sie dann in OpenSesame auf die Schaltfläche "Datei-Pool anzeigen" in der Hauptwerkzeugleiste (oder: Menü →Ansicht → Datei-Pool anzeigen). Dies zeigt den Datei-Pool standardmäßig auf der rechten Seite des Fensters an. Der einfachste Weg, die Stimuli zum Datei-Pool hinzuzufügen, besteht darin, sie vom Desktop (oder von dem Ort, an dem Sie die Dateien extrahiert haben) in den Datei-Pool zu ziehen. Alternativ können Sie auf die Schaltfläche '+' im Datei-Pool klicken und Dateien über den Dateiauswahldialog, der erscheint, hinzufügen. Der Datei-Pool wird automatisch mit Ihrem Experiment gespeichert.

Nachdem Sie alle Stimuli hinzugefügt haben, sieht Ihr Datei-Pool wie in %FigFilePool aus.

%--
Abbildung:
 ID: FigFilePool
 Quelle: file-pool.png
 Beschriftung: |
  Der Datei-Pool, der die Stimuli enthält.
--%


### Schritt 4: Erstellen einer statischen Kartendarstellung

Zunächst erstellen wir eine Anzeige mit vier Stimulus-Karten und einer Antwortkarte. Welche Karten jedoch gezeigt werden, hängt für den Moment nicht von Variablen ab; Das heißt, wir erstellen eine *statische* Anzeige.

Ziehen Sie eine SKETCHPAD in *trial_sequence* und benennen Sie sie in *card_display* um. Verwenden Sie das Bildwerkzeug, um vier Karten in einer horizontalen Reihe irgendwo oben in der Anzeige zu zeichnen; Dies sind die Stimulus-Karten. Zeichnen Sie eine einzelne Karte in der Nähe des unteren Randes der Anzeige; Dies wird die Antwortkarte sein. Fügen Sie auch etwas Text hinzu, um dem Teilnehmer anzuzeigen, was er oder sie tun muss, nämlich `a`, `b`, `c` oder `d` drücken, um anzuzeigen, welche der Stimulus-Karten der Antwortkarte entspricht. Der genaue Text, das Layout und die Karten bleiben Ihnen überlassen! Tipps: Sie können die Option *Skalierung* verwenden, um die Größe der Karten anzupassen. Sie können die Hintergrundfarbe in der Registerkarte Allgemeine Eigenschaften ändern, die Sie öffnen können, indem Sie auf das oberste Element des Experiments klicken.

Bei mir sieht das Ergebnis so aus:


%--
Abbildung:
 ID: FigStaticCards
 Quelle: static-cards.png
 Beschriftung: |
  Eine SKETCHPAD mit statisch definierten Karten.
--%


### Schritt 5: Machen Sie die Antwortkarte variabel

Im Moment zeigen wir immer die gleiche Antwortkarte (im obigen Beispiel ein einzelnes blaues Dreieck). Aber natürlich möchten wir bei jedem Versuch eine andere Antwortkarte anzeigen. Um dies zu tun, müssen wir zunächst die Variablen festlegen, die bestimmen, welche Antwortkarte wir anzeigen werden. Wir werden dies in der *block_loop* tun.

Öffnen Sie die *block_loop*. Die LOOP-Tabelle ist jetzt leer. Um die Farbe, Form und Anzahl der Antwortkarten zu bestimmen, könnten wir manuell drei Spalten (`response_color`, `response_shape` und `response_number`) und 64 Zeilen für alle möglichen Kombinationen aus Farben, Formen und Zahlen erstellen. Aber das wäre viel Arbeit. Stattdessen verwenden wir den Vollfaktorielle-Design-Assistenten, den Sie öffnen können, indem Sie auf die Schaltfläche "Vollfaktorielle design" klicken. (Ein vollfaktorielles Design ist ein Design, bei dem alle möglichen Kombinationen der Variablenwerte auftreten.) In diesem Assistenten erstellen Sie eine Spalte für jede der drei Variablen und geben in den Zellen darunter die möglichen Werte für diese Variable ein (siehe %FigDesignWizard).

%--
Abbildung:
 ID: FigDesignWizard
 Quelle: design-wizard.png
 Beschriftung: |
  Mit dem Vollfaktorielle-Design-Assistenten können Sie leicht große LOOP-Tabellen erstellen, die vollfaktoriellen Designs entsprechen.
--%

Klicken Sie anschließend auf die Schaltfläche OK. Die *block_loop* enthält jetzt alle 64 Kombinationen aus Farben, Zahlen und Formen (siehe %FigLoopTable1).

%--
Abbildung:
 ID: FigLoopTable1
 Quelle: loop-table-1.png
 Beschriftung: |
  Die *block_loop* am Ende von Schritt 5.
--%

Nun kehre zum *card_display* zurück. Jeder Artikel in OpenSesame wird durch ein Skript definiert. Dieses Skript wird automatisch von der Benutzeroberfläche generiert. Manchmal kann es praktisch (oder sogar notwendig) sein, dieses Skript direkt zu bearbeiten. Der häufigste Grund für die Bearbeitung des Skripts eines Artikels besteht darin, Variablen zum Skript hinzuzufügen, was wir jetzt tun werden!

Um das Skript anzuzeigen, klicke auf die Schaltfläche 'Ansicht' und wähle 'Skript anzeigen'. (Die Schaltfläche Ansicht ist die mittlere Schaltfläche oben rechts in den Elementsteuerelementen.) Dies öffnet einen Skript-Editor.

Das Skript für *card_display* besteht hauptsächlich aus `draw`-Befehlen, die jeweils eine der fünf Karten und auch die verschiedenen Textelemente definieren. Suche die Zeile, die der Antwortkarte entspricht. Du kannst es finden, indem du die Y-Koordinate betrachtest, die positiv sein sollte (d.h. im unteren Teil der Anzeige) oder indem du den Namen der Bilddatei betrachtest.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Im Moment ist in meinem Beispiel die Bilddatei für die Antwortkarte immer `"1-blue-triangle.png"`. Aber natürlich möchten wir nicht immer ein einziges blaues Dreieck zeigen. Stattdessen soll die Bilddatei von den Variablen abhängen, die wir in der *block_loop* definiert haben. Ersetze dazu die Zahl durch `[response_number]`, die Farbe durch `[response_color]` und die Form durch `[response_shape]`: (Die eckigen Klammern geben an, dass dies auf die Namen von Variablen verweist.)


```
draw image center=1 file="[response_number]-[response_color]-[response_shape].png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Klicke auf Übernehmen, um die Änderungen am Skript zu akzeptieren. Die Antwortkarte wurde nun durch ein Fragezeichen-Symbol ersetzt. Dies liegt daran, dass OpenSesame nicht weiß, wie eine Vorschau eines Bildes angezeigt werden soll, das mit Variablen definiert wurde. Aber keine Sorge: Das Bild wird angezeigt, wenn du das Experiment ausführst!

### Schritt 6: Variabilität der Stimuluskarten herstellen

Die Stimuluskarten sollten mehr oder weniger zufällig ausgewählt werden, aber jede Farbe, Form und Nummer sollte nur einmal vorkommen; das heißt, es sollte nie zwei rote Karten oder zwei Karten mit Dreiecken geben. (Wenn es das gäbe, würde das Matching-Verfahren mehrdeutig werden.) Um dies zu erreichen, können wir *horizontal shuffling* verwenden, was eine leistungsstarke, aber ungewöhnliche Funktion des LOOP-Elements ist.

- %link:loop%

Öffne zunächst die *block_loop* und erstelle 12 (!) neue Spalten, um die Stimuluskarten zu definieren: `color1` für die Farbe der ersten Karte, `color2`, `color3`, `color4` und `shape1` ... `shape4` und `number1` ... `number4`. Jede Spalte hat denselben Wert in jeder Zeile (siehe %FigLoopTable2).

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  Die *block_loop* während Schritt 6.
--%

Aber das ist noch nicht alles! Derzeit ist die erste Stimuluskarte immer ein einzelner roter Kreis, der zweite zwei blaue Dreiecke usw. Um dies zu randomisieren, sagen wir OpenSesame, dass es die Werte der vier Farbvariablen, der vier Formvariablen und der vier Nummernvariablen zufällig tauschen (horizontal mischen) soll. Öffne dazu das Skript für die *block_loop*. Füge in der vorletzten Zeile (direkt vor `run trial_sequence`) die folgenden Befehle hinzu:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Klicke auf Übernehmen, um das Skript zu akzeptieren. Um zu sehen, ob dies funktioniert hat, klicke auf die Schaltfläche Vorschau. Dies zeigt eine Vorschau der randomisierten LOOP-Tabelle während des Experiments an. Sieht es gut aus?

Kehre nun zum *card_display* zurück und lasse das Bild der ersten Stimuluskarte von der Variable `color1`, `shape1` und `number1` abhängen, und analog dazu für die anderen Stimuluskarten. (Wenn du unsicher bist, wie das geht, kehre zu Schritt 5 zurück.)

### Schritt 7: Die richtige Antwort ermitteln (für eine Übereinstimmungsregel)

Bisher nehmen wir an, dass die Teilnehmer immer nur nach einer Form abstimmen. (Eine der Zusatzaufgaben besteht darin, dies zu verbessern.)

Momentan ist die Dauer von *card_display* auf "keypress" eingestellt. Dies bedeutet, dass der *card_display* angezeigt wird, bis eine Taste gedrückt wird, bietet jedoch keine Kontrolle darüber, wie dieser Tastendruck behandelt wird. Ändern Sie daher die Dauer auf 0 und fügen Sie direkt nach dem *card_display* eine KEYBOARD_RESPONSE ein. Benennen Sie die KEYBOARD_RESPONSE in *press_a* um und geben Sie an, dass die richtige Antwort "a" ist und dass die zulässigen Antworten "a; b; c; d" sind.

%--
abbildung:
 id: FigPressA
 Quelle: press-a.png
 Bildunterschrift: |
  Eines der KEYBOARD_RESPONSE-Elemente, die in Schritt 7 definiert wurden.
--%


Aber das ist nicht genug! Im Moment gibt es ein einzelnes Antwortelement, das davon ausgeht, dass die richtige Antwort immer "a" ist. Wir haben noch nicht angegeben, *wann* die richtige Antwort "a" ist, noch haben wir Versuche berücksichtigt, bei denen die richtige Antwort "b", "c" oder "d" ist.

Um dies zu erreichen, erstellen Sie zunächst drei weitere KEYBOARD_RESPONSE-Elemente: *press_b*, *press_c* und *press_d*. Diese sind alle gleich, mit Ausnahme der richtigen Antwort, die für jedes von ihnen separat definiert ist und "b", "c" bzw. "d" sein sollte.

Schließlich verwenden Sie im *trial_sequence* Run If-Anweisungen, um unter welcher Bedingung jeder der vier KEYBOARD_RESPONSE-Elemente ausgeführt werden sollte (d.h., entscheiden Sie, was die richtige Antwort ist). Bei *press_a* lautet die Bedingung, dass `shape1` gleich `response_shape` sein sollte. Warum? Nun, weil das bedeutet, dass die Form der ersten Stimulus-Karte gleich der Form der Antwortkarte ist und in diesem Fall die richtige Antwort "a" ist. Diese Bedingung entspricht der folgenden Run-if-Anweisung: `[shape1] = [response_shape]`. Die Run-if-Anweisungen für die anderen KEYBOARD_RESPONSE-Elemente sind analog (siehe %FigTrialSequence1).

%--
abbildung:
 id: FigTrialSequence1
 Quelle: trial-sequence-1.png
 Bildunterschrift: |
  Die *trial_sequence* am Ende von Schritt 7.
--%


### Schritt 8: Teilnehmer Feedback geben

OpenSesame verfolgt automatisch, ob eine Antwort korrekt war oder nicht, indem die Variable `correct` auf jeweils 1 oder 0 gesetzt wird. (Vorausgesetzt, natürlich, dass Sie die richtige Antwort angegeben haben, wie wir es in Schritt 7 getan haben.) Wir können dies nutzen, um dem Teilnehmer Feedback darüber zu geben, ob er richtig oder falsch geantwortet hat.

Fügen Sie dazu zwei neue SKETCHPADs zur *trial_sequence* hinzu und nennen Sie sie *correct_feedback* und *incorrect_feedback*. Geben Sie dann an, welches der beiden mit einer Run-if-Anweisung ausgeführt werden soll (siehe %FigTrialSequence2).


%--
abbildung:
 id: FigTrialSequence2
 Quelle: trial-sequence-2.png
 Bildunterschrift: |
  Die *trial_sequence* am Ende von Schritt 8.
--%


Fügen Sie schließlich beiden SKETCHPADs nützliche Inhalte hinzu. Zum Beispiel könnten Sie für *correct_feedback* einen grünen Fixpunkt verwenden und für *incorrect_feedback* einen roten Fixpunkt, in beiden Fällen für 500 ms angezeigt (d.h. die SKETCHPAD-Dauer auf 500 einstellen). Farbige Punkte sind eine schöne, unauffällige Möglichkeit, Feedback zu geben.

### Schritt 9: Experiment testen

Sie haben nun eine grundlegende (aber unvollständige!) Implementierung des Wisconsin Card Sorting Test erstellt. (Sie werden die Implementierung als Teil der Extra-Aufgaben unten abschließen.)

%--
abbildung:
 id: FigRunButtons
 Quelle: run-buttons.png
 Bildunterschrift: |
  Die Haupt-Symbolleiste enthält Schaltflächen zum (von links nach rechts): Vollbildmodus, Fenstermodus, Schnellstart (Ausführen in einem Fenster ohne nach Protokolldateien oder Teilnehmernummern zu fragen), Abbrechen des Experiments und Ausführen in einem Browser.
--%

Um das Experiment zu testen, klicken Sie auf die Schnellstart-Schaltfläche (die blauen Doppelpfeile), um das Experiment auf dem Desktop zu testen (siehe %FigRunButtons). Wenn das Experiment wie erwartet auf dem Desktop läuft, klicken Sie auf die Schaltfläche "Im Browser ausführen" (Pfeil im grünen Kreis), um das Experiment in einem Browser zu testen.


## Extra Aufgaben

### Extra 1 (einfach): Fügen Sie einen Logger hinzu

OpenSesame protokolliert nicht automatisch Daten. Stattdessen müssen Sie explizit ein `logger`-Element zu Ihrem Experiment hinzufügen. In einem versuchsbasierten Experiment ist ein `logger` in der Regel das letzte Element der *trial_sequence*, so dass alle während des Versuchs gesammelten Daten protokolliert werden.

Derzeit protokolliert unser WCST keine Daten. Zeit, das zu beheben!


### Extra 2 (einfach): Die Datendatei inspizieren

*Setzt voraus, dass Extra 1 abgeschlossen wurde*.

Führen Sie einen kurzen Testlauf des Experiments durch. Betrachten Sie nun die Protokolldatei in einem Programm wie Excel, LibreOffice Calc oder JASP. Identifizieren Sie die relevanten Variablen und überlegen Sie, wie Sie die Ergebnisse analysieren könnten.

__Profi-Tipp:__ Stellen Sie den Wiederholungswert des *block_loop* auf 0,1 ein, um die Anzahl der Versuche während des Tests zu reduzieren.


### Extra 3 (einfach): Anweisungen und Abschiedsbildschirm hinzufügen

Ein gutes Experiment kommt mit klaren Anweisungen. Und ein höfliches Experiment verabschiedet sich von den Teilnehmern, wenn sie fertig sind. Sie können dazu ein SKETCHPAD verwenden.

__Profi-Tipp:__ Ein FORM_TEXT_DISPLAY ist nicht kompatibel mit OSWeb, daher sollten Sie es nicht für Anweisungen verwenden, wenn Sie Ihr Experiment online durchführen möchten.


### Extra 4 (mittel): Die korrekte Antwort und die zuordnungsregel über JavaScript festlegen

Um Skripterstellung in OSWeb einzuschließen, können Sie das INLINE_JAVASCRIPT-Element verwenden, das JavaScript unterstützt. (Es bietet jedoch derzeit nicht alle Funktionen, die von der regulären Python INLINE_SCRIPT [])

Bisher ist die Zuordnungsregel immer, nach Form zu ordnen. Um dies zu ändern, fügen Sie ein INLINE_JAVASCRIPT-Element zu Beginn des Experiments hinzu und verwenden Sie das folgende Skript (in der *prepare*-Phase), um die Variable `matching_rule` zufällig auf 'form', 'zahl' oder 'farbe' zu setzen.

```javascript
function choice(choices) {
    // JavaScript hat keine integrierte Auswahlfunktion, also definieren wir sie
    // hier.
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}


// Das vars-Objekt enthält alle experimentellen Variablen, wie das var-Objekt
// in Python inline script
vars.matching_rule = choice(['form', 'zahl', 'farbe'])
```

Fügen Sie nun ein weiteres INLINE_JAVASCRIPT-Element am Anfang der *trial_sequence* hinzu. In der *prepare*-Phase fügen Sie ein Skript hinzu, um die Variable `correct_response` auf 'a', 'b', 'c' oder 'd' zu setzen. Dazu benötigen Sie eine Reihe von `if`-Anweisungen, die erst die Zuordnungsregel betrachten und dann betrachten, welche Form der Antwortform entspricht (für die Form-Zuordnungsregel) oder welche Farbe der Antwortfarbe entspricht (für die Farbzuordnungsregel) usw.

Um Ihnen den Einstieg zu erleichtern, hier ein Teil der Lösung (aber sie muss noch vervollständigt werden!):

```javascript
if (vars.matching_rule === 'form') {
    if (vars.shape1 === vars.response_shape) vars.correct_response = 'a'
    // Noch nicht fertig
} // Noch nicht fertig

// Lassen Sie uns einige Informationen im Debug-Fenster ausgeben
console.log('matching_rule = ' + vars.matching_rule)
console.log('correct_response = ' + vars.correct_response)
```


### Extra 5 (schwierig): Die Zuordnungsregel periodisch ändern

Bisher wird die Zuordnungsregel am Anfang des Experiments zufällig festgelegt, bleibt dann aber während des gesamten Experiments konstant. Bei einem echten WCST ändert sich die Zuordnungsregel jedoch periodisch, normalerweise nachdem der Teilnehmer eine feste Anzahl korrekter Antworten gegeben hat.

Um dies zu implementieren, benötigen Sie ein weiteres INLINE_JAVASCRIPT. Hier sind einige Tipps, um Ihnen den Einstieg zu erleichtern:

- Verwenden Sie eine Zählervariable, die nach einer korrekten Antwort um 1 erhöht wird und nach einer falschen Antwort auf 0 zurückgesetzt wird.
- Achten Sie beim Ändern der Zuordnungsregel darauf, dass sie nicht (zufällig) erneut auf die gleiche Zuordnungsregel eingestellt wird.


### Extra 6 (sehr schwierig): Die Antwortkarte einschränken

Derzeit kann die Antwortkarte mit einer Stimuluskarte in mehreren Dimensionen überlappen. Wenn beispielsweise eine der Stimuluskarten ein einzelner blauer Kreis ist, könnte die Antwortkarte zwei blaue Kreise sein, die sich sowohl in Farbe als auch in Form überschneiden. In einem echten WCST sollte die Antwortkarte jedoch mit jeder Stimuluskarte in höchstens einer Dimension überlappen.

Das liegt bei Ihnen. Diesmal keine Hinweise!

### Extra 7 (einfach): Das Experiment online mit JATOS ausführen

Unser WCST ist mit OSWeb kompatibel, was bedeutet, dass Sie es in einem Browser ausführen können. Um zu testen, ob dies noch funktioniert, können Sie in OpenSesame auf die Schaltfläche "Im-Browser-starten" klicken.

Um jedoch tatsächliche Daten mit dem Experiment in einem Browser zu sammeln, müssen Sie das Experiment in JATOS importieren und JATOS verwenden, um einen Link zu generieren, den Sie an Ihre Teilnehmer weitergeben können. Das ist viel einfacher als es klingt! Weitere Informationen finden Sie unter:

- %link:manual/osweb/workflow%

## Lösungen

Sie können das vollständige Experiment, einschließlich der Lösungen für die zusätzlichen Aufgaben, hier herunterladen:

- <https://osf.io/f5er2/>