title: Wisconsin-Karten-Sortier-Test
hash: 4199e2aea0b73c7c2aec2a427017e0f2de9ffa30a72377e12ed75900a1fbc9a1
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


In diesem Tutorial werden Sie den Wisconsin Card Sorting Test (WCST) implementieren. Sie lernen auch, wie Sie Python-Code in das Experiment einbetten können. (Für die Implementierung dieser Aufgabe in OSWeb, siehe [dieses Tutorial](%url:wcst%)).

Im WCST sehen die Teilnehmer vier Reizkarten, die sich in drei Dimensionen unterscheiden: Farbe (rot, grün, blau, gelb), Form (Kreis, Stern, Dreieck, Kreuz) und Anzahl der Formen (eins, zwei, drei oder vier). Die Teilnehmer sehen auch eine einzelne Antwortkarte, die ebenfalls eine Farbe, Form und Anzahl hat.

Die Aufgabe des Teilnehmers besteht darin, die Antwortkarte der richtigen Reizkarte zuzuordnen, basierend auf einer bestimmten Dimension (z. B. Farbe) oder *Abgleichsregel*. Der Teilnehmer weiß zunächst nicht, nach welcher Dimension er die Karten abgleichen soll, und seine Aufgabe besteht darin, die Abgleichsregel durch Versuch und Irrtum herauszufinden.

Um die Sache schwieriger zu machen, ändert sich die Abgleichsregel nach jeweils fünf korrekten Antworten. Daher muss der Teilnehmer flexibel seine Abgleichsregeln aktualisieren.


### Schritt 1: OpenSesame herunterladen und starten

OpenSesame ist für Windows, Linux und Mac OS verfügbar. Dieses Tutorial ist für OpenSesame 4.0 oder höher geschrieben.

