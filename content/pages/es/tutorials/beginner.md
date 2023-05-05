title: Tutorial para principiantes: direccionamiento de la mirada
hash: 4b8cd383d0beb70ff7280b358bcb4c15a73635e4fb62d7260bc4b1e16d992e65
locale: es
language: Spanish

[TOC]

## Acerca de OpenSesame

OpenSesame es un programa para el fácil desarrollo de experimentos de comportamiento en psicología, neurociencia y economía experimental. Para principiantes, OpenSesame tiene una interfaz gráfica completa y fácil de usar. Para usuarios avanzados, OpenSesame admite scripts en Python (no cubiertos en este tutorial).

OpenSesame está disponible gratuitamente bajo la [Licencia Pública General v3][gpl].

## Acerca de este tutorial

Este tutorial muestra cómo crear un experimento psicológico simple pero completo usando OpenSesame [(Mathôt, Schreij y Theeuwes, 2012; Mathôt y March, 2022)][referencias]. Utilizará principalmente la interfaz gráfica de usuario de OpenSesame (es decir, sin codificación Python inline), aunque realizará pequeñas modificaciones en el script de OpenSesame. Este tutorial tiene una duración aproximada de una hora.

## Recursos

- __Descarga__ -- Este tutorial asume que estás utilizando la versión 4.0.0 o posterior de OpenSesame. Para comprobar qué versión estás utilizando, consulta la parte inferior derecha de la pestaña "Comenzar" (ver %FigGetStarted). Puedes descargar la versión más reciente de OpenSesame en:
	- %link:descarga%
- __Documentación__ -- Un sitio web de documentación dedicado se encuentra en:
	- <http://osdoc.cogsci.nl/>
- __Foro__ -- Se puede encontrar un foro de soporte en:
	- <http://forum.cogsci.nl/>

## El experimento

En este tutorial, crearás un experimento de mirada-guiada como el introducido por [Friesen y Kingstone (1998)][referencias]. En este experimento, se presenta una cara en el centro de la pantalla (%FigGazeCuing). Esta cara mira hacia la derecha o hacia la izquierda. Una letra objetivo (una 'F' o una 'H') se presenta a la izquierda o derecha de la cara. Un estímulo distractor (la letra 'X') se presenta en el otro lado de la cara. La tarea consiste en indicar lo más rápido posible si la letra objetivo es una 'F' o una 'H'. En la condición congruente, la cara mira al objetivo. En la condición incongruente, la cara mira al distractor. Como podrías haber adivinado, el hallazgo típico es que los participantes responden más rápido en la condición congruente que en la condición incongruente, aunque la dirección de la mirada no sea predictiva de la ubicación del objetivo. Esto demuestra que nuestra atención es guiada automáticamente por la mirada de otras personas, incluso en situaciones en las que esto no tiene ningún propósito. (¡E incluso cuando la cara es solo una carita!)

%--
figura:
 id: FigGazeCuing
 fuente: gaze-cuing.png
 leyenda: |
  El paradigma de mirada-guiada [(Friesen y Kingstone, 1998)][referencias] que implementarás en este tutorial. Este ejemplo representa una prueba en la condición incongruente, porque la carita está mirando al distractor ('X') y no al objetivo ('F').
--%

El experimento consiste en una fase de práctica y una fase experimental. Se presentará retroalimentación visual después de cada bloque de ensayos. Se reproducirá un sonido después de cada respuesta incorrecta.

## Diseño experimental

Este diseño:

- es *dentro de sujetos*, porque todos los participantes realizan todas las condiciones.
- es *completamente cruzado* (o factorial completo), porque todas las combinaciones de condiciones ocurren.
- tiene tres factores (o variables):
    - *lado de la mirada* con dos niveles (izquierdo, derecho)
    - *lado del objetivo* con dos niveles (izquierdo, derecho)
    - *letra objetivo* con dos niveles (F, H)
- tiene N sujetos

Consulte también %DesignScreencast para obtener una explicación de la lógica y el diseño del experimento:

%--
video:
 fuente: youtube
 id: DesignScreencast
 ID del video: aWvibRH6D4E
 ancho: 640
 alto: 360
 leyenda: |
  Explicación de la lógica y diseño del experimento.
--%

## Paso 1: Crear la secuencia principal

Cuando inicias OpenSesame, ves la pestaña '¡Empieza!' (%FigGetStarted). Debajo de 'Iniciar un nuevo experimento' se muestra una lista de plantillas. Estas plantillas proporcionan puntos de partida convenientes para nuevos experimentos. Después de guardar un experimento por primera vez, los experimentos recientemente abiertos se muestran en 'Continuar con un experimento reciente'. En la parte inferior de la página, hay enlaces a la documentación (que incluye este tutorial), el foro de la comunidad y una página con opciones de soporte profesional (de pago). ¡Y, por supuesto, un enlace donde puedes comprarnos una taza de café para ayudarnos a mantenernos despiertos mientras trabajamos para proporcionar el mejor software gratuito!

%--
figure:
  id: FigGetStarted
  source: get-started.png
  caption: |
    El diálogo 'Get started' al iniciar OpenSesame.
--%

Haz clic en 'Plantilla predeterminada' para comenzar con una plantilla experimental mínima.

Por defecto, hay una SECUENCIA principal, que simplemente se llama *experimento*. Haz clic en *experimento* en el área de descripción general (por defecto en el lado izquierdo, ver %FigInterface) para abrir sus controles en el área de pestañas. La SECUENCIA *experimento* consta de dos elementos: un `notepad` llamado *empezando* y un SKETCHPAD llamado *bienvenida*.

No necesitamos estos dos elementos. Elimina *empezando* haciendo clic derecho sobre él en el área de descripción general y seleccionando 'Eliminar' (atajo: `Del`). Elimina *bienvenida* de la misma manera. La SECUENCIA *experimento* ahora está vacía.

%--
figure:
  id: FigInterface
  source: interface.png
  caption: "El diseño predeterminado de la interfaz de OpenSesame."
--%

<div class='info-box' markdown='1'>

__Cuadro de información__

__Nombres vs tipos__ -- Los elementos en OpenSesame tienen un nombre y un tipo. El nombre y el tipo pueden ser los mismos, pero generalmente no lo son. Por ejemplo, un elemento SKETCHPAD puede tener el nombre *mi_boceto_objetivo*. Para dejar clara esta distinción, usaremos `monoespacio` para indicar tipos de elementos y *cursiva* para indicar nombres.

__Consejo__ -- La 'Plantilla extendida' es un buen punto de partida para muchos experimentos. Ya contiene la estructura básica de un experimento basado en ensayos.

