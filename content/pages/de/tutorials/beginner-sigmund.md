title: SigmundAI Anleitung: Blickhinweis
hash: d5304ea6608e83e51e1a0e01bbc9e8efc6602bc92944fcf1444d2848f9e097fe
locale: de
language: German

## Über dieses Tutorial

In diesem Tutorial baust du ein Psychologie-Experiment, indem du gemeinsam mit SigmundAI, deinem KI-Copiloten für OpenSesame, arbeitest. Du lernst, wie du Sigmund klare Anweisungen gibst, Fehler findest und behebst und Experimente schneller als je zuvor erstellst.

Wir erstellen ein klassisches Gaze-Cuing-Experiment. Dies ist ein unterhaltsames und interessantes Paradigma, bei dem Menschen unwillkürlich der Blickrichtung eines Gesichts folgen.

Dieses Tutorial baut auf dem [Einsteiger-Tutorial](%url:beginner%) auf. Wir verwenden dasselbe Experiment, zeigen dir aber, wie du es mit KI-Unterstützung erstellst.


## Was du lernen wirst

Am Ende dieses Tutorials weißt du, wie man:

- ✅ Sigmund klare, effektive Anweisungen gibt
- ✅ Komplexe Aufgaben in einfache Schritte zerlegt
- ✅ Sigmunds Fehler erkennt und korrigiert (ja, auch KI macht Fehler!)
- ✅ Experimentalstrukturen schnell erstellt
- ✅ Effizient mit einem KI-Copiloten arbeitet


## Was du benötigst

**OpenSesame 4.1 oder neuer** mit allen installierten Updates. Wenn eine Benachrichtigung über verfügbare Updates erscheint, klicke auf "Updates installieren ..." und dann auf "Update-Skript ausführen". Starte OpenSesame nach dem Update neu. Du kannst auch manuell über die folgende Eingabe in der OpenSesame-Konsole aktualisieren:

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**Grundkenntnisse in OpenSesame.** Neu in OpenSesame? Starte zuerst mit dem [Einsteiger-Tutorial](%url:beginner%). Wenn du die Grundlagen verstehst, kannst du besser mit Sigmund zusammenarbeiten. KI ist mächtig – aber sie ersetzt nicht das Verständnis, wie Dinge funktionieren.

