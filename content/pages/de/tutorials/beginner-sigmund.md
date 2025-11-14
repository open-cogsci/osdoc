title: SigmundAI Anleitung: Blickhinweis
hash: 80f0a9ae4381f62b46aa6b1cca4b807990e8235070ac5187f47bc98a6f028d00
locale: de
language: German

[TOC]


## Über dieses Tutorial

In diesem Tutorial erstellst du ein psychologisches Experiment in Zusammenarbeit mit SigmundAI, deinem AI-Copiloten für OpenSesame. Du lernst, wie du Sigmund klare Anweisungen gibst, Fehler erkennst und behebst und Experimente schneller als je zuvor erstellst.

Wir erstellen ein klassisches Gaze-Cuing-Experiment. Dies ist ein unterhaltsames und interessantes Paradigma, bei dem Menschen unwillkürlich dem Blick einer abgebildeten Person folgen.

Dieses Tutorial baut auf [dem Einsteiger-Tutorial](%url:beginner%) auf und verwendet dasselbe Experiment, zeigt dir jedoch, wie du es mit AI-Unterstützung erstellst.


## Was du lernen wirst

Nach Abschluss dieses Tutorials wirst du wissen, wie man:

- 💡 Sigmund klar und effektiv Anweisungen gibt
- 💡 Komplexe Aufgaben in einfache Schritte unterteilt
- 💡 Sigmunds Fehler erkennt und korrigiert (ja, AI macht Fehler!)
- 💡 Experimente schnell strukturiert
- 💡 Effizient mit einem AI-Copiloten zusammenarbeitet


## Was du benötigst

**OpenSesame 4.1 oder neuer** mit allen installierten Updates. Falls du eine Benachrichtigung über verfügbare Updates siehst, klicke auf „Updates installieren...“ und dann auf „Update-Skript ausführen“. Starte OpenSesame nach dem Update neu. Du kannst auch manuell aktualisieren, indem du folgenden Befehl in der OpenSesame-Konsole ausführst.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

**Grundkenntnisse in OpenSesame.** Noch neu bei OpenSesame? Starte zuerst mit dem [Einsteiger-Tutorial](%url:beginner%). Das Verständnis der Grundlagen hilft dir, effektiv mit Sigmund zusammenzuarbeiten. AI ist mächtig, ersetzt aber nicht das Verständnis der Funktionsweise.

