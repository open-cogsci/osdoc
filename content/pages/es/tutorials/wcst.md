title: Test de Clasificación de Tarjetas de Wisconsin
uptodate: false
hash: de605121ce6b894d920b49eb8caa88e9c60f258f6f573d69ce0a995939cbaf10
locale: es
language: Spanish

[TOC]

## Los pasos básicos

%--
figura:
 id: FigWCST
 fuente: wcst.png
 leyenda: |
  El Test de Clasificación de Cartas de Wisconsin (WCST) es una prueba neuropsicológica de funciones ejecutivas.
--%

En este tutorial, implementará el Test de Clasificación de Cartas de Wisconsin (WCST) y aprenderá cómo puede ejecutar esta prueba en línea con OSWeb.

En el WCST, los participantes ven cuatro cartas de estímulo, que difieren en tres dimensiones: color (rojo, verde, azul, amarillo), forma (círculo, estrella, triángulo, cruz) y cantidad de formas (uno, dos, tres o cuatro). Los participantes también ven una sola carta de respuesta, que también tiene un color, una forma y un número.

La tarea del participante es hacer coincidir la carta de respuesta con la carta de estímulo correcta, según una dimensión específica (por ejemplo, color), o *regla de coincidencia*. El participante inicialmente no sabe en qué dimensión hacer coincidir, y su tarea es descubrir la regla de coincidencia mediante ensayo y error.

Para hacer las cosas más difíciles, la regla de coincidencia cambia después de cada cinco respuestas correctas. Por lo tanto, el participante debe actualizar de manera flexible su regla de coincidencia.

### Paso 1: Descarga e inicia OpenSesame

OpenSesame está disponible para Windows, Linux y Mac OS. Este tutorial está escrito para OpenSesame 3.2 o superior.

Cuando inicie OpenSesame, se le dará una opción de experimentos de plantilla y (si corresponde) una lista de experimentos abiertos recientemente (ver% FigStartUp).

%--
figura:
 id: FigStartUp
 fuente: start-up.png
 leyenda: |
  La ventana de OpenSesame al inicio.
--%

La *plantilla extendida* proporciona un buen punto de partida para crear muchos experimentos que usan una estructura de bloques de prueba. Sin embargo, en este tutorial crearemos todo el experimento desde cero y utilizaremos la 'plantilla predeterminada', que ya está cargada cuando se lanza OpenSesame (% FigDefaultTemplate). Por lo tanto, simplemente cierre las pestañas '¡Comenzar!' e '¡Bienvenido!', si se muestran.

%--
figura:
 id: FigDefaultTemplate
 fuente: default-template.png
 leyenda: |
  La estructura de la "Plantilla predeterminada" como se ve en el área de descripción general.
--%

### Paso 2: Agrega un block_loop y trial_sequence

La plantilla predeterminada comienza con tres elementos: un NOTEPAD llamado *getting_started*, un SKETCHPAD llamado *welcome* y una SEQUENCE llamada *experiment*. No necesitamos *getting_started* y *welcome*, así que quitémoslos de inmediato. Para hacerlo, haga clic derecho en estos elementos y seleccione 'Eliminar'. No elimine *experiment*, porque es la entrada para el experimento (es decir, el primer elemento que se llama al iniciarse el experimento).

Nuestro experimento tendrá una estructura muy simple. En la parte superior de la jerarquía hay un LOOP, al que llamaremos *block_loop*. El *block_loop* es el lugar donde definiremos nuestras variables independientes. Para agregar un LOOP a tu experimento, arrastra el icono de LOOP desde la barra de herramientas de elementos hasta el elemento *experiment* en el área de descripción general.

Un elemento LOOP necesita otro elemento para ejecutarse; por lo general, y en este caso también, este es una SEQUENCE. Arrastra el elemento SEQUENCE desde la barra de herramientas de elementos hasta el elemento *new_loop* en el área de descripción general. OpenSesame preguntará si deseas insertar la SEQUENCE en el LOOP o después de él. Selecciona 'Insertar en new_loop'.

Por defecto, los elementos tienen nombres como *new_sequence*, *new_loop*, *new_sequence_2*, etc. Estos nombres no son muy informativos y es una buena práctica cambiarlos. Los nombres de los elementos deben constar de caracteres alfanuméricos y/o guiones bajos. Para cambiar el nombre de un elemento, haga doble clic en el elemento en el área de descripción general. Cambie el nombre de *new_sequence* a *trial_sequence* para indicar que corresponderá a una sola prueba. Cambie el nombre de *new_loop* a *block_loop* para indicar que corresponderá a un bloque de pruebas.