**Ein SigmundAI-Abonnement.** Du benötigst ein aktives Abonnement auf [sigmundai.eu](https://sigmundai.eu/).


## OpenSesame mit Sigmund verbinden

Sigmund ist ein KI-Assistent, der speziell für OpenSesame entwickelt wurde. Anders als allgemeine Chatbots wie ChatGPT:

- kennt Sigmund OpenSesame in- und auswendig,
- arbeitet direkt in der OpenSesame-Oberfläche,
- kann automatisch Änderungen an deinem Experiment vornehmen.

Um dich zu verbinden, melde dich einfach bei [sigmundai.eu](https://sigmundai.eu) an. Das Sigmund-Panel in OpenSesame stellt automatisch eine Verbindung her:

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>


## Das Experiment

Wie bereits erwähnt, erstellen wir ein Gaze-Cuing-Experiment, das ursprünglich von [Friesen und Kingstone (1998)][references] entwickelt wurde. So funktioniert es:

1. Ein Gesicht erscheint in der Mitte des Bildschirms.
2. Das Gesicht blickt nach links oder rechts.
3. Ein Zielbuchstabe ('F' oder 'H') erscheint auf einer Seite.
4. Ein Ablenkungsbuchstabe ('X') erscheint auf der anderen Seite.
5. Die Teilnehmenden identifizieren den Zielbuchstaben so schnell wie möglich.

Das Interessante: Menschen sind schneller, wenn das Gesicht zum Ziel blickt – obwohl die Blickrichtung nicht vorhersagt, wo das Ziel erscheinen wird. Das zeigt, dass Menschen automatisch der Blickrichtung anderer folgen.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Das Gaze-Cuing-Paradigma [(Friesen und Kingstone, 1998)][references]. Das Beispiel zeigt einen **inkongruenten** Durchgang, weil das Gesicht auf den Ablenker ('X') statt auf das Ziel ('F') blickt.
--%


## Schritt 1: Erstelle die Hauptsequenz

Beginnen wir mit dem grundlegenden Aufbau. Das Experiment besteht aus zwei Phasen: Übung und Experimentalphase. Jede Phase braucht eine Instruktion davor und eine Nachricht danach. Ein klarer Aufbau hilft sowohl dir als auch Sigmund, den Überblick zu behalten.

Wenn du mit Sigmund sprichst, sei spezifisch! Sag Sigmund genau, was du möchtest, und auch, was du *noch nicht* möchtest. Das verhindert, dass Sigmund zu viel auf einmal macht.

💬 **Prompt:**

```text
Hi Sigmund! Ich möchte gemeinsam ein Gaze-Cuing-Experiment bauen. Lass uns mit der Basisstruktur starten:

- experiment (sequence)
  - instructions (form_text_display)
  - practice_loop (loop)
    - block_sequence (sequence)
  - end_of_practice (form_text_display)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_of_experiment (form_text_display)
```

Bitte erstelle diese Struktur, aber füge noch keinen Inhalt zu den Items hinzu. Wir machen das Schritt für Schritt!
```

Nachdem Sigmund diese Struktur erstellt hat, lass uns etwas aufräumen. Frag danach in einer separaten Eingabe, um Sigmund nicht mit zu vielen Aufgaben auf einmal zu überfordern.

💬 **Prompt:**

```text
Super! Bitte entferne jetzt alle Items, die wir nicht benötigen, und vergib einen klaren Titel für das Experiment.
```

Dein Übersichtsbereich sollte wie %FigStep1 aussehen. (Der Titel deines Experiments kann leicht abweichen. Das ist in Ordnung!)

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  Der Übersichtsbereich am Ende von Schritt 1.
--%


<div class='info-box' markdown='1'>

**💡 Behalte Sigmund im Auge!**

Unten im Sigmund-Panel kannst du wählen, ob du Sigmunds Aktionen vor deren Ausführung überprüfen möchtest. Ist diese Option aktiviert, musst du jede Änderung von Sigmund freigeben.

- **Zum Lernen:** Lass diese Einstellung AN. So verstehst du, was Sigmund macht.
- **Für Schnelligkeit:** Schalte sie aus, sobald du dich sicher fühlst.

Denk daran, dass Sigmund Fehler macht! Kontrolliere die Ergebnisse immer doppelt, besonders am Anfang.

</div>


## Schritt 2: Erstelle die block_sequence

Jetzt bauen wir auf, was in jedem Block von Durchgängen passiert. Jeder Block folgt diesem Muster:

1. Rückmeldung zurücksetzen (damit die Leistung der vorherigen Blöcke keinen Einfluss auf das Feedback im aktuellen Block hat)
2. Eine Schleife mit Durchgängen ausführen
3. Leistungsrückmeldung anzeigen

Die Übungs- und Experimentalphase verwenden das gleiche *block_sequence*-Item. Das nennt man eine verlinkte Kopie. Änderst du eine, ändert sich auch die andere. Verlinkte Kopien sind praktisch, wenn die gleiche Funktionalität (z.B. ein Durchgangsblock) mehrfach im Experiment vorkommt.

💬 **Prompt:**

```text
Perfekt! Lass uns nun Inhalt zur block_sequence hinzufügen. Sie sollte zwischen Übungs- und Experimentalphase geteilt werden (verlinkte Kopie). Strukturiere sie so:

- block_sequence (sequence)
  - reset_feedback (reset_feedback)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)

Erstelle wieder nur die Struktur. Den Inhalt fügen wir später hinzu. Bereit? Los geht's!
```

Deine Übersicht sollte jetzt wie %FigStep2 aussehen.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  Der Übersichtsbereich am Ende von Schritt 2.
--%


## Schritt 3: Definiere die Versuchsbedingungen

Jedes Experiment hat unabhängige Variablen – das sind die Dinge, die du manipulierst. In unserem Experiment variieren wir:

- Blickrichtung des Gesichts (links oder rechts)
- Wo das Ziel erscheint (links bei -300, oder rechts bei 300)
- Welcher Buchstabe das Ziel ist (F oder H)

Wir müssen außerdem berechnen:

- Wo der Distraktor platziert wird (entgegengesetzte Seite des Ziels)
- Welche Antworttaste korrekt ist (z für F, m für H)

Das ergibt ein 2 × 2 × 2 Design = 8 verschiedene Trial-Typen.

Indem wir Sigmund das Design erklären, helfen wir Sigmund, die Logik zu verstehen und alle richtigen Kombinationen zu erzeugen.

💬 **Prompt:**

```text
Jetzt lass uns die Variablen im block_loop definieren. Es handelt sich um ein 2 × 2 × 2 Design (insgesamt 8 Zeilen):

- gaze_cue: left oder right
- target_pos: -300 oder 300 (x-Koordinate, negativ = links, 0 = Mitte)
- target_letter: F oder H
- dist_pos: gegenüber von target_pos
- correct_response: z bei target_letter = F, m bei target_letter = H

Kannst du das erstellen? Danke!
```

Dein *block_loop* sollte jetzt wie %FigStep3 aussehen, mit 8 Zeilen, die alle möglichen Kombinationen zeigen.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "Der *block_loop* am Ende von Schritt 3."
--%


<div class='info-box' markdown='1'>

**🤖 Wähle ein KI-Modell, das zu dir passt!**

Sigmund ist keine einzelne KI, sondern ein Chatbot, der verschiedene KI-Modelle verwenden kann. Auf [sigmundai.eu](https://sigmundai.eu) kannst du zwischen verschiedenen Modellen wählen.

Dieses Tutorial wurde mit **Claude Sonnet 4.5** und **GPT-5** im Gesprächsmodus getestet.

Tipps:

- Verschiedene Modelle haben unterschiedliche Stärken. Probiere sie aus, um deinen Favoriten zu finden.
- Problemlösemodelle sind langsam und nicht immer besser für einfache Aufgaben.

</div>


## Schritt 4: Füge Bilder und Töne dem Dateipool hinzu

Wir benötigen einige Dateien für unsere Stimuli:

- Bilder eines Gesichts mit neutralem Blick, nach links und nach rechts schauend
- Einen Ton, der abgespielt wird, wenn Teilnehmende einen Fehler machen

Sigmund kann keine Dateien für dich herunterladen, daher musst du diesen Teil manuell erledigen. Lade die folgenden Dateien herunter und ziehe sie in deinen file pool:

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Der file pool sollte wie %FigStep4 aussehen.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## Schritt 5: Baue die Versuch-Sequenz

Jetzt ist es Zeit, die Struktur eines einzelnen Versuchs zu erstellen. Folgendes passiert bei jedem Durchgang:

1. Zeige einen Fixationspunkt (Bereit machen!)
2. Zeige das neutrale Gesicht (hier kommt das Gesicht)
3. Zeige den Blick-Hinweis (Gesicht schaut nach links oder rechts)
4. Zeige Zielreiz und Distraktor (Zeit zu reagieren!)
5. Erhebe die Tastaturreaktion
6. Spiele Fehlerton ab (nur bei falscher Antwort)
7. Protokolliere die Daten

Der Fehlerton soll nur bei falschen Durchgängen abgespielt werden. Dafür wird ein run-if-Ausdruck verwendet: eine Bedingung, die bestimmt, wann ein Element ausgeführt wird.

💬 **Prompt:**

```text
Fügen wir Items zur trial_sequence hinzu:

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — nur abspielen nach einer falschen Antwort
- logger (logger)

Erstelle zunächst nur die Items, füge noch keinen Inhalt hinzu. Geht das?
```

Diese Aufgabe erfordert viele Schritte und Sigmund vertut sich manchmal dabei. Überprüfe seine Arbeit daher sorgfältig.

**Häufige Fehler, die Sigmund hier macht:**

- Vergisst, einige der Items zu erstellen
- Vergisst, für *incorrect_sound* den run-if-Ausdruck hinzuzufügen

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%

Falls Sigmund einen Fehler gemacht hat (z.B. logger oder run-if-Ausdruck für incorrect_sound vergessen), gib ihm eine freundliche Erinnerung mit konkreten Anweisungen:

💬 **Prompt** (je nach fehlendem Teil anpassen):

```text
Mir ist aufgefallen, dass der logger fehlt. Könntest du ihn bitte noch hinzufügen? 

Und könntest du dann die trial_sequence auswählen und einen run-if-Ausdruck für den incorrect_sound sampler ergänzen? Denk daran: run-if-Ausdrücke werden in der Sequenz gesetzt, die das Item enthält, nicht im Item selbst.
```

Warum macht Sigmund Fehler? Künstliche Intelligenz ist unvorhersehbar, weshalb Fehler bei jeder Aufgabe passieren können. Besonders schwer tun sich AIs aber mit Aufgaben, die viele einzelne Schritte beinhalten. Die Aufgabe oben forderte 9 separate Aktionen! Kontrolliere bei komplexen Aufgaben deshalb immer die Ergebnisse noch einmal genau.

Deine *trial_sequence* sollte wie %FigStep5 aussehen.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## Schritt 6: Zeichne die Anzeige-Elemente

Jetzt kommt der spaßige Teil: Wir gestalten die Anzeigen für die Teilnehmenden! Wir gehen jede Anzeige Schritt für Schritt durch.

Zuerst stellen wir die Farben ein und zeichnen den Fixationspunkt. Unsere Blickstimuli haben einen weißen Hintergrund, daher brauchen wir einen weißen Hintergrund mit schwarzen Elementen.

💬 **Prompt:**

```text
Könntest du die Experiment-Einstellungen ändern, sodass schwarze Stimuli auf weißem Hintergrund verwendet werden? Füge dann einen Fixationspunkt zum fixation_dot-Item hinzu und setze die Dauer auf 745 ms.
```

Jetzt das neutrale Gesichtsbild:

💬 **Prompt:**

```text
Super! Füge nun das neutrale Blickbild hinzu. Die Dauer beträgt 745 ms.
```

Sigmund sollte erkannt haben, dass er die Datei *gaze_neutral.png* aus dem file pool nutzen soll. Überprüfe das sketchpad daraufhin!

Jetzt der Blick-Hinweis (wohin das Gesicht schaut):

💬 **Prompt:**

```text
Perfekt! Jetzt füge die gaze cue-Anzeige hinzu. Sie sollte für 495 ms gezeigt werden.
```

Sigmund sollte die Variable `gaze_cue` verwenden, um entweder *gaze_left.png* oder *gaze_right.png* anzuzeigen.

Zum Schluss die Zielanzeige (das komplexeste Element):

💬 **Prompt:**

```text
Ausgezeichnet! Jetzt erstelle die Zielanzeige. Sie sollte Folgendes zeigen:

- Den Blickhinweis (Gesicht schaut weiterhin)
- Den Zielbuchstaben links oder rechts (je nach target_pos)
- Ein 'X' auf der gegenüberliegenden Seite
```

Die Dauer sollte 0 sein, da das *keyboard_response*-Element als nächstes kommt und auf die Eingabe wartet. Überprüfe, ob Sigmund dies richtig gemacht hat!


## Schritt 7: Konfiguriere die Tastaturantwort

Nun müssen wir die Antworten der Teilnehmer erfassen.

💬 **Anweisung:**

```text
Bitte konfiguriere das keyboard_response mit einem Timeout von 2000 ms. Akzeptiere nur die korrekten Antworttasten (z und m).
```


## Schritt 8: Richte das Fehlersignal ein

Wenn Teilnehmer Fehler machen, sollen sie Rückmeldung erhalten.

💬 **Anweisung:**

```text
Konfiguriere jetzt den incorrect_sound sampler so, dass die Fehlersound-Datei abgespielt wird.
```


## Schritt 9: Erstelle die Feedback-Anzeige

Nach jedem Block sollen die Teilnehmer sehen, wie sie abschneiden.

💬 **Anweisung:**

```text
Füge dem feedback-Element Rückmeldung hinzu, die die durchschnittliche Genauigkeit und Reaktionszeit für den Block anzeigt.
```


## Schritt 10: Blockwiederholungen einstellen

Jetzt müssen wir festlegen, wie oft jeder Block wiederholt werden soll.

💬 **Anweisung:**

```text
Setze die Übungsphase auf 2 Blöcke und die Experimentalphase auf 8 Blöcke. Erstelle außerdem eine 'practice'-Variable (ja oder nein), damit wir Übungsdurchgänge von Experimental-Durchgängen in unseren Daten unterscheiden können.
```


## Schritt 11: Schreibe die Instruktionsbildschirme

Die Teilnehmer müssen wissen, was zu tun ist! Lass Sigmund klare Anweisungen schreiben.

💬 **Anweisung:**

```text
Bitte schreibe klare, prägnante Anweisungen für das Experiment sowie hilfreiche Nachrichten am Ende der Übung und am Ende des Experiments. Überlege dir den Inhalt selbst!
```

Lies die Anweisungen durch. Ergibt alles Sinn? Sind sie verständlich? Bitte Sigmund ggf. um Überarbeitung!


## Schritt 12: Testen und Debuggen!

Der Moment der Wahrheit ist gekommen. Lass das Experiment laufen! Drücke auf den blauen Quick-Run-Button und beobachte, was passiert. Es kann sein, dass ein Fehler auftritt! Das ist völlig normal. Hier ein möglicher Fehler:

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "Ein Fehler erscheint. Keine Panik!"
--%

Was läuft schief? Das End-of-practice-Element versucht, die Variable `acc` anzuzeigen, bevor sie existiert. Dies passiert aufgrund der Prepare-Run-Phasen in OpenSesame: Elemente werden im Voraus vorbereitet, und manchmal sind Variablen zu diesem Zeitpunkt noch nicht definiert.

Sigmund kann solche Probleme meist beheben. Klicke einfach auf „Ask Sigmund to fix this“, wenn der Fehler erscheint. Sobald der Fehler behoben ist, führe das Experiment erneut aus. Wiederhole den Vorgang falls nötig.

Geschafft! Herzlichen Glückwunsch. Du hast mit Sigmund ein komplettes Experiment gebaut!

💬 **Finale Anweisung:**

```text
Danke Sigmund! Gute Arbeit!
```


## Wichtige Erkenntnisse

Du hast gelernt, wie man effektiv mit einem KI-Copiloten arbeitet! Hier die wichtigsten Lektionen:

1. **Sei spezifisch und klar** in deinen Anweisungen.
2. **Teile komplexe Aufgaben in einfache Schritte auf**. Bitte nicht zu viel auf einmal.
3. **Überprüfe immer Sigmunds Arbeit**. Auch KI macht Fehler!
4. **Stelle Rückfragen**, wenn etwas nicht passt.
5. **Hab Geduld**. Debugging gehört dazu.

Mit ein wenig Übung werdet ihr ein tolles Team! 🤝


## Literaturverzeichnis

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references