__Consejo__ -- Puedes hacer clic en los íconos de Ayuda en la parte superior derecha de la pestaña de un elemento para obtener ayuda contextual.

__Consejo__ -- ¡Guarda (atajo: `Ctrl+S`) tu experimento a menudo! En el desafortunado (e improbable) caso de pérdida de datos, a menudo podrás recuperar tu trabajo de las copias de seguridad que se crean automáticamente, por defecto, cada 10 minutos (Menú → Herramientas → Abrir carpeta de copia de seguridad).

__Consejo__ -- A menos que hayas usado 'Eliminar permanentemente' (atajo: `Shift+Del`), los elementos eliminados aún están disponibles en la papelera 'Elementos no utilizados', hasta que seleccionas 'Eliminar permanentemente elementos no utilizados' en la pestaña 'Elementos no utilizados'. Puedes volver a agregar elementos eliminados a una SECUENCIA arrastrándolos fuera de la papelera 'Elementos no utilizados' a algún lugar de tu experimento.

__Consejo__ -- %FigExperimentStructure muestra de manera esquemática la estructura del experimento que crearás. Si te confundes durante el tutorial, puedes consultar %FigExperimentStructure para ver dónde estás.

%--
figure:
  id: FigExperimentStructure
  source: experiment-structure.png
  caption: |
    Una representación esquemática de la estructura del experimento de 'Gaze cuing'. Los tipos de elementos están en negrita, los nombres de elementos en letra normal.
--%

</div>

__Agregar un elemento form_text_display para la pantalla de instrucciones__

Como su nombre indica, un `form_text_display` es un formulario que muestra texto. Vamos a utilizar un `form_text_display` para dar instrucciones al participante al comienzo del experimento.

Haz clic en *experimento* en el área de descripción general para abrir sus controles en el área de pestañas. Verás que la SECUENCIA está vacía. Arrastra un `form_text_display` desde la barra de herramientas de elementos (en 'Formulario', ver %FigInterface) a la SECUENCIA *experimento* en el área de pestañas. Cuando sueltes, se insertará un nuevo elemento `form_text_display` en la SECUENCIA. (Volveremos a esto en el Paso 12.)

<div class='info-box' markdown='1'>

__Cuadro de información__

__Consejo__ -- Puedes arrastrar elementos al área de descripción general y a las pestañas SEQUENCE.

__Consejo__ -- Si una acción de arrastre es ambigua, un menú emergente te preguntará qué deseas hacer.

__Consejo__ -- Un `form_text_display` solo muestra texto. Si requieres imágenes, etc., puedes utilizar un elemento SKETCHPAD. Conoceremos SKETCHPAD en el Paso 5.

</div>

__Añade un elemento de bucle, que contiene un nuevo elemento de secuencia, para la fase de práctica__

Necesitamos agregar un elemento LOOP a la SECUENCIA *experiment*. Usaremos este LOOP para la fase de práctica del experimento. Haz clic en la SECUENCIA *experiment* para abrir sus controles en el área de pestañas.

Arrastra el elemento LOOP desde la barra de herramientas de elementos hacia la SECUENCIA, de la misma manera en que agregaste el `form_text_display`. Los nuevos elementos se insertan debajo del elemento sobre el que se sueltan, por lo que si sueltas el nuevo LOOP sobre el `form_text_display` creado anteriormente, aparecerá donde lo deseas: después del `form_text_display`. Pero no te preocupes si sueltas un nuevo elemento en el lugar equivocado, siempre puedes reorganizar las cosas más tarde.

Por sí solo, un LOOP no hace nada. Un LOOP siempre necesita otro elemento para ejecutarse. Por lo tanto, debes completar el nuevo elemento LOOP con otro elemento. (Si ves el elemento de bucle, también verás una advertencia: 'No item selected'). Arrastra un elemento SEQUENCE desde la barra de herramientas de elementos al elemento LOOP. Aparecerá un menú emergente preguntándote si deseas insertar la SECUENCIA después o en el elemento LOOP. Selecciona 'Insert into new_loop'. (Volveremos a esto en el Paso 2).

<div class='info-box' markdown='1'>

__Caja de información__

__¿Qué es un elemento LOOP?__ -- Un LOOP es un elemento que añade estructura a tu experimento. Ejecuta repetidamente otro elemento, generalmente una SECUENCIA. Un LOOP también es el lugar donde normalmente definirás tus variables independientes, es decir, aquellas variables que manipulas en tu experimento.

__¿Qué es un elemento SEQUENCE?__ -- Un elemento SEQUENCE también agrega estructura a tu experimento. Como su nombre indica, una SECUENCIA ejecuta múltiples elementos, uno tras otro.

__La estructura LOOP-SEQUENCE__ -- A menudo deseas repetir una secuencia de eventos. Para hacer esto, necesitarás un elemento LOOP que contenga un elemento SEQUENCE. Por sí misma, una SECUENCIA no se repite. Simplemente comienza con el primer elemento y termina con el último elemento. Al 'envolver' un elemento LOOP alrededor de la SECUENCIA, puedes repetir la SECUENCIA varias veces. Por ejemplo, un ensayo único generalmente corresponde a una única SECUENCIA llamada *trial_sequence*. Un LOOP (a menudo llamado *block_loop*) alrededor de este *trial_sequence*, constituiría entonces un solo bloque de ensayos. De manera similar, pero en otro nivel del experimento, una SECUENCIA (a menudo llamada *block_sequence*) puede contener un único bloque de ensayos, seguido de una visualización de FEEDBACK. Un LOOP de *practice_phase* alrededor de esta SECUENCIA de 'bloque' constituiría entonces la fase de práctica del experimento. Esto puede parecer un poco abstracto en este momento, pero a medida que sigas este tutorial, te familiarizarás con el uso de LOOPs y SEQUENCEs.

__Consejo__ -- Para más información acerca de las SEQUENCEs y LOOPs, consulta:

- %link:loop%
- %link:sequence%

</div>

__Añade un nuevo elemento form_text_display para el mensaje de fin de práctica__

Después de la fase de práctica, queremos informar al participante que comenzará el experimento real. Para ello, necesitamos otro `form_text_display`. Vuelve a la SECUENCIA *experiment* y arrastra un `form_text_display` desde la barra de herramientas de elementos al elemento LOOP. Aparecerá el mismo menú emergente que antes. Esta vez, selecciona 'Insert after new_loop'. (Volveremos a esto en el Paso 12).

<div class='info-box' markdown='1'>

__Consejo__ -- No te preocupes si has cambiado accidentalmente el elemento de ejecución de un LOOP. Puedes deshacer esto fácilmente haciendo clic en el botón 'Deshacer' en la barra de herramientas (`Ctrl+Shift+Z`).

