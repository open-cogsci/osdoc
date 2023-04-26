title: Intermediäres Tutorial (Python) visuelle Suche
hash: bc6a941f73aa734c08871ddf1fd8ffcd188aed4dde8ec8200b599a033ffa1de4
locale: de
language: German

[TOC]

## Über OpenSesame

OpenSesame ist ein benutzerfreundliches Programm für die Entwicklung von Verhaltensexperimenten für Psychologie, Neurowissenschaften und experimentelle Wirtschaft. Für Anfänger bietet OpenSesame eine umfassende grafische, Point-and-Click-Schnittstelle. Für fortgeschrittene Benutzer unterstützt OpenSesame Python (nur Desktop) und JavaScript (Desktop und Browser).

OpenSesame ist unter der [General Public License v3][gpl] frei verfügbar.

## Über dieses Tutorial

In diesem Tutorial wird gezeigt, wie man mit OpenSesame ein grundlegendes visuelles Suchexperiment erstellt [(Mathôt, Schreij, & Theeuwes, 2012)][references]. Wir werden sowohl die grafische Schnittstelle als auch Python-Skripting verwenden, um ein Experiment zu entwickeln, das auf dem Desktop in einem traditionellen Laborsetting durchgeführt werden kann. Erfahrungen mit OpenSesame und Python sind empfehlenswert. Dieses Tutorial dauert etwa eine Stunde.

Eine JavaScript-basierte Version dieses Tutorials ist ebenfalls verfügbar. Wenn Sie Ihre Experimente online in einem Browser (mit OSWeb) durchführen möchten, ist das JavaScript-Tutorial das Richtige für Sie:

- %link:tutorials/intermediate-javascript%

## Ressourcen

- __Download__ — Dieses Tutorial setzt voraus, dass Sie mindestens Version 4.0.0 von OpenSesame verwenden. Sie können die neueste Version von OpenSesame herunterladen unter:
	- %link:download%
- __Dokumentation__ — Eine spezielle Dokumentationswebsite finden Sie unter:
	- <http://osdoc.cogsci.nl/>
- __Forum__ — Ein Supportforum finden Sie unter:
	- <http://forum.cogsci.nl/>

## Das Experiment

In diesem Tutorial erstellen Sie ein grundlegendes visuelles Suchexperiment. Das Experiment ähnelt den klassischen visuellen Suchstudien von [Treisman und Gelade (1980)][references], ist aber nicht identisch.

In diesem Experiment suchen die Teilnehmer nach einem Zielobjekt, das ein gelbes Quadrat, ein gelber Kreis, ein blaues Quadrat oder ein blauer Kreis sein kann; die Identität des Ziels variiert zwischen den Blöcken von Versuchen. Die Teilnehmer geben an, ob das Ziel vorhanden ist oder nicht, indem sie die rechte (vorhanden) oder linke (nicht vorhanden) Pfeiltaste drücken.

Zusätzlich zum Ziel werden null oder mehr Ablenkungsobjekte angezeigt. Es gibt drei Bedingungen, und die Bedingung bestimmt, welche Art von Ablenkern es gibt:

- In der *Konjunktions*-Bedingung können Ablenker jede Form und Farbe haben, mit der einzigen Einschränkung, dass Ablenker nicht identisch mit dem Ziel sein dürfen. Wenn das Ziel also beispielsweise ein gelbes Quadrat ist, dann sind die Ablenker gelbe Kreise, blaue Kreise und blaue Quadrate.
- In der *Shape-Feature*-Bedingung haben Ablenker eine andere Form als das Ziel, können aber jede Farbe haben. Wenn das Ziel also beispielsweise ein gelbes Quadrat ist, dann sind die Ablenker gelbe Kreise und blaue Kreise.
- In der *Color-Feature*-Bedingung können Ablenker jede Form haben, haben aber eine andere Farbe als das Ziel. Wenn das Ziel also beispielsweise ein gelbes Quadrat ist, dann sind die Ablenker blaue Quadrate und blaue Kreise.

Unmittelbares Feedback wird nach jedem Versuch angezeigt: ein grüner Punkt nach einer korrekten Antwort und ein roter Punkt nach einer falschen Antwort. Detailliertes Feedback über durchschnittliche Reaktionszeiten und Genauigkeit wird nach jedem Block von Versuchen angezeigt.

%--
Abbildung:
 id: FigVisualSearch
 Quelle: visual-search.svg
 Bildunterschrift: |
  Das visuelle Suchexperiment, das Sie in diesem Tutorial implementieren werden.
--%

