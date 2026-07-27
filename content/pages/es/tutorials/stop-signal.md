title: Tarea de señal de parada (trabajando con coroutines)
hash: a90dc175aa27f6f7bdfc95ae0c91f7aa1f0aacaeeac9a505a63772d5a363d5d5
locale: es
language: Spanish

[TOC]

## Acerca de OpenSesame

OpenSesame es un programa fácil de usar para el desarrollo de experimentos conductuales para psicología, neurociencia y economía experimental. Para principiantes, OpenSesame cuenta con una interfaz gráfica completa de apuntar y hacer clic. Para usuarios avanzados, OpenSesame es compatible con Python (solo escritorio) y JavaScript (escritorio y navegador).

OpenSesame está disponible gratuitamente bajo la [General Public License v3][gpl].

## Acerca de este tutorial

Este tutorial muestra cómo crear una tarea stop-signal en OpenSesame usando el plugin `coroutines`. El experimento se basa en la versión de tiempo de reacción simple de [Logan, Cowan and Davis (1984)][references]. El objetivo principal de este tutorial no es solo construir la tarea, sino también comprender cómo coroutines permiten situar varios eventos en una sola línea temporal de ensayo.

## Recursos

- __Descarga__ — Este tutorial asume que está ejecutando OpenSesame versión 4.1 o posterior, y que está ejecutando el experimento en el escritorio. Puede descargar la versión más reciente de OpenSesame desde:
	- <https://osdoc.cogsci.nl/4.1/download/>
- __Documentación__ — Puede encontrarse un sitio web de documentación dedicado en:
	- <http://osdoc.cogsci.nl/>
- __Foro__ — Puede encontrarse un foro de soporte en:
	- <http://forum.cogsci.nl/>
- __Sigmund__ — SigmundAI es un asistente de IA con conocimiento experto de OpenSesame y puede encontrarse en:
	- <https://sigmundai.eu/>

## El experimento

En este experimento, los participantes responden lo más rápido posible a las letras que aparecen en la pantalla. En la mayoría de los ensayos, deben pulsar la barra espaciadora cuando aparece una letra. En algunos ensayos, se reproduce un tono poco después de que aparezca la letra, y los participantes deben intentar inhibir su respuesta. El objetivo de la tarea es estimar el tiempo de reacción de la señal de parada (SSRT), una medida latente de la velocidad del proceso inhibitorio. La estimación fiable del SSRT requiere que los participantes respondan rápidamente en los ensayos go e intenten inhibir su respuesta solo cuando se presenta la señal de parada.

El experimento usa cuatro letras: `E`, `F`, `H` y `L`. La respuesta es siempre la misma, independientemente de qué letra se muestre. Esto hace que la tarea sea una versión de tiempo de reacción simple del paradigma stop-signal.

Cada ensayo tiene la siguiente estructura:

- Se muestra un punto de fijación durante 500 ms.
- Se muestra una letra después de la fijación.
- Se abre una ventana de respuesta cuando aparece la letra.
- En los ensayos stop, se reproduce un tono de 900 Hz tras un breve retraso.
- Una máscara sigue a la letra.
- La duración total del ensayo se fija en 3500 ms.

%--
figure:
 id: Fig_paradigm
 source: stop_paradigm.png
 caption: A schematic overview of the stop-signal paradigm implemented in this tutorial.
--%

Tareas como esta generalmente muestran que es menos probable que los participantes inhiban su respuesta cuando el retraso de la señal de parada es largo que cuando es corto. Los participantes pueden a veces ralentizarse estratégicamente si esperan una señal de parada. Por esta razón, las instrucciones deben enfatizar que los participantes deben responder rápidamente y no deben esperar el tono.

## Diseño experimental

Este diseño:

- es intrasujeto, porque todos los participantes completan todos los tipos de ensayo
- incluye ensayos go y ensayos stop
- incluye cuatro retrasos de señal de parada en los ensayos stop:
	- `50`
	- `100`
	- `150`
	- `200`
- incluye cuatro letras:
	- `E`
	- `F`
	- `H`
	- `L`

La tabla del loop contiene 80 filas y se repite cuatro veces, lo que da como resultado cuatro bloques de 80 ensayos.

Ahora construiremos el experimento paso a paso.

## Paso 1: Crear la estructura básica del experimento

Inicie OpenSesame y cree un experimento nuevo. En este tutorial, la secuencia principal se llama `experiment` y contiene:

- `new_form_consent`
- `instructions`
- `simple_rt`

El elemento `simple_rt` es un loop que contiene la estructura de ensayo del experimento.