</div>

__Agrega un nuevo elemento de bucle, que contiene la secuencia creada previamente, para la fase experimental__

Necesitamos un elemento LOOP para la fase experimental, como en la fase de práctica. Por lo tanto, arrastra un LOOP desde el menú de la barra de herramientas de elementos a *_form_text_display*.

El LOOP recién creado (llamado *new_loop_1*) está vacío y debe llenarse con una SECUENCIA, al igual que el LOOP que creamos antes. Sin embargo, debido a que los ensayos de la fase de práctica y experimental son idénticos, pueden usar la misma SECUENCIA. Por lo tanto, en lugar de arrastrar una nueva SECUENCIA desde la barra de herramientas de elementos, puedes reutilizar la *existente* (es decir, crear una copia vinculada).

Para hacer esto, haz clic con el botón derecho en el *new_sequence* creado anteriormente y selecciona "Copiar (vinculado)". Ahora, haz clic con el botón derecho en *new_loop_1* y selecciona 'Pegar'. En el menú emergente que aparece, selecciona 'Insertar en new_loop 1'.

<div class='info-box' markdown='1'>

__Recuadro de información__

__Consejo__ — Existe una distinción importante entre copias *vinculadas* y *no vinculadas*. Si creas una copia vinculada de un elemento, creas otra aparición del mismo elemento. Por lo tanto, si modificas el elemento original, la copia vinculada también cambiará. Por el contrario, si creas una copia no vinculada de un artículo, la copia inicialmente parecerá idéntica (excepto por su nombre), pero puedes editar el original sin afectar la copia no vinculada, y viceversa.

</div>

__Agregar un nuevo elemento form_text_display, para el mensaje de despedida__

Cuando el experimento haya terminado, debemos despedirnos del participante. Para ello necesitamos otro elemento `form_text_display`. Regresa a la SECUENCIA del *experimento* y arrastra un `form_text_display` desde la barra de herramientas de elementos hasta *new_loop_1*. En el menú emergente que aparece, selecciona 'Insertar después de new_loop_1'. (Volveremos a esto en el paso 12.)

__Dar nombres razonables a los nuevos elementos__

Por defecto, los nuevos elementos tienen nombres como *new_sequence* y *new_form_text_display_2*. Es recomendable dar nombres razonables a los elementos. Esto facilita mucho la comprensión de la estructura del experimento. Si quieres, también puedes agregar una descripción a cada elemento. Los nombres de los elementos deben constar de caracteres alfanuméricos y/o guiones bajos.

- Selecciona *new_form_text_display* en el área de descripción general, haz doble clic en su etiqueta en la parte superior del área de pestañas y cambia el nombre del elemento a *instrucciones*. (Acceso directo en el área de descripción general: `F2`)
- Cambia el nombre de *new_loop* a *practice_loop*.
- Cambia el nombre de *new_sequence* a *block_sequence*. Como has reutilizado este elemento en *new_loop_1*, el nombre cambia automáticamente allí también. (Esto ilustra por qué es eficiente crear copias vinculadas siempre que sea posible).
- Cambia el nombre de *new_form_text_display_1* a *end_of_practice*.
- Cambia el nombre de *new_loop_1* a *experimental_loop*.
- Cambia el nombre de *new_form_text_display_2* a *end_of_experiment*.

__Dar un nombre razonable a todo el experimento__

El experimento en su totalidad también tiene un título y una descripción. Haz clic en "Nuevo experimento" en el área de descripción general. Puedes cambiar el nombre del experimento de la misma manera que cambiaste los nombres de sus elementos. El título actual es "Nuevo experimento". Cambia el nombre del experimento a "Tutorial: Gaze cuing". A diferencia de los nombres de los elementos, el título del experimento puede contener espacios, etc.

El área de descripción general de tu experimento ahora se ve como en %FigStep1. Sería un buen momento para guardar tu experimento (atajo: `Ctrl+S`).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  El área de descripción general al final del paso 1.
--%


## Paso 2: Crear la secuencia de bloques

Haz clic en *block_sequence* en el resumen. Por ahora, esta SECUENCIA está vacía. Queremos que *block_sequence* consista en un bloque de ensayos, seguido de una pantalla de RETROALIMENTACIÓN. Para ello, necesitamos hacer lo siguiente:

__Agrega un elemento reset_feedback para restablecer las variables de retroalimentación__

No queremos que nuestra retroalimentación se vea afectada por las pulsaciones de tecla que los participantes han realizado durante la fase de instrucción o bloques anteriores de ensayos. Por lo tanto, comenzamos cada bloque de ensayos restableciendo las variables de retroalimentación. Para hacer esto, necesitamos un elemento `reset_feedback`. Toma `reset_feedback` de la barra de herramientas de elementos (en "Recopilación de respuestas") y arrástralo a *block_sequence*.

__Agrega un nuevo loop, que contenga una nueva secuencia, para un bloque de ensayos__

Para un solo ensayo necesitamos una SECUENCIA. Para un bloque de ensayos, necesitamos repetir esta SECUENCIA varias veces. Por lo tanto, para un bloque de ensayos necesitamos envolver un BUCLE alrededor de una SECUENCIA. Arrastra un BUCLE desde la barra de herramientas de elementos a *new_reset_feedback*. A continuación, arrastra una SECUENCIA desde la barra de herramientas de elementos al BUCLE recién creado y selecciona 'Insertar en new_loop' en el menú emergente que aparece. (Volveremos a esto en el Paso 3).

__Añadir un elemento de retroalimentación__

Después de cada bloque de ensayos, queremos dar retroalimentación al participante para que sepa qué tan bien está haciendo. Para esto necesitamos un elemento de RETROALIMENTACIÓN. Arrastra RETROALIMENTACIÓN desde la barra de herramientas de elementos a *new_loop* y selecciona 'Insertar después del bucle' en el menú emergente que aparece. (Volveremos a esto en el Paso 10).

__Asignar nombres adecuados a los nuevos elementos__

Renombrar: (Consulta el Paso 1 si no recuerdas cómo hacer esto).

- *new_loop* a *block_loop*
- *new_sequence* a *trial_sequence*
- *new_reset_feedback* a *reset_feedback*
- *new_feedback* a *feedback*

La descripción general de tu experimento ahora se ve como en %FigStep2. Recuerda guardar tu experimento regularmente.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  El área de descripción general al final del Paso 2.
--%

## Paso 3: Llena el bloque de bucles con variables independientes

Como sugiere el nombre, *block_loop* corresponde a un solo bloque de ensayos. En el paso anterior creamos el *block_loop*, pero aún necesitamos definir las variables independientes que se variarán dentro del bloque. Nuestro experimento tiene tres variables independientes:

- __gaze_cue__ puede ser 'izquierda' o 'derecha'.
- __target_pos__ (la posición del objetivo) puede ser '-300' o '300'. Estos valores reflejan la coordenada X del objetivo en píxeles (0 = centro). Usar las coordenadas directamente, en lugar de 'izquierda' y 'derecha', será conveniente cuando creemos las pantallas de destino (ver Paso 5).
- __target_letter__ (la letra objetivo) puede ser 'F' o 'H'.

Por lo tanto, nuestro experimento tiene 2 x 2 x 2 = 8 niveles. Aunque 8 niveles no son tantos (la mayoría de los experimentos tendrán más), no necesitamos ingresar todas las combinaciones posibles manualmente. Haz clic en *block_loop* en la descripción general para abrir su pestaña. Ahora haz clic en el botón 'Diseño factorial completo'. En el asistente de variables, simplemente define todas las variables escribiendo el nombre en la primera fila y los niveles en las filas debajo del nombre (ver %FigVariableWizard). Si seleccionas 'Ok', verás que *block_loop* se ha llenado con las 8 combinaciones posibles.

%--
figure:
 id: FigVariableWizard
 source: variable-wizard.png
 caption: |
  El asistente de variables de bucle en el Paso 3.
--%

En la tabla de bucle resultante, cada fila corresponde a una ejecución de *trial_sequence*. En nuestro caso, una ejecución de *trial_sequence* corresponde a un ensayo, cada fila en nuestra tabla de bucle corresponde a un ensayo. Cada columna corresponde a una variable, que puede tener un valor diferente en cada ensayo.

Pero aún no hemos terminado. Necesitamos agregar tres variables más: la ubicación del distractor, la respuesta correcta y la congruencia.

- __dist_pos__ -- En la primera fila de la primera columna vacía, ingrese 'dist_pos'. Esto agrega automáticamente una nueva variable experimental llamada 'dist_pos'. En las filas siguientes, ingrese '300' donde 'target_pos' es -300, y '-300' donde 'target_pos' es 300. En otras palabras, el objetivo y el distractor deben posicionarse opuestos entre sí.
- __correct_response__ -- Crea otra variable, en otra columna vacía, con el nombre 'correct_response'. Establece 'correct_response' en 'z' donde 'target_letter' es 'F' y en 'm' donde 'target_letter' es 'H'. Esto significa que el participante debe presionar la tecla 'z' si ve una 'F' y la tecla 'm' si ve una 'H'. (Siéntete libre de elegir teclas diferentes si 'z' y 'm' son incómodas en tu disposición de teclado; por ejemplo, 'w' y 'n' son mejores en teclados AZERTY).
- __congruency__ -- Crea otra variable con el nombre 'congruency'. Establece 'congruency' en 'congruente' donde 'target_pos' es '-300' y 'gaze_cue' está en 'izquierda', y donde 'target_pos' es '300' y 'gaze_cue' está en 'derecha'. En otras palabras, un ensayo es congruente si la cara mira al objetivo. Establece 'congruency' en 'incrongruente' para los ensayos en los que la cara mira al distractor. La variable 'congruency' no es necesaria para ejecutar el experimento; sin embargo, es útil para analizar los datos más adelante.

Necesitamos hacer una última cosa. 'Repeat' está actualmente configurado en '1.00'. Esto significa que cada ciclo se ejecutará una vez. Entonces, el bloque ahora consta de 8 ensayos, lo cual es un poco corto. Una longitud razonable para un bloque de ensayos es 24, así que establezca 'Repeat' en 3.00 (3 repeticiones x 8 ciclos = 24 ensayos). No necesitas cambiar 'Order', porque 'random' es exactamente lo que queremos.

El *block_loop* ahora se ve como %FigStep3. Recuerda guardar tu experimento regularmente.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%

<div class='info-box' markdown='1'>

__Background box__

__Consejo__ -- Puedes preparar tu tabla de bucle en tu programa de hoja de cálculo favorito y copiar-pegarla en la tabla variable LOOP.

__Consejo__ -- Puedes especificar tu tabla de bucle en un archivo separado (en formato `.xlsx` o `.csv`) y usar este archivo directamente. Para hacerlo, selecciona 'file' en 'Source'.

__Consejo__ -- Puedes establecer 'Repeat' en un número no entero. Por ejemplo, al establecer 'Repeat' en '0.5', solo se ejecutan la mitad de los ensayos (seleccionados aleatoriamente).

</div>

## Paso 4: Agregar imágenes y archivos de sonido al archivo de recursos

Para nuestros estímulos, utilizaremos imágenes de archivo. Además, reproduciremos un sonido si el participante comete un error. Para esto necesitamos un archivo de sonido.

Puedes descargar los archivos requeridos aquí (en la mayoría de los navegadores web, puedes hacer clic con el botón derecho en los enlaces y elegir 'Guardar enlace como' o una opción similar):

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)

Después de haber descargado estos archivos (en tu escritorio, por ejemplo), puedes agregarlos al archivo de recursos. Si el archivo de recursos no está visible (por defecto en el lado derecho de la ventana), haz clic en el botón 'Mostrar archivo de recursos' en la barra de herramientas principal (atajo: `Ctrl+P`). La forma más fácil de agregar los cuatro archivos al archivo de recursos es arrastrarlos desde el escritorio (o donde sea que los hayas descargado) al archivo de recursos. Alternativamente, puedes hacer clic en el botón '+' en el archivo de recursos y agregar archivos usando el diálogo de selección de archivos que aparece. El archivo de recursos se guardará automáticamente con tu experimento.

Tu archivo de recursos ahora se ve como %FigStep4. Recuerda guardar tu experimento regularmente.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%

## Paso 5: Llene la secuencia de ensayo con elementos

Un ensayo en nuestro experimento se ve de la siguiente manera:

1. __Punto de fijación__ -- 750 ms, elemento SKETCHPAD
2. __Mirada neutra__ -- 750 ms, elemento SKETCHPAD
3. __Señal de mirada__ -- 500 ms, elemento SKETCHPAD
4. __Objetivo__  -- 0 ms, elemento SKETCHPAD
5. __Recolección de respuestas__    -- elemento KEYBOARD_RESPONSE
6. __Reproducir un sonido si la respuesta fue incorrecta__ --  elemento SAMPLER
7. __Registrar respuesta en archivo__ -- elemento LOGGER

