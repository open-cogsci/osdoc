title: Katzen, Hunde und Capybaras
uptodate: false
hash: 66f26fecbe543127ecd03e1ed499f5e5ab9f112189ee97bc58925aeb119dddac
locale: de
language: German

%--
Abbildung:
 ID: FigCapybara
 Quelle: capybara.png
 Bildunterschrift: |
  Ein Capybara.
--%

[TOC]

## Über

Wir erstellen eine einfache, mit Tieren gefüllte multisensorische Integrationaufgabe, bei der die Teilnehmer ein Bild von einem Hund, einer Katze oder einem Capybara sehen. Während das Bild gezeigt wird, wird ein Miauen oder Bellen abgespielt. Der Teilnehmer meldet, ob ein Hund oder eine Katze gezeigt wird, indem er mit der Maus auf eine Antwortschaltfläche auf dem Bildschirm klickt. Bei der Anzeige eines Capybaras sollte keine Antwort gegeben werden: Dies sind Kontrollversuche.

Wir stellen zwei einfache Vorhersagen:

- Die Teilnehmer sollten schneller Hunde identifizieren, wenn ein Bellgeräusch abgespielt wird, und schneller Katzen identifizieren, wenn ein Miaugeräusch abgespielt wird. Mit anderen Worten, wir erwarten einen multisensorischen Kongruenzeffekt.
- Wenn die Teilnehmer ein Capybara sehen, melden sie wahrscheinlicher, dass sie einen Hund sehen, wenn sie ein Bellen hören, und wahrscheinlicher, dass sie eine Katze sehen, wenn sie ein Miauen hören. Mit anderen Worten, Fehlalarme werden durch den Klang beeinflusst.

## Tutorial

### Schritt 1: Herunterladen und starten von OpenSesame

OpenSesame ist verfügbar für Windows, Linux, Mac OS und Android (nur Laufzeit). Dieses Tutorial wurde für OpenSesame 3.3.X geschrieben. Sie können OpenSesame hier herunterladen:

- %link:download%

Wenn Sie OpenSesame starten, erhalten Sie eine Auswahl an Vorlagenexperimenten und (falls vorhanden) eine Liste kürzlich geöffneter Experimente (siehe %FigStartUp).

%--
Abbildung:
 ID: FigStartUp
 Quelle: start-up.png
 Bildunterschrift: |
  Das OpenSesame-Fenster beim Start.
--%

Die *Erweiterte Vorlage* bietet einen guten Ausgangspunkt für die Erstellung von versuchsbasierten Experimenten. In diesem Tutorial werden wir jedoch das gesamte Experiment von Grund auf neu erstellen. Daher fahren wir mit der "Standardvorlage" fort, die bereits geladen ist, wenn OpenSesame gestartet wird (%FigDefaultTemplate). Schließen Sie daher einfach die Registerkarten "Los geht's!" und (falls angezeigt) "Willkommen!".

%--
Abbildung:
 ID: FigDefaultTemplate
 Quelle: default-template.png
 Bildunterschrift: |
  Die Struktur der "Standardvorlage", wie sie im Übersichtsbereich zu sehen ist.
--%

<div class='info-box' markdown='1'>

**Hintergrundkasten 1: Grundlagen**

OpenSesame-Experimente sind Sammlungen von *Elementen*. Ein Element ist ein kleiner Funktionsblock, der beispielsweise zum Präsentieren visueller Reize (das SKETCHPAD-Element) oder zum Aufzeichnen von Tastendrücken (das KEYBOARD_RESPONSE-Element) verwendet werden kann. Elemente haben eine Art und einen Namen. Beispielsweise könnten Sie zwei Elemente des Typs KEYBOARD_RESPONSE mit den Namen *t1_response* und *t2_response* haben. Um den Unterschied zwischen Elementtypen und Elementnamen deutlich zu machen, verwenden wir DIESEN_STIL für Typen und *diesen Stil* für Namen.

Um Ihrem Experiment Struktur zu verleihen, sind zwei Arten von Elementen besonders wichtig: die LOOP und die SEQUENCE. Zu verstehen, wie LOOPs und SEQUENCEs kombiniert werden können, um Experimente zu erstellen, ist vielleicht der kniffligste Teil der Arbeit mit OpenSesame. Versuchen wir also, das zuerst zu klären.

