title: Impliziter Assoziationstest
uptodate: false
hash: d71135886d1eab5c8ea213f440c31193dc6e9c150ad7be41af10263195d05180
locale: de
language: German

## Impliziter Assoziationstest

Der implizite Assoziationstest misst die Stärke der Assoziationen zwischen Konzepten (z.B. junge Menschen und alte Menschen) und Bewertungen (z.B. gut und schlecht). Die Idee ist, dass die Abgabe einer Antwort einfacher (und daher *schneller*) ist, wenn verwandte Elemente denselben Antwortenschlüssel haben.

Hier werden wir die Assoziation zwischen jung und alt, sowie gut und schlecht messen. Wir gehen davon aus, dass junge Teilnehmer (unterbewusst) positive Wörter eher mit jungen Gesichtern als mit alten Gesichtern assoziieren.

## Anleitungs-Screencast

Diese Anleitung ist auch als Screencast verfügbar:

%--
video:
 source: youtube
 id: Screencast
 videoid: zd-nxgGOGlE
 width: 640
 height: 360
 caption: |
  Ein Screencast des IAT-Tutorials.
--%

## Experimentelle Hierarchie

Um diese Vorhersage zu testen, führen die Teilnehmer vier Blöcke von Versuchen durch (%Task)

- __Block 1__ -- Die Teilnehmer kategorisieren *Wörter* entweder als *POSITIV* oder *NEGATIV*. Die Kategorienamen erscheinen oben links und oben rechts auf dem Bildschirm, und die Teilnehmer drücken mit ihrer linken oder rechten Hand eine Taste, um anzuzeigen, zu welcher Kategorie ein zentral präsentiertes Wort gehört
- __Block 2__ -- Teilnehmer kategorisieren *Gesichter* als *ALT* oder *JUNG*, wieder durch eine linke oder rechte Handantwort
- __Block 3__ -- Ist eine Kombination aus Block 1 und 2. In diesem Beispiel erscheinen die Wörter *POSITIV* und *JUNG* oben links, während die Wörter *NEGATIV* und *ALT* oben rechts erscheinen. Da wir annehmen, dass (junge) Teilnehmer eine positivere Einstellung zu jungen Gesichtern haben, nennen wir diese Zuordnung *kongruent*
- __Block 4__ -- Ist wieder eine Kombination aus Block 1 und 2, aber diesmal ist die Zuordnung *inkongruent*

%--
figure:
 id: Task
 source: IAT-task.png
 caption: |
  Eine Übersicht über die vier Blöcke der impliziten Assoziationsaufgabe.
--%

## Vorhersage

Die Vorhersage ist, dass die Teilnehmer eine Präferenz für junge Menschen gegenüber alten Menschen haben, so dass es einfacher ist, Wörter zu kategorisieren, wenn jung und positiv einen Antwortenschlüssel teilen und alt und negativ einen Antwortenschlüssel teilen (im Vergleich zur umgekehrten Zuordnung). Dies sollte zu *schnelleren* Antworten im kongruenten Block als im inkongruenten Block führen (%Prediction).

%--
figure:
 id: Prediction
 source: prediction.png
 caption: |
  Wir gehen davon aus, dass die Teilnehmer es einfacher finden, Wörter und Gesichter zu kategorisieren, wenn die Kategorien *POSITIV/JUNG* und *NEGATIV/ALT* kombiniert sind (im Vergleich zur umgekehrten).
--%

## Ablauf einer Versuchsreihe

Um diese Vorhersage zu überprüfen, erstellen wir folgende Versuchsabfolge (%TrialSequence):

- Jeder Versuch beginnt mit einem __Fixationspunkt__ (500 ms)
- Als nächstes erscheinen die __zwei Kategorienamen__ in der oberen linken und rechten Seite des Bildschirms.
- Der zu kategorisierende __Stimulus__ erscheint in der Mitte
- Teilnehmer geben mit einem __Tastendruck__ an, ob der Stimulus der Kategorie links oder rechts angehört
- Die Variablen des aktuellen Versuchs werden __protokolliert__

%--
figure:
 id: TrialSequence
 source: trial_sequence.png
 caption: |
  Schematische Darstellung einer typischen Versuchsabfolge des (ersten Blocks der) IAT.
--%

## OpenSesame starten

Wenn Sie OpenSesame starten, sehen Sie eine Registerkarte "Get started!", die Ihnen eine Liste von Vorlagen sowie zuletzt geöffnete Experimente zeigt (%GetStarted). Um Zeit zu sparen, verwenden wir die "Erweiterte Vorlage".

