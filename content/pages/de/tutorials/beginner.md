title: Anfängertutorial: Blicklenkung
hash: 4b8cd383d0beb70ff7280b358bcb4c15a73635e4fb62d7260bc4b1e16d992e65
locale: de
language: German

[TOC]

## Über OpenSesame

OpenSesame ist ein Programm zur einfachen Entwicklung von Verhaltensexperimenten für Psychologie, Neurowissenschaften und experimentelle Ökonomie. Für Anfänger bietet OpenSesame eine umfassende grafische, point-and-click-Oberfläche. Für fortgeschrittene Benutzer unterstützt OpenSesame Python-Scripting (nicht in diesem Tutorial behandelt).

OpenSesame ist frei verfügbar unter der [General Public License v3][gpl].

## Über dieses Tutorial

In diesem Tutorial wird gezeigt, wie ein einfaches, aber vollständiges psychologisches Experiment mit OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012; Mathôt & March, 2022)][references] erstellt wird. Sie werden hauptsächlich die grafische Benutzeroberfläche von OpenSesame verwenden (d. h. kein Python Inline-Coding), obwohl Sie kleine Änderungen am OpenSesame-Skript vornehmen werden. Dieses Tutorial dauert ungefähr eine Stunde.

## Ressourcen

- __Herunterladen__ -- Dieses Tutorial geht davon aus, dass Sie OpenSesame Version 4.0.0 oder später verwenden. Um zu überprüfen, welche Version Sie verwenden, sehen Sie unteren rechts auf dem 'Get started'-Tab (siehe %FigGetStarted). Sie können die aktuellste Version von OpenSesame herunterladen von:
	- %link:download%
- __Dokumentation__ -- Eine spezielle Dokumentationswebsite finden Sie unter:
	- <http://osdoc.cogsci.nl/>
- __Forum__ -- Ein Support-Forum finden Sie unter:
	- <http://forum.cogsci.nl/>

## Das Experiment

In diesem Tutorial erstellen Sie ein Blickrichtungs-Experiment, wie es von [Friesen und Kingstone (1998)][references] eingeführt wurde. In diesem Experiment wird ein Gesicht in der Mitte des Bildschirms dargestellt (%FigGazeCuing). Dieses Gesicht schaut entweder nach rechts oder nach links. Ein Zielbuchstabe (ein 'F' oder ein 'H') wird links oder rechts vom Gesicht dargestellt. Ein Ablenkungsreiz (der Buchstabe 'X') wird auf der anderen Seite des Gesichts dargestellt. Die Aufgabe besteht darin, so schnell wie möglich anzugeben, ob der Zielbuchstabe ein 'F' oder ein 'H' ist. In der kongruenten Bedingung schaut das Gesicht auf das Ziel. In der inkongruenten Bedingung schaut das Gesicht auf den Ablenkungsreiz. Wie Sie vielleicht schon vermutet haben, ist der typische Befund, dass die Teilnehmer in der kongruenten Bedingung schneller reagieren als in der inkongruenten Bedingung, obwohl die Blickrichtung nicht voraussagend für den Zielort ist. Dies zeigt, dass unsere Aufmerksamkeit automatisch von anderen Menschen Blick gelenkt wird, sogar in Situationen, in denen dies keinen Zweck erfüllt. (Und sogar wenn das Gesicht nur ein Smiley ist!)

%--
Abbildung:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Das Blickrichtungsparadigma [(Friesen und Kingstone, 1998)][references], das Sie in diesem Tutorial implementieren werden. Dieses Beispiel zeigt einen Versuch in der inkongruenten Bedingung, da das Smiley auf den Ablenkungsreiz ('X') und nicht auf das Ziel ('F') schaut.
--%

Das Experiment besteht aus einer Übungs- und einer Versuchsphase. Visuelles Feedback wird nach jedem Block von Versuchen präsentiert. Nach jeder falschen Antwort wird ein Ton abgespielt.

## Experimentelles Design

Dieses Design:

- ist *within-subject*, da alle Teilnehmer an allen Bedingungen teilnehmen
- ist *vollständig gekreuzt* (oder vollfaktoriell), weil alle Kombinationen von Bedingungen auftreten
- hat drei Faktoren (oder Einflussgrößen):
    - *Blickrichtung* mit zwei Stufen (links, rechts)
    - *Zielseite* mit zwei Stufen (links, rechts)
    - *Zielbuchstabe* mit zwei Stufen (F, H)
- hat N Probanden


Siehe auch %DesignScreencast für eine Erklärung der Logik und des Designs des Experiments:

%--
video:
 source: youtube
 id: DesignScreencast
 videoid: aWvibRH6D4E
 width: 640
 height: 360
 caption: |
  Eine Erläuterung der Versuchslogik und des Designs.
--%

## Schritt 1: Die Hauptsequenz erstellen

Wenn Sie OpenSesame starten, sehen Sie die Registerkarte "Los geht's!" (%FigGetStarted). Unter "Start a new experiment" wird eine Liste von Vorlagen angezeigt. Diese Vorlagen bieten praktische Ausgangspunkte für neue Experimente. Nachdem Sie ein Experiment zum ersten Mal gespeichert haben, werden kürzlich geöffnete Experimente unter "Continue with a recent experiment" angezeigt. Am unteren Rand der Seite gibt es Links zur Dokumentation (einschließlich dieses Tutorials), zum Community-Forum und zu einer Seite mit professionellen (kostenpflichtigen) Supportoptionen. Und natürlich einen Link, über den Sie uns einen Kaffee kaufen können, um uns wach zu halten, während wir daran arbeiten, die beste kostenlose Software bereitzustellen!

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  Das Dialogfeld "Get started" beim Start von OpenSesame.
--%

Klicken Sie auf "Default template", um mit einer minimalen Experimentvorlage zu starten.

Standardmäßig gibt es eine Haupt-SEQUENZ, die einfach *experiment* genannt wird. Klicken Sie im Übersichtsbereich (standardmäßig auf der linken Seite, siehe %FigInterface) auf *experiment*, um seine Steuerelemente im Registerkartenbereich zu öffnen. Die SEQUENCE *experiment* besteht aus zwei Elementen: einem `notepad` namens *getting started* und einem SKETCHPAD namens *welcome*.

Wir brauchen diese beiden Elemente nicht. Entfernen Sie *getting_started*, indem Sie in der Übersicht mit der rechten Maustaste darauf klicken und "Delete" auswählen (Tastenkombination: `Del`). Entfernen Sie *welcome* auf die gleiche Weise. Die SEQUENCE *experiment* ist jetzt leer.

%--
figure:
 id: FigInterface
 source: interface.png
 caption: "Das Standardlayout der OpenSesame-Benutzeroberfläche."
--%

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Namen vs. Typen__ -- Elemente in OpenSesame haben einen Namen und einen Typ. Der Name und der Typ können gleich sein, aber meistens sind sie es nicht. Zum Beispiel kann ein SKETCHPAD-Element den Namen *my_target_sketchpad* haben. Um diese Unterscheidung klar zu machen, verwenden wir `monospace`, um Elementtypen anzuzeigen, und *kursive Schrift*, um Namen anzuzeigen.

__Tipp__ -- Die "Extended template" ist ein guter Ausgangspunkt für viele Experimente. Sie enthält bereits die grundlegende Struktur eines versuchsbasierten Experiments.

__Tipp__ -- Sie können auf die Hilfe-Symbole oben rechts in einer Registerkarte eines Elements klicken, um kontextsensitive Hilfe zu erhalten.