Eine LOOP ist, wo in den meisten Fällen Ihre unabhängigen Variablen definiert werden. In einer LOOP können Sie eine Tabelle erstellen, in der jede Spalte einer Variablen entspricht und jede Zeile einem einzelnen Durchlauf des "Elements zum Ausführen" entspricht. Um das konkreter zu machen, betrachten wir die folgende *block_loop* (unabhängig von diesem Tutorial):

%--
Abbildung:
 ID: FigLoopTable
 Quelle: loop-table.png
 Bildunterschrift: |
  Ein Beispiel für Variablen, die in einer Loop-Tabelle definiert sind. (Dieses Beispiel hat nichts mit dem im Tutorial erstellten Experiment zu tun.)
--%

Diese *block_loop* wird *trial_sequence* vier Mal ausführen. Einmal, während `soa` 100 und `target` 'F' ist, einmal während `soa` 100 und `target` 'H' ist usw. Die Reihenfolge, in der die Zeilen durchlaufen werden, ist standardmäßig zufällig, kann aber auch in der rechten oberen Ecke der Registerkarte auf sequenziell eingestellt werden.

Eine SEQUENCE besteht aus einer Reihe von Elementen, die nacheinander ausgeführt werden. Eine prototypische SEQUENCE ist die *trial_sequence*, die einem einzelnen Versuch entspricht. Zum Beispiel könnte eine einfache *trial_sequence* aus einem SKETCHPAD bestehen, um einen Reiz darzustellen, einem KEYBOARD_RESPONSE, um eine Antwort zu erfassen, und einem LOGGER, um die Versuchsinformationen in die Protokolldatei zu schreiben.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  Ein Beispiel für ein SEQUENCE-Element, das als Versuchssequenz verwendet wird. (Dieses Beispiel steht nicht im Zusammenhang mit dem in diesem Tutorial erstellten Experiment.)
--%

Sie können LOOPs und SEQUENCEs hierarchisch kombinieren, um Versuchsblöcke und Übungs- und Experimentalphasen zu erstellen. Zum Beispiel wird die *trial_sequence* von der *block_loop* aufgerufen. Zusammen entsprechen diese einem einzelnen Block von Versuchen. Eine Ebene höher wird die *block_sequence* von der *practice_loop* aufgerufen. Zusammen entsprechen diese der Übungsphase des Experiments.

</div>


### Schritt 2: Fügen Sie eine block_loop und trial_sequence hinzu

Die Standardvorlage beginnt mit drei Elementen: Einem NOTEPAD namens *getting_started*, einem SKETCHPAD namens *welcome* und einer SEQUENCE namens *experiment*. Wir benötigen *getting_started* und *welcome* nicht, also lassen Sie uns diese gleich entfernen. Klicken Sie dazu mit der rechten Maustaste auf diese Elemente und wählen Sie 'Löschen'. Entfernen Sie nicht *experiment*, da es der Einstiegspunkt für das Experiment ist (d.h. das erste Element, das aufgerufen wird, wenn das Experiment gestartet wird).

Unser Experiment hat eine sehr einfache Struktur. An der Spitze der Hierarchie steht eine LOOP, die wir *block_loop* nennen werden. Die *block_loop* ist der Ort, an dem wir unsere unabhängigen Variablen definieren werden (siehe auch Hintergrundkasten 1). Um eine LOOP zu Ihrem Experiment hinzuzufügen, ziehen Sie das LOOP-Symbol aus der Item-Menüleiste auf das *experiment* Element im Überblicksbereich.

Ein LOOP-Element benötigt ein weiteres Element zum Ausführen; normalerweise, und in diesem Fall auch, handelt es sich dabei um eine SEQUENCE. Ziehen Sie das SEQUENCE-Element aus der Item-Menüleiste auf das *new_loop* Element im Überblicksbereich. OpenSesame fragt, ob Sie die SEQUENCE in die oder nach der LOOP einfügen möchten. Wählen Sie "In new_loop einfügen".

