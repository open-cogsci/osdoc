title: JATOS
hash: b885bbb21d5bc5d8ffa13b6adf7ce306d93ad1253011bddf7529f22af3b5eb59
locale: es
language: Spanish

[TOC]

## Introducción a JATOS

[JATOS](https://www.jatos.org/) es un sistema para gestionar experimentos en línea. Te permite crear cuentas para experimentadores, subir experimentos y generar enlaces que puedes distribuir a los participantes. OpenSesame se integra estrechamente con JATOS.

Para acceder a un servidor JATOS, tienes tres opciones principales:

- Solicita una cuenta gratuita en [MindProbe](https://mindprobe.eu/), un servidor JATOS público patrocinado por ESCoP y OpenSesame.
- usa un servidor JATOS proporcionado por tu institución.
- Descargar JATOS e instalarlo en tu propio servidor.

## Vinculación de OpenSesame con JATOS/MindProbe

OpenSesame requiere un token de API para acceder a tu cuenta en un servidor JATOS como MindProbe. Sigue estos pasos para generar un token de API:

1. **Inicia sesión en JATOS.**
2. **Abre tu perfil de usuario** haciendo clic en tu nombre ubicado en la esquina superior derecha de la página.
3. **Crea un token de API** haciendo clic en 'API tokens' para ver todos tus tokens actuales, y luego haz clic en 'New Token'.
4. **Asigna un nombre a tu token**. Este nombre sirve como un descriptor que indica su uso previsto, como 'Integración con OpenSesame'.
5. **Establece una caducidad para tu token**. Los tokens caducan por defecto después de 30 días, lo que requiere que generes un nuevo token cada mes. Puedes seleccionar 'No Expiration' por conveniencia, pero ten en cuenta que es menos seguro. Si alguien accede a un token que no expira, puede usarlo indefinidamente, o hasta que revokes el token.

%--
figure:
 id: FigAPIToken
 source: api-token.png
 caption: Los tokens de API se pueden generar dentro de tu perfil de usuario de JATOS.
--%

Nota: Un token de API siempre comienza con `jap_`, seguido de una serie de caracteres y números. ¡Mantén tu token seguro!

Una vez que tengas tu token de API, abre el panel de control de OSWeb y JATOS en OpenSesame. Ingresa tu token de API en el campo correspondiente y también ajusta la URL del servidor JATOS, si es necesario.

%--
figure:
 id: FigJATOSControlPanel
 source: jatos-control-panel.png
 caption: Especifica el servidor JATOS y tu token de API en el panel de control de OSWeb y JATOS.
--%

## Publicar experimentos y descargarlos de JATOS/MindProbe

Después conectar exitosamente OpenSesame a JATOS, como se explicó anteriormente, puedes publicar tu experimento en JATOS. Para hacer esto, selecciona la opción 'Publicar en JATOS/MindProbe' del menú de archivos. Tras la publicación inicial, a tu experimento se le asignará un identificador único (UUID) que lo vincula a un estudio en JATOS.

Luego puedes visitar tu servidor JATOS y observar que el experimento recién publicado se ha agregado a tu lista de estudios.

A partir de ese momento, cada vez que publiques el experimento, el estudio JATOS existente se actualizará con la nueva versión. Si deseas publicar el experimento como un estudio completamente nuevo en JATOS, deberás restablecer el UUID de JATOS a través del panel de control de OSWeb y JATOS.

Para descargar un experimento de JATOS, selecciona la opción 'Abrir desde JATOS/MindProbe' del menú de archivos. Ten en cuenta que esta función solo es aplicable si el estudio JATOS correspondiente es compatible con OSWeb 2.