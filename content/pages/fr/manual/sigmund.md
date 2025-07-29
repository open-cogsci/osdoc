title: SigmundAI Copilot
hash: 72727f42fda075f92ed04c3fec80945ccbc7a18696b66aa3ddc6cb97f87a997c
locale: fr
language: French

%--
figure:
 id: FigExample
 source: example.png
 caption: Dépannage d'un problème avec Sigmund.
--%


[SigmundAI.eu](https://sigmundai.eu) est un assistant de recherche en IA conçu pour vous aider avec OpenSesame. Vous pouvez utiliser Sigmund directement depuis OpenSesame en installant une extension.


[TOC]


## Connexion à SigmundAI

Sigmund nécessite un abonnement mensuel, qui peut être résilié à tout moment. Rendez-vous sur <https://sigmundai.eu> pour vous abonner.

&#128150; Votre abonnement soutient le développement de logiciels open-source ! 

Une fois connecté à Sigmund, l'interface de chat devient visible. L’interface de chat écoute automatiquement les connexions entrantes depuis OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: L'interface de chat de SigmundAI.eu.
--%

Ensuite, activez SigmundAI Copilot en cliquant sur l’icône Sigmund.

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

### Sigmund peut modifier des items et des scripts

Tout d'abord, sélectionnez un item dans OpenSesame en cliquant dessus dans la zone d’aperçu. Ensuite, vous pouvez poser des questions à son sujet, et même demander à Sigmund de modifier directement l’item.

Par exemple, si vous demandez à Sigmund de changer la couleur du texte sur un SKETCHPAD en rouge, Sigmund proposera une modification simple du script SKETCHPAD. Cette modification apparaîtra dans ce que l’on appelle un visionneur de différences (diff viewer), où vous pourrez la consulter et décider si vous souhaitez l'appliquer ou non. Si vous cliquez sur Ok, la modification sera appliquée, et le texte sera désormais rouge.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: Lorsque Sigmund suggère des changements, vous pouvez d'abord les examiner avant de décider de les accepter.
--%


### Sigmund peut corriger les erreurs dans votre expérience

Si une erreur survient lors de l’exécution de votre expérience, vous pouvez demander à Sigmund de la corriger. Sigmund analysera alors l’erreur et pourra suggérer des modifications pour la corriger.


%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund peut diagnostiquer et corriger les erreurs dans votre expérience.
--%


### Correction des problèmes courants

Si vous voyez continuellement le message "Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect", cela signifie probablement que <https://sigmundai.eu> n’est pas ouvert ou pas actif dans un navigateur web. Beaucoup de navigateurs désactivent automatiquement les pages qui ne sont pas utilisées. Ouvrir (ou recharger) l’onglet Sigmund AI devrait réactiver la page.

Si vous voyez le message "Failed to listen to Sigmund. Maybe another application is already listening?", cela signifie probablement que vous avez déjà démarré OpenSesame (ou une autre application connectée à Sigmund). Une seule application peut se connecter à Sigmund à la fois.