Standardmäßig haben Elemente Namen wie *new_sequence*, *new_loop*, *new_sequence_2*, usw. Diese Namen sind nicht sehr informativ, und es ist ratsam, sie umzubenennen. Elementnamen müssen aus alphanumerischen Zeichen und/ oder Unterstrichen bestehen. Um einen Elementnamen zu ändern, doppelklicken Sie auf das Element im Überblicksbereich. Benennen Sie *new_sequence* in *trial_sequence* um, um anzuzeigen, dass es einem einzelnen Versuch entsprechen wird. Benennen Sie *new_loop* in *block_loop* um, um anzuzeigen, dass es einem Block von Versuchen entsprechen wird.

Der Überblicksbereich unseres Experiments sieht jetzt aus wie in %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  Der Überblicksbereich am Ende von Schritt 2.
--%

<div class='info-box' markdown='1'>

**Hintergrundkasten 3: Unbenutzte Elemente**

__Tipp__ — Gelöschte Elemente sind noch im Unbenutzte Elemente-Tab verfügbar, bis Sie "Unbenutzte Elemente dauerhaft löschen" im Unbenutzte Elemente-Tab auswählen. Sie können gelöschte Elemente zu Ihrem Experiment hinzufügen, indem Sie sie aus dem Unbenutzte Elemente-Tab in eine SEQUENCE oder LOOP ziehen.

</div>

### Schritt 3: Importieren von Bildern und Sound-Dateien

Für dieses Experiment verwenden wir Bilder von Katzen, Hunden und Capybaras. Wir werden auch Sound-Beispiele von Miauen und Bellen verwenden. Sie können alle benötigten Dateien von hier herunterladen:

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

Laden Sie `stimuli.zip` herunter und entpacken Sie es irgendwo (zum Beispiel auf Ihrem Desktop). Klicken Sie anschließend in OpenSesame auf die Schaltfläche "Datei-Pool anzeigen" in der Hauptsymbolleiste (oder: Menü → Ansicht → Datei-Pool anzeigen). Dadurch wird der Datei-Pool standardmäßig auf der rechten Seite des Fensters angezeigt. Der einfachste Weg, die Reize zum Datei-Pool hinzuzufügen, besteht darin, sie vom Desktop (oder wo immer Sie die Dateien extrahiert haben) in den Datei-Pool zu ziehen. Alternativ können Sie auf die Schaltfläche '+' im Datei-Pool klicken und Dateien über den angezeigten Dateiauswahldialog hinzufügen. Der Datei-Pool wird automatisch mit Ihrem Experiment gespeichert.

Nachdem Sie alle Reize hinzugefügt haben, sieht Ihr Datei-Pool wie in %FigStep4 aus.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  The file pool at the end of Step 3.
--%

### Schritt 4: Definieren Sie die experimentellen Variablen in der Blockschleife

Konzeptionell hat unser Experiment ein vollständig gekreuztes 3×2-Design: Wir haben drei Arten von visuellen Reizen (Katzen, Hunde und Capybaras), die in Kombination mit zwei Arten von akustischen Reizen (Miauen und Bellen) auftreten. Wir haben jedoch fünf Exemplare für jeden Reiztyp: fünf Miau-Geräusche, fünf Capybara-Bilder usw. Aus technischer Sicht ergibt es daher Sinn, unser Experiment als 5×5×3×2-Design zu betrachten, bei dem die Bildnummer und die Tonnummer Faktoren mit fünf Ebenen sind.

OpenSesame ist sehr gut darin, vollfaktorielle Designs zu generieren. Öffnen Sie zuerst *block_loop*, indem Sie darauf in der Übersichtsfläche klicken. Klicken Sie anschließend auf die Schaltfläche Vollfaktorielles Design. Dadurch wird ein Assistent zum Erstellen von vollfaktoriellen Designs geöffnet, der auf einfache Weise funktioniert: Jede Spalte entspricht einer experimentellen Variable (d. h. einem Faktor). Die erste Zeile ist der Name der Variablen, die Zeilen darunter enthalten alle möglichen Werte (d. h. Ebenen). In unserem Fall können wir unser 5×5×3×2-Design wie in %FigLoopWizard angegeben spezifizieren.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  The loop wizard generates full-factorial designs.
--%

