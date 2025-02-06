title: SigmundAI Copilot
hash: 7a5ad3e4d415e7ac0275d30a2a31a4805bf4ac5d702bfbad1b3ff4319dd6b942
locale: de
language: German

SigmundAI Copilot befindet sich derzeit in der öffentlichen Beta
{:.page-notification}


[SigmundAI.eu](https://sigmundai.eu) ist ein KI-Forschungsassistent, der entwickelt wurde, um Ihnen bei OpenSesame zu helfen. Sie können Sigmund direkt aus OpenSesame heraus verwenden, indem Sie eine Erweiterung installieren. Sigmund erfordert ein Abonnement.


[TOC]


## Installation der Sigmund-Erweiterung

Zuerst installieren Sie das Paket `opensesame-extension-sigmund`:

```
pip install opensesame-extension-sigmund
```

Unter Windows müssen Sie den obigen Befehl als Administrator ausführen oder das `--user`-Flag hinzufügen:

```
pip install opensesame-extension-sigmund --user
```

Weitere Informationen zur Installation von Paketen finden Sie unter:

- <https://rapunzel.cogsci.nl/manual/environment/>


## Verbindung zu Sigmund

Melden Sie sich bei <https://sigmunai.eu/>Sigmund</a> an. Die Chat-Oberfläche sollte jetzt sichtbar sein. Die Chat-Oberfläche hört automatisch auf eingehende Verbindungen von OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: Die Chat-Oberfläche von SigmundAI.eu.
--%

Aktivieren Sie innerhalb von OpenSesame den SigmundAI Copilot, indem Sie auf das Robotersymbol in der Hauptwerkzeugleiste klicken. OpenSesame versucht nun, sich mit der Sigmund-Chat-Oberfläche zu verbinden.


%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame verbindet sich mit Sigmund.
--%

Nach ein paar Sekunden sollte eine Verbindung hergestellt werden. Die Sigmund-Chat-Oberfläche im Browser zeigt an, dass sie mit OpenSesame verbunden ist. Innerhalb von OpenSesame erscheint eine integrierte Chat-Oberfläche.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame ist mit Sigmund verbunden.
--%


## Funktionalität

### Bearbeiten von Objekten und Skripten

Zuerst wählen Sie ein Objekt in OpenSesame, indem Sie darauf im Übersichtsbereich klicken. Danach können Sie Fragen dazu stellen und sogar Sigmund bitten, das Objekt direkt zu ändern. 

Wenn Sie Sigmund zum Beispiel bitten, die Farbe des Textes auf einem SKETCHPAD auf Rot zu ändern, wird Sigmund eine einfache Änderung des SKETCHPAD-Skripts vorschlagen. Diese Änderung wird in einem sogenannten Diff-Viewer angezeigt, in dem Sie die Änderung überprüfen und entscheiden können, ob Sie sie übernehmen möchten oder nicht. Wenn Sie auf Ok klicken, wird die Änderung übernommen und der Text ist nun rot.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: Wenn Sigmund Änderungen vorschlägt, können Sie diese zunächst überprüfen, bevor Sie entscheiden, ob Sie sie akzeptieren möchten.
--%


### Fehlerbehebung

Wenn ein Fehler beim Ausführen Ihres Experiments auftritt, können Sie Sigmund bitten, den Fehler zu beheben. Sigmund wird dann den Fehler analysieren und möglicherweise Änderungen vorschlagen, um ihn zu beheben.

%--
figure:
 id: FigError
 source: error.png
 caption: Sie können Sigmund bitten, Fehler in Ihrem Experiment zu beheben.
--%