El área de vista general ahora debería verse así:

%--
figure:
 id: Fig_overview
 source: stop_overview.png
 caption: The overview area of the stop-signal experiment.
--%

## Paso 2: Añadir un formulario de consentimiento y una pantalla de instrucciones

El experimento de ejemplo comienza con un formulario de consentimiento. Esto es opcional desde un punto de vista técnico, pero en muchos experimentos reales es útil o necesario pedir a los participantes su consentimiento informado antes de que comience la tarea.

Después del formulario de consentimiento, los participantes ven una pantalla de instrucciones. Las instrucciones explican que los participantes deben pulsar la barra espaciadora cada vez que aparezca una letra, pero intentar retener la respuesta cuando oigan el tono de stop. Las instrucciones también deben enfatizar que los participantes no deben esperar al tono antes de responder.

El elemento de instrucciones puede verse así:

%--
figure:
 id: Fig_instructions
 source: stop_instructions.png
 caption: The instruction screen shown before the experiment starts.
--%

## Paso 3: Crear el loop de ensayos

La estructura de los ensayos se define en un loop llamado `simple_rt`. Este loop contiene 80 filas y se repite cuatro veces. El orden de los ensayos se aleatoriza dentro de cada repetición.

Cada fila define al menos las siguientes variables:

- `letters`
- `is_stop`
- `delay`
- `correct_response`

Para los ensayos go:

- `is_stop` es `no`
- `delay` es `0`
- `correct_response` es `space`

Para los ensayos stop:

- `is_stop` es `yes`
- `delay` es uno de `50`, `100`, `150` o `200`
- `correct_response` es `None`

Esta es una forma práctica de usar la puntuación incorporada del elemento `keyboard_response`. En los ensayos go, pulsar espacio es correcto. En los ensayos stop, retener la respuesta es correcto porque la respuesta correcta se define como `None`.

La tabla del loop debe verse así:

%--
figure:
 id: Fig_loop
 source: stop_loop.png
 caption: The loop table that defines go trials and stop trials.
--%

## Paso 4: Crear los elementos del ensayo

La coroutine usa varios elementos que primero deben crearse por separado.

### 4.1 Fijación

Inserta un nuevo sketchpad y cámbiale el nombre a `fixation`. Dibuja en él un punto de fijación central. Aunque los sketchpads tienen su propia configuración de duración, más adelante la temporización de este elemento será controlada por la coroutine.

### 4.2 Presentación de la letra

Inserta un nuevo sketchpad y cámbiale el nombre a `letter`. Añade un elemento de texto que muestre el valor de la variable `{letters}`, de modo que la letra mostrada cambie de un ensayo a otro. Las llaves alrededor de `{letters}` indican que esto no es texto literal, sino el valor de la variable experimental `letters`, que está definida en la tabla del loop.

El sketchpad de la letra debe verse así:

%--
figure:
 id: Fig_letter
 source: stop_letter.png
 caption: The letter sketchpad, which shows the value of the variable `letters`.
--%

### 4.3 Máscara

Inserta un nuevo sketchpad y cámbiale el nombre a `mask`. En el experimento actual este sketchpad está vacío, por lo que funciona principalmente como un marcador de posición en la cronología del ensayo. Al igual que con los otros sketchpads, su temporización efectiva será determinada más adelante por la coroutine.

### 4.4 Elemento de respuesta

Inserta un nuevo elemento `keyboard_response` y cámbiale el nombre a `resp_simple_rt`. Establece la respuesta permitida en `space`. Cuando este elemento se usa dentro de la coroutine, la ventana de respuesta será controlada por la cronología de la coroutine en lugar de por la propia configuración de tiempo de espera del elemento.

La configuración de keyboard response debe verse así:

%--
figure:
 id: Fig_keyboard
 source: stop_keyboard.png
 caption: The keyboard response item configured to collect a spacebar response.
--%

### 4.5 Señal de stop

Inserta un nuevo elemento `synth` y cámbiale el nombre a `stop_signal`. Establece:

- waveform en `sine`
- frequency en `900`
- length en `500`
- duration en `0`

Una duración de `0` garantiza que el sonido comience y que la coroutine continúe inmediatamente, en lugar de esperar a que el sonido termine.

%--
figure:
 id: Fig_synth
 source: stop_synth.png
 caption: The synth item configured to produce a 900-Hz tone lasting 500 ms.
--%

### 4.6 Logger

