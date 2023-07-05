title: OSWeb
hash: d0eed8ce85e569f15d774ecf9cc4dff90b02dffd12470987bae00484d0c05865
locale: es
language: Spanish

[TOC]


## Acerca de OSWeb

OSWeb es un entorno de ejecución en línea para experimentos de OpenSesame. Es una biblioteca de JavaScript que ejecuta experimentos de OpenSesame en un navegador. Para usar OSWeb, necesitas el paquete `opensesame-extension-osweb`, que viene preinstalado con las distribuciones de Windows y macOS de OpenSesame.


## Ejecutando un experimento en un navegador web

Para ejecutar un experimento en un navegador web usando OSWeb, sigue estos pasos:

1. Abre las Propiedades del Experimento y selecciona 'En un navegador con OSWeb (osweb)' en la sección 'Ejecutar experimento'.
2. Haz clic en cualquiera de los botones 'Ejecutar' para comenzar el experimento.
3. Si el experimento no es compatible con OSWeb, aparecerá un mensaje de error que detalla los problemas de compatibilidad. (Consulta la sección 'funcionalidad soportada' para más detalles.)
4. Si no hay problemas de compatibilidad, el experimento se abrirá en una nueva ventana del navegador. Ten en cuenta que, aunque el experimento se esté ejecutando en un navegador web, aún se ejecuta localmente en tu propia computadora. Para alojar el experimento en línea, necesitas publicarlo en [JATOS](%url:jatos%).
5. Cuando el experimento finaliza, los datos se descargarán en formato `.json`. Este archivo de datos puede ser [convertido a formato `.xlsx` o `.csv`](%url:manual/osweb/data%) para su posterior análisis.


%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: Abre las Propiedades del Experimento y selecciona 'En un navegador con OSWeb (osweb)' en 'Ejecutar experimento'.
--%


## Panel de control OSWeb

Para tener más control sobre los experimentos de OSWeb, puedes acceder al panel de control de OSWeb y JATOS desde el menú de herramientas. Este panel ofrece una serie de opciones de configuración:

- **Números de sujeto posibles:** Cuando ejecutas un experimento desde JATOS, un número de sujeto se selecciona aleatoriamente de esta lista. Puedes especificar números individuales usando comas (por ejemplo, '1,2,3') o rangos de números (por ejemplo, '1-10'). Cuando ejecutas un experimento desde OpenSesame, esta opción no se aplica, ya que el número de sujeto se especifica cuando comienza el experimento.
- **Hacer navegador a pantalla completa:** Esta opción determina si el navegador debería cambiar al modo de pantalla completa cuando un experimento comienza dentro de JATOS. Si estás ejecutando un experimento directamente desde OpenSesame, esta opción se ignora; en lugar de ello, puedes ejecutar el experimento a pantalla completa utilizando el botón de ejecución regular, mientras que el botón de ejecución rápida no permite screen.
- **Mostrar pantalla de bienvenida de OSWeb:** Este interruptor controla si los participantes verán una pantalla de bienvenida antes de que comience el experimento. La pantalla de bienvenida puede transmitir información crucial a los participantes. Además, cumple una finalidad técnica: debido a las políticas de seguridad del navegador, la reproducción de medios y ciertas funcionalidades sólo están disponibles si el experimento es iniciado por una acción del usuario. Por lo tanto, generalmente se recomienda dejar esta opción habilitada.
- **Evitar la verificación de compatibilidad:** Habilitar esta opción te permite ejecutar el experimento incluso cuando la verificación de compatibilidad de OSWeb falla. Ten en cuenta que hacerlo no solucionará automáticamente los problemas de compatibilidad!
- **Texto de bienvenida:** Este campo te permite personalizar el mensaje de bienvenida que se muestra a los participantes en la pantalla de bienvenida.
- **Bibliotecas externas:** Este campo te permite especificar cualquier biblioteca externa que deba cargarse con tu experimento. El uso de bibliotecas externas se explica con más detalle en la sección de abajo.


%--
figure:
 id: FigOSWebControlPanel
 source: osweb-control-panel.png
 caption: El panel de control de OSWeb y JATOS ofrece una serie de opciones de configuración para tus experimentos de OSWeb.
--%


## Funcionalidad soportada

Cuando ejecutas el experimento desde OpenSesame, se realiza automáticamente una verificación de compatibilidad. Sin embargo, esta verificación es bastante superficial. A continuación, puedes encontrar una visión más completa de la funcionalidad soportada.

- `advanced_delay`
- `feedback`
    - Ver `sketchpad`
- `form_consent` (compatible >= v1.4)
- `form_text_display` (compatible >= 1.4)
- `form_text_input` (compatible >= 1.4)
    - No compatible: modo pantalla completa
- `form_multiple_choice` (compatible >= 1.4)
- `inline_html` (compatible >= 1.4)
- `inline_javascript`
- `keyboard`
    - No compatible: liberación de tecla
    - No compatible: espacios de color HSV, HSL y CIELab
- `logger`
- `loop`
    - No compatible: reanudar después de una pausa
    - No compatible: deshabilitación de la evaluación en el primer ciclo
    - No compatible: restricciones (pseudorandomización)
    - Compatible >= 1.4: fuente de archivo
- `mouse`
    - No compatible: liberación del mouse
    - No compatible: sketchpad vinculado
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Compatible >= 1.4.12: paneo, tono y entrada gradual
    - Compatible >= 1.4.12: reproducción de sonido en Safari en Mac OS o cualquier navegador en iOS
    - No compatible: detener después 
- `sequence`
- `sketchpad`
    - No compatible: elementos nombrados
    - Compatible >= 1.4: rotación de imagen
    - No compatible: espacios de color HSV, HSL y CIELab
- `touch_response`

La comprobación de compatibilidad también puede indicar errores del siguiente tipo:

> La fase de preparación para el elemento new_logger se llama varias veces seguidas

Este error resulta de cómo está estructurado el experimento, y específicamente del uso de copias vinculadas. No siempre es fácil entender de dónde proviene este error, pero puedes leer más sobre la estrategia de preparación-ejecución en [este artículo](%url:prepare-run%). Como solución alternativa, puedes poner los elementos problemáticos en un loop ficticio, es decir, un LOOP que simplemente llama al elemento una vez.

## Inclusión de paquetes JavaScript externos

Puede incluir paquetes JavaScript externos ingresando las URL a estos paquetes (una URL por línea) en el campo de entrada etiquetado como 'Bibliotecas JavaScript externas'. Estos paquetes se incluyen luego con etiquetas `<script>` en el encabezado del HTML.

Por ejemplo, puedes incluir [WebGazer](%url:webgazer%) para el navegador ingresando el siguiente enlace:

```
https://webgazer.cs.brown.edu/webgazer.js
```

## Depuración

Ver:

- %link:debugging%