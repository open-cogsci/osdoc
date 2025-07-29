title: SigmundAI Copilot


%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%


[SigmundAI.eu](https://sigmundai.eu) is an AI research assistant that has been designed to help you with OpenSesame. You can use Sigmund directly from within OpenSesame by installing an extension.


[TOC]


## Connecting to SigmundAI

Sigmund requires a monthly subscription, which can be cancelled at any time. Visit <https://sigmundai.eu> to subscribe.

&#128150; Your subscription supports the development of open-source software! 

Once you are logged in to Sigmund, the chat interface becomes visible. The chat interface automatically listens to incoming connections from OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%

Next, activate the SigmundAI Copilot by clicking on the Sigmund icon.

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame is connecting to Sigmund.
--%

After a few seconds, a connection should be established. The Sigmund chat interface in the browser indicates that it is connected to OpenSesame. Within OpenSesame, an integrated chat interface appears.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame is connected to Sigmund.
--%


## Functionality

### Sigmund can edit items and scripts

First, select an item in OpenSesame by clicking on it in the overview area. Next, you can questions about it, and even ask Sigmund to modify the item directly. 

For example, if you ask Sigmund to change the color of text on a SKETCHPAD to red, Sigmund will propose a simple change to the SKETCHPAD script. This change will appear in a so-called diff viewer, where you can review it and decide whether or not you want to apply the change. If you click Ok, the change will be applied, and the text will now be red.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%


### Sigmund can fix errors in your experiment

If an error occurs while running your experiment, you can ask Sigmund to fix the error. Sigmund will then analyze the error, and may suggest changes to fix it.


%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund can diagnose and fix errors in your experiment.
--%


### Fixing common issues

If you continuously see the message, "Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect", this likely means that <https://sigmundai.eu> is not open or not active in a web browser. Many browsers automatically deactivate pages that are not being used. Opening (or reloading) the Sigmund AI tab should re-activate the page.

If you see the message "Failed to listen to Sigmund. Maybe another application is already listening?", this likely means that you already started OpenSesame (or another application that has connected to Sigmund). Only one application can connect to Sigmund at a time.
