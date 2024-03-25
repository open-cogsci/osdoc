title: Fortgeschrittenes Tutorial (JavaScript): Visuelle Suche
hash: 8a884ef49e4ac79ec8dd0e01bf078980622b9f0365927917c21e42253e76321c
locale: de
language: German

[TOC]

## Über OpenSesame

OpenSesame ist ein benutzerfreundliches Programm für die Entwicklung von Verhaltensexperimenten in den Bereichen Psychologie, Neurowissenschaften und experimentelle Ökonomie. Für Anfänger bietet OpenSesame eine umfassende grafische, Point-and-Click-Oberfläche. Für fortgeschrittene Nutzer:innen unterstützt OpenSesame Python (nur Desktop) und JavaScript (Desktop und Browser).

OpenSesame ist frei verfügbar unter der [General Public License v3][gpl].

## Über dieses Tutorial

Dieses Tutorial zeigt, wie Sie ein einfaches visuelles Suchexperiment mit OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012)][references] erstellen. Wir werden sowohl die grafische Oberfläche als auch JavaScript verwenden, um ein Experiment zu entwickeln, das Sie online in einem Browser ausführen können. Einige Erfahrungen mit OpenSesame und JavaScript werden empfohlen. Dieses Tutorial dauert etwa eine Stunde.

Eine auf Python basierende Version dieses Tutorials ist ebenfalls verfügbar. Wenn Sie Ihre Experimente nicht online durchführen müssen, ist das Python-Tutorial wahrscheinlich das, was Sie benötigen:

- %link:tutorials/intermediate%

## Ressourcen

- __Herunterladen__ — Dieses Tutorial setzt voraus, dass Sie OpenSesame Version 4.0.0 oder neuer und OSWeb 2.0 oder neuer verwenden. Sie können die neueste Version von OpenSesame hier herunterladen:
	- %link:download%
- __Dokumentation__ — Eine dedizierte Dokumentationswebsite finden Sie unter:
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Ein Supportforum finden Sie unter:
	- <http://forum.cogsci.nl/>
- __Sigmund__ -- SigmundAI ist ein KI-Assistent mit Expertenwissen über OpenSesame und ist unter folgender Adresse erreichbar:
	- <https://sigmundai.eu/>

## Das Experiment

In diesem Tutorial erstellen Sie ein einfaches visuelles Suchexperiment. Das Experiment ähnelt den klassischen Studien zur visuellen Suche von [Treisman und Gelade (1980)][references], ist jedoch nicht identisch.

Bevor Sie beginnen, das Experiment selbst zu *erstellen*, können Sie bereits *teilnehmen*. Dies gibt Ihnen eine gute Vorstellung davon, worauf Sie in diesem Tutorial hinarbeiten.

<a role="button" class="btn btn-success btn-align-left" href="https://jatos.mindprobe.eu/publix/1938/start?batchId=2191&generalMultiple">Am Experiment teilnehmen!</a>

In diesem Experiment suchen die Teilnehmenden nach einem Zielobjekt, das ein gelbes Quadrat, ein gelber Kreis, ein blaues Quadrat oder ein blauer Kreis sein kann; die Identität des Ziels variiert zwischen den Blöcken. Die Teilnehmenden geben an, ob das Ziel vorhanden ist oder nicht, indem sie die rechte (vorhanden) oder linke (nicht vorhanden) Pfeiltaste drücken.

Zusätzlich zum Zielobjekt werden null oder mehr Ablenkungsobjekte gezeigt. Es gibt drei Bedingungen, und die Bedingung bestimmt, welche Art von Ablenkern vorhanden sind:

- In der *Conjunction*-Bedingung können Ablenker jede Form und Farbe haben, jedoch mit der Einschränkung, dass Ablenker nicht identisch mit dem Ziel sein dürfen. Wenn das Ziel also ein gelbes Quadrat ist, dann sind die Ablenker gelbe Kreise, blaue Kreise und blaue Quadrate.
- In der *Shape Feature*-Bedingung haben Ablenker eine andere Form als das Ziel, können aber jede Farbe haben. Wenn das Ziel also ein gelbes Quadrat ist, dann sind die Ablenker gelbe und blaue Kreise.
- In der *Color Feature*-Bedingung können Ablenker jede Form haben, aber eine andere Farbe als das Ziel. Wenn das Ziel also ein gelbes Quadrat ist, dann sind die Ablenker blaue Quadrate und blaue Kreise.

Nach jedem Versuch wird sofortiges Feedback gegeben: ein grüner Punkt bei einer richtigen Antwort und ein roter Punkt bei einer falschen Antwort. Detailliertes Feedback zu durchschnittlichen Reaktionszeiten und Genauigkeit wird nach jedem Block angezeigt.

%--
Abbildung:
 id: FigVisualSearch
 Quelle: visual-search.svg
 Bildunterschrift: |
  Das visuelle Suchexperiment, das Sie in diesem Tutorial umsetzen werden.
--%

Experimente wie dieses zeigen zwei typische Ergebnisse:

- Es dauert länger, das Ziel in der Verbindungskondition zu finden als in den beiden Merkmalsbedingungen.
- In der Verbindungskondition steigen die Reaktionszeiten, wenn die Anzahl der Störreize zunimmt. Dies legt nahe, dass die Menschen das Ziel nacheinander suchen; dies wird als *serielle Suche* bezeichnet.
- In den Merkmalsbedingungen (sowohl Form als auch Farbe) nehmen die Reaktionszeiten nicht oder kaum zu, wenn die Anzahl der Störreize zunimmt. Dies legt nahe, dass die Menschen das gesamte Bild gleichzeitig verarbeiten; dies wird als *parallele Suche* bezeichnet.

Nach Treisman und Gelades Merkmals-Integrations-Theorie spiegeln diese Ergebnisse wider, dass die Verbindungskondition erfordert, dass Sie die Farbe und die Form jedes Objekts kombinieren oder *binden*. Diese Bindung erfordert Aufmerksamkeit, und Sie müssen daher Ihre Aufmerksamkeit von einem Objekt zum nächsten verschieben; dies ist langsam und erklärt, warum die Reaktionszeiten davon abhängen, wie viele Objekte es gibt. Im Gegensatz dazu müssen in den Merkmalsbedingungen Farbe und Form nicht gebunden werden, und daher kann das gesamte Bild in einem einzigen Durchlauf verarbeitet werden, ohne dass die Aufmerksamkeit auf jedes einzelne Objekt gerichtet ist.

## Versuchsaufbau

Dieser Aufbau:

- Ist *innerhalb-subjektiv*, da alle Teilnehmer alle Bedingungen durchführen
- Ist *vollständig gekreuzt* (oder vollfaktoriell), da alle Kombinationen von Bedingungen auftreten
- Hat drei Bedingungen (oder Faktoren):
	- Variiert innerhalb von Blöcken:
		- `set_size` mit drei Stufen (1, 5, 15) oder SS<sub>3</sub>
		- `condition` mit drei Stufen (Verbindung, Merkmal_Form, Merkmal_Farbe) oder CN<sub>3</sub>
		- `target_present` mit zwei Stufen (vorhanden, abwesend) oder TP<sub>2</sub>
	- Variiert zwischen Blöcken:
		- `target_shape` mit zwei Stufen (Quadrat, Kreis) oder TS<sub>2</sub>
		- `target_color` mit zwei Stufen (gelb, blau) oder TC<sub>2</sub>
- Hat N Probanden, oder <u>S</u><sub>N</sub>

Sie können diesen Versuchsaufbau als <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub> schreiben

Weitere Informationen zu dieser Notation für den Versuchsaufbau finden Sie unter:

- %link:experimentaldesign%

## Schritt 1: Erstellen Sie die grundlegende Struktur des Experiments

Starten Sie OpenSesame und wählen Sie im Tab "Get started!" die Erweiterte Vorlage aus. Diese Vorlage bietet die grundlegende Struktur, die in vielen kognitiven Psychologieexperimenten üblich ist, wie zum Beispiel dem, das wir hier erstellen werden.

Die erweiterte Vorlage enthält einige Elemente, die wir nicht benötigen. Löschen Sie die folgenden Elemente:

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Wenn Sie diese Elemente gelöscht haben, sind sie noch im "Unused items" -Behälter sichtbar. Um diese Elemente endgültig zu löschen, klicken Sie auf den "Unused items" -Behälter und dann auf die Schaltfläche "Unused items endgültig löschen".

Geben Sie dem Experiment schließlich einen guten Titel, wie zum Beispiel "Visuelle Suche". Um dies zu tun, öffnen Sie die Registerkarte Allgemeine Eigenschaften (indem Sie im Übersichtsbereich auf "Extended template" klicken) und klicken Sie auf den Experimentnamen, um ihn zu bearbeiten.

Richten Sie OpenSesame auch so ein, dass das Experiment in einem Browser und nicht auf dem Desktop ausgeführt wird.

Der Übersichtsbereich sollte jetzt wie %FigStep1 aussehen:

%--
Abbildung:
 id: FigStep1
 source: step1.png
 caption: |
  Der Übersichtsbereich am Ende von Schritt 1.
--%


## Schritt 2: Definition von experimentellen Variablen, die zwischen Blöcken variieren

Wie oben beschrieben, werden zwei Variablen in unserem Experiment zwischen Blöcken variiert: `target_shape` und `target_color`. Daher müssen wir diese Variablen in der *experimental_loop* definieren. Um zu verstehen, warum, betrachten Sie die Struktur in %FigStep1, beginnend ab dem unteren Rand (d.h. der am stärksten eingerückten Ebene).

- *trial_sequence* entspricht einem einzelnen Versuch
- *block_loop* entspricht einem Block von Versuchen
	- Daher variieren hier definierte Variablen für jeden Durchlauf von *trial_sequence*; mit anderen Worten, in *block_loop* definierte Variablen variieren __innerhalb von Blöcken__.