__Tipp__ -- Speichern Sie Ihr Experiment oft (Tastenkombination: `Ctrl+S`)! Im unwahrscheinlichen Fall von Datenverlust können Sie oft Ihre Arbeit aus den automatisch erstellten Sicherungen wiederherstellen, die standardmäßig alle 10 Minuten erfolgen (Menü → Tools → Open backup folder).

__Tipp__ -- Wenn Sie "Permanently delete" (Tastenkombination: `Shift+Del`) nicht verwendet haben, sind gelöschte Elemente weiterhin im Papierkorb "Unused items" verfügbar, bis Sie "Permanently delete unused items" in der Registerkarte "Unused items" auswählen. Gelöschte Elemente können Sie wieder in eine SEQUENCE einfügen, indem Sie sie aus dem Papierkorb "Unused items" irgendwo in Ihr Experiment ziehen.

__Tipp__ -- %FigExperimentStructure zeigt schematisch die Struktur des zu erstellenden Experiments. Wenn Sie während des Tutorials verwirrt sind, können Sie auf %FigExperimentStructure verweisen, um zu sehen, wo Sie sich befinden.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  Eine schematische Darstellung der Struktur des 'Gaze cuing'-Experiments. Die Elementtypen sind in Fettschrift, die Elementnamen in normaler Schrift.
--%

</div>

__Fügen Sie ein form_text_display-Element für die Anzeige der Anweisungen hinzu__

Wie der Name schon sagt, ist ein `form_text_display` ein Formular, das Text anzeigen kann. Wir verwenden ein `form_text_display`, um dem Teilnehmer zu Beginn des Experiments Anweisungen zu geben.

Klicken Sie im Übersichtsbereich auf *experiment*, um seine Steuerelemente im Registerkartenbereich zu öffnen. Sie sehen eine leere SEQUENCE. Ziehen Sie ein `form_text_display` aus der Elementleiste (unter "Form", siehe %FigInterface) auf die SEQUENCE *experiment* im Registerkartenbereich. Wenn Sie loslassen, wird ein neues `form_text_display`-Element in die SEQUENCE eingefügt. (Darauf kommen wir in Schritt 12 zurück.)

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Sie können Elemente in den Übersichtsbereich und in SEQUENCE-Reiter ziehen.

__Tipp__ -- Wenn eine Drag-and-Drop-Aktion mehrdeutig ist, wird ein Popup-Menü angezeigt, das Sie fragt, was Sie tun möchten.

__Tipp__ -- Ein `form_text_display` zeigt nur Text an. Wenn Sie Bilder usw. benötigen, können Sie ein SKETCHPAD-Element verwenden. Wir werden das SKETCHPAD in Schritt 5 kennenlernen.

</div>

__Fügen Sie ein Loop-Element hinzu, das ein neues Sequence-Element für die Übungsphase enthält__

Wir müssen ein LOOP-Element zur *experiment*-SEQUENCE hinzufügen. Wir verwenden diese Schleife für die Übungsphase des Experiments. Klicken Sie auf die *experiment*-SEQUENCE, um deren Steuerelemente im Tab-Bereich zu öffnen.

Ziehen Sie das LOOP-Element aus der Element-Symbolleiste in die SEQUENCE, genau wie Sie das `form_text_display` hinzugefügt haben. Neue Elemente werden unterhalb des Elements eingefügt, auf das sie abgelegt werden. Wenn Sie also das neue LOOP auf das zuvor erstellte `form_text_display` ziehen, wird es dort angezeigt, wo Sie es möchten: nach dem `form_text_display`. Aber keine Sorge, wenn Sie ein neues Element an der falschen Stelle ablegen, denn Sie können die Reihenfolge später immer noch ändern.

Ein LOOP allein macht noch nichts. Ein LOOP benötigt immer ein anderes Element zum Ausführen. Daher müssen Sie das neue LOOP-Element mit einem anderen Element füllen. (Wenn Sie sich das Schleifen-Element ansehen, sehen Sie auch eine Warnung: "Kein Element ausgewählt".) Ziehen Sie ein SEQUENCE-Element aus der Element-Symbolleiste auf das LOOP-Element. Ein Popup-Menü wird angezeigt und fragt, ob Sie das SEQUENCE-Element nach oder in das LOOP-Element einfügen möchten. Wählen Sie "Einfügen in new_loop". (Wir werden in Schritt 2 darauf zurückkommen.)

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Was ist ein LOOP-Element?__ -- Ein LOOP ist ein Element, das Ihrem Experiment Struktur verleiht. Es führt wiederholt ein anderes Element aus, normalerweise eine SEQUENCE. In einem LOOP definieren Sie normalerweise auch Ihre unabhängigen Variablen, d. h. die Variablen, die Sie in Ihrem Experiment manipulieren.

__Was ist ein SEQUENCE-Element?__ -- Ein SEQUENCE-Element verleiht Ihrem Experiment ebenfalls Struktur. Wie der Name schon sagt, führt eine SEQUENCE mehrere andere Elemente nacheinander aus.

__Die LOOP-SEQUENCE-Struktur__ -- Sie möchten oft eine Sequenz von Ereignissen wiederholen. Dazu benötigen Sie ein LOOP-Element, das eine SEQUENCE-Element enthält. Eine SEQUENCE allein wiederholt sich nicht. Sie beginnt einfach mit dem ersten Element und endet mit dem letzten Element. Indem Sie ein LOOP-Element um die SEQUENCE legen, können Sie die SEQUENCE mehrmals wiederholen. Zum Beispiel entspricht ein einzelner Versuch normalerweise einer einzelnen SEQUENCE, die als *trial_sequence* bezeichnet wird. Eine LOOP (oft als *block_loop* bezeichnet) um diese *trial_sequence* würde dann einen einzelnen Block von Versuchen darstellen. Ebenso, aber auf einer anderen Ebene des Experiments, kann eine SEQUENCE (oft als *block_sequence* bezeichnet) einen einzelnen Block von Versuchen enthalten, gefolgt von einer FEEDBACK-Anzeige. Eine *practice_phase* LOOP um diese 'Block'-SEQUENCE würde dann die Übungsphase des Experiments darstellen. Das mag jetzt noch etwas abstrakt wirken, aber während Sie dieses Tutorial durchlaufen, werden Sie sich mit der Verwendung von LOOPs und SEQUENCEs vertraut machen.

__Tipp__ -- Für weitere Informationen zu SEQUENCEs und LOOPs siehe:

- %link:loop%
- %link:sequence%

</div>

__Fügen Sie ein neues form_text_display-Element für die End-of-Practice-Nachricht hinzu__

Nach der Übungsphase möchten wir den Teilnehmer darüber informieren, dass das eigentliche Experiment beginnt. Dazu benötigen wir ein weiteres `form_text_display`. Gehen Sie zurück zur *experiment*-SEQUENCE und ziehen Sie ein `form_text_display` aus der Element-Symbolleiste auf das LOOP-Element. Das gleiche Popup-Menü wird wie zuvor angezeigt. Wählen Sie diesmal "Einfügen nach new_loop". (Wir werden in Schritt 12 darauf zurückkommen.)

<div class='info-box' markdown='1'>

__Tipp__ -- Keine Sorge, wenn Sie versehentlich das auszuführende Element einer LOOP geändert haben. Sie können dies einfach rückgängig machen, indem Sie auf die Schaltfläche "Rückgängig" in der Symbolleiste klicken (`Ctrl+Shift+Z`).

</div>

__Fügen Sie ein neues Loop-Element hinzu, das das zuvor erstellte Sequence-Element für die Experimentalphase enthält__

