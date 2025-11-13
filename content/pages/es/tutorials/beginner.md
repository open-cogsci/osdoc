title: Tutorial para principiantes: direccionamiento de la mirada
hash: 8b68f010d5f28f2e59818b6c6aac4308f317f2ced632ba0c36993b1e159c8432
locale: es
language: Spanish

## Acerca de OpenSesame

OpenSesame es un programa gratuito para el desarrollo sencillo de experimentos conductuales en psicología, neurociencia y economía experimental. Para principiantes, OpenSesame cuenta con una interfaz gráfica completa, de apuntar y hacer clic. Para usuarios avanzados, OpenSesame admite scripting en Python (no cubierto en este tutorial).

## Acerca de este tutorial

Este tutorial muestra cómo crear un experimento psicológico simple pero completo utilizando OpenSesame [(Mathôt, Schreij, & Theeuwes, 2012; Mathôt & March, 2022)][references]. Utilizarás principalmente la interfaz gráfica de usuario de OpenSesame (es decir, sin codificación inline en Python), aunque realizarás pequeñas modificaciones al script de OpenSesame. Este tutorial toma aproximadamente una hora.

Este tutorial asume que estás usando OpenSesame 4.1 con todas las últimas actualizaciones aplicadas. Si ves una notificación que dice "Algunos paquetes pueden actualizarse (...)", haz clic en el botón "Instalar actualizaciones..." para abrir el panel de actualizaciones, y luego en "Ejecutar script de actualización" para realizar las actualizaciones. Después de actualizar, reinicia OpenSesame.

## El experimento

En este tutorial, crearás un experimento de direccionamiento de la mirada como fue introducido por [Friesen y Kingstone (1998)][references]. En este experimento, se presenta una cara en el centro de la pantalla (%FigGazeCuing). Esta cara mira ya sea a la derecha o a la izquierda. Una letra objetivo (una 'F' o una 'H') se presenta a la izquierda o derecha de la cara. Un estímulo distractor (la letra 'X') se presenta en el lado opuesto de la cara. La tarea es indicar lo más rápido posible si la letra objetivo es una 'F' o una 'H'. En la condición congruente, la cara mira hacia el objetivo. En la condición incongruente, la cara mira hacia el distractor. Como habrás adivinado, el hallazgo típico es que los participantes responden más rápido en la condición congruente que en la incongruente, aunque la dirección de la mirada no predice la ubicación del objetivo. Esto demuestra que nuestra atención es guiada automáticamente por la mirada de otras personas, incluso en situaciones donde esto no tiene ningún propósito. (¡Y aun cuando la cara es solo una carita feliz!)

El experimento consiste en una fase de práctica y una fase experimental. Se presentará retroalimentación visual después de cada bloque de ensayos. Se reproducirá un sonido después de cada respuesta incorrecta.

El diseño experimental:

- es *intra-sujetos*, porque todos los participantes hacen todas las condiciones
- es *completamente cruzado* (o factorial completo), porque ocurren todas las combinaciones de condiciones
- tiene tres factores (o variables):
    - *lado de la mirada* con dos niveles (izquierda, derecha)
    - *lado del objetivo* con dos niveles (izquierda, derecha)
    - *letra objetivo* con dos niveles (F, H)

Consulta %DesignScreencast para una explicación de la lógica y el diseño del experimento:

Haz clic en 'Default template' para comenzar con una plantilla experimental mínima.

Por defecto, existe una SECUENCIA principal, que simplemente se llama *experiment*. Haz clic en *experiment* en el área de vista general (por defecto a la izquierda, ver %FigInterface) para abrir sus controles en el área de pestañas. La SECUENCIA *experiment* consiste en dos elementos: un `notepad` llamado *getting started* y un SKETCHPAD llamado *welcome*.

<div class='info-box' markdown='1'>

__Caja de información__

__Nombres vs tipos__ -- Los elementos en OpenSesame tienen un nombre y un tipo. El nombre y el tipo pueden ser iguales, pero generalmente no lo son. Por ejemplo, un elemento SKETCHPAD puede tener el nombre *my_target_sketchpad*. Para dejar clara esta distinción, usaremos `monospace` para indicar tipos de elementos, y *cursiva* para indicar nombres.

__Consejo__ -- La 'Extended template' es un buen punto de partida para muchos experimentos. Ya contiene la estructura básica de un experimento basado en ensayos.

__Consejo__ -- Puedes hacer clic en los íconos de Ayuda en la parte superior derecha de la pestaña de un elemento para obtener ayuda contextual.

__Consejo__ -- ¡Guarda (acceso rápido: `Ctrl+S`) tu experimento con frecuencia! En el desafortunado (y poco probable) caso de pérdida de datos, a menudo podrás recuperar tu trabajo desde las copias de seguridad que se crean automáticamente, por defecto, cada 10 minutos (Menú → Herramientas → Abrir carpeta de copias de seguridad).

__Consejo__ -- A menos que hayas utilizado 'Eliminar permanentemente' (acceso rápido: `Shift+Del`), los elementos borrados todavía están disponibles en la papelera de 'Unused items' hasta que selecciones 'Permanently delete unused items' en la pestaña 'Unused items'. Puedes volver a agregar elementos borrados a una SECUENCIA arrastrándolos fuera de la papelera de 'Unused items' a algún lugar de tu experimento.

__Consejo__ -- %FigExperimentStructure muestra esquemáticamente la estructura del experimento que vas a crear. Si te confundes durante el tutorial, puedes consultar %FigExperimentStructure para ver dónde estás.

%--
figure:
 id: FigExperimentStructure
 source: experiment-structure.png
 caption: |
  A schematic representation of the structure of the 'Gaze cuing' experiment. The item types are in bold face, item names in regular face.
--%

</div>

__Elimina los elementos innecesarios__

No necesitamos los dos elementos que forman parte de la plantilla predeterminada. Elimina *getting_started* haciendo clic derecho sobre él en el área de vista general y seleccionando 'Delete' (acceso rápido: `Del`). Elimina *welcome* de la misma forma. La SECUENCIA *experiment* ahora está vacía.