Experimente wie dieses zeigen zwei typische Ergebnisse:

- Es dauert länger, das Ziel in der Konjunktionsbedingung zu finden als in den zwei Feature-Bedingungen.
- In der Konjunktionsbedingung nehmen die Reaktionszeiten zu, je mehr Ablenker es gibt. Das deutet darauf hin, dass Menschen das Ziel objektweise suchen; dies wird als *serielle Suche* bezeichnet.
- In den Feature-Bedingungen (sowohl Form als auch Farbe) nehmen die Reaktionszeiten nicht oder kaum zu, je mehr Ablenker es gibt. Das deutet darauf hin, dass die Menschen das gesamte Display auf einmal verarbeiten; dies wird als *parallele Suche* bezeichnet.

Laut Treismans und Gelades Merkmalsintegrations-Theorie spiegeln diese Ergebnisse wider, dass die Bedingung "Verbindung" erfordert, dass Sie Farbe und Form jedes Objekts kombinieren oder *binden*. Diese Bindung erfordert Aufmerksamkeit, und Sie müssen daher Ihre Aufmerksamkeit von einem Objekt zum nächsten verschieben; das ist langsam und erklärt, warum die Reaktionszeiten von der Anzahl der Objekte abhängen. Im Gegensatz dazu müssen in den Merkmalsbedingungen Farbe und Form nicht gebunden werden, und daher kann das gesamte Display in einem einzigen Durchgang verarbeitet werden, ohne dass die Aufmerksamkeit auf jedes einzelne Objekt gerichtet wird.

## Versuchsaufbau

Dieser Aufbau:

- Ist *innerhalb der Teilnehmergruppe*, weil alle Teilnehmer alle Bedingungen durchlaufen
- Ist *vollständig gekreuzt* (oder vollfaktoriell), weil alle Kombinationen von Bedingungen auftreten
- Hat drei Bedingungen (oder Faktoren):
	- Innerhalb der Blöcke variiert:
		- `set_size` mit drei Stufen (1, 5, 15), oder SS<sub>3</sub>
		- `condition` mit drei Stufen (Verbindung, Merkmal_Form, Merkmal_Farbe), oder CN<sub>3</sub>
		- `target_present` mit zwei Stufen (vorhanden, nicht vorhanden), oder TP<sub>2</sub>
	- Zwischen den Blöcken variiert:
		- `target_shape` mit zwei Stufen (Quadrat, Kreis), oder TS<sub>2</sub>
		- `target_color` mit zwei Stufen (Gelb, Blau), oder TC<sub>2</sub>
- Hat N Probanden, oder <u>S</u><sub>N</sub>

Sie können diesen Versuchsaufbau als <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub> schreiben

Für weitere Informationen zu dieser Notation für Versuchsaufbauten siehe:

- %link:experimentaldesign%

## Schritt 1: Die grundlegende Struktur des Experiments erstellen

Öffnen Sie OpenSesame und wählen Sie auf der Registerkarte "Los geht's!" die erweiterte Vorlage. Diese Vorlage bietet die grundlegende Struktur, die vielen kognitiv-psychologischen Experimenten gemeinsam ist, wie dem, das wir hier erstellen werden.

Die erweiterte Vorlage enthält einige Elemente, die wir nicht benötigen. Löschen Sie die folgenden Elemente:

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Wenn Sie diese Elemente gelöscht haben, sind sie noch im Bereich "Nicht verwendete Elemente" sichtbar. Um diese Elemente dauerhaft zu löschen, klicken Sie auf den Bereich "Nicht verwendete Elemente" und dann auf die Schaltfläche "Nicht verwendete Elemente dauerhaft löschen".

Geben Sie dem Experiment abschließend einen guten Titel, zum Beispiel "Visuelle Suche". Öffnen Sie dazu die Registerkarte "Allgemeine Eigenschaften" (indem Sie im Anzeigebereich auf "Erweiterte Vorlage" klicken) und klicken Sie auf den Experimentnamen, um ihn zu bearbeiten.

Der Anzeigebereich sollte nun aussehen wie in %FigStep1:

%--
Abbildung:
 Id: FigStep1
 Quelle: step1.png
 Bildunterschrift: |
  Der Anzeigebereich am Ende von Schritt 1.
--%

## Schritt 2: Experimentelle Variablen definieren, die zwischen Blöcken variieren

Wie oben beschrieben, variieren in unserem Experiment zwei Variablen zwischen den Blöcken: `target_shape` und `target_color`. Daher müssen wir diese Variablen in der *experimental_loop* definieren. Um zu verstehen, warum, betrachten Sie die Struktur, die in %FigStep1 gezeigt wird, beginnend von der untersten Ebene (d. h. die am weitesten eingerückte Ebene).