Wir benötigen ein LOOP-Element für die Experimentalphase, genau wie für die Übungsphase. Ziehen Sie daher ein LOOP aus dem Element-Symbolleisten-Menü auf *_form_text_display*.

Die neu erstellte LOOP (genannt *new_loop_1*) ist leer und sollte mit einer SEQUENCE gefüllt werden, genau wie die LOOP, die wir zuvor erstellt haben. Da jedoch die Durchläufe der Übungs- und Experimentierphase identisch sind, können sie dieselbe SEQUENCE verwenden. Anstatt also eine neue SEQUENCE aus der Elementleiste zu ziehen, können Sie die *vorhandene* wiederverwenden (d. h. eine verknüpfte Kopie erstellen).

Um dies zu tun, klicken Sie mit der rechten Maustaste auf die zuvor erstellte *new_sequence* und wählen Sie 'Copy (linked)'. Klicken Sie jetzt mit der rechten Maustaste auf *new_loop_1* und wählen Sie 'Paste'. Im daraufhin angezeigten Popup-Menü wählen Sie 'Insert into new_loop 1'.

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ — Es gibt einen wichtigen Unterschied zwischen *verknüpften* und *nicht verknüpften* Kopien. Wenn Sie eine verknüpfte Kopie eines Elements erstellen, erstellen Sie ein weiteres Vorkommen desselben Elements. Wenn Sie also das Original ändern, ändert sich auch die verknüpfte Kopie. Im Gegensatz dazu wird, wenn Sie eine nicht verknüpfte Kopie eines Elements erstellen, die Kopie zunächst identisch aussehen (bis auf den Namen), aber Sie können das Original bearbeiten, ohne die nicht verknüpfte Kopie zu beeinflussen und umgekehrt.

</div>

__Fügen Sie ein neues form_text_display Element hinzu, für die Verabschiedungsnachricht__

Wenn das Experiment abgeschlossen ist, sollten wir uns vom Teilnehmer verabschieden. Dafür benötigen wir ein weiteres 'form_text_display'-Element. Gehen Sie zurück zur *experiment*-SEQUENCE und ziehen Sie ein `form_text_display` aus der Elementleiste auf *new_loop_1*. Im daraufhin angezeigten Popup-Menü wählen Sie 'Insert after new_loop_1'. (Dazu kommen wir in Schritt 12 zurück.)

__Geben Sie den neuen Elementen sinnvolle Namen__

Standardmäßig haben neue Elemente Namen wie *new_sequence* und *new_form_text_display_2*. Es ist eine gute Praxis, den Elementen sinnvolle Namen zu geben. Dies erleichtert das Verständnis der Experimentstruktur erheblich. Wenn Sie möchten, können Sie jedem Element auch eine Beschreibung hinzufügen. Elementnamen müssen aus alphanumerischen Zeichen und/oder Unterstrichen bestehen.

- Wählen Sie *new_form_text_display* im Übersichtsbereich aus, doppelklicken Sie auf seine Bezeichnung im oberen Bereich der Registerkarte und benennen Sie das Element um in *instructions*. (Übersichtsbereichs-Shortcut: `F2`)
- Benennen Sie *new_loop* in *practice_loop* um.
- Benennen Sie *new_sequence* in *block_sequence* um. Da Sie dieses Element in *new_loop_1* wiederverwendet haben, ändert sich der Name auch dort automatisch. (Das verdeutlicht, warum es effizient ist, verknüpfte Kopien zu erstellen, wann immer dies möglich ist.)
- Benennen Sie *new_form_text_display_1* in *end_of_practice* um.
- Benennen Sie *new_loop_1* in *experimental_loop* um.
- Benennen Sie *new_form_text_display_2* in *end_of_experiment* um.

__Geben Sie dem gesamten Experiment einen sinnvollen Namen__

Das Experiment als Ganzes hat auch einen Titel und eine Beschreibung. Klicken Sie im Übersichtsbereich auf 'New experiment'. Sie können das Experiment auf dieselbe Weise umbenennen, wie Sie seine Elemente umbenannt haben. Der Titel lautet derzeit 'New experiment'. Benennen Sie das Experiment um in 'Tutorial: Gaze cuing'. Im Gegensatz zu Elementnamen dürfen im Titel des Experiments Leerzeichen usw. enthalten sein.

Der Übersichtsbereich Ihres Experiments sieht jetzt aus wie %FigStep1. Jetzt wäre ein guter Zeitpunkt, um Ihr Experiment zu speichern (Shortcut: `Strg+S`).

%--
Abbildung:
 id: FigStep1
 Quelle: step1.png
 Bildunterschrift: |
  Der Übersichtsbereich am Ende des Schritts 1.
--%


## Schritt 2: Erstellen Sie die Block-Sequenz

Klicken Sie im Überblick auf *block_sequence*. Derzeit ist diese SEQUENCE leer. Wir möchten, dass *block_sequence* aus einer Block-Reihe von Durchläufen besteht, gefolgt von einer FEEDBACK-Anzeige. Dazu müssen wir Folgendes tun:

__Fügen Sie ein reset_feedback-Element hinzu, um die Feedback-Variablen zurückzusetzen__

Wir möchten nicht, dass unser Feedback durch Tastendrücke beeinflusst wird, die die Teilnehmer während der Anweisungsphase oder früherer Durchläufe gemacht haben. Daher beginnen wir jeden Block von Durchläufen, indem wir die Feedback-Variablen zurücksetzen. Dafür benötigen wir ein `reset_feedback`-Element. Greifen Sie `reset_feedback` aus der Elementleiste (unter 'Response collection') und ziehen Sie es auf *block_sequence*.

__Fügen Sie eine neue Schleife hinzu, die eine neue Sequenz für einen Block von Durchläufen enthält__

Für einen einzelnen Durchgang benötigen wir eine SEQUENCE. Für einen Block von Durchgängen müssen wir diese SEQUENCE mehrmals wiederholen. Daher müssen wir für einen Block von Durchgängen eine LOOP um eine SEQUENCE legen. Ziehen Sie eine LOOP aus der Item-Toolbar auf *new_reset_feedback*. Ziehen Sie als Nächstes eine SEQUENCE aus der Item-Toolbar auf die neu erstellte LOOP und wählen Sie "Einfügen in new_loop" im aufklappenden Menü, das erscheint. (Dazu kommen wir in Schritt 3 zurück.)

__Ein Feedback-Item anhängen__

Nach jedem Block von Durchgängen möchten wir dem Teilnehmer Feedback geben, damit er/sie weiß, wie gut er/sie zurechtkommen. Dazu benötigen wir ein FEEDBACK-Element. Ziehen Sie ein FEEDBACK aus der Element-Symbolleiste auf *new_loop* und wählen Sie im aufklappenden Menü "Einfügen nach Schleife". (Dazu kommen wir in Schritt 10 zurück.)

__Geben Sie den neuen Elementen sinnvolle Namen__

Umbenennen (siehe Schritt 1, wenn Sie sich nicht mehr daran erinnern können, wie das geht):

- *new_loop* zu *block_loop*
- *new_sequence* zu *trial_sequence*
- *new_reset_feedback* zu *reset_feedback*
- *new_feedback* zu *feedback*

Die Übersicht Ihres Experiments sieht nun aus wie %FigStep2. Speichern Sie Ihr Experiment regelmäßig.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  Der Überblick über das Experiment am Ende von Schritt 2.
--%

## Schritt 3: Füllen Sie die Blockschleife mit unabhängigen Variablen

