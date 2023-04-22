title: Coureurs
hash: 06242415e6cca1b1434321f7ba96e925abe4ccd2fd31cac48ab7ff6b64f73876
locale: fr
language: French

[TOC]

## À propos des runners

Il existe plusieurs façons techniquement différentes d'exécuter votre expérience. Chacune d'elles correspond à un *runner*. Vous pouvez sélectionner un runner dans Menu → Outils → Préférences → Runner.

Sauf si vous avez une raison de ne pas le faire, vous devriez utiliser le runner *multiprocess*. Cependant, si OpenSesame se bloque parfois, vous pouvez essayer de voir si la sélection d'un autre runner résout ce problème.

## Runners disponibles

### Multiprocess

Le runner *multiprocess* exécute votre expérience dans un processus différent. Le principal avantage de cette méthode est que votre expérience peut se bloquer sans entraîner la fermeture de l'interface utilisateur. Un autre avantage du runner *multiprocess* est qu'il permet à l'inspecteur de variables d'afficher vos variables expérimentales pendant l'exécution de l'expérience.

### Inprocess

Le runner *inprocess* exécute l'expérience dans le même processus que l'interface utilisateur. L'avantage de cette méthode est sa simplicité. L'inconvénient est que l'interface utilisateur peut se bloquer si l'expérience se bloque, et vice versa.

### Externe

Le runner *externe* exécute l'expérience en lançant opensesamerun en tant qu'application distincte. Le principal avantage de cette méthode est que votre expérience peut se bloquer sans entraîner la fermeture de l'interface utilisateur.