- *trial_sequence* entspricht einem einzelnen Versuch
- *block_loop* entspricht einem Block von Versuchen
	- Variablen, die hier definiert werden, variieren für jeden Durchlauf von *trial_sequence*; mit anderen Worten, Variablen, die in *block_loop* definiert werden, werden __innerhalb von Blöcken__ variiert.
- *block_sequence* entspricht einem Block von Versuchen, vorangestellt von einem Zurücksetzen der Feedback-Variablen und gefolgt von Teilnehmer-Feedback
- *experimental_loop* entspricht mehreren Blöcken von Versuchen
	- Variablen, die hier definiert werden, variieren für jeden Durchlauf von *block_sequence*; mit anderen Worten, Variablen, die in *experimental_loop* definiert werden, werden __zwischen Blöcken__ variiert.
- *experiment* entspricht dem gesamten Experiment, das aus einem Anweisungsbildschirm besteht, gefolgt von mehreren Blöcken von Versuchen und einem Bildschirm zum Ende des Experiments

Klicken Sie auf die experimentelle Schleife und definieren Sie:

- `target_shape`, die entweder "Quadrat" oder "Kreis" sein kann; und
- `target_color`, die entweder "Gelb" oder "Blau" sein kann.

Wir haben ein vollfaktorielles Design, was bedeutet, dass alle 2 × 2 = 4 Kombinationen auftreten müssen. Die Tabelle von *experimental_loop* sollte jetzt wie %FigStep2 aussehen:

%--
Abbildung:
 ID: FigStep2
 Quelle: step2.png
 Bildunterschrift: |
  Die Tabelle von *experimental_loop* am Ende von Schritt 2.
--%

## Schritt 3: Anweisungen zu Beginn jedes Blocks geben

Im Moment beginnt das Experiment mit einem einzelnen *instructions* Bildschirm. In unserem Fall möchten wir vor jedem Block von Versuchsleitern Anweisungen geben, um dem Teilnehmer mitzuteilen, wonach er suchen soll (da sich die Identität des Ziels zwischen den Blöcken unterscheidet).

__Anweisungen in block_sequence verschieben__

Heben Sie dazu den *instructions* Artikel auf und ziehen Sie ihn auf *block_sequence*. Ein Popup-Fenster wird angezeigt und fragt Sie, ob Sie:

- Den Artikel in *block_sequence* einfügen möchten, in diesem Fall würde *instructions* das erste Element von *block_sequence*; oder
- Den Artikel nach *block_sequence* einfügen möchten, in diesem Fall würde *instructions* an einer Position nach *block_sequence* verschoben werden.

Wählen Sie die erste Option ("Einfügen in"). Jetzt beginnt *block_sequence* mit einem Anweisungsbildschirm, das ist, was wir wollen.

__Anleitungstext hinzufügen__

Klicken Sie auf *instructions*, um es zu öffnen, und fügen Sie einen guten Anleitungstext hinzu, wie zum Beispiel:

```text
ANWEISUNGEN

Suche nach dem {target_color} {target_shape}

Drücke die rechte Pfeiltaste, wenn du es gefunden hast
Drücke die linke Pfeiltaste, wenn du es nicht gefunden hast

Drücke eine beliebige Taste, um zu beginnen
```

Die geschweiften Klammern um "{target_color}" und "{target_shape}" zeigen an, dass dies kein wörtlicher Text ist, sondern sich auf die Variablen bezieht, die wir in *experimental_loop* definiert haben. Wenn das Experiment läuft, erscheinen hier die Werte dieser Variablen, und der Teilnehmer sieht (zum Beispiel) "Suche nach dem gelben Kreis".

__Ein visuelle Vorschau des Ziels geben__

Es ist auch gut, dem Teilnehmer den tatsächlichen Stimulus zu zeigen, den er finden muss. Gehen Sie dazu wie folgt vor:

- Zeichnen Sie einen gefüllten Kreis in der Mitte der Anzeige (achten Sie darauf, dass er nicht mit dem Text überlappt);
- Ändern Sie die Farbe des Kreises in "{target_color}". Dies bedeutet, dass die Farbe des Kreises von dem Wert der Variable `target_color` abhängt; und
- Ändern Sie den show-if-Ausdruck in `target_shape == 'circle'`. Dies ist ein Python-Ausdruck, der überprüft, ob die Variable `target_shape` den Wert "circle" hat.

