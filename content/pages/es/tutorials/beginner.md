title: Tutorial para principiantes: direccionamiento de la mirada
hash: 1bc0db6f02f63201f3d90855479f82e8a246736a8141fb744439c06fe8783002
locale: es
language: Spanish

## Sobre OpenSesame

OpenSesame es un programa gratuito para el desarrollo rápido de experimentos conductuales en psicología, neurociencia cognitiva y economía experimental. Para principiantes, OpenSesame cuenta con una interfaz gráfica integral y de apuntar y hacer clic. Para usuarios avanzados, OpenSesame admite la programación en Python y JavaScript (no cubierto en este tutorial).

## Sobre este tutorial

Crearemos un experimento clásico de dirección de mirada. Este es un paradigma divertido e interesante, donde las personas no pueden evitar seguir hacia dónde mira una cara.

Solamente usaremos la interfaz gráfica. *No* utilizaremos programación en Python ni JavaScript. (Esto se cubre en los tutoriales intermedios). Este tutorial toma aproximadamente una hora.

## Lo que aprenderás

Al finalizar este tutorial, sabrás cómo:

- 💡 Construir la estructura de un experimento con elementos SEQUENCE y LOOP
- 💡 Definir un diseño factorial completo con variables independientes en una tabla LOOP
- 💡 Crear estímulos visuales con elementos SKETCHPAD
- 💡 Recoger respuestas con elementos KEYBOARD_RESPONSE
- 💡 Proporcionar retroalimentación a los participantes con elementos FEEDBACK
- 💡 Mostrar texto usando elementos FORM_TEXT_DISPLAY
- 💡 Utilizar variables para definir tus estímulos
- 💡 Usar expresiones condicionales (run-if) para controlar el flujo de tu experimento
- 💡 Organizar los archivos de estímulos en el file pool
- 💡 Registrar datos

## Lo que necesitarás

**OpenSesame 4.1 o posterior** con todas las actualizaciones instaladas. Si ves una notificación sobre actualizaciones disponibles, haz clic en "Install updates..." y luego en "Run update script." Reinicia OpenSesame después de actualizar. También puedes actualizar manualmente ejecutando el siguiente comando en la consola de OpenSesame.

```bash
pip install opensesame-core opensesame-extension-sigmund --upgrade
```

## El experimento

Como se mencionó, crearemos un experimento de dirección de mirada, desarrollado originalmente por [Friesen y Kingstone (1998)][references]. Así funciona:

1. Una cara aparece en el centro de la pantalla
2. La cara mira hacia la izquierda o hacia la derecha
3. Una letra objetivo ('F' o 'H') aparece en un lado
4. Una letra distractora ('X') aparece en el otro lado
5. Los participantes identifican la letra objetivo lo más rápido posible

El experimento tiene una fase de práctica y una fase experimental. Mostrarás retroalimentación después de cada bloque. Un sonido suena tras respuestas incorrectas.

¿El hallazgo interesante? Las personas son más rápidas cuando la cara mira hacia el objetivo, aunque la dirección de la mirada no predice dónde aparecerá el objetivo. Esto muestra que los humanos siguen automáticamente hacia donde otros están mirando.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  The gaze-cuing paradigm [(Friesen and Kingstone, 1998)][references]. This example shows an **incongruent** trial, because the face looks at the distractor ('X') instead of the target ('F').
--%

%--
video:
 source: youtube
 id: DesignScreencast
 videoid: aWvibRH6D4E
 width: 640
 height: 360
 caption: |
  Experimental logic and design.
--%

## Paso 1: Crea la secuencia principal

🎯 __Objetivo:__ En este paso, crearemos la estructura básica de nuestro experimento: una fase de práctica, durante la cual los participantes podrán practicar la tarea; una fase experimental, durante la cual recogeremos datos para el análisis; y pantallas informativas antes y después de estas fases. Solo estableceremos la estructura. Los detalles se implementarán después.

Cuando inicies OpenSesame, aparecerá la pestaña ‘¡Comencemos!’ (%FigGetStarted). Elige “Default template”.

