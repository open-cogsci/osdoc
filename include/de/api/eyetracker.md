<div class="ClassDoc YAMLDoc" id="eyetracker" markdown="1">

# Klasse __eyetracker__

Eine generische Python-Bibliothek für Eye-Tracking.

<div class="FunctionDoc YAMLDoc" id="eyetracker-calibrate" markdown="1">

## Funktion __eyetracker\.calibrate__\(\)

Kalibriert das Eye-Tracking-System. Das tatsächliche Verhalten dieser
Funktion hängt von der Art des Eye-Trackers ab und ist unten beschrieben.

__EyeLink:__

Diese Funktion aktiviert den Kamera-Setup-Bildschirm, der es ermöglicht,
die Kamera einzustellen und ein Kalibrierungs-/Validierungsverfahren durchzuführen. Mit der Taste 'q' wird die Setup-Routine beendet. Das Drücken von "Entfernen" löst zunächst einen Bestätigungsdialog und dann, bei Bestätigung, eine Ausnahme aus.

__EyeTribe:__

Aktiviert eine einfache Kalibrierroutine.

__Returns:__

Gibt True zurück, wenn die Kalibrierung erfolgreich war, oder False, wenn nicht; zusätzlich wird ein Kalibrierungsprotokoll zur Protokolldatei hinzugefügt und einige Eigenschaften werden aktualisiert (z. B. die Schwellenwerte für die Erkennungsalgorithmen).

- Typ: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-close" markdown="1">

## Funktion __eyetracker\.close__\(\)

Schließt die Verbindung zum Tracker ordentlich. Speichert Daten und stellt
`self.connected` auf False.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-connected" markdown="1">

## Funktion __eyetracker\.connected__\(\)

Überprüft, ob der Tracker verbunden ist.

__Returns:__

True, wenn die Verbindung hergestellt ist, False, wenn nicht; stellt
`self.connected` auf denselben Wert.

- Typ: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_calibration_target" markdown="1">

## Funktion __eyetracker\.draw\_calibration\_target__\(x, y\)

Zeichnet ein Kalibrierungsziel.

__Arguments:__

- `x` -- Die X-Koordinate
	- Typ: int
- `y` -- Die Y-Koordinate
	- Typ: int

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_drift_correction_target" markdown="1">

## Funktion __eyetracker\.draw\_drift\_correction\_target__\(x, y\)

Zeichnet ein Driftkorrekturziel.

__Arguments:__

- `x` -- Die X-Koordinate
	- Typ: int
- `y` -- Die Y-Koordinate
	- Typ: int

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-drift_correction" markdown="1">

## Funktion __eyetracker\.drift\_correction__\(pos=None, fix\_triggered=False\)

Führt ein Driftkorrekturverfahren durch. Das genaue Verhalten dieser
Funktion hängt von der Art des Eye-Trackers ab und ist unten beschrieben. Da
die Driftkorrektur fehlschlagen kann, rufen Sie diese Funktion in der Regel
in einer Schleife auf.

__EyeLink:__

Während der Driftkorrektur wird mit der Taste 'q' der Kamera-Setup-Bildschirm aktiviert. Von dort aus verursacht das Drücken von 'q' erneut das sofortige Scheitern der Driftkorrektur. Das Drücken von "Entfernen" bietet die Möglichkeit, das Experiment abzubrechen, in diesem Fall wird eine Ausnahme ausgelöst.

__Keywords:__

- `pos` -- (x, y) Position des Fixationspunkts oder None für eine zentrale Fixation.
	- Typ: tuple, NoneType
	- Standard: None
- `fix_triggered` -- Boolescher Wert, der angibt, ob die Driftüberprüfung auf der Blickposition (True) oder auf dem Spacepress (False) basieren soll.
	- Typ: bool
	- Standard: False

__Returns:__

Ein Boolescher Wert, der angibt, ob die Driftüberprüfung in Ordnung ist (True) oder nicht (False).

- Typ: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-fix_triggered_drift_correction" markdown="1">

## Funktion __eyetracker\.fix\_triggered\_drift\_correction__\(pos=None, min\_samples=30, max\_dev=60, reset\_threshold=10\)

Führt eine Fixationsauslösung der Driftkorrektur durch, indem eine
bestimmte Anzahl von Proben gesammelt und die durchschnittliche Entfernung von der
Fixationsposition berechnet wird

