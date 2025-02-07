title: SigmundAI Copiloto
hash: 068066429b87ece4165a56d9298972b751462edb129261bcda7b23fb49f2dcf5
locale: es
language: Spanish

SigmundAI Copilot está actualmente en beta pública
{:.page-notification}

[SigmundAI.eu](https://sigmundai.eu) es un asistente de investigación de IA diseñado para ayudarte con OpenSesame. Puedes usar Sigmund directamente desde OpenSesame instalando una extensión.

## Primeros pasos

### Iniciar sesión en Sigmund

Sigmund requiere una suscripción mensual, la cual se puede cancelar en cualquier momento. Ve a <https://sigmundai.eu> para suscribirte.

&#128150; ¡Tu suscripción apoya el desarrollo de software de código abierto!

Una vez que inicies sesión en Sigmund, la interfaz de chat se vuelve visible. La interfaz de chat escucha automáticamente las conexiones entrantes desde OpenSesame.

### Instalando la extensión de Sigmund en OpenSesame

Para conectarte a Sigmund desde dentro de OpenSesame, necesitas instalar el paquete `opensesame-extension-sigmund`. Puedes hacerlo ingresando el siguiente comando en la consola de OpenSesame:

```
pip install opensesame-extension-sigmund
```

En Windows, necesitas ejecutar el comando anterior como Administrador, o pasar el flag `--user`:

```
pip install opensesame-extension-sigmund --user
```

Después de instalar la extensión, reinicia OpenSesame. El icono de Sigmund debería ahora aparecer en la barra de herramientas principal. Activa SigmundAI Copilot haciendo clic en el icono de Sigmund.

Después de unos segundos, debería establecerse una conexión. La interfaz de chat de Sigmund en el navegador indica que está conectada a OpenSesame. Dentro de OpenSesame, aparece una interfaz de chat integrada.

### Solucionar problemas comunes

Sigmund está en desarrollo activo. Si encuentras problemas, primero asegúrate de haber aplicado todas las actualizaciones, que aparecen a través del actualizador automático en OpenSesame.

Si el icono de Sigmund (una cara de robot amarilla) no aparece en la barra de herramientas principal, esto probablemente significa que la extensión de Sigmund no está instalada. Consulta [esta página](https://rapunzel.cogsci.nl/manual/environment/) para saber más sobre cómo gestionar paquetes en OpenSesame.

Si ves continuamente el mensaje, "Abre https://sigmundai.eu en un navegador e inicia sesión. OpenSesame se conectará automáticamente", esto probablemente significa que <https://sigmundai.eu> no está abierto o no está activo en un navegador web. Muchos navegadores desactivan automáticamente las páginas que no se están utilizando. Abrir (o recargar) la pestaña de Sigmund AI debería reactivar la página.

Si ves el mensaje "No se pudo escuchar a Sigmund. ¿Quizás otra aplicación ya está escuchando?", esto probablemente significa que iniciaste OpenSesame dos veces. Solo una instancia de OpenSesame puede conectarse a Sigmund a la vez. Una razón menos probable para este mensaje es que otro proceso (no relacionado) está utilizando el puerto 8080 en tu sistema. Para solucionar este problema, simplemente pregunta a Sigmund: "Estoy usando [tu sistema operativo aquí]. Creo que algún proceso está utilizando el puerto 8080. ¿Cómo puedo averiguar si esto es así, y si es el caso, qué proceso está utilizando el puerto 8080?"

## Funcionalidad

### Sigmund puede editar ítems y scripts

Primero, selecciona un ítem en OpenSesame haciendo clic en él en el área de vista general. A continuación, puedes hacer preguntas al respecto, e incluso pedir a Sigmund que modifique el ítem directamente.

Por ejemplo, si le pides a Sigmund que cambie el color del texto en un SKETCHPAD a rojo, Sigmund propondrá un cambio simple en el script del SKETCHPAD. Este cambio aparecerá en un visor de diferencias, donde puedes revisarlo y decidir si deseas aplicar el cambio. Si haces clic en Ok, el cambio se aplicará, y el texto ahora será rojo.

%--
figure:
 id: FigDiffViewer
 source: diff-viewer.png
 caption: When Sigmund suggests changes, you can first review the changes before deciding whether or not to accept them.
--%


### Sigmund puede corregir errores en tu experimento

Si ocurre un error mientras se ejecuta tu experimento, puedes pedir a Sigmund que lo solucione. Luego, Sigmund analizará el error y puede sugerir cambios para corregirlo.


%--
figure:
 id: FigError
 source: error.png
 caption: Sigmund puede diagnosticar y corregir errores en tu experimento.
--%