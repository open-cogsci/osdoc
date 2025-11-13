title: Anfängertutorial: Blicklenkung
hash: 8b68f010d5f28f2e59818b6c6aac4308f317f2ced632ba0c36993b1e159c8432
locale: de
language: German

[TOC]

## Über OpenSesame

OpenSesame ist ein kostenloses Programm zur einfachen Entwicklung von Verhaltensexperimenten für Psychologie, Neurowissenschaften und experimentelle Wirtschaftswissenschaften. Für Anfänger bietet OpenSesame eine umfassende, grafische Point-and-Click-Oberfläche. Fortgeschrittene Nutzer können Python-Skripting nutzen (in diesem Tutorial nicht behandelt).


## Über dieses Tutorial

Dieses Tutorial zeigt, wie man ein einfaches, aber vollständiges psychologisches Experiment mit OpenSesame erstellt [(Mathôt, Schreij, & Theeuwes, 2012; Mathôt & March, 2022)][references]. Du wirst hauptsächlich die grafische Benutzeroberfläche von OpenSesame verwenden (d. h. kein Python Inline-Coding), obwohl du kleine Änderungen am OpenSesame-Skript vornimmst. Dieses Tutorial dauert ungefähr eine Stunde.

Dieses Tutorial setzt voraus, dass du OpenSesame 4.1 mit allen aktuellen Updates verwendest. Wenn eine Benachrichtigung erscheint, dass „Einige Pakete können aktualisiert werden (…)", klicke auf die Schaltfläche „Updates installieren …“, öffne das Update-Panel und führe durch Klick auf „Update-Skript ausführen“ die eigentlichen Updates durch. Starte OpenSesame nach dem Update neu.


## Das Experiment

In diesem Tutorial erstellst du ein Gaze-Cuing-Experiment, wie es von [Friesen und Kingstone (1998)][references] vorgestellt wurde. In diesem Experiment wird ein Gesicht in der Mitte des Bildschirms gezeigt (%FigGazeCuing). Das Gesicht blickt entweder nach rechts oder nach links. Ein Zielbuchstabe (ein „F“ oder ein „H“) wird links oder rechts neben dem Gesicht präsentiert. Ein Distraktor-Stimulus (der Buchstabe „X“) erscheint auf der anderen Seite des Gesichts. Die Aufgabe besteht darin, so schnell wie möglich anzugeben, ob der Zielbuchstabe ein „F“ oder ein „H“ ist. In der kongruenten Bedingung blickt das Gesicht zum Ziel. In der inkongruenten Bedingung blickt das Gesicht zum Distraktor. Wie du dir vielleicht denken kannst, ist das typische Ergebnis, dass Teilnehmer*innen in der kongruenten Bedingung schneller reagieren als in der inkongruenten Bedingung, obwohl die Blickrichtung nicht vorhersagt, wo das Ziel auftaucht. Dies zeigt, dass unsere Aufmerksamkeit automatisch durch den Blick anderer Menschen gelenkt wird – auch in Situationen, wo dies keinen erkennbaren Zweck erfüllt. (Und selbst dann, wenn das Gesicht nur ein Smiley ist!)

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Das Gaze-Cuing-Paradigma [(Friesen und Kingstone, 1998)][references], welches du in diesem Tutorial umsetzen wirst. Dieses Beispiel zeigt einen Durchgang in der inkongruenten Bedingung, weil der Smiley zum Distraktor („X“) und nicht zum Ziel („F“) blickt.
--%

Das Experiment besteht aus einer Übungs- und einer Experimentalphase. Nach jedem Block von Durchgängen wird visuelles Feedback gegeben. Nach jeder falschen Antwort ertönt ein Ton.

Das experimentelle Design:

- ist *innerhalb der Versuchspersonen* (within-subject), weil alle Teilnehmenden alle Bedingungen durchlaufen
- ist *vollständig gekreuzt* (oder faktoriell), da alle Kombinationen der Bedingungen auftreten
- hat drei Faktoren (oder Variablen):
    - *Blickrichtung* mit zwei Stufen (links, rechts)
    - *Zielseite* mit zwei Stufen (links, rechts)
    - *Zielbuchstabe* mit zwei Stufen (F, H)

Siehe %DesignScreencast für eine Erklärung der Logik und des Designs des Experiments:


%--
video:
 source: youtube
 id: DesignScreencast
 videoid: aWvibRH6D4E
 width: 640
 height: 360
 caption: |
  Eine Erklärung der experimentellen Logik und des Designs.
--%


## Schritt 1: Erstelle die Hauptsequenz

Wenn du OpenSesame startest, siehst du den Tab „Get started!“ (%FigGetStarted). Unter „Start a new experiment“ wird eine Liste von Vorlagen angezeigt. Diese Vorlagen bieten praktische Ausgangspunkte für neue Experimente. Nachdem du ein Experiment das erste Mal gespeichert hast, werden zuletzt geöffnete Experimente unter „Continue with a recent experiment“ angezeigt.

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  Das „Get started“-Panel beim Start von OpenSesame.
--%

Klicke auf „Default template“, um mit einer minimalen Experimentvorlage zu starten.

Standardmäßig gibt es eine Haupt-SEQUENCE, die einfach *experiment* genannt wird. Klicke auf *experiment* im Übersichtsbereich (standardmäßig auf der linken Seite, siehe %FigInterface), um die Steuerelemente im Tab-Bereich zu öffnen. Die *experiment* SEQUENCE besteht aus zwei Items: einem `notepad` namens *getting started* und einem SKETCHPAD namens *welcome*.

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Namen vs Typen__ -- Items in OpenSesame haben einen Namen und einen Typ. Der Name und der Typ können gleich sein, sind es aber meist nicht. Zum Beispiel kann ein SKETCHPAD-Item den Namen *my_target_sketchpad* haben. Um diesen Unterschied deutlich zu machen, verwenden wir `Monospace` für Item-Typen und *Kursivschrift* für Namen.

__Tipp__ -- Die 'Extended template' ist ein guter Ausgangspunkt für viele Experimente. Sie enthält bereits die Grundstruktur eines versuchsbasierenden Experiments.

__Tipp__ -- Du kannst auf die Hilfe-Icons oben rechts in einem Item-Tab klicken, um kontextsensitiv Hilfe zu erhalten.

__Tipp__ -- Speichere (Tastenkombination: `Strg+S`) dein Experiment häufig! Im unglücklichen (und unwahrscheinlichen) Fall eines Datenverlusts kannst du deine Arbeit oft aus den automatisch erstellten Back-ups (standardmäßig alle 10 Minuten, Menü → Werkzeuge → Backup-Ordner öffnen) wiederherstellen.

__Tipp__ -- Sofern du nicht 'Endgültig löschen' verwendet hast (Tastenkombination: `Shift+Entf`), sind gelöschte Items weiterhin im 'Unused items'-Ordner verfügbar, bis du 'Permanently delete unused items' im Tab 'Unused items' auswählst. Du kannst gelöschte Items wieder zu einer SEQUENCE hinzufügen, indem du sie aus dem 'Unused items'-Ordner heraus an eine andere Stelle im Experiment ziehst.