__Keywords:__

- `pos` -- (x, y) Position des Fixationspunkts oder None für eine zentrale Fixation.
	- Typ: tuple, NoneType
	- Standard: None
- `min_samples` -- Die minimale Anzahl an Proben, nach denen eine durchschnittliche Abweichung berechnet wird.
	- Typ: int
	- Standard: 30
- `max_dev` -- Die maximale Abweichung von der Fixation in Pixeln.
	- Typ: int
	- Standard: 60
- `reset_threshold` -- Wenn der horizontale oder vertikale Abstand in Pixeln zwischen zwei aufeinanderfolgenden Proben größer als diese Schwelle ist, wird die Probensammlung zurückgesetzt.
	- Typ: int
	- Standard: 10

__Rückgabe:__

Ein Boolean, der angibt, ob die Driftprüfung in Ordnung ist (Wahr) oder nicht (Falsch).

- Typ: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-get_eyetracker_clock_async" markdown="1">

## Funktion __eyetracker\.get\_eyetracker\_clock\_async__\(\)

Gibt die Differenz zwischen Tracker-Zeit und PyGaze-Zeit zurück, die zur Synchronisation des Timings verwendet werden kann

__Rückgabe:__

Die Differenz zwischen Eyetracker-Zeit und PyGaze-Zeit.

- Typ: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log" markdown="1">

## Funktion __eyetracker\.log__\(msg\)

Schreibt eine Nachricht in die Protokolldatei.

__Argumente:__

- `msg` -- Eine Nachricht.
	- Typ: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log_var" markdown="1">

## Funktion __eyetracker\.log\_var__\(var, val\)

Schreibt den Namen und den Wert einer Variablen in die Protokolldatei

__Argumente:__

- `var` -- Ein Variablenname.
	- Typ: str, unicode
- `val` -- Ein Variablenwert

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-pupil_size" markdown="1">

## Funktion __eyetracker\.pupil\_size__\(\)

Gibt die neueste Pupillengrößenprobe zurück; die Größe kann je nach Einrichtung als Durchmesser oder Fläche der Pupille gemessen werden (beachten Sie, dass die Pupillengröße meist in willkürlichen Einheiten angegeben wird).

__Rückgabe:__

Gibt die Pupillengröße für das Auge zurück, das derzeit verfolgt wird (wie von self.eye_used angegeben) oder -1, wenn keine Daten abrufbar sind.

- Typ: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-sample" markdown="1">

## Funktion __eyetracker\.sample__\(\)

Gibt die neueste verfügbare Blickposition zurück.

__Rückgabe:__

Ein (x, y) Tupel oder ein (-1, -1) bei einem Fehler.

- Typ: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-send_command" markdown="1">

## Funktion __eyetracker\.send\_command__\(cmd\)

Sendet direkt einen Befehl an den Eyetracker (nicht für alle Marken unterstützt; kann eine Warnmeldung erzeugen, wenn Ihre Einrichtung direkte Befehle nicht unterstützt).

__Argumente:__

- `cmd` -- Der Befehl, der an den Eyetracker gesendet werden soll.
	- Typ: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_detection_type" markdown="1">

## Funktion __eyetracker\.set\_detection\_type__\(eventdetection\)

Setzt den Ereigniserkennungstyp entweder auf PyGaze-Algorithmen oder
native Algorithmen, wie sie vom Hersteller bereitgestellt werden (nur wenn
verfügbar: Erkennungstyp wird auf PyGaze zurückgesetzt, wenn keine nativen
Funktionen verfügbar sind)

__Argumente:__

- `eventdetection` -- Ein String, der angibt, welcher Erkennungstyp
verwendet werden soll: entweder 'pygaze' für
PyGaze Ereigniserkennungsalgorithmen oder
'native' für Algorithmen der Hersteller (nur
wenn verfügbar; wird auf 'pygaze' zurückgesetzt, wenn keine
native Ereigniserkennung verfügbar ist)
	- Typ: str, unicode

__Rückgabe:__

Erkennungstyp für Sakkaden, Fixationen und Blinzeln in einem Tupel, z.B. ('pygaze','native','native'), wenn 'native' übergeben wurde, aber native Erkennung für Sakkaden nicht verfügbar war.

