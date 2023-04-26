title: Wisconsin-Karten-Sortier-Test
uptodate: false
hash: 62801ccad4fe18407f604f09c0a01cdc6bafc8cd4b09f38777af7ebaa44f1c71
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

In diesem Tutorial implementierst du den Wisconsin Card Sorting Test (WCST). Du wirst auch lernen, wie man Python-Code in das Experiment einbettet. (Für die OSWeb-Implementierung dieser Aufgabe siehe [dieses Tutorial](%url:wcst%)).

Im WCST sehen die Teilnehmer vier Stimuluskarten, die sich in drei Dimensionen unterscheiden: Farbe (rot, grün, blau, gelb), Form (Kreis, Stern, Dreieck, Kreuz) und Anzahl der Formen (eins, zwei, drei oder vier). Die Teilnehmer sehen auch eine einzelne Antwortkarte, die ebenfalls eine Farbe, Form und Anzahl hat.

Die Aufgabe des Teilnehmers besteht darin, die Antwortkarte der richtigen Stimuluskarte zuzuordnen, basierend auf einer bestimmten Dimension (z. B. Farbe) oder *Übereinstimmungsregel*. Der Teilnehmer weiß zunächst nicht, auf welcher Dimension er abgleichen soll, und seine Aufgabe besteht darin, die Übereinstimmungsregel durch Versuch und Irrtum herauszufinden.

Um die Sache schwieriger zu gestalten, ändert sich die Übereinstimmungsregel nach jeweils fünf richtigen Antworten. Daher muss der Teilnehmer seine Übereinstimmungsregel flexibel aktualisieren.


### Schritt 1: Herunterladen und starten von OpenSesame

OpenSesame ist für Windows, Linux und Mac OS verfügbar. Dieses Tutorial ist für OpenSesame 3.2 oder höher geschrieben.

