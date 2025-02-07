title: SigmundAI Copilot
hash: 068066429b87ece4165a56d9298972b751462edb129261bcda7b23fb49f2dcf5
locale: fr
language: French

SigmundAI Copilot est actuellement en version bêta publique
{:.page-notification}

%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%


[SigmundAI.eu](https://sigmundai.eu) est un assistant de recherche en IA conçu pour vous aider avec OpenSesame. Vous pouvez utiliser Sigmund directement depuis OpenSesame en installant une extension.


[TOC]


## Premiers pas

### Se connecter à Sigmund

Sigmund nécessite un abonnement mensuel, que vous pouvez annuler à tout moment. Rendez-vous sur <https://sigmundai.eu> pour vous abonner.

&#128150; Votre abonnement soutient le développement de logiciels open-source !

Une fois connecté à Sigmund, l'interface de chat devient visible. L'interface de chat écoute automatiquement les connexions entrantes d'OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%


### Installer l'extension Sigmund dans OpenSesame

Pour se connecter à Sigmund depuis OpenSesame, vous devez installer le package `opensesame-extension-sigmund`. Vous pouvez le faire en entrant la commande suivante dans la console d'OpenSesame :

```
pip install opensesame-extension-sigmund
```

Sous Windows, vous devez exécuter la commande ci-dessus en tant qu'Administrateur, ou ajouter le paramètre `--user` :

```
pip install opensesame-extension-sigmund --user
```

Après avoir installé l'extension, redémarrez OpenSesame. L'icône de Sigmund devrait maintenant apparaître dans la barre d'outils principale. Activez SigmundAI Copilot en cliquant sur l'icône Sigmund.


%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame is connecting to Sigmund.
--%

Après quelques secondes, une connexion devrait être établie. L'interface de chat Sigmund dans le navigateur indique qu'elle est connectée à OpenSesame. Dans OpenSesame, une interface de chat intégrée apparaît.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame is connected to Sigmund.
--%

### Résoudre les problèmes courants

Sigmund est en cours de développement actif. Si vous rencontrez des problèmes, assurez-vous d'avoir appliqué toutes les mises à jour disponibles, qui apparaissent via le programme de mise à jour automatique d'OpenSesame.

Si l'icône de Sigmund (un visage de robot jaune) n'apparaît pas dans la barre d'outils principale, cela signifie probablement que l'extension Sigmund n'est pas installée. Consultez [cette page](https://rapunzel.cogsci.nl/manual/environment/) pour en savoir plus sur la gestion des packages dans OpenSesame.

Si vous voyez continuellement le message : "Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect", cela signifie probablement que <https://sigmundai.eu> n'est pas ouvert ou n'est pas actif dans un navigateur web. De nombreux navigateurs désactivent automatiquement les pages qui ne sont pas utilisées. Ouvrir (ou recharger) l'onglet Sigmund AI devrait réactiver la page.

Si vous voyez le message "Failed to listen to Sigmund. Maybe another application is already listening?", cela signifie probablement que vous avez démarré OpenSesame deux fois. Une seule instance d'OpenSesame peut se connecter à Sigmund à la fois. Une raison moins probable pour ce message est qu'un autre processus (non lié) utilise le port 8080 sur votre système. Pour déboguer cela, demandez simplement à Sigmund : "J'utilise [votre système d'exploitation ici]. Je pense qu'un processus utilise le port 8080. Comment puis-je savoir si c'est le cas, et si oui, quel processus utilise le port 8080?"


## Fonctionnalité

### Sigmund peut éditer des items et des scripts

Tout d'abord, sélectionnez un item dans OpenSesame en cliquant dessus dans la zone de vue d'ensemble. Ensuite, vous pouvez poser des questions à son sujet, et même demander à Sigmund de modifier directement l'item.

Par exemple, si vous demandez à Sigmund de changer la couleur du texte sur un SKETCHPAD en rouge, Sigmund proposera un changement simple au script SKETCHPAD. Ce changement apparaîtra dans ce qu'on appelle un "diff viewer", où vous pouvez le passer en revue et décider si vous souhaitez ou non l'appliquer. Si vous cliquez sur Ok, le changement sera appliqué et le texte sera désormais rouge.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%

### Sigmund peut corriger les erreurs dans votre expérience

Si une erreur survient lors de l'exécution de votre expérience, vous pouvez demander à Sigmund de la corriger. Sigmund analysera alors l'erreur et pourra suggérer des modifications pour la résoudre.

%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund can diagnose and fix errors in your experiment.
--%