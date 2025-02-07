title: SigmundAI Copilot


SigmundAI Copilot is currently in public beta
{:.page-notification}

%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%


[SigmundAI.eu](https://sigmundai.eu) is an AI research assistant that has been designed to help you with OpenSesame. You can use Sigmund directly from within OpenSesame by installing an extension.


[TOC]


## Getting started

### Logging into Sigmund

Sigmund requires a monthly subscription, which can be cancelled at any time. Go to <https://sigmundai.eu> to subscribe.

&#128150; Your subscription supports the development of open-source software! 

Once you are logged in to Sigmund, the chat interface becomes visible. The chat interface automatically listens to incoming connections from OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%


### Installing the Sigmund extension in OpenSesame

To connect to Sigmund from within OpenSesame, you need to install the `opensesame-extension-sigmund` package. You can do this by entering the following command in the OpenSesame console:

```
pip install opensesame-extension-sigmund
```

On Windows, you need to run the above command as Administrator, or pass the `--user` flag:

```
pip install opensesame-extension-sigmund --user
```

After installing the extension, restart OpenSesame. The Sigmund icon should now appear in the main toolbar. Activate the SigmundAI Copilot by clicking on the Sigmund icon.


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

### Fixing common issues

Sigmund is under active development. If you encounter issues, first make sure that you have applied all updates, which appear through the automatic updater in OpenSesame.

If the Sigmund icon (a yellow robot face) does not appear in the main toolbar, this likely means that the Sigmund extension is not installed. See [this page](https://rapunzel.cogsci.nl/manual/environment/) to learn more about how to manage packages in OpenSesame.

If you continuously see the message, "Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect", this likely means that <https://sigmundai.eu> is not open or not active in a web browser. Many browsers automatically deactivate pages that are not being used. Opening (or reloading) the Sigmund AI tab should re-activate the page.

If you see the message "Failed to listen to Sigmund. Maybe another application is already listening?", this likely means that you started OpenSesame twice. Only one instance of OpenSesame can connect to Sigmund at a time. A less likely reason for this message is that another (unrelated) process is using port 8080 on your system. To debug this, simply ask Sigmund: "I'm using [your operating system here]. I think that some process is using port 8080. How can I find out whether this is the case, and if so, which process is using port 8080?"


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