Inserte un nuevo elemento `logger` y cámbiele el nombre a `logger`. Desactive el registro automático y registre manualmente las variables críticas. En particular, asegúrese de que se incluyan variables como `letters`, `is_stop`, `delay`, `response`, `response_time` y `correct`.

La configuración de logger debería verse así:

%--
figure:
 id: Fig_logger
 source: stop_logger.png
 caption: The logger item configured to log the critical stop-signal variables.
--%

## Paso 5: Añadir el elemento coroutine

Ahora inserte un elemento `coroutines` y cámbiele el nombre a `coroutines`. Este elemento definirá la temporización de cada ensayo en una línea temporal compartida.

Establezca la duración total de la coroutine en `3500` y añada los elementos del ensayo para que se coloquen en la misma línea temporal del ensayo.

En esta etapa, es importante tener en cuenta que no todos los elementos de OpenSesame pueden usarse dentro de una coroutine. Los elementos compatibles incluyen al menos:

- `feedback`
- `inline_script`
- `keyboard_response`
- `logger`
- `mouse_response`
- `sampler`
- `synth`
- `sketchpad`

Si un elemento no es compatible con coroutines, no puede colocarse en la línea temporal compartida de la coroutine.

## Paso 6: Configurar el elemento coroutines

El elemento `coroutines` es el núcleo temporal del experimento. Permite coordinar múltiples eventos del ensayo en una sola línea temporal, de modo que la presentación, la recogida de respuestas y la programación del sonido puedan solaparse en el tiempo.

Esto es especialmente útil para la tarea stop-signal. La pantalla de fijación aparece primero, la letra aparece más tarde, el participante puede responder mientras el ensayo continúa, y el tono de stop se presenta solo en algunos ensayos y solo después de un retraso variable. Un elemento sequence normal no se adapta bien a este tipo de solapamiento temporal, mientras que una coroutine está diseñada exactamente para este propósito.

### 6.1 La línea temporal de la coroutine

En este experimento:

- `fixation` comienza en `0`
- `letter` comienza en `500`
- `resp_simple_rt` comienza en `500`
- `mask` comienza en `1000`
- `stop_signal` comienza en `{delay + 500}` solo en los ensayos stop
- `logger` se ejecuta al final del ensayo

El valor de `delay` proviene de la tabla del loop. Como la letra aparece a los `500` ms, la expresión `{delay + 500}` programa la señal stop en relación con el inicio de la letra, en lugar de en relación con el comienzo de todo el ensayo.

### 6.2 Cómo funcionan `start`, `end` y `run_if`

Cada fila en una coroutine especifica cuándo debe ejecutarse un elemento y, en algunos casos, cuándo debe detenerse.

- `start` indica cuándo comienza el elemento, en milisegundos después del inicio de la coroutine.
- `end` indica cuándo se detiene el elemento, si el elemento permanece activo durante un intervalo.
- `run_if` indica si el elemento debe ejecutarse o no.

Esto significa que la coroutine hace más que simplemente enumerar elementos. Define una línea temporal y coloca cada elemento en esa línea temporal.

Por ejemplo:

- `letter` comienza en `500`, lo que significa que la letra aparece 500 ms después del comienzo del ensayo.
- `resp_simple_rt` también comienza en `500`, lo que significa que la recogida de respuestas comienza cuando aparece la letra.
- `stop_signal` usa una condición `run_if` para que solo se reproduzca en los ensayos stop.

Una expresión `run_if` típica para la señal stop es:

`is_stop == "yes"`

Esta expresión se evalúa para cada ensayo. En los ensayos stop, se ejecuta el elemento synth. En los ensayos go, se omite.

### 6.3 Cuándo es aplicable `end`

No todos los elementos en una coroutine usan `end` de la misma manera.

Algunos elementos son, de hecho, elementos de una sola ejecución. Un sketchpad, por ejemplo, prepara una pantalla y la muestra cuando se inicia. En la práctica, la configuración importante para ese tipo de elemento suele ser el momento de `start`. El cambio de pantalla ocurre en ese momento, y el propio sketchpad no necesita permanecer activo de la misma manera que un elemento de respuesta o un elemento de sonido.

Otros elementos sí permanecen activos durante un período de tiempo. Un `keyboard_response`, por ejemplo, puede permanecer activo durante una ventana de respuesta, y un elemento de sonido puede permanecer activo mientras se reproduce el audio. Para estos elementos, `end` es significativo porque determina cuándo el elemento deja de estar activo en la línea temporal de la coroutine.

Así que, en general:

- `start` es relevante para todos los elementos
- `end` es principalmente relevante para los elementos que permanecen activos durante un intervalo
- `run_if` es relevante siempre que un elemento deba ejecutarse solo bajo ciertas condiciones

### 6.4 Cómo se aplica esto a la tarea stop-signal

En el experimento actual:

- `fixation`, `letter` y `mask` se usan principalmente para actualizar la pantalla en momentos específicos
- `resp_simple_rt` permanece activo durante la ventana de respuesta
- `stop_signal` se inicia solo cuando `is_stop == "yes"`
- `logger` se ejecuta al final del ensayo

Esto significa que los sketchpads dependen principalmente de sus tiempos de `start`, mientras que el elemento de respuesta y el elemento stop-signal se entienden mejor como elementos que están activos durante una parte de la línea temporal del ensayo.

### 6.5 Cómo se relaciona la duración de los elementos con la temporización de la coroutine

Al trabajar con coroutines, es importante recordar que la coroutine controla cuándo los elementos están activos. En otras palabras, la temporización efectiva está determinada por la configuración de `start`, `end` y `run_if` de la coroutine, no principalmente por la configuración de duración o timeout dentro de los elementos individuales.

Por eso los sketchpads de este experimento no necesitan sus propias duraciones para definir la estructura del ensayo. Su papel en la línea temporal está determinado por la coroutine. La misma lógica se aplica al `keyboard_response`: aunque el elemento tenga su propia configuración de timeout, la ventana de respuesta queda definida efectivamente por la línea temporal de la coroutine.

El synth `stop_signal` ilustra esto claramente. Sus propiedades de sonido, como la forma de onda y la duración, se definen en el propio elemento synth, pero el momento en que comienza está definido por la coroutine.

### 6.6 Por qué el synth stop-signal usa `duration = 0`

El elemento `stop_signal` tiene una duración de sonido de 500 ms y una duración de `0`. Esto es importante porque significa que el sonido comienza y la coroutine continúa inmediatamente, en lugar de esperar a que el sonido termine.

Como resultado, el tono puede reproducirse mientras continúa el resto de la línea temporal de la coroutine. Esto es exactamente lo que se necesita en una tarea stop-signal: la señal debe ocurrir en un momento preciso, pero no debe pausar la recogida de respuestas ni el resto del ensayo.

La configuración de la coroutine debería verse así:

%--
figure:
 id: Fig_coroutines
 source: stop_coroutines.png
 caption: The coroutine item that controls the shared trial timeline.
--%

### 6.7 Por qué el logger se coloca en `3400`

En el experimento de ejemplo, la duración total de la coroutine es de `3500` ms, pero tanto `resp_simple_rt` como `logger` están configurados en `3400`. Esto significa que la ventana de respuesta se cierra a los `3400` ms y el ensayo se registra en ese mismo punto, en lugar de hacerlo al final de la coroutine.

Esto es útil porque garantiza que la recogida de respuestas no continúe más allá del momento en que se registra el ensayo. Al mismo tiempo, los `100` ms finales de la coroutine permanecen sin usarse como un pequeño margen de seguridad antes de que la propia coroutine termine.

En la práctica, esto significa que cuando se ejecuta el logger, las variables de respuesta relevantes, como `response`, `response_time` y `correct`, ya se han establecido.

## Paso 7: Probar el experimento

Cuando la estructura del experimento esté completa, pruébalo y verifica que:

- el punto de fijación aparezca primero
- la letra aparezca después de 500 ms
- la ventana de respuesta se abra con el inicio de la letra
- el tono stop se reproduzca solo en los ensayos stop
- la temporización del tono stop dependa de `delay`
- la duración del ensayo sea siempre de 3500 ms

También es útil inspeccionar el archivo de registro para comprobar que `letters`, `is_stop`, `delay`, `response`, `response_time` y `correct` se almacenan correctamente.

## Finalizado

Enhorabuena, el experimento está completo. Ahora puedes hacer una prueba pulsando el botón azul de doble flecha (atajo: `Ctrl+W`).

A continuación se muestra una demostración de una versión abreviada del experimento creada con fines tutoriales.

<video controls width ="100%"> 
    <source src="/video/stop_demo.mp4" type="video/mp4">
</video>
<p align="center"><em>Vídeo 1. Demostración de la tarea stop-signal completada.</em></p>

## Referencias

Logan, G. D., Cowan, W. B., & Davis, K. A. (1984). On the ability to inhibit simple and choice reaction time responses: A model and a method. *Journal of Experimental Psychology: Human Perception and Performance*, *10*(2), 276–291.

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314–324.

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html