Nachdem Sie auf "Ok" geklickt haben, sehen Sie, dass es jetzt eine LOOP-Tabelle mit vier Zeilen gibt, eine für jede experimentelle Variable. Es gibt 150 Zyklen (=5×5×3×2), was bedeutet, dass wir 150 einzigartige Versuche haben. Ihre LOOP-Tabelle sieht jetzt aus wie in %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  The LOOP table at the end of Step 4.
--%

### Schritt 5: Elemente zur Versuchssequenz hinzufügen

Öffnen Sie *trial_sequence*, das noch leer ist. Es ist Zeit, einige Elemente hinzuzufügen! Unsere grundlegende *trial_sequence* besteht aus:

1. Einem SKETCHPAD zur Anzeige eines zentralen Fixationspunkts für 500 ms
2. Einem SAMPLER zum Abspielen eines Tiergeräusches
3. Einem SKETCHPAD zur Anzeige eines Tierbildes
4. Eine MOUSE_RESPONSE, um eine Antwort zu erfassen
5. Ein LOGGER, um die Daten in eine Datei zu schreiben

Um diese Elemente hinzuzufügen, ziehen Sie sie einfach nacheinander aus der Elementleiste in die *trial_sequence*. Wenn Sie versehentlich Elemente an der falschen Stelle ablegen, können Sie sie einfach durch Ziehen und Ablegen neu anordnen. Benennen Sie jedes Element sinnvoll, sobald alle Elemente in der richtigen Reihenfolge sind. Die Übersichtsfläche sieht jetzt aus wie in %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  The overview area at the end of Step 5.
--%

### Schritt 6: Definieren Sie den zentralen Fixationspunkt

Klicken Sie auf *fixation_dot* im Übersichtsbereich. Dies öffnet eine einfache Zeichenfläche, die Sie zur Gestaltung Ihrer visuellen Reize verwenden können. Um einen zentralen Fixationspunkt zu zeichnen, klicken Sie zuerst auf das Fadenkreuzsymbol und dann auf die Mitte der Anzeige, also auf Position (0, 0).

Wir müssen auch angeben, wie lange der Fixationspunkt sichtbar ist. Ändern Sie dazu die Dauer von "Tastendruck" in 495 ms, um eine Dauer von 500 ms anzugeben. (Siehe Hintergrundkasten 4 für eine Erklärung.)

Das *fixation_dot*-Element sieht jetzt aus wie in %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: |
  The *fixation_dot* item at the end of Step 6.
--%

<div class='info-box' markdown='1'>

**Hintergrundbox 4: Die richtige Dauer auswählen**

Warum eine Dauer von 495 angeben, wenn wir eine Dauer von 500 ms wollen? Der Grund dafür ist, dass die tatsächliche Präsentationsdauer immer auf einen Wert aufgerundet wird, der mit der Bildwiederholrate Ihres Monitors kompatibel ist. Das mag kompliziert klingen, aber für die meisten Zwecke sind die folgenden Faustregeln ausreichend:

1. Wählen Sie eine Dauer, die angesichts der Bildwiederholrate Ihres Monitors möglich ist. Wenn zum Beispiel die Bildwiederholrate Ihres Monitors 60 Hz beträgt, bedeutet dies, dass jedes Bild 16,7 ms dauert (=1000 ms/60 Hz). Daher sollten Sie auf einem Monitor mit 60 Hz immer eine Dauer wählen, die ein Vielfaches von 16,7 ms ist, wie z. B. 16,7, 33,3, 50, 100, usw.
2. Geben Sie im Dauerfeld des SKETCHPAD eine Dauer an, die einige Millisekunden kürzer ist als das, was Sie anstreben. Wenn Sie also ein SKETCHPAD für 50 ms präsentieren möchten, wählen Sie eine Dauer von 45. Wenn Sie ein SKETCHPAD für 1000 ms präsentieren möchten, wählen Sie eine Dauer von 995. Und so weiter.

Für eine detaillierte Diskussion über experimentelles Timing, siehe:

- %link:timing%

</div>

### Schritt 7: Definieren Sie den Tierlaut

Öffnen Sie *animal_sound*. Das SAMPLER-Element bietet eine Reihe von Optionen, wobei die wichtigste das abzuspielende Soundfile ist. Klicken Sie auf die Schaltfläche "Durchsuchen", um den Dateipool-Auswahldialog zu öffnen, und wählen Sie eine der Sounddateien, wie z. B. `bark1.ogg`.