%--
figure:
 id: GetStarted
 source: get-started.png
 caption: |
  Willkommensfenster von OpenSesame. Hier verwenden wir die "Erweiterte Vorlage".
--%

Nachdem Sie die erweiterte Vorlage geöffnet haben, speichern Sie Ihr Experiment. Klicken Sie dazu auf *Datei* -> *Speichern* (Tastenkombination: `Strg+S`), navigieren Sie zum entsprechenden Ordner und geben Sie Ihrem Experiment einen aussagekräftigen Namen.


## Übersichtsbereich

Der *Übersichtsbereich* zeigt die hierarchische Struktur unseres Experiments an. Um unsere Struktur zu vereinfachen, beginnen wir damit, den Übungsblock zu löschen. Gehen Sie wie folgt vor:

- Klicken Sie mit der rechten Maustaste auf das Element namens *Übungsloop*
- Klicken Sie auf "Löschen" (Tastenkürzel: `Entf`)
- Machen Sie dasselbe für das Element *end_of_practice*

Der Übersichtsbereich Ihres Experiments sollte jetzt so aussehen:

%--
Abbildung:
 id: Übersicht
 Quelle: overview.png
 Bildunterschrift: |
  Der Übersichtsbereich Ihres Experiments.
--%

## Block 1: Wortkategorisierung

### Schritt 1: Modifiziere die Blockschleife

Wir beginnen mit der Erstellung des ersten Blocks des IAT (Block 1 in %Task), in dem die Teilnehmer Wörter als entweder positiv oder negativ kategorisieren müssen. Da wir mehr als einen Block erstellen werden, ist der Name *block_loop* nicht sehr aussagekräftig. Also benennen wir ihn um:

- Klicken Sie mit der rechten Maustaste auf das Element *block_loop*, wählen Sie Umbenennen (Tastenkürzel: `F2`) und nennen Sie es *words_block_loop*

Als Nächstes möchten wir die folgenden drei Variablen im *block_loop item* definieren:

- __stimulus__ -- Das zu kategorisierende Wort
- __category__ -- Die Kategorie, zu der das Wort gehört
- __correct_response__ -- Die Antwort, die die Teilnehmer geben sollen

Um diese Variablen zu erstellen:

- Öffnen Sie den Tab des *words_block_loop*, indem Sie darauf im Übersichtsbereich klicken
- Sie sehen zunächst eine leere Tabelle
- Doppelklicken Sie auf die Überschrift der ersten Spalte (zunächst 'empty_column') und nennen Sie sie 'stimulus'
- Füllen Sie die erste Spalte mit sechs positiven und sechs negativen Wörtern, eins pro Zeile
- Erstellen Sie eine zweite Spalte mit der Überschrift 'category' und geben Sie an, zu welcher Kategorie (*POSITIV* oder *NEGATIV*) jedes Stimulus gehört
- Erstellen Sie eine dritte Spalte, nennen Sie sie *correct_response* und geben Sie die korrekte Antwort für jedes Stimulus an
- Um die Antwortregel festzulegen, sagen wir, dass:
    - Das Wort *POSITIV* wird auf der linken Seite des Bildschirms erscheinen, während das Wort *NEGATIV* auf der rechten Seite erscheint
    - Um anzuzeigen, dass ein Wort zur linken Seite gehört, müssen die Teilnehmer 'e' drücken, während sie für die rechte Seite 'i' drücken müssen.

<div class='info-box' markdown='1'>

__Tipp__ -- *correct_response* ist eine integrierte Variable, die es OpenSesame ermöglicht, die Leistung der Teilnehmer zu verfolgen, wie z.B. 'acc' (für Genauigkeit oder Prozentsatz der korrekten Antworten).

</div>

Der Inhalt Ihres *words_block_loop* sollte jetzt in etwa so aussehen:

%--
Abbildung:
 id: Überblick
 Quelle: words_block_loop.png
 Bildunterschrift: |
  Die Schleifentabelle des ersten Blocks des IAT enthält die drei experimentellen Variablen und ihre Werte.
--%

### Schritt 2: Ändern der Versuchssequenz

Wie in %TrialSequence gezeigt, möchten wir bei jedem Versuch:

1. Einen Fixationspunkt anzeigen
2. Das Stimulus in der Mitte und die beiden Kategorien auf beiden oberen Seiten des Bildschirms anzeigen
3. Eine Tastendruckreaktion erfassen
4. Die Variablen in die Ausgabedatei speichern