Finalmente, haga clic en 'Nuevo experimento' para abrir la pestaña de Propiedades Generales. Haga clic en el título del experimento y cámbiolo a 'Test de Clasificación de Cartas de Wisconsin'.

El área de descripción general de nuestro experimento ahora se ve como en % FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  The overview area at the end of Step 2.
--%


### Paso 3: Importar imágenes y archivos de sonido

Para este experimento, utilizaremos imágenes para las cartas. Puedes descargarlas desde aquí:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Descarga `stimuli.zip` y extráelo en algún lugar (en tu escritorio, por ejemplo). A continuación, en OpenSesame, haz clic en el botón "Mostrar archivo de recursos" en la barra de herramientas principal (o: Menú → Ver → Mostrar archivo de recursos). Esto mostrará el archivo de recursos, por defecto en el lado derecho de la ventana. La forma más fácil de agregar los estímulos al archivo de recursos es arrastrándolos desde el escritorio (o desde donde los hayas extraído) al archivo de recursos. Alternativamente, puedes hacer clic en el botón "+" en el archivo de recursos y agregar archivos utilizando el cuadro de diálogo de selección de archivos que aparece. El archivo de recursos se guardará automáticamente con tu experimento.

Después de haber agregado todos los estímulos, tu archivo de recursos se verá como en %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  The file pool containing the stimuli.
--%


### Paso 4: Crear una pantalla de cartas estática

Para comenzar, crearemos una pantalla con cuatro cartas de estímulo y una carta de respuesta. Sin embargo, qué cartas se muestran no dependerá, por ahora, de las variables; es decir, crearemos una pantalla *estática*.

Arrastra un SKETCHPAD a *trial_sequence* y cámbialo el nombre por *card_display*. Utiliza la herramienta de imagen para dibujar cuatro cartas en una fila horizontal cerca de la parte superior de la pantalla; estas serán las cartas de estímulo. Dibuja una sola carta cerca de la parte inferior de la pantalla; esta será la carta de respuesta. También agrega texto para indicar al participante qué tiene que hacer, es decir, presionar `a`, `b`, `c` o `d` para indicar cuál de las cartas de estímulo coincide con la carta de respuesta. ¡El texto exacto, el diseño y las cartas dependen de ti! Consejos: puedes usar la opción *scale* para ajustar el tamaño de las cartas y puedes cambiar el color de fondo en la pestaña General Properties, que puedes abrir haciendo clic en el elemento de nivel superior del experimento.

Para mí, el resultado se ve así:

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  A SKETCHPAD with statically defined cards.
--%


### Paso 5: Haz que la carta de respuesta sea variable

Ahora mismo siempre mostramos la misma carta de respuesta (en el ejemplo de arriba, un triángulo azul único). Pero, por supuesto, queremos mostrar una carta de respuesta diferente en cada ensayo. Para hacerlo, primero necesitamos definir las variables que determinan qué carta de respuesta mostraremos. Lo haremos en el *block_loop*.

Abre el *block_loop*. La tabla LOOP está vacía. Para determinar el color, la forma y el número de la carta de respuesta, podríamos crear manualmente tres columnas (`response_color`, `response_shape` y `response_number`) y 64 filas para todas las combinaciones posibles de colores, formas y números. Pero eso sería mucho trabajo. En su lugar, utilizaremos el asistente de diseño factorial completo, que puedes abrir haciendo clic en el botón "Diseño factorial completo". (Un diseño factorial completo es un diseño en el que ocurren todas las posibles combinaciones de niveles de variables). En este asistente, crea una columna para cada una de las tres variables e ingresa los posibles valores para esa variable en las celdas de abajo (ver %FigDesignWizard).

%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  The full-factorial-design wizard allows you to easily generate large LOOP tables that correspond to full-factorial designs.
--%