Natürlich wollen wir nicht immer wieder den gleichen Ton abspielen! Stattdessen möchten wir einen Sound auswählen, der auf den Variablen `sound` und `sound_nr` basiert, die wir in der *block_loop* (Schritt 5) definiert haben. Um dies zu tun, ersetzen Sie einfach den Teil der Zeichenkette, der von einer Variablen abhängig sein soll, durch den Namen dieser Variablen in eckigen Klammern. Genauer gesagt, 'bark1.ogg' wird zu '[sound][sound_nr].ogg', weil wir 'bark' durch den Wert der Variablen `sound` und '1' durch den Wert von `sound_nr` ersetzen möchten.

Wir müssen auch die Dauer des SAMPLER ändern. Standardmäßig ist die Dauer 'sound', was bedeutet, dass das Experiment pausiert, während der Ton abgespielt wird. Ändern Sie die Dauer in 0. Das bedeutet nicht, dass der Ton nur 0 ms lang abgespielt wird, sondern dass das Experiment sofort zum nächsten Element übergeht, während der Ton im Hintergrund weiter abgespielt wird. Das Element *animal_sound* sieht nun aus wie in %FigStep8.

%--
Abbildung:
 id: FigStep8
 source: step8.png
 caption: |
  Das Element *animal_sound* am Ende von Schritt 7.
--%

<div class='info-box' markdown='1'>

**Hintergrundkasten 5: Variablen**

Weitere Informationen zum Umgang mit Variablen finden Sie unter:

- %link:manual/variables%

</div>

### Schritt 8: Definieren Sie das Tierbild

Öffnen Sie *animal_picture*. Wählen Sie das Bildwerkzeug aus, indem Sie auf die Schaltfläche mit dem landschaftsähnlichen Symbol klicken. Klicken Sie auf die Mitte (0,0) der Anzeige. Wählen Sie im aufklappenden Datei-Pool-Dialog `capybara1.png`. Der seitliche Blick des Capybaras wird Ihnen nun träge aus der Mitte der Anzeige entgegenstarren. Aber natürlich wollen wir nicht immer das gleiche Capybara zeigen. Stattdessen möchten wir das Bild von den Variablen `animal` und `pic_nr` abhängig machen, die wir in der *block_loop* (Schritt 4) definiert haben.

Wir können im Wesentlichen denselben Trick wie bei *animal_sound* anwenden, obwohl die Dinge bei Bildern etwas anders funktionieren. Klicken Sie zunächst mit der rechten Maustaste auf das Capybara und wählen Sie "Skript bearbeiten". Dadurch können Sie die folgende Zeile des OpenSesame-Skripts bearbeiten, die dem Capybara-Bild entspricht:

```python
draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0
```

Ändern Sie nun den Namen der Bilddatei von 'capybara.png' in '[animal][pic_nr].png':

```python
draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0
```

Klicken Sie auf "Ok", um die Änderung zu übernehmen. Das Capybara ist nun verschwunden und durch ein Platzhalterbild ersetzt, und OpenSesame sagt Ihnen, dass ein Objekt nicht angezeigt wird, weil es als Variable definiert ist. Keine Sorge, es wird während des Experiments angezeigt!

Wir fügen auch zwei Antwortkreise hinzu:

- Ein Kreis mit dem Namen 'Hund' auf der linken Seite des Bildschirms. (Um den Teilnehmer an die Antwortregel zu erinnern, können Sie dem Kreis ein Textelement mit dem Text 'Hund' hinzufügen. Dies ist rein visuell.)
- Ein Kreis mit dem Namen 'Katze' auf der rechten Seite des Bildschirms. (Um den Teilnehmer an die Antwortregel zu erinnern, können Sie dem Kreis ein Textelement mit dem Text 'Katze' hinzufügen.)

Wir werden diese Kreise als *Interessengebiete* für unsere Mausantworten verwenden. Genauer gesagt, weil wir den Kreisen Namen gegeben haben, wird unser *mouse_response* Element in der Lage sein, zu überprüfen, ob der Mausklick innerhalb eines dieser Kreise liegt. Wir werden darauf in Schritt 9 zurückkommen.