- Typ: tuple

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_calibration_target_func" markdown="1">

## Funktion __eyetracker\.set\_draw\_calibration\_target\_func__\(func\)

Gibt eine benutzerdefinierte Funktion zum Zeichnen des Kalibrierungsziels an. Diese Funktion ersetzt das Standard [draw_calibration_target].

__Argumente:__

- `func` -- Die Funktion zum Zeichnen eines Kalibrierungsziels. Diese Funktion sollte zwei Parameter akzeptieren, für die x- und y-Koordinate des Ziels.
	- Typ: function

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_drift_correction_target_func" markdown="1">

## Funktion __eyetracker\.set\_draw\_drift\_correction\_target\_func__\(func\)

Gibt eine benutzerdefinierte Funktion zum Zeichnen des Driftkorrekturziels an. Diese Funktion ersetzt das Standard [draw_drift_correction_target].

__Argumente:__

- `func` -- Die Funktion zum Zeichnen eines Driftkorrekturziels. Diese Funktion sollte zwei Parameter akzeptieren, für die x- und y-Koordinate des Ziels.
	- Typ: function

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_eye_used" markdown="1">

## Funktion __eyetracker.set_eye_used__()

Protokolliert die `eye_used` Variable, basierend darauf, welches Auge angegeben wurde (wenn beide Augen verfolgt werden, wird das linke Auge verwendet). Gibt nichts zurück.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-start_recording" markdown="1">

## Funktion __eyetracker.start_recording__()

Beginnt die Aufnahme. Setzt `self.recording` auf `True`, wenn die Aufnahme erfolgreich gestartet wurde.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-status_msg" markdown="1">

## Funktion __eyetracker.status_msg__(msg)

Sendet eine Statusmeldung an den Eye-Tracker, die in der GUI des Trackers angezeigt wird (nur für EyeLink-Setups verfügbar).

__Argumente:__

- `msg` -- Ein String, der auf dem Versuchsleiter-PC angezeigt wird,
z.B.: "aktueller Versuch: %d" % trialnr.
	- Typ: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-stop_recording" markdown="1">

## Funktion __eyetracker.stop_recording__()

Stoppt die Aufnahme. Setzt `self.recording` auf `False`, wenn die Aufnahme erfolgreich gestoppt wurde.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_end" markdown="1">

## Funktion __eyetracker.wait_for_blink_end__()