__Tipp__ -- %FigExperimentStructure zeigt schematisch den Aufbau des Experiments, das du erstellen wirst. Falls du während des Tutorials den Überblick verlierst, kannst du auf %FigExperimentStructure zurückgreifen, um zu sehen, wo du dich befindest.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  A schematic representation of the structure of the 'Gaze cuing' experiment. The item types are in bold face, item names in regular face.
--%

</div>

__Entferne unnötige Items__

Wir benötigen die beiden Items aus der Standardvorlage nicht. Entferne *getting_started*, indem du mit der rechten Maustaste darauf im Übersichtsbereich klickst und 'Löschen' wählst (Tastenkombination: `Entf`). Entferne *welcome* auf dieselbe Weise. Die *experiment* SEQUENCE ist jetzt leer.

__Füge ein form_text_display-Item zur Anzeige der Instruktion hinzu__

Wie der Name schon sagt, ist ein `form_text_display` ein Formular, das Text anzeigt. Wir werden ein `form_text_display` verwenden, um dem Teilnehmer zu Beginn des Experiments Instruktionen zu geben.

Klicke im Übersichtsbereich auf *experiment*, um die Steuerelemente im Tab-Bereich zu öffnen. Du siehst eine leere SEQUENCE. Ziehe ein `form_text_display` aus der Item-Werkzeugleiste (unter 'Form', siehe %FigInterface) auf die *experiment* SEQUENCE im Tab-Bereich. Wenn du loslässt, wird ein neues `form_text_display`-Item in die SEQUENCE eingefügt. (Hierzu mehr in Schritt 12.)

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ -- Du kannst Items sowohl in den Übersichtsbereich als auch in SEQUENCE-Tabs ziehen.

__Tipp__ -- Wenn eine Zieh-Aktion nicht eindeutig ist, erscheint ein Pop-up-Menü, das dich fragt, was du tun möchtest.

__Tipp__ -- Ein `form_text_display` zeigt nur Text an. Wenn du Bilder usw. benötigst, kannst du ein SKETCHPAD-Item verwenden. Wir werden das SKETCHPAD in Schritt 5 kennenlernen.

</div>

__Füge ein Loop-Item hinzu, das ein neues Sequence-Item für die Übungsphase enthält__

Wir müssen ein LOOP-Item zur *experiment* SEQUENCE hinzufügen. Wir werden diese LOOP für die Übungsphase des Experiments nutzen. Klicke auf die *experiment* SEQUENCE, um die Steuerelemente im Tab-Bereich zu öffnen.

Ziehe das LOOP-Element aus der Element-Werkzeugleiste in die SEQUENCE, genauso wie du zuvor das `form_text_display` hinzugefügt hast. Neue Elemente werden unterhalb des Elements eingefügt, auf das sie gezogen werden. Wenn du das neue LOOP also auf das zuvor erstellte `form_text_display` ziehst, erscheint es an der gewünschten Position: nach dem `form_text_display`. Aber mach dir keine Sorgen, falls du ein neues Element an die falsche Stelle ziehst, denn du kannst die Reihenfolge jederzeit später ändern.

Ein LOOP macht für sich genommen nichts. Ein LOOP benötigt immer ein weiteres Element, das ausgeführt wird. Deshalb musst du das neue LOOP-Element mit einem weiteren Element füllen. (Wenn du das Loop-Element ansiehst, siehst du auch eine Warnung: 'No item selected'.) Ziehe ein SEQUENCE-Element aus der Element-Werkzeugleiste auf das LOOP-Element. Ein Pop-up-Menü erscheint und fragt dich, ob du die SEQUENCE nach oder in das LOOP-Element einfügen möchtest. Wähle 'Insert into new_loop'. (Darauf kommen wir in Schritt 2 zurück.)

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Was ist ein LOOP-Element?__ -- Ein LOOP ist ein Element, das deinem Experiment Struktur verleiht. Es wiederholt ein anderes Element, typischerweise eine SEQUENCE. In einem LOOP definierst du üblicherweise auch deine unabhängigen Variablen, also jene Variablen, die du in deinem Experiment manipulierst.

__Was ist ein SEQUENCE-Element?__ -- Auch ein SEQUENCE-Element strukturiert dein Experiment. Wie der Name schon sagt, führt eine SEQUENCE mehrere andere Elemente nacheinander aus.

__Die LOOP-SEQUENCE-Struktur__ -- Oft möchtest du eine Abfolge von Ereignissen wiederholen. Dafür benötigst du ein LOOP-Element, das eine SEQUENCE enthält. Eine SEQUENCE allein wiederholt nicht. Sie beginnt einfach mit dem ersten Element und endet mit dem letzten. Durch das „Ummanteln“ einer SEQUENCE mit einem LOOP-Element kannst du die SEQUENCE mehrfach wiederholen. Zum Beispiel entspricht eine einzelne Versuchsdurchführung meistens einer einzelnen SEQUENCE, die *trial_sequence* heißt. Ein LOOP (häufig *block_loop* genannt) um diese *trial_sequence* stellt dann einen einzelnen Block von Durchgängen dar. Ähnlich kann auf einer anderen Ebene des Experiments eine SEQUENCE (oft *block_sequence* genannt) einen einzigen Block von Durchgängen enthalten, gefolgt von einer FEEDBACK-Anzeige. Ein *practice_phase*-LOOP um diese 'block'-SEQUENCE bildet dann die Übungsphase des Experiments. Das klingt jetzt vielleicht noch etwas abstrakt, aber während du dieses Tutorial durchgehst, wirst du mit der Verwendung von LOOPs und SEQUENCEs vertraut werden.

__Tipp__ -- Für weitere Informationen zu SEQUENCEs und LOOPs siehe:

- %link:loop%
- %link:sequence%

</div>

__Füge ein neues form_text_display-Element für die End-der-Übungsphase-Nachricht hinzu__

Nach der Übungsphase möchten wir die Teilnehmer darauf hinweisen, dass das eigentliche Experiment beginnt. Dafür benötigen wir ein weiteres `form_text_display`. Gehe zurück zur *experiment*-SEQUENCE und ziehe ein `form_text_display` aus der Element-Werkzeugleiste auf das LOOP-Element. Das gleiche Pop-up-Menü wie zuvor erscheint. Wähle diesmal 'Insert after new_loop'. (Darauf kommen wir in Schritt 12 zurück.)

<div class='info-box' markdown='1'>

__Tipp__ -- Keine Sorge, wenn du versehentlich ein zu laufendes Element eines LOOPs geändert hast. Du kannst dies ganz einfach rückgängig machen, indem du auf die Schaltfläche „Rückgängig“ in der Werkzeugleiste klickst (`Strg+Umschalt+Z`).

</div>

__Füge ein neues Loop-Element, das die zuvor erstellte Sequence enthält, für die Experimentalphase hinzu__

Wir benötigen für die Experimentalphase ein LOOP-Element, genauso wie für die Übungsphase. Ziehe deshalb ein LOOP aus dem Element-Werkzeugleisten-Menü auf *_form_text_display*.