Stellen Sie schließlich das Feld 'Dauer' auf '0' ein. Dies bedeutet nicht, dass das Bild nur 0 ms präsentiert wird, sondern dass das Experiment sofort zum nächsten Element (*response*) weitergeht. Da *response* auf eine Antwort wartet, aber das Bildschirminhalt nicht ändert, bleibt das Ziel sichtbar, bis eine Antwort gegeben wurde.

%--
Abbildung:
 ID: FigStep9
 Quelle: step9.png
 Beschriftung: |
  Das *animal_picture* SKETCHPAD am Ende von Schritt 8.
--%

<div class='info-box' markdown='1'>

**Hintergrund-Box 6: Bildformate**

__Tipp__ -- OpenSesame kann eine Vielzahl von Bildformaten verarbeiten. Einige (nicht standard) `.bmp` Formate sind jedoch bekanntlich problematisch. Wenn Sie feststellen, dass ein `.bmp` Bild nicht angezeigt wird, sollten Sie vielleicht ein anderes Format wie `.png` verwenden. Mit kostenlosen Tools wie [GIMP] können Sie Bilder problemlos konvertieren.

</div>


### Schritt 9: Die Antwort definieren

Öffnen Sie das *mouse_response* Element. Dies ist ein MOUSE_RESPONSE Element, das einen einzelnen Mausklick (oder das Loslassen) erfasst. Es gibt einige Optionen:

- __Korrekte Antwort__ — Hier können Sie angeben, welche Maustaste die korrekte Antwort ist. Da wir jedoch basierend darauf, wo der Teilnehmer klickt, und nicht basierend darauf, welche Taste geklickt wird, feststellen möchten, ob eine Antwort korrekt ist, können wir dieses Feld leer lassen.
- __Erlaubte Antworten__ ist eine Semikolon-getrennte Liste der Maustasten, die akzeptiert werden. Lassen Sie uns dies auf 'left_button' einstellen.
- __Timeout__ gibt eine Dauer an, nach der die Antwort auf 'None' gesetzt wird und das Experiment weitergeht. Ein Timeout ist in unserem Experiment wichtig, da die Teilnehmer die Möglichkeit haben müssen, *nicht* zu antworten, wenn sie ein Kapibara sehen. Stellen Sie also das Timeout auf 2000 ein.
- __Verknüpftes Sketchpad__ gibt ein SKETCHPAD an, dessen Elemente als Interessengebiete verwendet werden sollen. Wir wählen *animal_picture*. Wenn wir nun auf das Element mit dem Namen 'Katze' klicken, wird die Variable `cursor_roi` automatisch auf 'Katze' gesetzt.
- __Sichtbarer Mauszeiger__ - Gibt an, dass der Mauszeiger während der Erfassung der Antwort angezeigt werden soll. Wir müssen dies aktivieren, damit die Teilnehmer sehen können, wo sie klicken.
- __Anstehende Mausklicks löschen__ zeigt an, dass wir nur neue Mausklicks akzeptieren sollen. Es ist am besten, diese Option aktiviert zu lassen (standardmäßig ist sie aktiviert).

%--
Abbildung:
 ID: FigStep10
 Quelle: step10.png
 Beschriftung: |
  Das *mouse_response* MOUSE_RESPONSE am Ende von Schritt 9.
--%


### Schritt 10: Den Logger definieren

Wir müssen den LOGGER nicht konfigurieren, da seine Standardeinstellungen in Ordnung sind. Schauen wir uns trotzdem an. Klicken Sie auf *logger* im Übersichtsbereich, um es zu öffnen. Sie sehen, dass die Option 'Variablen loggen (empfohlen)' ausgewählt ist. Das bedeutet, dass OpenSesame alles protokolliert, was in Ordnung ist.

<div class='info-box' markdown='1'>

**Hintergrund-Box 8: Überprüfen Sie immer Ihre Daten!**

__Der wichtigste Tipp__ — Überprüfen Sie immer dreifach, ob alle erforderlichen Variablen in Ihrem Experiment protokolliert wurden! Die beste Methode, dies zu überprüfen, besteht darin, das Experiment auszuführen und die resultierenden Protokolldateien zu untersuchen.

</div>

### Schritt 11: Fertig! (Irgendwie …)