__Agrega un elemento form_text_display para mostrar las instrucciones__

Como su nombre indica, un `form_text_display` es un formulario que muestra texto. Vamos a utilizar un `form_text_display` para dar instrucciones al participante al inicio del experimento.

Haz clic en *experiment* en el área de vista general para abrir sus controles en el área de pestañas. Verás una SECUENCIA vacía. Arrastra un `form_text_display` desde la barra de herramientas de elementos (en 'Form', ver %FigInterface) hacia la SECUENCIA *experiment* en el área de pestañas. Cuando sueltes, se insertará un nuevo elemento `form_text_display` en la SECUENCIA. (Volveremos a esto en el Paso 12.)

<div class='info-box' markdown='1'>

__Caja de información__

__Consejo__ -- Puedes arrastrar elementos al área de vista general y a las pestañas de SECUENCIA.

__Consejo__ -- Si una acción de arrastre es ambigua, aparecerá un menú emergente preguntando qué deseas hacer.

__Consejo__ -- Un `form_text_display` solo muestra texto. Si necesitas imágenes, etc., puedes usar un elemento SKETCHPAD. Nos encontraremos con el SKETCHPAD en el Paso 5.

</div>

__Agrega un elemento loop, que contenga un nuevo elemento sequence, para la fase de práctica__

Necesitamos agregar un elemento LOOP a la SECUENCIA *experiment*. Usaremos este LOOP para la fase de práctica del experimento. Haz clic en la SECUENCIA *experiment* para abrir sus controles en el área de pestañas.

Arrastra el elemento LOOP desde la barra de herramientas de elementos hacia la SEQUENCE, de la misma manera que añadiste el `form_text_display`. Los elementos nuevos se insertan debajo del elemento sobre el que se sueltan, así que si sueltas el nuevo LOOP sobre el `form_text_display` previamente creado, aparecerá justo donde lo quieres: después del `form_text_display`. Pero no te preocupes si colocas un nuevo elemento en el lugar equivocado, porque siempre puedes reordenar los elementos más tarde.

Por sí solo, un LOOP no hace nada. Un LOOP siempre necesita otro elemento para ejecutarse. Por lo tanto, debes llenar el nuevo elemento LOOP con otro elemento. (Si visualizas el elemento loop, también verás una advertencia: 'No item selected'). Arrastra un elemento SEQUENCE desde la barra de herramientas de elementos hasta el elemento LOOP. Aparecerá un menú emergente que te preguntará si deseas insertar la SEQUENCE después o dentro del elemento LOOP. Selecciona 'Insert into new_loop'. (Volveremos a esto en el Paso 2.)

<div class='info-box' markdown='1'>

__Caja de información__

__¿Qué es un elemento LOOP?__ -- Un LOOP es un elemento que añade estructura a tu experimento. Ejecuta repetidamente otro elemento, que normalmente es una SEQUENCE. Un LOOP también es el lugar donde normalmente definirás tus variables independientes, es decir, aquellas variables que manipulas en tu experimento.

__¿Qué es un elemento SEQUENCE?__ -- Un elemento SEQUENCE también añade estructura a tu experimento. Como su nombre indica, una SEQUENCE ejecuta múltiples elementos uno tras otro.

__La estructura LOOP-SEQUENCE__ -- A menudo, quieres repetir una secuencia de eventos. Para hacer esto, necesitarás un elemento LOOP que contenga un elemento SEQUENCE. Por sí misma, una SEQUENCE no se repite. Simplemente comienza con el primer elemento y termina con el último. Al 'envolver' una SEQUENCE con un LOOP, puedes repetir la SEQUENCE varias veces. Por ejemplo, una sola prueba normalmente corresponde a una única SEQUENCE llamada *trial_sequence*. Un LOOP (a menudo llamado *block_loop*) alrededor de esta *trial_sequence* constituiría entonces un solo bloque de pruebas. De manera similar, pero a otro nivel del experimento, una SEQUENCE (a menudo llamada *block_sequence*) puede contener un solo bloque de pruebas, seguido de una pantalla FEEDBACK. Un LOOP *practice_phase* alrededor de esta SEQUENCE de 'bloque' constituiría entonces la fase de práctica del experimento. Esto puede parecer un poco abstracto por ahora, pero a medida que sigas este tutorial, te familiarizarás con el uso de LOOPs y SEQUENCEs.

__Sugerencia__ -- Para más información sobre SEQUENCEs y LOOPs, consulta:

- %link:loop%
- %link:sequence%

</div>

__Añade un nuevo elemento form_text_display para el mensaje de fin de práctica__

Después de la fase de práctica, queremos informar al participante que el experimento real va a comenzar. Para esto necesitamos otro `form_text_display`. Regresa a la SEQUENCE *experiment* y arrastra un `form_text_display` desde la barra de herramientas de elementos hasta el elemento LOOP. Aparecerá el mismo menú emergente que antes. Esta vez, selecciona 'Insert after new_loop'. (Volveremos a esto en el Paso 12.)

<div class='info-box' markdown='1'>

__Sugerencia__ -- No te preocupes si accidentalmente has cambiado el elemento a ejecutar de un LOOP. Puedes deshacer esto fácilmente haciendo clic en el botón 'Deshacer' en la barra de herramientas (`Ctrl+Shift+Z`).

</div>

__Añade un nuevo elemento loop, que contenga la secuencia creada previamente, para la fase experimental__

Necesitamos un elemento LOOP para la fase experimental, igual que para la fase de práctica. Por lo tanto, arrastra un LOOP desde el menú de la barra de herramientas sobre *_form_text_display*.

El LOOP recién creado (llamado *new_loop_1*) está vacío, y debe ser llenado con una SEQUENCE, igual que el LOOP que creamos antes. Sin embargo, como los ensayos de la fase de práctica y de la fase experimental son idénticos, pueden usar la misma SEQUENCE. Por lo tanto, en lugar de arrastrar una nueva SEQUENCE desde la barra de herramientas de elementos, puedes reutilizar la ya existente (es decir, crear una copia enlazada).