Wenn Sie OpenSesame starten, haben Sie die Wahl zwischen verschiedenen Vorlagen für Experimente und (falls vorhanden) einer Liste kürzlich geöffneter Experimente (%FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  Das OpenSesame-Fenster beim Start.
--%

Die *Erweiterte Vorlage* bietet einen guten Ausgangspunkt für die Erstellung vieler Experimente, die eine Block-Versuchs-Struktur verwenden. In diesem Tutorial werden wir jedoch das gesamte Experiment von Grund auf erstellen und die "Standardvorlage" verwenden, die bereits beim Start von OpenSesame geladen ist (%FigDefaultTemplate). Schließen Sie daher einfach die Registerkarten "Los geht's!" und (falls angezeigt) "Willkommen!".

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  Die Struktur der "Standardvorlage" im Überblicksbereich.
--%


### Schritt 2: Blockschleife und Versuchsreihenfolge hinzufügen

Die Standardvorlage beginnt mit drei Elementen: Einem NOTIZBLOCK namens *getting_started*, einem SKIZZENBLOCK namens *welcome* und einer SEQUENZ namens *experiment*. Wir benötigen *getting_started* und *welcome* nicht, also entfernen wir sie gleich. Klicken Sie dazu mit der rechten Maustaste auf diese Elemente und wählen Sie "Löschen". Entfernen Sie nicht *experiment*, da es der Einstiegspunkt für das Experiment ist (d. h. das erste Element, das aufgerufen wird, wenn das Experiment gestartet wird).

Unser Experiment wird eine sehr einfache Struktur haben. An der Spitze der Hierarchie steht eine LOOP, die wir *block_loop* nennen. Im *block_loop* definieren wir unsere unabhängigen Variablen. Um eine LOOP zu Ihrem Experiment hinzuzufügen, ziehen Sie das LOOP-Symbol aus der Elementleiste auf das Element *experiment* im Überblicksbereich.

Ein LOOP-Element benötigt ein anderes Element zum Ausführen; normalerweise ist dies eine SEQUENZ, in diesem Fall auch. Ziehen Sie das SEQUENZ-Element aus der Elementleiste auf das Element *new_loop* im Überblicksbereich. OpenSesame fragt, ob Sie die SEQUENZ in die oder nach der LOOP einfügen möchten. Wählen Sie "In new_loop einfügen".

Standardmäßig haben Elemente Namen wie *new_sequence*, *new_loop*, *new_sequence_2* usw. Diese Namen sind nicht sehr aussagekräftig, und es ist sinnvoll, sie umzubenennen. Elementnamen müssen aus alphanumerischen Zeichen und/oder Unterstrichen bestehen. Um ein Element umzubenennen, doppelklicken Sie auf das Element im Überblicksbereich. Benennen Sie *new_sequence* in *trial_sequence* um, um anzuzeigen, dass es einem einzelnen Versuch entspricht. Benennen Sie *new_loop* in *block_loop* um, um anzuzeigen, dass es einem Block von Versuchen entspricht.

Klicken Sie abschließend auf "Neues Experiment", um die Registerkarte "Allgemeine Eigenschaften" zu öffnen. Klicken Sie auf den Titel des Experiments und benennen Sie ihn in "Wisconsin Card Sorting Test" um.

Der Übersichtsbereich unseres Experiments sieht nun aus wie in %FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  Der Übersichtsbereich am Ende von Schritt 2.
--%


### Schritt 3: Bilder und Tondateien importieren

Für dieses Experiment verwenden wir Bilder für die Spielkarten. Sie können diese von hier herunterladen:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Laden Sie `stimuli.zip` herunter und entpacken Sie es irgendwo (zum Beispiel auf Ihrem Desktop). Klicken Sie anschließend in OpenSesame auf die Schaltfläche "Dateipool anzeigen" in der Hauptwerkzeugleiste (oder: Menü → Ansicht → Dateipool anzeigen). Dadurch wird der Dateipool standardmäßig auf der rechten Seite des Fensters angezeigt. Der einfachste Weg, die Reize in den Dateipool hinzuzufügen, besteht darin, sie vom Desktop (oder von dem Ort, an dem Sie die Dateien extrahiert haben) in den Dateipool zu ziehen. Alternativ können Sie auf die Schaltfläche "+" im Dateipool klicken und Dateien über den angezeigten Dateiauswahldialog hinzufügen. Der Dateipool wird automatisch mit Ihrem Experiment gespeichert.

Nachdem Sie alle Reize hinzugefügt haben, sieht Ihr Dateipool wie in %FigFilePool aus.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  Der Dateipool mit den Reizen.
--%


### Schritt 4: Eine statische Kartendarstellung erstellen

Zunächst erstellen wir eine Anzeige mit vier Reizkarten und einer Antwortkarte. Welche Karten jedoch gezeigt werden, hängt vorerst nicht von Variablen ab; das heißt, wir erstellen eine *statische* Anzeige.

Ziehen Sie ein SKETCHPAD in *trial_sequence* und benennen Sie es in *card_display* um. Verwenden Sie das Bild-Werkzeug, um vier Karten in einer horizontalen Reihe in der Nähe der Oberseite der Anzeige zu zeichnen; dies werden die Reizkarten sein. Zeichnen Sie in der Nähe des unteren Randes der Anzeige eine einzelne Karte; dies wird die Antwortkarte sein. Fügen Sie außerdem einen Text hinzu, um dem Teilnehmer mitzuteilen, was er tun soll, nämlich `a`, `b`, `c` oder `d` drücken, um anzugeben, welche der Reizkarten der Antwortkarte entspricht. Der genaue Text, das Layout und die Karten bleiben Ihnen überlassen! Tipps: Sie können die Option *Skalierung* verwenden, um die Größe der Karten anzupassen; Sie können die Hintergrundfarbe im Tab „Allgemeine Eigenschaften“ ändern, den Sie durch Klicken auf den obersten Eintrag des Experiments öffnen können.

Für mich sieht das Ergebnis so aus:

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Ein SKETCHPAD mit statisch definierten Karten.
--%


### Schritt 5: Die Antwortkarte variabel gestalten

Im Moment zeigen wir immer die gleiche Antwortkarte (im obigen Beispiel ein einzelnes blaues Dreieck). Natürlich möchten wir aber auf jedem Versuch eine andere Antwortkarte zeigen. Um dies zu tun, müssen wir zunächst die Variablen definieren, die bestimmen, welche Antwortkarte wir zeigen werden. Wir werden dies im *block_loop* tun.

Öffnen Sie den *block_loop*. Die LOOP-Tabelle ist jetzt leer. Um die Farbe, Form und Anzahl der Antwortkarten zu bestimmen, könnten wir manuell drei Spalten (`response_color`, `response_shape` und `response_number`) und 64 Zeilen für alle möglichen Kombinationen aus Farben, Formen und Zahlen erstellen. Das wäre jedoch viel Arbeit. Stattdessen verwenden wir den Assistenten für vollfaktorielle Designs, den Sie durch Klicken auf die Schaltfläche "Vollfaktorielles Design" öffnen können (Ein vollfaktorielles Design ist ein Design, in dem alle möglichen Kombinationen von Variablenstufen auftreten). In diesem Assistenten erstellen Sie für jede der drei Variablen eine Spalte und geben in den Zellen darunter die möglichen Werte für diese Variable ein (siehe %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  Der Assistent für vollfaktorielle Designs ermöglicht es Ihnen, große LOOP-Tabellen zu generieren, die vollfaktoriellem Designs entsprechen.
--%


Klicken Sie anschließend auf die Schaltfläche OK. Der *block_loop* enthält nun alle 64 Kombinationen von Farben, Zahlen und Formen (siehe %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  Der *block_loop* am Ende von Schritt 5.
--%

Kehren Sie jetzt zum *card_display* zurück. Jeder Artikel in OpenSesame wird durch ein Skript definiert. Dieses Skript wird automatisch von der Benutzeroberfläche generiert. Manchmal kann es praktisch (oder sogar notwendig) sein, dieses Skript direkt zu bearbeiten. Der häufigste Grund für das Bearbeiten des Skripts eines Elements besteht darin, Variablen zum Skript hinzuzufügen, was auch das ist, was wir jetzt tun werden!

Um das Skript anzuzeigen, klicken Sie auf die Schaltfläche "Ansicht" und wählen Sie "Skript anzeigen". (Die Schaltfläche "Ansicht" ist die mittlere Schaltfläche oben rechts in den Elementsteuerungen.) Dadurch wird ein Skripteditor geöffnet.

Das Skript für *card_display* besteht hauptsächlich aus `draw`-Befehlen, die jeweils eine der fünf Karten sowie die verschiedenen Textelemente definieren. Suchen Sie die Zeile, die zur Antwortkarte gehört. Sie können es finden, indem Sie auf die Y-Koordinate achten, die positiv sein sollte (d. h. im unteren Bereich der Anzeige) oder indem Sie den Namen der Bilddatei suchen.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Im Moment ist die Bilddatei für die Antwortkarte in meinem Beispiel immer `"1-blue-triangle.png"`. Aber natürlich möchten wir nicht immer ein einziges blaues Dreieck zeigen. Stattdessen möchten wir, dass die Bilddatei von den Variablen abhängt, die wir im *block_loop* definiert haben. Ersetzen Sie dazu die Zahl durch `{response_number}`, die Farbe durch `{response_color}` und die Form durch `{response_shape}`: (Die eckigen Klammern geben an, dass sich diese auf Namen von Variablen beziehen.)

```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Klicken Sie auf Übernehmen, um die Änderungen am Skript zu akzeptieren. Die Antwortkarte wurde nun durch ein Fragezeichen-Symbol ersetzt. Dies liegt daran, dass OpenSesame nicht weiß, wie man eine Vorschau eines Bildes anzeigt, das über Variablen definiert wurde. Aber keine Sorge: Das Bild wird angezeigt, wenn Sie das Experiment ausführen!


### Schritt 6: Machen Sie die Stimulus-Karten variabel

Die Stimulus-Karten sollten mehr oder weniger zufällig ausgewählt werden, aber jede Farbe, Form und Nummer sollte nur einmal vorkommen; das heißt, es sollte nie zwei rote Karten oder zwei Karten mit Dreiecken geben. (Wenn dies der Fall wäre, würde das Abgleichverfahren mehrdeutig.) Um dies zu erreichen, können wir *horizontales Mischen* verwenden, eine leistungsstarke, aber ungewöhnliche Funktion des LOOP-Elements.

- %link:loop%

Öffnen Sie zuerst die *block_loop* und erstellen Sie 12 (!) neue Spalten, um die Stimulus-Karten zu definieren: `color1` für die Farbe der ersten Karte, `color2`, `color3`, `color4` und `shape1` ... `shape4`, und `number1`...`number4`. Jede Spalte hat denselben Wert in jeder Zeile (siehe %FigLoopTable2).


%--
Abbildung:
 id: FigLoopTable2
 Quelle: loop-table-2.png
 Unterschrift: |
  Die *block_loop* während Schritt 6.
--%


Aber wir sind noch nicht fertig! Im Moment ist die erste Stimulus-Karte immer ein einziger roter Kreis, der zweite zwei blaue Dreiecke usw. Um dies zu randomisieren, sagen wir OpenSesame, um die Werte der vier Farbvariablen, der vier Formvariablen und der vier Anzahlvariablen zufällig zu tauschen (horizontal zu mischen). Öffnen Sie dazu das Skript für die *block_loop*. Fügen Sie in der vorletzten Zeile (direkt vor `run trial_sequence`) die folgenden Befehle hinzu:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Klicken Sie auf Übernehmen, um das Skript anzunehmen. Um zu sehen, ob dies funktioniert hat, klicken Sie auf die Schaltfläche "Vorschau". Dadurch wird eine Vorschau angezeigt, wie die LOOP-Tabelle während des Experiments randomisiert wird. Sieht das gut aus?

Kehren Sie jetzt zum *card_display* zurück und lassen Sie das Bild der ersten Stimulus-Karte von der Variable `color1`, `shape1` und `number1` abhängen und analog für die anderen Stimulus-Karten. (Wenn Sie sich nicht sicher sind, wie Sie dies tun sollen, kehren Sie zu Schritt 5 zurück.)


### Schritt 7: Bestimmen Sie die richtige Antwort (für eine Übereinstimmungsregel)


Zunächst gehen wir davon aus, dass die Teilnehmer immer nach Form abgleichen. (Eine der Zusatzaufgaben besteht darin, dies zu verbessern.)

Momentan ist die Dauer von *card_display* auf 'keypress' eingestellt. Das bedeutet, dass die *card_display* angezeigt wird, bis eine Taste gedrückt wird, aber es bietet keine Kontrolle darüber, wie dieser Tastendruck behandelt wird. Ändern Sie daher die Dauer auf 0 und fügen Sie direkt nach der *card_display* eine KEYBOARD_RESPONSE ein. Benennen Sie die KEYBOARD_RESPONSE in *press_a* um und geben Sie an, dass die richtige Antwort 'a' und die erlaubten Antworten 'a; b; c; d' sind.

%--
Abbildung:
 ID: FigPressA
 Quelle: press-a.png
 Bildunterschrift: |
  Eines der KEYBOARD_RESPONSE-Elemente, das in Schritt 7 definiert ist.
--%

Aber das ist nicht genug! Im Moment gibt es ein einzelnes Antwort-Element, das annimmt, dass die richtige Antwort immer "a" ist. Wir haben noch nicht angegeben, *wann* die richtige Antwort "a" ist, noch haben wir Testläufe in Betracht gezogen, bei denen die richtige Antwort "b", "c" oder "d" ist.

Um dies zu erreichen, erstellen Sie zuerst drei weitere KEYBOARD_RESPONSE-Elemente: *press_b*, *press_c* und *press_d*. Diese sind alle gleich, mit Ausnahme der richtigen Antwort, die für jedes von ihnen separat definiert ist und jeweils 'b', 'c' und 'd' sein sollte.

Schließlich verwenden Sie in der *trial_sequence* Run If-Anweisungen, um zu entscheiden, unter welchen Bedingungen jedes der vier KEYBOARD_RESPONSE-Elemente ausgeführt werden soll (und damit entscheiden, was die richtige Antwort ist). Für *press_a* lautet die Bedingung, dass `shape1` gleich `response_shape` sein sollte. Warum? Nun, weil das bedeutet, dass die Form der ersten Stimulus-Karte der Form der Antwortkarte entspricht und in diesem Fall die richtige Antwort "a" ist. Dieser Zustand entspricht der folgenden Run-if-Anweisung: `shape1 = response_shape`. Die Run-if-Anweisungen für die anderen KEYBOARD_RESPONSE-Elemente sind analog (siehe %FigTrialSequence1).

%--
Abbildung:
 ID: FigTrialSequence1
 Quelle: trial-sequence-1.png
 Bildunterschrift: |
  Die *trial_sequence* am Ende von Schritt 7.
--%

### Schritt 8: Geben Sie dem Teilnehmer Feedback

OpenSesame behält automatisch im Auge, ob eine Antwort korrekt war oder nicht, indem es die Variable `correct` auf 1 oder 0 setzt. (Vorausgesetzt natürlich, dass Sie die richtige Antwort angegeben haben, wie wir es in Schritt 7 getan haben.) Wir können dies nutzen, um dem Teilnehmer Feedback darüber zu geben, ob er korrekt geantwortet hat oder nicht.

Fügen Sie dazu zwei neue SKETCHPADs zur *trial_sequence* hinzu und nennen Sie sie *correct_feedback* und *incorrect_feedback*. Geben Sie dann an, welche der beiden mit einer Run-if-Anweisung ausgeführt werden soll (siehe %FigTrialSequence2).

%--
Abbildung:
 ID: FigTrialSequence2
 Quelle: trial-sequence-2.png
 Bildunterschrift: |
  Die *trial_sequence* am Ende von Schritt 8.
--%

Fügen Sie schließlich beiden SKETCHPADs nützliche Inhalte hinzu. Zum Beispiel könnten Sie bei *correct_feedback* einen grünen Fixationspunkt verwenden und bei *incorrect_feedback* einen roten Fixationspunkt, der in beiden Fällen für 500 ms angezeigt wird (d. h. die Dauer der SKETCHPAD auf 500 einstellen). Farbige Punkte sind eine dezente Möglichkeit, Feedback zu geben.

### Schritt 9: Testen Sie das Experiment

Sie haben jetzt eine grundlegende (aber unvollständige!) Implementierung des Wisconsin Card Sorting Tests erstellt. (Sie werden die Implementierung als Teil der Extra-Aufgaben unten abschließen.)

Klicken Sie zum Testen des Experiments auf die Schnellstart-Schaltfläche (die blauen Doppelpfeile) oder auf die Schaltfläche "Im Vollbildmodus ausführen" (der grüne Pfeil).

## Extra-Aufgaben

### Extra 1 (einfach): Fügen Sie einen Logger hinzu

OpenSesame protokolliert nicht automatisch Daten. Stattdessen müssen Sie Ihrem Experiment explizit ein `logger`-Element hinzufügen. In einem probenbasierten Experiment ist ein `logger` im Allgemeinen das letzte Element der *trial_sequence*, sodass alle Daten erfasst werden, die während des Tests gesammelt wurden.

Momentan protokolliert unser WCST keine Daten. Zeit, das zu ändern!

### Extra 2 (einfach): Untersuchen Sie die Datei

*Voraussetzung dafür ist, dass Sie Extra 1 abgeschlossen haben*.

Geben Sie dem Experiment einen kurzen Testlauf. Untersuchen Sie nun die Log-Datei in einem Programm wie Excel, LibreOffice Calc oder JASP. Identifizieren Sie die relevanten Variablen und überlegen Sie, wie Sie die Ergebnisse analysieren könnten.

__Profi-Tipp:__ Setzen Sie den Wiederholungswert der *block_loop* auf 0,1, um die Anzahl der Versuche während des Tests zu reduzieren.

### Extra 3 (einfach): Anweisungen und Abschiedsbildschirm hinzufügen

Ein gutes Experiment enthält klare Anweisungen. Und ein höfliches Experiment verabschiedet sich von den Teilnehmern, wenn sie fertig sind. Sie können dazu ein SKETCHPAD verwenden.

### Extra 4 (mittel): Die richtige Antwort und passende Regel durch Python-Inline-Skript festlegen

Um Python-Scripting in OpenSesame zu verwenden, können Sie den INLINE_SCRIPT-Element verwenden.

Bisher ist die passende Regel immer, nach Form abzugleichen. Um dies zu ändern, fügen Sie ein INLINE_SCRIPT-Element zu Beginn des Experiments hinzu und verwenden Sie das folgende Skript (in der *prepare*-Phase), um die Variable `matching_rule` zufällig auf 'shape', 'number' oder 'color' zu setzen.

```python
import random

matching_rule = random.choice(['shape', 'number', 'color'])
```

Fügen Sie nun ein weiteres INLINE_SCRIPT-Element zu Beginn der *trial_sequence* hinzu. Fügen Sie in der *prepare*-Phase ein Skript hinzu, um die Variable `correct_response` auf 'a', 'b', 'c' oder 'd' zu setzen. Dazu benötigen Sie eine Reihe von `if`-Anweisungen, die zuerst die passende Regel betrachten und dann untersuchen, welche Form der Antwortform entspricht (für die Formabgleichsregel) oder welche Farbe der Antwortfarbe entspricht (für die Farbabgleichsregel) usw.

Zum Einstieg finden Sie hier einen Teil der Lösung (aber es muss noch vervollständigt werden!):

```python
if matching_rule == 'shape':
    if shape1 == response_shape:
        correct_response = 'a'
    # Noch nicht fertig
# Noch nicht fertig

# Lassen Sie uns einige Informationen in das Debug-Fenster ausgeben
print('matching_rule = {}'.format(matching_rule))
print('correct_response = {}'.format(correct_response))
```

### Extra 5 (schwierig): Passende Regel periodisch ändern

Bisher wird die passende Regel zufällig am Anfang des Experiments festgelegt, bleibt dann aber während des gesamten Experiments konstant. In einem echten WCST ändert sich die passende Regel jedoch periodisch, typischerweise nachdem der Teilnehmer eine feste Anzahl von richtigen Antworten gegeben hat.

Dazu benötigen Sie ein weiteres INLINE_SCRIPT. Hier sind einige Tipps zum Einstieg:

- Verwenden Sie eine Zählvariable, die nach einer richtigen Antwort um 1 erhöht wird und nach einer falschen Antwort auf 0 zurückgesetzt wird.
- Stellen Sie bei der Änderung der passenden Regel sicher, dass sie nicht (zufälligerweise) wieder auf die gleiche passende Regel gesetzt wird.

### Extra 6 (wirklich schwierig): Antwortkarte einschränken

Im Moment kann die Antwortkarte in mehreren Dimensionen mit einer Reizkarte überlappen. Wenn beispielsweise eine der Reizkarten ein einzelner blauer Kreis ist, kann die Antwortkarte zwei blaue Kreise enthalten und somit sowohl in Farbe als auch in Form überlappen. In einem echten WCST sollte die Antwortkarte jedoch in nicht mehr als einer Dimension mit jeder Reizkarte überlappen.

Diesmal ist es Ihnen überlassen. Keine Tipps diesmal!

## Lösungen

Sie können das vollständige Experiment, einschließlich der Lösungen für die zusätzlichen Aufgaben, hier herunterladen:

- <https://osf.io/f5er2/>