- *block_sequence* entspricht einem Block von Versuchen, gefolgt von einem Zurücksetzen der Feedback-Variablen und Teilnehmer-Feedback
- *experimental_loop* entspricht mehreren Blöcken von Versuchen
	- Daher variieren hier definierte Variablen für jeden Durchlauf von *block_sequence*; mit anderen Worten, in *experimental_loop* definierte Variablen variieren __zwischen den Blöcken__.
- *experiment* entspricht dem gesamten Experiment, das aus einem Anweisungsbildschirm, gefolgt von mehreren Blöcken von Versuchen und einem End-of-Experiment-Bildschirm besteht

Klicken Sie auf die experimentelle Schleife und definieren Sie:

- `target_shape`, das entweder 'quadrat' oder 'kreis' sein kann; und
- `target_color`, das entweder 'gelb' oder 'blau' sein kann.

Wir haben ein vollfaktorielles Design, das bedeutet, dass alle 2 × 2 = 4 Kombinationen vorkommen müssen. Die Tabelle von *experimental_loop* sollte jetzt wie %FigStep2 aussehen:

%--
Abb.:
 ID: FigStep2
 Quelle: step2.png
 Bildunterschrift: |
  Die Tabelle von *experimental_loop* am Ende von Schritt 2.
--%

## Schritt 3: Anweisungen vor jedem Block geben

Im Moment beginnt das Experiment mit einem einzigen *Anweisungen*-Bildschirm. In unserem Fall möchten wir vor jedem Block von Versuchen Anweisungen geben, um dem Teilnehmer mitzuteilen, nach welchem Ziel er suchen soll (weil die Identität des Ziels zwischen den Blöcken variiert).

__Verschieben Sie die Anweisungen in block_sequence__

Heben Sie dazu den *Anweisungen*-Gegenstand auf und ziehen Sie ihn auf *block_sequence*. Es erscheint ein Popup, das Sie fragt, ob Sie:

- das Element in *block_sequence* einfügen möchten, in diesem Fall würden *Anweisungen* zum ersten Element von *block_sequence* werden oder
- das Element nach *block_sequence* einfügen möchten, in diesem Fall würden *Anweisungen* an eine Position nach *block_sequence* verschoben.

Wählen Sie die erste Option ('Einfügen in'). Jetzt beginnt *block_sequence* mit einem Anweisungsbildschirm, was wir wollen.

__Fügen Sie Anweisungstext hinzu__

Klicken Sie auf *Anweisungen*, um sie zu öffnen, und fügen Sie einen guten Anweisungstext hinzu, wie zum Beispiel:

```text
ANWEISUNGEN

Suchen Sie nach dem {target_color} {target_shape}

Drücken Sie die rechts-Pfeiltaste, wenn Sie es gefunden haben
Drücken Sie die links-Pfeiltaste, wenn Sie es nicht gefunden haben

Drücken Sie eine beliebige Taste, um zu beginnen
```

Die geschweiften Klammern um '{target_color}' und '{target_shape}' zeigen an, dass dies kein wörtlicher Text ist, sondern sich auf die Variablen bezieht, die wir in *experimental_loop* definiert haben. Wenn das Experiment läuft, werden die Werte dieser Variablen hier erscheinen und der Teilnehmer wird sehen (zum Beispiel) 'Suchen Sie nach dem gelben Kreis'.

__Geben Sie eine visuelle Vorschau des Ziels__

Es ist auch gut, dem Teilnehmer das tatsächliche Stimulus zu zeigen, das sie finden muss. Um dies zu tun:

- Zeichnen Sie einen gefüllten Kreis in der Mitte der Anzeige (achten Sie darauf, dass er sich nicht mit dem Text überschneidet);
- Ändern Sie die Farbe des Kreises in '{target_color}'. Dies bedeutet, dass die Farbe des Kreises von dem Wert der Variablen `target_color` abhängt; und
- Ändern Sie den show-if-Ausdruck in `target_shape == 'kreis'`. Dies ist ein Python-Ausdruck, der prüft, ob die Variable `target_shape` den Wert 'kreis' hat. Beachten Sie, dass Sie zwar keine vollwertigen Python `inline_script`-Elemente für die Ausführung von Experimenten in einem Browser verwenden können, aber Sie *können* Python für diese einfachen bedingten Ausdrücke verwenden.

Mit anderen Worten, wir haben einen Kreis gezeichnet, dessen Farbe durch `target_color` bestimmt wird; außerdem wird dieser Kreis nur angezeigt, wenn die Variable `target_shape` den Wert 'kreis' hat. Für weitere Informationen über Variablen und Show-if-Anweisungen siehe:

- %link:manual/variables%

Wir verwenden den gleichen Trick, um ein Quadrat zu zeichnen:

- Zeichnen Sie ein gefülltes Quadrat in der Mitte der Anzeige;
- Ändern Sie die Farbe des Quadrats in '{target_color}'; and
- Ändern Sie die Show-if-Anweisung in `target_shape == 'quadrat'`

