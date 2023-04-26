title: Prolific
hash: ae0240db997107f3570b2cbf0d4576f801d25a57fbdd0a043e7f8be1bb82d715
locale: de
language: German

[TOC]


## Über Prolific

[Prolific](https://prolific.co/) ist ein kommerzielles Tool zur Rekrutierung von Teilnehmern für Forschungen. Um OSWeb-Experimente auf Prolific durchzuführen, müssen Sie den unten erklärten Schritten folgen.

Siehe auch:

- <http://www.jatos.org/Use-Prolific.html>


## Erstellen einer Studie auf JATOS

Zuerst importieren Sie Ihr Experiment in JATOS, wie oben beschrieben. Gehen Sie als Nächstes zum Worker & Batch Manager, aktivieren Sie den General Multiple Worker, klicken Sie auf Get Link, um eine URL zu erhalten, und kopieren Sie diese (%FigJatosURL).


%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: Erhalten einer Studien-URL von JATOS.
--%



## Erstellen einer Studie auf Prolific

Erstellen Sie als Nächstes eine Studie auf Prolific. Unter Studiendetails (%FigProlific) fügen Sie die JATOS-Studien-URL in das Feld mit der Bezeichnung "What is the URL of your study?" ein. Dies gibt Prolific an, wie das Experiment gestartet wird. Fügen Sie am Ende der URL Folgendes hinzu (dies gibt wichtige Informationen von Prolific an Ihr Experiment weiter):

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

Wenn das Experiment abgeschlossen ist, muss Prolific darüber informiert werden. Zu diesem Zweck verwendet Prolific ein End Redirect URL, das im Feld mit der Bezeichnung "To prove that participants have completed your study …" aufgeführt ist. Kopieren Sie diese End Redirect URL. Markieren Sie auch das Kästchen mit der Bezeichnung "I've set up my study to redirect to this url at the end".

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Studiendetails auf Prolific.
--%



## Festlegen einer End Redirect-URL in JATOS

Gehen Sie jetzt zurück zu JATOS und öffnen Sie die Eigenschaften Ihrer Studie (%FigJatosProperties). Fügen Sie dort die End Redirect-URL, die Sie von Prolific kopiert haben, in das Feld mit der Bezeichnung "End Redirect URL" ein. Dadurch wird JATOS mitgeteilt, dass der Teilnehmer nach Abschluss des Experiments auf Prolific zurückgeleitet werden soll, damit Prolific weiß, dass der Teilnehmer das Experiment abgeschlossen hat.

%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: Festlegen der End Redirect-URL in JATOS.
--%


## Registrieren von Prolific-Informationen in Ihrem Experiment

Jeder Teilnehmer von Prolific wird durch eine eindeutige ID identifiziert. Es ist wichtig, diese ID in Ihrem Experiment zu protokollieren, da Sie damit feststellen können, welcher Teilnehmer von Prolific welchem Eintrag in den JATOS-Ergebnissen entspricht. Sie können dies tun, indem Sie das unten stehende Skript in der Vorbereitungsphase eines `inline_javascript`-Elements am Anfang Ihres Experiments hinzufügen.

Wenn Sie das Experiment über Prolific ausführen, steht die Prolific-ID als experimentelle Variable `prolific_participant_id` zur Verfügung. Wenn Sie das Experiment auf eine andere Weise ausführen (z. B. während Tests), wird die Variable `prolific_participant_id` auf -1 gesetzt. Die gleiche Logik gilt für die Prolific Study ID (`prolific_study_id`) und die Prolific Session ID (`prolific_session_id`).

```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Prolific-Informationen sind verfügbar')
    vars.prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    vars.prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    vars.prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Prolific-Informationen sind nicht verfügbar (Werte auf -1 gesetzt)')
    vars.prolific_participant_id = -1
    vars.prolific_study_id = -1
    vars.prolific_session_id = -1
}
console.log('prolific_participant_id = ' + vars.prolific_participant_id)
console.log('prolific_study_id = ' + vars.prolific_study_id)
console.log('prolific_session_id = ' + vars.prolific_session_id)
```


## Testen der Studie

Gehen Sie zurück zur Studiendetails-Seite auf Prolific. Am unteren Ende der Seite befindet sich eine Vorschau-Schaltfläche. Damit können Sie das Experiment testen, indem Sie selbst als Teilnehmer agieren. Vergessen Sie nicht, die JATOS-Ergebnisse zu überprüfen, um sicherzustellen, dass das Experiment erfolgreich abgeschlossen wurde und dass alle notwendigen Informationen (einschließlich der Prolific-Informationen) protokolliert wurden!