Das neu erzeugte LOOP (genannt *new_loop_1*) ist leer und sollte mit einer SEQUENCE gefüllt werden, genauso wie das zuvor erstellte LOOP. Da aber die Durchgänge der Übungs- und Experimentalphase identisch sind, können sie die gleiche SEQUENCE verwenden. Daher musst du diesmal keine neue SEQUENCE aus der Element-Werkzeugleiste ziehen, sondern kannst die *bestehende* wiederverwenden (d.h. eine verknüpfte Kopie anlegen).

Dazu klicke mit der rechten Maustaste auf die zuvor erstellte *new_sequence* und wähle 'Copy (linked)'. Jetzt klicke mit der rechten Maustaste auf *new_loop_1* und wähle 'Paste'. Im angezeigten Pop-up-Menü wähle dann 'Insert into new_loop 1'.

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ – Es gibt einen wichtigen Unterschied zwischen *verknüpften* und *unverknüpften* Kopien. Wenn Sie eine verknüpfte Kopie eines Elements erstellen, fügen Sie ein weiteres Vorkommen desselben Elements hinzu. Daher wird eine Änderung am Originalelement auch die verknüpfte Kopie betreffen. Im Gegensatz dazu sieht eine unverknüpfte Kopie anfangs identisch aus (außer beim Namen), aber Sie können das Original bearbeiten, ohne dass sich dies auf die unverknüpfte Kopie auswirkt – und umgekehrt.

</div>

__Fügen Sie ein neues form_text_display-Element für die Abschiedsnachricht hinzu__

Wenn das Experiment beendet ist, sollten wir uns vom Teilnehmer verabschieden. Dafür benötigen wir ein weiteres `form_text_display`-Element. Gehen Sie zurück zur *experiment*-SEQUENCE und ziehen Sie ein `form_text_display` aus der Werkzeugleiste auf *new_loop_1*. Wählen Sie in dem erscheinenden Menü 'Nach new_loop_1 einfügen' aus. (Wir kommen darauf in Schritt 12 zurück.)

__Geben Sie den neuen Elementen sinnvolle Namen__

Standardmäßig haben neue Elemente Namen wie *new_sequence* und *new_form_text_display_2*. Es ist eine gute Praxis, Elementen sinnvolle Namen zu geben. Das erleichtert das Verständnis der Struktur des Experiments erheblich. Wenn Sie möchten, können Sie auch eine Beschreibung zu jedem Element hinzufügen. Elementnamen dürfen nur aus alphanumerischen Zeichen und/oder Unterstrichen bestehen.

- Wählen Sie *new_form_text_display* im Übersichtsbereich, doppelklicken Sie auf das Label oben im Tab-Bereich und benennen Sie das Element in *instructions* um. (Übersichtsbereich-Kurzbefehltaste: `F2`)
- Benennen Sie *new_loop* in *practice_loop* um.
- Benennen Sie *new_sequence* in *block_sequence* um. Da Sie dieses Element in *new_loop_1* erneut verwendet haben, ändert sich der Name dort automatisch mit. (Dies verdeutlicht, warum es effizient ist, wann immer möglich verknüpfte Kopien zu erstellen.)
- Benennen Sie *new_form_text_display_1* in *end_of_practice* um.
- Benennen Sie *new_loop_1* in *experimental_loop* um.
- Benennen Sie *new_form_text_display_2* in *end_of_experiment* um.

__Geben Sie dem gesamten Experiment einen sinnvollen Namen__

Das gesamte Experiment hat ebenfalls einen Titel und eine Beschreibung. Klicken Sie im Übersichtsbereich auf 'New experiment'. Sie können das Experiment auf die gleiche Weise umbenennen, wie Sie die Elemente umbenannt haben. Der aktuelle Titel lautet 'New experiment'. Benennen Sie das Experiment in 'Tutorial: Gaze cuing' um. Im Gegensatz zu Elementnamen darf der Experiment-Titel Leerzeichen usw. enthalten.

Der Übersichtsbereich Ihres Experiments sieht nun wie %FigStep1 aus. Jetzt wäre ein guter Zeitpunkt, um Ihr Experiment zu speichern (Tastenkürzel: `Ctrl+S`).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of the step 1.
--%


## Schritt 2: Erstellen Sie die Block-Sequenz

Klicken Sie im Überblick auf *block_sequence*. Diese SEQUENCE ist derzeit leer. Wir möchten, dass die *block_sequence* aus einem Block von Durchgängen besteht, gefolgt von einer FEEDBACK-Anzeige. Dazu müssen wir Folgendes tun:

__Fügen Sie ein reset_feedback-Element zum Zurücksetzen der Feedback-Variablen hinzu__

Wir möchten nicht, dass unser Feedback durch Tastendrücke während der Anweisungsphase oder vorheriger Blöcke beeinflusst wird. Daher beginnen wir jeden Durchgangsblock mit dem Zurücksetzen der Feedback-Variablen. Dafür benötigen wir ein `reset_feedback`-Element. Ziehen Sie `reset_feedback` aus der Werkzeugleiste (unter 'Antwortsammlung') auf *block_sequence*.

__Fügen Sie eine neue Schleife, die eine neue Sequenz für einen Block von Durchgängen enthält, hinzu__

Für einen einzelnen Durchgang benötigen wir eine SEQUENCE. Für einen Durchgangsblock müssen wir diese SEQUENCE mehrfach wiederholen. Daher müssen wir für einen Durchgangsblock eine LOOP um eine SEQUENCE herumlegen. Ziehen Sie eine LOOP aus der Werkzeugleiste auf *new_reset_feedback*. Ziehen Sie als Nächstes eine SEQUENCE aus der Werkzeugleiste auf die neu erstellte LOOP und wählen Sie im darauf erscheinenden Menü 'In new_loop einfügen' aus. (Wir werden darauf in Schritt 3 zurückkommen.)

__Fügen Sie ein feedback-Element hinzu__

Nach jedem Block von Durchgängen möchten wir dem Teilnehmer eine Rückmeldung geben, damit er weiß, wie gut er abschneidet. Dafür benötigen wir ein FEEDBACK-Element. Ziehen Sie ein FEEDBACK aus der Element-Werkzeugleiste auf *new_loop* und wählen Sie im erscheinenden Pop-up-Menü „Insert after loop“ aus. (Wir werden in Schritt 10 darauf zurückkommen.)

__Geben Sie den neuen Elementen sinnvolle Namen__

Benennen Sie um: (Siehe Schritt 1, falls Sie sich nicht mehr erinnern, wie das geht.)

- *new_loop* in *block_loop*
- *new_sequence* in *trial_sequence*
- *new_reset_feedback* in *reset_feedback*
- *new_feedback* in *feedback*

Die Übersicht Ihres Experiments sieht nun wie %FigStep2 aus. Denken Sie daran, Ihr Experiment regelmäßig zu speichern.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## Schritt 3: Füllen Sie den block_loop mit unabhängigen Variablen

Wie der Name schon sagt, entspricht *block_loop* einem einzelnen Block von Durchgängen. Im vorherigen Schritt haben wir den *block_loop* erstellt, aber wir müssen noch die unabhängigen Variablen definieren, die innerhalb des Blocks variiert werden. Unser Experiment hat drei unabhängige Variablen:

- __gaze_cue__ kann 'left' oder 'right' sein.
- __target_pos__ (die Position des Ziels) kann '-300' oder '300' sein. Diese Werte spiegeln die X-Koordinate des Ziels in Pixeln wider (0 = Mitte). Wenn wir die Koordinaten direkt verwenden und nicht 'left' und 'right', ist das praktisch, wenn wir die Zielanzeigen erstellen (siehe Schritt 5).
- __target_letter__ (der Zielbuchstabe) kann 'F' oder 'H' sein.

Daher hat unser Experiment 2 x 2 x 2 = 8 Stufen. Obwohl 8 Stufen nicht allzu viele sind (die meisten Experimente haben mehr), müssen wir nicht alle möglichen Kombinationen per Hand eingeben. Klicken Sie auf *block_loop* in der Übersicht, um dessen Tab zu öffnen. Klicken Sie dann auf die Schaltfläche „Full-factorial design“. Im Variablen-Assistenten definieren Sie alle Variablen, indem Sie den Namen in die erste Zeile und die Stufen in die Zeilen darunter eingeben (siehe %FigVariableWizard). Wenn Sie „Ok“ auswählen, sehen Sie, dass *block_loop* mit allen 8 möglichen Kombinationen gefüllt wurde.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  The loop variable wizard in Step 3.
--%

In der resultierenden Loop-Tabelle entspricht jede Zeile einem Durchlauf von *trial_sequence*. Da in unserem Fall ein Durchlauf von *trial_sequence* einem Durchgang entspricht, entspricht jede Zeile in unserer Loop-Tabelle einem Durchgang. Jede Spalte steht für eine Variable, die in jedem Durchgang einen anderen Wert haben kann.

Aber wir sind noch nicht fertig. Wir müssen drei weitere Variablen hinzufügen: die Position des Distraktors, die korrekte Antwort und die Kongruenz.

- __dist_pos__ -- Geben Sie in der ersten Zeile der ersten leeren Spalte 'dist_pos' ein. Dadurch wird automatisch eine neue experimentelle Variable mit dem Namen 'dist_pos' hinzugefügt. Geben Sie in den darauffolgenden Zeilen überall dort '300' ein, wo 'target_pos' -300 ist, und '-300' überall dort, wo 'target_pos' 300 ist. Mit anderen Worten: Das Ziel und der Distraktor sollten sich gegenüberliegen.
- __correct_response__ -- Erstellen Sie eine weitere Variable in einer anderen leeren Spalte mit dem Namen 'correct_response'. Setzen Sie 'correct_response' auf 'z', wenn 'target_letter' 'F' ist, und auf 'm', wenn 'target_letter' 'H' ist. Das bedeutet, dass der Teilnehmer die Taste 'z' drücken sollte, wenn er ein 'F' sieht, und die Taste 'm', wenn er ein 'H' sieht. (Sie können auch andere Tasten wählen, falls 'z' und 'm' auf Ihrer Tastatur ungünstig liegen; auf AZERTY-Tastaturen sind beispielsweise 'w' und 'n' besser.)
- __congruency__ -- Erstellen Sie eine weitere Variable mit dem Namen 'congruency'. Setzen Sie 'congruency' auf 'congruent', wenn 'target_pos' '-300' und 'gaze_cue' 'left' ist oder wenn 'target_pos' '300' und 'gaze_cue' 'right' ist. Mit anderen Worten: Ein Durchgang ist kongruent, wenn das Gesicht das Ziel anschaut. Setzen Sie 'congruency' auf 'incongruent' bei den Durchgängen, in denen das Gesicht den Distraktor anschaut. Die Variable 'congruency' ist nicht notwendig, um das Experiment durchzuführen; sie ist jedoch hilfreich, um die Daten später auszuwerten.

Wir müssen noch eine letzte Sache erledigen. 'Repeat' ist aktuell auf '1.00' gesetzt. Das bedeutet, dass jeder Durchlauf einmal ausgeführt wird. Der Block besteht jetzt also aus 8 Durchgängen, was etwas kurz ist. Eine sinnvolle Länge für einen Block ist 24 Durchgänge, setze daher 'Repeat' auf 3.00 (3 Wiederholungen x 8 Durchgänge = 24 Durchgänge). Du musst 'Order' nicht ändern, denn 'random' ist genau das, was wir wollen.

Der *block_loop* sieht nun aus wie %FigStep3. Denke daran, dein Experiment regelmäßig zu speichern.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Du kannst deine Loop-Tabelle in deinem bevorzugten Tabellenkalkulationsprogramm vorbereiten und sie dann in die LOOP-Variablentabelle einfügen.

__Tipp__ -- Du kannst deine Loop-Tabelle auch in einer separaten Datei (im `.xlsx`- oder `.csv`-Format) angeben und diese Datei direkt verwenden. Wähle dazu 'file' unter 'Source' aus.

__Tipp__ -- Du kannst 'Repeat' auf eine nicht-ganzzahlige Zahl setzen. Zum Beispiel werden bei 'Repeat' auf '0.5' nur die Hälfte der Durchgänge (zufällig ausgewählt) ausgeführt.

</div>

## Schritt 4: Füge Bilder und Tondateien zum Datei-Pool hinzu

Für unsere Stimuli verwenden wir Bilddateien. Zusätzlich wird ein Ton abgespielt, wenn der Teilnehmer einen Fehler macht. Dafür benötigen wir eine Tondatei.

Du kannst die benötigten Dateien hier herunterladen (in den meisten Webbrowsern kannst du mit einem Rechtsklick auf die Links 'Link speichern unter' oder eine ähnliche Option auswählen):

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Nachdem du diese Dateien (zum Beispiel auf deinen Desktop) heruntergeladen hast, kannst du sie zum Datei-Pool hinzufügen. Falls der Datei-Pool noch nicht sichtbar ist (standardmäßig auf der rechten Seite des Fensters), klicke auf den Button 'Show file pool' in der Hauptsymbolleiste (Tastenkürzel: `Ctrl+P`). Am einfachsten fügst du die vier Dateien hinzu, indem du sie vom Desktop (oder von dem Speicherort, an den du sie heruntergeladen hast) direkt in den Datei-Pool ziehst. Alternativ kannst du auf das '+'-Symbol im Datei-Pool klicken und die Dateien über den daraufhin erscheinenden Dateiauswahldialog hinzufügen. Der Datei-Pool wird automatisch mit deinem Experiment gespeichert.

Dein Datei-Pool sieht nun aus wie %FigStep4. Denke daran, dein Experiment regelmäßig zu speichern.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

## Schritt 5: Fülle die *trial_sequence* mit Items

Ein Durchgang (trial) in unserem Experiment sieht wie folgt aus:

1. __Fixationspunkt__ -- 750 ms, SKETCHPAD-Item
2. __Neutraler Blick__ -- 750 ms, SKETCHPAD-Item
3. __Blickrichtungshinweis__ -- 500 ms, SKETCHPAD-Item
4. __Target__  -- 0 ms, SKETCHPAD-Item
5. __Antworterfassung__ 	-- KEYBOARD_RESPONSE-Item
6. __Ton abspielen, falls die Antwort falsch war__ --  SAMPLER-Item
7. __Antwort in die Datei schreiben__ -- LOGGER-Item

