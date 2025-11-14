title: Anfängertutorial: Blicklenkung
hash: 1bc0db6f02f63201f3d90855479f82e8a246736a8141fb744439c06fe8783002
locale: de
language: German

[TOC]


## Über OpenSesame

OpenSesame ist ein kostenloses Programm zur schnellen Entwicklung von Verhaltensexperimenten für Psychologie, kognitive Neurowissenschaften und experimentelle Ökonomie. Für Einsteiger:innen bietet OpenSesame eine umfassende grafische Point-and-Click-Oberfläche. Für fortgeschrittene Nutzer:innen unterstützt OpenSesame Python- und JavaScript-Skripting (dies wird in diesem Tutorial nicht behandelt).


## Über dieses Tutorial

Wir erstellen ein klassisches Gaze-Cuing-Experiment. Dies ist ein unterhaltsames und interessantes Paradigma, bei dem Menschen unweigerlich dem Blick einer dargestellten Person folgen.

Wir verwenden ausschließlich die grafische Oberfläche. Wir *programmieren nicht* mit Python oder JavaScript. (Dies wird in den fortgeschrittenen Tutorials behandelt.) Dieses Tutorial dauert etwa eine Stunde.


## Was du lernen wirst

Am Ende dieses Tutorials wirst du wissen, wie du:

- 💡 Eine Versuchsstruktur mit SEQUENCE- und LOOP-Items erstellst
- 💡 Ein vollfaktorielles Design mit unabhängigen Variablen in einer LOOP-Tabelle definierst
- 💡 Visuelle Reize mit SKETCHPAD-Items erstellst
- 💡 Antworten mit KEYBOARD_RESPONSE-Items erfasst
- 💡 Teilnehmer:innen mit FEEDBACK-Items Rückmeldungen gibst
- 💡 Texte mit FORM_TEXT_DISPLAY-Items anzeigst
- 💡 Variablen zur Definition deiner Reize verwendest
- 💡 Bedingte (run-if) Ausdrücke benutzt, um den Ablauf deines Experiments zu steuern
- 💡 Stimulusdateien im Datei-Pool organisierst
- 💡 Daten protokollierst


## Was du brauchst