Para hacer esto, haz clic derecho sobre la *new_sequence* creada previamente, y selecciona 'Copy (linked)'. Ahora, haz clic derecho sobre *new_loop_1* y selecciona 'Paste'. En el menú emergente que aparece, selecciona 'Insert into new_loop 1'.

<div class='info-box' markdown='1'>

__Caja de información de fondo__

__Consejo__ — Hay una distinción importante entre copias *vinculadas* y *no vinculadas*. Si creas una copia vinculada de un elemento, estás creando otra ocurrencia del mismo elemento. Por lo tanto, si modificas el elemento original, la copia vinculada también cambiará. En cambio, si creas una copia no vinculada de un elemento, la copia inicialmente será idéntica (excepto por su nombre), pero puedes editar el original sin afectar a la copia no vinculada y viceversa.

</div>

__Agrega un nuevo elemento form_text_display para el mensaje de despedida__

Cuando el experimento termina, debemos despedirnos del participante. Para esto necesitamos otro elemento `form_text_display`. Vuelve a la SECUENCIA *experiment*, y arrastra un `form_text_display` desde la barra de elementos hasta *new_loop_1*. En el menú emergente que aparece, selecciona 'Insertar después de new_loop_1'. (Volveremos a esto en el Paso 12).

__Asigna nombres descriptivos a los nuevos elementos__

Por defecto, los nuevos elementos tienen nombres como *new_sequence* y *new_form_text_display_2*. Es una buena práctica darles nombres descriptivos. Esto facilita mucho la comprensión de la estructura del experimento. Si quieres, también puedes añadir una descripción a cada elemento. Los nombres de los elementos deben estar compuestos por caracteres alfanuméricos y/o guiones bajos.

- Selecciona *new_form_text_display* en el área de vista general, haz doble clic en su etiqueta en la parte superior del área de pestañas y renombra el elemento a *instructions*. (Acceso directo del área de vista general: `F2`)
- Renombra *new_loop* a *practice_loop*.
- Renombra *new_sequence* a *block_sequence*. Debido a que has reutilizado este elemento en *new_loop_1*, el nombre también cambiará automáticamente allí. (Esto ilustra por qué es eficiente crear copias vinculadas siempre que sea posible).
- Renombra *new_form_text_display_1* a *end_of_practice*.
- Renombra *new_loop_1* a *experimental_loop*.
- Renombra *new_form_text_display_2* a *end_of_experiment*.

__Asigna un nombre descriptivo a todo el experimento__

El experimento en su totalidad también tiene un título y una descripción. Haz clic en 'New experiment' en el área de vista general. Puedes cambiar el nombre del experimento de la misma manera que cambiaste el nombre de sus elementos. El título actual es 'New experiment'. Renombra el experimento a 'Tutorial: Gaze cuing'. A diferencia de los nombres de los elementos, el título del experimento puede contener espacios, etc.

El área de vista general de tu experimento ahora se ve como %FigStep1. Este sería un buen momento para guardar tu experimento (acceso directo: `Ctrl+S`).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of the step 1.
--%


## Paso 2: Crear la secuencia del bloque

Haz clic en *block_sequence* en la vista general. Por el momento, esta SECUENCIA está vacía. Queremos que *block sequence* consista en un bloque de pruebas, seguido de una pantalla de FEEDBACK. Para esto necesitamos hacer lo siguiente:

__Agrega un elemento reset_feedback para restablecer las variables de feedback__

No queremos que nuestro feedback se vea afectado por las teclas que los participantes hayan presionado durante la fase de instrucciones o en bloques de pruebas anteriores. Por ello, comenzamos cada bloque de pruebas restableciendo las variables de feedback. Para hacer esto, necesitamos un elemento `reset_feedback`. Toma `reset_feedback` de la barra de elementos (en 'Recopilación de respuestas') y arrástralo a *block_sequence*.

__Agrega un nuevo loop, que contenga una nueva secuencia, para un bloque de pruebas__

Para una sola prueba necesitamos una SECUENCIA. Para un bloque de pruebas, necesitamos repetir esta SECUENCIA varias veces. Por lo tanto, para un bloque de pruebas necesitamos envolver un LOOP alrededor de una SECUENCIA. Arrastra un LOOP desde la barra de elementos hasta *new_reset_feedback*. Luego, arrastra una SECUENCIA desde la barra de elementos al LOOP recién creado, y selecciona 'Insertar en new_loop' en el menú emergente que aparece. (Volveremos a esto en el Paso 3).

__Agrega un elemento feedback__

Después de cada bloque de ensayos queremos dar retroalimentación al participante, para que sepa qué tan bien lo está haciendo. Para esto necesitamos un elemento FEEDBACK. Arrastra un FEEDBACK de la barra de herramientas de elementos a *new_loop*, y selecciona 'Insertar después del bucle' en el menú emergente que aparece. (Volveremos a esto en el Paso 10.)

__Pon nombres significativos a los nuevos elementos__

Renombra: (Consulta el Paso 1 si no recuerdas cómo hacer esto.)

- *new_loop* a *block_loop*
- *new_sequence* a *trial_sequence*
- *new_reset_feedback* a *reset_feedback*
- *new_feedback* a *feedback*

La vista general de tu experimento ahora se ve como %FigStep2. Recuerda guardar tu experimento regularmente.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%

## Paso 3: Llena el bucle de bloque con variables independientes

Como su nombre indica, *block_loop* corresponde a un solo bloque de ensayos. En el paso anterior creamos el *block_loop*, pero todavía necesitamos definir las variables independientes que se variarán dentro del bloque. Nuestro experimento tiene tres variables independientes:

- __gaze_cue__ puede ser 'left' o 'right'.
- __target_pos__ (la posición del objetivo) puede ser '-300' o '300'. Estos valores reflejan la coordenada X del objetivo en píxeles (0 = centro). Usar las coordenadas directamente, en lugar de 'left' y 'right', será conveniente cuando creemos las pantallas objetivo (ver Paso 5).
- __target_letter__ (la letra objetivo) puede ser 'F' o 'H'.

