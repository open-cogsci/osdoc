title: Verwenden Sie guided generation, um ein beliebiges Experiment mit SigmundAI zu erstellen
hash: 9fd2992708f865ec29c9a7080a645de89d5d0a9619c8e543101fe468cd89d355
locale: de
language: German

[TOC]


## Über dieses Tutorial

In diesem Tutorial lernst du, wie du jedes Experiment mit SigmundAI erstellen kannst. Dies ist kein Schritt-für-Schritt-Tutorial, das auf ein bestimmtes Experiment fokussiert ist. Stattdessen beschreibt es einen allgemeinen Workflow, den du an deine Bedürfnisse anpassen kannst.

Erwarte keine Wunder! Wenn du ein komplexes Experiment hast, wird Sigmund wahrscheinlich Schwierigkeiten haben, wenn es völlig sich selbst überlassen wird. Oft musst du aktiv mit Sigmund zusammenarbeiten, um ein Experiment zu implementieren.

Ich bezeichne dies als *guided generation*, weil du Sigmund durch den Prozess führst.

Falls du noch nicht mit Sigmund gearbeitet hast, empfehle ich dir, zuerst [das Einsteiger-Tutorial für SigmundAI](%url:beginner-sigmund%) abzuschließen.


## Was du lernen wirst

Am Ende dieses Tutorials wirst du wissen, wie man:

- 💡 Sigmund klare, effektive Anweisungen gibt
- 💡 den Prozess, ein vollständiges Experiment von Grund auf zu erstellen, in überschaubare Schritte aufteilt
- 💡 Fehler behebt, die Sigmund beim Erstellen eines Experiments machen kann.


## Welches Modell sollte ich verwenden?

Die meisten Schritte erfordern kein besonders leistungsstarkes Modell. Ich verwende meistens Z.ai GLM 5.2, das zum Zeitpunkt des Schreibens ein gutes Gleichgewicht zwischen Intelligenz und Kosten bietet. Der abschließende Implementierungsschritt bringt jedoch die Grenzen dessen, was die meisten KI-Modelle leisten können, an ihre Grenzen. Daher kannst du an diesem Punkt zu einem leistungsstärkeren Modell wechseln, etwa Claude Sonnet 5. Bedenke jedoch, dass leistungsstärkere Modelle auch (deutlich) teurer sind.

In der Praxis solltest du verschiedene Modelle ausprobieren, um zu sehen, was für deine spezifischen Experimente die besten Ergebnisse liefert.


## Workflow

Folgendes werden wir tun:

1. Beschreibe das Experiment, das du erstellen möchtest, in klarer Sprache.
2. Bitte Sigmund, deine Beschreibung zu einer umfassenden narrativen Beschreibung auszuarbeiten, die das Experiment vollständig im Detail spezifiziert.
3. Überprüfe die umfassende Beschreibung. Falls nötig, diskutiere sie und passe sie an.
4. Bitte Sigmund, eine JSON-Spezifikation (ein menschenlesbares technisches Format) zu erstellen, die die experimentelle Struktur beschreibt.
5. Überprüfe die JSON-Spezifikation. Falls nötig, diskutiere sie und passe sie an.
6. Bitte Sigmund, das gesamte Experiment auf einmal zu erstellen.
7. Teste und verfeinere das Experiment.

In diesem Tutorial geht es darum, effektiv mit Sigmund zu kommunizieren. Wir werden Sigmund dabei helfen, die komplexe Aufgabe, ein Experiment zu erstellen, in überschaubare Teilaufgaben zu unterteilen, und konkrete Anweisungen geben, was wann zu tun ist.

__Wichtig:__ Du musst mit Sigmund über das Chat-Panel innerhalb von OpenSesame sprechen. Wenn du das Web-Interface verwendest, kann Sigmund OpenSesame nicht steuern.


## Entwicklung einer umfassenden narrativen Beschreibung des Experiments

Hier ist die Experimentbeschreibung, die wir für dieses Beispiel verwenden werden:

💬 **Beschreibung:**

```text
Eine typische Visual-Working-Memory-Aufgabe, bei der Kreise unterschiedlicher Farben erinnert werden müssen. Ein Kreis wird getestet, indem an der ursprünglichen Position des Kreises ein Kreis entweder in derselben oder in einer anderen Farbe präsentiert wird. Die Versuchsperson antwortet mit einem Gleich-/Verschieden-Urteil. Die Setgröße wird variiert.
```