Wie der Name schon sagt, entspricht *block_loop* einem einzelnen Block von Durchgängen. Im vorherigen Schritt haben wir die *block_loop* erstellt, aber wir müssen noch die unabhängigen Variablen definieren, die innerhalb des Blocks variiert werden. Unser Experiment hat drei unabhängige Variablen:

- __gaze_cue__ kann "links" oder "rechts" sein.
- __target_pos__ (die Position des Ziels) kann "-300" oder "300" sein. Diese Werte spiegeln die X-Koordinate des Ziels in Pixeln (0 = Zentrum) wider. Die Verwendung der Koordinaten direkt, anstatt "links" und "rechts", wird praktisch sein, wenn wir die Zielanzeigen erstellen (siehe Schritt 5).
- __target_letter__ (der Zielbuchstabe) kann "F" oder "H" sein.

Daher hat unser Experiment 2 x 2 x 2 = 8 Stufen. Obwohl 8 Stufen nicht so viele sind (die meisten Experimente werden mehr haben), müssen wir nicht alle möglichen Kombinationen von Hand eingeben. Klicken Sie auf *block_loop* in der Übersicht, um den Reiter zu öffnen. Klicken Sie nun auf die Schaltfläche "Vollfaktorieller Versuchsplan". Im Variablen-Assistenten definieren Sie einfach alle Variablen, indem Sie den Namen in der ersten Zeile eingeben und die Stufen in den Zeilen unter dem Namen (siehe %FigVariableWizard). Wenn Sie "Ok" auswählen, sehen Sie, dass *block_loop* mit allen 8 möglichen Kombinationen gefüllt wurde.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  Der Loop-Variable-Assistent in Schritt 3.
--%

In der resultierenden Schleifentabelle entspricht jede Zeile einem Lauf von *trial_sequence*. Da in unserem Fall ein Lauf von *trial_sequence* einem Durchgang entspricht, entspricht jede Zeile in unserer Schleifentabelle einem Durchgang. Jede Spalte entspricht einer Variablen, die in jedem Durchgang einen anderen Wert haben kann.

Aber wir sind noch nicht fertig. Wir müssen noch drei weitere Variablen hinzufügen: die Position des Distraktors, die korrekte Antwort und die Kongruenz.

- __dist_pos__ -- In der ersten Zeile der ersten leeren Spalte gibst du 'dist_pos' ein. Dadurch wird automatisch eine neue experimentelle Variable namens 'dist_pos' hinzugefügt. In den Zeilen darunter, gib '300' ein, wo 'target_pos' -300 ist, und '-300', wo 'target_pos' 300 ist. Mit anderen Worten, das Ziel und der Distraktor sollten sich gegenüber voneinander positioniert sein.
- __correct_response__ -- Erstelle eine weitere Variable in einer anderen leeren Spalte mit dem Namen 'correct_response'. Setze 'correct_response' auf 'z', wo 'target_letter' 'F' ist, und auf 'm', wo 'target_letter' 'H' ist. Das bedeutet, dass der Teilnehmer die Taste 'z' drücken sollte, wenn er ein 'F' sieht, und die Taste 'm', wenn er ein 'H' sieht. (Fühlen Sie sich frei, andere Tasten zu wählen, wenn 'z' und 'm' auf Ihrer Tastaturanordnung umständlich sind; zum Beispiel sind 'w' und 'n' besser auf AZERTY-Tastaturen geeignet.)
- __congruency__ -- Erstelle eine weitere Variable mit dem Namen 'congruency'. Setze 'congruency' auf 'congruent', wo 'target_pos' '-300' ist und 'gaze_cue' 'left', und wo 'target_pos' '300' ist und 'gaze_cue' 'right'. Mit anderen Worten, ein Versuch ist kongruent, wenn das Gesicht das Ziel betrachtet. Setze 'congruency' auf 'inkongruent' für die Versuche, bei denen das Gesicht den Distraktor anschaut. Die Variable 'congruency' ist nicht notwendig, um das Experiment auszuführen; sie ist jedoch nützlich, um die Daten später zu analysieren.

Wir müssen noch eine letzte Sache tun. 'Repeat' ist derzeit auf '1,00' eingestellt. Das bedeutet, dass jeder Zyklus einmal ausgeführt wird. Der Block besteht jetzt also aus 8 Versuchen, was etwas kurz ist. Eine angemessene Länge für einen Block von Versuchen ist 24, daher setze 'Repeat' auf 3,00 (3 Wiederholungen x 8 Zyklen = 24 Versuche). Du musst 'Order' nicht ändern, denn 'random' ist genau das, was wir wollen.

Die *block_loop* sieht jetzt aus wie %FigStep3. Denken Sie daran, Ihr Experiment regelmäßig zu speichern.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "Die *block_loop* am Ende von Schritt 3."
--%

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ -- Du kannst deine Loop-Tabelle in deinem bevorzugten Tabellenkalkulationsprogramm erstellen und sie in die LOOP-Variablentabelle kopieren und einfügen.

__Tipp__ -- Du kannst deine Loop-Tabelle in einer separaten Datei (im `.xlsx` oder `.csv` Format) angeben und diese Datei direkt verwenden. Um dies zu tun, wähle 'Datei' unter 'Quelle'.

__Tipp__ -- Du kannst 'Repeat' auf eine nicht-ganzzahlige Zahl setzen. Beispielsweise führst du durch Einstellen von 'Repeat' auf '0,5' nur die Hälfte der Versuche (zufällig ausgewählt) aus.

</div>

## Schritt 4: Bilder und Sounddateien zur Dateisammlung hinzufügen

Für unsere Reize verwenden wir Bilddateien. Zusätzlich spielen wir einen Ton ab, wenn der Teilnehmer einen Fehler macht. Dafür benötigen wir eine Audiodatei.

Die erforderlichen Dateien können hier heruntergeladen werden (in den meisten Webbrowsers kannst du mit der rechten Maustaste auf die Links klicken und "Link speichern unter" oder eine ähnliche Option wählen):

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Nachdem du diese Dateien heruntergeladen hast (zum Beispiel auf deinem Desktop), kannst du sie zur Dateisammlung hinzufügen. Wenn die Dateisammlung noch nicht sichtbar ist (standardmäßig auf der rechten Seite des Fensters), klicke auf die Schaltfläche "Dateisammlung anzeigen" in der Hauptwerkzeugleiste (Tastenkombination: `Strg+P`). Der einfachste Weg, die vier Dateien zur Dateisammlung hinzuzufügen, besteht darin, sie vom Desktop (oder von der Stelle, an der du die Dateien heruntergeladen hast) in die Dateisammlung zu ziehen. Alternativ kannst du auf die Schaltfläche '+' in der Dateisammlung klicken und Dateien über den Dateiauswahldialog hinzufügen, der erscheint. Die Dateisammlung wird automatisch mit deinem Experiment gespeichert.

Deine Dateisammlung sieht jetzt aus wie %FigStep4. Denken Sie daran, Ihr Experiment regelmäßig zu speichern.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "Die Dateisammlung am Ende von Schritt 4."
--%

## Schritt 5: Fülle die Versuchssequenz mit Elementen

Ein Versuch in unserem Experiment sieht wie folgt aus:

1. __Fixationspunkt__ -- 750 ms, SKETCHPAD-Element
2. __Neutraler Blick__ -- 750 ms, SKETCHPAD-Element
3. __Blick-Hinweis__ -- 500 ms, SKETCHPAD-Element
4. __Ziel__  -- 0 ms, SKETCHPAD-Element
5. __Antworterfassung__  -- TASTATUR_ANTWORT Element
6. __Geräusch abspielen, wenn die Antwort falsch war__ -- SAMPLER Element
7. __Antwort in Datei protokollieren__ -- LOGGER Element