Por lo tanto, nuestro experimento tiene 2 x 2 x 2 = 8 niveles. Aunque 8 niveles no son tantos (la mayoría de los experimentos tendrán más), no necesitamos ingresar todas las combinaciones posibles a mano. Haz clic en *block_loop* en la vista general para abrir su pestaña. Ahora haz clic en el botón 'Diseño factorial completo'. En el asistente de variables, simplemente define todas las variables escribiendo el nombre en la primera fila y los niveles en las filas debajo del nombre (ver %FigVariableWizard). Si seleccionas 'Ok', verás que *block_loop* se ha llenado con todas las 8 combinaciones posibles.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  The loop variable wizard in Step 3.
--%

En la tabla del bucle resultante, cada fila corresponde a una ejecución de *trial_sequence*. Porque, en nuestro caso, una ejecución de *trial_sequence* corresponde a un ensayo, cada fila en nuestra tabla de bucle corresponde a un ensayo. Cada columna corresponde a una variable, que puede tener un valor diferente en cada ensayo.

Pero aún no hemos terminado. Necesitamos agregar tres variables más: la ubicación del distractor, la respuesta correcta y la congruencia.

- __dist_pos__ -- En la primera fila de la primera columna vacía, ingresa 'dist_pos'. Esto añade automáticamente una nueva variable experimental llamada 'dist_pos'. En las filas debajo, ingresa '300' donde 'target_pos' es -300, y '-300' donde 'target_pos' es 300. En otras palabras, el objetivo y el distractor deben ubicarse en posiciones opuestas.
- __correct_response__ -- Crea otra variable, en otra columna vacía, con el nombre 'correct_response'. Establece 'correct_response' en 'z' donde 'target_letter' es 'F', y en 'm' donde 'target_letter' es 'H'. Esto significa que el participante debe presionar la tecla 'z' si ve una 'F' y la tecla 'm' si ve una 'H'. (Siéntete libre de elegir otras teclas si 'z' y 'm' son incómodas en la distribución de tu teclado; por ejemplo, 'w' y 'n' son mejores en teclados AZERTY).
- __congruency__ -- Crea otra variable con el nombre 'congruency'. Establece 'congruency' en 'congruent' donde 'target_pos' es '-300' y 'gaze_cue' es 'left', y donde 'target_pos' es '300' y 'gaze_cue' es 'right'. En otras palabras, un ensayo es congruente si la cara mira al objetivo. Establece 'congruency' en 'incronguent' para los ensayos en los que la cara mira al distractor. La variable 'congruency' no es necesaria para ejecutar el experimento; sin embargo, es útil para analizar los datos posteriormente.

Necesitamos hacer una última cosa. 'Repeat' está actualmente en '1.00'. Esto significa que cada ciclo se ejecutará una vez. Así que el bloque ahora consiste en 8 ensayos, lo cual es un poco corto. Una longitud razonable para un bloque de ensayos es 24, así que pon 'Repeat' en 3.00 (3 repeticiones x 8 ciclos = 24 ensayos). No necesitas cambiar 'Order', porque 'random' es exactamente lo que queremos.

El *block_loop* ahora se ve como %FigStep3. Recuerda guardar tu experimento regularmente.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

__Cuadro de información__

__Consejo__ -- Puedes preparar tu tabla del bucle en tu programa de hojas de cálculo favorito y copiarla y pegarla en la tabla de variables de LOOP.

__Consejo__ -- Puedes especificar tu tabla del bucle en un archivo separado (en formato `.xlsx` o `.csv`) y usar este archivo directamente. Para hacerlo, selecciona 'file' en 'Source'.

__Consejo__ -- Puedes establecer 'Repeat' en un número no entero. Por ejemplo, ajustando 'Repeat' en '0.5', solo se ejecutará la mitad de los ensayos (seleccionados aleatoriamente).

</div>

## Paso 4: Añadir imágenes y archivos de sonido al pool de archivos

Para nuestros estímulos, usaremos imágenes de archivo. Además, reproduciremos un sonido si el participante comete un error. Para esto necesitamos un archivo de sonido.

Puedes descargar los archivos requeridos aquí (en la mayoría de los navegadores web puedes hacer clic derecho en los enlaces y elegir 'Guardar enlace como' o una opción similar):

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Después de descargar estos archivos (por ejemplo, en tu escritorio), puedes agregarlos al pool de archivos. Si el pool de archivos no es visible (por defecto está en el lado derecho de la ventana), haz clic en el botón 'Show file pool' en la barra principal de herramientas (acceso rápido: `Ctrl+P`). La forma más fácil de añadir los cuatro archivos es arrastrarlos desde el escritorio (o desde donde los hayas descargado) al pool de archivos. Alternativamente, puedes hacer clic en el botón '+' en el pool de archivos y añadir los archivos usando el cuadro de diálogo que aparece. El pool de archivos se guardará automáticamente con tu experimento.

Tu pool de archivos ahora se ve como %FigStep4. Recuerda guardar tu experimento regularmente.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

## Paso 5: Rellenar la secuencia del ensayo con ítems

Un ensayo en nuestro experimento es el siguiente:

1. __Punto de fijación__ -- 750 ms, ítem SKETCHPAD
2. __Mirada neutral__ -- 750 ms, ítem SKETCHPAD
3. __Clave de mirada__ -- 500 ms, ítem SKETCHPAD
4. __Objetivo__ -- 0 ms, ítem SKETCHPAD
5. __Recopilación de respuesta__ -- ítem KEYBOARD_RESPONSE
6. __Reproducir un sonido si la respuesta fue incorrecta__ -- ítem SAMPLER
7. __Registrar respuesta en archivo__ -- ítem LOGGER

Haz clic en *trial_sequence* en la vista general para abrir la pestaña *trial_sequence*. Toma un SKETCHPAD de la barra de ítems y arrástralo a la *trial_sequence*. Repite esto tres veces más, de manera que la *trial_sequence* contenga cuatro SKETCHPADs. Después, selecciona y añade un ítem KEYBOARD_RESPONSE, un ítem SAMPLER y un ítem LOGGER.

De nuevo, renombraremos los nuevos ítems para asegurarnos de que la *trial_sequence* sea fácil de entender. Renombra:

- *new_sketchpad* a *fixation_dot*
- *new_sketchpad_1* a *neutral_gaze*
- *new_sketchpad_2* a *gaze_cue*
- *new_sketchpad_3* a *target*
- *new_keyboard_response* a *keyboard_response*
- *new_sampler* a *incorrect_sound*
- *new_logger* a *logger*

Por defecto, los ítems siempre se ejecutan, lo cual se indica mediante la expresión run-if `True`. Sin embargo, queremos cambiar esto para el ítem *incorrect_sound*, que solo debe ejecutarse si se cometió un error. Para ello, necesitamos cambiar la expresión 'Run if' a `correct == 0` en la pestaña *trial_sequence*. Esto funciona porque el ítem *keyboard_response* crea automáticamente una variable `correct`, que se establece en `1` (correcto), `0` (incorrecto), o `undefined` (esto depende de la variable `correct_response` que se definió en el Paso 3). El doble signo igual es sintaxis de Python e indica que deseas comparar si dos cosas son iguales entre sí, en este caso, si la variable `correct` es igual a 0. Para cambiar una expresión run-if, haz doble clic sobre ella (atajo: `F3`).

Ahora, el *trial_sequence* se ve como %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "La *trial_sequence* al final del Paso 5."
--%

<div class='info-box' markdown='1'>

__Cuadro de fondo__

__¿Qué es un ítem SKETCHPAD?__ -- Un SKETCHPAD se usa para presentar estímulos visuales: texto, figuras geométricas, puntos de fijación, parches de Gabor, etc. Puedes dibujar en el SKETCHPAD usando las herramientas de dibujo integradas.

__¿Qué es un ítem KEYBOARD_RESPONSE?__ -- Un ítem KEYBOARD_RESPONSE recopila la respuesta de un participante desde el teclado.

__¿Qué es un ítem SAMPLER?__ -- Un ítem SAMPLER reproduce un sonido desde un archivo de audio.

__¿Qué es un ítem LOGGER?__ -- Un ítem LOGGER escribe datos en el archivo de registro. ¡Esto es muy importante! Si olvidas incluir un ítem LOGGER, no se registrarán datos durante el experimento.

__Consejo__ -- ¡Las variables y las expresiones condicionales "if" son muy potentes! Para aprender más sobre ellas, consulta:

- %link:manual/variables%

</div>

## Paso 6: Dibuja los ítems sketchpad

Los ítems SKETCHPAD que creamos en el Paso 5 aún están en blanco. ¡Es hora de dibujar!

__Configura el color de fondo a blanco__

Haz clic en *fixation_dot* en el área de vista general para abrir su pestaña. El SKETCHPAD todavía es gris oscuro, mientras que las imágenes que hemos descargado tienen un fondo blanco. Ups, olvidamos configurar el color de fondo del experimento a blanco (por defecto es gris oscuro). Haz clic en 'Tutorial: Gaze cuing' en el área de vista general para abrir la pestaña 'Propiedades generales'. Cambia 'Foreground' a 'black' y 'Background' a 'white'.

<div class='info-box' markdown='1'>

__Cuadro de fondo__

__Consejo__ -- Para un control más detallado sobre los colores, también puedes usar la notación hexadecimal RGB (por ejemplo, `#FF000` para rojo), usar varios espacios de color, o el selector de colores. Consulta también:

- %link:manual/python/canvas%

</div>

__Dibuja el punto de fijación__

Vuelve a *fixation_dot* haciendo clic en *fixation_dot* en la vista general. Ahora selecciona el elemento del punto de fijación haciendo clic en el botón con la mira. Si mueves el cursor sobre el sketchpad, puedes ver las coordenadas de pantalla en la parte superior derecha. Configura el color (del primer plano) a 'black'. Haz clic en el centro de la pantalla (0, 0) para dibujar un punto de fijación central.

Finalmente, cambia el campo 'Duration' de 'keypress' a '745', porque queremos que el punto de fijación se presente durante 750 ms. Espera... *¿por qué no especificamos simplemente una duración de 750 ms?* La razón es que la duración real de la presentación en pantalla siempre se redondea hacia arriba a un valor que sea compatible con la frecuencia de actualización de tu monitor. Esto puede sonar complicado, pero para la mayoría de los propósitos, las siguientes reglas prácticas son suficientes:

1. Elige una duración que sea posible dado la tasa de refresco de tu monitor. Por ejemplo, si la tasa de refresco de tu monitor es de 60 Hz, significa que cada cuadro dura 16,7 ms (= 1000 ms/60 Hz). Por lo tanto, en un monitor de 60 Hz, siempre debes seleccionar una duración que sea un múltiplo de 16,7 ms, como 16,7, 33,3, 50, 100, etc.
2. En el campo de duración del SKETCHPAD especifica una duración que sea unos pocos milisegundos menor de lo que tienes como objetivo. Así que, si quieres presentar un SKETCHPAD durante 50 ms, elige una duración de 45. Si quieres presentar un SKETCHPAD durante 1000 ms, elige una duración de 995. Etcétera.

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- Para una discusión detallada sobre la temporización experimental, consulta:

- %link:timing%

__Consejo__ -- La duración de un SKETCHPAD puede ser un valor en milisegundos, pero también puedes ingresar 'keypress' o 'mouseclick' para recoger una pulsación de teclado o un clic del ratón, respectivamente. En este caso, un SKETCHPAD funcionará de manera muy similar a un elemento KEYBOARD_RESPONSE (pero con menos opciones).

__Consejo__ -- ¡Asegúrate de que el color (primer plano) esté configurado en negro! De lo contrario, dibujarás blanco sobre blanco y no verás nada.

</div>

__Dibuja la mirada neutral__