Diese vier Schritte nennt man *events*, und wir werden sie mit *items* in der *trial sequence* verwirklichen. Aber zuerst, weil die Versuchssequenz für jeden Block des Experiments leicht unterschiedlich sein wird (siehe %Task), nennen wir sie in *words_trial_sequence* um.

Für die ersten beiden Events verwenden wir `sketchpad`-Elemente. Die fortgeschrittene Vorlage enthält bereits ein Sketchpad-Element. Um ein zweites hinzuzufügen:

- Greifen Sie ein `sketchpad`-Element aus der *item toolbar*
- Ziehen Sie es in die *words_trial_sequence*

%--
Video:
 Quelle: youtube
 Id: DragDrop
 Videoid: vvJewWTjlts
 width: 640
 height: 360
 Bildunterschrift: |
  Elemente per Drag & Drop hinzufügen.
--%

<div class='info-box' markdown='1'>

__Tipp__ -- Um ein bestimmtes Element *nach* einem anderen Element erscheinen zu lassen, lassen Sie es *auf* diesem anderen Element fallen.

</div>

Standardmäßig gibt OpenSesame seinen Elementen Namen wie *sketchpad*, *new_sketchpad*, und *new_sketchpad_1*. Da diese Namen nicht aussagekräftig sind, benennen wir die Elemente in etwas Bedeutungsvolleres um. Um dies zu tun:

- Klicken Sie mit der rechten Maustaste auf das Element im Überblicksbereich (Tastenkürzel: `F2`)
- Wählen Sie 'Umbenennen'
- Nennen Sie die beiden `sketchpad`-Elemente jeweils *fixation* und *word*

Die beiden letzten Ereignisse der Versuchssequenz (Erfassen der Antwort und Speichern der Daten) werden bereits durch das `keyboard_response`-Element und das `logger`-Element repräsentiert.

Ihr Übersichtsbereich sollte jetzt so aussehen:



%--
figure:
 id: OverviewWordBlock
 source: overview_words_block.png
 caption: |
  Neue Übersicht über (den ersten Teil von) dem Experiment.
--%


### Schritt 3: Ändern Sie die Elemente in der Versuchssequenz

#### Fixation

Der nächste Schritt besteht darin, den Elementen in der Versuchssequenz Inhalte hinzuzufügen. Wir beginnen mit der `sketchpad`, die den Fixationspunkt zu Beginn jedes Versuchs darstellt.

- Öffnen Sie die Registerkarte *fixation*, indem Sie darauf im Übersichtsbereich klicken. Da wir die "Erweiterte Vorlage" gewählt haben, hat OpenSesame bereits einen Fixationspunkt für uns erstellt. Das Einzige, was wir ändern müssen, ist, wie lange der Fixationspunkt auf dem Bildschirm bleiben soll
- Klicken Sie auf das "Duration"-Feld, und ändern Sie den Wert auf 500


#### Wort

__Zeichnen Sie die Kategorienamen__

Nachdem der Fixationspunkt verschwindet, möchten wir die beiden Kategorienamen in der oberen linken und rechten Seite des Bildschirms anzeigen (siehe %TrialSequence). Gehen Sie dazu folgendermaßen vor:

- Öffnen Sie die Registerkarte *word*, indem Sie darauf im Übersichtsbereich klicken
- Wählen Sie das Element `Draw textline` aus der schwarz-weißen Symbolleiste
- Klicken Sie irgendwo im oberen linken Quadranten des Sketchpad
- Geben Sie 'POSITIVE' ein
- Wiederholen Sie dieses Verfahren, um das Wort 'NEGATIVE' auf der gegenüberliegenden Seite erscheinen zu lassen

__Zeichnen Sie den Reiz__

Als Nächstes möchten wir den zu kategorisierenden Reiz in der Mitte des Bildschirms anzeigen. Wichtig ist, dass der Reiz _*variabel*_ ist. Das bedeutet, welches Wort gezeigt wird, hängt davon ab, welche Zeile aus der *words_block_loop* gerade ausgeführt wird. Um OpenSesame zu ermöglichen, den Wert der Wort-Variable in der Blockschleife zu finden, verwenden wir die *eckige-Klammer-Syntax*. Gehen Sie dazu folgendermaßen vor:

- Wählen Sie das `draw textline`-Element des Sketchpads
- Klicken Sie auf die Mitte des Bildschirms
- Geben Sie ein:

~~~ .python
[stimulus]
~~~


<div class='info-box' markdown='1'>

__Tipp__ -- Das Wort, das Sie in Klammern eingeben, sollte genau der Spaltenüberschrift entsprechen, die Sie in der *word_block_loop* erstellt haben.

</div>

