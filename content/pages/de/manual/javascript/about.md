title: Über JavaScript
hash: 1a7fe7974b0f26b2ee7c29211c43267ef47dff0d720592d5fd82996550c56b07
locale: de
language: German

In OpenSesame können Sie komplexe Experimente allein über die grafische Benutzeroberfläche (GUI) erstellen. Aber manchmal stoßen Sie auf Situationen, in denen die Funktionalität der GUI nicht ausreicht. In diesen Fällen können Sie JavaScript-Code zu Ihrem Experiment hinzufügen.

JavaScript ist für Experimente gedacht, die in einem Browser mit OSWeb laufen. Wenn Sie Ihr Experiment auf dem Desktop ausführen müssen, sollten Sie [Python](%url:manual/python/about%) anstatt JavaScript verwenden.

__Versionshinweis:__ Die Desktopunterstützung für JavaScript wurde in OpenSesame 4.0 entfernt. Dies liegt daran, dass die JavaScript-Unterstützung auf dem Desktop unvollständig war und von den Benutzern als verwirrend empfunden wurde, ohne einen großen Mehrwert zu bieten.
{: .page-notification}

[TOC]

## JavaScript lernen

Es gibt viele JavaScript-Tutorials online. Eine gute Ressource ist Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript in der OpenSesame GUI


### Inline_javascript-Elemente

Um JavaScript-Code zu verwenden, müssen Sie ein Inline_javascript-Element zu Ihrem Experiment hinzufügen. Nachdem Sie dies getan haben, werden Sie etwas Ähnliches wie %FigInlineJavaScript sehen.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: Das Inline_javascript-Element.
--%

Wie Sie sehen können, besteht das Inline_javascript-Element aus zwei Tabs: einem für die Prepare-Phase und einem für die Run-Phase. Die Prepare-Phase wird zuerst ausgeführt, sodass die Elemente sich auf die zeitkritische Run-Phase vorbereiten können. Es ist eine gute Praxis, `Canvas`-Objekte während der Prepare-Phase zu erstellen, sodass sie ohne Verzögerung während der Run-Phase präsentiert werden können. Aber das ist nur eine Konvention; Sie können beliebigen JavaScript-Code während beider Phasen ausführen.

Für mehr Informationen über die Prepare-Run-Strategie, siehe:

- %link:prepare-run%


### Ausgabe in die Konsole drucken

Sie können mit dem Befehl `console.log()` in die Konsole drucken:

```js
console.log('Dies wird in der Konsole erscheinen!')
```

Wenn das Experiment auf dem Desktop läuft, erscheint die Ausgabe in der OpenSesame-Konsole (oder: Debug-Fenster). Wenn es in einem Browser läuft, erscheint die Ausgabe in der Browser-Konsole.


## Wissenswertes

### Häufige Funktionen

Viele häufig verwendete Funktionen stehen direkt in einem Inline_javascript-Element zur Verfügung. Zum Beispiel:

```js
// `Canvas()` ist eine Factory-Funktion, die ein `Canvas`-Objekt zurückgibt
let fixdotCanvas = Canvas()
if (sometimes()) {  // Manchmal ist der Fixpunkt grün
    fixdotCanvas.fixdot({color: 'green'})
} else {  // Manchmal ist er rot
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

Für eine Liste häufig verwendeter Funktionen, siehe:

- %link:manual/javascript/common%


### Variablen deklarieren (let und var)

Inline_javascript-Elemente werden im Non-Strict-Modus (oder: Sloppy-Modus) ausgeführt. Das bedeutet, dass Sie einer Variablen, die nicht explizit deklariert wurde, einen Wert zuweisen können. Wenn Sie das tun, wird die Variable implizit mit `var` deklariert, falls sie nicht bereits deklariert wurde.

```js
my_variable = 'mein Wert'  // implizit deklariert mit var
```

Variablen, die implizit oder explizit mit `var` deklariert werden, sind global, was hauptsächlich bedeutet, dass sie von einem Logger protokolliert werden können. Variablen, die mit `let` deklariert werden, sind nicht global, was hauptsächlich bedeutet, dass sie nicht von einem Logger protokolliert werden.

```js
this_is_a_global_variable = 'mein Wert'
var this_is_also_a_global_variable = 'mein Wert'
let this_is_not_a_global_variable = 'mein Wert'
```


### Das `persistent`-Objekt: Objekte über Skripte hinweg erhalten

__Versionshinweis__ Ab OSWeb 2.0 wird aller JavaScript-Code im selben Arbeitsbereich ausgeführt und Objekte werden daher über Skripte hinweg erhalten. Das bedeutet, dass Sie das `persistent`-Objekt nicht mehr benötigen.
{:.page-notification}

Jedes INLINE_JAVASCRIPT-Element wird in seinem eigenen Arbeitsbereich ausgeführt. Das bedeutet – und das ist anders als bei Python INLINE_SCRIPT-Elementen! –, dass Sie keine Variablen oder Funktionen verwenden können, die Sie in einem Skript deklariert haben, in einem anderen Skript. Um das Problem zu umgehen, können Sie Variablen oder Funktionen als Eigenschaften an das `persistent`-Objekt anhängen, das als Behälter für Dinge dient, die Sie zwischen Skripten erhalten möchten.

So können Sie ein `Canvas` in einem INLINE_JAVASCRIPT konstruieren ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

... und es in einem anderen INLINE_JAVASCRIPT anzeigen:

```js
persistent.myCanvas.show()
```


### Das `vars`-Objekt: Zugriff auf experimentelle Variablen

__Versionshinweis__ Ab OSWeb 2.0 sind alle experimentellen Variablen als Globale verfügbar. Das bedeutet, dass Sie das `vars`-Objekt nicht mehr benötigen.
{:.page-notification}

Sie können auf experimentelle Variablen über das `vars`-Objekt zugreifen:

```js
// OSWeb <= 1.4 (mit vars-Objekt)
// Eine experimentelle Variable erhalten
console.log('my_variable ist: ' + vars.my_variable)
// Eine experimentelle Variable setzen
vars.my_variable = 'my_value'

// OSWeb >= 2.0 (ohne vars-Objekt)
// Eine experimentelle Variable erhalten
console.log('my_variable ist: ' + my_variable)
// Eine experimentelle Variable setzen
my_variable = 'my_value'
```


### Das `pool`-Objekt: Zugriff auf den Dateipool

Sie greifen über das `pool`-Objekt auf 'Dateien' aus dem Dateipool zu. Die offensichtlichste Verwendung dafür ist das Parsen von CSV-Dateien, zum Beispiel mit experimentellen Bedingungen, aus dem Dateipool mit Hilfe der `csv-parse`-Bibliothek (weiter unten detaillierter beschrieben).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Sie können auch direkt Sounddateien aus dem Dateipool abspielen. Angenommen, im Dateipool befindet sich eine Datei namens `bark.ogg`, können Sie sie folgendermaßen abspielen:

```js
pool['bark.ogg'].data.play()
```


### Die `Canvas`-Klasse: Präsentation visueller Stimuli

Die `Canvas`-Klasse wird verwendet, um visuelle Stimuli zu präsentieren. Zum Beispiel können Sie so einen Fixationspunkt zeigen:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Einen vollständigen Überblick über die `Canvas`-Klasse finden Sie hier:

- %link:manual/javascript/canvas%

## Verfügbar JavaScript-Bibliotheken

Die folgenden JavaScript-Bibliotheken sind standardmäßig enthalten:

- [Zufallsfunktionen (`random-ext`)](%url:manual/javascript/random%)
- [Farbkonvertierungsfunktionen (`color-convert`)](%url:manual/javascript/color-convert%)
- [CSV-Funktionen (`csv-parse`)](%url:manual/javascript/csv%)
- [Python-artige Iteratoren (`pythonic`)](%url:manual/javascript/pythonic%)

Sie können zusätzliche JavaScript-Bibliotheken einbinden, indem Sie URLs zu den Bibliotheken im Feld 'Externe JavaScript-Bibliotheken' des OSWeb-Kontrollfelds eingeben.


## Debugging

Siehe:

- %link:debugging%