Abre el SKETCHPAD *neutral_gaze*. Ahora selecciona la herramienta de imagen haciendo clic en el botón con el ícono de paisaje de montaña. Haz clic en el centro de la pantalla (0, 0). Aparecerá el diálogo 'Seleccionar archivo de la pool'. Selecciona el archivo `gaze_neutral.png` y haz clic en el botón 'Seleccionar'. ¡La imagen de la mirada neutral ahora te estará mirando desde el centro de la pantalla! Finalmente, como antes, cambia el campo 'Duración' de 'keypress' a '745'. (¡Y observa nuevamente que esto significa una duración de 750 ms en la mayoría de los monitores!)

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- OpenSesame puede manejar una amplia variedad de formatos de imagen. Sin embargo, se sabe que algunos formatos `.bmp` (no estándar) pueden causar problemas. Si encuentras que una imagen `.bmp` no se muestra, puedes convertirla a otro formato, como `.png`. Puedes convertir imágenes fácilmente con herramientas gratuitas como [GIMP].
</div>

__Dibuja la pista de mirada__

Abre el SKETCHPAD *gaze_cue* y, nuevamente, selecciona la herramienta de imagen. Haz clic en el centro de la pantalla (0, 0) y selecciona el archivo `gaze_left.png`.

¡Pero aún no hemos terminado! Porque la pista de mirada no siempre debería ser 'left', sino que depende de la variable `gaze_cue`, que hemos definido en el Paso 3. Sin embargo, al dibujar la imagen `gaze_left.png` en el SKETCHPAD, hemos generado un script que necesita solo una pequeña modificación para asegurarnos de que se muestre la imagen correcta. Haz clic en el botón 'Select view' en la parte superior derecha de la pestaña *gaze_cue* y selecciona 'View script'. Ahora verás el script que corresponde al sketchpad que acabamos de crear:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Lo único que tenemos que hacer es reemplazar `gaze_left.png` por `gaze_{gaze_cue}.png`. Esto significa que OpenSesame utiliza la variable `gaze_cue` (que tiene los valores `left` y `right`) para determinar qué imagen se debe mostrar.

Ya que estamos, también podemos cambiar la duración a '495' (¡redondeado a 500!). Ahora el script se ve así:

~~~ .python
set duration 495
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Haz clic en el botón 'Apply' en la parte superior derecha para aplicar los cambios al script y volver a los controles normales del elemento. OpenSesame te advertirá que la imagen no puede mostrarse porque está definida usando variables, y se mostrará una imagen de marcador de posición en su lugar. ¡No te preocupes, la imagen correcta se mostrará durante el experimento!

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- El inspector de variables (acceso rápido: `Ctrl+I`) es una herramienta potente para averiguar qué variables se han definido en tu experimento y qué valores tienen (ver %FigVariableInspector). Cuando tu experimento no está en ejecución, la mayoría de las variables aún no tienen valor. Pero cuando ejecutas tu experimento en una ventana, mientras tienes visible el inspector de variables, puedes ver las variables cambiando en tiempo real. Esto es muy útil para depurar tu experimento.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "El inspector de variables es una forma conveniente de obtener una visión general de las variables que existen en tu experimento."
--%

</div>

__Dibujar el objetivo__

Queremos que tres objetos formen parte de la pantalla objetivo: la letra objetivo, la letra distractora y la señal de mirada (ver %FigGazeCuing). Como antes, empezaremos creando una pantalla estática usando el editor SKETCHPAD. Después de esto, solo necesitaremos hacer pequeños cambios en el script para que la presentación exacta dependa de las variables.

Haz clic en *target* en la vista general para abrir la pestaña target y, como antes, dibuja la imagen `gaze_left.png` en el centro de la pantalla. Ahora selecciona la herramienta de dibujo de texto haciendo clic en el botón con el icono 'A'. Cambia el color de primer plano a 'negro' (si no está ya seleccionado). El tamaño de fuente predeterminado es de 18 px, lo cual es algo pequeño para nuestro propósito, así que cambia el tamaño de fuente a 32 px. Ahora haz clic en (-320, 0) en el SKETCHPAD (la coordenada X no tiene que ser exactamente 320, ya que vamos a cambiarla por una variable de todos modos). Escribe "{target_letter}" en el cuadro de diálogo que aparece, para dibujar la letra objetivo (al dibujar texto, puedes usar variables directamente). De manera similar, haz clic en (320, 0) y dibuja una 'X' (el distractor siempre es una 'X').

Ahora abre el editor de script haciendo clic en el botón 'Select view' en la parte superior derecha de la pestaña y seleccionando 'View script'. El script se ve así:

~~~ .python
set duration keypress
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

Como antes, cambia `gaze_left.png` por `gaze_{gaze_cue}.png`. También necesitamos hacer que la posición del objetivo y del distractor dependan de las variables `target_pos` y `dist_pos` respectivamente. Para hacer esto, simplemente cambia `-320` por `{target_pos}` y `320` por `{dist_pos}`. Asegúrate de dejar el `0`, que es la coordenada Y. El script ahora se ve así:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

Haz clic en el botón 'Apply' para aplicar el script y volver a los controles normales del elemento.

Por último, establece el campo 'Duration' en '0'. Esto no significa que el objetivo se presente solo durante 0 ms, sino que el experimento pasará al siguiente elemento (el *keyboard_response*) inmediatamente. Dado que el *keyboard_response* espera una respuesta, pero no cambia lo que hay en la pantalla, el objetivo permanecerá visible hasta que se dé una respuesta.

Recuerda guardar tu experimento regularmente.

<div class='info-box' markdown='1'>

__Caja de contexto__

__Consejo__ -- Cada elemento de un SKETCHPAD tiene una opción 'Mostrar si', que especifica cuándo debe mostrarse el elemento. Puedes usar esto para ocultar/mostrar elementos de un SKETCHPAD dependiendo de ciertas variables, similar a las sentencias run-if en una SEQUENCE.

__Consejo__ -- Asegúrate de que el color (de primer plano) esté configurado en negro. ¡De lo contrario, dibujarás blanco sobre blanco y no verás nada!

</div>

## Paso 7: Configura el elemento de respuesta por teclado

Haz clic en *keyboard_response* en la vista general para abrir su pestaña. Verás tres opciones: Respuesta correcta, Respuestas permitidas, Tiempo de espera y Tipo de evento.

