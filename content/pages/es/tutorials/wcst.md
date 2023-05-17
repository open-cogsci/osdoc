title: Test de Clasificación de Tarjetas de Wisconsin
hash: c76af36f9cc3e81cddcf0d468272405a3bebc0c73931400b287f211d586c3db3
locale: es
language: Spanish

[TOC]


## Los pasos básicos


%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  La Prueba de Clasificación de Tarjetas de Wisconsin (WCST) es una prueba neuropsicológica de funciones ejecutivas.
--%


En este tutorial, implementarás la Prueba de Clasificación de Tarjetas de Wisconsin (WCST) y aprenderás cómo puedes ejecutar esta prueba en línea con OSWeb.

En el WCST, los participantes ven cuatro cartas de estímulo, que difieren en tres dimensiones: color (rojo, verde, azul, amarillo), forma (círculo, estrella, triángulo, cruz) y número de formas (uno, dos, tres o cuatro). Los participantes también ven una sola carta de respuesta, que también tiene un color, forma y número.

La tarea del participante es hacer coincidir la carta de respuesta con la carta de estímulo correcta, basándose en una dimensión específica (por ejemplo, color) o *regla de coincidencia*. Inicialmente, el participante no sabe en qué dimensión hacer coincidir, y su tarea es descubrir la regla de coincidencia mediante prueba y error.

Para complicar aún más las cosas, la regla de coincidencia cambia después de cada cinco respuestas correctas. Por lo tanto, el participante necesita actualizar de manera flexible su regla de coincidencia.


### Paso 1: Descarga e inicia OpenSesame

OpenSesame está disponible para Windows, Linux y Mac OS. Este tutorial está escrito para OpenSesame 4.0 o superior.