%--
figure:
 id: FigGetStarted
 source: get-started.png
 caption: |
  The ‘Get started’ panel on OpenSesame start-up.
--%

Abre la SEQUENCE principal llamada *experiment*. Contiene dos elementos por defecto: un notepad (*getting_started*) y un SKETCHPAD (*welcome*).

<details class='info-box' markdown='1'>

<summary markdown='1'>Consejos útiles para este tutorial</summary>

- Haz clic en el icono de Ayuda en la pestaña de cualquier elemento para obtener ayuda contextual.
- Guarda con frecuencia (Ctrl+S). Las copias de seguridad se crean automáticamente (Herramientas → Abrir carpeta de copias de seguridad).
- Los elementos eliminados se pueden recuperar desde "Elementos no usados" a menos que se eliminen permanentemente (Shift+Del).
- Consulta la figura abajo para ver la estructura que construiremos.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  Structure of the gaze-cuing experiment. Item types in bold, item names regular.
--%

</details>

Elimina los elementos predeterminados:

- Haz clic derecho en *getting_started* → Eliminar
- Haz clic derecho en *welcome* → Eliminar

La SECUENCIA *experiment* ahora está vacía. Agrega un formulario para las instrucciones:

- Arrastra un FORM_TEXT_DISPLAY desde la barra de herramientas (Form) a *experiment*. Esto mostrará las instrucciones al inicio (definiremos las instrucciones reales en el Paso 12).

Agrega un LOOP con una SECUENCIA para la fase de práctica:

- Arrastra un LOOP a *experiment* (colócalo después del formulario de instrucciones).
- Arrastra una SECUENCIA dentro del LOOP y elige "Insertar en [nombre del elemento loop]".

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre la estructura LOOP/ SEQUENCE</summary>

A menudo repites una secuencia de eventos, como un ensayo. Esto se implementa típicamente combinando un LOOP, que repite un solo elemento, y una SECUENCIA, que ejecuta varios elementos en orden.

Ejemplo: Un *block_loop* contiene un *trial_sequence*, que a su vez contiene múltiples elementos correspondientes a un ensayo. Juntos, esta estructura LOOP/ SEQUENCE corresponde a un solo bloque de múltiples ensayos.

</details>

Agrega un formulario al final de la práctica

- En *experiment*, arrastra otro FORM_TEXT_DISPLAY y elige "Insertar después de [nombre del elemento practice loop]". Esto mostrará un mensaje de "fin de práctica" (Paso 12).

Agrega un LOOP para la fase experimental, reutilizando una copia vinculada de la misma SECUENCIA que usaste para el LOOP de práctica:

- Arrastra un LOOP y colócalo después del formulario de fin de práctica.
- Reutiliza la SECUENCIA que creaste para el LOOP de práctica:
  - Haz clic derecho en la SECUENCIA existente > Copiar (vinculado).
  - Haz clic derecho en el nuevo LOOP experimental > Pegar > "Insertar en [loop experimental]".

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre copias vinculadas vs. no vinculadas</summary>

Cuando el mismo elemento exacto aparece en varios lugares, se llaman copias vinculadas. Las copias vinculadas son convenientes, porque si deseas cambiar el elemento, solo necesitas hacerlo una vez.

Las copias no vinculadas son independientes entre sí, de modo que puedes cambiar una sin afectar las otras.

¡Es una buena práctica usar copias vinculadas siempre que sea posible!

</details>

Agrega un formulario de despedida:

- Arrastra un FORM_TEXT_DISPLAY e insértalo después del loop experimental.

Renombra los elementos para mayor claridad:

- new_form_text_display → *instructions*
- new_loop → *practice_loop*
- new_sequence → *block_sequence* (las copias vinculadas se actualizan automáticamente)
- new_form_text_display_1 → *end_of_practice*
- new_loop_1 → *experimental_loop*
- new_form_text_display_2 → *end_of_experiment*

Renombra el experimento:

- Haz clic en New experiment en la vista general. Renombra como “Tutorial: Gaze cuing”. Luego guarda (Ctrl+S).