Haz clic en *trial_sequence* en la vista general para abrir la pestaña *trial_sequence*. Toma un SKETCHPAD en la barra de herramientas de elementos y arrástralo en *trial_sequence*. Repite esto tres veces más, de modo que *trial_sequence* contenga cuatro SKETCHPADs. A continuación, selecciona y añade un elemento KEYBOARD_RESPONSE, un elemento SAMPLER y un elemento LOGGER.

Nuevamente, cambiaremos el nombre de los nuevos elementos, para asegurarnos de que el *trial_sequence* sea fácil de entender. Cambiar el nombre:

- *new_sketchpad* a *fixation_dot*
- *new_sketchpad_1* a *neutral_gaze*
- *new_sketchpad_2* a *gaze_cue*
- *new_sketchpad_3* a *target*
- *new_keyboard_response* a *keyboard_response*
- *new_sampler* a *incorrect_sound*
- *new_logger* a *logger*

Por defecto, los elementos siempre se ejecutan, lo que se indica mediante la expresión run-if `True`. Sin embargo, queremos cambiar esto para el elemento *incorrect_sound*, que solo debe ejecutarse si se cometió un error. Para hacer esto, debemos cambiar la expresión "Ejecutar si" a `correct == 0` en la pestaña *trial_sequence*. Esto funciona porque el elemento *keyboard_response* crea automáticamente una variable `correct`, que se establece en `1` (correcto), `0` (incorrecto) o `undefined` (esto se basa en la variable `correct_response` que se definió en el Paso 3). El signo igual doble es la sintaxis de Python e indica que desea comparar si las dos cosas son iguales entre sí, en este caso, si la variable `correct` es igual a 0. Para cambiar una expresión run-if, haz doble clic en ella (atajo: `F3`).

El *trial_sequence* ahora se ve como %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "El *trial_sequence* al final del Paso 5."
--%

<div class='info-box' markdown='1'>

__Caja informativa__

__¿Qué es un elemento SKETCHPAD?__ -- Un SKETCHPAD se utiliza para presentar estímulos visuales: texto, formas geométricas, puntos de fijación, parches Gabor, etc. Puedes dibujar en el SKETCHPAD usando las herramientas de dibujo integradas.

__¿Qué es un elemento KEYBOARD_RESPONSE?__ -- Un elemento KEYBOARD_RESPONSE recopila una única respuesta del participante desde el teclado.

__¿Qué es un elemento SAMPLER?__ -- Un elemento SAMPLER reproduce un sonido desde un archivo de sonido.

__¿Qué es un elemento LOGGER?__ -- Un elemento LOGGER escribe datos en el archivo de registro. Esto es muy importante: si olvidas incluir un elemento LOGGER, no se registrarán datos durante el experimento.

__Consejo__ -- ¡Las variables y las expresiones condicionales "if" son muy poderosas! Para obtener más información sobre ellos, consulta:

- %link:manual/variables%

</div>

## Paso 6: Dibujar los elementos del sketchpad

Los elementos SKETCHPAD que hemos creado en el Paso 5 aún están en blanco. ¡Es hora de hacer un poco de dibujo!

__Establecer el color de fondo en blanco__

Haz clic en *fixation_dot* en el área de vista general para abrir su pestaña. El SKETCHPAD todavía es de color gris oscuro, mientras que las imágenes que hemos descargado tienen un fondo blanco. Vaya, olvidamos establecer el color de fondo del experimento en blanco (por defecto es gris oscuro). Haz clic en "Tutorial: Gaze cuing" en el área de vista general para abrir la pestaña "Propiedades generales". Cambia "Primer plano" a "negro" y "Fondo" a "blanco".

<div class='info-box' markdown='1'>

__Caja informativa__

__Consejo__ -- Para un control más detallado de los colores, también puedes usar la notación hexadecimal RGB (por ejemplo, `#FF000` para rojo), usar varios espacios de color o usar la herramienta de selección de color. Consulta también:

- %link:manual/python/canvas%

</div>

__Dibujar el punto de fijación__

Vuelve al *fixation_dot* haciendo clic en *fixation_dot* en la descripción general. Ahora selecciona el elemento de punto de fijación haciendo clic en el botón con la mira. Si mueves el cursor sobre el sketchpad, puedes ver las coordenadas de pantalla en la parte superior derecha. Establece el color (de primer plano) en 'negro'. Haz clic en el centro de la pantalla (0, 0) para dibujar un punto de fijación central.

Por último, cambia el campo "Duración" de "keypress" a "745", porque queremos que el punto de fijación se presente durante 750 ms. Espera... *¿por qué no especificamos simplemente una duración de 750 ms?* La razón es que la duración real de presentación en pantalla siempre se redondea hacia arriba a un valor que es compatible con la tasa de refresco de tu monitor. Esto puede sonar complicado, pero para la mayoría de los propósitos las siguientes reglas prácticas son suficientes:

1. Elige una duración que sea posible dada la tasa de refresco de tu monitor. Por ejemplo, si la tasa de refresco de tu monitor es de 60 Hz, significa que cada fotograma dura 16,7 ms (= 1000 ms/60 Hz). Por lo tanto, en un monitor de 60 Hz, siempre debes seleccionar una duración que sea múltiplo de 16.7 ms, como 16.7, 33.3, 50, 100, etc.
2. En el campo de duración del SKETCHPAD, especifica una duración que sea unos milisegundos menor de lo que estás buscando. Así que si quieres presentar un SKETCHPAD durante 50 ms, elige una duración de 45. Si quieres presentar un SKETCHPAD durante 1000 ms, elige una duración de 995. Y así sucesivamente.

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- Para una discusión detallada sobre el tiempo experimental, consulta:

- %link:timing%

__Consejo__ -- La duración de un SKETCHPAD puede ser un valor en milisegundos, pero también puedes ingresar 'keypress' o 'mouseclick' para recopilar una tecla del teclado o un clic del mouse, respectivamente. En este caso, un SKETCHPAD funcionará de manera muy similar a un elemento KEYBOARD_RESPONSE (pero con menos opciones).

__Consejo__ -- Asegúrate de que el color (de primer plano) esté configurado en negro. ¡De lo contrario, dibujarás blanco sobre blanco y no verás nada!

</div>

__Dibuja la mirada neutral__

Abre el SKETCHPAD *neutral_gaze*. Ahora selecciona la herramienta de imagen haciendo clic en el botón con el icono similar a un paisaje montañoso. Haz clic en el centro de la pantalla (0, 0). Aparecerá el cuadro de diálogo "Seleccionar archivo del grupo". Selecciona el archivo `gaze_neutral.png` y haz clic en el botón "Seleccionar". ¡La imagen de mirada neutral ahora te mirará fijamente desde el centro de la pantalla! Por último, como antes, cambia el campo "Duración" de "keypress" a "745". (¡Y ten en cuenta nuevamente que esto significa una duración de 750 ms en la mayoría de los monitores!)

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- OpenSesame puede manejar una amplia variedad de formatos de imagen. Sin embargo, algunos formatos `.bmp` (no estándar) se sabe que causan problemas. Si encuentras que una imagen `.bmp` no se muestra, puedes convertirla a un formato diferente, como `.png` . Puedes convertir imágenes fácilmente con herramientas gratuitas como [GIMP].
</div>