Klicken Sie auf *trial_sequence* in der Übersicht, um den Tab *trial_sequence* zu öffnen. Nehmen Sie ein SKETCHPAD aus der Element-Symbolleiste und ziehen Sie es in die *trial_sequence*. Wiederholen Sie dies dreimal, sodass die *trial_sequence* vier SKETCHPADs enthält. Wählen Sie anschließend ein TASTATUR_ANTWORT Element, ein SAMPLER Element und ein LOGGER Element aus und hängen Sie sie an.

Noch einmal werden wir die neuen Elemente umbenennen, damit die *trial_sequence* einfach zu verstehen ist. Benennen Sie um:

- *new_sketchpad* in *fixation_dot*
- *new_sketchpad_1* in *neutral_gaze*
- *new_sketchpad_2* in *gaze_cue*
- *new_sketchpad_3* in *target*
- *new_keyboard_response* in *keyboard_response*
- *new_sampler* in *incorrect_sound*
- *new_logger* in *logger*

Standardmäßig werden Elemente immer ausgeführt, was durch den Run-if-Ausdruck `True` angezeigt wird. Für das Element *incorrect_sound* möchten wir das jedoch ändern, es sollte nur ausgeführt werden, wenn ein Fehler gemacht wurde. Um dies zu erreichen, müssen wir den "Run if"-Ausdruck in `correct == 0` im Tab *trial_sequence* ändern. Dies funktioniert, da das Element *keyboard_response* automatisch eine Variable `correct` erstellt, die auf `1` (correct), `0` (incorrect) oder `undefined` gesetzt ist (dies hängt von der Variablen `correct_response` ab, die in Schritt 3 definiert wurde). Das doppelte Gleichheitszeichen ist Python-Syntax und gibt an, dass Sie überprüfen möchten, ob die beiden Dinge gleich sind, in diesem Fall, ob die Variable ` correct` gleich 0 ist. Um einen Run-if-Ausdruck zu ändern, doppelklicken Sie darauf (Shortcut: `F3`).

Die *trial_sequence* sieht jetzt aus wie %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Was ist ein SKETCHPAD-Element?__ -- Ein SKETCHPAD wird verwendet, um visuelle Reize darzustellen: Text, geometrische Formen, Fixationspunkte, Gabor-Patches usw. Mit den integrierten Zeichenwerkzeugen können Sie auf dem SKETCHPAD zeichnen.

__Was ist ein TASTATUR_ANTWORT-Element?__ -- Mit einem TASTATUR_ANTWORT-Element wird eine einzelne Teilnehmerantwort von der Tastatur erfasst.

__Was ist ein SAMPLER-Element?__ -- Ein SAMPLER-Element spielt einen Ton aus einer Audiodatei ab.

__Was ist ein LOGGER-Element?__ -- Ein LOGGER-Element schreibt Daten in die Protokolldatei. Das ist sehr wichtig: Wenn Sie das LOGGER-Element vergessen, werden während des Experiments keine Daten protokolliert!

__Tipp__ -- Variablen und bedingte "if"-Ausdrücke sind sehr leistungsfähig! Um mehr darüber zu erfahren, sehen Sie:

- %link:manual/variables%

</div>

## Schritt 6: Zeichnen der SKETCHPAD-Elemente

Die in Schritt 5 erstellten SKETCHPAD-Elemente sind noch leer. Es ist Zeit für etwas Zeichnung!

__Hintergrundfarbe auf Weiß einstellen__

Klicken Sie auf *fixation_dot* in der Übersicht, um den zugehörigen Tab zu öffnen. Das SKETCHPAD ist noch dunkelgrau, während die heruntergeladenen Bilder einen weißen Hintergrund haben. Huch, wir haben vergessen, die Hintergrundfarbe des Experiments auf Weiß zu setzen (standardmäßig ist es dunkelgrau)! Klicken Sie auf 'Tutorial: Gaze cuing' in der Übersicht, um den Tab 'Allgemeine Eigenschaften' zu öffnen. Ändern Sie 'Vordergrund' in 'schwarz' und 'Hintergrund' in 'weiß'.

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ -- Für genauere Farbsteuerung können Sie auch die hexadezimale RGB-Notation verwenden (z.B. `#FF000` für Rot), verschiedene Farbräume verwenden oder das Farbauswahl-Tool verwenden. Siehe auch:

- %link:manual/python/canvas%

</div>

__Den Fixationspunkt zeichnen__

Gehen Sie zurück zum *fixation_dot*, indem Sie im Überblick auf *fixation_dot* klicken. Wählen Sie dann das Fixationspunkt-Element aus, indem Sie auf die Schaltfläche mit dem Fadenkreuz klicken. Wenn Sie Ihren Cursor über das Sketchpad bewegen, können Sie die Bildschirmkoordinaten oben rechts sehen. Setzen Sie die (Vordergrund-)Farbe auf "schwarz". Klicken Sie auf die Mitte des Bildschirms (0, 0), um einen zentralen Fixationspunkt zu zeichnen.

Ändern Sie abschließend das Feld "Dauer" von "Tastendruck" auf "745", da der Fixationspunkt für 750 ms angezeigt werden soll. Warten ... *Warum haben wir nicht einfach eine Dauer von 750 ms angegeben?* Der Grund dafür ist, dass die tatsächliche Anzeigepräsentationsdauer immer auf einen Wert aufgerundet wird, der mit der Bildwiederholfrequenz Ihres Monitors kompatibel ist. Das mag kompliziert klingen, aber für die meisten Zwecke genügen die folgenden Faustregeln:

1. Wählen Sie eine Dauer, die angesichts der Bildwiederholfrequenz Ihres Monitors möglich ist. Wenn beispielsweise die Bildwiederholfrequenz Ihres Monitors 60 Hz beträgt, bedeutet dies, dass jedes Bild 16,7 ms lang ist (= 1000 ms/60 Hz). Daher sollten Sie auf einem 60-Hz-Monitor immer eine Dauer wählen, die ein Vielfaches von 16,7 ms ist, wie z. B. 16,7, 33,3, 50, 100 usw.
2. Geben Sie im Dauerfeld des SKETCHPAD eine Dauer ein, die einige Millisekunden kürzer ist als das, worauf Sie abzielen. Wenn Sie also ein SKETCHPAD für 50 ms präsentieren möchten, wählen Sie eine Dauer von 45. Wenn Sie ein SKETCHPAD für 1000 ms präsentieren möchten, wählen Sie eine Dauer von 995. Et cetera.

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ - Für eine ausführliche Diskussion zum experimentellen Timing, siehe:

- %link:timing%

__Tipp__ - Die Dauer eines SKETCHPAD kann in Millisekunden angegeben werden, aber Sie können auch "keypress" oder "mouseclick" eingeben, um einen Tastendruck oder einen Mausklick zu erfassen. In diesem Fall funktioniert ein SKETCHPAD ähnlich wie ein KEYBOARD_RESPONSE-Element (jedoch mit weniger Optionen).

__Tipp__ - Stellen Sie sicher, dass die (Vordergrund-)Farbe auf Schwarz eingestellt ist. Andernfalls zeichnen Sie Weiß auf Weiß und sehen nichts!

</div>

__Zeichnen des neutralen Blicks__