Der *Anweisungen*-Bildschirm sollte jetzt wie %FigStep3 aussehen:

%--
Abbildung:
 id: FigStep3
 source: step3.png
 caption: |
  Der *Anweisungen* Bildschirm am Ende von Schritt 3.
--%


## Schritt 4: Experimentelle Variablen definieren, die innerhalb von Blöcken variieren

In unserem Experiment variieren innerhalb von Blöcken drei Variablen: `condition`, `set_size` und `target_present`. Wie unter Schritt 2 beschrieben, müssen wir diese Variablen im *block_loop* definieren, damit sie bei jedem Durchlauf von *trial_sequence* variieren.

Die drei Variablen ergeben insgesamt 3 × 3 × 2 = 18 verschiedene Kombinationen. Wir können diese manuell in die Tabelle eingeben, aber da wir ein vollfaktorielles Design haben, können wir auch den Vollfaktorielles-Design-Assistenten verwenden. Um dies zu tun, öffnen Sie zuerst *block_loop* und klicken Sie auf die Schaltfläche "Vollfaktorielles Design".

Geben Sie in der erscheinenden Tabelle die Variablennamen in der ersten Zeile und die Werte in den Zeilen darunter ein, wie in %FigFullFactorial gezeigt.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  Der *Anweisungen* Bildschirm am Ende von Schritt 3.
--%

Klicken Sie nun auf "OK", um das vollständige Design zu erzeugen. Die Tabelle von *block_loop* sollte jetzt wie %FigStep4 aussehen.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Die Tabelle von *block_loop* am Ende von Schritt 4.
--%

## Schritt 5: Erstellen Sie die Trial-Sequenz und fügen Sie ein Initialisierungsskript hinzu

Unsere Versuchssequenz soll wie folgt aussehen:

- Ein Fixationspunkt, für den wir ein SKETCHPAD verwenden.
- Eine Suchanzeige, die wir in JavaScript mit einem benutzerdefinierten INLINE_JAVASCRIPT erstellen.
- Antwort-Sammlung, für die wir ein KEYBOARD_RESPONSE verwenden.
- Datenprotokollierung, für die wir einen LOGGER verwenden.
- (Wir möchten auch sofortiges Feedback nach jedem Versuch, aber wir werden später darauf zurückkommen.)

Das einzige, was in *trial_sequence* noch fehlt, ist ein INLINE_JAVASCRIPT.

- Fügen Sie ein neues INLINE_JAVASCRIPT nach *sketchpad* ein und benennen Sie es in *search_display_script* um.
- Benennen Sie *sketchpad* in *fixation_dot* um, damit seine Funktion klar ist; und
- Ändern Sie die Dauer von *fixation_dot* auf 500, damit der Fixationspunkt für 500 ms angezeigt wird. (Es sollte bereits ein Fixationspunkt gezeichnet sein; wenn nicht, zeichnen Sie einen in die Mitte von *fixation_dot*.)

Wir müssen auch ein Initialisierungsskript zum Start des Experiments hinzufügen. Wir verwenden dies nur, um eine Variable (`let`) zu definieren, die das `Canvas`-Objekt, auf dem wir zeichnen, halten wird. In JavaScript müssen Sie eine Variable genau einmal definieren, weshalb wir dies in der *trial_sequence* nicht tun.

- Fügen Sie ein neues INLINE_JAVASCRIPT an der Spitze der *experiment_sequence* ein und benennen Sie es in *init* um.

Der Übersichtsbereich sollte jetzt wie %FigStep5 aussehen.

%--
Abbildung:
 id: FigStep5
 source: step5.png
 caption: |
  Der Übersichtsbereich am Ende von Schritt 5.
--%

## Schritt 6: Generieren Sie die Suchanzeige

__Top-Down und defensives Programmieren__

Jetzt wird es interessant: Wir werden mit JavaScript programmieren. Dabei werden wir zwei Leitprinzipien nutzen: *Top-Down* und *defensives* Programmieren.

- *Top-Down-Programmierung* bedeutet, dass wir mit der abstraktesten Logik beginnen, ohne uns um deren Implementierung zu kümmern. Sobald die abstrakteste Logik vorhanden ist, gehen wir zu einer etwas weniger abstrakten Logik über und so weiter, bis wir bei den Details der Implementierung ankommen. Diese Technik hilft, den Code strukturiert zu halten.
- *Defensives Programmieren* bedeutet, dass wir davon ausgehen, dass wir Fehler machen. Daher bauen wir zum Schutz vor uns selbst Sicherheitsprüfungen in den Code ein.

*Hinweis:* Die Erklärung unten setzt voraus, dass Sie mit JavaScript etwas vertraut sind. Wenn Ihnen Begriffe wie `Array`, `for`-Schleife und Funktionen nichts sagen, sollten Sie zuerst ein JavaScript-Einführungstutorial durcharbeiten. Links zu JavaScript-Tutorials finden Sie hier:

- %link:manual/javascript/about%