__Dibuja la señal de la mirada__

Abre el SKETCHPAD *gaze_cue*, y nuevamente selecciona la herramienta de imagen. Haz clic en el centro de la pantalla (0, 0) y selecciona el archivo `gaze_left.png`.

¡Pero aún no hemos terminado! Porque la señal de la mirada no siempre debe ser "izquierda", sino que debe depender de la variable `gaze_cue`, que hemos definido en el Paso 3. Sin embargo, al dibujar la imagen `gaze_left.png` en el SKETCHPAD, hemos generado un script que solo necesita una modificación mínima para asegurarse de que se muestre la imagen adecuada. Haz clic en el botón "Seleccionar vista" en la parte superior derecha de la pestaña *gaze_cue* y selecciona "Ver script". Ahora verás el script que corresponde al sketchpad que acabamos de crear:

~~~ .python
set duration keypress
set description "Displays stimuli"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Lo único que necesitamos hacer es reemplazar `gaze_left.png` por `gaze_{gaze_cue}.png`. Esto significa que OpenSesame utiliza la variable `gaze_cue` (que tiene los valores `left` y `right`) para determinar qué imagen se debe mostrar.

Mientras estamos en eso, también podríamos cambiar la duración a '495' (¡redondeado a 500!). El script ahora se ve así:

~~~ .python
set duration 495
set description "Muestra estímulos"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
~~~

Haz clic en el botón 'Aplicar' en la parte superior derecha para aplicar los cambios al script y volver a los controles regulares del elemento. OpenSesame te advertirá que la imagen no se puede mostrar, porque se define mediante variables, y se mostrará una imagen marcador de posición. No te preocupes, ¡la imagen correcta se mostrará durante el experimento!

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- El inspector de variables (atajo: `Ctrl+I`) es una forma poderosa de averiguar qué variables se han definido en tu experimento y qué valores tienen (ver %FigVariableInspector). Cuando tu experimento no se está ejecutando, la mayoría de las variables aún no tienen un valor. Pero cuando ejecutas tu experimento en una ventana, mientras tienes visible el inspector de variables, puedes ver cómo cambian las variables en tiempo real. Esto es muy útil para depurar tu experimento.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: "El inspector de variables es una forma conveniente de obtener una descripción general de las variables que existen en tu experimento."
--%

</div>

__Dibujar el objetivo__

Queremos que tres objetos sean parte de la pantalla del objetivo: la letra objetivo, la letra distractora y la señal de mirada (ver %FigGazeCuing). Como antes, comenzaremos creando una pantalla estática utilizando el editor SKETCHPAD. Después de esto, solo necesitaremos hacer cambios menores en el script para que la pantalla exacta dependa de las variables.

Haz clic en *target* en la descripción general para abrir la pestaña de objetivo y, como antes, dibuja la imagen `gaze_left.png` en el centro de la pantalla. Ahora selecciona la herramienta de dibujo de texto haciendo clic en el botón con el ícono 'A'. Cambia el color de primer plano a 'negro' (si aún no lo está). El tamaño de fuente predeterminado es 18 px, que es un poco pequeño para nuestro propósito, así que cambia el tamaño de fuente a 32 px. Ahora haz clic en (-320, 0) en el SKETCHPAD (la coordenada X no necesita ser exactamente 320, ya que de todos modos cambiaremos esto a una variable). Ingresa "{target_letter}" en el cuadro de diálogo que aparece, para dibujar la letra objetivo (al dibujar texto, puedes usar variables directamente). De manera similar, haz clic en (320, 0) y dibuja una 'X' (el distractor siempre es una 'X').

Ahora abre el editor de scripts haciendo clic en el botón 'Seleccionar vista' en la parte superior derecha de la pestaña y seleccionando 'Ver script'. El script se ve así:

~~~ .python
set duration keypress
set duration keypress
set description "Muestra estímulos"
draw image center=1 file="gaze_left.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x=-320 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x=320 y=0 z_index=0
~~~

Como antes, cambia `gaze_left.png` a `gaze_{gaze_cue}.png`. También necesitamos hacer que la posición del objetivo y el distractor dependa de las variables `target_pos` y `dist_pos` respectivamente. Para hacer esto, simplemente cambia `-320` a `{target_pos}` y `320` a `{dist_pos}`. Asegúrate de dejar el `0`, que es la coordenada Y. El script ahora se ve así:

~~~ .python
set duration keypress
set description "Muestra estímulos"
draw image center=1 file="gaze_{gaze_cue}.png" scale=1 show_if=True x=0 y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text="{target_letter}" x={target_pos} y=0 z_index=0
draw textline center=1 color=black font_bold=no font_family=mono font_italic=no font_size=32 html=yes show_if=True text=X x={dist_pos} y=0 z_index=0
~~~

Haz clic en el botón 'Aplicar' para aplicar el script y volver a los controles regulares del elemento.

Finalmente, establece el campo 'Duration' en '0'. Esto no significa que el objetivo se presente solo durante 0 ms, sino que el experimento avanzará al siguiente elemento (el *keyboard_response*) de inmediato. Como el *keyboard_response* espera una respuesta, pero no cambia lo que se muestra en la pantalla, el objetivo permanecerá visible hasta que se dé una respuesta.

Recuerda guardar tu experimento regularmente.

<div class='info-box' markdown='1'>

__Caja de información__

__Consejo__ -- Cada elemento de un SKETCHPAD tiene una opción 'Mostrar si' que especifica cuándo se debe mostrar el elemento. Puedes usar esto para ocultar/mostrar elementos dependiendo de ciertas variables, similar a las declaraciones run-if en una secuencia.

__Consejo__ -- Asegúrate de que el color (primario) esté en negro. De lo contrario, dibujarás blanco sobre blanco y no verás nada.

</div>

## Paso 7: Configurar el elemento de respuesta del teclado

Haz clic en *keyboard_response* en la descripción general para abrir su pestaña. Verás tres opciones: Respuesta correcta, Respuestas permitidas, Tiempo de espera (Timeout) y tipo de evento.

Ya hemos establecido la variable `correct_response` en el paso 3. A menos que especifiquemos explícitamente una respuesta correcta, OpenSesame utiliza automáticamente la variable `correct_response` si está disponible. Por lo tanto, no necesitamos cambiar el campo 'Respuesta correcta' aquí.