Öffnen Sie das *neutral_gaze* SKETCHPAD. Wählen Sie nun das Bildwerkzeug aus, indem Sie auf die Schaltfläche mit dem berglandschaftsartigen Symbol klicken. Klicken Sie auf die Mitte des Bildschirms (0, 0). Das Dialogfeld "Datei aus dem Pool auswählen" wird angezeigt. Wählen Sie die Datei `gaze_neutral.png` und klicken Sie auf die Schaltfläche "Auswählen". Das neutrale Blickbild wird nun von der Mitte des Bildschirms auf Sie blicken! Ändern Sie schließlich, wie zuvor, das Feld "Dauer" von "Tastendruck" auf "745". (Und beachten Sie erneut, dass dies auf den meisten Monitoren eine Dauer von 750 ms bedeutet!)

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ - OpenSesame kann eine Vielzahl von Bildformaten verarbeiten. Allerdings ist bekannt, dass einige (nicht standardmäßige) `.bmp`-Formate Probleme verursachen. Wenn Sie feststellen, dass ein `.bmp`-Bild nicht angezeigt wird, können Sie es in ein anderes Format konvertieren, z. B. `.png`. Mit kostenlosen Tools wie [GIMP] können Sie Bilder einfach umwandeln.
</div>

__Zeichnen des Blick-Hinweises__

Öffnen Sie das *gaze_cue* SKETCHPAD und wählen Sie erneut das Bildwerkzeug aus. Klicken Sie auf die Mitte des Bildschirms (0, 0) und wählen Sie die Datei `gaze_left.png`.

Wir sind aber noch nicht fertig! Denn der Blick-Hinweis sollte nicht immer "links" sein, sondern sollte von der Variable `gaze_cue` abhängen, die wir in Schritt 3 definiert haben. Indem wir das Bild `gaze_left.png` auf das SKETCHPAD gezeichnet haben, haben wir jedoch ein Skript generiert, das nur eine kleine Änderung benötigt, um sicherzustellen, dass das richtige Bild angezeigt wird. Klicken Sie auf die Schaltfläche "Ansicht auswählen" oben rechts auf der Registerkarte *gaze_cue* und wählen Sie "Skript anzeigen". Sie sehen nun das Skript, das dem Sketchpad entspricht, das wir gerade erstellt haben:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Das Einzige, was wir tun müssen, ist `gaze_left.png` durch `gaze_{gaze_cue}.png` zu ersetzen. Das bedeutet, dass OpenSesame die Variable `gaze_cue` (die die Werte `left` und `right` hat) verwendet, um zu bestimmen, welches Bild angezeigt werden soll.

Während wir dabei sind, können wir die Dauer auch auf '495' ändern (aufgerundet auf 500!). Das Skript sieht jetzt so aus:

~~~ .python
set duration 495
set description "Zeigt Reize an"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Klicken Sie auf die Schaltfläche 'Übernehmen' oben rechts, um Ihre Änderungen am Skript anzuwenden und zu den regulären Elementsteuerungen zurückzukehren. OpenSesame warnt Sie, dass das Bild nicht angezeigt werden kann, weil es mit Variablen definiert ist, und stattdessen wird ein Platzhalterbild angezeigt. Machen Sie sich keine Sorgen, im Experiment wird das richtige Bild angezeigt!

<div class='info-box' markdown='1'>

__Hintergrundbox__

__Tipp__ -- Der Variableninspektor (Tastenkombination: `Strg+I`) ist eine leistungsstarke Möglichkeit, herauszufinden, welche Variablen in Ihrem Experiment definiert wurden und welche Werte sie haben (siehe %FigVariableInspector). Wenn Ihr Experiment nicht läuft, haben die meisten Variablen noch keinen Wert. Wenn Sie jedoch Ihr Experiment in einem Fenster ausführen und dabei den Variableninspektor sichtbar lassen, können Sie die Variablen in Echtzeit ändern sehen. Das ist sehr nützlich für das Debuggen Ihres Experiments.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "Der Variableninspektor ist eine praktische Möglichkeit, einen Überblick über die Variablen zu erhalten, die in Ihrem Experiment vorhanden sind."
--%

</div>

__Das Ziel darstellen__

Wir möchten, dass drei Objekte Teil der Zielanzeige sind: der Zielbuchstabe, der Ablenkbuchstabe und der Blickhinweis (siehe %FigGazeCuing). Wie zuvor werden wir zunächst eine statische Anzeige mit dem SKETCHPAD-Editor erstellen. Danach müssen wir nur noch kleinere Änderungen am Skript vornehmen, damit die genaue Anzeige von den Variablen abhängt.

Klicken Sie auf *target* in der Übersicht, um den Target-Tab zu öffnen, und zeichnen Sie wie zuvor das Bild `gaze_left.png` in der Mitte des Bildschirms. Wählen Sie nun das Textzeichnungswerkzeug aus, indem Sie auf die Schaltfläche mit dem 'A'-Symbol klicken. Ändern Sie die Vordergrundfarbe in 'schwarz' (falls sie noch nicht schwarz ist). Die Standard-Schriftgröße beträgt 18 px, was für unseren Zweck etwas klein ist, daher ändern Sie die Schriftgröße auf 32 px. Klicken Sie jetzt auf (-320, 0) im SKETCHPAD (die X-Koordinate muss nicht genau 320 betragen, da wir diese sowieso in eine Variable ändern werden). Geben Sie "{target_letter}" in den Dialog ein, um den Zielbuchstaben zu zeichnen (beim Zeichnen von Text können Sie Variablen direkt verwenden). Klicken Sie auf die gleiche Weise auf (320, 0) und ziehen Sie ein 'X' (der Distraktor ist immer ein 'X').

Öffnen Sie nun den Skripteditor, indem Sie oben rechts auf die Schaltfläche 'Ansicht auswählen' klicken und 'Skript anzeigen' auswählen. Das Skript sieht folgendermaßen aus:

~~~ .python
set duration keypress
set duration keypress
set description "Zeigt Reize an"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

Ändern Sie wie zuvor `gaze_left.png` in `gaze_{gaze_cue}.png`. Wir müssen auch die Position des Ziels und des Ablenkers in Abhängigkeit von den Variablen `target_pos` und `dist_pos` ändern. Um dies zu tun, ändern Sie einfach `-320` in `{target_pos}` und `320` in `{dist_pos}`. Achten Sie darauf, dass Sie die `0` belassen, die die Y-Koordinate ist. Das Skript sieht jetzt so aus:

~~~ .python
set duration keypress
set description "Zeigt Reize an"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

Klicken Sie auf die Schaltfläche 'Anwenden', um das Skript anzuwenden und zurück zu den regulären Elementsteuerungen zu gelangen.

Schließlich setzen Sie das Feld "Duration" auf "0". Das bedeutet nicht, dass das Ziel nur für 0 ms präsentiert wird, sondern dass das Experiment sofort zum nächsten Element (dem *keyboard_response*) übergeht. Da das *keyboard_response* auf eine Antwort wartet, aber nicht ändert, was auf dem Bildschirm zu sehen ist, bleibt das Ziel sichtbar, bis eine Antwort gegeben wurde.

Denken Sie daran, Ihr Experiment regelmäßig zu speichern.

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ -- Jedes Element eines SKETCHPAD hat eine "Show if"-Option, die angibt, wann das Element angezeigt werden soll. Sie können dies verwenden, um Elemente in einem SKETCHPAD abhängig von bestimmten Variablen ein- oder auszublenden, ähnlich wie Run-if-Anweisungen in einer SEQUENCE.

__TIPP__ -- Stellen Sie sicher, dass die (Vordergrund-)Farbe auf Schwarz eingestellt ist. Andernfalls zeichnen Sie Weiß auf Weiß und sehen nichts!

</div>

