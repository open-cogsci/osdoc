title: SigmundAI Copilot
hash: 068066429b87ece4165a56d9298972b751462edb129261bcda7b23fb49f2dcf5
locale: de
language: German

SigmundAI Copilot befindet sich derzeit in der öffentlichen Beta
{:.page-notification}

%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%

[SigmundAI.eu](https://sigmundai.eu) ist ein KI-Forschungsassistent, der entwickelt wurde, um Ihnen mit OpenSesame zu helfen. Sie können Sigmund direkt aus OpenSesame heraus nutzen, indem Sie eine Erweiterung installieren.

[TOC]

## Erste Schritte

### Anmeldung bei Sigmund

Sigmund erfordert ein monatliches Abonnement, das jederzeit gekündigt werden kann. Gehen Sie zu <https://sigmundai.eu>, um sich anzumelden.

&#128150; Ihr Abonnement unterstützt die Entwicklung von Open-Source-Software!

Sobald Sie bei Sigmund eingeloggt sind, wird die Chat-Oberfläche sichtbar. Die Chat-Oberfläche hört automatisch auf eingehende Verbindungen von OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%

### Installation der Sigmund-Erweiterung in OpenSesame

Um sich mit Sigmund aus OpenSesame heraus zu verbinden, müssen Sie das Paket `opensesame-extension-sigmund` installieren. Sie können dies tun, indem Sie den folgenden Befehl in der OpenSesame-Konsole eingeben:

```
pip install opensesame-extension-sigmund
```

Unter Windows müssen Sie den obigen Befehl als Administrator ausführen oder das `--user`-Flag verwenden:

```
pip install opensesame-extension-sigmund --user
```

Nach der Installation der Erweiterung starten Sie OpenSesame neu. Das Sigmund-Icon sollte jetzt in der Hauptsymbolleiste erscheinen. Aktivieren Sie den SigmundAI Copilot, indem Sie auf das Sigmund-Icon klicken.

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame is connecting to Sigmund.
--%

Nach einigen Sekunden sollte eine Verbindung hergestellt werden. Die Sigmund-Chat-Oberfläche im Browser zeigt an, dass sie mit OpenSesame verbunden ist. Innerhalb von OpenSesame erscheint eine integrierte Chat-Oberfläche.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame is connected to Sigmund.
--%

### Beheben von häufigen Problemen

Sigmund befindet sich in aktiver Entwicklung. Wenn Sie auf Probleme stoßen, stellen Sie zunächst sicher, dass Sie alle Updates angewendet haben, die über den automatischen Updater in OpenSesame erscheinen.

Wenn das Sigmund-Icon (ein gelbes Roboter-Gesicht) nicht in der Hauptsymbolleiste erscheint, bedeutet dies wahrscheinlich, dass die Sigmund-Erweiterung nicht installiert ist. Siehe [diese Seite](https://rapunzel.cogsci.nl/manual/environment/), um mehr darüber zu erfahren, wie man Pakete in OpenSesame verwaltet.

Wenn Sie ständig die Nachricht sehen: "Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect", bedeutet dies wahrscheinlich, dass <https://sigmundai.eu> nicht geöffnet oder nicht aktiv in einem Webbrowser ist. Viele Browser deaktivieren automatisch Seiten, die nicht genutzt werden. Das Öffnen (oder Neuladen) des Sigmund AI-Tabs sollte die Seite reaktivieren.

Wenn Sie die Nachricht "Failed to listen to Sigmund. Maybe another application is already listening?" sehen, bedeutet dies wahrscheinlich, dass Sie OpenSesame zweimal gestartet haben. Nur eine Instanz von OpenSesame kann gleichzeitig zu Sigmund verbinden. Ein weniger wahrscheinlicher Grund für diese Nachricht ist, dass ein anderer (unabhängiger) Prozess Port 8080 auf Ihrem System verwendet. Um dies zu debuggen, fragen Sie einfach Sigmund: "Ich benutze [Ihr Betriebssystem hier]. Ich denke, dass ein Prozess Port 8080 benutzt. Wie kann ich herausfinden, ob dies der Fall ist und wenn ja, welcher Prozess Port 8080 benutzt?"

## Funktionalität

### Sigmund kann Items und Skripte bearbeiten

Zuerst wählen Sie ein Item in OpenSesame aus, indem Sie darauf im Übersichtsbereich klicken. Anschließend können Sie Fragen dazu stellen und Sigmund sogar bitten, das Item direkt zu ändern.

Zum Beispiel, wenn Sie Sigmund bitten, die Farbe des Textes auf einer SKETCHPAD in rot zu ändern, wird Sigmund eine einfache Änderung des SKETCHPAD-Skripts vorschlagen. Diese Änderung wird in einem sogenannten Diff-Viewer angezeigt, wo Sie sie überprüfen und entscheiden können, ob Sie die Änderung übernehmen wollen oder nicht. Wenn Sie auf Ok klicken, wird die Änderung angewendet und der Text ist nun rot.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%


### Sigmund kann Fehler in deinem Experiment beheben

Wenn während der Durchführung deines Experiments ein Fehler auftritt, kannst du Sigmund bitten, den Fehler zu beheben. Sigmund wird dann den Fehler analysieren und möglicherweise Änderungen vorschlagen, um ihn zu beheben.


%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund can diagnose and fix errors in your experiment.
--%