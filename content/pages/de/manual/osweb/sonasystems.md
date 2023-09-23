title: Sona Systeme
hash: d944a35b3e0c80d34ad14fc5152e628c6249312a06e28b86e5e6da4470fa60a2
locale: de
language: German

[TOC]

## Über Sona Systems

Sona Systems ist ein Online-Instrument, das viele Universitäten zur Rekrutierung von Teilnehmern, zur Gewährung von Studienkrediten für Studententeilnehmer usw. verwenden.

Siehe auch:

- <https://www.sona-systems.com/help/integration_test.aspx>


## Erstellen Sie eine Studie auf JATOS

Importieren Sie zunächst Ihr Experiment in JATOS, wie oben beschrieben. Gehen Sie als nächstes zum Worker & Batch Manager, aktivieren Sie den General Multiple Worker, erhalten Sie eine URL, indem Sie auf Get Link klicken, und kopieren Sie diese.


## Erstellen Sie eine Studie auf Sona Systems

Erstellen Sie als nächstes eine Studie auf Sona Systems. Fügen Sie die JATOS-Studie-URL in das Feld "Study URL" ein. Dies teilt Sona Systems mit, wie das Experiment gestartet werden soll. Fügen Sie wichtig das Folgende am Ende der URL hinzu (dies wird die Sona-ID des Teilnehmers an Ihr Experiment weitergeben):

```bash
?SONA_ID=%SURVEY_CODE% 
```

Sona Systems verwendet keine Redirect-URL. Das bedeutet, dass Sona Systems nicht automatisch wissen wird, ob der Teilnehmer die Studie abgeschlossen hat oder nicht.


## Registrieren Sie die Sona-ID in Ihrem Experiment

Jeder Teilnehmer von Sona wird durch eine eindeutige ID identifiziert. Es ist wichtig, diese ID in Ihrem Experiment zu protokollieren, da Sie so erkennen können, welcher Teilnehmer von Sona welchem Eintrag in den JATOS-Ergebnissen entspricht. Sie können dies tun, indem Sie das untenstehende Skript in der Prepare-Phase eines `inline_javascript` Elements ganz am Anfang Ihres Experiments hinzufügen.

Wenn das Experiment über Sona ausgeführt wird, wird die Sona-ID als experimentelle Variable `sona_participant_id` verfügbar sein. Wenn das Experiment auf andere Weise ausgeführt wird (z.B. während des Tests), wird die Variable `sona_participant_id` auf -1 gesetzt.


```javascript
if (window.jatos && jatos.urlQueryParameters.SONA_ID) {
    console.log('Sona information is available')
    var sona_participant_id = jatos.urlQueryParameters.SONA_ID
} else {
    console.log('Sona information is not available (setting value to -1)')
    var sona_participant_id = -1
}
console.log('sona_participant_id = ' + sona_participant_id)
```


## Automatisch Kredite bei Studienabschluss gewähren

Sona Systems bietet eine Abschluss-URL (clientseitig), die aufgerufen werden sollte, wenn eine Studie erfolgreich abgeschlossen wurde, damit Sona Systems dem Teilnehmer Kredite gewähren kann (siehe %FigCompletionURL).

%--
figure:
 id: FigCompletionURL
 source: completion-url.png
 caption: The completion URL in the Sona Systems study information.
--%

Die Abschluss-URL (clientseitig) hat darin drei Argumente:

- `experiment_id`, die die Studie identifiziert und für alle Teilnehmer gleich ist
- `credit_token`, der (anscheinend) ändert sich, wenn Sie die Studieninformationen ändern, ist aber sonst für alle Teilnehmer gleich
- `survey_code`, der der Sona-Teilnehmer-ID entspricht und daher für jeden Teilnehmer anders ist

Kopieren Sie die Abschluss-URL und ersetzen Sie die `XXX` durch `[SONA_ID]`. Gehen Sie zu den Studieneigenschaften auf JATOS und fügen Sie die resultierende URL in das Feld End Redirect URL ein.

%--
figure:
 id: FigEndRedirectURL
 source: end-redirect-url.png
 caption: The end-redirect URL in the JATOS study properties.
--%