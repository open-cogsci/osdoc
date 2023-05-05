title: OSWeb
hash: f4b6385f8676fac692cea87fc3795747281bf6498d80317d8a07196db11d38ee
locale: es
language: Spanish

[TOC]


## Acerca de OSWeb

OSWeb es un entorno de ejecución en línea para experimentos de OpenSesame. Es una biblioteca de JavaScript que interpreta y ejecuta experimentos de OpenSesame.


## La extensión OSWeb

La extensión OSWeb para OpenSesame (%FigOSWebExtension) te permite probar experimentos en un navegador y exportar experimentos en un formato que puedes importar en [JATOS](%url:jatos%).

%--
figure:
 id: FigOSWebExtension
 source: osweb-extension.png
 caption: La extensión OSWeb para OpenSesame.
--%


## Pruebas en un navegador

- En OpenSesame, abre la extensión OSWeb (Menú → Herramientas → OSWeb).
- La extensión realizará una comprobación simple (e incompleta) para ver si tu experimento parece ser compatible con OSWeb.
- Si no se detectan problemas, haz clic en 'Probar experimento en navegador externo' o haz clic en el botón correspondiente en la barra de herramientas principal.
- Esto abrirá el experimento en tu navegador predeterminado para que puedas verificar si el experimento se ejecuta como se esperaba (%FigTestRun).
- También puedes hacer clic en el botón 'Ejecutar en navegador' en la barra de herramientas principal (Alt+Ctrl+W)

%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: La pantalla de bienvenida de OSWeb al probar el experimento en un navegador.
--%


## Depuración

Primero, asegúrate de que tu experimento solo use la funcionalidad compatible, como se describe a continuación. A continuación, ejecuta el experimento en la forma tradicional (no en el navegador) en OpenSesame. Esto te dará los mensajes de error más informativos que puedes utilizar para la depuración.

Si tu experimento utiliza solo la funcionalidad compatible y se ejecuta normalmente en OpenSesame, entonces puedes usar la consola del navegador para ver los mensajes de error de JavaScript. Estos mensajes son mucho menos informativos que los mensajes de error de OpenSesame, pero aún pueden ser útiles. Cada navegador tiene una forma diferente de acceder a la consola. En Chrome, puedes acceder a la consola haciendo clic derecho en algún lugar, seleccionando Inspeccionar (`Ctrl+Shift+I`) y luego cambiando a la pestaña Consola (ver %FigChromeConsole). En Firefox, puedes acceder a la consola haciendo clic en el ícono del menú en la parte superior derecha y luego seleccionando Desarrollador web → Consola web (`Ctrl+Shift+I`).

Si estás utilizando elementos INLINE_JAVASCRIPT en tu experimento, la consola del navegador también es una forma poderosa de depurar tus scripts, como se describe aquí:

- %link:manual/javascript/about%

%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: La consola del navegador Chrome.
--%



## Funcionalidad compatible

Puedes verificar si tu experimento es compatible con OSWeb utilizando la Comprobación de compatibilidad (%FigOSWebExtension). Esta comprobación de compatibilidad es bastante superficial. A continuación, se muestra una descripción más completa de la funcionalidad compatible.

__Importante__: Se agregó mucha funcionalidad compatible en OSWeb 1.4. Por lo tanto, verifica tu versión de OSWeb con las notas de la versión en la lista a continuación.

- `advanced_delay`
- `feedback`
    - Ver `sketchpad`
- `form_consent` (compatible >= v1.4)
- `form_text_display` (compatible >= 1.4)
- `form_text_input` (compatible >= 1.4)
    - No compatible: modo de pantalla completa
- `form_multiple_choice` (compatible >= 1.4)
- `inline_html` (compatible >= 1.4)
- `inline_javascript`
- `keyboard`
    - No compatible: liberación de teclas
    - No compatible: espacios de color HSV, HSL y CIELab
- `logger`
- `loop`
    - No compatible: reanudar después de una pausa
    - No compatible: Desactivación de evaluación en el primer ciclo
    - No compatible: restricciones (seudorandomización)
    - Compatible >= 1.4: fuente de archivo
- `mouse`
    - No compatible: liberación del mouse
    - No compatible: sketchpad vinculado
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Compatible >= 1.4.12: panorámica, tono y desvanecimiento de entrada
    - Compatible >= 1.4.12: Reproducción de sonido en Safari en Mac OS o cualquier navegador en iOS
    - No compatible: detener después de
- `sequence`
- `sketchpad`
    - No compatible: elementos nombrados
    - Compatible >= 1.4: rotación de imágenes
    - No compatible: espacios de color HSV, HSL y CIELab
- `touch_response`

La verificación de compatibilidad también puede indicar errores del siguiente tipo:

```bash
La fase de preparación para el elemento new_logger se llama varias veces seguidas
La fase de ejecución para el elemento new_logger se llama varias veces seguidas
```

Este error es resultado de cómo está estructurado el experimento y, específicamente, del uso de copias vinculadas. No siempre es fácil entender de dónde proviene este error, pero puedes leer más sobre la estrategia de preparación-ejecución en [este artículo](%url:prepare-run%). Como solución alternativa, puedes colocar los elementos problemáticos en un LOOP ficticio, es decir, un LOOP que simplemente llama al elemento una vez.

## Navegadores soportados

Las siguientes combinaciones de navegador y sistemas operativos han sido probadas con la última versión de OSWeb. Versiones anteriores de navegadores, sistemas operativos y versiones de OSWeb pueden funcionar, pero no han sido sometidas a pruebas recientes. Algunas extensiones, como bloqueadores de anuncios o bloqueadores de scripts, pueden impedir que se ejecute OSWeb.

### Completamente soportado

- Chrome >= 101 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Edge >= 101 (Windows 11, Mac OS Monterey)
- Firefox >= 99 (Windows 11, Mac OS Monterey, Ubuntu 22.04, Android 12.0)
- Opera >= 86 (Windows 11) 
- Chromium >= 101 (iOS 15.2)
- Firefox >= 99 (iOS 15.2)
- Opera >= 86 (Mac OS Monterey) 
- Safari >= 15 (iOS 15.2, Mac OS Monterey)

### No soportado

- Internet Explorer >= 11 (Windows 10) 



## Actualizando OSWeb

OSWeb se encuentra en desarrollo activo. Si desea asegurarse de estar utilizando la última versión, puede actualizar la extensión OSWeb, que se llama `opensesame-extension-osweb`. A partir de OpenSesame 3.3, puedes hacer esto ejecutando el siguiente comando en la consola:

```bash
conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

O:

```bash
pip install --pre opensesame-extension-osweb --upgrade
```

Ver también:

- <https://rapunzel.cogsci.nl/manual/environment/>


## Incluir paquetes externos de JavaScript

Nuevo en OSWeb v1.4.6.1
{:.page-notification}

Puedes incluir paquetes externos de JavaScript ingresando las URL de estos paquetes (una URL por línea) en el campo de entrada etiquetado como 'Bibliotecas externas de JavaScript'. Estos paquetes se incluirán con etiquetas `<script>` en el encabezado del HTML.

Por ejemplo, puedes incluir [WebGazer](%url:webgazer%) para navegadores ingresando el siguiente enlace:

```
https://webgazer.cs.brown.edu/webgazer.js
```