Mit anderen Worten, wir haben einen Kreis gezeichnet, dessen Farbe von `target_color` bestimmt wird; außerdem wird dieser Kreis nur angezeigt, wenn die Variable `target_shape` den Wert "circle" hat. Weitere Informationen zu Variablen und Show-if-Anweisungen finden Sie unter:

- %link:manual/variables%

Wir verwenden den gleichen Trick, um ein Quadrat zu zeichnen:

- Zeichnen Sie ein gefülltes Quadrat in der Mitte der Anzeige;
- Ändern Sie die Farbe des Quadrats in "{target_color}"; und
- Ändern Sie die Show-if-Anweisung in `target_shape == 'square'`

Der *instructions* Bildschirm sollte jetzt wie %FigStep3 aussehen:

%--
Abbildung:
 ID: FigStep3
 Quelle: step3.png
 Bildunterschrift: |
  Der *instructions* Bildschirm am Ende von Schritt 3.
--%

## Schritt 4: Experimentelle Variablen definieren, die innerhalb der Blöcke variieren

Drei Variablen variieren innerhalb der Blöcke in unserem Experiment: `condition`, `set_size` und `target_present`. Wie in Schritt 2 beschrieben, müssen wir diese Variablen in der *block_loop* definieren, damit sie bei jedem Durchlauf von *trial_sequence* variieren.

Die drei Variablen ergeben insgesamt 3 × 3 × 2 = 18 verschiedene Kombinationen. Wir können diese manuell in die Tabelle eingeben, aber da wir ein vollfaktorielles Design haben, können wir auch den Vollfaktorielles-Design-Assistenten verwenden. Um dies zu tun, öffnen Sie zuerst *block_loop* und klicken Sie auf die Schaltfläche "Vollfaktorielles Design".

Geben Sie in der angezeigten Tabelle die Variablennamen in der ersten Zeile und die Werte in den Zeilen darunter ein, wie in %FigFullFactorial gezeigt.

%--
Abbildung:
 ID: FigFullFactorial
 Quelle: fullfactorial.png
 Bildunterschrift: |
  Der *instructions* Bildschirm am Ende von Schritt 3.
--%

Klicken Sie nun auf "Ok", um das vollständige Design zu generieren. Die Tabelle von *block_loop* sollte jetzt wie %FigStep4 aussehen.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  Die Tabelle des *block_loop* am Ende von Schritt 4.
--%

## Schritt 5: Erstellen Sie die Versuchsabfolge

Unsere Versuchsabfolge soll wie folgt aussehen:

- Ein Fixationspunkt, für den wir ein SKETCHPAD verwenden.
- Eine Suchanzeige, die wir in Python mit einem benutzerdefinierten INLINE_SCRIPT erstellen.
- Antworterfassung, für die wir eine KEYBOARD_RESPONSE verwenden.
- Datenaufzeichnung, für die wir einen LOGGER verwenden.
- (Wir wollen auch sofortiges Feedback nach jedem Versuch, aber dazu kommen wir später.)

Das Einzige, was fehlt, ist ein INLINE_SCRIPT.

- Fügen Sie ein neues INLINE_SCRIPT nach *sketchpad* ein und benennen Sie es in *search_display_script* um.
- Benennen Sie *sketchpad* in *fixation_dot* um, damit seine Funktion klar ist; und
- Ändern Sie die Dauer von *fixation_dot* auf 500, damit der Fixationspunkt 500 ms lang angezeigt wird. (Ein Fixationspunkt sollte bereits gezeichnet sein; falls nicht, zeichnen Sie einen in der Mitte des *fixation_dot*.)

Der Übersichtsbereich sollte jetzt wie %FigStep5 aussehen.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  Der Übersichtsbereich am Ende von Schritt 5.
--%

## Schritt 6: Erstellen Sie die Suchanzeige

__Top-down und defensive Programmierung__

Jetzt wird es interessant: Wir beginnen mit der Programmierung in Python. Wir verwenden zwei grundlegende Prinzipien: *Top-down* und *defensive* Programmierung.

- *Top-down-Programmierung* bedeutet, dass wir mit der abstraktesten Logik beginnen, ohne uns darum zu kümmern, wie diese Logik implementiert wird. Sobald die abstrakteste Logik vorhanden ist, gehen wir zu einer etwas weniger abstrakten Logik über und so weiter, bis wir bei den Details der Implementierung ankommen. Diese Technik hilft, den Code strukturiert zu halten.
- *Defensive Programmierung* bedeutet, dass wir davon ausgehen, dass wir Fehler machen. Um uns vor uns selbst zu schützen, bauen wir Sicherheitsprüfungen in den Code ein.