Klicke im Überblick auf *trial_sequence*, um den *trial_sequence*-Tab zu öffnen. Nimm ein SKETCHPAD aus der Elementleiste und ziehe es in die *trial_sequence*. Wiederhole dies drei weitere Male, sodass die *trial_sequence* vier SKETCHPADs enthält. Füge anschließend ein KEYBOARD_RESPONSE-Item, ein SAMPLER-Item und ein LOGGER-Item hinzu.

Wir werden die neuen Items wieder umbenennen, damit die *trial_sequence* leicht verständlich ist. Benenne:

- *new_sketchpad* in *fixation_dot* um
- *new_sketchpad_1* in *neutral_gaze* um
- *new_sketchpad_2* in *gaze_cue* um
- *new_sketchpad_3* in *target* um
- *new_keyboard_response* in *keyboard_response* um
- *new_sampler* in *incorrect_sound* um
- *new_logger* in *logger* um

Standardmäßig werden Items immer ausgeführt, was durch den Run-if-Ausdruck `True` angezeigt wird. Wir möchten dies jedoch für das *incorrect_sound* Item ändern, das nur ausgeführt werden soll, wenn ein Fehler gemacht wurde. Dazu müssen wir den 'Run if'-Ausdruck im *trial_sequence* Tab auf `correct == 0` ändern. Das funktioniert, weil das *keyboard_response* Item automatisch eine `correct` Variable erzeugt, die auf `1` (korrekt), `0` (inkorrekt) oder `undefined` gesetzt wird (dies hängt von der in Schritt 3 definierten `correct_response` Variable ab). Das doppelte Gleichheitszeichen ist Python-Syntax und zeigt an, dass überprüft werden soll, ob die beiden Werte gleich sind, in diesem Fall, ob die Variable `correct` gleich 0 ist. Um einen Run-if-Ausdruck zu ändern, doppelklicken Sie darauf (Shortcut: `F3`).

Die *trial_sequence* sieht jetzt aus wie %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Was ist ein SKETCHPAD-Item?__ -- Ein SKETCHPAD dient zur Präsentation visueller Reize: Text, geometrische Formen, Fixationspunkte, Gabor-Patches usw. Sie können mit den integrierten Zeichenwerkzeugen auf das SKETCHPAD zeichnen.

__Was ist ein KEYBOARD_RESPONSE-Item?__ -- Ein KEYBOARD_RESPONSE-Item sammelt die Antwort einer Teilnehmerin/eines Teilnehmers über die Tastatur.

__Was ist ein SAMPLER-Item?__ -- Ein SAMPLER-Item spielt einen Ton aus einer Audiodatei ab.

__Was ist ein LOGGER-Item?__ -- Ein LOGGER-Item schreibt Daten in die Protokolldatei. Das ist sehr wichtig: Wenn Sie vergessen, ein LOGGER-Item einzufügen, werden während des Experiments keine Daten protokolliert!

__Tipp__ -- Variablen und bedingte "if"-Ausdrücke sind sehr leistungsstark! Um mehr darüber zu erfahren, siehe:

- %link:manual/variables%

</div>

## Schritt 6: Die Sketchpad-Items zeichnen

Die in Schritt 5 erstellten SKETCHPAD-Items sind noch leer. Es ist Zeit, etwas zu zeichnen!

__Setzen Sie die Hintergrundfarbe auf Weiß__

Klicken Sie im Übersichtsbereich auf *fixation_dot*, um das entsprechende Tab zu öffnen. Das SKETCHPAD ist noch dunkelgrau, während die heruntergeladenen Bilder einen weißen Hintergrund haben. Ups, wir haben vergessen, die Hintergrundfarbe des Experiments auf Weiß zu setzen (standardmäßig ist sie dunkelgrau)! Klicken Sie im Übersichtsbereich auf 'Tutorial: Gaze cuing', um das Tab 'Allgemeine Eigenschaften' zu öffnen. Ändern Sie 'Vordergrund' auf 'schwarz' und 'Hintergrund' auf 'weiß'.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Für eine feinere Kontrolle über Farben können Sie auch die hexadezimale RGB-Notation verwenden (z.B. `#FF000` für Rot), verschiedene Farbräume nutzen oder das Farbauswahlwerkzeug verwenden. Siehe auch:

- %link:manual/python/canvas%

</div>

__Den Fixationspunkt zeichnen__

Gehen Sie zurück zu *fixation_dot*, indem Sie in der Übersicht auf *fixation_dot* klicken. Wählen Sie nun das Fixationspunkt-Element aus, indem Sie auf die Schaltfläche mit dem Fadenkreuz klicken. Wenn Sie den Cursor über das Sketchpad bewegen, sehen Sie die Bildschirmkoordinaten oben rechts. Setzen Sie die (Vordergrund-)Farbe auf 'schwarz'. Klicken Sie auf die Bildschirmmitte (0, 0), um einen zentralen Fixationspunkt zu zeichnen.

Ändern Sie schließlich das Feld 'Dauer' von 'keypress' auf '745', weil wir möchten, dass der Fixationspunkt für 750 ms präsentiert wird. Moment ... *warum haben wir nicht einfach eine Dauer von 750 ms angegeben?* Der Grund dafür ist, dass die tatsächliche Anzeigedauer immer auf einen Wert aufgerundet wird, der mit der Bildwiederholrate Ihres Monitors kompatibel ist. Das klingt vielleicht kompliziert, aber für die meisten Zwecke reichen folgende Faustregeln aus:

1. Wählen Sie eine Dauer, die mit der Bildwiederholrate Ihres Monitors möglich ist. Wenn Ihre Bildwiederholrate beispielsweise 60 Hz beträgt, bedeutet dies, dass jedes Bild 16,7 ms dauert (= 1000 ms/60 Hz). Daher sollten Sie auf einem 60-Hz-Monitor immer eine Dauer wählen, die ein Vielfaches von 16,7 ms ist, z. B. 16,7, 33,3, 50, 100 usw.
2. Geben Sie im Dauer-Feld des SKETCHPAD eine Dauer an, die ein paar Millisekunden weniger als Ihr Zielwert ist. Wenn Sie beispielsweise ein SKETCHPAD für 50 ms präsentieren möchten, wählen Sie eine Dauer von 45. Wenn Sie ein SKETCHPAD für 1000 ms präsentieren möchten, wählen Sie eine Dauer von 995. Und so weiter.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Eine ausführliche Diskussion zum experimentellen Timing finden Sie unter:

- %link:timing%

__Tipp__ -- Die Dauer eines SKETCHPAD kann einen Wert in Millisekunden annehmen, Sie können aber auch 'keypress' oder 'mouseclick' eingeben, um eine Tastatureingabe bzw. einen Mausklick abzufragen. In diesem Fall funktioniert ein SKETCHPAD ähnlich wie ein KEYBOARD_RESPONSE-Item (aber mit weniger Optionen).