Ya hemos definido la variable `correct_response` en el Paso 3. A menos que especifiquemos explícitamente una respuesta correcta, OpenSesame utiliza automáticamente la variable `correct_response` si está disponible. Por lo tanto, no necesitamos cambiar el campo 'Respuesta correcta' aquí.

Sí necesitamos establecer las respuestas permitidas. Ingresa 'z;m' en el campo de respuestas permitidas (u otras teclas si has elegido diferentes teclas de respuesta). El punto y coma se utiliza para separar las respuestas. El KEYBOARD_RESPONSE ahora solo acepta las teclas 'z' y 'm'. Todas las demás pulsaciones de teclas son ignoradas, con la excepción de 'escape', que pausa el experimento.

También queremos establecer un tiempo de espera, que es el intervalo máximo que el KEYBOARD_RESPONSE espera antes de decidir que la respuesta es incorrecta y establecer la variable 'response' en 'None'. '2000' (ms) es un buen valor.

No necesitamos cambiar el Tipo de evento, porque queremos que el participante responda presionando una tecla (keypress, el valor predeterminado) y no soltando una tecla (keyrelease).

El KEYBOARD_RESPONSE ahora se ve como %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "El KEYBOARD_RESPONSE al final del Paso 7."
--%

<div class='info-box' markdown='1'>

__Caja de contexto__

__Consejo__ -- Por defecto, el KEYBOARD_RESPONSE utilizará la variable `correct_response` para determinar si una respuesta fue correcta. Pero también puedes usar una variable diferente. Para hacer esto, ingresa un nombre de variable entre llaves (`{mi_variable}`) en el campo de respuesta correcta.

__Consejo__ -- Si 'eliminar pulsaciones pendientes' está habilitado (lo está por defecto), todas las pulsaciones de teclas pendientes se descartan cuando se llama al elemento KEYBOARD_RESPONSE. Esto previene efectos de arrastre, que de otro modo pueden ocurrir si el participante presiona accidentalmente una tecla durante una parte de la prueba en la que no hay respuesta.

__Consejo__ -- Para utilizar teclas especiales, como '/' o la flecha hacia arriba, puedes usar los nombres de las teclas (por ejemplo, 'up' y 'space') o los caracteres asociados (por ejemplo, '/' y ']'). El botón 'Listar teclas disponibles' proporciona una vista general de todos los nombres de teclas válidos.

</div>

## Paso 8: Configura el elemento incorrecto (sampler)

El elemento *incorrect_sound* no requiere mucho trabajo: solo necesitamos seleccionar el sonido que debe reproducirse. Haz clic en *incorrect_sound* en la vista general para abrir su pestaña. Haz clic en el botón 'Examinar' y selecciona `incorrect.ogg` del grupo de archivos.

El sampler ahora se ve como %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "El elemento *incorrect_sound* al final del Paso 8."
--%

<div class='info-box' markdown='1'>

__Caja de contexto__

__Consejo__ -- Puedes usar variables para especificar qué sonido debe reproducirse usando un nombre de variable entre llaves como (parte de) el nombre del archivo. Por ejemplo: `{a_word}.ogg`

__Consejo__ -- El SAMPLER maneja archivos en formato `.ogg`, `.mp3` y `.wav`. Si tienes archivos de sonido en un formato diferente, [Audacity] es una excelente herramienta gratuita para convertir archivos de sonido (y mucho más).

</div>

## Paso 9: Configura el logger de variables

En realidad, no necesitamos configurar el LOGGER de variables, pero echemos un vistazo de todos modos. Haz clic en *logger* en la vista general para abrir su pestaña. Verás que la opción 'Registrar automáticamente todas las variables' está seleccionada. Esto significa que OpenSesame registra todo, lo cual está bien.

<div class='info-box' markdown='1'>

__Caja de contexto__

__Consejo__ -- Si prefieres que tus archivos de registro estén limpios, puedes desactivar la opción 'Registrar automáticamente todas las variables' y seleccionar manualmente las variables, ya sea introduciendo los nombres de las variables manualmente ('Agregar variable personalizada'), o arrastrando las variables desde el inspector de variables a la tabla LOGGER. También puedes dejar activada la opción 'Registrar automáticamente todas las variables' y excluir las variables que no te interesan.

__El consejo que lo gobierna todo__ -- ¡Comprueba siempre tres veces que todas las variables necesarias se registran en tu experimento! La mejor manera de comprobar esto es ejecutar el experimento e investigar los archivos de registro resultantes.

</div>

## Paso 10: Dibuja el elemento de feedback

Después de cada bloque de ensayos, queremos presentar retroalimentación al participante para informarle sobre su desempeño. Por eso, en el Paso 2, agregamos un elemento FEEDBACK, llamado simplemente *feedback* al final de *block_sequence*.

Haz clic en *feedback* en el resumen para abrir su pestaña, selecciona la herramienta de dibujar texto, cambia el color de primer plano a 'negro' (si no lo está ya), y haz clic en (0, 0). Ahora introduce el siguiente texto:

```text
Fin del bloque

Tu tiempo de respuesta promedio fue de {avg_rt} ms
Tu precisión fue de {acc} %

Presiona cualquier tecla para continuar
```

Como queremos que el elemento de feedback permanezca visible tanto tiempo como el participante desee (es decir, hasta que pulse una tecla), dejamos el campo 'Duración' configurado en 'keypress'.

El elemento de feedback ahora se ve como %FigStep_10.

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "The feedback item at the end of Step 10."
--%

<div class='info-box' markdown='1'>

__Caja de fondo__

__¿Qué es un elemento de feedback?__ -- Un elemento FEEDBACK es casi idéntico a un elemento SKETCHPAD. La única diferencia es que un elemento FEEDBACK no se prepara por adelantado. Esto significa que puedes usarlo para presentar retroalimentación, lo que requiere información actualizada sobre la respuesta de un participante. No deberías usar elementos FEEDBACK para presentar pantallas sensibles al tiempo, porque el hecho de que no se preparen por adelantado significa que sus propiedades de temporización no son tan buenas como las del elemento SKETCHPAD. Ver también:

- %link:visual%