Sí necesitamos establecer las respuestas permitidas. Ingresa 'z;m' en el campo de las respuestas permitidas (o otras teclas si has elegido teclas de respuesta diferentes). El punto y coma se utiliza para separar las respuestas. El KEYBOARD_RESPONSE ahora solo acepta las teclas 'z' y 'm'. Todos los demás pulsaciones de teclas se ignoran, con la excepción de 'escape', que pausa el experimento.

También queremos establecer un tiempo de espera (timeout). '2000' (ms) es un buen valor.

No necesitamos cambiar el tipo de evento, porque queremos que el participante responda presionando una tecla (keypress, el valor predeterminado) y no soltándola (keyrelease).

El KEYBOARD_RESPONSE ahora se ve como %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "El KEYBOARD_RESPONSE al final del Paso 7."
--%

<div class='info-box' markdown='1'>

__Caja de información__

__Consejo__ -- De forma predeterminada, el KEYBOARD_RESPONSE utilizará la variable `correct_response` para determinar si una respuesta fue correcta. Pero también puede usar una variable diferente. Para hacer esto, ingresa el nombre de una variable entre llaves (`{mi_variable}`) en el campo de respuesta correcta.

__Consejo__ -- Si 'descartar pulsaciones de teclas pendientes' está habilitado (lo está de forma predeterminada), todas las pulsaciones de teclas pendientes se descartan cuando se llama al elemento KEYBOARD_RESPONSE. Esto evita efectos de arrastre, que podrían ocurrir si el participante presiona accidentalmente una tecla durante una parte del ensayo que no es de respuesta.

__Consejo__ -- Para usar teclas especiales, como '/' o la tecla de flecha hacia arriba, puedes usar nombres de teclas (por ejemplo, 'up' y 'space') o caracteres asociados (por ejemplo, '/' y ']'). El botón 'Lista de teclas disponibles' proporciona una descripción general de todos los nombres de teclas válidos.

</div>

## Paso 8: Configurar el elemento incorrecto (sampler)

El elemento *incorrect_sound* no requiere mucho trabajo: solo necesitamos seleccionar el sonido que se reproducirá. Haz clic en *incorrect_sound* en la descripción general para abrir su pestaña. Haz clic en el botón 'Examinar' (Browse) y selecciona `incorrect.ogg` del grupo de archivos.

El sampler ahora se ve como %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: "El elemento *incorrect_sound* al final del Paso 8."
--%

<div class='info-box' markdown='1'>

__Caja de información__

__Consejo__ -- Puedes usar variables para especificar qué sonido se debe reproducir utilizando un nombre de variable entre llaves como (parte de) el nombre del archivo. Por ejemplo: `{una_palabra}.ogg`

__Consejo__ -- El SAMPLER maneja archivos en formato `.ogg`, `.mp3`, y `.wav`. Si tienes archivos de sonido en otro formato, [Audacity] es una excelente herramienta gratuita para convertir archivos de sonido (y mucho más).

</div>

## Paso 9: Configurar el registrador de variables

En realidad, no necesitamos configurar el registrador de variables (LOGGER), pero echemos un vistazo de todos modos. Haga clic en *logger* en la vista general para abrir su pestaña. Verá que la opción 'Registrar automáticamente todas las variables' está seleccionada. Esto significa que OpenSesame registra todo, lo cual está bien.

<div class='info-box' markdown='1'>

__Recuadro de información__

__Consejo__ -- Si desea que sus archivos de registro estén limpios, puede desactivar la opción 'Registrar automáticamente todas las variables' y seleccionar variables manualmente, ya sea ingresando nombres de variables manualmente ('Agregar variable personalizada'), o arrastrando variables desde el inspector de variables a la tabla LOGGER. También puede dejar habilitada la opción 'Registrar automáticamente todas las variables' y excluir las variables que no le interesen.

__El consejo supremo__ -- ¡Siempre verifique tres veces si todas las variables necesarias están registradas en su experimento! La mejor manera de verificar esto es ejecutar el experimento e investigar los archivos de registro resultantes.

</div>

## Paso 10: Dibujar el elemento de retroalimentación

Después de cada bloque de pruebas, queremos presentar una retroalimentación al participante para informarle qué tan bien lo está haciendo. Por lo tanto, en el Paso 2, agregamos un elemento de retroalimentación (FEEDBACK), llamado simplemente *feedback* al final de *block_sequence*.

Haga clic en *feedback* en la vista general para abrir su pestaña, seleccione la herramienta de dibujo de texto, cambie el color de primer plano a 'negro' (si aún no lo está) y haga clic en (0, 0). Ahora ingrese el siguiente texto:

```texto
Fin del bloque

Tu tiempo de respuesta promedio fue de {avg_rt} ms
Tu precisión fue del {acc} %

Presiona cualquier tecla para continuar
```

Como queremos que el elemento de retroalimentación permanezca visible el tiempo que el participante desee (es decir, hasta que presione una tecla), dejamos el campo 'Duración' establecido en 'keypress'.

El elemento de retroalimentación ahora se ve como %FigStep_10.

%--
figure:
 id: FigStep_10
 source: step10.png
 caption: "El elemento de retroalimentación al final del Paso 10."
--%

<div class='info-box' markdown='1'>

__Recuadro de información__

__¿Qué es un elemento de retroalimentación?__ -- Un elemento de retroalimentación (FEEDBACK) es casi idéntico a un elemento de SKETCHPAD. La única diferencia es que un elemento de FEEDBACK no se prepara con anticipación. Esto significa que puede usarlo para presentar retroalimentación, lo que requiere información actualizada sobre la respuesta de un participante. No debe usar elementos de FEEDBACK para presentar pantallas críticas en cuanto al tiempo, porque el hecho de que no estén preparados con antelación significa que sus propiedades de tiempo no son tan buenas como las del elemento SKETCHPAD. Ver también:

- %link:visual%

__Retroalimentación y variables__ -- Los elementos de respuesta controlan automáticamente la precisión y el tiempo de respuesta promedio del participante en las variables 'acc' (sinónimo: 'accuracy') y 'avg_rt' (sinónimo: 'average_response_time') respectivamente. Ver también:

- %link:manual/variables%

__Consejo__ -- ¡Asegúrate de que el color (primer plano) esté configurado en negro! De lo contrario, dibujarás blanco sobre blanco y no verás nada.

</div>

## Paso 11: Establecer la duración de la fase de práctica y la fase experimental

