title: JATOS


[TOC]


## Introduction to JATOS

[JATOS](https://www.jatos.org/) is a system for managing online experiments. It allows you to create accounts for experimenters, upload experiments, and generate links that you can distribute to participants. OpenSesame integrates closely with JATOS.

To access a JATOS server, you have three main options:

- Request a free account on [MindProbe](https://mindprobe.eu/), a public JATOS server sponsored by ESCoP and OpenSesame.
- se a JATOS server provided by your institution.
- Download JATOS and install it on your own server.

## Linking OpenSesame with JATOS/MindProbe

OpenSesame requires an API token to access your account on a JATOS server such as MindProbe. Follow these steps to generate an API token:

1. **Log into JATOS.**
2. **Open your user profile** by clicking on your name located in the top right corner of the page.
3. **Create an API token** by clicking on 'API tokens' to view all your current tokens, and then click 'New Token'.
4. **Assign a name to your token**. This name serves as a descriptor indicating its intended use, such as 'OpenSesame integration'.
5. **Set an expiration for your token**. Tokens default to expire after 30 days, requiring you to generate a new token each month. You can select 'No Expiration' for convenience, but be aware that it is less secure. If someone gains access to a non-expiring token, they can use it indefinitely, or until you revoke the token.

%--
figure:
 id: FigAPIToken
 source: api-token.png
 caption: API tokens can be generated within your JATOS user profile.
--%

Note: An API token always begins with `jap_`, followed by a series of characters and numbers. Keep your token secure!

Once you have your API token, open the OSWeb and JATOS control panel in OpenSesame. Enter your API token into the corresponding field and also adjust the JATOS server URL, if necessary.

%--
figure:
 id: FigJATOSControlPanel
 source: jatos-control-panel.png
 caption: Specify the JATOS server and your API token in the OSWeb and JATOS control panel.
--%


## Publishing experiments to, and downloading from, JATOS/MindProbe

After successfully connecting OpenSesame to JATOS, as explained above, you can publish your experiment to JATOS. To do this, select the 'Publish to JATOS/MindProbe' option from the File menu. Upon initial publication, your experiment will be assigned a unique identifier (UUID) that links it to a study on JATOS.

You can then visit your JATOS server and observe that the newly published experiment has been added to your list of studies.

From that point forward, each time you publish the experiment, the existing JATOS study will be updated with the new version. If you wish to publish the experiment as a completely new study on JATOS, you will need to reset the JATOS UUID via the OSWeb and JATOS control panel.

To download an experiment from JATOS, select the 'Open from JATOS/MindProbe' option from the File menu. Please note, this function is only applicable if the corresponding JATOS study is compatible with OSWeb 2.