%--
figure:
 id: FigStep_1
 source: step1.png
 caption: |
  Overview at the end of Step 1.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre los diferentes tipos de elementos</summary>

- SEQUENCE: Ejecuta elementos en orden.
- LOOP: Repite otro elemento, a menudo una SEQUENCE, y define las variables independientes.
- SKETCHPAD: Presenta estímulos visuales. Se prepara con anticipación, por lo que es adecuado para estímulos que requieren temporización precisa.
- FEEDBACK: Presenta estímulos visuales. No se prepara con anticipación, por lo que es adecuado para presentar contenido actualizado, como retroalimentación sobre las respuestas de un participante.
- KEYBOARD_RESPONSE: Recoge una sola respuesta mediante pulsación de tecla.
- SAMPLER: Reproduce un sonido desde un archivo.
- LOGGER: Escribe datos en un archivo.
- RESET_FEEDBACK: Restablece las variables de retroalimentación al inicio de un bloque.
- FORM_TEXT_DISPLAY: Muestra texto usando un diseño de formulario.

</details>

## Paso 2: Crea la secuencia de bloque

🎯 __Objetivo:__ En este paso, nuevamente añadiremos estructura a nuestro experimento. Esta vez implementaremos la estructura para un solo bloque de ensayos, que corresponde a *block_sequence*. Solo estableceremos la estructura. Los detalles se implementarán más adelante.

Abre *block_sequence* y añade los siguientes elementos en orden:

- RESET_FEEDBACK (para restablecer las variables de retroalimentación al inicio del bloque)
- LOOP con una nueva SEQUENCE insertada (para manejar la lógica real del bucle y el ensayo)
- FEEDBACK (para brindar retroalimentación al participante al final del bloque)

Renombra

- new_reset_feedback → *reset_feedback*
- new_loop → *block_loop*
- new_sequence → *trial_sequence*
- new_feedback → *feedback*

%--
figure:
 id: FigStep_2
 source: step2.png
 caption: |
  Overview at the end of Step 2.
--%


## Paso 3: Llena el block loop con variables independientes

🎯 __Objetivo:__ En este paso, definiremos las variables independientes (condiciones) de nuestro experimento. Nuestro experimento es un ejemplo de diseño completamente aleatorizado, lo que significa que las variables independientes varían de un ensayo a otro.

Abre *block_loop*. Haz clic en Full-factorial design. Define:

- `gaze_cue`: left, right
- `target_pos`: -300, 300 (coordenada x en píxeles; 0 = centro; negativo = izquierda)
- `target_letter`: F, H

Esto crea 2×2×2 = 8 combinaciones. También necesitamos definir varias variables que se derivan de las anteriores. Para esto, necesitas agregar manualmente una columna para cada variable e ingresar los valores correctos en cada celda.

- `dist_pos`: Para cada fila, pon 300 si `target_pos` es -300, y -300 si `target_pos` es 300
- `correct_response`: z para F, m para H
- `congruency`: congruente si la dirección de la mirada apunta hacia el objetivo, e incongruente de lo contrario

Asegúrate de que la tabla del loop tenga 8 filas. Luego pon Repetir en 3 para tener 3 × 8 = 24 ensayos por bloque.

%--
figure:
 id: FigStep_3
 source: step3.png
 caption: |
  The *block_loop* at the end of Step 3.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Más información sobre la tabla LOOP</summary>

- Puedes copiar y pegar una tabla desde una hoja de cálculo, o cargar un archivo .csv/.xlsx configurando Source como file.
- Repetir puede tener valores fraccionarios. Por ejemplo, si configuras repeat en 0.5, solo se ejecuta la mitad de las filas, seleccionadas al azar.

</details>


## Paso 4: Agrega imágenes y archivos de sonido al file pool

🎯 __Objetivo:__ En este paso, usaremos el file pool para agrupar archivos de estímulo (imágenes y un sonido) junto con el experimento.

Descarga los siguientes archivos:

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Abre el file pool (Ctrl+P) y arrastra los archivos dentro. O bien, usa el botón + para agregarlos. El file pool se agrupa automáticamente con tu experimento.