*Hinweis:* Die folgende Erklärung setzt voraus, dass Sie mit Python-Code vertraut sind. Wenn Ihnen Begriffe wie `list`, `tuple` und Funktionen nichts sagen, sollten Sie zunächst ein Einführungstutorial zu Python durchlaufen, wie etwa:

- <https://pythontutorials.eu/>

Die Logik des Codes wird in %FigHierarchy gezeigt. Die Zahlen geben die Reihenfolge an, in der wir die Funktionalitäten implementieren, beginnend mit der abstrakten Ebene.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  Die Logik des Codes, um eine visuelle Suchanzeige zu zeichnen.
--%

__Die Prepare- und Run-Phase__

Öffnen Sie *search_display_script* und wechseln Sie zur Registerkarte Prepare. OpenSesame unterscheidet zwei Phasen der Ausführung:

- Während der Prepare-Phase hat jedes Element die Möglichkeit, sich selbst vorzubereiten; was das bedeutet, hängt von dem Element ab: Bei einem SKETCHPAD bedeutet es, eine Leinwand (aber nicht zeigen) zu zeichnen; bei einem SAMPLER bedeutet es, eine Sounddatei (aber nicht abspielen) zu laden; usw.
- Während der Run-Phase wird jedes Element tatsächlich ausgeführt; wieder hängt dies vom Element ab: Bei einem SKETCHPAD bedeutet das, die zuvor vorbereitete Leinwand zu zeigen; bei einem SAMPLER bedeutet es, eine zuvor geladene Sounddatei abzuspielen.

Für ein INLINE_SCRIPT müssen Sie selbst entscheiden, was Sie in der Prepare-Phase und was Sie in der Run-Phase platzieren möchten. Die Unterscheidung ist normalerweise ziemlich klar: In unserem Fall setzen wir den Code zum Zeichnen der Leinwand in die Prepare-Phase und den Code zum Anzeigen der Leinwand (der klein ist) in die Run-Phase.

Mehr dazu finden Sie hier:

- %link:prepare-run%

__Implementierung der abstrakten Ebene__

Wir beginnen mit der abstraktesten Ebene: Definieren einer Funktion, die eine visuelle Suchanzeige zeichnet. Wir geben nicht an, *wie* das geschieht; wir gehen einfach davon aus, dass es eine Funktion gibt, die das tut, und wir kümmern uns später um die Details - das ist Top-down-Programmierung.

Geben Sie in der Registerkarte Prepare folgenden Code ein:

~~~ .python
c = draw_canvas()
~~~

Was passiert hier? Wir …

- Rufe `draw_canvas()` auf, das ein `Canvas`-Objekt zurückgibt, das wir als `c` speichern; mit anderen Worten, `c` ist ein `Canvas`-Objekt, das der Suchanzeige entspricht. Dies setzt voraus, dass es eine Funktion `draw_canvas()` gibt, obwohl wir sie noch nicht definiert haben.

Ein `Canvas`-Objekt ist eine einzelne Anzeige; es ist in gewisser Weise das Python-Pendant zu einem SKETCHPAD. Siehe auch:

- %link:manual/python/canvas%

Wir gehen nun einen Schritt weiter, indem wir `draw_canvas()` (über dem Rest des bisherigen Skripts) definieren:

~~~ .python
def draw_canvas():
    """Zeichnet die Suchanzeige.

    Gibt zurück
    -------
    Canvas
    """
    c = Canvas()
    xy_list = xy_random(n=set_size, width=500, height=500, min_dist=75)
    if target_present == 'present':
        x, y = xy_list.pop()
        draw_target(c, x, y)
    elif target_present != 'absent':
        raise Exception(f'Ungültiger Wert für target_present: {target_present}')
    for x, y in xy_list:
        draw_distractor(c, x, y)
    return c
~~~

Was passiert hier? Wir …

- Erstellen eine leere Leinwand, `c`, mit der Factory-Funktion `Canvas()`.
- Generieren eine Liste von zufälligen `x, y`-Koordinaten, genannt `xy_list`, mit einer weiteren häufigen Funktion, `xy_random()`. Diese Liste bestimmt, wo die Reize gezeigt werden.
- Überprüfen, ob die experimentelle Variable `target_present` den Wert 'präsent' hat; wenn ja, `pop()` ein `x, y`-Tupel aus `xy_list` und zeichnen das Ziel an dieser Position. Dies setzt voraus, dass es eine Funktion `draw_target()` gibt, obwohl wir sie noch nicht definiert haben.
- Wenn `target_present` weder 'präsent' noch 'abwesend' ist, erheben wir eine `Exception`; dies ist defensives Programmieren und schützt uns vor Tippfehlern (z. B. wenn wir versehentlich 'presenr' statt 'present' eingegeben hätten).
- Schleifen Sie durch alle verbleibenden `x, y`-Tupel und zeichnen Sie an jeder Position einen Distraktor. Dies setzt voraus, dass es eine Funktion `draw_distractor()` gibt, obwohl wir sie noch nicht definiert haben.
- Gib `c` zurück, das nun die Suchanzeige darauf gezeichnet hat.