Wir beginnen damit, Sigmund zu bitten, auf Grundlage dieser Beschreibung eine detaillierte Beschreibung eines Experiments auszuarbeiten. Gib in deiner Experimentbeschreibung so viele Details wie möglich an, denn das hilft Sigmund dabei, ein Design zu entwickeln, das deinen Vorstellungen entspricht. Wenn du zum Beispiel denkst, dass die trial logic mit einem `inline_script` implementiert werden sollte, gib dies an.

Wir fügen diese Beschreibung in einen Prompt ein, der Sigmund klare Anweisungen gibt:

💬 **Prompt:**

```text
Ich habe eine anspruchsvolle Aufgabe für dich! Wir werden ein OpenSesame-Experiment von Grund auf implementieren. Wir werden den Prozess in einige Schritte unterteilen, damit alles überschaubar bleibt. Im aktuellen Schritt besteht deine Aufgabe darin, die Beschreibung der experimentellen Aufgabe so zu erweitern, dass sie alle Details enthält, die wir für ihre Implementierung brauchen.

Hier sind einige Dinge, die du für die trial structure berücksichtigen solltest:
```

- Die Art und Weise, wie die Teilnehmenden reagieren
- Das Timing der Stimuli
- Das Erscheinungsbild der Stimuli
- Das Layout der Stimuli
- Ob Rückmeldung für die Teilnehmenden gegeben wird und falls ja, wie
- Alle Stimuli, die nicht ausdrücklich erwähnt werden, aber enthalten sein sollten
- Leere oder Fixationsanzeigen zwischen den Stimuli (wenn es einen Fixationspunkt gibt, wird dieser üblicherweise während des gesamten Trials angezeigt)

Hier sind einige Dinge, die Sie für die Experimentstruktur berücksichtigen sollten:

- Unabhängige und abhängige Variablen
- Ob es eine Übungsphase gibt oder nicht
- Ob die Trials in Blöcke von Trials unterteilt sind oder nicht
- Die Anzahl der Trials und (falls zutreffend) Blöcke
- Alle Willkommens-, Instruktions- und Abschiedsbildschirme

Bitte fügen Sie auch alle zusätzlichen Informationen hinzu, die Sie für relevant halten.

<experimental_task_description>
Eine typische visuelle Arbeitsgedächtnisaufgabe, bei der Kreise in verschiedenen Farben erinnert werden müssen. Ein Kreis wird abgefragt, indem ein Kreis entweder in derselben oder in einer anderen Farbe an der ursprünglichen Position des Kreises präsentiert wird. Die teilnehmende Person antwortet mit einem Gleich-/Verschieden-Urteil. Die Set-Größe wird variiert.
</experimental_task_description>

Bitte antworten Sie mit einer umfassenden Beschreibung. Speichern Sie sie noch nicht als Notiz, denn wir werden sie zuerst überprüfen.
```

Sigmund wird mit einer ausführlichen Beschreibung des Experiments antworten. Überprüfen Sie sie und nehmen Sie bei Bedarf Korrekturen vor. Wenn Sie zufrieden sind, bitten Sie Sigmund, eine Notiz daraus zu machen.


💬 **Prompt:**

```text
Super! Bitte speichere die umfassende Beschreibung als dauerhafte Notiz, damit du sie nicht vergisst. Fasse sie nicht zusammen, sondern speichere sie vollständig.
```


## Entwicklung einer JSON-Spezifikation für die Experimentstruktur

Jetzt werden wir Sigmund bitten, die Experimentstruktur zu entwerfen. Diese legt fest, aus welchen items das Experiment besteht und wie sie miteinander verbunden sind.

Der zweite Punkt des Prompts erwähnt, welche item-Typen verwendet werden können. Um Sigmund zu helfen, entferne item-Typen, von denen du weißt, dass sie nicht notwendig sein werden. Wenn Teilnehmende zum Beispiel nicht die Maus zum Antworten verwenden, kannst du den item-Typ `mouse_response` entfernen.


💬 **Prompt:**

```text
Weiter geht's! Hier ist deine nächste Aufgabe:

- Erstelle eine JSON-Spezifikation basierend auf der narrativen Beschreibung des Experiments, die du gerade als Notiz gespeichert hast.
- Jedes dict in der JSON sollte einem einzelnen OpenSesame-Item entsprechen. Du kannst die folgenden Items verwenden: [loop, sequence, sketchpad, feedback, synth, sampler, keyboard_response, mouse_response, logger, inline_script, inline_javascript, form_multiple_choice, form_text_display, form_text_input, reset_feedback]
- sketchpad-Items werden im Voraus vorbereitet und können daher keine Variablen berücksichtigen, die nach ihrer prepare-Phase definiert werden. Daher solltest du, um Displays mit variablem Inhalt anzuzeigen, oft lieber feedback-Items verwenden, aber nur für Displays, die nicht zeitkritisch sind.
- Verwende nicht mehrere nicht verknüpfte logger-Items, da dies zu unübersichtlichen Log-Dateien führt. Verwende stattdessen verknüpfte Kopien desselben logger.
- Platziere keine reset_feedback-Items in der main experiment sequence, da dies nicht mit OSWeb kompatibel ist.
- Füge keine Implementierungsdetails für die Items ein. Dazu kommen wir später. Gib vorerst nur eine Beschreibung, einen Namen und einen Typ an. Für Items, die Teil einer sequence sind, kannst du auch einen run-if-Ausdruck angeben. Für Items, die verknüpfte Kopien von Items sind, die an anderer Stelle vorkommen, gib Details nur für das erste Vorkommen an und für nachfolgende Vorkommen nur den Namen (Items mit demselben Namen sind verknüpfte Kopien).
- Items, die Child-Items haben, haben zusätzlich ein Feld `items`. Ein loop hat immer genau eine sequence als Child-Item. Eine sequence hat im Allgemeinen mehrere Child-Items verschiedener Typen.
- Bitte verwende nach Möglichkeit verknüpfte Kopien von Items. Um anzuzeigen, dass ein Item eine verknüpfte Kopie eines anderen ist, verwende einfach denselben Namen und füge ein Feld `linked` hinzu, das auf `true` gesetzt ist.
- Das unten stehende Beispiel einer JSON-Spezifikation zeigt die allgemeine Idee, ist aber stark vereinfacht. Deine JSON-Spezifikation wird wahrscheinlich deutlich ausführlicher sein.

<json_example>
{
  "name": "experiment",
  "type": "sequence",
  "description": "Eine einzeilige Beschreibung der Aufgabe",
  "items": [
    {
      "name": "task_description",
      "type": "notepad",
      "description": "Die vollständige narrative Beschreibung der Aufgabe steht hier."
    },
    {
      "name": "welcome",
      "type": "sketchpad",
      "description": "Kurze Begrüßungsnachricht"
    },
    {
      "name": "block_loop",
      "type": "loop",
      "description": "Ein Block von Trials. Unabhängige Variablen werden hier ebenfalls definiert.",
      "items": [
        {
          "name": "trial_sequence",
          "type": "sequence",
          "description": "Sequence für einen einzelnen Trial",
          "items": [
            {
              "name": "fixation",
              "type": "sketchpad",
              "description": "Zeigt 500 ms lang ein schwarzes Fixationskreuz (+)"
            },
            {
              "name": "target_display",
              "type": "sketchpad",
              "description": "Zeigt den target-Stimulus, während das Fixationskreuz sichtbar bleibt"
            },
            {
              "name": "keyboard_response",
              "type": "keyboard_response",
              "description": "Erfasst die Antwort der Versuchsperson auf den target-Stimulus"
            },
            {
              "name": "correct_feedback",
              "type": "sketchpad",
              "description": "Zeigt nach einer korrekten Antwort 500 ms lang einen grünen Fixationspunkt",
              "run_if": "correct == 1"
            },
            {
              "name": "fixation",
              "linked": true
            },
            {
              "name": "logger",
              "type": "logger",
              "description": "Protokolliert alle Trial-Daten"
            }
          ]
        }
      ]
    }
  ]
}
</json_example>

Bitte antworte mit der JSON-Spezifikation für die narrative Beschreibung des Experiments. Speichere die JSON-Spezifikation noch nicht als Notiz, da wir sie zuerst überprüfen werden.
```

Sigmund wird nun eine detaillierte JSON-Spezifikation bereitstellen, die im Wesentlichen eine technische Ansicht des Übersichtsbereichs in OpenSesame ist. Prüfe die Spezifikation und gib bei Bedarf Feedback. Wenn du zufrieden bist, bitte Sigmund, sich eine Notiz dazu zu machen.

💬 **Prompt:**

```text
Beautiful, well done Sigmund! Please save this as another persistent note so you don't forget. Do not summarize it, but save it in full.
```


## Implementierung des Experiments

Jetzt kann es losgehen! Dieser letzte Schritt geht an die Grenzen dessen, was die meisten AI-Modelle leisten können. Wenn du feststellst, dass Sigmund wiederholt scheitert, versuche, zu einem leistungsfähigeren Modell zu wechseln. Ich habe mit Claude Sonnet 5 gute Erfahrungen gemacht.

💬 **Prompt:**

```text
We're now ready to implement the experiment. A few pointers:

- Save these instructions as a persistent note so you don't forget.
- Do *not* inspect items of the current experiment. They're not relevant, because we're going to completely overwrite the current experiment.
- Do *not* inspect the general script of the current experiment for the same reason.
- Before writing the experiment script, call `opensesame_get_syntax_documentation` with `save_as="note"` to get all relevant documentation.
- Finally, write the new experiment as a single complete general script and pass it to `opensesame_update_general_script`.

This is a challenging task, but I know you can do it. Let's go!
```

Sigmund schafft es, das als Beispiel verwendete Visual-Working-Memory-Experiment erfolgreich zu implementieren. Allerdings werden nicht alle Experimente reibungslos verlaufen.

Wenn Sigmund bemerkt, dass es beim Generieren des Experiments einen Syntaxfehler gemacht hat, wird es versuchen, diesen zu beheben. Dabei kann Sigmund in einer Endlosschleife stecken bleiben, während es versucht, alles zum Laufen zu bringen. Wenn das passiert, brich die Konversation ab.

Wenn das Experiment erfolgreich generiert wurde, kann es dennoch Fehler oder Unvollkommenheiten enthalten. Teste und optimiere es sorgfältig!


## Beispiele für Experimente, die mit geführter Generierung erstellt wurden

Bei allen folgenden Beispielen wurden die ersten Schritte mit Z.ai GLM 5.2 durchgeführt, und der letzte Implementierungsschritt wurde mit Claude Sonnet 5 ausgeführt. Ich habe kein Feedback zur umfassenden Beschreibung oder zur JSON-Spezifikation gegeben. Das endgültige Experiment habe ich jedoch, wie in den folgenden Notizen beschrieben, nachbearbeitet.


### Visuelles Arbeitsgedächtnis

💬 **Beschreibung:**

```text
A typical visual-working-memory task where circles of different colors need to be remembered. One circle is probed by presenting a circle of either the same or a different color at the original circle's location. The participant responds with a same/different judgment. Set size is varied.
```

Notizen:

- Sigmund verwendete die veraltete `[square_brackets_syntax]`, um in sketchpad-Items auf Variablen zu verweisen. Das funktioniert, aber ich habe es auf die bevorzugte `{curly_brackets_syntax}` geändert.
- Sigmund verwendete für dieses Experiment Python INLINE_SCRIPT. Daher kann es nicht in einem Browser ausgeführt werden.

Probiere das Experiment aus:

- %static:attachments/sigmund/sigmund-visual-working-memory.osexp%


### Posner-Cueing

💬 **Beschreibung:**

```text
A Posner cuing paradigm with a central cue and a letter-discrimination task.
```

Notizen:

- Sigmund verwendete Unicode-Marker (z. B. `\u2190`) für Pfeil-Cues. Diese werden von OpenSesame nicht gerendert und mussten durch die tatsächlichen Zeichen ersetzt werden (z. B. „←“).
- Sigmund verwendete die veraltete `[square_brackets_syntax]`, um in sketchpad-Items auf Variablen zu verweisen. Das funktioniert, aber ich habe es auf die bevorzugte `{curly_brackets_syntax}` geändert.

Probiere das Experiment aus:

- %static:attachments/sigmund/sigmund-posner-cuing.osexp%
- [Im Browser ausführen](https://jatos.mindprobe.eu/publix/QgymMCSRYzL)


### AX continuous performance

💬 **Beschreibung:**

```text
An AX continuous performance task.
```

Notizen:

- Sigmund vergaß festzulegen, welche Items in den verschiedenen `sequence`-Items ausgeführt werden sollen. Dies musste manuell korrigiert werden.

Probiere das Experiment aus:

- %static:attachments/sigmund/sigmund-axcpt.osexp%
- [Im Browser ausführen](https://jatos.mindprobe.eu/publix/5s8TbGLx0bZ)