Wenn du OpenSesame startest, hast du die Auswahl zwischen Vorlage-Experimenten und (falls vorhanden) einer Liste kürzlich geöffneter Experimente (siehe %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  Das Startfenster von OpenSesame.
--%

Die *Erweiterte Vorlage* bietet einen guten Ausgangspunkt für die Erstellung vieler Experimente, die eine Blockversuchsstruktur verwenden. In diesem Tutorial werden wir jedoch das gesamte Experiment von Grund auf erstellen und die "Standardvorlage" verwenden, die bereits geladen ist, wenn OpenSesame gestartet wird (%FigDefaultTemplate). Schließe einfach die Registerkarten 'Get started!' und (falls angezeigt) 'Welcome!'`.

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  Die Struktur der "Standardvorlage" im Überblicksbereich.
--%

### Schritt 2: Einen block_loop und trial_sequence hinzufügen

Die Standardvorlage beginnt mit drei Elementen: Einem NOTEPAD namens *getting_started*, einem SKETCHPAD namens *welcome* und einer SEQUENCE namens *experiment*. Wir benötigen *getting_started* und *welcome* nicht, also entfernen wir sie sofort. Um dies zu tun, klicke mit der rechten Maustaste auf diese Elemente und wähle "Löschen". Entferne nicht das *experiment*, da es den Einstiegspunkt für das Experiment ist (d. h. das erste Element, das aufgerufen wird, wenn das Experiment gestartet wird).

Unser Experiment wird eine sehr einfache Struktur haben. An der Spitze der Hierarchie steht eine LOOP, die wir *block_loop* nennen. In der *block_loop* definieren wir unsere unabhängigen Variablen. Um eine LOOP zu deinem Experiment hinzuzufügen, ziehe das LOOP-Symbol aus der Elementsymbolleiste auf das *experiment* Element im Überblicksbereich.

Ein LOOP-Element benötigt ein weiteres Element zum Ausführen; normalerweise, und auch in diesem Fall, ist dies eine SEQUENCE. Ziehe das SEQUENCE-Element aus der Elementsymbolleiste auf das Element *new_loop* im Überblicksbereich. OpenSesame fragt, ob du die SEQUENCE in oder nach der LOOP einfügen möchtest. Wähle "In new_loop einfügen".

Standardmäßig haben Elemente Namen wie *new_sequence*, *new_loop*, *new_sequence_2*, usw. Diese Namen sind nicht sehr informativ, und es ist ratsam, sie umzubenennen. Elementnamen müssen aus alphanumerischen Zeichen und/oder Unterstrichen bestehen. Um ein Element umzubenennen, klicke zweimal auf das Element im Überblicksbereich. Benenne *new_sequence* in *trial_sequence* um, um anzuzeigen, dass es einer einzelnen Versuchsreihe entspricht. Benenne *new_loop* in *block_loop* um, um anzuzeigen, dass es einem Block von Versuchsreihen entspricht.

Klicke abschließend auf "Neues Experiment", um die Allgemeinen Eigenschaften zu öffnen. Klicke auf den Titel des Experiments und benenne es in "Wisconsin Card Sorting Test" um.

Der Überblicksbereich unseres Experiments sieht nun wie in %FigBasicStructure aus.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  Der Überblicksbereich am Ende von Schritt 2.
--%


### Schritt 3: Bilder und Tondateien importieren

Für dieses Experiment verwenden wir Bilder für die Spielkarten. Sie können diese hier herunterladen:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Laden Sie `stimuli.zip` herunter und entpacken Sie es irgendwo (zum Beispiel auf Ihrem Desktop). Klicken Sie als Nächstes in OpenSesame auf die Schaltfläche 'Dateipool anzeigen' in der Hauptwerkzeugleiste (oder: Menü → Ansicht → Dateipool anzeigen). Dadurch wird der Dateipool standardmäßig auf der rechten Seite des Fensters angezeigt. Der einfachste Weg, die Reize im Dateipool hinzuzufügen, besteht darin, sie vom Desktop (oder von dem Ort, an dem Sie die Dateien extrahiert haben) in den Dateipool zu ziehen. Alternativ können Sie auf die Schaltfläche '+' im Dateipool klicken und Dateien über den erscheinenden Dateiauswahldialog hinzufügen. Der Dateipool wird automatisch mit Ihrem Experiment gespeichert.

Nachdem Sie alle Reize hinzugefügt haben, sieht Ihr Dateipool wie in %FigFilePool aus.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Der Dateipool mit den Reizen.
--%


### Schritt 4: Eine statische Kartendarstellung erstellen

Zunächst erstellen wir eine Darstellung mit vier Reizkarten und einer Antwortkarte. Welche Karten jedoch angezeigt werden, hängt noch nicht von den Variablen ab; das heißt, wir erstellen eine *statische* Anzeige.

Ziehen Sie eine SKETCHPAD in die *trial_sequence* und benennen Sie es in *card_display* um. Verwenden Sie das Bildwerkzeug, um vier Karten in einer horizontalen Reihe irgendwo am oberen Rand der Anzeige zu zeichnen; dies werden die Reizkarten sein. Zeichnen Sie eine einzelne Karte in der Nähe des unteren Randes der Anzeige; dies wird die Antwortkarte sein. Fügen Sie auch einen Text hinzu, um dem Teilnehmer mitzuteilen, was er oder sie tun muss, nämlich `a`, `b`, `c` oder `d` drücken, um anzuzeigen, welche der Reizkarten mit der Antwortkarte übereinstimmt. Der genaue Text, das Layout und die Karten liegen bei Ihnen! Tipps: Sie können die Option *scale* verwenden, um die Größe der Karten anzupassen; Sie können die Hintergrundfarbe im Tab Allgemeine Eigenschaften ändern, den Sie öffnen können, indem Sie auf das oberste Element des Experiments klicken.

Bei mir sieht das Ergebnis so aus:


%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Eine SKETCHPAD mit statisch definierten Karten.
--%


### Schritt 5: Die Antwortkarte variabel gestalten

Im Moment zeigen wir immer dieselbe Antwortkarte (im Beispiel oben ein einzelnes blaues Dreieck). Aber natürlich möchten wir auf jedem Test eine andere Antwortkarte anzeigen. Um dies zu tun, müssen wir zunächst die Variablen definieren, die bestimmen, welche Antwortkarte wir zeigen werden. Wir werden dies im *block_loop* tun.

Öffnen Sie den *block_loop*. Die LOOP-Tabelle ist jetzt leer. Um die Farbe, Form und Anzahl der Antwortkarte zu bestimmen, könnten wir manuell drei Spalten (`response_color`, `response_shape` und `response_number`) und 64 Zeilen für alle möglichen Kombinationen von Farben, Formen und Zahlen erstellen. Aber das wäre viel Arbeit. Stattdessen verwenden wir den Vollfaktoriellen-Design-Assistenten, den Sie öffnen können, indem Sie auf die Schaltfläche 'Vollfaktorielles Design' klicken. (Ein vollfaktorielles Design ist ein Design, in dem alle möglichen Kombinationen von Variablenebenen auftreten.) In diesem Assistenten erstellen Sie für jede der drei Variablen eine Spalte und geben in den darunter liegenden Zellen die möglichen Werte für diese Variable ein (siehe %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  Der Vollfaktorielle-Design-Assistent ermöglicht es Ihnen, große LOOP-Tabellen zu erstellen, die vollfaktoriellen Designs entsprechen.
--%


Klicken Sie anschließend auf die Schaltfläche OK. Der *block_loop* enthält nun alle 64 Kombinationen von Farben, Zahlen und Formen (siehe %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  Der *block_loop* am Ende von Schritt 5.
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

OpenSesame protokolliert Daten nicht automatisch. Stattdessen müssen Sie explizit ein `logger`-Element zu Ihrem Experiment hinzufügen. In einem versuchsweisen Experiment ist ein `logger` normalerweise das letzte Element der *trial_sequence*, damit alle während des Versuchs gesammelten Daten protokolliert werden.

Im Moment protokolliert unser WCST keine Daten. Zeit, das zu beheben!

### Extra 2 (einfach): Überprüfen Sie die Datendatei

*Voraussetzung dafür ist, dass Sie Extra 1 abgeschlossen haben*.

Führen Sie das Experiment kurz durch. Überprüfen Sie nun die Protokolldatei in einem Programm wie Excel, LibreOffice Calc oder JASP. Identifizieren Sie die relevanten Variablen und überlegen Sie, wie Sie die Ergebnisse analysieren könnten.

__Pro-Tipp:__ Setzen Sie den Wiederholungswert von *block_loop* auf 0,1, um die Anzahl der Versuche während des Tests zu reduzieren.

### Extra 3 (einfach): Anweisungen und Verabschiedungsbildschirm hinzufügen

Ein gutes Experiment enthält klare Anweisungen. Und ein höfliches Experiment verabschiedet sich von den Teilnehmern, wenn sie fertig sind. Sie können dazu ein SKETCHPAD verwenden.

### Extra 4 (mittel): Die korrekte Antwort und die passende Regel mit Python Inline-Skript einstellen

Um Python-Skripte in OpenSesame einzufügen, können Sie das INLINE_SCRIPT-Element verwenden.

Bisher ist die passende Regel immer nach Form abzugleichen. Um dies zu ändern, fügen Sie ein INLINE_SCRIPT-Element zu Beginn des Experiments hinzu und verwenden Sie das folgende Skript (in der *prepare*-Phase), um die Variable `matching_rule` zufällig auf 'shape', 'number' oder 'color' zu setzen.

```python
import random

var.matching_rule = random.choice(['shape', 'number', 'color'])
```

Fügen Sie jetzt ein weiteres INLINE_SCRIPT-Element zum Start der *trial_sequence* hinzu. Fügen Sie in der *prepare*-Phase ein Skript hinzu, um die Variable `correct_response` auf 'a', 'b', 'c' oder 'd' zu setzen. Dazu benötigen Sie eine Reihe von `if`-Anweisungen, die zunächst die passende Regel betrachten und dann prüfen, welche Form der Antwortform entspricht (bei der Formabgleichsregel) oder welche Farbe der Antwortfarbe entspricht (bei der Farbabgleichsregel) usw.

Hier ist ein Teil der Lösung, um Ihnen den Einstieg zu erleichtern (aber es muss noch vervollständigt werden!):

```python
if var.matching_rule == 'shape':
    if var.shape1 == var.response_shape:
        var.correct_response = 'a'
    # Noch nicht fertig
# Noch nicht fertig

# Ein paar Informationen in das Debug-Fenster drucken
print('matching_rule = {}'.format(var.matching_rule))
print('correct_response = {}'.format(var.correct_response))
```

### Extra 5 (schwierig): Ändern Sie die passende Regel regelmäßig

Bisher wird die passende Regel zu Beginn des Experiments zufällig bestimmt, bleibt aber während des gesamten Experiments konstant. In einem echten WCST ändert sich die passende Regel in der Regel periodisch, normalerweise nachdem der Teilnehmer eine feste Anzahl von richtigen Antworten gegeben hat.

Um dies zu implementieren, benötigen Sie ein weiteres INLINE_SCRIPT. Hier einige Tipps zum Einstieg:

- Verwenden Sie eine Zählervariable, die nach einer richtigen Antwort um 1 erhöht wird und nach einer falschen Antwort auf 0 zurückgesetzt wird.
- Achten Sie darauf, dass die passende Regel nicht (durch Zufall) wieder auf dieselbe passende Regel gesetzt wird.

### Extra 6 (wirklich schwierig): Beschränken Sie die Antwortkarte

Im Moment kann die Antwortkarte in mehreren Dimensionen mit einer Stimuluskarte überlappen. Wenn beispielsweise eine der Stimuluskarten ein einzelner blauer Kreis ist, kann die Antwortkarte zwei blaue Kreise enthalten, die sich sowohl in der Farbe als auch in der Form überlappen. In einem echten WCST sollte die Antwortkarte mit jeder Stimuluskarte nur in einer Dimension maximal übereinstimmen.

Diesmal liegt es an Ihnen. Keine Hinweise diesmal!

## Lösungen

Das vollständige Experiment, einschließlich der Lösungen zu den Extraaufgaben, können Sie hier herunterladen:

- <https://osf.io/f5er2/>