Die Logik des Codes wird in %FigHierarchy dargestellt. Die Zahlen zeigen die Reihenfolge an, in der wir die Funktionen implementieren, beginnend auf der abstrakten Ebene.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  Die Logik des Codes zum Zeichnen einer visuellen Suchanzeige.
--%

__Variablen mit let, var und const deklarieren__

In JavaScript müssen Sie eine Variable 'deklarieren', bevor Sie sie verwenden können. (In Python ist dies nicht erforderlich.) In unserem Fall werden wir eine Variable namens `c` verwenden, die wir daher deklarieren müssen. Öffnen Sie dazu die Registerkarte Vorbereiten des *init*-Skripts und verwenden Sie das Stichwort `let`, um die Variable `c` zu deklarieren:

```js
let c
```

Es gibt drei verschiedene Möglichkeiten, Variablen zu deklarieren:

- Mit `let`, wie wir es hier getan haben. In OpenSesame macht dies die Variable in JavaScript verfügbar, aber nicht als experimentelle Variable in der Benutzeroberfläche.
- Mit `var`. In OpenSesame macht dies die Variable auch als experimentelle Variable in der Benutzeroberfläche verfügbar. (Das werden wir später für die Variable `correct_response` tun.)
- Mit `const`. Dies ist wie `var` mit dem wichtigen Unterschied, dass die Variable später nicht neu zugewiesen werden kann.

__Die Prepare- und Run-Phasen__

Öffnen Sie *search_display_script* und wechseln Sie zur Registerkarte Vorbereiten. OpenSesame unterscheidet zwei Phasen der Ausführung:

- Während der Prepare-Phase hat jedes Item die Möglichkeit, sich vorzubereiten; was dies bedeutet, hängt vom Item ab: Bei einem SKETCHPAD bedeutet dies, eine Leinwand zu zeichnen (aber nicht zu zeigen); bei einem SAMPLER bedeutet dies, eine Tondatei zu laden (aber nicht abzuspielen); usw.
- Während der Run-Phase wird jedes Item tatsächlich ausgeführt; auch hier hängt die Bedeutung vom Item ab: Bei einem SKETCHPAD bedeutet dies, die zuvor vorbereitete Leinwand anzuzeigen; bei einem SAMPLER bedeutet dies, eine zuvor geladene Tondatei abzuspielen.

Für ein INLINE_JAVASCRIPT müssen Sie selbst entscheiden, was Sie in die Prepare-Phase und was Sie in die Run-Phase einfügen. Die Unterscheidung ist normalerweise ziemlich klar: In unserem Fall setzen wir den Code zum Zeichnen der Leinwand in die Prepare-Phase und den Code zum Anzeigen der Leinwand (der klein ist) in die Run-Phase.

Siehe auch:

- %link:prepare-run%

__Implementierung der abstrakten Ebene__

Wir beginnen auf der abstraktesten Ebene: Die Definition einer Funktion, die eine visuelle Suchanzeige zeichnet. Wir spezifizieren nicht *wie* dies geschieht; wir gehen einfach davon aus, dass es eine Funktion gibt, die dies tut, und werden uns später um die Details kümmern - das ist Top-Down-Programmierung.

Geben Sie im Reiter Vorbereiten den folgenden Code ein:

```js
c = draw_canvas()
```

Was passiert hier? Wir ...

- Rufen Sie `draw_canvas()` auf, das ein `Canvas`-Objekt zurückgibt, das wir als `c` speichern. Mit anderen Worten, `c` ist ein `Canvas`-Objekt, das der Suchanzeige entspricht. Dabei wird angenommen, dass es eine Funktion `draw_canvas()` gibt, obwohl wir sie bisher noch nicht definiert haben.

Ein `Canvas`-Objekt ist eine einzelne Anzeige; es ist gewissermaßen das JavaScript-Pendant zu einem SKETCHPAD. Siehe auch:

- %link:manual/javascript/canvas%

