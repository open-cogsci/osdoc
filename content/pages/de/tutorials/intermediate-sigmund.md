title: SigmundAI-Tutorial: Visual Search Task
hash: 2662b1ce900715b74ee381b68acb991140b33a5656bfb23c5b7bee6cd4c44cec
locale: de
language: German

[TOC]

## Über dieses Tutorial

Dieses Tutorial zeigt, wie Sie in OpenSesame mithilfe von SigmundAI, dem direkt in die OpenSesame-Oberfläche integrierten KI-Copiloten, ein klassisches Visual-Search-Experiment erstellen. Anstatt das Experiment vollständig von Hand aufzubauen, lernen Sie, wie Sie mit Sigmund zusammenarbeiten, um die vollständige Experimentstruktur zu konstruieren, faktorielle Designs zu definieren und eine dynamische Stimulusgenerierung durch skriptgesteuerte Logik umzusetzen.


## Was Sie lernen werden

Am Ende dieses Tutorials werden Sie wissen, wie man:

- 💡 Sigmund klare, effektive Anweisungen gibt
- 💡 komplexe Aufgaben in einfache Schritte unterteilt
- 💡 Sigmunds Fehler erkennt und korrigiert (ja, KI macht Fehler!)
- 💡 Experimentstrukturen schnell aufbaut
- 💡 mit Sigmund Skripte schreibt
- 💡 effizient mit einem KI-Copiloten arbeitet

## OpenSesame mit Sigmund verbinden

Sigmund ist ein KI-Assistent, der speziell für OpenSesame entwickelt wurde. Anders als allgemeine Chatbots wie ChatGPT:

- kennt Sigmund OpenSesame in- und auswendig
- arbeitet direkt innerhalb der OpenSesame-Oberfläche
- kann automatisch Änderungen an Ihrem Experiment vornehmen

