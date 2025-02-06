title: SigmundAI Copilot


SigmundAI Copilot is currently in public beta
{:.page-notification}

%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%


[SigmundAI.eu](https://sigmundai.eu) is an AI research assistant that has been designed to help you with OpenSesame. You can use Sigmund directly from within OpenSesame by installing an extension. Sigmund requires a subscription.


[TOC]


## Installing the Sigmund extension

First, install the `opensesame-extension-sigmund` package:

```
pip install opensesame-extension-sigmund
```

On Windows, you need to run the above command as Administrator, or pass the `--user` flag:

```
pip install opensesame-extension-sigmund --user
```

For more information about installing packages, see:

- <https://rapunzel.cogsci.nl/manual/environment/>


## Connecting to Sigmund

Log into <https://sigmundai.eu/>. The chat interface should now be visible. The chat interface automatically listens to incoming connections from OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%

Within OpenSesame, activate the SigmundAI Copilot by clicking on the Robot icon in the main toolbar. OpenSesame now tries to connect to the Sigmund chat interface.


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

### Editing items and scripts

First, select an item in OpenSesame by clicking on it in the overview area. Next, you can questions about it, and even ask Sigmund to modify the item directly. 

For example, if you ask Sigmund to change the color of text on a SKETCHPAD to red, Sigmund will propose a simple change to the SKETCHPAD script. This change will appear in a so-called diff viewer, where you can review it and decide whether or not you want to apply the change. If you click Ok, the change will be applied, and the text will now be red.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%


### Fixing errors

If an error occurs while running your experiment, you can ask Sigmund to fix the error. Sigmund will then analyze the error, and may suggest changes to fix it.


%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund can diagnose and fix errors in your experiment.
--%