Wartet auf das Ende eines Blinzelns und gibt die Zeit des Blinzel-Endes zurück.
Detektion basiert auf Dalmaijer et al. (2013), wenn EVENTDETECTION auf 'pygaze' gesetzt ist, oder mit nativen Detektionsfunktionen, wenn EVENTDETECTION auf 'native' gesetzt ist (HINWEIS: nicht jedes System hat native Funktionalität;
wird auf ;pygaze' zurückgreifen, wenn 'native' nicht verfügbar ist!)

__Rückgabe:__

Blink-Endzeit in Millisekunden, gemessen ab Experimentbeginn.

- Typ: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_start" markdown="1">

## Funktion __eyetracker.wait_for_blink_start__()

Wartet auf den Beginn eines Blinzelns und gibt die Zeit des Blinzel-Beginns zurück.
Detektion basiert auf Dalmaijer et al. (2013), wenn EVENTDETECTION auf 'pygaze' gesetzt ist, oder mit nativen Detektionsfunktionen, wenn EVENTDETECTION auf 'native' gesetzt ist (HINWEIS: nicht jedes System hat native Funktionalität;
wird auf ;pygaze' zurückgreifen, wenn 'native' nicht verfügbar ist!)

__Rückgabe:__

Blink-Startzeit in Millisekunden, gemessen ab Experimentbeginn

- Typ: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_event" markdown="1">

## Funktion __eyetracker.wait_for_event__(event)

Wartet auf ein Ereignis.

__Argumente:__

- `event` -- Ein ganzzahliger Event-Code, einer der folgenden:

- 3 = STARTBLINK
- 4 = ENDBLINK
- 5 = STARTSACC
- 6 = ENDSACC
- 7 = STARTFIX
- 8 = ENDFIX
	- Typ: int

__Rückgabe:__

Je nach angegebenem Ereignis wird eine `self.wait_for_*` Methode aufgerufen; der Rückgabewert der entsprechenden Methode wird zurückgegeben.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_end" markdown="1">

## Funktion __eyetracker.wait_for_fixation_end__()

Gibt Zeit und Blickposition zurück, wenn eine Fixierung beendet wurde;
Funktion geht davon aus, dass eine 'Fixierung' beendet wurde, wenn eine Abweichung
von mehr als self.pxfixtresh von der ursprünglichen Fixierungsposition erkannt wurde
(self.pxfixtresh wird in self.calibration erstellt, basierend auf self.fixtresh, einer Eigenschaft, die in self.__init__ definiert ist).
Detektion basiert auf Dalmaijer et al. (2013), wenn EVENTDETECTION auf 'pygaze' gesetzt ist, oder mit nativen Detektionsfunktionen, wenn EVENTDETECTION auf 'native' gesetzt ist (HINWEIS: nicht jedes System hat native Funktionalität;
wird auf ;pygaze' zurückgreifen, wenn 'native' nicht verfügbar ist!)

__Rückgabe:__

Ein `time, gazepos` Tupel. Time ist die Endzeit in Millisekunden (ab expstart), gazepos ist ein (x,y) Blickpositionstupel der Position, von der aus die Fixierung initiiert wurde.

- Typ: Tupel

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_start" markdown="1">

## Funktion __eyetracker.wait_for_fixation_start__()

Gibt Startzeit und Position zurück, wenn eine Fixierung beginnt;
Funktion geht davon aus, dass eine "Fixierung" beginnt, wenn die Blickposition
weitgehend stabil bleibt (d.h. wenn die meisten abweichenden Proben innerhalb von self.pxfixtresh liegen) für fünf Proben hintereinander (self.pxfixtresh
wird in self.calibration erstellt, basierend auf self.fixtresh, einer Eigenschaft
definiert in self.__init__).
Erkennung basiert auf Dalmaijer et al. (2013), wenn EVENTDETECTION auf
'pygaze' gesetzt ist, oder mit nativen Erkennungsfunktionen, wenn EVENTDETECTION
auf 'native' gesetzt ist (HINWEIS: Nicht jedes System hat native Funktionalität;
wird auf 'pygaze' zurückgreifen, wenn 'native' nicht verfügbar ist!)

__Gibt zurück:__

Ein `time, gazepos` Tupel. Die Zeit ist die Startzeit in Millisekunden (von expstart), gazepos ist ein (x,y) Blickpositionstupel der Position, von der die Fixierung initiiert wurde.

- Typ: Tupel

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_end" markdown="1">

## Funktion __eyetracker\.wait\_for\_saccade\_end__\(\)

Gibt Endzeit, Start- und Endposition zurück, wenn eine Sakkade endet; basiert auf Dalmaijer et al. (2013) Online-Sakkaden-Erkennungsalgorithmus, wenn EVENTDETECTION auf 'pygaze' gesetzt ist, oder mit nativen Erkennungsfunktionen, wenn EVENTDETECTION auf 'native' gesetzt ist (HINWEIS: Nicht jedes System hat native Funktionalität; wird auf 'pygaze' zurückgreifen, wenn 'native' nicht verfügbar ist!)

__Gibt zurück:__

Ein `endtime, startpos, endpos` Tupel. Endzeit in Millisekunden (von expbegintime); startpos und endpos sind (x,y) Blickpositionstupel.

- Typ: Tupel

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_start" markdown="1">

## Funktion __eyetracker\.wait\_for\_saccade\_start__\(\)

Gibt Startzeit und Startposition zurück, wenn eine Sakkade beginnt; basiert auf Dalmaijer et al. (2013) Online-Sakkaden-Erkennungsalgorithmus, wenn EVENTDETECTION auf 'pygaze' gesetzt ist, oder mit nativen Erkennungsfunktionen, wenn EVENTDETECTION auf 'native' gesetzt ist (HINWEIS: Nicht jedes System hat native Funktionalität; wird auf 'pygaze' zurückgreifen, wenn 'native' nicht verfügbar ist!)

__Gibt zurück:__

Ein `endtime, startpos` Tupel. Endzeit in Millisekunden (von expbegintime); startpos ist ein (x,y) Blickpositionstupel.

- Typ: Tupel

</div>

</div>