Diese Methode ist sehr praktisch, weil sie es vermeidet, separate Sketchpads für jedes positive und negative Wort erstellen zu müssen.

__Ändern Sie die Dauer__

Schließlich ändern wir die Dauer des aktuellen Sketchpads auf 0. Das bedeutet nicht, dass das aktuelle Sketchpad nur 0 ms angezeigt wird. Stattdessen wird es aufgrund des direkt danach folgenden `keyboard_response`-Elements auf dem Bildschirm bleiben, bis der Teilnehmer eine Taste drückt.

Ihr Sketchpad sollte jetzt so aussehen:

%--
figure:
 id: SketchpadWord
 source: sketchpad-word.png
 caption: |
  Das `sketchpad`-Element, das zum Zeichnen der Kategorienamen und des Reizes auf dem Bildschirm verwendet wird.
--%


Es ist eine gute Praxis, Ihr Experiment häufig zu testen, um Fehler sofort zu erkennen und zu beheben. Testen Sie Ihr Experiment jetzt, indem Sie auf einen der drei "run"-Pfeile klicken.

<div class='info-box' markdown='1'>

__Tipp__ -- Wenn Sie einen schnellen Testlauf Ihres Experiments durchführen möchten, müssen Sie möglicherweise nicht alle Elemente eines gegebenen Blocks ausführen. Um die Anzahl der Versuche zu verkürzen, können Sie Folgendes tun:

- Öffnen Sie Ihre Blockschleifentabelle
- Ändern Sie den Wert im Feld "Repeat" auf etwas kleineres als 1,00 (z. B. 0,1)
- (Auf einigen Systemen werden Dezimalzahlen durch ein Komma anstelle eines Punkts angezeigt)
- In unserem Beispiel bedeutet dies, dass OpenSesame nur *eine* Zeile (zufällig ausgewählt) anstelle aller 12 ausführen wird
- Vergessen Sie nicht, "Repeat" auf 1,00 zurückzusetzen, wenn Sie mit dem Testen fertig sind

</div>


## Experimentelle Hierarchie

Das IAT enthält mehr Blöcke als der aktuelle. Es enthält auch einen Block, in dem Bilder von Gesichtern als jung oder alt kategorisiert werden müssen, und zwei Blöcke, die beide Aufgaben miteinander verbinden (siehe %Task). Das bedeutet, dass wir weitere drei Blöcke von Versuchen erstellen müssen, die jeweils ihre eigene Versuchssequenz enthalten. Die hierarchische Struktur des Experiments sieht daher wie folgt aus (und wenn wir mit der Programmierung fertig sind, sollte unser Übersichtsbereich diesem ähneln):

%--
Abbildung:
 ID: Hierarchie
 Quelle: hierarchy.png
 Bildunterschrift: |
  Die experimentelle Hierarchie des IAT.
--%

## Block 2: Gesichterkategorisierung

Konzentrieren wir uns zunächst auf die Aufgabe zur Gesichterkategorisierung. Genauer gesagt, werden wir

- Einen zusätzlichen Block-Loop und Versuchssequenz erstellen
- Wiederverwenden Sie alles, was wir aus dem vorherigen Teil des Experiments wiederverwenden können
- Fügen Sie neue Variablen und Ereignisse hinzu, die spezifisch für die Gesichterkategorisierungsaufgabe sind

### Schritt 4: Erstellen Sie einen zusätzlichen Block-Loop

- Greifen Sie ein `Loop`-Element aus der `Item Toolbar`
- Ziehen Sie es in den Übersichtsbereich
- Um den neuen Block nach dem ersten erscheinen zu lassen, ziehen Sie ihn *auf* das `words_block_loop`-Element (siehe %AppendLoopAndSequence)
- OpenSesame fragt Sie, ob Sie das aktuelle Element *in den* `words_block_loop` oder *danach* einfügen möchten. Wähle letzteres

<div class='info-box' markdown='1'>

__Tipp__ -- Wenn Sie den neuen Gegenstand versehentlich *in den* Block-Loop einfügen, können Sie dies immer rückgängig machen, indem Sie `Strg + Alt + Z` drücken.

</div>

- Geben Sie der neuen Schleife einen aussagekräftigen Namen, zum Beispiel *faces_block_loop*

### Schritt 5: Fügen Sie eine neue Versuchssequenz hinzu

Obwohl die Versuchssequenz der Gesichterkategorisierungsaufgabe einige Überschneidungen mit der Wortkategorisierungsaufgabe aufweist, sind sie nicht identisch. Daher können wir die zuvor erstellte Versuchssequenz nicht wiederverwenden.

