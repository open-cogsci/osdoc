title: Über JavaScript
hash: b35489df1d7af79c088585c5b57e0661050203bbe5a62da2cd5449da48a08da6
locale: de
language: German

In OpenSesame können Sie komplexe Experimente mit der grafischen Benutzeroberfläche (GUI) erstellen. Manchmal stoßen Sie jedoch auf Situationen, in denen die Funktionen der GUI nicht ausreichen. In diesen Fällen können Sie JavaScript-Code zu Ihrem Experiment hinzufügen.

JavaScript ist für Experimente, die in einem Browser mit OSWeb laufen. Wenn Sie Ihr Experiment auf dem Desktop ausführen müssen, müssen Sie [Python](%url:manual/python/about%) anstelle von JavaScript verwenden.

__Hinweis zur Version:__ Die Desktop-Unterstützung für JavaScript wurde in OpeSesame 4.0 entfernt. Dies liegt daran, dass die JavaScript-Unterstützung auf dem Desktop unvollständig war und von Benutzern als verwirrend empfunden wurde, ohne viel Nutzen zu bieten.
{: .page-notification}

[TOC]


## JavaScript lernen

Es gibt viele JavaScript-Tutorials online. Eine gute Ressource ist Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript in der OpenSesame GUI


### Inline_javascript Elemente

Um JavaScript-Code zu verwenden, müssen Sie ein INLINE_JAVASCRIPT-Element zu Ihrem Experiment hinzufügen. Nachdem Sie dies getan haben, sehen Sie etwas wie %FigInlineJavaScript.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: Das INLINE_JAVASCRIPT Element.
--%

Wie Sie sehen können, besteht das INLINE_JAVASCRIPT Element aus zwei Registerkarten: einer für die Vorbereitungsphase und einer für die Laufphase. Die Vorbereitungsphase wird zuerst ausgeführt, damit die Elemente sich auf die zeitkritische Laufphase vorbereiten können. Es ist ratsam, `Canvas`-Objekte während der Vorbereitungsphase zu erstellen, damit sie während der Laufphase ohne Verzögerung präsentiert werden können. Dies ist jedoch nur Konvention; Sie können in beiden Phasen beliebigen JavaScript-Code ausführen.

Weitere Informationen zur Prepare-Run-Strategie finden Sie unter:

- %link:prepare-run%


### Ausgabe auf der Konsole ausgeben

Sie können mit dem `console.log()` Befehl auf der Konsole ausgeben:

```js
console.log('Das wird in der Konsole erscheinen!')
```

Bei Ausführung auf dem Desktop erscheint die Ausgabe in der OpenSesame-Konsole (oder: Debug-Fenster). Beim Ausführen in einem Browser erscheint die Ausgabe in der Browser-Konsole.


## Wissenswertes

### Häufig verwendete Funktionen

Viele gängige Funktionen sind direkt in einem INLINE_JAVASCRIPT-Element verfügbar. Zum Beispiel:

```js
// `Canvas()` ist eine Fabrikfunktion, die ein `Canvas`-Objekt zurückgibt
let fixdotCanvas = Canvas()
if (sometimes()) {  // Manchmal ist der Fixpunkt grün
    fixdotCanvas.fixdot({color: 'green'})
} else {  // Manchmal ist er rot
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

Für eine Liste häufig verwendeter Funktionen siehe:

- %link:manual/javascript/common%


### Das `persistent` Objekt: Objekte über Skripte hinweg erhalten

__Versionshinweis__ Ab OSWeb 2.0 wird gesamter JavaScript-Code im selben Arbeitsbereich ausgeführt und Objekte werden daher über Skripte hinweg erhalten. Dies bedeutet, dass Sie das `persistent`-Objekt nicht mehr benötigen.
{:.page-notification}

Jedes INLINE_JAVASCRIPT-Element wird in seinem eigenen Arbeitsbereich ausgeführt. Das bedeutet - und das unterscheidet sich von Python INLINE_SCRIPT-Elementen! - dass Sie in einem anderen Skript keine Variablen oder Funktionen verwenden können, die Sie in einem Skript deklariert haben. Als Workaround können Sie Variablen oder Funktionen als Eigenschaften an das `persistent`-Objekt anhängen, das als Behälter für Dinge dient, die Sie über Skripte hinweg erhalten möchten.

Auf diese Weise können Sie in einem INLINE_JAVASCRIPT ein `Canvas` erstellen...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

..und in einem anderen INLINE_JAVASCRIPT anzeigen:

```js
persistent.myCanvas.show()
```


### Das `vars` Objekt: Zugriff auf experimentelle Variablen

__Versionshinweis__ Ab OSWeb 2.0 sind alle experimentellen Variablen als global verfügbar. Dies bedeutet, dass Sie das `vars`-Objekt nicht mehr benötigen.
{:.page-notification}

Sie können über das `vars`-Objekt auf experimentelle Variablen zugreifen:

```js
// Eine experimentelle Variable abrufen
console.log('meine_variable ist: ' + vars.my_variable)
// Eine experimentelle Variable festlegen
vars.my_variable = 'mein_wert'
```

### Das `pool`-Objekt: Zugriff auf den Datei-Pool

Du greifst auf 'Dateien' im Datei-Pool über das `pool`-Objekt zu. Am offensichtlichsten ist die Verwendung, um CSV-Dateien, zum Beispiel mit experimentellen Bedingungen, aus dem Datei-Pool mithilfe der `csv-parse`-Bibliothek (weiter unten ausführlicher beschrieben) zu parsen.

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Du kannst auch Tondateien direkt aus dem Datei-Pool abspielen. Angenommen, es gibt eine Datei namens `bark.ogg` im Datei-Pool, kannst du sie wie folgt abspielen:

```js
pool['bark.ogg'].data.play()
```


### Die `Canvas`-Klasse: Visuelle Reize präsentieren

Die `Canvas`-Klasse wird verwendet, um visuelle Reize zu präsentieren. Du kannst zum Beispiel einen Fixationspunkt wie folgt anzeigen:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Eine vollständige Übersicht über die `Canvas`-Klasse findest du hier:

- %link:manual/javascript/canvas%


## Verfügbare JavaScript-Bibliotheken

Mehrere praktische JavaScript-Bibliotheken sind mit OSWeb gebündelt.


### random-ext: erweiterte Zufallsgenerierung

Die `random-ext`-Bibliothek ist als `random` verfügbar. Diese Bibliothek bietet viele praktische, höherwertige Funktionen für die Zufallsgenerierung.

__Beispiel:__

Zeichne acht Kreise mit einer zufälligen Farbe und einer Position, die zufällig aus einem 5x5-Raster ausgewählt wird:

```js
let positions = xy_grid(5, 50)
positions = random.subArray(positions, 8)
const cnv = Canvas()
cnv.fixdot()
for (const [x, y] of positions) {
    cnv.circle({x: x, y: y, r: 20, fill: true, color: random.color()})
}
cnv.show()
```

Für eine Übersicht, siehe:

- <https://www.npmjs.com/package/random-ext>


### pythonic: Python-ähnliche Funktionen zum Durchlaufen von Arrays

Die `pythonic`-Bibliothek bietet Python-ähnliche Funktionen zum Durchlaufen von Arrays. Verfügbare Funktionen sind: `range()`, `enumerate()`, `items()`, `zip()` und `zipLongest()`.

__Beispiel:__

Zeichne ein 5x5-Raster mit ansteigenden Zahlen:

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

Für eine Übersicht, siehe:

- <https://www.npmjs.com/package/pythonic>


### color-convert: Farbumwandlungs-Utility

Die `color-convert`-Bibliothek ist als `convert` verfügbar. Sie bietet praktische High-Level-Funktionen für die Umwandlung von einer Farbspezifikation in eine andere.

__Beispiel:__

```js
console.log('Die RGB-Werte für Blau sind ' + convert.keyword.rgb('blue'))
```

Für eine Übersicht, siehe:

- <https://www.npmjs.com/package/color-convert>


### csv-parse: CSV-formatierten Text in ein Objekt umwandeln

Die synchronen `parse()`-Funktion aus der `csv-parse`-Bibliothek ist verfügbar. Damit kannst du CSV-formatierten Text, zum Beispiel aus einer CSV-Datei im Datei-Pool, in ein Objekt umwandeln.

__Beispiel:__

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Für eine Übersicht, siehe:

- <https://csv.js.org/parse/api/sync/#sync-api>


## Debugging

Die meisten modernen Browser, insbesondere Chrome und Firefox, verfügen über einen leistungsstarken integrierten Debugger. Du kannst den Debugger aktivieren, indem du eine Zeile hinzufügst, die einfach `debugger` in dein Skript aussagt (%FigDebuggerInlineJavaScript).

%--
abbildung:
 id: FigDebuggerInlineJavaScript
 source: debugger-inline-javascript.png
 caption: Aktivierung des Debuggers aus einem INLINE_JAVASCRIPT-Element.
--%


Starte dann das Experiment und zeige den Debugger (oder: Entwicklertools in Chrome, oder: Web-Entwickler-Tools in Firefox) an, sobald der OSWeb-Startbildschirm erscheint. Der Debugger hält dann das Experiment an, wenn er auf die `debugger`-Anweisung trifft. An diesem Punkt kannst du die Konsole verwenden, um mit dem JavaScript-Arbeitsbereich zu interagieren, oder du kannst Variablen mit dem Scope-Tool untersuchen (%FigDebuggerChrome).

%--
Abbildung:
 ID: FigDebuggerChrome
 Quelle: debugger-chrome.png
Beschriftung: Inspektion des Variablenbereichs in Chrome.
--%

Siehe auch:

- %link:manual/osweb/osweb%