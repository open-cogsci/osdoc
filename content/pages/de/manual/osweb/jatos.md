title: JATOS
hash: b885bbb21d5bc5d8ffa13b6adf7ce306d93ad1253011bddf7529f22af3b5eb59
locale: de
language: German

[TOC]


## Einführung in JATOS

[JATOS](https://www.jatos.org/) ist ein System zur Verwaltung von Online-Experimenten. Es ermöglicht Ihnen die Erstellung von Konten für Experimentatoren, das Hochladen von Experimenten und das Generieren von Links, die Sie an Teilnehmer verteilen können. OpenSesame ist eng mit JATOS integriert.

Um auf einen JATOS-Server zuzugreifen, haben Sie drei Hauptoptionen:

- Beantragen Sie ein kostenloses Konto auf [MindProbe](https://mindprobe.eu/), einem öffentlichen JATOS-Server, der von ESCoP und OpenSesame gesponsert wird.
- Nutzen Sie einen JATOS-Server, der von Ihrer Institution bereitgestellt wird.
- Laden Sie JATOS herunter und installieren Sie es auf Ihrem eigenen Server.

## Verknüpfung von OpenSesame mit JATOS/MindProbe

OpenSesame benötigt ein API-Token, um auf Ihr Konto auf einem JATOS-Server wie MindProbe zuzugreifen. Befolgen Sie diese Schritte, um ein API-Token zu erstellen:

1. **Melden Sie sich bei JATOS an**.
2. **Öffnen Sie Ihr Benutzerprofil** , indem Sie auf Ihren Namen klicken, der sich in der oberen rechten Ecke der Seite befindet.
3. **Erstellen Sie ein API-Token** , indem Sie auf 'API-Token' klicken, um alle Ihre aktuellen Token anzuzeigen, und dann auf 'Neues Token' klicken.
4. **Weisen Sie Ihrem Token einen Namen zu**. Dieser Name dient als Beschreibung für seinen vorgesehenen Einsatz, wie z.B. 'OpenSesame-Integration'.
5. **Legen Sie ein Ablaufdatum für Ihr Token fest**. Tokens laufen standardmäßig nach 30 Tagen ab, so dass Sie jeden Monat ein neues Token erstellen müssen. Sie können 'Kein Ablaufdatum' auswählen, um es bequem zu machen, aber seien Sie sich bewusst, dass es weniger sicher ist. Wenn jemand Zugang zu einem nicht ablaufenden Token erhält, kann er es unbegrenzt verwenden oder bis Sie das Token widerrufen.

%--
Figure:
 id: FigAPIToken
 source: api-token.png
 caption: API-Tokens können innerhalb Ihres JATOS-Benutzerprofils generiert werden.
--%

Hinweis: Ein API-Token beginnt immer mit `jap_`, gefolgt von einer Reihe von Zeichen und Zahlen. Schützen Sie Ihr Token!

Sobald Sie Ihr API-Token haben, öffnen Sie das OSWeb und JATOS-Kontrollpanel in OpenSesame. Geben Sie Ihr API-Token in das entsprechende Feld ein und passen Sie auch die JATOS-Server-URL an, falls erforderlich.

%--
Figure:
 id: FigJATOSControlPanel
 source: jatos-control-panel.png
 caption: Geben Sie den JATOS-Server und Ihr API-Token im OSWeb und JATOS-Kontrollpanel an.
--%


## Experimente auf JATOS/MindProbe veröffentlichen und von dort herunterladen

Nachdem Sie OpenSesame erfolgreich mit JATOS verknüpft haben, wie oben erklärt, können Sie Ihr Experiment auf JATOS veröffentlichen. Dazu wählen Sie die Option 'Auf JATOS/MindProbe veröffentlichen' aus dem Datei-Menü. Bei der Erstveröffentlichung wird Ihrem Experiment eine eindeutige Kennung (UUID) zugewiesen, die es mit einer Studie auf JATOS verknüpft.

Sie können dann Ihren JATOS-Server besuchen und feststellen, dass das neu veröffentlichte Experiment zu Ihrer Liste der Studien hinzugefügt wurde.

Ab diesem Zeitpunkt wird jedes Mal, wenn Sie das Experiment veröffentlichen, die bestehende JATOS-Studie mit der neuen Version aktualisiert. Wenn Sie das Experiment als völlig neue Studie auf JATOS veröffentlichen möchten, müssen Sie die JATOS-UUID über das OSWeb und JATOS-Kontrollpanel zurücksetzen.

Um ein Experiment von JATOS herunterzuladen, wählen Sie die Option 'Von JATOS/MindProbe öffnen' aus dem Datei-Menü. Bitte beachten Sie, dass diese Funktion nur anwendbar ist, wenn die entsprechende JATOS-Studie mit OSWeb 2 kompatibel ist.