__Tipp__ -- Stellen Sie sicher, dass die (Vordergrund-)Farbe auf Schwarz eingestellt ist. Ansonsten zeichnen Sie Weiß auf Weiß und sehen nichts!

</div>

__Zeichnen Sie den neutralen Blick__

Öffnen Sie das *neutral_gaze* SKETCHPAD. Wählen Sie nun das Bild-Werkzeug, indem Sie auf die Schaltfläche mit dem Berglandschaft-Symbol klicken. Klicken Sie auf die Bildschirmmitte (0, 0). Der Dialog 'Datei aus Pool auswählen' erscheint. Wählen Sie die Datei `gaze_neutral.png` und klicken Sie auf die Schaltfläche 'Auswählen'. Das Bild mit dem neutralen Blick schaut Sie nun aus der Bildschirmmitte an! Ändern Sie abschließend wie zuvor das Feld 'Dauer' von 'keypress' auf '745'. (Und beachten Sie erneut, dass dies auf den meisten Monitoren eine Dauer von 750 ms bedeutet!)

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- OpenSesame kann eine Vielzahl von Bildformaten verarbeiten. Allerdings können einige (nicht standardisierte) `.bmp`-Formate Probleme verursachen. Wenn Sie feststellen, dass ein `.bmp`-Bild nicht angezeigt wird, können Sie es in ein anderes Format wie `.png` konvertieren. Sie können Bilder einfach mit kostenlosen Tools wie [GIMP] konvertieren.
</div>

__Zeichnen Sie den Blickhinweis__

Öffnen Sie das *gaze_cue* SKETCHPAD und wählen Sie erneut das Bild-Werkzeug. Klicken Sie auf die Bildschirmmitte (0, 0) und wählen Sie die Datei `gaze_left.png`.

Aber wir sind noch nicht fertig! Denn der Blickhinweis sollte nicht immer 'left' sein, sondern von der Variable `gaze_cue` abhängen, die wir in Schritt 3 definiert haben. Durch das Einfügen des Bildes `gaze_left.png` in das SKETCHPAD haben wir jedoch bereits ein Skript generiert, das nur noch minimal bearbeitet werden muss, um sicherzustellen, dass das richtige Bild angezeigt wird. Klicken Sie auf die Schaltfläche 'Select view' oben rechts im *gaze_cue*-Tab und wählen Sie 'View script'. Nun sehen Sie das Skript, das dem gerade erstellten sketchpad entspricht:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Das Einzige, was wir ändern müssen, ist `gaze_left.png` durch `gaze_{gaze_cue}.png` zu ersetzen. Das bedeutet, dass OpenSesame die Variable `gaze_cue` (mit den Werten `left` und `right`) verwendet, um zu bestimmen, welches Bild angezeigt wird.

Wenn wir schon dabei sind, können wir die Dauer auf '495' (aufgerundet auf 500!) ändern. Das Skript sieht dann so aus:

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Klicken Sie oben rechts auf die Schaltfläche 'Apply', um Ihre Änderungen am Skript zu übernehmen und zu den normalen Item-Einstellungen zurückzukehren. OpenSesame wird Sie warnen, dass das Bild nicht angezeigt werden kann, da es mithilfe von Variablen definiert wurde, und ein Platzhalterbild angezeigt wird. Keine Sorge, während des Experiments wird das korrekte Bild angezeigt!

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Der Variablen-Inspektor (Tastenkürzel: `Strg+I`) ist eine leistungsstarke Möglichkeit, herauszufinden, welche Variablen in deinem Experiment definiert wurden und welche Werte sie haben (siehe %FigVariableInspector). Wenn dein Experiment nicht läuft, haben die meisten Variablen noch keinen Wert. Wenn du jedoch dein Experiment in einem Fenster ausführst und dabei den Variablen-Inspektor sichtbar hast, kannst du sehen, wie sich Variablen in Echtzeit verändern. Das ist sehr nützlich, um dein Experiment zu debuggen.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "Der Variablen-Inspektor ist eine praktische Möglichkeit, einen Überblick über die Variablen zu bekommen, die in deinem Experiment existieren."
--%

</div>

__Zeichne das Target__

Wir möchten, dass drei Objekte auf dem Target-Bildschirm angezeigt werden: der Target-Buchstabe, der Distraktor-Buchstabe und der Blickrichtungshinweis (siehe %FigGazeCuing). Wie zuvor beginnen wir mit dem Erstellen einer statischen Darstellung mithilfe des SKETCHPAD-Editors. Anschließend müssen wir nur geringfügige Änderungen am Skript vornehmen, sodass die genaue Anzeige von den Variablen abhängt.

Klicke im Überblick auf *target*, um den Target-Tab zu öffnen, und zeichne wie zuvor das Bild `gaze_left.png` in die Bildschirmmitte. Wähle dann das Textwerkzeug aus, indem du auf die Schaltfläche mit dem 'A'-Symbol klickst. Ändere die Vordergrundfarbe auf 'black' (falls dies nicht bereits der Fall ist). Die Standard-Schriftgröße ist 18 px, was für unseren Zweck etwas klein ist. Ändere daher die Schriftgröße auf 32 px. Klicke nun auf (-320, 0) im SKETCHPAD (die X-Koordinate muss nicht exakt -320 sein, da wir das ohnehin in eine Variable ändern werden). Gib im erscheinenden Dialogfeld "{target_letter}" ein, um den Target-Buchstaben zu zeichnen (beim Zeichnen von Text kannst du Variablen direkt verwenden). Klicke anschließend auf (320, 0) und zeichne ein 'X' (der Distraktor ist immer ein 'X').

Öffne nun den Script-Editor, indem du oben rechts auf die Schaltfläche 'Select view' klickst und 'View script' auswählst. Das Script sieht folgendermaßen aus:

~~~ .python
set duration keypress
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

Wie zuvor änderst du `gaze_left.png` in `gaze_{gaze_cue}.png`. Wir müssen außerdem die Position des Targets und des Distraktors von den Variablen `target_pos` und `dist_pos` abhängig machen. Dazu ersetzt du einfach `-320` durch `{target_pos}` und `320` durch `{dist_pos}`. Vergiss nicht, dass du die `0` (die Y-Koordinate) stehen lassen musst. Das Script sieht nun so aus:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

Klicke auf die Schaltfläche 'Apply', um das Script anzuwenden und zu den regulären Item-Kontrollen zurückzukehren.

Stelle abschließend das Feld 'Duration' auf '0'. Das bedeutet nicht, dass das Target nur für 0 ms angezeigt wird, sondern dass das Experiment direkt zum nächsten Item (*keyboard_response*) übergeht. Da *keyboard_response* auf eine Antwort wartet, aber nichts auf dem Bildschirm verändert, bleibt das Target so lange sichtbar, bis eine Antwort gegeben wurde.

Denke daran, dein Experiment regelmäßig zu speichern.

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ – Jedes Element eines SKETCHPAD verfügt über eine „Show if“-Option, die angibt, wann das Element angezeigt werden soll. Du kannst dies verwenden, um Elemente eines SKETCHPADs abhängig von bestimmten Variablen ein- oder auszublenden, ähnlich wie bei run-if-Anweisungen in einer SEQUENCE.