Um einen neuen zu erstellen:

- Greifen Sie ein `Sequence`-Element aus der Item Toolbar
- Ziehen Sie es *in den* *faces_block_loop*
- Wählen Sie diesmal "Einfügen in" (siehe %AppendLoopAndSequence)
- Benennen Sie das Element in *faces_trial_sequence* um

%--
Video:
 Quelle: Youtube
 ID: AppendLoopAndSequence
 Videoid: PVcXdAN3rjM
 Breite: 640
 Höhe: 360
 Bildunterschrift: |
  Schritt 5 und 6: Block 2 und die zugehörige Versuchssequenz zum Experiment hinzufügen.
--%


### Schritt 6: Wählen Sie die Reiz-Gesichter

__Download der Gesichtsreize__

In der Gesichtsvariante der Aufgabe benötigen wir Bilder von sechs jungen und sechs alten Gesichtern. Um zu vermeiden, dass Geschlechterverzerrungen unsere Ergebnisse beeinflussen, erscheint es am besten, pro Kategorie eine gleiche Anzahl männlicher und weiblicher Gesichter zu verwenden (hier: drei).

Sie können ein Beispiel-Set von Stimuli (im JPG-Format) hier herunterladen:

- %static:attachments/iat/face-stimuli.zip%

In den meisten Webbrowsern können Sie mit der rechten Maustaste auf den Link klicken und 'Link speichern unter' oder eine ähnliche Option wählen. Nachdem Sie diese Dateien heruntergeladen haben (z.B. in Ihren Download-Ordner), können Sie sie entpacken.

__Fügen Sie die JPG-Dateien dem Datei-Pool hinzu__

- Wenn der Datei-Pool nicht bereits sichtbar ist (standardmäßig auf der rechten Seite des Fensters), klicken Sie auf die Schaltfläche "Datei-Pool anzeigen" in der Haupt-Toolleiste (Tastenkombination: `Strg + P`).
- Klicken Sie auf das Pluszeichen, um Dateien hinzuzufügen
- Navigieren Sie zu Ihrem Download-Ordner (oder wohin auch immer Sie den entpackten *face-stimuli*-Ordner gespeichert haben) und fügen Sie die 12 JPG-Dateien hinzu.

Der Datei-Pool sollte jetzt ähnlich aussehen wie %FacesBlockLoop

### Schritt 7: Inhalt der Loop-Tabelle

Genau wie im vorherigen Teil des Experiments (siehe Schritt 1) benötigen wir drei Spalten, um die experimentellen Variablen zu definieren: *stimulus*, *category* und *correct_response*. Der einzige Unterschied besteht darin, dass die Stimuli diesmal die JPG-Dateien sind, die wir gerade dem Datei-Pool hinzugefügt haben.

In Bezug auf die korrekte Antwort, sagen wir, dass:

- Die Kategorie *YOUNG* erscheint auf der linken Seite des Bildschirms, während die Kategorie *OLD* auf der rechten Seite erscheint.
- Die Antwortregel ist wie zuvor

Erstellen Sie die oben genannten Spalten und stellen Sie sicher, dass Ihr Block-Loop am Ende so aussieht:

%--
Abbildung:
 ID: FacesBlockLoop
 source: faces_block_loop.png
 caption: |
  Inhalt des Dateipools und der Loop-Tabelle, die dem Block 2 (Kategorisierung von Gesichtern) des IAT entsprechen.
--%

<div class='info-box' markdown='1'>

__Tipp__ -- Die Werte in der Spalte *stimulus* sollten genau den Namen der Dateien im Dateipool entsprechen. Andernfalls kann OpenSesame die JPGs später nicht finden, wenn wir darauf verweisen wollen.

</div>

### Schritt 8: Ändern der Versuchsreihenfolge

Im Moment ist unsere neue Versuchsreihenfolge noch leer. Wir müssen sie mit den folgenden Ereignissen füllen (siehe %TrialSequence):

1. Zeige einen Fixationspunkt für 500 ms
2. Zeigen Sie ein Bild eines Gesichts zusammen mit den beiden Kategorienamen (*ALT* und *JUNG*)
3. Erfassen einer Tastaturantwort
4. Schreibe alle Variablen in die Ausgabedatei

__Kopieren wiederverwendbarer Elemente__

Ereignisse 1, 3, und 4 sind identisch mit dem Wortteil des Experiments. Wir können daher die entsprechenden Elemente durch Kopieren wiederverwenden. Um dies zu tun:

- Klicke mit der rechten Maustaste auf *fixation* (als Teil der *words_trial_sequence*) im Übersichtsbereich
- Wählen Sie "kopieren (verknüpft)", weil wir eine weitere Instanz desselben Elements erstellen möchten
- Klicke mit der rechten Maustaste auf *faces_trial_sequence* (d.h., die neue Sequenz)
- Wähle "Einfügen"
- Wähle "Einfügen in ..."
- Wiederholen Sie dieses Verfahren für die Elemente *keyboard_response* und *logger* (siehe %LinkedCopies)


<div class='info-box' markdown='1'>

__Tipp__ -- Wenn die Reihenfolge der Elemente in der Sequenz falsch ist, können Sie dies durch Ziehen und Ablegen korrigieren

__Tipp__ -- Wenn Sie versehentlich eine Kopie an einer anderen Stelle im Übersichtsbereich abgelegt haben (d.h. außerhalb der zu bearbeitenden Versuchsreihenfolge), können Sie dies jederzeit durch Drücken von `Strg + Alt + Z` rückgängig machen.

</div>


%--
video:
 source: youtube
 id: LinkedCopies
 videoid: _vDGpPsSqIY
 width: 640
 height: 360
 caption: |
  Verwendung verknüpfter Kopien.
--%

### Schritt 9: Erstellen der Gesichtsanzeige

Schließlich müssen wir ein neues `sketchpad`-Element erstellen, um die Gesichtsreize anzuzeigen. Um dies zu tun:

- Nimm ein `sketchpad`-Element aus dem Übersichtsbereich
- Ziehe es in die *faces_trial_sequence*
- Stellen Sie sicher, dass es direkt nach dem Fixationspunkt erscheint
- Benenne das Element als *face*

Momentan sollte Ihr Übersichtsbereich so aussehen:


%--
Abbildung:
 ID: OverviewBlock1-2.png
 source: overview-area-with-face-block.png
 caption: |
  Übersichtsbereich nachdem alle Elemente zur *faces_trial_sequence* hinzugefügt wurden.
--%

### Schritt 10: Konfigurieren der Inhalte des Gesichter-Sketchpads

__Zeichnen Sie die Kategorienamen__

- Zeigen Sie wie zuvor die beiden Kategorien (hier: *JUNG* in der oberen linken und *ALT* in der oberen rechten Ecke) an, indem Sie das Element `Draw textline` verwenden
- Setzen Sie die Dauer des Sketchpads auf 0 ms

__Zeigen des Gesichtsreizes__

Als nächstes wollen wir ein Bild eines Gesichts in der Mitte des Bildschirms anzeigen. Wie zuvor ist der Reiz *variabel*, so dass welches Gesicht gezeigt wird, hängt von der Zeile in der Blockschleife ab, die derzeit ausgeführt wird. Daher verwenden wir wieder die `square-bracket-Syntax`. Aber zuerst:

- Wählen Sie das `Draw image`-Sketchpad-Element
- Klicken Sie auf die Mitte
- Wählen Sie eine der jpg-Dateien

Als nächstes möchten wir die jpg-Datei variabel statt statisch machen. Um dies zu tun, müssen wir eine kleine Anpassung am *Skript* des Sketchpad-Elements vornehmen:

- Klicken Sie auf die Schaltfläche "Ansicht auswählen" oben rechts auf der *face*-Registerkarte und wählen Sie "Skript anzeigen". Sie sehen nun das Skript, das dem Sketchpad entspricht, das wir gerade erstellt haben:

~~~ .python
set duration 0
set description "Displays stimuli"
draw image center=1 file="of1.jpg" scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text="JUNG<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text=ALT x=320 y=-192 z_index=0
~~~

- Das Einzige, was wir tun müssen, ist den String 'of1.jpg' durch `[stimulus]` zu ersetzen. Das bedeutet, dass OpenSesame die Variable `[stimulus]` (die alle JPG-Namen enthält) verwendet, um zu bestimmen, welches Bild angezeigt werden soll.


~~~ .python
set duration 0
set description "Zeigt Reize an"
draw image center=1 file=[stimulus] scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text="JUNG<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text=ALT x=320 y=-192 z_index=0
~~~

- Klicken Sie auf 'übernehmen und schließen'

Als Nächstes ist es an der Zeit, zu testen, ob Ihr Experiment bis zu diesem Punkt funktioniert.


## Die gemischten Blöcke

### Kongruente Zuordnung