Jetzt sollten Sie Ihr Experiment ausführen können. Es ist noch viel Raum für Verbesserungen und Sie werden im Rahmen der Zusatzaufgaben weiter unten an der Verbesserung des Experiments arbeiten. Aber die grundlegende Struktur ist da!

Klicken Sie auf die Schaltfläche "Vollbild ausführen" (`Strg+R`) in der Hauptwerkzeugleiste, um einen Testlauf durchzuführen.

<div class='info-box' markdown='1'>

**Hintergrund-Box 11: Schneller Testlauf**

__Tipp__ — Ein Testlauf wird noch schneller ausgeführt, indem Sie auf die orangefarbene Schaltfläche "Im Fenster ausführen" klicken, die Ihnen nicht die Frage stellt, wie Sie die Logdatei speichern sollen (und sollte daher nur für Testzwecke verwendet werden).

</div>


## Zusatzaufgaben

Die folgenden zusätzlichen Aufgaben sollen Sie selbst lösen. Die Lösungen finden Sie in der [Versuchsdatei](https://osf.io/2gr3a/). Aber der beste Weg zu lernen ist, sie selbst zu lösen!


### Einfach: Füge eine Anweisungs- und Abschiedsbildschirm hinzu

- SKETCHPAD- und FORM_TEXT_DISPLAY- Elemente können Text anzeigen
- Gute Anweisungen sind kurz und konkret


### Einfach: Daten überprüfen

- Führen Sie das Experiment einmal für sich selbst durch. Sie können die Anzahl der Versuche reduzieren, indem Sie den Wiederholungswert der *block_loop* auf weniger als eins setzen.
- Öffnen Sie die Datendatei in Excel, LibreOffice oder JASP


### Mittel: Feedback für jeden Versuch geben

- Um dies zu tun, müssen Sie bereits eine korrekte Antwort definiert haben! (Siehe unten.)
- Eine gute, unaufdringliche Möglichkeit, Feedback zu geben, besteht darin, nach einer falschen Antwort kurz einen roten Punkt und nach einer richtigen Antwort einen grünen Punkt anzuzeigen.
- Verwenden Sie Run If-Anweisungen!


### Mittel: Gegenseitige Regelung der Antwort

- Die Variable `subject_parity` ist 'gerade' oder 'ungerade'
- Verwenden Sie zwei verschiedene Tierbild-SKETCHPAD- und MOUSE_RESPONSE-Elemente für gerade und ungerade Teilnehmer


### Mittel: Wiederhole nicht das gleiche Tierbild

- Zufallsbeschränkungen können als fortgeschrittene Schleifenoperationen angegeben werden


### Schwierig: Ermitteln, ob die Antwort korrekt war

- Dies erfordert ein INLINE_SCRIPT
- Setzen Sie die Variable `correct` auf 0 für eine falsche Antwort und auf 1 für eine korrekte Antwort
- Bei einem Timeout ist die Variable `response` der String 'None'
- Andernfalls enthält die Variable `cursor_roi` eine durch Semikolon getrennte Liste aller Elementnamen (aus dem verknüpften SKETCHPAD), auf die geklickt wurde. Es ist möglich, auf mehr als ein Element zu klicken, zum Beispiel wenn das Tierbild und der Antwortkreis überlappen


### Schwierig: Aufteilung der Versuche in mehrere Blöcke

- Fügen Sie am Ende der Versuchssequenz ein SKETCHPAD hinzu, das die Teilnehmer zu einer kurzen Pause einlädt
- Verwenden Sie eine Run If-Anweisung, um dieses SKETCHPAD nur nach jeweils 15 Versuchen auszuführen
- Sie benötigen den Modulo-(`%`) Operator und die Variable `count_trial_sequence`, um dies zu tun


### Schwierig: Anpassung des Experiments für die Online-Ausführung

- Dies erfordert ein INLINE_JAVASCRIPT
- Derzeit unterstützt OSWeb keine Verknüpfung von MOUSE_RESPONSE mit einem SKETCHPAD. Das bedeutet, dass Sie die Variable `cursor_x` verwenden müssen, um herauszufinden, wo der Teilnehmer geklickt hat und ob die Antwort korrekt war.
- OSWeb unterstützt keine INLINE_SCRIPT-Elemente


## Referenzen

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}