%--
figure:
 id: FigStep_4
 source: step4.png
 caption: |
  File pool at the end of Step 4.
--%

## Paso 5: Llena la trial sequence con elementos

🎯 __Objetivo:__ En este paso, definiremos la secuencia de ensayo. Por ahora, solo añadiremos los elementos necesarios sin definirlos. Lo haremos más adelante.

Un ensayo consiste en:

1. Punto de fijación — 750 ms — SKETCHPAD  
2. Mirada neutral — 750 ms — SKETCHPAD  
3. Señal de mirada — 500 ms — SKETCHPAD  
4. Objetivo — 0 ms — SKETCHPAD (la duración de 0 ms permite que el experimento avance de inmediato a la recolección de respuestas)  
5. Recolección de respuesta — KEYBOARD_RESPONSE  
6. Sonido incorrecto — SAMPLER (solo si es incorrecto)  
7. Registro — LOGGER  

Abre *trial_sequence* y los ítems en el orden indicado arriba. Cuando termines, renómbralos:

- *new_sketchpad* → *fixation_dot*
- *new_sketchpad_1* → *neutral_gaze*
- *new_sketchpad_2* → *gaze_cue*
- *new_sketchpad_3* → *target*
- *new_keyboard_response* → *keyboard_response*
- *new_sampler* → *incorrect_sound*
- *new_logger* → *logger*

En *trial_sequence*, configura run-if para *incorrect_sound* a: `correct == 0`. Es importante usar el doble signo igual (`==`), que verifica si dos valores son idénticos, en este caso si `correct` es igual a 0. (Si accidentalmente utilizas un solo signo igual, `correct = 1`, obtendrás un `SyntaxError` al ejecutar el experimento.)

%--
figure:
 id: FigStep_5
 source: step5.png
 caption: |
  *trial_sequence* al final del Paso 5.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre variables y expresiones condicionales (run-if)</summary>

¡Las variables y las expresiones condicionales (run-if) son poderosas! Consulta %link:manual/variables%

</details>


## Paso 6: Dibuja los ítems sketchpad

🎯 __Objetivo:__ En este paso, definiremos los cuatro ítems SKETCHPAD de la secuencia del ensayo: punto de fijación, mirada neutral (mirando al frente), señal de mirada (mirando a la izquierda o derecha) y pantalla de objetivo (dos letras a cada lado de la señal de mirada, que sigue mirando a la izquierda o derecha).

Configura el color de fondo del experimento a blanco y el color de primer plano a negro:

- Haz clic en el título del experimento para abrir las Propiedades generales
- Cambia Background a 'white' y Foreground a 'black'

Define el punto de fijación:

- Abre *fixation_dot*
- Selecciona el elemento fixdot. Este es el ícono del punto de fijación en la barra de herramientas vertical a la izquierda del lienzo.
- Dibuja un punto de fijación en el centro de la pantalla (0, 0)
- Configura la duración a 745 ms. Esto se redondeará a la duración deseada de 750 ms.

<details class='info-box' markdown='1'>

<summary markdown='1'>¿Por qué especificar una duración de 745 ms si quieres mostrar una pantalla por 750 ms?</summary>

Las pantallas se actualizan periódicamente. En un monitor de 60 Hz, un ciclo de actualización tarda 1000 / 60 = 16.67 ms. Esto significa que, en un monitor de 60 Hz, la duración de una pantalla debe ser necesariamente un múltiplo de 16.67.

745 *no* es un múltiplo de 16.67. Por lo tanto, la duración será redondeada al siguiente múltiplo de 16.67, que es 750.

Para más información, consulta:

- %link:timing%

</details>

Define la pantalla de mirada neutral:

- Abre *neutral_gaze*
- Selecciona el elemento de imagen
- Dibuja una imagen en el centro de la pantalla y elige `gaze_neutral.png` en el diálogo del archivo pool que aparece.
- Establece la duración en 745 ms

Define la pantalla de señal de mirada:

- Abre *gaze_cue*
- Dibuja `gaze_left.png` en el centro de la pantalla

Por supuesto, no siempre queremos mostrar `gaze_left.png`. Más bien, queremos mostrar `gaze_left.png` cuando la variable `gaze_cue` es "left", y `gaze_right.png` cuando la variable `gaze_cue` es "right". Es decir, queremos mostrar `gaze_{gaze_cue}.png`, donde las llaves indican que se debe insertar una variable.

Podemos especificar esto en el script del ítem. Haz clic en Select view (el del medio de los tres íconos en la parte superior derecha) → View script. Esto muestra el llamado script de OpenSesame que define el ítem. (¡Esto no es Python ni JavaScript!). Cambia el comando `draw image` como se indica abajo. Ya que lo haces, también puedes definir la duración (recuerda que 495 ms se redondeará a 500 ms, como se explicó arriba).

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Haz clic en Aplicar. La vista ahora regresa a la vista de controles gráficos. La imagen ahora aparece como un signo de interrogación. ¡No te preocupes! La imagen correcta se mostrará durante el experimento.

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre las variables que existen en tu experimento</summary>

Abre el inspector de variables (Ctrl+I) para ver qué variables existen en tu experimento. ¡Cuando el experimento esté corriendo, incluso verás cómo sus valores cambian en tiempo real!

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: |
  El inspector de variables.
--%

</details>

Define la presentación objetivo:

- Abre *target*
- Dibuja `gaze_left.png` en el centro de la pantalla.
- Selecciona el elemento textline
- Dibuja "{target_letter}" en algún lugar del lado izquierdo de la pantalla. Las coordenadas exactas no importan, porque más adelante usaremos una variable para ello. Como antes, las llaves indican que se debe insertar la variable `target_letter`.
- Dibuja "X" en algún lugar del lado derecho de la pantalla

Edita el script del item (Selecciona vista → Ver script). Como antes, la señal de mirada debe depender de la variable `gaze_cue`. Además, la coordenada X de la letra objetivo debe depender de la variable `target_pos` y la coordenada X de la "X" debe depender de la variable `dist_pos`.

Es importante destacar que establecemos Duración en 0. Esto no significa que el objetivo se muestre durante 0 ms. Más bien, esto significa que el experimento avanza inmediatamente al siguiente item, que es un KEYBOARD_RESPONSE. ¡En otras palabras, la recolección de respuestas comienza tan pronto como se muestra el objetivo!

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x="{target_pos}" y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="X" x="{dist_pos}" y=0 z_index=0
~~~

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre cómo usar expresiones de variables complejas en el script de OpenSesame</summary>

En el script de OpenSesame, puedes incluir expresiones complejas usando llaves. Por ejemplo, en vez de especificar `x="{dist_pos}"` para la "X", podríamos haber especificado `x="{-1 * target_pos}"`. Esto se basa en los [literales de cadenas formateadas](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) de Python.

</details>


## Paso 7: Configura el item keyboard_response

🎯 __Objetivo:__ En este paso, configuraremos las teclas que los participantes pueden usar para responder, y cuánto tiempo tienen para responder.

Abre *keyboard_response*:

- Deja en blanco Respuesta correcta. Por defecto se usará la variable `correct_response` (del Paso 3).
- Establece Respuestas permitidas en `z;m`
- Establece el Tiempo límite en `2000` ms
- Deja el Tipo de evento en keypress

%--
figure:
 id: FigStep_7
 source: step7.png
 caption: |
  KEYBOARD_RESPONSE al final del Paso 7.
--%


## Paso 8: Configura el sampler

🎯 __Objetivo:__ En este paso, especificaremos qué sonido debe reproducirse después de una respuesta incorrecta.

Abre *incorrect_sound*. Haz clic en Buscar y selecciona `incorrect.ogg` de la biblioteca de archivos.

%--
figure:
 id: FigStep_8
 source: step8.png
 caption: |
  *incorrect_sound* al final del Paso 8.
--%


## Paso 9: Configura el logger

🎯 __Objetivo:__ En este paso, revisaremos cómo se registran los datos.

