title: Prolific
hash: fd3ba787ea541676148e558d0e902641c2b9f9eb848745aff73e95c443e9fc56
locale: de
language: German

[TOC]


## Über Prolific

[Prolific](https://prolific.co/) ist ein kommerzielles Tool zur Rekrutierung von Teilnehmern für die Forschung. Um OSWeb-Experimente auf Prolific durchzuführen, müssen Sie die unten erklärten Schritte befolgen.

Siehe auch:

- <http://www.jatos.org/Use-Prolific.html>


## Erstellen Sie eine Studie auf JATOS

Importieren Sie zunächst Ihr Experiment in JATOS, wie oben beschrieben. Gehen Sie dann zum Worker & Batch Manager, aktivieren Sie den General Multiple Worker, holen Sie sich eine URL, indem Sie auf Get Link klicken, und kopieren Sie diese (%FigJatosURL).


%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: Holen Sie sich eine Studien-URL von JATOS.
--%



## Erstellen Sie eine Studie auf Prolific

Erstellen Sie als Nächstes eine Studie auf Prolific. Unter Studiendetails (%FigProlific) fügen Sie die JATOS-Studien-URL in das Feld "What is the URL of your study?" ein. Dies sagt Prolific, wie das Experiment gestartet werden soll. Fügen Sie am Ende der URL das Folgende hinzu (dadurch werden wichtige Informationen von Prolific an Ihr Experiment weitergegeben):

{% raw %}
```bash
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```
{% endraw %}

Wenn das Experiment abgeschlossen ist, muss Prolific darüber informiert werden. Zu diesem Zweck verwendet Prolific eine End Redirect URL, die im Feld "Um zu beweisen, dass Teilnehmer Ihre Studie abgeschlossen haben ..." aufgeführt ist. Kopieren Sie diese End Redirect URL. Überprüfen Sie auch das Kästchen "Ich habe meine Studie so eingerichtet, dass sie am Ende auf diese URL umleitet".

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Studiendetails auf Prolific.
--%



## Legen Sie eine End Redirect URL in JATOS fest

Gehen Sie jetzt zurück zu JATOS und öffnen Sie die Eigenschaften Ihrer Studie (%FigJatosProperties). Dort fügen Sie die End Redirect URL ein, die Sie von Prolific kopiert haben, in das Feld "End Redirect URL". Dies zeigt JATOS an, dass der Teilnehmer am Ende des Experiments zu Prolific zurückgeleitet werden soll, damit Prolific weiß, dass der Teilnehmer das Experiment abgeschlossen hat.


%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: Legen Sie die End Redirect URL in JATOS fest.
--%


## Registrieren Sie Prolific-Informationen in Ihrem Experiment

Jeder Teilnehmer von Prolific wird durch eine einzigartige ID identifiziert. Es ist wichtig, diese ID in Ihrem Experiment zu protokollieren, da dies es Ihnen ermöglicht, den Teilnehmer von Prolific den Einträgen in den JATOS-Ergebnissen zuzuordnen. Dies können Sie tun, indem Sie das unten stehende Skript in der Vorbereitungsphase eines `inline_javascript` Items ganz am Anfang Ihres Experiments hinzufügen.

Wenn das Experiment über Prolific läuft, steht die Prolific-ID als experimentelle Variable `prolific_participant_id` zur Verfügung. Wenn das Experiment auf andere Weise (z.B. während des Testens) läuft, wird die Variable `prolific_participant_id` auf -1 gesetzt. Die gleiche Logik gilt für die Prolific Study ID (`prolific_study_id`) und die Prolific Session ID (`prolific_session_id`).


```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Prolific-Informationen sind verfügbar')
    var prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    var prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    var prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Prolific-Informationen sind nicht verfügbar (Werte auf -1 setzen)')
    var prolific_participant_id = -1
    var prolific_study_id = -1
    var prolific_session_id = -1
}
console.log('prolific_participant_id = ' + prolific_participant_id)
console.log('prolific_study_id = ' + prolific_study_id)
console.log('prolific_session_id = ' + prolific_session_id)
```


## Teste die Studie

Gehen Sie zurück zur Studiendetails-Seite auf Prolific. Am unteren Ende der Seite befindet sich eine Vorschau-Schaltfläche. Damit können Sie das Experiment testen, indem Sie selbst als Teilnehmer agieren. Vergessen Sie nicht, die JATOS-Ergebnisse zu überprüfen, um sicherzustellen, dass das Experiment erfolgreich abgeschlossen wurde und dass alle notwendigen Informationen (einschließlich der Prolific-Informationen) protokolliert wurden!