**OpenSesame 4.1 oder neuer** mit allen installierten Updates. Wenn du eine Benachrichtigung über verfügbare Updates siehst, klicke auf „Updates installieren...“ und dann auf „Update-Skript ausführen“. Starte OpenSesame nach dem Update neu. Du kannst auch manuell aktualisieren, indem du folgenden Befehl in der OpenSesame-Konsole ausführst.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```


## Das Experiment

Wie bereits erwähnt, erstellen wir ein Gaze-Cuing-Experiment, das ursprünglich von [Friesen und Kingstone (1998)][references] entwickelt wurde. So funktioniert es:

1. Ein Gesicht erscheint in der Mitte des Bildschirms.
2. Das Gesicht blickt nach links oder rechts.
3. Ein Zielbuchstabe („F“ oder „H“) erscheint auf einer Seite.
4. Ein Ablenkungsbuchstabe („X“) erscheint auf der anderen Seite.
5. Die Teilnehmenden identifizieren den Zielbuchstaben so schnell wie möglich.

Das Experiment besteht aus einer Übungsphase und einer Experimentalphase. Nach jedem Block wird Feedback angezeigt. Nach falschen Antworten ertönt ein Ton.

Die interessante Entdeckung? Menschen sind schneller, wenn das Gesicht zum Ziel blickt, obwohl die Blickrichtung nicht vorhersagt, wo das Ziel erscheint. Das zeigt, dass wir Menschen automatisch Blicken folgen.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Das Gaze-Cuing-Paradigma [(Friesen und Kingstone, 1998)][references]. Dieses Beispiel zeigt einen **inkongruenten** Durchgang, da das Gesicht auf den Ablenker („X“) statt auf das Ziel („F“) blickt.
--%

%--
video:
 source: youtube
 id: DesignScreencast
 videoid: aWvibRH6D4E
 width: 640
 height: 360
 caption: |
  Experimentallogik und -design.
--%


## Schritt 1: Erstelle die Hauptsequenz

🎯 __Ziel:__ In diesem Schritt erstellen wir die Grundstruktur unseres Experiments: eine Übungsphase, in der die Teilnehmenden die Aufgabe üben können; eine Experimentalphase, in der wir Daten für die Analyse sammeln; sowie informative Bildschirme vor und nach diesen Phasen. Hier wird nur die Struktur erstellt. Die Details werden später umgesetzt.

Beim Start von OpenSesame erscheint die Registerkarte „Get started!“ (%FigGetStarted). Wähle „Standardvorlage“.

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  Das „Get started“-Panel beim Start von OpenSesame.
--%

Öffne die Haupt-SEQUENCE mit dem Namen *experiment*. Sie enthält standardmäßig zwei Items: einen Notizblock (*getting_started*) und ein SKETCHPAD (*welcome*).

<details class='info-box' markdown='1'>

<summary markdown='1'>Nützliche Tipps für dieses Tutorial</summary>

- Klicken Sie auf das Hilfe-Symbol im Tab eines beliebigen Elements, um kontextbezogene Hilfe zu erhalten.
- Speichern Sie häufig (Strg+S). Backups werden automatisch erstellt (Werkzeuge → Backup-Ordner öffnen).
- Gelöschte Elemente können aus „Nicht verwendete Elemente“ wiederhergestellt werden, sofern sie nicht endgültig gelöscht wurden (Shift+Entf).
- Siehe Abbildung unten für die Struktur, die wir aufbauen werden.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  Structure of the gaze-cuing experiment. Item types in bold, item names regular.
--%

</details>

Entfernen Sie die Standardelemente:

- Rechtsklick auf *getting_started* → Löschen
- Rechtsklick auf *welcome* → Löschen

Die *experiment*-SEQUENCE ist nun leer. Fügen Sie ein Formular für Anweisungen hinzu:

- Ziehen Sie ein FORM_TEXT_DISPLAY aus der Symbolleiste (Form) in *experiment*. Dies zeigt die Anweisungen am Anfang an (die tatsächlichen Anweisungen definieren wir im Schritt 12).

Fügen Sie eine LOOP mit einer SEQUENCE für die Übungsphase hinzu:

- Ziehen Sie eine LOOP in *experiment* (platzieren Sie diese nach dem Anweisungsformular).
- Ziehen Sie eine SEQUENCE in die LOOP und wählen Sie „In [Name des Loop-Elements] einfügen“.

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahren Sie mehr über die LOOP/ SEQUENCE Struktur</summary>

Oftmals wiederholen Sie eine Abfolge von Ereignissen, wie zum Beispiel einen Durchgang (trial). Dies wird typischerweise umgesetzt, indem man eine LOOP, die ein einzelnes Element wiederholt, mit einer SEQUENCE kombiniert, die mehrere Elemente der Reihe nach ablaufen lässt.

Beispiel: Eine *block_loop* enthält eine *trial_sequence*, die wiederum mehrere Elemente entsprechend einem Durchgang enthält. Zusammen bildet diese LOOP/SEQUENCE-Struktur einen einzelnen Block mit mehreren Durchgängen.

</details>

Fügen Sie ein Formular am Ende der Übung hinzu

- Ziehen Sie in *experiment* ein weiteres FORM_TEXT_DISPLAY und wählen Sie „Nach [Name des Übungsloops] einfügen“. Dies zeigt eine „Ende der Übung“-Nachricht an (Schritt 12).

Fügen Sie eine LOOP für die Experimentierphase hinzu, und verwenden Sie eine verknüpfte Kopie derselben SEQUENCE wie bei der Übungs-LOOP:

- Ziehen Sie eine LOOP und fügen Sie sie nach dem Formular „Ende der Übung“ ein.
- Wiederverwenden Sie die SEQUENCE, die Sie für die Übungs-LOOP erstellt haben:
  - Rechtsklick auf die bestehende SEQUENCE > Kopieren (verknüpft).
  - Rechtsklick auf die neue Experimentier-LOOP > Einfügen > „In [Experimentier-Loop] einfügen“.

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahren Sie mehr über verknüpfte vs. nicht-verknüpfte Kopien</summary>

Wenn dasselbe Element an mehreren Stellen vorkommt, handelt es sich um verknüpfte Kopien. Verknüpfte Kopien sind praktisch, weil Sie, wenn Sie das Element ändern möchten, dies nur einmal tun müssen.

Nicht-verknüpfte Kopien sind unabhängig voneinander, sodass Sie eine ändern können, ohne die andere zu beeinflussen.

Es ist gute Praxis, wann immer möglich verknüpfte Kopien zu verwenden!

</details>

Fügen Sie ein Abschiedsformular hinzu:

- Ziehen Sie ein FORM_TEXT_DISPLAY und fügen Sie es nach der Experimentier-LOOP ein.

Benennen Sie die Elemente zur besseren Übersichtlichkeit um:

- new_form_text_display → *instructions*
- new_loop → *practice_loop*
- new_sequence → *block_sequence* (verknüpfte Kopien werden automatisch aktualisiert)
- new_form_text_display_1 → *end_of_practice*
- new_loop_1 → *experimental_loop*
- new_form_text_display_2 → *end_of_experiment*

Benennen Sie das Experiment um:

- Klicken Sie in der Übersicht auf New experiment. Benennen Sie es um in „Tutorial: Gaze cuing“. Dann speichern (Strg+S).

%--
figure:
 id: FigStep_1
 source: step1.png
 caption: |
  Overview at the end of Step 1.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahren Sie mehr über die verschiedenen Elementtypen</summary>

- SEQUENZ: Führt Items der Reihe nach aus.
- WIEDERHOLUNG: Wiederholt ein anderes Item, oft eine SEQUENZ, und definiert unabhängige Variablen.
- SKETCHPAD: Präsentiert visuelle Stimuli. Wird im Voraus vorbereitet und ist daher für Stimuli geeignet, die eine genaue Zeitsteuerung erfordern.
- FEEDBACK: Präsentiert visuelle Stimuli. Wird nicht im Voraus vorbereitet und eignet sich daher für die Anzeige aktueller Inhalte, wie zum Beispiel Feedback zu den Antworten eines Teilnehmers.
- TASTATUR_ANTWORT: Erfasst eine einzelne Tastenanschlags-Antwort.
- SAMPLER: Spielt eine Audiodatei ab.
- LOGGER: Schreibt Daten in eine Datei.
- RESET_FEEDBACK: Setzt Feedback-Variablen zu Beginn eines Blocks zurück.
- FORM_TEXT_DISPLAY: Zeigt Text mithilfe eines Formularlayouts an.

</details>

## Schritt 2: Die Blocksequenz erstellen

🎯 __Ziel:__ In diesem Schritt fügen wir erneut Struktur zu unserem Experiment hinzu. Dieses Mal implementieren wir die Struktur für einen einzelnen Block von Durchgängen, der der *block_sequence* entspricht. Wir legen nur die Struktur fest. Details werden später implementiert.

Öffne *block_sequence* und füge die folgenden Items in dieser Reihenfolge hinzu:

- RESET_FEEDBACK (um die Feedback-Variablen am Anfang des Blocks zurückzusetzen)
- LOOP mit einer neuen SEQUENCE darin (um die eigentliche Schleife und Logik der Durchgänge zu steuern)
- FEEDBACK (um den Teilnehmern am Ende des Blocks Rückmeldung zu geben)

Umbenennen

- new_reset_feedback → *reset_feedback*
- new_loop → *block_loop*
- new_sequence → *trial_sequence*
- new_feedback → *feedback*

%--
figure:
 id: FigStep_2
 source: step2.png
 caption: |
  Übersicht am Ende von Schritt 2.
--%


## Schritt 3: Die Blockschleife mit unabhängigen Variablen füllen

🎯 __Ziel:__ In diesem Schritt definieren wir die unabhängigen Variablen (Bedingungen) unseres Experiments. Unser Experiment ist ein Beispiel für ein vollständig randomisiertes Design, das bedeutet, dass unabhängige Variablen von Durchgang zu Durchgang variiert werden.

Öffne *block_loop*. Klicke auf Full-factorial design. Definiere:

- `gaze_cue`: left, right
- `target_pos`: -300, 300 (x-Koordinate in Pixel; 0 = Mitte; negativ = links)
- `target_letter`: F, H

Das ergibt 2×2×2 = 8 Kombinationen. Wir müssen auch einige Variablen hinzufügen, die sich aus den obigen Variablen ableiten. Dazu musst du manuell für jede Variable eine Spalte hinzufügen und die korrekten Werte in jede Zelle eintragen.

- `dist_pos`: Setze für jede Zeile 300, wenn `target_pos` -300 ist, und -300, wenn `target_pos` 300 ist
- `correct_response`: z für F, m für H
- `congruency`: kongruent, wenn der Blickhinweis in die Richtung des Ziels schaut, und inkongruent sonst

Stelle sicher, dass die LOOP-Tabelle aus 8 Zeilen besteht. Setze dann Wiederholen auf 3, damit wir am Ende 3 × 8 = 24 Durchgänge pro Block erhalten.

%--
figure:
 id: FigStep_3
 source: step3.png
 caption: |
  Die *block_loop* am Ende von Schritt 3.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahre mehr über die LOOP-Tabelle</summary>

- Du kannst eine Tabelle aus einer Tabellenkalkulation kopieren und einfügen oder eine .csv/ .xlsx-Datei laden, indem du die Quelle auf Datei setzt.
- Wiederholen kann eine Dezimalzahl sein. Wenn du Wiederholen beispielsweise auf 0,5 setzt, werden nur die Hälfte der Zeilen ausgeführt, zufällig ausgewählt.

</details>


## Schritt 4: Bilder und Audiodateien zum Dateipool hinzufügen

🎯 __Ziel:__ In diesem Schritt verwenden wir den Dateipool, um Stimulusdateien (Bilder und eine Audiodatei) mit dem Experiment zu bündeln.

Lade die folgenden Dateien herunter:

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Öffne den Dateipool (Strg+P) und ziehe die Dateien hinein. Oder benutze die + Taste, um sie hinzuzufügen. Der Dateipool wird automatisch mit deinem Experiment gebündelt.

%--
figure:
 id: FigStep_4
 source: step4.png
 caption: |
  Dateipool am Ende von Schritt 4.
--%

## Schritt 5: Die Versuchssequenz mit Items füllen

🎯 __Ziel:__ In diesem Schritt definieren wir die Versuchssequenz. Für den Moment fügen wir nur die notwendigen Items hinzu, ohne sie zu definieren. Das holen wir später nach.

Ein Durchgang besteht aus:

1. Fixationspunkt — 750 ms — SKETCHPAD  
2. Neutraler Blick — 750 ms — SKETCHPAD  
3. Blickhinweis — 500 ms — SKETCHPAD  
4. Zielreiz — 0 ms — SKETCHPAD (die 0 ms Dauer ermöglicht es dem Experiment, sofort zur Antwortabfrage weiterzugehen)  
5. Antwortabfrage — KEYBOARD_RESPONSE  
6. Fehler-Sound — SAMPLER (wird nur bei falscher Antwort ausgeführt)  
7. Log — LOGGER  

Öffne *trial_sequence* und die Items in der oben angegebenen Reihenfolge. Wenn du fertig bist, benenne sie um:

- *new_sketchpad* → *fixation_dot*
- *new_sketchpad_1* → *neutral_gaze*
- *new_sketchpad_2* → *gaze_cue*
- *new_sketchpad_3* → *target*
- *new_keyboard_response* → *keyboard_response*
- *new_sampler* → *incorrect_sound*
- *new_logger* → *logger*

Setze in *trial_sequence* den Run-if für *incorrect_sound* auf: `correct == 0`. Es ist wichtig, ein doppeltes Gleichheitszeichen (`==`) zu verwenden, das prüft, ob zwei Werte identisch sind – in diesem Fall, ob `correct` gleich 0 ist. (Wenn du versehentlich ein einzelnes Gleichheitszeichen benutzt, `correct = 1`, erhältst du beim Ausführen des Experiments einen `SyntaxError`.)

%--
figure:
 id: FigStep_5
 source: step5.png
 caption: |
  *trial_sequence* am Ende von Schritt 5.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Mehr über Variablen und Run-if-Ausdrücke erfahren</summary>

Variablen und bedingte (Run-if-)Ausdrücke sind leistungsfähig! Siehe %link:manual/variables%

</details>


## Schritt 6: Die Sketchpad-Items zeichnen

🎯 __Ziel:__ In diesem Schritt definieren wir die vier SKETCHPAD-Items der Versuchsequenz: Fixationspunkt, neutraler Blick (schaut geradeaus), Blickhinweis (schaut nach links oder rechts) und Zielanzeige (zwei Buchstaben auf jeder Seite des Blickhinweises, welcher weiterhin nach links oder rechts schaut).

Lege die Hintergrundfarbe des Experiments auf Weiß und die Vordergrundfarbe auf Schwarz fest:

- Klicke auf den Experimenttitel, um die allgemeinen Eigenschaften zu öffnen
- Ändere Background zu 'white' und Foreground zu 'black'

Definiere den Fixationspunkt:

- Öffne *fixation_dot*
- Wähle das Fixationspunkt-Element aus. Dies ist das Fixationspunkt-Symbol in der vertikalen Werkzeugleiste links der Zeichenfläche.
- Zeichne einen Fixationspunkt im Zentrum der Anzeige (0, 0)
- Setze die Dauer auf 745 ms. Dies wird auf die gewünschte Dauer von 750 ms aufgerundet.

<details class='info-box' markdown='1'>

<summary markdown='1'>Warum eine Dauer von 745 ms angeben, wenn eine Anzeige für 750 ms gezeigt werden soll?</summary>

Anzeigen werden periodisch aktualisiert. Auf einem 60-Hz-Monitor dauert ein Aktualisierungszyklus 1000 / 60 = 16,67 ms. Das bedeutet, dass auf einem 60-Hz-Monitor die Dauer einer Anzeige zwangsläufig ein Vielfaches von 16,67 ist.

745 ist *kein* Vielfaches von 16,67. Deshalb wird die Dauer auf das nächste Vielfache von 16,67 aufgerundet, also 750.

Weitere Informationen findest du unter:

- %link:timing%

</details>

Definiere die neutrale Blickanzeige:

- Öffne *neutral_gaze*
- Wähle das Bildelement aus
- Platziere ein Bild im Zentrum der Anzeige und wähle `gaze_neutral.png` im erscheinenden Datei-Pool-Dialog aus
- Setze die Dauer auf 745 ms

Definiere die Blickhinweisanzeige:

- Öffne *gaze_cue*
- Zeichne `gaze_left.png` im Zentrum der Anzeige

Natürlich soll nicht immer `gaze_left.png` angezeigt werden. Stattdessen soll `gaze_left.png` angezeigt werden, wenn die Variable `gaze_cue` "left" ist, und `gaze_right.png`, wenn die Variable `gaze_cue` "right" ist. Mit anderen Worten: Es soll `gaze_{gaze_cue}.png` angezeigt werden, wobei die geschweiften Klammern angeben, dass eine Variable eingefügt werden soll.

Dies können wir im Item-Skript angeben. Klicke Select view (das mittlere der drei Symbole oben rechts) → View script. Dadurch wird das sogenannte OpenSesame-Skript angezeigt, das das Item definiert. (Dies ist kein Python oder JavaScript!) Ändere den `draw image`-Befehl wie unten angegeben. Dabei kannst du auch die Dauer angeben (denk daran, dass 495 ms, wie oben erklärt, auf 500 ms aufgerundet werden):

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Klicken Sie auf Übernehmen. Die Ansicht wechselt nun zurück zur Ansicht mit grafischen Steuerelementen. Das Bild erscheint jetzt als Fragezeichen. Keine Sorge! Das korrekte Bild wird während des Experiments angezeigt.

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahren Sie mehr über die Variablen, die in Ihrem Experiment existieren</summary>

Öffnen Sie den Variableninspektor (Strg+I), um zu sehen, welche Variablen in Ihrem Experiment existieren. Während das Experiment läuft, können Sie sogar sehen, wie sich ihre Werte in Echtzeit ändern!

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: |
  Der Variableninspektor.
--%

</details>

Definieren Sie die Zielanzeige:

- Öffnen Sie *target*
- Zeichnen Sie `gaze_left.png` in die Mitte der Anzeige.
- Wählen Sie das Textelement “textline” aus
- Zeichnen Sie "{target_letter}" irgendwo auf die linke Seite der Anzeige. Die genauen Koordinaten sind egal, da wir später eine Variable dafür verwenden werden. Wie zuvor zeigen die geschweiften Klammern an, dass die Variable `target_letter` eingefügt werden soll.
- Zeichnen Sie "X" irgendwo auf die rechte Seite der Anzeige

Bearbeiten Sie das Item-Skript (Ansicht auswählen → Skript anzeigen). Wie zuvor sollte der Blickhinweis (gaze cue) von der Variable `gaze_cue` abhängen. Zusätzlich sollte die X-Koordinate des Zielbuchstabens (“target letter”) von der Variable `target_pos` abhängen und die X-Koordinate des "X" von der Variable `dist_pos`.

Wichtig: Wir setzen die Dauer auf 0. Das bedeutet nicht, dass das Ziel 0 ms lang angezeigt wird, sondern dass das Experiment sofort zum nächsten Item weitergeht, das ein KEYBOARD_RESPONSE ist. Anders gesagt: Die Antwortaufnahme beginnt, sobald das Ziel erscheint!

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x="{target_pos}" y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="X" x="{dist_pos}" y=0 z_index=0
~~~

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahren Sie mehr über die Verwendung komplexer Variablenausdrücke im OpenSesame-Skript</summary>

Im OpenSesame-Skript können Sie komplexe Ausdrücke mit geschweiften Klammern einbinden. Anstatt zum Beispiel `x="{dist_pos}"` für das "X" anzugeben, könnten wir auch `x="{-1 * target_pos}"` verwenden. Dies nutzt Pythons [formatierte Zeichenkettenliterale](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).

</details>


## Schritt 7: Konfigurieren Sie das keyboard_response-Item

🎯 __Ziel:__ In diesem Schritt konfigurieren wir, welche Tasten die Teilnehmenden zur Antwort nutzen können und wie lange sie Zeit haben.

Öffnen Sie *keyboard_response*:

- Lassen Sie “Korrekte Antwort” leer. Die Variable `correct_response` (aus Schritt 3) wird standardmäßig verwendet.
- Setzen Sie “Erlaubte Antworten” auf `z;m`
- Setzen Sie “Timeout” auf `2000` ms
- Lassen Sie “Ereignis-Typ” auf keypress

%--
figure:
 id: FigStep_7
 source: step7.png
 caption: |
  KEYBOARD_RESPONSE am Ende von Schritt 7.
--%


## Schritt 8: Konfigurieren Sie den sampler

🎯 __Ziel:__ In diesem Schritt legen wir fest, welcher Ton nach einer falschen Antwort abgespielt werden soll.

Öffnen Sie *incorrect_sound*. Klicken Sie auf „Durchsuchen” und wählen Sie `incorrect.ogg` aus dem Datei-Pool aus.

%--
figure:
 id: FigStep_8
 source: step8.png
 caption: |
  *incorrect_sound* am Ende von Schritt 8.
--%


## Schritt 9: Konfigurieren Sie den logger

🎯 __Ziel:__ In diesem Schritt überprüfen wir, wie die Daten protokolliert werden.

Öffnen Sie *logger*. Standardmäßig ist „Automatisch alle Variablen protokollieren” aktiviert. Das ist eine gute Vorgehensweise, deshalb müssen wir hier nichts ändern!

<details class='info-box' markdown='1'>

<summary markdown='1'>Erfahren Sie mehr über individuelles Logging</summary>

Sie können auch bestimmte Variablen ausschließen, die nicht protokolliert werden sollen. Sie können außerdem das automatische Logging komplett deaktivieren und manuell spezifische Variablen auswählen, die protokolliert werden sollen. Dies hilft dabei, die Logdateien übersichtlich zu halten. Überprüfen Sie jedoch immer sorgfältig, dass alle benötigten Variablen tatsächlich protokolliert werden!

</details>

## Schritt 10: Zeichnen Sie das Feedback-Element

🎯 __Ziel:__ In diesem Schritt definieren wir das Feedback, das die Teilnehmer:innen am Ende jedes Blocks zu ihrer Leistung erhalten.

Öffnen Sie *feedback*. Lassen Sie die Dauer auf 'keypress'. Fügen Sie folgenden Feedback-Text hinzu:

```text
Ende des Blocks