Cuando inicies OpenSesame, se te dará a elegir entre experimentos de plantilla y, si los hay, una lista de experimentos abiertos recientemente (ver %FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La ventana de OpenSesame al iniciar.
--%

La *Plantilla ampliada* proporciona un buen punto de partida para crear muchos experimentos que utilizan una estructura de bloque de prueba. Sin embargo, en este tutorial crearemos todo el experimento desde cero y utilizaremos la "plantilla predeterminada", que ya está cargada cuando se inicia OpenSesame (%FigDefaultTemplate). Por lo tanto, simplemente cierra las pestañas "¡Empezar!" y "¡Bienvenido!" (si se muestran).

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  La estructura de la "Plantilla predeterminada" vista en el área de descripción general.
--%


### Paso 2: Agrega un block_loop y trial_sequence

La plantilla predeterminada comienza con tres elementos: un NOTEPAD llamado *getting_started*, un SKETCHPAD llamado *welcome* y una SECUENCIA llamada *experiment*. No necesitamos *getting_started* y *welcome*, así que eliminémoslos de inmediato. Para hacerlo, haz clic derecho en estos elementos y selecciona "Eliminar". No elimines *experiment*, ya que es la entrada del experimento (es decir, el primer elemento que se llama cuando se inicia el experimento).

Nuestro experimento tendrá una estructura muy simple. En la parte superior de la jerarquía hay un LOOP, al que llamaremos *block_loop*. El *block_loop* es el lugar donde definiremos nuestras variables independientes. Para agregar un LOOP a tu experimento, arrastra el ícono LOOP desde la barra de herramientas de elementos al elemento *experiment* en el área de descripción general.

Un elemento LOOP necesita otro elemento para ejecutarse; generalmente, y también en este caso, es una SECUENCIA. Arrastra el elemento SECUENCIA desde la barra de herramientas de elementos al elemento *new_loop* en el área de descripción general. OpenSesame preguntará si deseas insertar la SECUENCIA en o después del LOOP. Selecciona "Insertar en new_loop".

Por defecto, los elementos tienen nombres como *new_sequence*, *new_loop*, *new_sequence_2*, etc. Estos nombres no son muy informativos y es una buena práctica cambiarlos. Los nombres de los elementos deben constar de caracteres alfanuméricos y / o guiones bajos. Para cambiar el nombre de un elemento, haz doble clic en el elemento en el área de descripción general. Cambia el nombre de *new_sequence* a *trial_sequence* para indicar que corresponderá a una sola prueba. Cambia el nombre de *new_loop* a *block_loop* para indicar que corresponderá a un bloque de pruebas.

Por último, haz clic en "Nuevo experimento" para abrir la pestaña de Propiedades generales. Haz clic en el título del experimento y cambia el nombre a "Prueba de Clasificación de Tarjetas de Wisconsin".

El área de descripción general de nuestro experimento ahora se ve como en %FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  The overview area at the end of Step 2.
--%

### Paso 3: Importar imágenes y archivos de sonido

Para este experimento, utilizaremos imágenes de las cartas. Puede descargarlas desde aquí:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Descargue `stimuli.zip` y extráigalo en algún lugar (en su escritorio, por ejemplo). A continuación, en OpenSesame, haga clic en el botón 'Mostrar archivo del grupo' en la barra de herramientas principal (o: Menú → Ver → Mostrar archivo del grupo). Esto mostrará el archivo del grupo, por defecto en el lado derecho de la ventana. La forma más fácil de agregar los estímulos al archivo del grupo es arrastrándolos desde el escritorio (o desde donde los haya extraído) al archivo del grupo. Alternativamente, puede hacer clic en el botón '+' en el grupo de archivos y agregar archivos utilizando el cuadro de diálogo de selección de archivos que aparece. El grupo de archivos se guardará automáticamente con su experimento.

Después de haber agregado todos los estímulos, su grupo de archivos se verá como en %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  The file pool containing the stimuli.
--%

### Paso 4: Crear una pantalla de cartas estática

Para empezar, crearemos una pantalla con cuatro cartas de estímulo y una carta de respuesta. Sin embargo, las cartas que se muestran no dependerán, por ahora, de las variables; es decir, crearemos una pantalla *estática*.

Arrastre un SKETCHPAD a *trial_sequence* y renómbrelo a *card_display*. Utilice la herramienta de imagen para dibujar cuatro cartas en una fila horizontal cerca de la parte superior de la pantalla; estas serán las cartas de estímulo. Dibuje una sola carta cerca de la parte inferior de la pantalla; esta será la carta de respuesta. También agregue algo de texto para indicar a los participantes qué tienen que hacer, es decir, presionar `a`, `b`, `c` o `d` para indicar qué carta de estímulo coincide con la carta de respuesta. El texto exacto, el diseño y las cartas dependen de usted. Consejos: puede utilizar la opción *scale* para ajustar el tamaño de las cartas; puede cambiar el color de fondo en la pestaña Propiedades generales, a la que puede acceder haciendo clic en el elemento de nivel superior del experimento.

Para mí, el resultado se ve así:

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  A SKETCHPAD with statically defined cards.
--%

### Paso 5: Hacer que la carta de respuesta sea variable

Actualmente siempre mostramos la misma carta de respuesta (en el ejemplo de arriba, un único triángulo azul). Pero, por supuesto, queremos mostrar una carta de respuesta diferente en cada ensayo. Para hacerlo, primero necesitamos definir las variables que determinan qué carta de respuesta mostraremos. Haremos esto en *block_loop*.

Abra *block_loop*. La tabla LOOP ahora está vacía. Para determinar el color, la forma y el número de la carta de respuesta, podríamos crear manualmente tres columnas (`response_color`, `response_shape` y `response_number`) y 64 filas para todas las combinaciones posibles de colores, formas y números. Pero eso sería mucho trabajo. En cambio, utilizaremos el asistente de diseño factorial completo, al que puede acceder haciendo clic en el botón "Diseño factorial completo". (Un diseño factorial completo es un diseño en el que ocurren todas las combinaciones posibles de niveles de variables). En este asistente, cree una columna para cada una de las tres variables y, en las celdas siguientes, ingrese los posibles valores para esa variable (vea %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  The full-factorial-design wizard allows you to easily generate large LOOP tables that correspond to full-factorial designs.
--%

A continuación, haga clic en el botón Aceptar. El *block_loop* ahora contiene las 64 combinaciones de colores, números y formas (ver %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  The *block_loop* at the end of step 5.
--%

Ahora regresa al *card_display*. Cada elemento en OpenSesame está definido a través de un script. Este script es generado automáticamente por la interfaz de usuario. A veces puede ser conveniente (¡o incluso necesario!) editar este script directamente. La razón más común para editar el script de un elemento es agregar variables al script, ¡que también es lo que haremos ahora!

Para ver el script, haz clic en el botón 'Ver' y selecciona 'Ver script'. (El botón de vista es el botón central en la parte superior derecha de los controles del elemento). Esto abrirá un editor de scripts.

El script para *card_display* consiste principalmente en comandos `draw`, que definen cada una de las cinco cartas y también los diversos elementos de texto. Ubica la línea que corresponde a la carta de respuesta. Puedes encontrarla mirando la coordenada Y, que debería ser positiva (es decir, en la parte inferior de la pantalla) o mirando el nombre del archivo de imagen.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Ahora mismo, en mi ejemplo, el archivo de imagen de la carta de respuesta siempre es `"1-blue-triangle.png"`. Pero, por supuesto, no siempre queremos mostrar un solo triángulo azul. En su lugar, queremos que el archivo de imagen dependa de las variables que hemos definido en el *block_loop*. Para hacerlo, sustituye el número por `{response_number}`, el color por `{response_color}` y la forma por `{response_shape}`: (Las llaves indican que se refieren a nombres de variables.)

```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Haz clic en Aplicar para aceptar los cambios en el script. La carta de respuesta ahora ha sido reemplazada por un icono de interrogación. Esto se debe a que OpenSesame no sabe cómo mostrar una vista previa de una imagen que se ha definido usando variables. Pero no te preocupes: ¡la imagen se mostrará cuando ejecutes el experimento!

### Paso 6: Haz que las tarjetas de estímulo sean variables

Las tarjetas de estímulo deben seleccionarse más o menos al azar, pero cada color, forma y número solo debe ocurrir una vez; es decir, nunca debería haber dos cartas rojas o dos cartas con triángulos. (Si lo hubiera, el procedimiento de coincidencia se volvería ambiguo.) Para lograr esto, podemos usar *horizontal shuffling*, que es una función poderosa pero inusual del elemento LOOP.

- %link:loop%

Primero, abre el *block_loop* y crea 12 (!) nuevas columnas para definir las tarjetas de estímulo: `color1`, para el color de la primera carta, `color2`, `color3`, `color4`, y `shape1`... `shape4`, y `number1`... `number4`. Cada columna tiene el mismo valor en cada fila (ver %FigLoopTable2).

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  The *block_loop* durante el paso 6.
--%

¡Pero aún no hemos terminado! Ahora mismo, la primera carta de estímulo siempre es un círculo rojo individual, la segunda son dos triángulos azules, etc. Para aleatorizar esto, le decimos a OpenSesame que intercambie al azar (horizontal shuffle) los valores de las cuatro variables de color, las cuatro variables de forma y las cuatro variables de número. Para hacerlo, abre el script para el *block_loop*. En la penúltima línea (justo antes de `run trial_sequence`) agrega los siguientes comandos:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Haz clic en Aplicar para aceptar el script. Para ver si esto ha funcionado, haz clic en el botón Vista previa. Esto mostrará una vista previa de cómo se aleatorizará la tabla LOOP durante el experimento. ¿Se ve bien?

Ahora regresa al *card_display* y haz que la imagen de la primera carta de estímulo dependa de la variable `color1`, `shape1` y `number1`, y análogamente para las otras tarjetas de estímulo. (Si no estás seguro de cómo hacer esto, visita el paso 5.)


### Paso 7: Determina la respuesta correcta (para una regla de coincidencia)

Por ahora, vamos a suponer que los participantes siempre coinciden por la forma. (Una de las Tareas Extra es mejorar esto.)

En este momento, la duración de *card_display* está configurada en 'keypress'. Esto significa que el *card_display* se muestra hasta que se presiona una tecla, pero no proporciona control sobre cómo se maneja esta presión de tecla. Por lo tanto, cambie la duración a 0 e inserte un KEYBOARD_RESPONSE directamente después del *card_display*. Cambie el nombre del KEYBOARD_RESPONSE a *press_a* y especifique que la respuesta correcta es 'a' y que las respuestas permitidas son 'a; b; c; d'.

Pero esto no es suficiente. En este momento hay un solo elemento de respuesta que supone que la respuesta correcta siempre es 'a'. Todavía no hemos especificado *cuándo* la respuesta correcta es 'a', ni hemos considerado pruebas en las que la respuesta correcta es 'b', 'c' o 'd'.

Para lograr esto, primero cree tres elementos KEYBOARD_RESPONSE más: *press_b*, *press_c* y *press_d*. Todos son iguales, excepto por la respuesta correcta, que está definida para cada uno de ellos por separado y debe ser respectivamente 'b', 'c' y 'd'.

Finalmente, en el *trial_sequence*, use declaraciones Run If para decidir bajo qué condición cada uno de los cuatro elementos KEYBOARD_RESPONSE debe ejecutarse (decidiendo cuál es la respuesta correcta). Para *press_a*, la condición es que `shape1` debe ser igual a `response_shape`. ¿Por qué? Bueno, porque eso significa que la forma de la primera tarjeta de estímulo es igual a la forma de la tarjeta de respuesta, y en ese caso la respuesta correcta es 'a'. Esta condición corresponde a la siguiente declaración run-if: `shape1 = response_shape`. Las declaraciones run-if para los otros elementos de KEYBOARD_RESPONSE son análogas (ver %FigTrialSequence1).

### Paso 8: dar feedback al participante

OpenSesame automáticamente lleva un registro de si una respuesta fue correcta o no, estableciendo la variable `correct` en respectivamente 1 o 0. (Siempre que haya especificado la respuesta correcta, como hemos hecho en el paso 7). Podemos usar esto para dar feedback al participante sobre si respondieron correctamente o no.

Para hacer esto, agregue dos nuevos SKETCHPAD al *trial_sequence* y llámelos *correct_feedback* e *incorrect_feedback*. Luego, especifique cuál de los dos se ejecutará utilizando una declaración run-if (ver %FigTrialSequence2).

Finalmente, agregue contenido útil a ambos SKETCHPAD. Por ejemplo, para *correct_feedback* podría usar un punto de fijación verde y para *incorrect_feedback* podría usar un punto de fijación rojo, en ambos casos mostrado por 500 ms (es decir, estableciendo la duración del SKETCHPAD en 500). Los puntos de colores son una forma agradable y discreta de proporcionar feedback.

### Paso 9: probar el experimento

Ahora ha creado una implementación básica (¡pero incompleta!) Del Wisconsin Card Sorting Test. (Completará la implementación como parte de las Tareas adicionales a continuación).

Para probar el experimento, puede hacer clic en el botón de ejecución rápida (las flechas dobles azules) o en el botón Ejecutar en pantalla completa (la flecha verde).


## Tareas extra

### Extra 1 (fácil): agregar un registrador

OpenSesame no registra automáticamente los datos. En su lugar, debe agregar explícitamente un elemento `logger` a su experimento. En un experimento basado en pruebas, un `logger` generalmente es el último elemento del *trial_sequence*, por lo que registra todos los datos que se recopilaron durante la prueba.

En este momento, nuestro WCST no registra ningún dato. ¡Hora de solucionarlo!

### Extra 2 (fácil): inspeccione el archivo de datos

 *Requiere que haya completado Extra 1*.

Dele al experimento una prueba rápida. Ahora inspeccione el archivo de registro en un programa como Excel, LibreOffice Calc o JASP. Identifique las variables relevantes y piense en cómo podría analizar los resultados.

__Pro-tip:__ Ajusta el valor de repetición del *block_loop* a 0.1 para reducir la cantidad de ensayos durante las pruebas.

### Extra 3 (fácil): Añadir instrucciones y pantalla de despedida

Un buen experimento viene con instrucciones claras. Y un experimento cortés se despide de los participantes cuando terminan. Puedes usar un SKETCHPAD o un FORM_TEXT_DISPLAY para hacer esto.

### Extra 4 (medio): Establecer la respuesta correcta y la regla de coincidencia a través de JavaScript

Para incluir scripting en OSWeb, puedes usar el elemento INLINE_JAVASCRIPT, que admite JavaScript. (¡Pero actualmente no ofrece toda la funcionalidad que ofrece el INLINE_SCRIPT regular de Python!). Consulta
[aquí](https://osdoc.cogsci.nl/4.0/manual/javascript/about/) para más detalles.

Hasta ahora, la regla de coincidencia siempre es coincidir por forma. Para cambiar esto, agrega un elemento INLINE_JAVASCRIPT al inicio del experimento y utiliza el siguiente script (en la fase *prepare*) para establecer aleatoriamente la variable `matching_rule` a 'forma', 'número' o 'color'.

```javascript
function choice(choices) {
    // JavaScript no tiene una función de elección incorporada, por lo que la definimos
    // aquí.
    // use let para introducir una nueva variable temporal
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}


// use var para introducir una nueva variable global
var matching_rule = choice(['shape', 'number', 'color'])
```

Ahora agrega otro elemento INLINE_JAVASCRIPT al inicio de la *trial_sequence*. En la fase *prepare*, añade un script para establecer la variable `correct_response` en 'a', 'b', 'c' o 'd'. Para hacerlo, necesitas una serie de declaraciones `if`, que primero miren la regla de coincidencia y luego miren qué forma corresponde a la forma de respuesta (para la regla de coincidencia de formas) o qué color corresponde al color de respuesta (para la regla de coincidencia de color) etc.

Para comenzar, aquí tienes parte de la solución (¡pero necesita completarse!):

```javascript
if (matching_rule === 'shape') {
    if (shape1 === response_shape) correct_response = 'a'
    // Aún no terminado
} // Aún no terminado

// Imprimamos información en la ventana de depuración
console.log('matching_rule = ' + matching_rule)
console.log('correct_response = ' + correct_response)
```

### Extra 5 (difícil): Cambiar periódicamente la regla de coincidencia

Hasta ahora, la regla de coincidencia se determina aleatoriamente al inicio del experimento, pero luego permanece constante durante todo el experimento. En un WCST real, la regla de coincidencia cambia periódicamente, generalmente después de que el participante haya realizado un número fijo de respuestas correctas.

Para implementar esto, necesitas otro INLINE_JAVASCRIPT. Aquí hay algunas sugerencias para comenzar:

- Utiliza una variable de contador que se incremente en 1 después de una respuesta correcta y se restablezca a 0 después de una respuesta incorrecta.
- Al cambiar la regla de coincidencia, asegúrate de que no se establezca (por coincidencia) en la misma regla de coincidencia nuevamente.


### Extra 6 (realmente difícil): Restringir la tarjeta de respuesta

Ahora mismo, la tarjeta de respuesta puede superponerse con una tarjeta de estímulo en múltiples dimensiones. Por ejemplo, si una de las tarjetas de estímulo es un círculo azul único, la tarjeta de respuesta podría ser dos círculos azules, superponiéndose tanto en color como en forma. En un WCST real, la tarjeta de respuesta debería superponerse con cada tarjeta de estímulo en no más de una dimensión.

Esta vez te toca a ti. ¡No hay pistas!


### Extra 7 (fácil): Ejecutar el experimento en línea con JATOS

Nuestro WCST es compatible con OSWeb, lo que significa que puedes ejecutarlo en un navegador. Para probar si esto todavía funciona, puedes seleccionar el backend de OSWeb en la pestaña de propiedades generales del ítem del experimento. Una vez seleccionado, simplemente puedes hacer clic en el botón verde y el experimento comenzará en tu navegador predeterminado.

Sin embargo, para recopilar datos reales de uno de tus estudios, querrás importar el experimento a JATOS y utilizar JATOS para generar un enlace que puedas distribuir a tus participantes. ¡Esto es mucho más fácil de lo que parece! Para obtener más información, consulta:

- %link:manual/osweb/workflow%

## Soluciones

Puedes descargar el experimento completo, incluyendo las soluciones a las tareas adicionales, aquí:

- <https://osf.io/f5er2/>