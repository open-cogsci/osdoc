title: SigmundAI Copiloto
hash: 72727f42fda075f92ed04c3fec80945ccbc7a18696b66aa3ddc6cb97f87a997c
locale: es
language: Spanish

%--
figure:
 id: FigExample
 source: example.png
 caption: Debugging an issue with Sigmund.
--%


[SigmundAI.eu](https://sigmundai.eu) es un asistente de investigación de IA diseñado para ayudarte con OpenSesame. Puedes usar Sigmund directamente desde OpenSesame instalando una extensión.


[TOC]


## Conectarse a SigmundAI

Sigmund requiere una suscripción mensual, la cual se puede cancelar en cualquier momento. Visita <https://sigmundai.eu> para suscribirte.

&#128150; ¡Tu suscripción apoya el desarrollo de software de código abierto!

Una vez que hayas iniciado sesión en Sigmund, la interfaz de chat se vuelve visible. La interfaz de chat escucha automáticamente las conexiones entrantes desde OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: The chat interface of SigmundAI.eu.
--%

A continuación, activa el Copilot de SigmundAI haciendo clic en el icono de Sigmund.

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame is connecting to Sigmund.
--%

Después de unos segundos, debería establecerse una conexión. La interfaz de chat de Sigmund en el navegador indica que está conectada a OpenSesame. Dentro de OpenSesame, aparece una interfaz de chat integrada.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame is connected to Sigmund.
--%


## Funcionalidad

### Sigmund puede editar ítems y scripts

Primero, selecciona un ítem en OpenSesame haciendo clic en él en el área de vista general. Luego, puedes hacer preguntas sobre ese ítem, e incluso pedirle a Sigmund que modifique el ítem directamente.

Por ejemplo, si le pides a Sigmund que cambie el color del texto en un SKETCHPAD a rojo, Sigmund propondrá un cambio simple en el script del SKETCHPAD. Este cambio aparecerá en un visor de diferencias, donde podrás revisarlo y decidir si quieres aplicar el cambio o no. Si haces clic en Ok, el cambio se aplicará y el texto ahora será rojo.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%


### Sigmund puede corregir errores en tu experimento

Si ocurre un error mientras ejecutas tu experimento, puedes pedirle a Sigmund que corrija el error. Sigmund analizará el error y podrá sugerir modificaciones para solucionarlo.

%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund can diagnose and fix errors in your experiment.
--%


### Solución de problemas comunes

Si continuamente ves el mensaje "Open https://sigmundai.eu in a browser and log in. OpenSesame will automatically connect", esto probablemente significa que <https://sigmundai.eu> no está abierto o no está activo en un navegador web. Muchos navegadores desactivan automáticamente páginas que no están siendo usadas. Abrir (o recargar) la pestaña de Sigmund AI debería reactivar la página.

Si ves el mensaje "Failed to listen to Sigmund. Maybe another application is already listening?", esto probablemente significa que ya has iniciado OpenSesame (u otra aplicación que se haya conectado a Sigmund). Solo una aplicación puede conectarse a Sigmund al mismo tiempo.