Es gibt mehrere häufig verwendete Funktionen, wie `Canvas()` und `xy_random()`, die immer verfügbar sind. Siehe:

- %link:manual/python/common%

Experimentelle Variablen sind globale Variablen. Deshalb können Sie auf `set_size` verweisen, das in *block_loop* definiert ist, obwohl die Variable `set_size` im Skript niemals explizit definiert ist. Das Gleiche gilt für `target_shape`, `target_color`, `condition` usw. Siehe:

- %link:var%

__Implementierung der Zwischenebene__

Wir gehen nun einen weiteren Schritt, indem wir `draw_target` definieren (über dem Rest des bisherigen Skripts):

~~~ .python
def draw_target(c, x, y):
    """Zeichnet das Ziel.

    Parameter
    ----------
    c: Canvas
    x: int
    y: int
    """
    draw_shape(c, x, y, color=target_color, shape=target_shape)
~~~

Was passiert hier? Wir …

- Rufen eine weitere Funktion, `draw_shape()`, auf und geben die Farbe und Form an, die gezeichnet werden sollen. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

Wir definieren auch `draw_distractor` (über dem Rest des bisherigen Skripts):

~~~ .python
def draw_distractor(c, x, y):
    """Zeichnet einen einzelnen Distraktor.

    Parameter
    ----------
    c: Canvas
    x: int
    y: int
    """
    if condition == 'conjunction':
        draw_conjunction_distractor(c, x, y)
    elif condition == 'feature_shape':
        draw_feature_shape_distractor(c, x, y)
    elif condition == 'feature_color':
        draw_feature_color_distractor(c, x, y)
    else:
        raise Exception(f'Ungültige Bedingung: {condition}')
~~~

Was passiert hier? Wir …

- Rufen eine andere Funktion auf, um einen spezifischeren Distraktor abhängig von der Bedingung zu zeichnen.
- Überprüfen, ob `condition` einen der erwarteten Werte hat. Wenn nicht, erheben wir eine `Exception`. Dies ist defensives Programmieren! Ohne diese Überprüfung könnte es passieren, dass ein Distraktor aufgrund eines Tippfehlers einfach nicht angezeigt wird, ohne dass eine Fehlermeldung angezeigt wird.

Nun definieren wir die Funktion, die Distraktoren in der Conjunction-Bedingung zeichnet (über dem Rest des bisherigen Skripts):

~~~ .python
import random

def draw_conjunction_distractor(c, x, y):
    """Zeichnet einen einzelnen Ablenker in der Verbindungskondition: ein Objekt, das
    jede Form und Farbe annehmen kann, aber nicht identisch mit dem Ziel sein darf.

    Parameter
    ----------
    c: Leinwand
    x: int
    y: int
    """
    verbindungen = [('gelb', 'kreis'),
                    ('blau',   'kreis'),
                    ('gelb', 'quadrat'),
                    ('blau',   'quadrat')]
    verbindungen.remove((target_color, target_shape))
    farbe, form = random.choice(verbindungen)
    draw_shape(c, x, y, color=farbe, shape=form)
~~~

Was passiert hier? Wir …

- Definieren eine Liste `verbindungen` mit allen möglichen Kombinationen von Farbe und Form.
- Entfernen das Ziel aus dieser Liste; das ist notwendig, weil der Ablenker nicht identisch mit dem Ziel sein darf.
- Wählen zufällig eine der Farb- und Formkombinationen aus `verbindungen`.
- Rufen eine andere Funktion `draw_shape()` auf und geben die Farbe und Form des zu zeichnenden Ablenkers an. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

Außerdem fügen wir …

- die Zeile `import random` am Anfang des Skripts hinzu. Das ist notwendig, damit wir Funktionen verwenden können, die Teil des `random`-Moduls sind, wie zum Beispiel `random.choice()`.

Jetzt definieren wir die Funktion, die Ablenker in der Shape Feature-Bedingung zeichnet (direkt unterhalb der `import`-Anweisung):