Ihre durchschnittliche Reaktionszeit war {avg_rt} ms
Ihre Genauigkeit betrug {acc} %

Drücken Sie eine beliebige Taste, um fortzufahren
```

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: |
  *feedback* am Ende von Schritt 10.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Mehr über Feedback-Variablen erfahren</summary>

OpenSesame verfolgt Feedback-Variablen automatisch:

- `response` ist der Wert der letzten Antwort. Beispiele: "z", "left" usw.
- `correct` ist 1 nach einer richtigen Antwort und 0 nach einer falschen Antwort
- `response_time` ist die Reaktionszeit (in Millisekunden) der letzten Antwort
- `acc` ist der Prozentsatz richtiger Antworten, seit die Feedback-Variablen zurückgesetzt wurden, in diesem Fall durch das RESET_FEEDBACK-Element am Beginn des Blocks
- `avg_rt` ist die durchschnittliche Reaktionszeit, seit die Feedback-Variablen zurückgesetzt wurden

Siehe auch:

- %link:manual/variables%

</details>

## Schritt 11: Legen Sie die Anzahl der Blöcke für die Übungs- und Experimentalphase fest

🎯 __Ziel:__ In diesem Schritt geben wir die Anzahl der Durchgangsblöcke in der Übungs- und Experimentalphase an.

Öffnen Sie *practice_loop* und setzen Sie Wiederholen auf 2, sodass wir zwei Übungsblöcke haben. Fügen Sie außerdem eine practice-Variable zur Schleifen-Tabelle hinzu und setzen Sie diese auf 'yes'. Dies ist praktisch, da Sie bei der Datenanalyse leicht erkennen können, welche Durchgänge Teil der Übungsphase waren.

Öffnen Sie *experimental_loop* und setzen Sie Wiederholen auf 8. Fügen Sie ebenfalls eine practice-Variable hinzu, setzen Sie diese diesmal aber auf 'no'.


## Schritt 12: Schreiben Sie die Anweisung, *end_of_practice* und *end_of_experiment* Formulare

🎯 __Ziel:__ In diesem Schritt fügen wir informative Anweisungen an verschiedenen Stellen im Experiment hinzu.

Öffnen Sie die drei FORM_TEXT_DISPLAY-Elemente und geben Sie kurze, klare Instruktionen ein. Gute Anleitungen sind einfach, vollständig und spezifisch!


## Schritt 13: Führen Sie das Experiment durch!

🎯 __Ziel:__ In diesem Schritt führen wir einen ersten Testlauf des Experiments durch!

Der doppelte blaue Pfeil in der Symbolleiste ist die Quick run (Strg+Shift+W) Schaltfläche. Damit wird das Experiment in einem Fenster mit einer Dummy-Versuchsnummer und einem Logfile-Pfad gestartet. Dies ist hauptsächlich während der Entwicklung nützlich.

Der einzelne grüne Pfeil ist die Run fullscreen (Strg+R) Schaltfläche. Hier werden Sie zuerst nach einer Versuchsnummer und einem Logfile gefragt und ob Sie das Experiment im Vollbild- oder Fenstermodus starten wollen. Diese Funktion ist hauptsächlich für die Datenerhebung gedacht.

Drücken Sie eine der beiden Schaltflächen, um Ihr Experiment zu testen!

🏁 Wenn das Experiment läuft, sind Sie fertig! Aber bevor Sie aufhören, besprechen wir noch zwei weitere wichtige Punkte bezüglich Debugging und Backend-Auswahl:


## Effektives Debugging und Verständnis von Fehlern

Fehler beim Erstellen von Experimenten sind normal. Lesen Sie Fehlermeldungen sorgfältig und versuchen Sie, sie zu verstehen. Das ist der einzig wahre Weg zum effektiven Debugging!

%FigErrorMessage zeigt eine Beispiel-Fehlermeldung:

- Der Fehlertyp ist `FStringError`
- Die Beschreibung gibt an: „Failed to evaluate f-string expression in the following text: `gaze_{gaze_ceu}.png`”
- Der Fehler ist in der Prepare-Phase der *gaze_cue*-Elemente aufgetreten
- Das Traceback ist eine Python-Fehlermeldung. Sie ist eine technischere Version der obigen Beschreibung.

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: |
  Eine Fehlermeldung in OpenSesame.
--%

Sobald du verstanden hast, woher der Fehler kommt, kannst du versuchen, ihn zu beheben. In diesem Beispiel resultiert der Fehler aus einem Tippfehler bei der Definition des *gaze_cue*-Items in Schritt 6. `gaze_{gaze_ceu}.png` sollte `gaze_{gaze_cue}.png` sein. Leicht behoben!

<details class='info-box' markdown='1'>

<summary markdown='1'>Mehr über effektives Debugging erfahren</summary>

Effektives Debugging ist eine wichtige Fähigkeit. Wenn du sie beherrschst, sparst du viel Zeit und Frustration! Unter dem folgenden Link findest du Tipps:

- %link:manual/debugging%

</details>

## Timing und Backend-Auswahl

Im Tab 'Allgemeine Eigenschaften' (der Tab, den du öffnest, indem du auf den Namen des Experiments klickst), kannst du ein Backend auswählen. Das Backend ist die Softwareschicht, die die Anzeige, Eingabegeräte, Ton usw. steuert. Die meisten Experimente funktionieren mit allen Backends, aber es gibt Gründe, eines gegenüber dem anderen zu bevorzugen, meist im Zusammenhang mit dem Timing. Derzeit gibt es vier Backends:

- __psycho__ ist der Standard. Es basiert auf PsychoPy und bietet ein exzellentes Timing [(Peirce, 2007)][references].
- xpyriment — basiert auf Expyriment und bietet ebenfalls ein exzellentes Timing [(Krause & Lindemann, 2013)][references]
- legacy — ist eine Fallback-Option, die auf mehr Systemen funktioniert, aber weniger präzises Timing bietet
- osweb — führt Experimente im Browser aus [(Mathôt & March, 2022)][references]

Siehe auch:

- %link:backends%
- %link:timing%

## Wichtigste Erkenntnisse

Du hast gelernt, wie man ein einfaches, aber vollständiges Experiment erstellt!

- ✅ Die Struktur eines Experiments wird üblicherweise durch die Kombination von SEQUENCE- und LOOP-Items erstellt
- ✅ Variablen werden üblicherweise in der LOOP-Tabelle definiert
- ✅ Zeitkritische visuelle Stimuli werden üblicherweise mit einem SKETCHPAD präsentiert
- ✅ Rückmeldungen für Teilnehmende werden üblicherweise mit FEEDBACK-Items präsentiert
- ✅ Das FORM_TEXT_DISPLAY ist praktisch, um Text anzuzeigen
- ✅ Variablen und Ausdrücke können mit geschweiften Klammern eingefügt werden. Beispiel: `{gaze_cue}`
- ✅ Run-if-Ausdrücke werden in einer SEQUENCE definiert und bestimmen, welche Items tatsächlich ausgeführt werden: Beispiel: `correct == 0`
- ✅ Überprüfe immer das Timing und die Logdateien mit einem umfassenden Testrun, bevor du Daten sammelst

## Nächste Schritte

Du hast nun ein grundlegendes Verständnis von OpenSesame. Das reicht aus, um viele einfache Experimente zu erstellen. Möglicherweise möchtest oder musst du jedoch noch mehr lernen! Hier sind sinnvolle nächste Schritte:

- [Lerne, wie du zusammen mit SigmundAI Experimente erstellst](%url:beginner-sigmund%)
- [Lerne, wie du Python-Code in deinen Experimenten verwendest](%url:intermediate%)
- [Lerne, wie du JavaScript-Code in deinen Online-Experimenten einsetzt](%url:intermediate-javascript%)

## Literatur

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. Social Science Computer Review. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? Behavior Research Methods, 42, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. Psychonomic Bulletin & Review, 5, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. Behavior Research Methods. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. Behavior Research Methods, 44(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. Language Learning. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Zeitauflösung von Uhren: Auswirkungen auf die Messung der Reaktionszeit—Gute Nachrichten für schlechte Uhren. British Journal of Mathematical and Statistical Psychology, 42(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[referenzen]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about