Der dritte Block ist eine Mischung aus Block 1 und 2, so dass die Teilnehmer sowohl Wörter als auch Gesichter kategorisieren müssen. Die Zuordnung ist *kongruent*, so dass *POSITIVE* Wörter und *JUNGE* Gesichter eine Antwort mit der linken Hand erfordern, während *NEGATIVE* Wörter und *ALTE* Gesichter eine Antwort mit der rechten Hand erfordern (siehe %Task).

### Schritt 11: Erstellen einer dritten Blockschleife und Versuchssequenz

Um den dritten Block des IAT zu erstellen, müssen wir:

- Erstellen Sie eine neue Blockschleife (und benennen Sie sie in *congruent_block_loop* um) (vgl. Schritt 4)
- Erstellen Sie eine neue Versuchssequenz (innerhalb der neuen Blockschleife) und nennen Sie sie *congruent_trial_sequence* (vgl. Schritt 5).

Ihre experimentelle Übersicht sollte jetzt so aussehen (%OverviewWithCongruent):

%--
figure:
 id: OverviewWithCongruent
 source: overview_with_congruent_loop.png
 caption: |
  Experimentelle Übersicht nach dem Einfügen einer dritten Blockschleife und Versuchssequenz.
--%

### Schritt 12: Füllen der *congruent_block_loop*

Der Inhalt der Kongruent-Block-Schleife ähnelt sehr dem Wort- und dem Gesichts-Block-Schleife, enthält jedoch beide Arten von Reizen. Daher:

- Kopiere den Inhalt der *word_block_loop* in die congruent_block_loop. Dies wird Reihe 1 bis 12 einnehmen
- Machen Sie dasselbe für den Inhalt der *faces_block_loop*. Dies wird die Reihe 13 bis 24 einnehmen
- (Achten Sie darauf, dass Sie die Spaltenüberschriften nicht zweimal kopieren)

### Schritt 13: Füllen der *congruent_trial_sequence*

- Wie in Schritt 8, kopieren Sie die Elemente *fixation*, *keyboard_response* und *logger* in die neue Versuchssequenz
- Leider können wir keine Kopien der *word* Skizzenblock- und der *face* Skizzenblock verwenden, da wir *beide* Kategorien (d. H. POSITIVE vs NEGATIVE und JUNG vs ALT) auf der linken und rechten Seite des Bildschirms anzeigen möchten
- Daher fügen wir dem congruent_trial_sequence einen neuen `sketchpad`-Punkt hinzu und nennen ihn *congruent_stimulus*
- Stellen Sie sicher, dass der neue Skizzenblock direkt nach dem Fixationspunkt erscheint und vor dem `keyboard_response item`

Ihre experimentelle Übersicht sollte jetzt so aussehen (%OverviewWithCongruent):

%--
figure:
 id: OverviewWithCongruent
 source: overview_congruent_filled_in.png
 caption: |
  Experimentelle Übersicht nach dem Ausfüllen der Versuchssequenz des kongruenten Blocks.
--%

### Schritt 14: Anpassen des Inhalts des *congruent_sketchpad*

Öffnen Sie den Reiter des *congruent_stimulus* Sketchpads und ändern Sie dessen Dauer auf 0 statt "keypress".

__Kategorienamen__

- Stellen Sie sicher, dass beide Kategorienamen oben links und rechts auf dem Bildschirm erscheinen (siehe %Task). Verwenden Sie die folgende Zuordnung:
    - Die Kategorienamen *POSITIV* und *JUNG* erscheinen auf der linken Seite
    - *NEGATIV* und *ALT* erscheinen auf der rechten Seite

__Wort-Reize__

Zeichnen Sie den Wortreiz in der Mitte des Bildschirms auf die gleiche Weise wie für Block 1 (siehe Schritt 3). Verwenden Sie die `eckige-Klammer-Syntax`.

__Gesichtsreize__

Zeichnen Sie den Gesichtsreiz in der Mitte des Bildschirms auf die gleiche Weise wie für Block 2 (siehe Schritt 9). Fügen Sie hinzu

<div class='info-box' markdown='1'>

__Tipp__ -- Machen Sie sich keine Sorgen, wenn Ihr Skizzenblock unordentlich aussieht. Wir werden das in Kürze in Ordnung bringen.

</div>


## Schritt 15: Verwenden von Show-if-Anweisungen

Im gemischten Teil des Experiments möchten wir, dass OpenSesame bestimmt, ob es ein Gesicht oder ein Wort anzeigen soll. Wir können dies tun, indem wir *Show-if-Anweisungen* verwenden. Genauer gesagt, wollen wir, dass das stimulus_sketchpad:

- Zeigt ein Wort *nur*, wenn der Reiz ein Wort ist (d. h., wenn die aktuelle Zelle in der Spalte *Reiz* in der Blockschleife ein Wort ist)
- Zeigt ein Gesicht *nur*, wenn der Reiz ein Gesicht ist