~~~ .python
def draw_feature_shape_distractor(c, x, y):
    """Zeichnet einen einzelnen Ablenker in der Feature-Shape-Bedingung: Ein Objekt, das
    eine andere Form als das Ziel hat, aber jede Farbe haben kann.

    Parameter
    ----------
    c: Leinwand
    x: int
    y: int
    """
    farben = ['gelb', 'blau']
    farbe = random.choice(farben)
    if target_shape == 'circle':
        form = 'square'
    elif target_shape == 'square':
        form = 'circle'
    else:
        raise Exception(f'Ungültige Ziel-Form: {target_shape}')
    draw_shape(c, x, y, color=farbe, shape=form)
~~~

Was passiert hier? Wir …

- Wählen zufällig eine Farbe
- Wählen eine quadratische Form, wenn das Ziel ein Kreis ist, oder eine runde Form, wenn das Ziel ein Quadrat ist.
- Wenn `target_shape` weder 'circle' noch 'square' ist, erzeuge eine `Exception`—mehr defensive Programmierung!
- Rufen die Funktion `draw_shape()` auf und geben die Farbe und Form des zu zeichnenden Ablenkers an. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

Jetzt definieren wir die Funktion, die Ablenker im Color Feature-Zustand zeichnet (gleich unterhalb der `import`-Anweisung):

~~~ .python
def draw_feature_color_distractor(c, x, y):
    """Zeichnet einen einzelnen Ablenker in der Feature-Farbe-Kondition: Ein Objekt, das
    eine andere Farbe als das Ziel hat, aber jede Form haben kann.

    Parameter
    ----------
    c: Leinwand
    x: int
    y: int
    """
    formen = ['circle', 'square']
    form = random.choice(formen)
    if target_color == 'yellow':
        farbe = 'blue'
    elif target_color == 'blue':
        farbe = 'yellow'
    else:
        raise Exception(f'Ungültige Ziel-Farbe: {target_color}')
    draw_shape(c, x, y, color=farbe, shape=form)
~~~

Was passiert hier? Wir …

- Wählen zufällig eine Form.
- Wählen eine blaue Farbe, wenn das Ziel gelb ist, und eine gelbe Farbe, wenn das Ziel blau ist.
- Wenn `target_color` weder 'yellow' noch 'blue' ist, erzeuge eine `Exception`—mehr defensive Programmierung!
- Rufen die Funktion `draw_shape()` auf und geben die Farbe und Form des zu zeichnenden Ablenkers an. Dies setzt voraus, dass es eine Funktion `draw_shape()` gibt, obwohl wir sie noch nicht definiert haben.

__Implementieren Sie das detaillierte Level__

Jetzt gehen wir bis ins Detail, indem wir die Funktion definieren, die tatsächlich eine Form auf die Leinwand zeichnet (direkt unterhalb der `import`-Anweisung):

~~~ .python
def draw_shape(c, x, y, color, shape):
    """Zeichnet eine einzige Form.

    Parameter
    ----------
    c: Leinwand
    x: int
    y: int
    color: str
    shape: str
    """
    if shape == 'quadrat':
        c += Rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=True)
    elif shape == 'kreis':
        c += Circle(x=x, y=y, r=25, color=color, fill=True)
    else:
        raise Exception(f'Ungültige Form: {shape}')
    if color not in ['gelb', 'blau']:
        raise Exception(f'Ungültige Farbe: {color}')
~~~

Was passiert hier? Wir ...

- Überprüfen, welche Form gezeichnet werden soll. Für Quadrate fügen wir ein `Rect()` Element zur Leinwand hinzu. Für Kreise fügen wir ein `Circle()` Element hinzu.
- Überprüfen, ob die Form entweder ein Quadrat oder ein Kreis ist, und falls nicht, geben wir eine `Exception` aus. Dies ist ein weiteres Beispiel für defensives Programmieren! Wir stellen sicher, dass wir nicht versehentlich eine ungültige Form angegeben haben.
- Überprüfen, ob die Farbe weder gelb noch blau ist, und falls nicht, geben wir eine `Exception` aus.

__Implementiere die Run Phase__

Da wir die ganze Arbeit in der Vorbereitungsphase erledigt haben, besteht die Run-Phase nur aus:

~~~ .python
c.show()
~~~

Das war's! Jetzt haben Sie eine vollständige visuelle Suchanzeige gezeichnet. Und was noch wichtiger ist, Sie haben dies auf eine Weise getan, die leicht verständlich ist, aufgrund des Top-Down-Programmierungsansatzes, und sicher, aufgrund des defensiven Programmierens.


