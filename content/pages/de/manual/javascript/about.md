title: Über JavaScript
hash: c3cfb549c6deb5d2a4f14b8681cb80f556bc41109c145df9574880d7eaa2399b
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

### Das `pool` Objekt: Zugriff auf den Datei-Pool

Sie greifen auf 'Dateien' aus dem Datei-Pool über das `pool` Objekt zu. Der offensichtlichste Gebrauch dafür ist das Parsen von CSV-Dateien, zum Beispiel mit experimentellen Bedingungen, aus dem Datei-Pool mit der `csv-parse` Bibliothek (weiter unten genauer beschrieben).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Sie können auch direkt Sounddateien aus dem Datei-Pool abspielen. Angenommen, es gibt eine Datei namens `bark.ogg` im Datei-Pool, können Sie sie folgendermaßen abspielen:

```js
pool['bark.ogg'].data.play()
```


### Die `Canvas` Klasse: Präsentation von visuellen Reizen

Die `Canvas` Klasse wird verwendet, um visuelle Reize zu präsentieren. Zum Beispiel können Sie einen Fixierungspunkt wie folgt anzeigen:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Eine vollständige Übersicht über die `Canvas` Klasse finden Sie hier:

- %link:manual/javascript/canvas%

## Verfügbar JavaScript-Bibliotheken

Die folgenden JavaScript-Bibliotheken sind standardmäßig enthalten:

- [Zufallsfunktionen (`random-ext`)](%url:manual/javascript/random%)
- [Farbkonvertierungsfunktionen (`color-convert`)](%url:manual/javascript/color-convert%)
- [CSV-Funktionen (`csv-parse`)](%url:manual/javascript/csv%)
- [Python-ähnliche Iteratoren (`pythonic`)](%url:manual/javascript/pythonic%)

Sie können zusätzliche JavaScript-Bibliotheken durch URLs zu den Bibliotheken im Feld 'Externe JavaScript-Bibliotheken' im OSWeb-Kontrollfeld einbinden.


## Debuggen

Siehe:

- %link:debugging%