Jetzt gehen wir einen Schritt weiter, indem wir `draw_canvas()` definieren (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet das Such-Canvas.
 * @return Ein Canvas
 **/
function draw_canvas() {
    let c = Canvas()
    let xy_list = xy_random(set_size, 500, 500, 75)
    if (target_present === 'present') {
        let [x, y] = xy_list.pop()
        draw_target(c, x, y)
    } else if (target_present !== 'absent') {
        throw 'Ungültiger Wert für target_present ' + target_present
    }
    for (let [x, y] of xy_list) {
        draw_distractor(c, x, y)
    }
    return c
}
```


Was passiert hier? Wir …

- Erstellen Sie eine leere Leinwand, `c`, mit der Factory-Funktion `Canvas()`.
- Generiere ein Array von zufälligen `x,y`-Koordinaten, genannt `xy_list`, mit einer weiteren gängigen Funktion, `xy_random()`. Dieses Array bestimmt, wo die Reize angezeigt werden. Standorte werden aus einem 500 × 500 px Bereich mit einem Mindestabstand von 75 px entnommen.
- Überprüfe, ob die experimentelle Variable `target_present` den Wert 'present' hat; wenn ja, `pop()` ein `x,y`-Tupel aus `xy_list` und zeichne das Ziel an dieser Stelle. Dies setzt voraus, dass es eine Funktion `draw_target()` gibt, obwohl wir sie noch nicht definiert haben.
- Wenn `target_present` weder 'present' noch 'absent' ist, werfen wir einen Fehler; dies ist defensives Programmieren und schützt uns vor Tippfehlern (z.B. wenn wir versehentlich 'presenr' statt 'present' eingegeben hätten).
- Schleife durch alle verbleibenden `x, y` Werte und zeichne einen Distraktor an jeder Position. Dies setzt voraus, dass es eine Funktion `draw_distractor()` gibt, obwohl wir sie noch nicht definiert haben.
- Gib `c` zurück, das nun das Suchdisplay darauf gezeichnet hat.

Es gibt mehrere gängige Funktionen, wie `Canvas()` und `xy_random()`, die in einem INLINE_JAVASCRIPT-Element immer verfügbar sind. Siehe:

- %link:manual/javascript/common%

Experimentelle Variablen sind globale Variablen. Deshalb kannst du dich auf `set_size` beziehen, das in *block_loop* definiert ist, obwohl die Variable `set_size` im Skript nie explizit definiert wird. Das Gleiche gilt für `target_shape`, `target_color`, `condition` usw. Siehe:

- %link:var%


__Die Zwischenebene implementieren__

Wir definieren nun einen Schritt weiter `draw_target` (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet das Ziel.
 * @param c Eine Leinwand
 * @param x Eine x-Koordinate
 * @param y Eine y-Koordinate
 **/
function draw_target(c, x, y) {
    draw_shape(c, x, y, target_color, target_shape)
}
```

Was passiert hier? Wir …

- Rufen eine andere Funktion, `draw_shape()`, auf und geben die Farbe und Form an, die gezeichnet werden sollen. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

Wir definieren auch `draw_distractor` (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet einen einzelnen Distraktor.
 * @param c Eine Leinwand
 * @param x Eine x-Koordinate
 * @param y Eine y-Koordinate
 **/
function draw_distractor(c, x, y) {
    if (condition === 'conjunction') {
        draw_conjunction_distractor(c, x, y)
    } else if (condition === 'feature_shape') {
        draw_feature_shape_distractor(c, x, y)
    } else if (condition === 'feature_color') {
        draw_feature_color_distractor(c, x, y)
    } else {
        throw 'Ungültige Bedingung: ' + condition
    }
}
```

Was passiert hier? Wir ...

- Rufen eine andere Funktion auf, um einen spezifischeren Distraktor abhängig von der Bedingung zu zeichnen.
- Überprüfen, ob `condition` einen der erwarteten Werte hat. Wenn nicht, werfen wir einen Fehler. Dies ist defensives Programmieren! Ohne diese Überprüfung könnte es passieren, dass bei einem Tippfehler der Distraktor einfach nicht angezeigt wird, ohne eine Fehlermeldung auszulösen.

Nun definieren wir die Funktion, die Distraktoren in der Conjunction-Bedingung zeichnet (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet einen einzelnen Distraktor in der Conjunction-Bedingung: ein Objekt, das
 * jede Form und Farbe haben kann, jedoch nicht identisch mit dem Ziel sein darf.
 * @param c Eine Leinwand.
 * @param x Eine x-Koordinate.
 * @param y Eine y-Koordinate.
 **/
function draw_conjunction_distractor(c, x, y) {
    let conjunctions = [
        ['gelb', 'Kreis'],
        ['blau', 'Kreis'],
        ['gelb', 'Quadrat'],
        ['blau', 'Quadrat']
    ]
    let [color, shape] = random.pick(conjunctions)
    while (color === target_color && shape === target_shape) {
        [color, shape] = random.pick(conjunctions)
    }
    draw_shape(c, x, y, color, shape)
}
```

Was passiert hier? Wir …

- Definiere eine Liste `conjunctions` mit allen möglichen Farb- und Formkombinationen.
- Wähle zufällig eine der Farb- und Formkombinationen aus `conjunctions`.
- Überprüfe, ob die ausgewählte Farbe und Form beide gleich der Farbe und Form des Ziels sind. Wenn dies der Fall ist, wähle weiterhin eine neue Farbe und Form aus, bis dies nicht mehr der Fall ist. Schließlich darf der Distraktor nicht identisch mit dem Ziel sein!
- Rufe eine weitere Funktion namens `draw_shape()` auf und gib die Farbe und Form des zu zeichnenden Distraktors an. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

Außerdem verwenden wir ...

- Die `random`-Bibliothek, welche dem `random-ext`-Paket entspricht. Diese enthält nützliche Zufallsfunktionen (wie z. B. `random.pick()`) und ist eine der nicht standardmäßigen JavaScript-Bibliotheken, die mit OSWeb geliefert werden.

Nun definieren wir die Funktion, welche die Distraktoren in der Shape-Feature-Bedingung zeichnet (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet einen einzelnen Distraktor in der Feature-Form-Bedingung: ein Objekt, das
 * eine andere Form als das Ziel hat, aber jede beliebige Farbe haben kann.
 * @param c Eine Leinwand.
 * @param x Eine x-Koordinate.
 * @param y Eine y-Koordinate.
 **/
function draw_feature_shape_distractor(c, x, y) {
    let colors = ['yellow', 'blue']
    let color = random.pick(colors)
    let shape
    if (target_shape === 'circle') {
        shape = 'square'
    } else if (target_shape === 'square') {
        shape = 'circle'
    } else {
        throw 'Ungültige target_shape: ' + target_shape
    }
    draw_shape(c, x, y, color, shape)
}
```

Was passiert hier? Wir ...

- Wählen eine Farbe zufällig aus.
- Wählen eine quadratische Form, wenn das Ziel ein Kreis ist, und eine kreisförmige Form, wenn das Ziel ein Quadrat ist.
- Wenn `target_shape` weder 'circle' noch 'square' ist, löse einen Fehler aus - noch mehr Defensive Programmierung!
- Rufen Sie eine weitere Funktion, `draw_shape()` auf, und geben Sie die Farbe und die Form des zu zeichnenden Distraktors an. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

Jetzt definieren wir die Funktion, welche die Distraktoren in der Color-Feature-Bedingung zeichnet (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet einen einzelnen Distraktor in der Feature-Farben-Voraussetzung: ein Objekt, das
 * eine andere Farbe als das Ziel hat, aber jede beliebige Form haben kann.
 * @param c Eine Leinwand.
 * @param x Eine x-Koordinate.
 * @param y Eine y-Koordinate.
 **/
function draw_feature_color_distractor(c, x, y) {
    let shapes = ['circle', 'square']
    let shape = random.pick(shapes)
    let color
    if (target_color === 'yellow') {
        color = 'blue'
    } else if (target_color === 'blue') {
        color = 'yellow'
    } else {
        throw 'Ungültige target_color: ' + target_color
    }
    draw_shape(c, x, y, color, shape)
}
```

Was passiert hier? Wir ...

- Wählen zufällig eine Form aus.
- Wählen eine blaue Farbe, wenn das Ziel gelb ist, und eine gelbe Farbe, wenn das Ziel blau ist.
- Wenn `target_color` weder 'yellow' noch 'blue' ist, lösen Sie einen Fehler aus - noch mehr defensive Programmierung!
- Rufen Sie eine weitere Funktion, `draw_shape()` auf, und geben Sie die Farbe und die Form des zu zeichnenden Distraktors an. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

__Implementiere die detaillierte Ebene__

Jetzt gehen wir bis ins Detail und definieren die Funktion, welche eine Form tatsächlich auf die Leinwand zeichnet (oberhalb des bisherigen Skripts):

```js
/**
 * Zeichnet eine einzelne Form.
 * @param c Ein Canvas.
 * @param x Eine x-Koordinate.
 * @param y Eine y-Koordinate.
 * @param color Eine Farbe (gelb oder blau)
 * @param shape Eine Form (Quadrat oder Kreis)
 **/
function draw_shape(c, x, y, color, shape) {
    if (shape === 'square') {
        // Parameter werden als Objekt übergeben!
        c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
    } else if (shape === 'circle') {
        // Parameter werden als Objekt übergeben!
        c.circle({x:x, y:y, r:25, color:color, fill:true})
    } else {
        throw 'Ungültige Form: ' + shape
    }
    if (color !== 'yellow' && color !== 'blue') {
        throw 'Ungültige Farbe: ' + color
    }
}
```

Was passiert hier? Wir …

- Prüfen, welche Form gezeichnet werden soll. Für Quadrate fügen wir ein `rect()`-Element zur Leinwand hinzu. Für Kreise fügen wir ein `circle()`-Element hinzu.
- Prüfen, ob die Form entweder ein Quadrat oder ein Kreis ist, und wenn nicht, geben wir einen Fehler mit `throw` aus. Dies ist ein weiteres Beispiel für defensive Programmierung! Wir stellen sicher, dass wir nicht versehentlich eine ungültige Form angegeben haben.
- Prüfen, ob die Farbe weder gelb noch blau ist, und wenn nicht, geben wir einen Fehler mit `throw` aus.

Wichtig ist, dass `Canvas`-Funktionen ein einzelnes Objekt (`{}`) akzeptieren, das alle Parameter beim Namen angibt, so:

```js
// Richtig: Übergeben Sie ein einzelnes Objekt, das alle Parameter beim Namen enthält
c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
// Falsch: Übergeben Sie keine Parameter nach Reihenfolge
// c.rect(x-25, y-25, 50, 50, color, true)
// Falsch: benannte Parameter werden in JavaScript nicht unterstützt
// c.rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=true)
```

__Implementiere die Run-Phase__

Da wir in der Prepare-Phase bereits die schwierigen Aufgaben erledigt haben, besteht die Run-Phase einfach aus:

```js
c.show()
```

Das war's! Jetzt hast du ein vollständiges visuelles Such-Display gezeichnet. Und vor allem hast du dies auf eine leicht verständliche Art und Weise gemacht, dank der Top-Down-Programmierung, und sicher, dank der defensiven Programmierung.

## Schritt 7: Definiere die richtige Antwort

Um zu wissen, ob der Teilnehmer korrekt antwortet, müssen wir die richtige Antwort kennen. Du kannst dies explizit in der *block_loop* definieren (wie im Anfängertutorial); aber hier werden wir einfach etwas JavaScript verwenden, das überprüft, ob das Ziel vorhanden ist oder nicht, und die richtige Antwort entsprechend definiert.

Dazu müssen wir die Variable im Prepare-Tab des *init*-Skripts deklarieren, kurz unter `let c`. Diesmal verwenden wir das Schlüsselwort `var`, um `correct_response` zu deklarieren, da dies die Variable in der Benutzeroberfläche verfügbar macht (während `let` dies nicht tut):

```js
var correct_response
```

Füge anschließend ein neues INLINE_JAVASCRIPT am Anfang von *trial_sequence* ein und benenne es in *correct_response_script* um. In der Prepare-Phase gib den folgenden Code ein:

```js
if (target_present === 'present') {
    correct_response = 'right'
} else if (vars.target_present === 'absent') {
    correct_response = 'left'
} else {
- throw 'target_present sollte abwesend oder vorhanden sein, nicht ' + target
}
```

Was passiert hier? Wir …

- Prüfen, ob das Ziel vorhanden ist oder nicht. Wenn das Ziel vorhanden ist, ist die richtige Antwort 'right' (die rechte Pfeiltaste); wenn das Ziel fehlt, ist die korrekte Antwort 'left' (die linke Pfeiltaste). Die experimentelle Variable `correct_response` wird automatisch von OpenSesame verwendet; daher müssen wir nicht explizit angeben, dass diese Variable die richtige Antwort enthält.
- Prüfen, ob das Ziel entweder vorhanden oder abwesend ist, und wenn nicht, geben wir einen Fehler mit `throw` aus – ein weiteres Beispiel für defensive Programmierung.

## Schritt 8: Gib Rückmeldungen pro Versuch

Feedback nach jedem Versuch kann die Teilnehmer motivieren. Allerdings sollte das Feedback pro Versuch nicht den Fluss des Experiments stören. Eine gute Möglichkeit, Feedback pro Versuch zu geben, ist, kurz nach einer richtigen Antwort einen grünen Fixationspunkt und nach einer falschen Antwort einen roten Fixationspunkt anzuzeigen.

So geht's:

- Fügen Sie zwei neue SKETCHPADs in die *trial_sequence* ein, gleich nach *keyboard_response*.
- Benennen Sie ein SKETCHPAD in *green_dot* um, zeichnen Sie darauf einen grünen Fixierungspunkt in der Mitte und ändern Sie seine Dauer auf 500.
- Benennen Sie das andere SKETCHPAD in *red_dot* um, zeichnen Sie darauf einen roten Fixierungspunkt in der Mitte und ändern Sie seine Dauer auf 500.

Natürlich sollte in jedem Durchgang nur einer der beiden Punkte angezeigt werden. Um dies zu erreichen, werden wir run-if-Bedingungen in der *trial_sequence* festlegen:

- Ändern Sie die run-if-Bedingung für *green_dot* in 'correct == 1', was anzeigt, dass es nur nach einer korrekten Antwort gezeigt werden soll.
- Ändern Sie die run-if-Bedingung für *red_dot* in 'correct == 0', was anzeigt, dass es nur nach einer falschen Antwort gezeigt werden soll.

Die Variable `correct` wird automatisch erstellt, wenn die Variable `correct_response` verfügbar ist; deshalb haben wir `correct_response` in Schritt 7 definiert. Für weitere Informationen über Variablen und run-if-Bedingungen, siehe:

- %link:manual/variables%

Die *trial_sequence* sollte nun so aussehen wie in %FigStep8.

%--
Abbildung:
 id: FigStep8
 Quelle: step8.png
 Bildunterschrift: |
  Die *trial_sequence* am Ende von Schritt 8.
--%


## Fertig!

Herzlichen Glückwunsch, das Experiment ist vollständig! Sie können es testen, indem Sie auf die Schaltfläche in der Symbolleiste klicken, die einen grünen Kreis mit einem grauen Play-Button darin zeigt (Tastenkombination: `Alt+Ctrl+W`).

Wenn das Experiment beim ersten Versuch nicht funktioniert: Keine Sorge, und finden Sie ruhig heraus, wo der Fehler liegt. Abstürze gehören zum normalen Entwicklungsprozess. Aber Sie können sich viel Zeit und Ärger ersparen, indem Sie strukturiert arbeiten, wie wir es in diesem Tutorial getan haben.

## Referenzen

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Ein Open-Source, grafischer Experiment-Builder für die Sozialwissenschaften. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). Eine Integrations-Theorie der Aufmerksamkeit. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html