## Schritt 7: Die richtige Antwort definieren

Um zu wissen, ob der Teilnehmer korrekt antwortet, müssen wir die richtige Antwort kennen. Sie können dies explizit in der *block_loop* definieren (wie im Anfänger-Tutorial gemacht); aber hier werden wir ein einfaches Python-Skript verwenden, das überprüft, ob das Ziel vorhanden ist oder nicht, und die richtige Antwort entsprechend definiert.

Fügen Sie dazu ein neues INLINE_SCRIPT am Anfang von *trial_sequence* ein und benennen Sie es in *correct_response_script* um. Geben Sie in der Vorbereitungsphase (nicht in der Run-Phase!) den folgenden Code ein:

~~~ .python
if target_present == 'present':
    correct_response = 'right'
elif target_present == 'absent':
    correct_response = 'left'
else:
    raise Exception(f'target_present sollte absent oder present sein, nicht {target}')
~~~

Was passiert hier? Wir ...

- Überprüfen, ob das Ziel vorhanden ist oder nicht. Wenn das Ziel vorhanden ist, ist die richtige Antwort 'right' (die rechte Pfeiltaste); wenn das Ziel nicht vorhanden ist, ist die korrekte Antwort 'left' (die linke Pfeiltaste). Die experimentelle (globale) Variable `correct_response` wird automatisch von *keyboard_response* erkannt; Daher müssen wir nicht explizit angeben, dass diese Variable die richtige Antwort enthält.
- Überprüfen, ob das Ziel entweder vorhanden oder abwesend ist, und falls nicht, eine `Exception` ausgeben - ein weiteres Beispiel für defensives Programmieren.

## Schritt 8: Per-Trial-Feedback geben

Feedback nach jedem Versuch kann die Teilnehmer motivieren; Allerdings sollte das per-trial-Feedback den Ablauf des Experiments nicht beeinträchtigen. Eine gute Möglichkeit, per-trial-Feedback zu geben, besteht darin, nach einer korrekten Antwort kurz einen grünen Fixpunkt und nach einer falschen Antwort einen roten Fixpunkt anzuzeigen.

Um dies zu tun:

- Fügen Sie zwei neue SKETCHPADs in *trial_sequence* ein, direkt nach *keyboard_response*.
- Benennen Sie ein SKETCHPAD in *green_dot* um, zeichnen Sie einen zentralen grünen Fixpunkt darauf und ändern Sie dessen Dauer auf 500.
- Benennen Sie das andere SKETCHPAD in *red_dot* um, zeichnen Sie einen zentralen roten Fixpunkt darauf und ändern Sie dessen Dauer auf 500.

Natürlich sollte auf jedem Versuch nur einer der beiden Punkte gezeigt werden. Um dies zu erreichen, werden wir in *trial_sequence* run-if Ausdrücke angeben:

- Ändern Sie den run-if Ausdruck für *green_dot* in 'correct == 1', um anzuzeigen, dass es nur nach einer richtigen Antwort angezeigt werden sollte.
- Ändern Sie den run-if Ausdruck für *red_dot* in 'correct == 0', um anzuzeigen, dass es nur nach einer falschen Antwort angezeigt werden sollte.

Die Variable `correct` wird automatisch erstellt, wenn die Variable `correct_response` verfügbar ist; Darum haben wir `correct_response` in Schritt 7 definiert. Weitere Informationen zu Variablen und run-if-Aussagen finden Sie unter:

- %link:manual/variables%

Die *trial_sequence* sollte nun aussehen wie %FigStep8.

%--
Abbildung:
  Id: FigStep8
  Quelle: step8.png
  Beschriftung: |
   Die *trial_sequence* am Ende von Schritt 8.
--%

## Fertig!

Herzlichen Glückwunsch, das Experiment ist abgeschlossen! Sie können einen Testlauf starten, indem Sie auf den blauen Doppelpfeil-Button klicken (Tastenkombination: `Strg+W`).

Wenn das Experiment beim ersten Versuch nicht funktioniert: Keine Sorge, und finden Sie in Ruhe heraus, wo der Fehler herkommt. Abstürze gehören zum normalen Entwicklungsprozess. Aber Sie können sich viel Zeit und Kopfschmerzen ersparen, indem Sie in einer strukturierten Weise arbeiten, wie wir es in diesem Tutorial getan haben.

## Referenzen

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Eine Open-Source-, grafische Experimentbaukasten für die Sozialwissenschaften. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). Eine Feature-Integrationstheorie der Aufmerksamkeit. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[referenzen]: #referenzen
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html