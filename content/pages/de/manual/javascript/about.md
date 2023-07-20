title: Über JavaScript
hash: a7f9ce07f8ba8ef35658430e6e490db256a6c6c1681e7b791f85a4d8f288ae44
locale: de
language: German

In OpenSesame können Sie komplexe Experimente ausschließlich mit der grafischen Benutzeroberfläche (GUI) erstellen. Manchmal stoßen Sie jedoch auf Situationen, in denen die von der GUI bereitgestellte Funktionalität unzureichend ist. In diesen Fällen können Sie Ihrem Experiment JavaScript-Code hinzufügen.

JavaScript dient für Experimente, die in einem Browser mit OSWeb laufen. Wenn Sie Ihr Experiment auf dem Desktop ausführen müssen, müssen Sie anstelle von JavaScript [Python](%url:manual/python/about%) verwenden.

__Versionshinweis:__ Die Unterstützung für JavaScript auf dem Desktop wurde in OpenSesame 4.0 entfernt. Der Grund dafür ist, dass die JavaScript-Unterstützung auf dem Desktop unvollständig war und von den Benutzern als verwirrend empfunden wurde, ohne viel Nutzen zu bringen.
{: .page-notification}

[TOC]


## JavaScript lernen

Es gibt viele JavaScript-Tutorials online. Eine gute Ressource ist Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript in der OpenSesame GUI


### Inline_javascript Elemente

Um JavaScript-Code zu verwenden, müssen Sie ein INLINE_JAVASCRIPT-Element zu Ihrem Experiment hinzufügen. Nachdem Sie dies getan haben, wird Ihnen etwas wie %FigInlineJavaScript angezeigt.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: Das INLINE_JAVASCRIPT-Element.
--%

Wie Sie sehen können, besteht das INLINE_JAVASCRIPT-Element aus zwei Tabs: einem für die Vorbereitungsphase und einem für die Ausführungsphase. Die Vorbereitungsphase wird zuerst ausgeführt, um die Elemente auf die zeitkritische Ausführungsphase vorzubereiten. Es ist gute Praxis, `Canvas`-Objekte während der Vorbereitungsphase zu konstruieren, damit sie während der Ausführungsphase ohne Verzögerung präsentiert werden können. Dies ist jedoch nur eine Konvention; Sie können während beider Phasen beliebigen JavaScript-Code ausführen.

Für weitere Informationen zur Vorbereitungs-Ausführungs-Strategie, siehe:

- %link:prepare-run%


### Ausgabe auf die Konsole drucken

Sie können mit dem Befehl `console.log()` auf die Konsole drucken:

```js
console.log('Das wird in der Konsole angezeigt!')
```

Wenn Sie auf dem Desktop ausführen, erscheint die Ausgabe in der OpenSesame-Konsole (oder: Debug-Fenster). Bei der Ausführung in einem Browser erscheint die Ausgabe in der Konsolenausgabe des Browsers.


## Dinge, die Sie wissen sollten

### Typische Funktionen

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

Für eine Liste der gängigen Funktionen, siehe:

- %link:manual/javascript/common%


### Das `persistent`-Objekt: Objekte über Skripte hinweg bewahren

__Versionshinweis__ Ab OSWeb 2.0 wird der gesamte JavaScript-Code im selben Arbeitsbereich ausgeführt und Objekte werden daher über Skripte hinweg bewahrt. Dies bedeutet, dass Sie das `persistent`-Objekt nicht mehr benötigen.
{:.page-notification}

Jedes INLINE_JAVASCRIPT-Element wird in seinem eigenen Arbeitsbereich ausgeführt. Dies bedeutet - und das ist anders als bei Python INLINE_SCRIPT-Elementen! - dass Sie Variablen oder Funktionen, die Sie in einem Skript deklariert haben, nicht in einem anderen Skript verwenden können. Als Workaround können Sie Variablen oder Funktionen als Eigenschaften zum `persistent`-Objekt hinzufügen, das als Behälter für Dinge dient, die Sie über Skripte hinweg bewahren möchten.

Auf diese Weise können Sie ein `Canvas` in einem INLINE_JAVASCRIPT konstruieren...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

.. und es in einem anderen INLINE_JAVASCRIPT anzeigen:

```js
persistent.myCanvas.show()
```


### Das `vars`-Objekt: Zugriff auf experimentelle Variablen

__Versionshinweis__ Ab OSWeb 2.0 sind alle experimentellen Variablen als Globale verfügbar. Das bedeutet, dass Sie das `vars`-Objekt nicht mehr benötigen.
{:.page-notification}

Sie können auf experimentelle Variablen über das `vars`-Objekt zugreifen:

```js
// OSWeb <= 1.4 (mit vars-Objekt)
// Abrufen einer experimentellen Variable
console.log('my_variable ist: ' + vars.my_variable)
// Setzen einer experimentellen Variable
vars.my_variable = 'my_value'

// OSWeb >= 2.0 (ohne vars-Objekt)
// Abrufen einer experimentellen Variable
console.log('my_variable ist: ' + my_variable)
// Setzen einer experimentellen Variable
var my_variable = 'my_value'
```


### Das `pool`-Objekt: Zugriff auf den Dateipool

Sie greifen auf 'Dateien' aus dem Dateipool über das `pool`-Objekt zu. Am offensichtlichsten ist die Verwendung davon, um CSV-Dateien, z. B. mit experimentellen Bedingungen, mit der `csv-parse`-Bibliothek (unten näher beschrieben) aus dem Dateipool zu parsen.

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

Sie können auch Tondateien direkt aus dem Dateipool abspielen. Angenommen, es gibt eine Datei namens `bark.ogg` im Dateipool, können Sie sie wie folgt abspielen:

```js
pool['bark.ogg'].data.play()
```


### Die `Canvas`-Klasse: Präsentation von visuellen Reizen

Die `Canvas`-Klasse wird zur Präsentation von visuellen Reizen verwendet. Zum Beispiel können Sie einen Fixationspunkt wie folgt anzeigen:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

Eine vollständige Übersicht über die `Canvas`-Klasse finden Sie hier:

- %link:manual/javascript/canvas%

## Verfügbare JavaScript-Bibliotheken

Die folgenden JavaScript-Bibliotheken sind standardmäßig enthalten:

- [Random-Funktionen (`random-ext`)](%url:manual/javascript/random%)
- [Farbumwandlungsfunktionen (`color-convert`)](%url:manual/javascript/color-convert%)
- [CSV-Funktionen (`csv-parse`)](%url:manual/javascript/csv%)
- [Python-ähnliche Iteratoren (`pythonic`)](%url:manual/javascript/pythonic%)

Zusätzliche JavaScript-Bibliotheken können Sie durch Hinzufügen von URLs zu den Bibliotheken im Feld 'Externe JavaScript-Bibliotheken' des OSWeb-Kontrollfelds einfügen.


## Debugging

Siehe:

- %link:debugging%