## Schritt 7: Konfigurieren des Keyboard-Response-Elements

Klicken Sie auf *keyboard_response* in der Übersicht, um dessen Registerkarte zu öffnen. Sie sehen drei Optionen: Correct response, Allowed responses, Timeout und Event type.

Wir haben bereits die Variable `correct_response` in Schritt 3 gesetzt. Wenn wir keine korrekte Antwort explizit angeben, verwendet OpenSesame automatisch die Variable `correct_response`, wenn sie verfügbar ist. Daher müssen wir das Feld "Correct response" hier nicht ändern.

Wir müssen jedoch die erlaubten Antworten einstellen. Geben Sie "z;m" in das Feld für erlaubte Antworten ein (oder andere Tasten, wenn Sie andere Antworttasten gewählt haben). Das Semikolon wird verwendet, um Antworten zu trennen. Das KEYBOARD_RESPONSE akzeptiert jetzt nur noch die Tasten "z" und "m". Alle anderen Tastendrücke werden ignoriert, mit Ausnahme von "escape", das das Experiment pausiert.

Wir möchten auch ein Timeout setzen, das das maximale Intervall ist, das das KEYBOARD_RESPONSE wartet, bevor es entscheidet, dass die Antwort inkorrekt ist und die Variable "response" auf "None" setzt. "2000" (ms) ist ein guter Wert.

Wir müssen den Eventtyp nicht ändern, weil wir möchten, dass der Teilnehmer durch Drücken einer Taste antwortet (Tastendruck, der Standard) und nicht durch Loslassen einer Taste (Tastenfreigabe).

Das KEYBOARD_RESPONSE sieht jetzt aus wie %FigSchritt7.

%--
figure:
 id: FigSchritt7
 source: step7.png
 caption: "Das KEYBOARD_RESPONSE am Ende von Schritt 7."
--%

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ -- Standardmäßig verwendet das KEYBOARD_RESPONSE die Variable `correct_response`, um festzustellen, ob eine Antwort korrekt war. Sie können jedoch auch eine andere Variable verwenden. Um dies zu tun, geben Sie einen Variablennamen in geschweiften Klammern (`{my_variable}`) in das Feld für die korrekte Antwort ein.

__Tipp__ -- Wenn "Flush pending key presses" aktiviert ist (standardmäßig ist es aktiviert), werden alle ausstehenden Tastendrücke verworfen, wenn das KEYBOARD_RESPONSE-Element aufgerufen wird. Dies verhindert Carry-over-Effekte, die sonst auftreten könnten, wenn der Teilnehmer versehentlich während eines Nicht-Antwort-Teils des Versuchs eine Taste drückt.

__Tipp__ -- Um spezielle Tasten wie `/` oder die Hoch-Pfeil-Taste zu verwenden, können Sie Tastennamen (z. B. "up" und "space") oder zugeordnete Zeichen (z. B. `/` und `]`) verwenden. Die Schaltfläche "List available keys" bietet eine Übersicht über alle gültigen Tastennamen.

</div>

## Schritt 8: Konfigurieren des Inkorrekt-Samplers

Das *incorrect_sound*-Element braucht nicht viel Arbeit: Wir müssen nur den Ton auswählen, der abgespielt werden soll. Klicken Sie auf *incorrect_sound* in der Übersicht, um dessen Registerkarte zu öffnen. Klicken Sie auf die Schaltfläche "Durchsuchen" und wählen Sie `incorrect.ogg` aus dem Datei-Pool.

Der Sampler sieht jetzt aus wie %FigSchritt8.

%--
figure:
 id: FigSchritt8
 source: step8.png
 caption: "Das *incorrect_sound*-Element am Ende von Schritt 8."
--%

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ -- Sie können Variablen verwenden, um anzugeben, welcher Ton abgespielt werden soll, indem Sie einen Variablennamen in geschweiften Klammern als (Teil des) Dateinamens verwenden. Zum Beispiel: `{a_word}.ogg`

__Tipp__ -- Der SAMPLER behandelt Dateien in den Formaten `.ogg`, `.mp3` und `.wav`. Wenn Sie Audiodateien in einem anderen Format haben, ist [Audacity] ein großartiges kostenloses Tool zum Konvertieren von Audiodateien (und vielem mehr).

</div>

## Schritt 9: Konfiguration des Variable Loggers

Tatsächlich müssen wir den Variable LOGGER nicht konfigurieren, aber wir werfen trotzdem einen Blick darauf. Klicken Sie auf *logger* in der Übersicht, um die Registerkarte zu öffnen. Sie sehen, dass die Option "Automatisch alle Variablen protokollieren" ausgewählt ist. Das bedeutet, dass OpenSesame alles protokolliert, was in Ordnung ist.

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ -- Wenn Sie Ihre Log-Dateien übersichtlich halten möchten, können Sie die Option "Automatisch alle Variablen protokollieren" deaktivieren und Variablen manuell auswählen, indem Sie entweder Variablennamen manuell eingeben ("Benutzerdefinierte Variable hinzufügen") oder Variablen aus dem Variableninspektor in die LOGGER-Tabelle ziehen. Sie können auch die Option "Automatisch alle Variablen protokollieren" aktiviert lassen und Variablen, an denen Sie nicht interessiert sind, ausschließen.

__Der ultimative Tipp__ -- Überprüfen Sie immer dreifach, ob alle notwendigen Variablen in Ihrem Experiment protokolliert werden! Der beste Weg, dies zu überprüfen, besteht darin, das Experiment auszuführen und die daraus resultierenden Log-Dateien zu untersuchen.

</div>

## Schritt 10: Zeichnen des Feedback-Elements

Nach jedem Block von Versuchen möchten wir dem Teilnehmer Feedback geben, um ihm/ ihr mitzuteilen, wie gut er/ sie abschneidet. Daher haben wir in Schritt 2 ein FEEDBACK-Element namens *feedback* am Ende von *block_sequence* hinzugefügt.

Klicken Sie auf *feedback* in der Übersicht, um die Registerkarte zu öffnen, wählen Sie das Zeichnen von Textwerkzeug aus, ändern Sie die Vordergrundfarbe auf "schwarz" (falls noch nicht geschehen) und klicken Sie auf (0, 0). Geben Sie nun den folgenden Text ein:

```text
Ende des Blocks

Deine durchschnittliche Reaktionszeit betrug {avg_rt} ms
Deine Genauigkeit lag bei {acc} %

Drücke eine beliebige Taste, um fortzufahren
```

Da wir möchten, dass das Feedback-Element so lange sichtbar bleibt, wie der Teilnehmer möchte (d. h. bis er/sie eine Taste drückt), belassen wir das Feld "Dauer" auf "keypress".

Das Feedback-Element sieht jetzt aus wie %FigStep_10.

%--
abbildung:
 id: FigStep_10
 source: step10.png
 caption: "Das Feedback-Element am Ende von Schritt 10."
--%

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Was ist ein Feedback-Element?__ -- Ein FEEDBACK-Element ist fast identisch mit einem SKETCHPAD-Element. Der einzige Unterschied besteht darin, dass ein FEEDBACK-Element nicht im Voraus vorbereitet wird. Das bedeutet, dass Sie es verwenden können, um Feedback zu präsentieren, das aktuelle Informationen über die Reaktion eines Teilnehmers erfordert. Sie sollten FEEDBACK-Elemente nicht verwenden, um zeitkritische Anzeigen zu präsentieren, da die Tatsache, dass es nicht im Voraus vorbereitet wird, bedeutet, dass seine zeitlichen Eigenschaften nicht so gut sind wie die des SKETCHPAD-Elements. Siehe auch:

- %link:visual%

__Feedback und Variablen__ -- Antwortelemente behalten automatisch die Genauigkeit und durchschnittliche Reaktionszeit des Teilnehmers in den Variablen "acc" (Synonym: "Genauigkeit") und "avg_rt" (Synonym: "average_response_time") bei. Siehe auch:

- %link:manual/variables%

__Tipp__ -- Stellen Sie sicher, dass die (Vordergrund-)Farbe auf Schwarz eingestellt ist. Andernfalls zeichnen Sie weiß auf weiß und sehen nichts!

</div>

## Schritt 11: Festlegen der Länge der Übungsphase und der Experimentierphase

Wir haben zuvor die Elemente *practice_loop* und *experiment_loop* erstellt, die beide *block_sequence* aufrufen (d. h. einen Block von Versuchen). Derzeit rufen sie jedoch nur einmal *block_sequence* auf, was bedeutet, dass sowohl die Übungsphase als auch die Experimentierphase nur aus einem einzigen Block von Versuchen bestehen.

Klicken Sie auf *practice_loop*, um die Registerkarte zu öffnen, und setzen Sie "Wiederholung" auf "2,00". Das bedeutet, dass die Übungsphase aus zwei Blöcken besteht.

Klicken Sie auf *experimental_loop*, um die Registerkarte zu öffnen, und setzen Sie "Wiederholung" auf "8,00". Das bedeutet, dass die Experimentierphase aus acht Blöcken besteht.

<div class='info-box' markdown='1'>

__Hintergrund-Box__

__Tipp__ -- Sie können in den Elementen *practice_loop* und *experimental_loop* eine Variable `practice` erstellen und sie jeweils auf "ja" und "nein" setzen. Dies ist eine einfache Möglichkeit, den Überblick darüber zu behalten, welche Versuche Teil der Übungsphase waren.

</div>

## Schritt 12: Schreiben Sie die Anweisungen, end_of_practice und end_of_experiment Formulare

Ich denke, du kannst diesen Schritt alleine bewältigen! Öffne einfach die entsprechenden Elemente und füge Text hinzu, um Anweisungen, eine Endnachricht für die Übung und eine Endnachricht für das Experiment zu präsentieren.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Du kannst einige HTML-Tags verwenden, um deinen Text zu formatieren. Zum Beispiel wird *&lt;b&gt;dies wird fett dargestellt&lt;b&gt;* und *&lt;span color='red'&gt;dies wird rot sein&lt;span&gt;*. Weitere Informationen findest du unter:

- %link:text%

</div>

## Schritt 13: Führe das Experiment aus!

Fertig! Klicke auf die Schaltflächen 'In Fenster ausführen' (Shortcut: `Ctrl+W`) oder 'Vollbild ausführen' (Shortcut: `Ctrl+R`) in der Symbolleiste, um dein Experiment auszuführen.

<div class='info-box' markdown='1'>

__Hintergrundkasten__

__Tipp__ -- Ein Testlauf wird noch schneller ausgeführt, indem du auf die orangefarbene Schaltfläche "In Fenster ausführen" klickst (Shortcut: `Ctrl+Shift+W`), die dich nicht fragt, wie das Logfile gespeichert werden soll (und sollte daher nur für Testzwecke verwendet werden).

</div>


## Fehler verstehen

Fehlermeldungen verstehen zu können, ist eine wichtige Fähigkeit beim Arbeiten mit OpenSeame. Schließlich läuft ein neu erstelltes Experiment selten sofort ohne Fehler!

Nehmen wir an, wir haben bei einem der oben genannten Schritte einen Fehler gemacht. Beim Versuch, das Experiment auszuführen, erhalten wir die folgende Fehlermeldung (%FigErrorMessage):

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "Eine Fehlermeldung in OpenSesame."
--%

Die Fehlermeldung beginnt mit einem Namen, in diesem Fall `FStringError`, der den allgemeinen Fehler-Typ angibt. Dies wird gefolgt von einem kurzen Erläuterungstext, in diesem Fall "Fehlgeschlagene Auswertung des f-string-Ausdrucks im folgenden Text: gaze_{gaze_ceu}.png". Auch ohne zu verstehen, was ein f-string ist (es ist eine Zeichenkette, die Python-Code zwischen geschweiften Klammern enthält), ist klar, dass mit dem Text '{gaze_ceu}.png' etwas nicht stimmt.

Die Fehlermeldung zeigt auch an, dass der Fehler aus der Vorbereitungsphase des *gaze_cue* Elements kommt.

Schließlich zeigt die Fehlermeldung an, was genau schiefgelaufen ist, als der Text 'gaze_{gaze_ceu}.png' ausgewertet wurde: Der Name "gaze_ceu" ist nicht definiert.

Beim sorgfältigen Lesen der Fehlermeldung sind Ihnen wahrscheinlich bereits Ursache und Lösung in den Sinn gekommen: Wir haben einen einfachen Schreibfehler im *gaze_cue* Element gemacht und '{gaze_ceu}' statt '{gaze_cue}' geschrieben! Dies führte zu einem Fehler, weil keine Variable mit dem Namen `gaze_ceu` existiert. Dies kann leicht behoben werden, indem Sie das Skript des *gaze_cue* Elements öffnen und den Tippfehler korrigieren.


## Abschließend: Einige allgemeine Überlegungen zur Timing- und Backend-Auswahl

Im Reiter "Allgemeine Eigenschaften" des Experiments (der Reiter, den du öffnest, indem du auf den Namen des Experiments klickst), kannst du ein Backend auswählen. Das Backend ist die Softwareebene, die die Anzeige, Eingabegeräte, Ton usw. steuert. Die meisten Experimente funktionieren mit allen Backends, aber es gibt Gründe, ein Backend gegenüber einem anderen zu bevorzugen, vor allem in Bezug auf das Timing. Derzeit gibt es vier Backends (abhängig von deinem System sind möglicherweise nicht alle drei verfügbar):

- __psycho__ -- ein hardwarebeschleunigtes Backend auf Basis von PsychoPy [(Peirce, 2007)][references]. Dies ist die Standardeinstellung.
- __xpyriment__ -- ein hardwarebeschleunigtes Backend auf Basis von Expyriment [(Krause & Lindeman, 2013)][references]
- __legacy__ -- ein "sicheres" Backend, basierend auf PyGame. Es bietet eine zuverlässige Leistung auf den meisten Plattformen, aber aufgrund fehlender Hardwarebeschleunigung sind die Zeitgebungseigenschaften nicht so gut wie bei den anderen Backends.
- __osweb__ -- führt Experimente in einem Browser aus [(Mathôt & March, 2022)][references].

Siehe auch:

- %link:backends%
- %link:timing%


## Referenzen

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Beurteilung der Auswirkungen technischer Varianz auf die statistischen Ergebnisse von Web-Experimenten, die Reaktionszeiten messen. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Überwiegt die Variabilität in der menschlichen Leistung die Ungenauigkeit von Antwortgeräten wie Computertastaturen? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). Die Augen haben es! Reflexive Orientierung wird durch nichtvorhersagenden Blick ausgelöst. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: Eine Python-Bibliothek für kognitive und neurowissenschaftliche Experimente. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Ein Open-Source-, grafischer Experimentbuilder für die Sozialwissenschaften. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Durchführung linguistischer Experimente online mit OpenSesame und OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysik-Software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Zeitauflösung von Uhren: Auswirkungen auf die Messung der Reaktionszeit - Gute Nachrichten für schlechte Uhren. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[referenzen]: #referenzen
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about