Zum Verbinden melden Sie sich einfach bei [sigmundai.eu](https://sigmundai.eu) an. Das Sigmund-Panel in OpenSesame wird sich automatisch verbinden:

<video controls width ="100%"> 
    <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>
<p align="center"><em>Video 1. OpenSesame mit Sigmund verbinden.</em></p>


## Das Experiment

In diesem Tutorial erstellen Sie ein einfaches Visual-Search-Experiment. Das Experiment ähnelt den klassischen Visual-Search-Studien von [Treisman and Gelade (1980)][references], ist aber nicht identisch.

In diesem Experiment suchen die Teilnehmenden nach einem Zielobjekt, das ein gelbes Quadrat, ein gelber Kreis, ein blaues Quadrat oder ein blauer Kreis sein kann; die Identität des Zielobjekts variiert zwischen den Blöcken von Durchgängen. Die Teilnehmenden geben durch Drücken der rechten (vorhanden) oder linken (nicht vorhanden) Pfeiltaste an, ob das Zielobjekt vorhanden ist oder nicht.

Zusätzlich zum Zielobjekt werden null oder mehr Distraktorobjekte gezeigt. Es gibt drei Bedingungen, und die Bedingung bestimmt, welche Art von Distraktoren es gibt:

- In der Bedingung *Conjunction* können Distraktoren jede Form und Farbe haben, mit der einzigen Einschränkung, dass Distraktoren nicht mit dem Zielobjekt identisch sein dürfen. Wenn das Zielobjekt also zum Beispiel ein gelbes Quadrat ist, dann sind die Distraktoren gelbe Kreise, blaue Kreise und blaue Quadrate.

- In der Bedingung *Shape Feature* haben Distraktoren eine andere Form als das Zielobjekt, können aber jede Farbe haben. Wenn das Zielobjekt also zum Beispiel ein gelbes Quadrat ist, dann sind die Distraktoren gelbe Kreise und blaue Kreise.

- In der Bedingung *Color Feature* können Distraktoren jede Form haben, haben aber eine andere Farbe als das Zielobjekt. Wenn das Zielobjekt also zum Beispiel ein gelbes Quadrat ist, dann sind die Distraktoren blaue Quadrate und blaue Kreise.

Unmittelbares Feedback wird nach jedem Durchgang gezeigt: ein grüner Punkt nach einer korrekten Antwort und ein roter Punkt nach einer inkorrekten Antwort. Detailliertes Feedback zu durchschnittlichen Reaktionszeiten und Genauigkeit wird nach jedem Durchgangsblock gezeigt.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg.png
 caption: The visual-search experiment that you will implement in this tutorial.
--%


Experimente wie dieses zeigen zwei typische Befunde:

- Es dauert länger, das Zielobjekt in der Bedingung Conjunction zu finden als in den beiden Feature-Bedingungen.
- In der Bedingung Conjunction steigen die Reaktionszeiten mit zunehmender Anzahl von Distraktoren. Das legt nahe, dass Menschen nach dem Zielobjekt jeweils ein Element nach dem anderen suchen; dies wird *serial search* genannt.
- In den Feature-Bedingungen (sowohl Form als auch Farbe) steigen die Reaktionszeiten nicht oder kaum mit zunehmender Anzahl von Distraktoren. Das legt nahe, dass Menschen die gesamte Anzeige auf einmal verarbeiten; dies wird *parallel search* genannt.

Gemäß der Merkmalsintegrationstheorie von Treisman und Gelade spiegeln diese Ergebnisse wider, dass die Conjunction-Bedingung erfordert, dass Sie die Farbe und Form jedes Objekts kombinieren oder *binden*. Diese Bindung erfordert Aufmerksamkeit, und Sie müssen daher Ihre Aufmerksamkeit von einem Objekt zum nächsten verlagern; das ist langsam und erklärt, warum die Reaktionszeiten davon abhängen, wie viele Objekte vorhanden sind. Im Gegensatz dazu müssen in den Feature-Bedingungen Farbe und Form nicht gebunden werden, und daher kann die gesamte Anzeige in einem einzigen Durchgang verarbeitet werden, ohne dass die Aufmerksamkeit auf jedes einzelne Objekt gerichtet wird.

## Schritt 1: Die Hauptstruktur erstellen  

Bevor wir mit dem Erstellen eines Experiments beginnen, ist es hilfreich zu verstehen, wie Experimente in OpenSesame organisiert sind. 
In OpenSesame besteht ein Experiment aus items, die steuern, was in welcher Reihenfolge passiert. 
Wir möchten diese Struktur zunächst definieren, damit Sigmund darauf aufbauen kann. 

Das grundlegende Gerüst für unser Experiment umfasst:

1. Die experiment sequence – Diese enthält das gesamte Experiment
2. Einen Platz für allgemeine Anweisungen – Die Teilnehmenden benötigen Anweisungen, bevor das Experiment beginnt.
3. Eine loop, die die verschiedenen experimentellen Blöcke definiert – Eine loop wiederholt einen Teil des Experiments mehrfach. In unserem Fall entspricht jede Wiederholung einem experimentellen Block.
4. Eine sequence, die definiert, was innerhalb jedes Blocks passiert – Diese sequence wird später die trials und die block-spezifische Logik enthalten.
5. Und einen abschließenden Endbildschirm – Damit die Teilnehmenden wissen, wann das Experiment beendet ist.

Eine klare Struktur wie diese hält sowohl uns als auch Sigmund organisiert. Wenn wir versuchen, Sigmund alles auf einmal erstellen zu lassen, macht Sigmund eher Fehler, und es wird für uns schwieriger, Fehler zu erkennen und zu beheben. 

Also erstellen wir zuerst das Gerüst und füllen die Details später aus!


💬 **Prompt:**

```text
Hi Sigmund! Ich möchte ein visuelles Such-Experiment erstellen. Bitte erstelle diese Struktur, ohne vorerst Inhalte hinzuzufügen:

- experiment (sequence)
  - instructions (sketchpad)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_message (sketchpad)
```

Wenn Sigmund fertig ist, sollte die Übersicht wie %FigStep1 aussehen: 

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area after creating the main structure.
--%


Bevor wir fortfahren, sollten wir Sigmund bitten, unserem Experiment einen passenden Namen zu geben und alle unnötigen items zu entfernen: 


💬 **Prompt:**
```text
Please remove unnecessary default items and give the experiment a clear title.
```

%--
figure:
 id: FigStep1b
 source: step1b.png
 caption: |
  The overview area at the end of Step 1.
--%


## Schritt 2: block_sequence erstellen 

Das visuelle Such-Experiment ist hierarchisch. Das bedeutet, dass das Experiment Blöcke enthält und die Blöcke selbst trials enthalten. In jedem Block absolvieren die Teilnehmenden mehrere trials, bei denen sie nach demselben Zielreiz suchen. Es ist wichtig, dass wir diese Ebenen nicht verwechseln, da sich die Zielreize sonst zwischen den trials ändern könnten! 


Der nächste Schritt besteht darin, die Struktur für einen einzelnen Block zu erstellen. Jeder Block sollte Folgendes enthalten: 

1. Anweisungen, die der teilnehmenden Person mitteilen, was der Zielreiz ist
2. Eine loop, die alle trials für diesen Block ausführt 
3. Einen Block-Feedback-Bildschirm

💬 **Prompt:**

```text
Now create the block_sequence contents. It should look like this:

- block_sequence (sequence)
  - block_instructions (sketchpad)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)
  
Just build the structure for now.
```

Ihre Übersicht sollte nun wie %FigStep2 aussehen.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%


## Schritt 3: Variablen zwischen Blöcken definieren

Die targets haben zwei Merkmale, Form und Farbe, die sich zwischen den Blöcken ändern. Daher muss Sigmund diese in der äußeren Schleife (experimental_loop) definieren.  
Wenn wir diese Variablen stattdessen innerhalb der trial-Schleife definieren, ändert sich das target bei jedem trial statt bei jedem Block.

Wir sagen Sigmund jetzt, dass er Variablen in experimental_loop definieren soll, um alle Kombinationen aus Kreis/Quadrat und Blau/Gelb zu erzeugen.


💬 **Prompt:**

```text
Bitte definiere die Variablen in experimental_loop so, dass alle Kombinationen von:

  1. target_shape (circle/square)
  2. target_color (blue/yellow)

über die Blöcke hinweg gleich häufig auftreten.
```

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The table of experimental_loop at the end of step 3."
--%


## Schritt 4: trial-Bedingungen definieren

Innerhalb jedes Blocks variieren drei Faktoren von trial zu trial:

1. Die Bedingung (conjunction / shape / color)
2. Die Anzahl der Stimuli (1 / 5 / 15)
3. Ob das target vorhanden ist oder nicht.

Wir möchten, dass Sigmund trial-Bedingungen für alle Kombinationen erstellt, also ein vollständiges faktorielles Design.
3 Bedingungen x 3 set sizes x 2 presence-Stufen = 18 trial-Typen

💬 **Prompt:**

```text
Definiere jetzt die Variablen von block_loop. Dies soll ein vollständiges faktorielles Design sein mit:

- condition: conjunction, feature_shape, feature_color
- set_size: 1, 5, 15
- target_present: present, absent

Bitte erstelle alle Kombinationen.
```

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The table of block_loop at the end of step 4."
--%


## Schritt 5: trial_sequence erstellen

Jetzt müssen wir definieren, was in einem einzelnen trial passiert. Lassen Sie uns zuerst die items erstellen; den Inhalt fügen wir in den nächsten Schritten hinzu.
Während eines einzelnen trials:

1. Zeigen wir einen Fixationspunkt 
2. Zeigen wir das Haupt-Suchdisplay (dafür ist ein Python inline_script erforderlich)
3. Erfassen wir die Reaktion der Versuchsperson 
4. Protokollieren wir die Daten, die wir benötigen 
5. Geben wir der Versuchsperson Feedback


💬 **Prompt:**

```text
Bitte füge in dieser Reihenfolge items zu trial_sequence hinzu:

- fixation (sketchpad)
- search_display_script (inline_script)
- keyboard_response (keyboard_response)
- logger (logger)
- green_feedback (sketchpad)
- red_feedback (sketchpad)

Erstelle vorerst nur die items und füge noch keinen Inhalt hinzu.
```

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The trial_sequence at the end of Step 5."
--%


## Schritt 6: Fixationsdisplay

Beginnen wir damit, Inhalt hinzuzufügen! Lassen Sie Sigmund einen zentralen Fixationspunkt auf das sketchpad zeichnen: 

💬 **Prompt:**

```text
Bitte zeichne einen zentralen Fixationspunkt im item fixation und setze seine Dauer auf 500 ms.
```

%--
figure:
 id: FigStep6
 source: step6.png
 caption: "The fixation display"
--%


## Schritt 7: Das visuelle Suchdisplay erzeugen

Das visuelle Suchdisplay zu erzeugen, geht über das hinaus, was die grafische Benutzeroberfläche von OpenSesame leisten kann. Wir brauchen eine dynamische Erzeugung von Stimuli, zufällige Platzierung und bedingte Logik. OpenSesame bietet die Möglichkeit, dies mit Python (`inline_script`) oder JavaScript (`inline_javscript`) umzusetzen. In unserem Fall verwenden wir Python. Ein (leeres) inline script haben wir bereits in Schritt 5 zur trial sequence hinzugefügt.

Aber was, wenn wir selbst kein script schreiben können oder wollen? Sigmund kann das für uns erledigen! Sagen Sie Sigmund, dass er das script schreiben soll, das wir benötigen: 

💬 **Prompt:**

```text
Implementiere jetzt das Suchdisplay mit dem inline script. Es soll:

- ein canvas erstellen
- zufällige, sich nicht überlappende Positionen erzeugen
- das target zeichnen, falls vorhanden
- Distraktoren abhängig von der condition zeichnen:
  - conjunction: jede Form/Farbe außer der target-Kombination
  - feature_shape: die Form muss sich vom target unterscheiden
  - feature_color: die Farbe muss sich vom target unterscheiden
- die Variable set_size für die Anzahl der items verwenden
- einen Fehler auslösen, wenn ungültige Werte auftreten

Das script soll das canvas anzeigen.
```

Da diese Aufgabe etwas komplexer ist, macht Sigmund manchmal Fehler. Sigmund kann sie jedoch möglicherweise selbst beheben! Versuchen Sie, das Experiment auszuführen, und falls ein Fehler zurückgegeben wird, bitten Sie Sigmund, ihn zu beheben.

Ein Beispiel für einen häufigen Fehler ist, dass Sigmund manchmal vergisst, eine Python-Bibliothek zu importieren, wie zum Beispiel `random`. Wenn dir das auffällt, kannst du darauf hinweisen und Sigmund bitten, es zu beheben!

💬 **Prompt:**

```text
It looks like you forgot to import random. Please fix it!
```

Wenn alles gut gelaufen ist, kannst du das Experiment jetzt ausführen (auch wenn es noch unvollständig ist), und es wird eine Anzeige wie diese zeigen:

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "A visual search display."
--%


## Schritt 8: Die korrekte Antwort definieren 

Das keyboard_response-Item, das Sigmund zuvor eingefügt hat, prüft Antworten anhand einer Variable namens correct_response. Deshalb müssen wir definieren, was die korrekte Antwort ist, bevor die Reaktion erfasst wird. Wir können Sigmund mit einem inline script darum bitten: 

💬 **Prompt:**

```text
Add logic so the experiment knows the correct response.

- If target_present is present → correct_response is right arrow key.
- If target_present is absent → correct_response is left arrow key.

Please implement this using a new inline script placed before the keyboard response item.
```

## Schritt 9: Die keyboard_response konfigurieren 

Nur die linke und rechte Pfeiltaste sind gültige Antworten, daher beschränken wir die Teilnehmenden auf diese Tasten. Wir können Sigmund auch bitten, nach einer festgelegten Zeitspanne automatisch zum nächsten Trial weiterzugehen, falls die teilnehmende Person nicht innerhalb einer angemessenen Zeit reagiert (d. h. ein Timeout).

💬 **Prompt:**

```text
Please configure the keyboard response so that:

- timeout is 3000 ms
- only left and right arrow keys are allowed
```

## Schritt 10: Die Feedback-Anzeigen erstellen 

Als Nächstes möchten wir den Teilnehmenden Feedback dazu geben, ob sie die Anwesenheit des Ziels in einem Trial korrekt erkannt haben. Bitte Sigmund, die Feedback-sketchpads dynamisch festzulegen:

💬 **Prompt:**

```text
Now configure the feedback sketchpads:

- green_feedback should show a green fixation dot for 500 ms
- red_feedback should show a red fixation dot for 500 ms

Show green only after correct responses and red only after incorrect responses.
```

## Schritt 11: Blockanweisungen 

Die Teilnehmenden müssen wissen, wonach sie suchen sollen! Bitte Sigmund, den Anweisungsbildschirm zu erstellen und eine Darstellung des aktuellen Ziels anzuzeigen: 

💬 **Prompt:**

```
Please add instructions to block_instructions that tell participants which target to search for, based on the current block’s target shape and color. Visually show what the target looks like.
```

%--
figure:
 id: FigStep11
 source: step11.png
 caption: "The instruction display."
--%


## Schritt 12: Block-Feedback 

Nach jedem Block geben wir den Teilnehmenden Feedback dazu, wie gut sie abgeschnitten haben, basierend auf Genauigkeit und Reaktionszeit. Lass Sigmund den Bildschirm für uns erstellen:

💬 **Prompt:**

```text
Configure the feedback item so it shows average accuracy and response time for the block.
```

%--
figure:
 id: FigStep12
 source: step12.png
 caption: "The block feedback display."
--%


## Schritt 13: Abschlussnachricht

Zum Schluss fügen wir eine Abschlussnachricht hinzu.

💬 **Prompt:**

```text
Set an end of experiment message in end_message.
```

## Fertig

Glückwunsch, das Experiment ist abgeschlossen! Du kannst einen Testlauf starten, indem du auf die blaue Doppelpfeil-Schaltfläche klickst (Tastenkürzel: Ctrl+W).

So sieht ein abgeschlossener Visual-Search-Block aus:

<video controls width="100%">
  <source src="/video/visual-search-demo.mp4" type="video/mp4">
</video>

<p align="center"><em>Video 2. Demonstration of a completed visual-search block.</em></p>

Um sicherzustellen, dass das Experiment gut funktioniert, prüfe, ob du die folgenden Elemente wiedererkennst:

1. Jeder Block beginnt mit Anweisungen, die die aktuelle Zielform und -farbe zeigen
2. Jeder Trial hat einen Fixationspunkt und das korrekte Feedback wird direkt nach jedem Trial angezeigt 
3. Über die Trials hinweg variieren Set-Größen und Zielanwesenheit 
4. Nach jedem Block gibt es eine Leistungszusammenfassung

Falls dir kleine Bugs oder Fehler auffallen—keine Sorge. Sigmund kann diese oft selbst beheben. Versuche, das Experiment auszuführen, und wenn ein Fehler erscheint, beschreibe Sigmund einfach das Problem und bitte ihn, es zu beheben. Zum Beispiel kann Sigmund in der Regel fehlende imports, falsche Variablennamen oder kleine Logikfehler beheben, wenn du ihn darauf hinweist. Zu lernen, dein Experiment zu testen und Sigmund iterativ um gezielte Korrekturen zu bitten, ist ein wichtiger Teil davon, effizient mit einem KI-Copiloten zu arbeiten.

## References

<div class='reference' markdown='1'>
Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, *12*(1), 97–136. doi:10.1016/0010-0285(80)90005-5
</div>

[references]: #references