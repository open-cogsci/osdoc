title: Sona Systeme
hash: b16a73f1e8a3fb7fd7efb983a26825940c0de47ec814bf27280a22d31c398657
locale: de
language: German

[TOC]


## Über Sona Systems

Sona Systems ist ein Online-Tool, das viele Universitäten zur Rekrutierung von Teilnehmern, Gewährung von Studienkrediten für Studententeilnehmer usw. verwenden.

Siehe auch:

- <https://www.sona-systems.com/help/integration_test.aspx>


## Eine Studie auf JATOS erstellen

Zuerst importieren Sie Ihr Experiment in JATOS, wie oben beschrieben. Gehen Sie dann zum Worker & Batch Manager, aktivieren Sie den General Multiple Worker, klicken Sie auf Get Link und kopieren Sie die URL.


## Eine Studie auf Sona Systems erstellen

Erstellen Sie als Nächstes eine Studie auf Sona Systems. Fügen Sie die JATOS-Studien-URL in das Feld "Study URL" ein. Dies teilt Sona Systems mit, wie das Experiment gestartet werden soll. Wichtig ist, dass Sie dem URL am Ende folgendes hinzufügen (dies übermittelt die Sona-ID des Teilnehmers an Ihr Experiment):

```bash
&SONA_ID=%SURVEY_CODE%
```

Sona Systems verwendet keine Redirect URL. Dies bedeutet, dass Sona Systems nicht automatisch wissen wird, ob der Teilnehmer die Studie abgeschlossen hat oder nicht.


## Registrieren Sie die Sona ID in Ihrem Experiment

Jeder Teilnehmer von Sona wird durch eine eindeutige ID identifiziert. Es ist wichtig, diese ID in Ihrem Experiment zu protokollieren, da Sie so erkennen können, welcher Teilnehmer von Sona welchem Eintrag in den JATOS-Ergebnissen entspricht. Sie können dies tun, indem Sie das unten stehende Skript in der Vorbereitungsphase eines `inline_javascript`-Elements am Anfang Ihres Experiments hinzufügen.

Wenn das Experiment über Sona ausgeführt wird, steht die Sona ID als experimentelle Variable `sona_participant_id` zur Verfügung. Wenn das Experiment auf andere Weise ausgeführt wird (z.B. während des Tests), wird die Variable `sona_participant_id` auf -1 gesetzt.


```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Sona information is available')
    vars.sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Sona information is not available (setting value to -1)')
    vars.sona_participant_id = -1
}
console.log('sona_participant_id = ' + vars.sona_participant_id)
```


## Automatisches Gewähren von Credits bei Studienabschluss

Sona Systems bietet eine Abschluss-URL (clientseitig) an, die aufgerufen werden sollte, wenn eine Studie erfolgreich abgeschlossen ist, damit Sona Systems dem Teilnehmer Credits gewähren kann (siehe %FigCompletionURL).

%--
Abbildung:
 id: FigCompletionURL
 Quelle: completion-url.png
 Bildunterschrift: Die Abschluss-URL in den Studieninformationen von Sona Systems.
--%

Die Abschluss-URL (clientseitig) hat drei Argumente:

- `experiment_id`, die die Studie identifiziert und für alle Teilnehmer gleich ist
- `credit_token`, das (anscheinend) geändert wird, wenn Sie die Studieninformationen ändern, aber ansonsten für alle Teilnehmer gleich ist
- `survey_code`, das der Sona-Teilnehmer-ID entspricht und daher für jeden Teilnehmer unterschiedlich ist

Kopieren Sie die Abschluss-URL und ersetzen Sie die `XXX` durch `[SONA_ID]`. Gehen Sie zu den Studieneigenschaften auf JATOS und fügen Sie die resultierende URL in das Feld End Redirect URL ein.

%--
Abbildung:
 id: FigEndRedirectURL
 Quelle: end-redirect-url.png
 Bildunterschrift: Die End-Redirect-URL in den JATOS-Studieneigenschaften.
--%