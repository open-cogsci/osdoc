title: SigmundAI Copilot
hash: 7a5ad3e4d415e7ac0275d30a2a31a4805bf4ac5d702bfbad1b3ff4319dd6b942
locale: fr
language: French

SigmundAI Copilot est actuellement en version bêta publique
{:.page-notification}


[SigmundAI.eu](https://sigmundai.eu) est un assistant de recherche en IA qui a été conçu pour vous aider avec OpenSesame. Vous pouvez utiliser Sigmund directement à partir d'OpenSesame en installant une extension. Sigmund nécessite un abonnement.


[TOC]


## Installation de l'extension Sigmund

Tout d'abord, installez le paquet `opensesame-extension-sigmund` :

```
pip install opensesame-extension-sigmund
```

Sur Windows, vous devez exécuter la commande ci-dessus en tant qu'Administrateur, ou passer le drapeau `--user` :

```
pip install opensesame-extension-sigmund --user
```

Pour plus d'informations sur l'installation des paquets, consultez :

- <https://rapunzel.cogsci.nl/manual/environment/>


## Connexion à Sigmund

Connectez-vous à <https://sigmunai.eu/>Sigmund</a>. L'interface de chat devrait maintenant être visible. L'interface de chat écoute automatiquement les connexions entrantes d'OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: L'interface de chat de SigmundAI.eu.
--%

Dans OpenSesame, activez SigmundAI Copilot en cliquant sur l'icône Robot dans la barre d'outils principale. OpenSesame essaie maintenant de se connecter à l'interface de chat de Sigmund.

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame se connecte à Sigmund.
--%

Après quelques secondes, une connexion devrait être établie. L'interface de chat Sigmund dans le navigateur indique qu'elle est connectée à OpenSesame. Dans OpenSesame, une interface de chat intégrée apparaît.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame est connecté à Sigmund.
--%


## Fonctionnalités

### Édition d'éléments et de scripts

Tout d'abord, sélectionnez un élément dans OpenSesame en cliquant dessus dans la zone de vue d'ensemble. Ensuite, vous pouvez poser des questions à son sujet, et même demander à Sigmund de modifier l'élément directement.

Par exemple, si vous demandez à Sigmund de changer la couleur du texte sur un SKETCHPAD en rouge, Sigmund proposera une simple modification dans le script SKETCHPAD. Ce changement apparaîtra dans un visualiseur de diff, où vous pourrez l'examiner et décider si vous souhaitez ou non l'appliquer. Si vous cliquez sur Ok, le changement sera appliqué, et le texte sera désormais rouge.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: Lorsque Sigmund propose des changements, vous pouvez d'abord les examiner avant de décider de les accepter ou non.
--%


### Correction des erreurs

Si une erreur survient lors de l'exécution de votre expérience, vous pouvez demander à Sigmund de la corriger. Sigmund analysera alors l'erreur et pourra suggérer des modifications pour la corriger.

%--
figure:
 id: FigError
 source: error.png
 caption: Vous pouvez demander à Sigmund de corriger les erreurs dans votre expérience.
--%