**Ein SigmundAI-Abo.** Du benötigst ein aktives Abo auf [sigmundai.eu](https://sigmundai.eu/).


## OpenSesame mit Sigmund verbinden

Sigmund ist ein speziell für OpenSesame entwickelter AI-Assistent. Im Gegensatz zu allgemeinen Chatbots wie ChatGPT:

- kennt Sigmund OpenSesame in- und auswendig,
- arbeitet direkt in der OpenSesame-Oberfläche,
- kann Änderungen an deinem Experiment automatisch vornehmen.

Um die Verbindung herzustellen, einfach bei [sigmundai.eu](https://sigmundai.eu/) anmelden. Das Sigmund-Panel in OpenSesame stellt dann automatisch die Verbindung her:

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>


## Das Experiment

Wie bereits erwähnt, erstellen wir ein Gaze-Cuing-Experiment, das ursprünglich von [Friesen und Kingstone (1998)][references] entwickelt wurde. So funktioniert es:

1. Ein Gesicht erscheint in der Bildschirmmitte.
2. Das Gesicht blickt nach links oder rechts.
3. Ein Ziellbuchstabe („F“ oder „H“) erscheint auf einer Seite.
4. Ein Ablenkungsbuchstabe („X“) erscheint auf der anderen Seite.
5. Die Teilnehmenden identifizieren den Zielbuchstaben so schnell wie möglich.

Die interessante Erkenntnis? Menschen sind schneller, wenn das Gesicht zum Ziel blickt, obwohl die Blickrichtung nicht vorhersagt, wo das Ziel erscheint. Das zeigt, dass Menschen automatisch dem Blick anderer folgen.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  Das Gaze-Cuing-Paradigma [(Friesen und Kingstone, 1998)][references]. Dieses Beispiel zeigt einen **inkongruenten** Durchgang, da das Gesicht auf den Ablenker („X“) statt auf das Ziel („F“) blickt.
--%


## Schritt 1: Die Hauptsequenz erstellen

Beginnen wir mit dem Grundaufbau. Das Experiment hat zwei Phasen: Übungsphase und Experimentalphase. Jede Phase benötigt eine Instruktion davor und eine Nachricht danach. Ein klarer Aufbau hilft dir und Sigmund, organisiert zu bleiben.

Sei bei deinen Anweisungen an Sigmund präzise! Sage Sigmund genau, was du möchtest – und auch, was du *noch nicht* möchtest. Das verhindert, dass Sigmund zu viel auf einmal machen will.

💬 **Eingabeaufforderung:**

```text
Hi Sigmund! Ich möchte zusammen ein Gaze-Cuing-Experiment erstellen. Lass uns mit dem Grundaufbau beginnen:

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

- Bilder eines Gesichts, das neutral, nach links und nach rechts blickt
- Einen Ton, der abgespielt wird, wenn Teilnehmende einen Fehler machen

Sigmund kann keine Dateien für dich herunterladen, deshalb musst du diesen Teil manuell machen. Lade die folgenden Dateien herunter und ziehe sie in deinen Dateipool:

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Der Dateipool sollte wie %FigStep4 aussehen.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## Schritt 5: Die Trial-Sequenz erstellen

Nun ist es an der Zeit, die Struktur eines einzelnen Trials zu erstellen. Folgendes passiert in jedem Trial:

1. Zeige einen Fixationspunkt (bereit machen!)
2. Zeige das neutrale Gesicht (jetzt kommt das Gesicht)
3. Zeige die Blickrichtung (Gesicht blickt nach links oder rechts)
4. Zeige Zielreiz und Distraktor (jetzt antworten!)
5. Erfasse die Tastatureingabe
6. Spiele Fehlerton ab (nur bei falscher Antwort)
7. Protokolliere die Daten

Der Fehlerton sollte nur bei falschen Durchgängen abgespielt werden. Dafür wird ein Run-if-Ausdruck verwendet: eine Bedingung, die bestimmt, wann ein Element ausgeführt wird.

💬 **Prompt:**

```text
Fügen wir die folgenden Elemente zur trial_sequence hinzu:

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) — soll nur nach einer falschen Antwort abgespielt werden
- logger (logger)

Erstelle die Elemente zunächst nur, füge aber noch keinen Inhalt hinzu. Schaffst du das?
```

Diese Aufgabe erfordert viele Schritte, und Sigmund macht hier manchmal Fehler. Überprüfe deshalb seine Arbeit sorgfältig.

Häufige Fehler von Sigmund an dieser Stelle:

- Vergisst, einige der Elemente zu erstellen
- Vergisst, den Run-if-Ausdruck für *incorrect_sound* hinzuzufügen

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%

Falls Sigmund einen Fehler gemacht hat (z. B. logger oder Run-if-Ausdruck vergessen), gib ihm eine freundliche, aber gezielte Erinnerung mit spezifischen Anweisungen:

💬 **Prompt** (anpassen je nachdem, was fehlt):

```text
Mir ist aufgefallen, dass der logger fehlt. Könntest du ihn bitte noch hinzufügen?

Und dann könntest du bitte die trial_sequence auswählen und einen Run-if-Ausdruck für den incorrect_sound sampler hinzufügen? Denk daran: Run-if-Ausdrücke werden in der Sequenz gesetzt, die das Element enthält, nicht im Element selbst.
```

Warum macht Sigmund Fehler? KI ist unvorhersehbar, daher können bei jeder Aufgabe Fehler passieren. Besonders schwierig sind für Sigmund Aufgaben mit vielen Einzelschritten. Die Aufgabe oben erforderte ganze 9 Einzelschritte! Überprüfe bei komplexen Aufgaben immer sorgfältig das Ergebnis.

Deine *trial_sequence* sollte wie %FigStep5 aussehen.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## Schritt 6: Die Anzeige-Elemente gestalten

Nun zum spannenden Teil: Gestalte, was die Teilnehmenden sehen! Wir arbeiten jede Anzeige einzeln ab.

Zuerst richten wir die Farben ein und zeichnen den Fixationspunkt. Unsere Blickstimuli verwenden einen weißen Hintergrund, also benötigen wir ebenfalls einen weißen Hintergrund mit schwarzen Elementen.

💬 **Prompt:**

```text
Könntest du die Einstellungen des Experiments so ändern, dass schwarze Stimuli auf weißem Hintergrund verwendet werden? Dann füge im fixation_dot-Element einen Fixationspunkt hinzu und setze die Dauer auf 745 ms.
```

Als Nächstes die Anzeige für das neutrale Gesicht:

💬 **Prompt:**

```text
Super! Jetzt füge das Bild mit neutralem Blick ein. Die Dauer sollte 745 ms betragen.
```

Sigmund sollte das *gaze_neutral.png*-Bild aus dem Dateipool nutzen. Schau auf das sketchpad, um das zu prüfen!

Jetzt die Anzeige für den Blickhinweis (wohin das Gesicht schaut):

💬 **Prompt:**

```text
Perfekt! Füge jetzt die Anzeige für den Blickhinweis hinzu. Sie soll für 495 ms angezeigt werden.
```

Sigmund soll die Variable `gaze_cue` nutzen, um entweder *gaze_left.png* oder *gaze_right.png* anzuzeigen.

Zum Schluss das Target-Display (das komplexeste):

💬 **Prompt:**

```text
Ausgezeichnet! Erstelle nun die Zielanzeige. Sie sollte Folgendes zeigen:

- Den Blickhinweis (Gesicht schaut immer noch)
- Den Zielbuchstaben links oder rechts (je nach target_pos)
- Ein 'X' auf der gegenüberliegenden Seite
```

Die Dauer sollte 0 betragen, da als Nächstes das *keyboard_response*-Element kommt und auf eine Eingabe wartet. Überprüfe, ob Sigmund dies korrekt gemacht hat!


## Schritt 7: Konfiguriere die Tastatureingabe

Jetzt müssen wir die Antworten der Teilnehmer erfassen.

💬 **Aufforderung:**

```text
Bitte konfiguriere die keyboard_response mit einem Timeout von 2000 ms. Akzeptiere nur die korrekten Antworttasten (z und m).
```


## Schritt 8: Richte das Fehlersignal ein

Wenn Teilnehmer Fehler machen, sollen sie eine Rückmeldung hören.

💬 **Aufforderung:**

```text
Konfiguriere jetzt den incorrect_sound sampler so, dass die Fehlermeldung abgespielt wird.
```


## Schritt 9: Erstelle die Feedback-Anzeige

Nach jedem Block sollen die Teilnehmer sehen, wie sie abschneiden.

💬 **Aufforderung:**

```text
Füge dem feedback-Element Rückmeldung hinzu, die die durchschnittliche Genauigkeit und Reaktionszeit für den Block anzeigt.
```


## Schritt 10: Blockwiederholungen festlegen

Jetzt müssen wir festlegen, wie oft jeder Block wiederholt werden soll.

💬 **Aufforderung:**

```text
Setze die Übungsphase auf 2 Blöcke und die experimentelle Phase auf 8 Blöcke. Erstelle außerdem eine 'practice'-Variable (yes oder no), damit wir Übung und experimentelle Durchgänge in unseren Daten unterscheiden können.
```


## Schritt 11: Schreibe die Instruktionsbildschirme

Die Teilnehmer müssen wissen, was zu tun ist! Lass Sigmund klare Anweisungen schreiben.

💬 **Aufforderung:**

```text
Bitte schreibe klare, prägnante Anweisungen für das Experiment sowie hilfreiche Nachrichten am Ende der Übungsphase und am Ende des Experiments. Entscheide dich selbst für den Inhalt!
```

Lies die Anweisungen sorgfältig durch. Ergibt alles Sinn? Sind sie verständlich? Bitte Sigmund ggf. um Überarbeitung!


## Schritt 12: Teste und debugge!

Jetzt kommt der Moment der Wahrheit. Starte das Experiment mit dem blauen Schnellstart-Button und beobachte, was passiert. Ein Fehler kann auftreten – das ist völlig normal. Hier ist ein möglicher Fehler:

%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "Ein Fehler wird angezeigt. Keine Panik!"
--%

Was läuft schief? Das End-of-Practice-Element versucht, die Variable `acc` anzuzeigen, bevor sie existiert. Das passiert wegen der Prepare-Run-Phasen von OpenSesame: Items werden im Voraus vorbereitet, und manchmal sind Variablen zu diesem Zeitpunkt noch nicht definiert.

Sigmund kann solche Probleme normalerweise beheben. Klicke einfach auf „Ask Sigmund to fix this“, wenn der Fehler auftritt. Sobald der Fehler behoben ist, probiere das Experiment erneut aus. Wiederhole den Vorgang bei Bedarf.

Fertig! Glückwunsch. Du hast mit Sigmund ein vollständiges Experiment gebaut!

💬 **Letzter Schritt:**

```text
Danke, Sigmund! Großartige Arbeit!
```


## Wichtigste Erkenntnisse

Du hast gelernt, wie man effektiv mit einem KI-Copiloten zusammenarbeitet! Hier die wichtigsten Lektionen:

- ✅ **Sei spezifisch und klar** in deinen Aufforderungen.
- ✅ **Teile komplexe Aufgaben in einfache Schritte auf**. Frage nicht zu viel auf einmal.
- ✅ **Überprüfe immer Sigmunds Arbeit**. KI macht Fehler!
- ✅ **Stelle Rückfragen**, wenn etwas nicht stimmt.
- ✅ **Sei geduldig**. Debugging gehört dazu.

Mit etwas Übung werdet ihr und Sigmund ein tolles Team! 🤝


## Literatur

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references