__Tipp__ – Stelle sicher, dass die (Vordergrund-)Farbe auf Schwarz eingestellt ist. Andernfalls zeichnest du Weiß auf Weiß und siehst nichts!

</div>

## Schritt 7: Konfiguriere das keyboard_response-Element

Klicke im Überblick auf *keyboard_response*, um dessen Tab zu öffnen. Du siehst drei Optionen: Korrekte Antwort, Erlaubte Antworten, Zeitlimit und Ereignistyp.

Wir haben die Variable `correct_response` bereits in Schritt 3 gesetzt. Sofern wir keine korrekte Antwort explizit festlegen, verwendet OpenSesame automatisch die Variable `correct_response`, sofern sie verfügbar ist. Daher müssen wir das Feld 'Korrekte Antwort' hier nicht ändern.

Wir müssen jedoch die erlaubten Antworten festlegen. Gib 'z;m' in das Feld für die erlaubten Antworten ein (oder andere Tasten, falls du andere Antworttasten ausgewählt hast). Das Semikolon trennt die Antworten voneinander. Die KEYBOARD_RESPONSE akzeptiert jetzt nur noch die Tasten 'z' und 'm'. Alle anderen Tastendrücke werden ignoriert, mit Ausnahme von 'escape', das das Experiment pausiert.

Wir möchten außerdem ein Zeitlimit setzen, also das maximale Intervall, das die KEYBOARD_RESPONSE wartet, bevor sie entscheidet, dass die Antwort falsch ist und die Variable 'response' auf 'None' setzt. '2000' (ms) ist ein guter Wert.

Den Ereignistyp müssen wir nicht ändern, da wir wollen, dass die Teilnehmenden durch Tastendruck (keypress, Standard) und nicht durch das Loslassen einer Taste (keyrelease) antworten.

Die KEYBOARD_RESPONSE sieht jetzt wie %FigStep7 aus.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "Die KEYBOARD_RESPONSE am Ende von Schritt 7."
--%

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ – Standardmäßig verwendet die KEYBOARD_RESPONSE die Variable `correct_response`, um zu bestimmen, ob eine Antwort korrekt war. Du kannst aber auch eine andere Variable verwenden. Gib hierzu einfach einen Variablennamen in geschweiften Klammern (`{meine_variable}`) in das Feld für die richtige Antwort ein.

__Tipp__ – Wenn 'flush pending key presses' aktiviert ist (standardmäßig ist dies der Fall), werden alle ausstehenden Tastendrücke verworfen, wenn das KEYBOARD_RESPONSE-Element aufgerufen wird. Das verhindert Übertragungen, die sonst passieren könnten, wenn die Teilnehmer:innen während eines Nicht-Antwort-Abschnitts der Versuchsdurchführung versehentlich eine Taste drücken.

__Tipp__ – Um Sondertasten wie '/' oder die Pfeil-hoch-Taste zu verwenden, kann man Tastenbezeichnungen (z. B. 'up' und 'space') oder zugehörige Zeichen (z. B. '/' und ']') benutzen. Die Schaltfläche 'List available keys' bietet einen Überblick über alle gültigen Tastennamen.

</div>

## Schritt 8: Konfiguriere das falsche (sampler) Element

Das *incorrect_sound*-Element benötigt kaum Arbeit: Wir müssen nur den abzuspielenden Ton auswählen. Klicke im Überblick auf *incorrect_sound*, um dessen Tab zu öffnen. Klicke auf die Schaltfläche 'Browse' und wähle `incorrect.ogg` aus dem file pool aus.

Der sampler sieht jetzt wie %FigStep8 aus.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "Das *incorrect_sound*-Element am Ende von Schritt 8."
--%

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ – Du kannst Variablen verwenden, um zu bestimmen, welcher Ton abgespielt werden soll, indem du einen Variablennamen in geschweifte Klammern als (Teil des) Dateinamens schreibst. Beispiel: `{a_word}.ogg`

__Tipp__ – Der SAMPLER verarbeitet Dateien im Format `.ogg`, `.mp3` und `.wav`. Wenn du Sounddateien in einem anderen Format hast, ist [Audacity] ein großartiges, kostenloses Tool, um Sounddateien (und vieles mehr) zu konvertieren.

</div>

## Schritt 9: Konfiguriere den variable logger

Tatsächlich müssen wir den LOGGER nicht konfigurieren, aber wir werfen trotzdem einen Blick darauf. Klicke im Überblick auf *logger*, um dessen Tab zu öffnen. Du siehst, dass die Option 'Automatically log all variables' aktiviert ist. Das bedeutet, dass OpenSesame alles protokolliert – das ist in Ordnung.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Wenn Sie Ihre Logdateien übersichtlich halten möchten, können Sie die Option "Alle Variablen automatisch loggen" deaktivieren und Variablen manuell auswählen, entweder indem Sie die Variablennamen selbst eingeben ("Benutzerdefinierte Variable hinzufügen") oder indem Sie Variablen aus dem Variableninspektor in die LOGGER-Tabelle ziehen. Sie können auch die Option "Alle Variablen automatisch loggen" aktiviert lassen und die Variablen ausschließen, die Sie nicht interessieren.

__Der wichtigste Tipp überhaupt__ -- Überprüfen Sie immer dreifach, ob alle notwendigen Variablen in Ihrem Experiment geloggt werden! Die beste Methode, dies zu kontrollieren, besteht darin, das Experiment durchzuführen und die daraus resultierenden Logdateien zu überprüfen.

</div>

## Schritt 10: Zeichnen Sie das Feedback-Element

Nach jedem Block von Durchgängen möchten wir dem Teilnehmer Feedback geben, damit er/sie weiß, wie gut er/sie abschneidet. Daher haben wir in Schritt 2 ein FEEDBACK-Element mit dem Namen *feedback* ans Ende von *block_sequence* hinzugefügt.

Klicken Sie im Überblick auf *feedback*, um dessen Tab zu öffnen, wählen Sie das "Text zeichnen"-Werkzeug, ändern Sie die Vordergrundfarbe auf "schwarz" (falls sie nicht schon schwarz ist), und klicken Sie auf (0, 0). Geben Sie nun folgenden Text ein:

```text
Ende des Blocks

Ihre durchschnittliche Reaktionszeit betrug {avg_rt} ms
Ihre Genauigkeit betrug {acc} %

Drücken Sie eine beliebige Taste, um fortzufahren
```

Da wir möchten, dass das Feedback-Element so lange sichtbar bleibt, wie der Teilnehmer es möchte (d. h. bis er/sie eine Taste drückt), lassen wir das Feld "Dauer" auf "keypress" eingestellt.