Abre *logger*. Por defecto, “Registrar automáticamente todas las variables” está habilitado. Esto es una buena práctica, así que no es necesario cambiar nada aquí.

<details class='info-box' markdown='1'>

<summary markdown='1'>Aprende más sobre registro personalizado</summary>

También puedes excluir variables específicas que no deseas registrar. Asimismo, puedes desactivar el registro automático por completo y seleccionar manualmente las variables específicas que quieres registrar. Hacer esto puede ayudar a mantener los archivos de registro limpios. Sin embargo, ¡siempre revisa cuidadosamente que se hayan registrado todas las variables requeridas!

</details>

## Paso 10: Dibujar el elemento de retroalimentación

🎯 __Objetivo:__ En este paso, definiremos la retroalimentación que los participantes reciben sobre su desempeño al final de cada bloque.

Abre *feedback*. Deja la duración en 'keypress'. Agrega el siguiente texto de retroalimentación:

```text
Fin del bloque

Tu tiempo de respuesta promedio fue de {avg_rt} ms
Tu precisión fue de {acc} %

Presiona cualquier tecla para continuar
```

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: |
  *feedback* al final del Paso 10.
--%

<details class='info-box' markdown='1'>

<summary markdown='1'>Más información sobre las variables de retroalimentación</summary>

OpenSesame realiza un seguimiento automático de las variables de retroalimentación:

- `response` es el valor de la última respuesta. Ejemplos: "z", "left", etc.
- `correct` es 1 después de una respuesta correcta, y 0 después de una respuesta incorrecta
- `response_time` es el tiempo de respuesta (en milisegundos) de la última respuesta
- `acc` es el porcentaje de respuestas correctas desde que las variables de retroalimentación se reiniciaron, en este caso por el elemento RESET_FEEDBACK al inicio del bloque
- `avg_rt` es el tiempo de respuesta promedio desde que las variables de retroalimentación se reiniciaron

Ver también:

- %link:manual/variables%

</details>

## Paso 11: Establecer el número de bloques para la fase de práctica y experimental

🎯 __Objetivo:__ En este paso, especificaremos el número de bloques de ensayos tanto en la fase de práctica como en la fase experimental.

Abre *practice_loop* y configura Repetir en 2, para que tengamos dos bloques de práctica. También agrega una variable de práctica a la tabla del bucle y asígnale el valor 'yes'. Esto es conveniente porque, durante el análisis de datos, nos permitirá identificar fácilmente cuáles ensayos fueron parte de la fase de práctica.

Abre *experimental_loop* y configura Repetir en 8. Nuevamente, agrega una variable de práctica, pero esta vez asígnale el valor 'no'.


## Paso 12: Escribir las formas de instrucciones, *end_of_practice* y *end_of_experiment*

🎯 __Objetivo:__ En este paso, añadiremos mensajes informativos e instrucciones a lo largo del experimento.

Abre los tres elementos FORM_TEXT_DISPLAY e ingresa instrucciones breves, claras y concisas. ¡Las buenas instrucciones son simples, completas y específicas!


## Paso 13: ¡Ejecuta el experimento!

🎯 __Objetivo:__ En este paso, haremos una primera prueba del experimento.

La doble flecha azul en la barra de herramientas es el botón de Ejecución rápida (Ctrl+Shift+W). Esto lanza el experimento en una ventana usando un número de sujeto y una ubicación de archivo de registro de prueba. Esto es útil principalmente durante el desarrollo.

La flecha verde simple es el botón Ejecutar en pantalla completa (Ctrl+R). Primero solicita un número de sujeto y archivo de registro, y si deseas ejecutar el experimento en pantalla completa o en una ventana. Esto es útil principalmente durante la recolección de datos.

¡Presiona uno de los dos botones para darle una prueba a tu experimento!

🏁 ¡Si el experimento se ejecuta, ya terminaste! Pero antes de terminar, revisemos dos puntos finales importantes, relacionados con la depuración y la selección del backend:


## Depuración efectiva y comprensión de errores