Anteriormente creamos los elementos *practice_loop* y *experiment_loop*, que ambos llaman a *block_sequence* (es decir, un bloque de pruebas). Sin embargo, en este momento solo llaman a *block_sequence* una vez, lo que significa que tanto la fase de práctica como la experimental constan de un solo bloque de pruebas.

Haga clic en *practice_loop* para abrir su pestaña y establecer 'Repeat' en '2.00'. Esto significa que la fase de práctica consta de dos bloques.

Haga clic en *experimental_loop* para abrir su pestaña y establecer 'Repeat' en '8.00'. Esto significa que la fase experimental consta de ocho bloques.

<div class='info-box' markdown='1'>

__Recuadro de información__

__Consejo__ -- Puede crear una variable 'practice' en *practice_loop* y *experimental_loop* y configurarla en 'yes' y 'no' respectivamente. Esta es una forma fácil de analizar qué pruebas formaron parte de la fase de práctica.

</div>

## Paso 12: Escribir las instrucciones, end_of_practice y end_of_experiment formularios

Creo que puedes manejar este paso por ti mismo. Simplemente abre los elementos apropiados y añade texto para presentar instrucciones, un mensaje de fin de práctica y un mensaje de fin de experimento.

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- Puedes usar un subconjunto de etiquetas HTML para dar formato a tu texto. Por ejemplo, *&lt;b&gt;esto estará en negrita&lt;b&gt;* y *&lt;span color='red'&gt;esto estará en rojo&lt;span&gt;*. Para obtener más información, consulta:

- %link:texto%

</div>

## Paso 13: ¡Ejecutar el experimento!

¡Terminaste! Haz clic en los botones 'Ejecutar en ventana' (atajo: `Ctrl+W`) o 'Ejecutar a pantalla completa' (atajo: `Ctrl+R`) en la barra de herramientas para ejecutar tu experimento.

<div class='info-box' markdown='1'>

__Caja de fondo__

__Consejo__ -- Una prueba de ejecución es aún más rápida al hacer clic en el botón naranja 'Ejecutar en ventana' (atajo: `Ctrl+Shift+W`), que no te pregunta cómo guardar el archivo de registro (y por lo tanto solo debe ser utilizado para fines de prueba).

</div>


## Entendiendo los errores

Ser capaz de entender los mensajes de error es una habilidad crucial cuando se trabaja con OpenSeame. Después de todo, ¡un experimento recién construido rara vez se ejecuta inmediatamente sin errores!

Digamos que cometimos un error durante uno de los pasos anteriores. Al intentar ejecutar el experimento, obtenemos el siguiente mensaje de error (%FigErrorMessage):

%--
figure:
 id: FigErrorMessage
 source: error-message.png
 caption: "Un mensaje de error en OpenSesame."
--%

El mensaje de error comienza con un nombre, en este caso `FStringError`, que indica el tipo general de error. A esto le sigue un breve texto explicativo, en este caso 'Error al evaluar la expresión f-string en el siguiente texto: gaze_{gaze_ceu}.png`. Incluso sin entender qué es un f-string (es una cadena que contiene código Python entre llaves), está claro que hay algo mal con el texto '{gaze_ceu}.png'.

El mensaje de error también indica que el error proviene de la fase de preparación del elemento *gaze_cue*.

Por último, el mensaje de error indica qué fue lo que salió mal específicamente al evaluar el texto 'gaze_{gaze_ceu}.png': el nombre 'gaze_ceu' no está definido.

Mientras lees cuidadosamente el mensaje de error, la causa y la solución probablemente ya te vinieron a la mente: cometimos un simple error tipográfico en el elemento *gaze_cue*, escribiendo '{gaze_ceu}' en lugar de '{gaze_cue}'! Y esto resultó en un error porque no hay ninguna variable con el nombre `gaze_ceu`. Esto se puede solucionar fácilmente abriendo el script del elemento *gaze_cue* y corrigiendo el error tipográfico.


## Finalmente: Algunas consideraciones generales sobre la sincronización y la selección del backend

En la pestaña 'Propiedades generales' del experimento (la pestaña que abres al hacer clic en el nombre del experimento), puedes seleccionar un backend. El backend es la capa de software que controla la pantalla, los dispositivos de entrada, el sonido, etc. La mayoría de los experimentos funcionan con todos los backends, pero hay razones para preferir un backend por encima de otro, principalmente relacionadas con la sincronización. Actualmente hay cuatro backends (dependiendo de tu sistema, es posible que no todos estén disponibles):

- __psycho__ -- un backend acelerado por hardware basado en PsychoPy [(Peirce, 2007)][referencias]. Este es el predeterminado.
- __xpyriment__ -- un backend acelerado por hardware basado en Expyriment [(Krause & Lindeman, 2013)][referencias]
- __legacy__ -- un backend 'seguro', basado en PyGame. Proporciona un rendimiento fiable en la mayoría de las plataformas, pero, debido a la falta de aceleración por hardware, sus propiedades de sincronización no son tan buenas como las de los otros backends.
- __osweb__ -- ejecuta los experimentos en un navegador [(Mathôt & March, 2022)][referencias].

Ver también:

- %link:backends%
- %link:timing%


## Referencias

<div class='reference' markdown='1'>

Brand, A., & Bradley, M. T. (2011). Evaluación de los efectos de la variación técnica en los resultados estadísticos de los experimentos web que miden los tiempos de respuesta. *Social Science Computer Review*. doi:10.1177/0894439311415604

Damian, M. F. (2010). ¿La variabilidad en el rendimiento humano supera la imprecisión en dispositivos de respuesta como los teclados de computadora? *Behavior Research Methods*, *42*, 205-211. doi:10.3758/BRM.42.1.205

Friesen, C. K., & Kingstone, A. (1998). ¡Los ojos lo tienen! La orientación refleja se activa por la mirada no predictiva. *Psychonomic Bulletin & Review*, *5*, 490-495. doi:10.3758/BF03208827

Krause, F., & Lindemann, O. (2013). Expyriment: una biblioteca de Python para experimentos cognitivos y neurocientíficos. *Behavior Research Methods*. doi:10.3758/s13428-013-0390-6

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: un constructor de experimentos gráfico de código abierto para las ciencias sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Realización de experimentos lingüísticos en línea con OpenSesame y OSWeb. *Language Learning*. doi:10.1111/lang.12509

Peirce, J. W. (2007). PsychoPy: software de psicofísica en Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017

Ulrich, R., & Giray, M. (1989). Resolución de tiempo de los relojes: efectos en la medición del tiempo de reacción: buenas noticias para los relojes malos. *British Journal of Mathematical and Statistical Psychology*, *42*(1), 1-12. doi:10.1111/j.2044-8317.1989.tb01111.x

</div>