A continuación, haz clic en el botón Aceptar. El *block_loop* ahora contiene las 64 combinaciones de colores, números y formas (ver %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  The *block_loop* at the end of step 5.
--%

Ahora regresa al *card_display*. Cada elemento en OpenSesame está definido a través de un script. Este script se genera automáticamente mediante la interfaz de usuario. A veces puede ser conveniente (o incluso necesario) editar este script directamente. La razón más común para editar el script de un elemento es agregar variables al script, que es también lo que haremos ahora.

Para ver el script, haz clic en el botón 'View' y selecciona 'View script'. (El botón de vista es el botón central en la parte superior derecha de los controles del elemento). Esto abrirá un editor de script.

El script de *card_display* consiste principalmente en comandos `draw`, que definen cada una de las cinco tarjetas, así como los diversos elementos de texto. Localiza la línea que corresponde a la tarjeta de respuesta. Puedes encontrarlo mirando la coordenada Y, que debe ser positiva (es decir, en la parte inferior de la pantalla) o mirando el nombre del archivo de imagen.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Ahora mismo, en mi ejemplo, el archivo de imagen para la tarjeta de respuesta siempre es `"1-blue-triangle.png"`. Pero, por supuesto, no siempre queremos mostrar un único triángulo azul. En cambio, queremos que el archivo de imagen dependa de las variables que hemos definido en el *block_loop*. Para hacerlo, reemplaza el número por `[response_number]`, el color por `[response_color]` y la forma por `[response_shape]`: (Los corchetes indican que se refieren a nombres de variables.)

```
draw image center=1 file="[response_number]-[response_color]-[response_shape].png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Haz clic en Apply para aceptar los cambios en el script. La tarjeta de respuesta ahora ha sido reemplazada por un ícono de interrogación. Esto se debe a que OpenSesame no sabe cómo mostrar una vista previa de una imagen que se ha definido mediante variables. Pero no te preocupes: ¡la imagen se mostrará cuando ejecutes el experimento!

### Paso 6: Hacer las tarjetas de estímulo variables

Las tarjetas de estímulo deben seleccionarse más o menos al azar, pero cada color, forma y número solo debe ocurrir una vez; es decir, nunca debe haber dos tarjetas rojas o dos tarjetas con triángulos (si lo hubiera, el procedimiento de coincidencia se volvería ambiguo). Para lograr esto, podemos usar *horizontal shuffling*, que es una función poderosa pero inusual del elemento LOOP.

- %link:loop%

Primero, abre el *block_loop* y crea 12 (!) Nuevas columnas para definir las tarjetas de estímulo: `color1`, para el color de la primera tarjeta, `color2`, `color3`, `color4`, y `shape1` ... `shape4`, y `number1` ... `number4`. Cada columna tiene el mismo valor en cada fila (ver %FigLoopTable2),

%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  El *block_loop* durante el paso 6.
--%

¡Pero aún no hemos terminado! Ahora mismo, la primera tarjeta de estímulo siempre es un círculo rojo único, la segunda dos triángulos azules, etc. Para randomizar esto, le decimos a OpenSesame que intercambie al azar (baraje horizontalmente) los valores de las cuatro variables de color, las cuatro variables de forma y las cuatro variables de número. Para hacerlo, abre el script del *block_loop*. En la penúltima línea (justo antes de `run trial_sequence`) agrega los siguientes comandos:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Haz clic en Apply para aceptar el script. Para ver si esto ha funcionado, haz clic en el botón de vista previa. Esto mostrará una vista previa de cómo se aleatorizará la tabla LOOP durante el experimento. ¿Se ve bien?

Ahora regresa al *card_display* y haz que la imagen de la primera tarjeta de estímulo dependa de las variables `color1`,`shape1` y `number1`, y análogamente para las otras tarjetas de estímulo. (Si no estás seguro de cómo hacer esto, revisa el paso 5.)

### Paso 7: Determinar la respuesta correcta (para una regla de coincidencia)

Por ahora, vamos a suponer que los participantes siempre coinciden en forma. (Uno de los Extra Assignments es mejorar esto.)

Ahora mismo, la duración de *card_display* está configurada como 'keypress'. Esto significa que el *card_display* se muestra hasta que se presiona una tecla, pero no proporciona control sobre cómo se maneja esta pulsación de tecla. Por lo tanto, cambia la duración a 0 e inserta una KEYBOARD_RESPONSE directamente después de la *card_display*. Cambia el nombre de KEYBOARD_RESPONSE a *press_a* y especifica que la respuesta correcta es 'a' y que las respuestas permitidas son 'a;b;c;d'.

%--
figure:
 id: FigPressA
 source: press-a.png
 caption: |
  Uno de los elementos KEYBOARD_RESPONSE definidos en el paso 7.
--%

¡Pero esto no es suficiente! En este momento hay un solo elemento de respuesta que asume que la respuesta correcta siempre es 'a'. No hemos especificado *cuándo* la respuesta correcta es 'a', ni hemos considerado ensayos en los que la respuesta correcta es 'b', 'c' o 'd'.

Para lograr esto, primero crea tres elementos KEYBOARD_RESPONSE más: *press_b*, *press_c* y *press_d*. Todos son iguales, excepto por la respuesta correcta, que se define para cada uno de ellos por separado y debe ser respectivamente 'b', 'c' y 'd'.

Finalmente, en el *trial_sequence*, usa las declaraciones Run If para decidir bajo qué condición cada uno de los cuatro elementos KEYBOARD_RESPONSE debe ejecutarse (decidiendo así cuál es la respuesta correcta). Para *press_a*, la condición es que `shape1` debe ser igual a `response_shape`. ¿Por qué? Bueno, porque eso significa que la forma de la primera tarjeta de estímulo es igual a la forma de la tarjeta de respuesta y, en ese caso, la respuesta correcta es 'a'. Esta condición corresponde a la siguiente declaración run-if: `[shape1] = [response_shape]`. Las declaraciones run-if para los otros elementos KEYBOARD_RESPONSE son análogas (ver %FigTrialSequence1).

%--
figure:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 caption: |
  El *trial_sequence* al final del paso 7.
--%

### Paso 8: Proporcionar retroalimentación al participante

OpenSesame registra automáticamente si una respuesta fue correcta o no, estableciendo la variable `correct` en 1 o 0, respectivamente. (Siempre que hayas especificado la respuesta correcta, como lo hicimos en el paso 7). Podemos utilizar esto para dar retroalimentación al participante sobre si respondieron correctamente o no.

Para hacer esto, añade dos SKETCHPADs nuevos al *trial_sequence* y llámalos *correct_feedback* e *incorrect_feedback*. Luego, especifica cuál de los dos se debe ejecutar utilizando una declaración run-if (ver %FigTrialSequence2).

%--
figure:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 caption: |
  El *trial_sequence* al final del paso 8.
--%

Finalmente, añade contenido útil a ambos SKETCHPADs. Por ejemplo, para *correct_feedback* podrías usar un punto de fijación verde y para *incorrect_feedback* podrías usar un punto de fijación rojo, en ambos casos mostrados durante 500 ms (es decir, configurando la duración del SKETCHPAD a 500). Los puntos de color son una forma agradable y discreta de proporcionar retroalimentación.

### Paso 9: Prueba el experimento

Ahora has creado una implementación básica (¡pero incompleta!) del Wisconsin Card Sorting Test. (Completarás la implementación como parte de las Tareas Extra a continuación.)

%--
figure:
 id: FigRunButtons
 source: run-buttons.png
 caption: |
  La barra de herramientas principal contiene botones para (de izquierda a derecha): ejecutar en pantalla completa, ejecutar en una ventana, ejecución rápida (ejecutar en una ventana sin solicitar archivo de registro o número de participante), abortar el experimento y ejecutar en un navegador.
--%

Para probar el experimento, haz clic en el botón de ejecución rápida (las flechas azules dobles) para probar el experimento en el escritorio (ver %FigRunButtons). Si el experimento se ejecuta según lo esperado en el escritorio, haz clic en el botón para ejecutar en el navegador (la flecha dentro de un círculo verde) para probar el experimento en un navegador.

## Tareas extra

### Extra 1 (fácil): Agrega un logger

OpenSesame no registra automáticamente los datos. En cambio, necesita agregar explícitamente un elemento `logger` a su experimento. En un experimento basado en pruebas, un `logger` generalmente es el último elemento de la *secuencia de prueba*, de modo que registra todos los datos que se recopilaron durante la prueba.

Ahora mismo, nuestro WCST no registra ningún dato. ¡Hora de arreglar eso!

### Extra 2 (fácil): Inspeccione el archivo de datos

*Requiere que haya completado el Extra 1*.

Realice una prueba corta del experimento. Ahora inspeccione el archivo de registro en un programa como Excel, LibreOffice Calc o JASP. Identifique las variables relevantes y piense en cómo podría analizar los resultados.

__Pro-tip:__ Establezca el valor de repetición de *block_loop* en 0.1 para reducir el número de pruebas durante las pruebas.

### Extra 3 (fácil): Agregar instrucciones y pantalla de despedida

Un buen experimento viene con instrucciones claras. Y un experimento educado se despide de los participantes cuando terminan. Puede usar SKETCHPAD para hacer esto.

__Pro-tip:__ Un FORM_TEXT_DISPLAY no es compatible con OSWeb, por lo que no debe usarlo para obtener instrucciones si desea ejecutar su experimento en línea.

### Extra 4 (intermedio): Establecer la respuesta correcta y la regla de coincidencia a través de JavaScript

Para incluir secuencias de comandos en OSWeb, puede usar el elemento INLINE_JAVASCRIPT, que admite JavaScript. (¡Pero actualmente no proporciona toda la funcionalidad que ofrece la INLINE_SCRIPT regular de Python!)

Hasta ahora, la regla de coincidencia siempre coincide con la forma. Para cambiar esto, agregue un elemento INLINE_JAVASCRIPT al comienzo del experimento y use el siguiente script (en la fase *prepare*) para establecer aleatoriamente la variable `matching_rule` en 'shape', 'number' o 'color'.

```javascript
function choice(choices) {
    // JavaScript no tiene una función de elección incorporada, por lo que la definimos
    // aquí.
    let index = Math.floor(Math.random() * choices.length)
    return choices[index]
}


// El objeto vars contiene todas las variables experimentales, como el objeto var
// en Python inline script
vars.matching_rule = choice(['shape', 'number', 'color'])
```

Agregue otro elemento INLINE_JAVASCRIPT al comienzo de la *secuencia de prueba*. En la fase *prepare*, agregue un script para establecer la variable `correct_response` en 'a', 'b', 'c' o 'd'. Para hacerlo, necesita una serie de declaraciones `if`, que primero miren la regla de coincidencia y luego miren qué forma corresponde a la forma de respuesta (para la regla de coincidencia de forma) o qué color corresponde al color de respuesta (para la regla de coincidencia de color) etc.

Para comenzar, aquí hay parte de la solución (¡pero debe completarse!):

```javascript
if (vars.matching_rule === 'shape') {
    if (vars.shape1 === vars.response_shape) vars.correct_response = 'a'
    // No terminado todavía
} // No terminado todavía

// Imprimamos algo de información en la ventana de depuración
console.log('matching_rule = ' + vars.matching_rule)
console.log('correct_response = ' + vars.correct_response)
```

### Extra 5 (difícil): Cambie periódicamente la regla de coincidencia

Hasta ahora, la regla de coincidencia se determina aleatoriamente al comienzo del experimento, pero luego permanece constante durante todo el experimento. En un WCST real, la regla de coincidencia cambia periódicamente, generalmente después de que el participante ha realizado un número fijo de respuestas correctas.

Para implementar esto, necesitará otro INLINE_JAVASCRIPT. Aquí hay algunos consejos para comenzar:

- Utilice una variable contador que se incremente en 1 después de una respuesta correcta y se restablezca a 0 después de una respuesta incorrecta.
- Al cambiar la regla de coincidencia, asegúrese de que no se establezca (por coincidencia) en la misma regla de coincidencia nuevamente.

### Extra 6 (realmente difícil): Restringir la tarjeta de respuesta

En este momento, la tarjeta de respuesta puede superponerse con una tarjeta de estímulo en varias dimensiones. Por ejemplo, si una de las tarjetas de estímulo es un círculo azul único, la tarjeta de respuesta podría ser dos círculos azules, superponiéndose tanto en color como en forma. En un WCST real, la tarjeta de respuesta debe superponerse con cada tarjeta de estímulo en no más de una dimensión.

Esto queda a tu criterio. ¡Sin sugerencias esta vez!

### Extra 7 (fácil): Ejecutar el experimento en línea con JATOS

Nuestro WCST es compatible con OSWeb, lo que significa que puedes ejecutarlo en un navegador. Para probar si esto aún funciona, puedes hacer clic en el botón ejecutar-en-navegador en OpenSesame.

Sin embargo, para recopilar datos reales con el experimento en un navegador, necesitas importar el experimento a JATOS y utilizar JATOS para generar un enlace que puedes distribuir a tus participantes. ¡Esto es mucho más fácil de lo que parece! Para obtener más información, consulta:

- %link:manual/osweb/workflow%

## Soluciones

Puedes descargar el experimento completo, incluidas las soluciones a las tareas adicionales, aquí:

- <https://osf.io/f5er2/>