Um dies zu erreichen:

- Fügen Sie eine Spalte zur *congruent_block_loop* hinzu und nennen Sie sie *stimulus_type*
- Geben Sie den Zellen den Wert "word" oder "face", abhängig vom Stimulus (siehe %CongrLoop)

%--
figur:
 ID: CongrLoop
 Ursprung: congruent_block_loop.png
 Beschriftung: |
  Inhalt der Blockschleife des kongruenten Teils des Experiments.
--%

Als nächstes, um den Inhalt des Skizzenblocks *abhängig* von den Werten in der neu erstellten Spalte zu gestalten:

- Wählen Sie den schwarzen Pfeil in der Elementleiste des Skizzenblocks
- Klicken Sie auf das Fragezeichen (was das `Draw image element` anzeigt, das für die Präsentation der JPG-Dateien zuständig ist)
- Klicken Sie auf das `Show if`-Feld, das zu diesem Element gehört und standardmäßig auf "immer" eingestellt ist
- Verwenden Sie die eckige-Klammer-Syntax, um anzugeben, dass dieser Teil des Skizzenblocks nur gezeichnet werden soll, wenn der aktuelle Versuch ein Gesichtsbild enthält, indem Sie eingeben:

~~~ .python
[stimulus_type] = face
~~~

%--
video:
 Quelle: youtube
 ID: RunIf
 videoid: jqGFefCmn1k
 Breite: 640
 Höhe: 360
 Bildunterschrift: |
  Verwendung einer Run-if-Anweisung in einem `sketchpad`-Element.
--%

- Tun Sie dasselbe für das `Draw text element`, das die Präsentation der geschriebenen Wörter steuert. Diesmal sollte die Show-if-Anweisung lauten

~~~ .python
[stimulus_type] = word
~~~

Testen Sie, ob die ersten drei Blöcke Ihres Experiments wie gewünscht funktionieren.

## Inkongruente Zuordnung

## Schritt 16: Erstellen Sie den inkongruenten Block des Experiments

### Aufgabe

Verwenden Sie, was Sie in den vorherigen Schritten gelernt haben, um den abschließenden, inkongruenten Teil des Experiments zu erstellen.

Einige Tipps:

- Geben Sie neuen Elementen (z.B. den neuen `loop`- und `sequence`-Elementen) aussagekräftige Namen (z.B. *incongruent_block_loop*, *incongruent_trial_sequence*)
- Kopieren Sie die Elemente, die für jeden Block identisch sind (d.h. den Fixpunkt, die Tastaturantwort und den Logger)
- Sie können das Stimulus-Skizzenblock nicht kopieren, da die Zuordnung der Kategorien (die oben links und rechts erscheinen) getauscht werden sollte, so dass:
    - Die linke Seite zeigt *POSITIV* und *ALT*
    - Die rechte Seite zeigt *NEGATIV* und *JUNG* (siehe %Task)
- Die Werte in der Spalte *correct_response* sollten entsprechend geändert werden

<div class='info-box' markdown='1'>

__Tipp__ Sie können eine *unverknüpfte* Kopie des *congruent_stimulus*-Skizzenblocks verwenden, um den *incongruent_stimulus*-Skizzenblock zu erstellen (der fast identisch ist, außer dass die Kategorienamen *OLD* und *YOUNG* vertauscht sind).

Im Gegensatz zu einer *verknüpften* Kopie sieht eine *unverknüpfte* Kopie zunächst identisch aus (mit Ausnahme ihres Namens), aber Sie können das Original bearbeiten, ohne die unverknüpfte Kopie zu beeinflussen, und umgekehrt.

</div>


## Extra-Aufgaben:

### Einfach: Fügen Sie eine Anweisungs- und Abschiedsbildschirm hinzu

- `sketchpad`- und `form_text_display`-Elemente können Text anzeigen
- Gute Anweisungen sind kurz und konkret

### Mittel: Geben Sie nach jedem Versuch Feedback

- Verwenden Sie die integrierte Variable *correct*, die
    - den Wert 1 hat, wenn der Teilnehmer korrekt geantwortet hat
    - den Wert 0 hat, wenn der Teilnehmer einen Fehler gemacht hat
- Eine einfache Möglichkeit, Feedback zu geben, besteht darin, nach einer falschen Antwort kurz einen roten Punkt und nach einer richtigen Antwort einen grünen Punkt zu präsentieren
- Verwenden Sie Show-if-Anweisungen
