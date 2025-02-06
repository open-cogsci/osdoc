title: SigmundAI Copiloto
hash: 7a5ad3e4d415e7ac0275d30a2a31a4805bf4ac5d702bfbad1b3ff4319dd6b942
locale: es
language: Spanish

SigmundAI Copilot está actualmente en beta pública
{:.page-notification}


[SigmundAI.eu](https://sigmundai.eu) es un asistente de investigación de IA diseñado para ayudarte con OpenSesame. Puedes usar Sigmund directamente desde OpenSesame instalando una extensión. Sigmund requiere una suscripción.


[TOC]


## Instalando la extensión de Sigmund

Primero, instala el paquete `opensesame-extension-sigmund`:

```
pip install opensesame-extension-sigmund
```

En Windows, necesitas ejecutar el comando anterior como Administrador, o usar el flag `--user`:

```
pip install opensesame-extension-sigmund --user
```

Para más información sobre la instalación de paquetes, consulta:

- <https://rapunzel.cogsci.nl/manual/environment/>


## Conectando con Sigmund

Inicia sesión en <https://sigmunai.eu/>Sigmund</a>. La interfaz de chat debería ser visible ahora. La interfaz de chat escucha automáticamente las conexiones entrantes de OpenSesame.

%--
figure:
 id: FigChatWindow
 source: chat-window.png
 caption: La interfaz de chat de SigmundAI.eu.
--%

Dentro de OpenSesame, activa el SigmundAI Copilot haciendo clic en el icono de Robot en la barra de herramientas principal. OpenSesame ahora intenta conectarse a la interfaz de chat de Sigmund.

%--
figure:
 id: FigListening
 source: listening.png
 caption: OpenSesame se está conectando a Sigmund.
--%

Después de unos segundos, una conexión debería establecerse. La interfaz de chat de Sigmund en el navegador indica que está conectada a OpenSesame. Dentro de OpenSesame, aparece una interfaz de chat integrada.

%--
figure:
 id: FigConnected
 source: connected.png
 caption: OpenSesame está conectado a Sigmund.
--%


## Funcionalidad

### Editando ítems y scripts

Primero, selecciona un ítem en OpenSesame haciendo clic en él en el área de vista general. A continuación, puedes hacer preguntas sobre él, e incluso pedirle a Sigmund que modifique el ítem directamente.

Por ejemplo, si le pides a Sigmund que cambie el color del texto en un SKETCHPAD a rojo, Sigmund propondrá un cambio simple en el script de SKETCHPAD. Este cambio aparecerá en un visor de diferencias, donde podrás revisarlo y decidir si deseas aplicar el cambio o no. Si haces clic en Ok, el cambio se aplicará, y el texto ahora será rojo.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: Cuando Sigmund sugiere cambios, primero puedes revisarlos antes de decidir si los aceptas o no.
--%


### Corregir errores

Si se produce un error mientras ejecutas tu experimento, puedes pedirle a Sigmund que lo corrija. Sigmund entonces analizará el error, y puede sugerir cambios para solucionarlo.

%--
figure:
 id: FigError
 source: error.png
 caption: Puedes pedirle a Sigmund que corrija errores en tu experimento.
--%