Es normal encontrarse con errores al construir experimentos. Lee los errores cuidadosamente e intenta entender lo que significan. ¡Este es el Camino Verdadero hacia una depuración efectiva!

%FigErrorMessage muestra un ejemplo de mensaje de error:

- El tipo de error es `FStringError`
- La descripción indica: “No se pudo evaluar la expresión f-string en el siguiente texto: `gaze_{gaze_ceu}.png`”
- El error ocurrió en la fase de preparación de los elementos *gaze_cue*
- El seguimiento es un mensaje de error de Python. Es una versión más técnica de la descripción anterior.

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: |
  Un mensaje de error en OpenSesame.
--%

Una vez que entiendas de dónde proviene el error, puedes intentar solucionarlo. En este ejemplo, el error resulta de un error tipográfico al definir el elemento *gaze_cue* en el Paso 6. `gaze_{gaze_ceu}.png` debería ser `gaze_{gaze_cue}.png`. ¡Fácil de arreglar!


<details class='info-box' markdown='1'>

<summary markdown='1'>Más información sobre depuración efectiva</summary>

La depuración efectiva es una habilidad importante. ¡Aprenderla te ahorrará mucho tiempo y frustración! Consulta el siguiente enlace para obtener consejos:

- %link:manual/debugging%

</details>


## Sincronización y selección de backend

En la pestaña 'Propiedades generales' del experimento (la pestaña que se abre al hacer clic en el nombre del experimento), puedes seleccionar un backend. El backend es la capa de software que controla la pantalla, los dispositivos de entrada, el sonido, etc. La mayoría de los experimentos funcionan con todos los backends, pero hay razones para preferir uno sobre otro, principalmente relacionadas con la sincronización. Actualmente hay cuatro backends:

- __psycho__ es el predeterminado. Está basado en PsychoPy y proporciona una excelente sincronización [(Peirce, 2007)][references].
- xpyriment — está basado en Expyriment y también proporciona una excelente sincronización[(Krause & Lindemann, 2013)][references]
- legacy — es una opción de respaldo que funciona en más sistemas, pero ofrece una sincronización menos precisa
- osweb — ejecuta experimentos en un navegador [(Mathôt & March, 2022)][references]

Ver también:

- %link:backends%
- %link:timing%

## Puntos clave

¡Has aprendido a construir un experimento simple pero completo!

- ✅ La estructura de un experimento normalmente se construye combinando elementos SEQUENCE y LOOP
- ✅ Las variables normalmente se definen en la tabla LOOP
- ✅ Los estímulos visuales sensibles al tiempo suelen presentarse con un SKETCHPAD
- ✅ La retroalimentación al participante suele presentarse con elementos FEEDBACK
- ✅ El FORM_TEXT_DISPLAY es conveniente para presentar texto
- ✅ Las variables y expresiones pueden insertarse usando llaves. Ejemplo: `{gaze_cue}`
- ✅ Las expresiones Run-if se definen en una SEQUENCE y determinan qué elementos se ejecutan realmente: Ejemplo: `correct == 0`
- ✅ Siempre verifica el tiempo y los archivos de registro con una prueba exhaustiva antes de recoger los datos


## Siguientes pasos

Ahora tienes una comprensión básica de OpenSesame. Esto es suficiente para construir muchos experimentos simples. Sin embargo, ¡puedes necesitar o querer aprender aún más! Aquí tienes próximos pasos recomendados:

- [Aprende a construir experimentos junto a SigmundAI](%url:beginner-sigmund%)
- [Aprende a usar código Python en tus experimentos](%url:intermediate%)
- [Aprende a usar código JavaScript en tus experimentos en línea](%url:intermediate-javascript%)

## Referencias

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. Social Science Computer Review. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? Behavior Research Methods, 42, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. Psychonomic Bulletin & Review, 5, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. Behavior Research Methods. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. Behavior Research Methods, 44(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. Language Learning. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Resolución temporal de los relojes: Efectos en la medición del tiempo de reacción—Buenas noticias para relojes malos. British Journal of Mathematical and Statistical Psychology, 42(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about