Das Feedback-Element sieht nun aus wie %FigStep_10.

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "The feedback item at the end of Step 10."
--%

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Was ist ein Feedback-Element?__ -- Ein FEEDBACK-Element ist fast identisch mit einem SKETCHPAD-Element. Der einzige Unterschied besteht darin, dass ein FEEDBACK-Element nicht im Voraus vorbereitet wird. Das bedeutet, dass Sie es verwenden können, um Feedback zu präsentieren, das aktuelle Informationen über die Antwort eines Teilnehmers benötigt. FEEDBACK-Elemente sollten nicht verwendet werden, um zeitkritische Anzeigen darzustellen, da sie nicht vorab vorbereitet werden und somit zeitlich nicht so präzise wie ein SKETCHPAD-Element sind. Siehe auch:

- %link:visual%

__Feedback und Variablen__ -- Antwort-Elemente erfassen automatisch die Genauigkeit und die durchschnittliche Reaktionszeit des Teilnehmers in den Variablen "acc" (Synonym: "accuracy") und "avg_rt" (Synonym: "average_response_time"). Siehe auch:

- %link:manual/variables%

__Tipp__ -- Achten Sie darauf, dass die (Vordergrund-)Farbe auf Schwarz eingestellt ist. Andernfalls malen Sie Weiß auf Weiß und sehen nichts!

</div>

## Schritt 11: Legen Sie die Länge der Übungs- und Experimentalphase fest

Wir haben zuvor die Elemente *practice_loop* und *experiment_loop* erstellt, die beide *block_sequence* aufrufen (also einen Block von Durchgängen). Allerdings rufen sie momentan *block_sequence* nur einmal auf, sodass sowohl die Übungs- als auch die Experimentalphase jeweils nur aus einem einzigen Block besteht.

Klicken Sie auf *practice_loop*, um dessen Tab zu öffnen, und setzen Sie "Repeat" auf "2,00". Das bedeutet, dass die Übungsphase aus zwei Blöcken besteht.

Klicken Sie auf *experimental_loop*, um dessen Tab zu öffnen, und setzen Sie "Repeat" auf "8,00". Das bedeutet, dass die Experimentalphase aus acht Blöcken besteht.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Sie können in *practice_loop* und *experimental_loop* jeweils eine Variable `practice` erstellen und sie auf "yes" bzw. "no" setzen. So können Sie leicht verfolgen, welche Durchgänge Teil der Übungsphase waren.

</div>

## Schritt 12: Schreiben Sie die Anweisung, end_of_practice und end_of_experiment Formulare

Ich denke, diesen Schritt bekommen Sie selbst hin! Öffnen Sie einfach die entsprechenden Elemente und fügen Sie etwas Text hinzu, um Instruktionen, eine Nachricht zum Ende der Übungsphase und eine Nachricht zum Ende des Experiments zu präsentieren.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Sie können eine Teilmenge von HTML-Tags verwenden, um Ihren Text zu formatieren. Zum Beispiel, *&lt;b&gt;dies wird fett&lt;b&gt;* und *&lt;span color='red'&gt;dies wird rot&lt;span&gt;*. Für weitere Informationen siehe:

- %link:text%

</div>

## Schritt 13: Führe das Experiment aus!

Geschafft! Klicke auf die Schaltflächen „Im Fenster ausführen“ (Tastenkürzel: `Strg+W`) oder „Im Vollbildmodus ausführen“ (Tastenkürzel: `Strg+R`) in der Symbolleiste, um dein Experiment zu starten.

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ -- Ein Testrun wird noch schneller ausgeführt, wenn du auf die orangefarbene Schaltfläche „Im Fenster ausführen“ (Tastenkürzel: `Strg+Shift+W`) klickst, welche dich nicht fragt, wie die Logdatei gespeichert werden soll (und sollte daher nur zu Testzwecken verwendet werden).

</div>


## Fehler verstehen

Die Fähigkeit, Fehlermeldungen zu verstehen, ist eine entscheidende Kompetenz bei der Arbeit mit OpenSesame. Schließlich läuft ein neu gebautes Experiment selten sofort ohne Fehler!

Angenommen, wir haben bei einem der obigen Schritte einen Fehler gemacht. Beim Versuch, das Experiment zu starten, erhalten wir folgende Fehlermeldung (%FigErrorMessage):

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "Eine Fehlermeldung in OpenSesame."
--%

Die Fehlermeldung beginnt mit einem Namen, in diesem Fall `FStringError`, der den allgemeinen Fehlertyp angibt. Darauf folgt ein kurzer erklärender Text, in diesem Fall „Failed to evaluate f-string expression in the following text: gaze_{gaze_ceu}.png“. Auch ohne zu wissen, was ein f-string ist (es ist ein String, der Python-Code in geschweiften Klammern enthält), wird klar, dass mit dem Text '{gaze_ceu}.png' etwas nicht stimmt.

Die Fehlermeldung zeigt außerdem, dass der Fehler aus der Preparation-Phase des *gaze_cue*-Items stammt.

Schließlich gibt die Fehlermeldung an, was genau beim Auswerten des Textes 'gaze_{gaze_ceu}.png' schiefgelaufen ist: Der Name 'gaze_ceu' ist nicht definiert.

Wenn du die Fehlermeldung aufmerksam liest, wird dir wahrscheinlich schon die Ursache und die Lösung einfallen: Wir haben im *gaze_cue*-Item einen einfachen Tippfehler gemacht und '{gaze_ceu}' statt '{gaze_cue}' geschrieben! Dadurch tritt der Fehler auf, weil es keine Variable mit dem Namen `gaze_ceu` gibt. Dies lässt sich leicht beheben, indem man das Skript des *gaze_cue*-Items öffnet und den Tippfehler korrigiert.


## Abschließend: Einige allgemeine Überlegungen zu Timing und Backend-Auswahl

Im Tab „Allgemeine Eigenschaften“ des Experiments (der Tab, den du durch Klicken auf den Experimentnamen öffnest), kannst du ein Backend auswählen. Das Backend ist die Softwareschicht, die die Anzeige, Eingabegeräte, Ton usw. steuert. Die meisten Experimente funktionieren mit allen Backends, aber es gibt Gründe, eines zu bevorzugen – meistens im Zusammenhang mit dem Timing. Aktuell gibt es vier Backends (je nach System sind möglicherweise nicht alle drei verfügbar):

- __psycho__ -- ein hardwarebeschleunigtes Backend, basierend auf PsychoPy [(Peirce, 2007)][references]. Dies ist die Voreinstellung.
- __xpyriment__ -- ein hardwarebeschleunigtes Backend, basierend auf Expyriment [(Krause & Lindeman, 2013)][references]
- __legacy__ -- ein „sicheres“ Backend, basierend auf PyGame. Es bietet auf den meisten Plattformen zuverlässige Leistung, aber aufgrund fehlender Hardwarebeschleunigung sind die Timingeigenschaften nicht so gut wie bei den anderen Backends.
- __osweb__ -- führt Experimente im Browser aus [(Mathôt & March, 2022)][references].

Siehe auch:

- %link:backends%
- %link:timing%


## Literatur

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Ein quelloffener, grafischer Experiment-Builder für die Sozialwissenschaften. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Sprachwissenschaftliche Experimente online durchführen mit OpenSesame und OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysik-Software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Zeitauflösung von Uhren: Auswirkungen auf die Messung der Reaktionszeit – Gute Nachrichten für schlechte Uhren. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about