__Feedback y variables__ -- Los elementos de respuesta registran automáticamente la precisión y el tiempo de respuesta promedio del participante en las variables 'acc' (sinónimo: 'accuracy') y 'avg_rt' (sinónimo: 'average_response_time'), respectivamente. Ver también:

- %link:manual/variables%

__Consejo__ -- Asegúrate de que el color (de primer plano) esté configurado en negro. ¡De lo contrario, dibujarás blanco sobre blanco y no verás nada!

</div>

## Paso 11: Establece la duración de las fases de práctica y experimental

Previamente creamos los elementos *practice_loop* y *experiment_loop*, los cuales ambos llaman a *block_sequence* (es decir, un bloque de ensayos). Sin embargo, ahora mismo llaman a *block_sequence* solo una vez, lo que significa que tanto la fase de práctica como la fase experimental consisten en un solo bloque de ensayos.

Haz clic en *practice_loop* para abrir su pestaña y establece 'Repetir' a '2.00'. Esto significa que la fase de práctica consiste en dos bloques.

Haz clic en *experimental_loop* para abrir su pestaña y establece 'Repetir' a '8.00'. Esto significa que la fase experimental consiste en ocho bloques.

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- Puedes crear una variable `practice` tanto en *practice_loop* como en *experimental_loop* y configurarla en 'yes' y 'no' respectivamente. Esta es una forma sencilla de controlar qué ensayos formaron parte de la fase de práctica.

</div>

## Paso 12: Escribe los formularios de instrucciones, end_of_practice y end_of_experiment

¡Creo que puedes encargarte de este paso tú mismo! Simplemente abre los elementos apropiados y agrega un texto para presentar las instrucciones, un mensaje de final de práctica y un mensaje de final de experimento.

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- Puedes usar un subconjunto de etiquetas HTML para dar formato a tu texto. Por ejemplo, *&lt;b&gt;esto estará en negrita&lt;b&gt;* y *&lt;span color='red'&gt;esto estará en rojo&lt;span&gt;*. Para obtener más información, consulta:

- %link:text%

</div>

## Paso 13: ¡Ejecutar el experimento!

¡Has terminado! Haz clic en los botones 'Ejecutar en ventana' (atajo: `Ctrl+W`) o 'Ejecutar en pantalla completa' (atajo: `Ctrl+R`) en la barra de herramientas para ejecutar tu experimento.

<div class='info-box' markdown='1'>

__Caja de información__

__Consejo__ -- Una prueba se ejecuta aún más rápido haciendo clic en el botón naranja 'Ejecutar en ventana' (atajo: `Ctrl+Shift+W`), que no te preguntará cómo guardar el archivo de registro (por lo que solo debe usarse para pruebas).

</div>

## Entendiendo los errores

Poder comprender los mensajes de error es una habilidad crucial al trabajar con OpenSesame. Después de todo, ¡un experimento recién creado rara vez se ejecuta inmediatamente sin errores!

Supongamos que cometimos un error en uno de los pasos anteriores. Al intentar ejecutar el experimento, recibimos el siguiente mensaje de error (%FigErrorMessage):

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "Un mensaje de error en OpenSesame."
--%

El mensaje de error comienza con un nombre, en este caso `FStringError`, que indica el tipo general del error. A esto le sigue un breve texto explicativo, en este caso 'Failed to evaluate f-string expression in the following text: gaze_{gaze_ceu}.png`. Incluso sin entender exactamente qué es un f-string (es una cadena que contiene código Python entre llaves), queda claro que hay algo mal con el texto '{gaze_ceu}.png'.

El mensaje de error también indica que el error proviene de la fase de preparación del elemento *gaze_cue*.

Finalmente, el mensaje de error indica qué salió mal específicamente al evaluar el texto 'gaze_{gaze_ceu}.png': el nombre 'gaze_ceu' no está definido.

Al leer cuidadosamente el mensaje de error, probablemente ya se te ocurrió la causa y la solución: ¡cometimos un simple error de ortografía en el elemento *gaze_cue*, escribiendo '{gaze_ceu}' en lugar de '{gaze_cue}'! Y esto resultó en un error porque no existe una variable con el nombre `gaze_ceu`. Esto se puede arreglar fácilmente abriendo el script del elemento *gaze_cue* y corrigiendo el error tipográfico.

## Finalmente: Algunas consideraciones generales sobre la sincronización y la selección del backend

En la pestaña 'Propiedades generales' del experimento (la pestaña que se abre haciendo clic en el nombre del experimento) puedes seleccionar un backend. El backend es la capa de software que controla la pantalla, los dispositivos de entrada, el sonido, etc. La mayoría de los experimentos funcionan con todos los backends, pero existen razones para preferir uno sobre otro, principalmente relacionadas con la sincronización del tiempo. Actualmente hay cuatro backends (dependiendo de tu sistema, puede que no estén disponibles los cuatro):

- __psycho__ -- un backend con aceleración por hardware basado en PsychoPy [(Peirce, 2007)][references]. Este es el predeterminado.
- __xpyriment__ -- un backend con aceleración por hardware basado en Expyriment [(Krause & Lindeman, 2013)][references]
- __legacy__ -- un backend 'seguro', basado en PyGame. Ofrece un rendimiento fiable en la mayoría de las plataformas, pero, debido a la falta de aceleración por hardware, sus propiedades de sincronización no son tan buenas como las de los demás backends.
- __osweb__ -- ejecuta experimentos en un navegador [(Mathôt & March, 2022)][references].

Ver también:

- %link:backends%
- %link:timing%


## Referencias

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Assessing the effects of technical variance on the statistical outcomes of web experiments measuring response times. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). Does variability in human performance outweigh imprecision in response devices such as computer keyboards? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: A Python library for cognitive and neuroscientific experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un generador de experimentos gráfico y de código abierto para las ciencias sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Realización de experimentos lingüísticos en línea con OpenSesame y OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: Software de psicofísica en Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Resolución temporal de relojes: efectos sobre la medición del tiempo de reacción—Buenas noticias para relojes malos. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>

[references]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html
[gimp]: http://www.gimp.org/
[audacity]: http://audacity.sourceforge.net/
[python inline scripting]: /python/about