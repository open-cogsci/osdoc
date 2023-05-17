title: Test de Clasificación de Tarjetas de Wisconsin
hash: 4199e2aea0b73c7c2aec2a427017e0f2de9ffa30a72377e12ed75900a1fbc9a1
locale: es
language: Spanish

[TOC]


## Los pasos básicos


%--
figure:
 id: FigWCST
 source: wcst.png
 caption: |
  El Wisconsin Card Sorting Test (WCST) es una prueba neuropsicológica de las funciones ejecutivas.
--%


En este tutorial, implementarás el Wisconsin Card Sorting Test (WCST). También aprenderás cómo incorporar código Python en el experimento. (Para la implementación de esta tarea en OSWeb, consulta [este tutorial](%url:wcst%)).

En el WCST, los participantes ven cuatro tarjetas de estímulo, que difieren en tres dimensiones: color (rojo, verde, azul, amarillo), forma (círculo, estrella, triángulo, cruz) y número de formas (uno, dos, tres o cuatro). Los participantes también ven una única tarjeta de respuesta, que también tiene un color, una forma y un número.

La tarea del participante es hacer coincidir la tarjeta de respuesta con la tarjeta de estímulo correcta, basándose en una dimensión específica (por ejemplo, color) o *regla de coincidencia*. El participante inicialmente no sabe en qué dimensión hacer coincidir y su tarea es descubrir la regla de coincidencia a través del ensayo y error.

Para dificultar las cosas, la regla de coincidencia cambia después de cada cinco respuestas correctas. Por lo tanto, el participante necesita actualizar de manera flexible su regla de coincidencia.


### Paso 1: Descarga e inicia OpenSesame

OpenSesame está disponible para Windows, Linux y Mac OS. Este tutorial está escrito para OpenSesame 4.0 o superior.

Cuando inicies OpenSesame, se te dará a elegir entre experimentos de plantilla y, si los hay, una lista de experimentos abiertos recientemente (ver % FigStartUp).

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La ventana de OpenSesame al inicio.
--%

La *Plantilla extendida* ofrece un buen punto de partida para crear muchos experimentos que utilizan una estructura de bloque-ensayo. Sin embargo, en este tutorial crearemos todo el experimento desde cero y utilizaremos la "plantilla predeterminada", que ya está cargada cuando se inicia OpenSesame (% FigDefaultTemplate). Por lo tanto, simplemente cierra las pestañas "¡Para empezar!" y "¡Bienvenido!" (si se muestran).

%--
figure:
 id: FigDefaultTemplate
 source: default-template.png
 caption: |
  La estructura de la "Plantilla predeterminada" como se ve en el área de descripción general.
--%


### Paso 2: Agrega un block_loop y trial_sequence

La plantilla predeterminada comienza con tres elementos: un NOTEPAD llamado *getting_started*, un SKETCHPAD llamado *welcome* y un SEQUENCE llamado *experiment*. No necesitamos *getting_started* y *welcome*, así que eliminémoslos de inmediato. Para hacerlo, haz clic derecho en estos elementos y selecciona "Eliminar". No elimines *experiment*, porque es la entrada del experimento (es decir, el primer elemento que se llama al iniciar el experimento).

Nuestro experimento tendrá una estructura muy sencilla. En la parte superior de la jerarquía se encuentra un LOOP, al que llamaremos *block_loop*. En *block_loop* es donde definiremos nuestras variables independientes. Para agregar un LOOP a tu experimento, arrastra el ícono de LOOP desde la barra de herramientas de elementos al elemento *experiment* en el área de descripción general.

Se necesita otro elemento para ejecutar un elemento LOOP; por lo general, y también en este caso, es una SEQUENCE. Arrastra el elemento SEQUENCE desde la barra de herramientas de elementos al elemento *new_loop* en el área de descripción general. OpenSesame preguntará si deseas insertar la SEQUENCE en o después del LOOP. Selecciona "Insertar en new_loop".

Por defecto, los elementos tienen nombres como *new_sequence*, *new_loop*, *new_sequence_2*, etc. Estos nombres no son muy informativos y es una buena práctica cambiarlos. Los nombres de los elementos deben estar compuestos por caracteres alfabéticos y/o guiones bajos. Para cambiar el nombre de un elemento, haz doble clic en el elemento en el área de descripción general. Cambia el nombre de *new_sequence* a *trial_sequence* para indicar que corresponderá a un solo ensayo. Cambia el nombre de *new_loop* a *block_loop* para indicar que corresponderá a un bloque de ensayos.

Finalmente, haz clic en "Nuevo experimento" para abrir la pestaña de Propiedades Generales. Haz clic en el título del experimento y renómbralo a "Wisconsin Card Sorting Test".

El área de descripción general de nuestro experimento ahora se ve como en %FigBasicStructure.

%--
figure:
 id: FigBasicStructure
 source: basic-structure.png
 caption: |
  El área de descripción general al final del paso 2.
--%


### Paso 3: Importar imágenes y archivos de sonido

Para este experimento, utilizaremos imágenes para las cartas. Puedes descargarlas desde aquí:

- %static:attachments/wisconsin-card-sorting-test/stimuli.zip%

Descarga `stimuli.zip` y extráelo en algún lugar (en tu escritorio, por ejemplo). A continuación, en OpenSesame, haz clic en el botón 'Mostrar grupo de archivos' en la barra de herramientas principal (o: Menú → Vista → Mostrar grupo de archivos). Esto mostrará el grupo de archivos, por defecto en el lado derecho de la ventana. La forma más fácil de agregar los estímulos al grupo de archivos es arrastrándolos desde el escritorio (o donde los hayas extraído) al grupo de archivos. Alternativamente, puedes hacer clic en el botón '+' en el grupo de archivos y agregar archivos usando el cuadro de selección de archivos que aparecerá. El grupo de archivos se guardará automáticamente con tu experimento.

Después de agregar todos los estímulos, tu grupo de archivos se verá como en %FigFilePool.

%--
figure:
 id: FigFilePool
 source: file-pool.png
 caption: |
  El grupo de archivos que contiene los estímulos.
--%


### Paso 4: Crear una pantalla de cartas estática

Para empezar, crearemos una pantalla con cuatro cartas de estímulo y una carta de respuesta. Sin embargo, por ahora, las cartas mostradas no dependerán de variables; es decir, crearemos una pantalla *estática*.

Arrastra un SKETCHPAD a *trial_sequence* y cámbiale el nombre a *card_display*. Utiliza la herramienta de imágenes para dibujar cuatro cartas en una fila horizontal cerca de la parte superior de la pantalla; estas serán las cartas de estímulo. Dibuja una sola carta cerca de la parte inferior de la pantalla; esta será la carta de respuesta. También agrega algo de texto para indicar al participante qué tiene que hacer, es decir, presionar `a`, `b`, `c` o `d` para indicar cuál de las cartas de estímulo coincide con la carta de respuesta. ¡El texto exacto, el diseño y las cartas dependen de ti! Consejos: puedes utilizar la opción *escala* para ajustar el tamaño de las cartas; puedes cambiar el color de fondo en la pestaña Propiedades Generales, que puedes abrir haciendo clic en el elemento de nivel superior del experimento.

Para mí, el resultado se ve así:

%--
figure:
 id: FigStaticCards
 source: static-cards.png
 caption: |
  Un SKETCHPAD con cartas definidas estáticamente.
--%


### Paso 5: Hacer variable la carta de respuesta

Ahora siempre estamos mostrando la misma carta de respuesta (en el ejemplo anterior, un único triángulo azul) Pero, por supuesto, queremos mostrar una carta de respuesta diferente en cada ensayo. Para hacerlo, primero necesitamos definir las variables que determinan qué carta de respuesta mostraremos. Haremos esto en el *block_loop*.

Abre el *block_loop*. La tabla LOOP está vacía. Para determinar el color, la forma y el número de la carta de respuesta, podríamos crear manualmente tres columnas (`response_color`, `response_shape` y `response_number`) y 64 filas para todas las combinaciones posibles de colores, formas y números. Pero eso sería mucho trabajo. En su lugar, utilizaremos el asistente de diseño factorial completo, que puedes abrir haciendo clic en el botón 'Diseño factorial completo'. (Un diseño factorial completo es un diseño en el que ocurren todas las combinaciones posibles de niveles de variables.) En este asistente, creas una columna para cada una de las tres variables, y en las celdas inferiores ingresas los posibles valores para esa variable (ver %FigDesignWizard).


%--
figure:
 id: FigDesignWizard
 source: design-wizard.png
 caption: |
  El asistente de diseño factorial completo te permite generar fácilmente grandes tablas LOOP que corresponden a diseños factoriales completos.
--%


Luego, haz clic en el botón Aceptar. El *block_loop* ahora contiene todas las 64 combinaciones de colores, números y formas (ver %FigLoopTable1).

%--
figure:
 id: FigLoopTable1
 source: loop-table-1.png
 caption: |
  El *block_loop* al final del paso 5.
--%

Ahora regresa al *card_display*. Cada elemento en OpenSesame está definido a través de un script. Este script se genera automáticamente mediante la interfaz de usuario. A veces puede ser conveniente (o incluso necesario) editar este script directamente. La razón más común para editar el script de un elemento es agregar variables al script, ¡que es precisamente lo que haremos ahora!

Para ver el script, haz clic en el botón "Ver" y selecciona "Ver script". (El botón de vista es el botón central en la parte superior derecha de los controles del elemento). Esto abrirá un editor de scripts.

El script para *card_display* consiste principalmente en comandos `draw`, que definen cada una de las cinco cartas, y también los diversos elementos de texto. Localiza la línea que corresponde a la carta de respuesta. Puedes encontrarlo mirando la coordenada Y, que debe ser positiva (es decir, en la parte inferior de la pantalla), o buscando el nombre del archivo de imagen.

```
draw image center=1 file="1-blue-triangle.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Ahora mismo, en mi ejemplo, el archivo de imagen para la carta de respuesta siempre es `"1-blue-triangle.png"`. Pero, por supuesto, no siempre queremos mostrar un solo triángulo azul. En su lugar, queremos que el archivo de imagen dependa de las variables que hemos definido en el *block_loop*. Para hacerlo, reemplace el número por `{response_number}`, el color por `{response_color}` y la forma por `{response_shape}`: (Los corchetes indican que se trata de nombres de variables.)


```
draw image center=1 file="{response_number}-{response_color}-{response_shape}.png" scale=0.5 show_if=always x=0 y=192 z_index=0
```

Haz clic en Aplicar para aceptar los cambios en el script. La carta de respuesta ahora ha sido reemplazada por un ícono de interrogación. Esto se debe a que OpenSesame no sabe cómo mostrar una vista previa de una imagen que se ha definido utilizando variables. Pero no te preocupes: ¡la imagen se mostrará cuando ejecutes el experimento!


### Paso 6: Hacer que las cartas de estímulo sean variables

Las cartas de estímulo deben seleccionarse más o menos al azar, pero cada color, forma y número debería aparecer solo una vez; es decir, nunca debe haber dos cartas rojas o dos cartas con triángulos. (Si lo hubiera, el procedimiento de coincidencia se volvería ambiguo). Para lograr esto, podemos utilizar *horizontal shuffling*, una función poderosa pero inusual del elemento LOOP.

- %link:loop%

Primero, abre el *block_loop* y crea 12 (!) columnas nuevas para definir las cartas de estímulo: `color1`, para el color de la primera carta, `color2`, `color3`, `color4`, y `shape1` ... `shape4`, y `number1` ... `number4`. Cada columna tiene el mismo valor en cada fila (ver %FigLoopTable2).


%--
figure:
 id: FigLoopTable2
 source: loop-table-2.png
 caption: |
  El *block_loop* durante el paso 6.
--%


¡Pero aún no hemos terminado! Ahora mismo, la primera carta de estímulo siempre es un círculo rojo, la segunda son dos triángulos azules, etc. Para hacer esto al azar, le decimos a OpenSesame que intercambie aleatoriamente (barajar horizontalmente) los valores de las cuatro variables de color, las cuatro variables de forma y las cuatro variables de número. Para hacerlo, abre el script para el *block_loop*. En la penúltima línea (justo antes de `run trial_sequence`) agregue los siguientes comandos:

```
shuffle_horiz color1 color2 color3 color4
shuffle_horiz shape1 shape2 shape3 shape4
shuffle_horiz number1 number2 number3 number4
```

Haz clic en Aplicar para aceptar el script. Para ver si esto ha funcionado, haz clic en el botón Previsualizar. Esto mostrará una vista previa de cómo se randomizará la tabla LOOP durante el experimento. ¿Se ve bien?

Ahora regresa al *card_display* y haz que la imagen de la primera carta de estímulo dependa de la variable `color1`, `shape1` y `number1`, y análogamente para las otras cartas de estímulo. (Si no estás seguro de cómo hacer esto, vuelve al paso 5).


### Paso 7: Determinar la respuesta correcta (para una regla de coincidencia)


Por ahora, vamos a suponer que los participantes siempre coinciden en la forma. (Una de las Tareas adicionales es mejorar esto).

Actualmente, la duración de *card_display* está configurada como 'keypress'. Esto significa que el *card_display* se muestra hasta que se presiona una tecla, pero no ofrece control sobre cómo se maneja esta pulsación de tecla. Por lo tanto, cambia la duración a 0 e inserta un KEYBOARD_RESPONSE directamente después del *card_display*. Cambia el nombre del KEYBOARD_RESPONSE a *press_a* y especifica que la respuesta correcta es 'a' y que las respuestas permitidas son 'a;b;c;d'.

%--
figure:
 id: FigPressA
 source: press-a.png
 caption: |
  Uno de los elementos KEYBOARD_RESPONSE definidos en el paso 7.
--%

¡Pero esto no es suficiente! Ahora mismo hay un solo elemento de respuesta que asume que la respuesta correcta siempre es 'a'. No hemos especificado *cuándo* la respuesta correcta es 'a', ni hemos considerado ensayos en los que la respuesta correcta es 'b', 'c' o 'd'.

Para lograr esto, primero crea tres elementos KEYBOARD_RESPONSE adicionales: *press_b*, *press_c* y *press_d*. Todos ellos son iguales, excepto por la respuesta correcta, que se define para cada uno de ellos por separado y debe ser respectivamente 'b', 'c' y 'd'.

Finalmente, en la *trial_sequence*, usa las declaraciones Run If para decidir bajo qué condición cada uno de los cuatro elementos KEYBOARD_RESPONSE debería ser ejecutado (decidiendo así cuál es la respuesta correcta). Para *press_a*, la condición es que `shape1` debe ser igual a `response_shape`. ¿Por qué? Bueno, porque eso significa que la forma de la primera tarjeta del estímulo es igual a la forma de la tarjeta de respuesta, y en ese caso la respuesta correcta es 'a'. Esta condición corresponde a la siguiente declaración run-if: `shape1 = response_shape`. Las declaraciones run-if para los otros elementos KEYBOARD_RESPONSE son análogas (ver %FigTrialSequence1).

%--
figure:
 id: FigTrialSequence1
 source: trial-sequence-1.png
 caption: |
  La *trial_sequence* al final del paso 7.
--%

### Paso 8: Dar retroalimentación al participante

OpenSesame registra automáticamente si una respuesta fue correcta o no, estableciendo la variable `correct` en 1 o 0 respectivamente. (Siempre y cuando, por supuesto, hayas especificado la respuesta correcta, como lo hicimos en el paso 7). Podemos usar esto para dar retroalimentación al participante sobre si respondió correctamente o no.

Para hacer esto, agrega dos SKETCHPADs nuevos a *trial_sequence* y llámalos como *correct_feedback* e *incorrect_feedback*. Luego, especifica cuál de los dos debe ser ejecutado usando una declaración run-if (ver %FigTrialSequence2).

%--
figure:
 id: FigTrialSequence2
 source: trial-sequence-2.png
 caption: |
  La *trial_sequence* al final del paso 8.
--%

Finalmente, agrega contenido útil a ambos SKETCHPADs. Por ejemplo, para *correct_feedback* podrías usar un punto de fijación verde y para *incorrect_feedback* podrías usar un punto de fijación rojo, en ambos casos mostrados durante 500 ms (es decir, estableciendo la duración del SKETCHPAD en 500). Los puntos de colores son una forma discreta y agradable de proporcionar retroalimentación.

### Paso 9: Probar el experimento

Ahora has creado una implementación básica (¡pero incompleta!) del Wisconsin Card Sorting Test. (Completarás la implementación como parte de las Tareas Extras a continuación).

Para probar el experimento, haz clic en el botón de ejecución rápida (las flechas azules dobles) o en el botón Ejecutar en pantalla completa (la flecha verde).

## Tareas extras

### Extra 1 (fácil): Agregar un logger

OpenSesame no registra automáticamente los datos. En su lugar, debes agregar explícitamente un elemento `logger` a tu experimento. En un experimento basado en ensayos, un `logger` generalmente es el último elemento de la *trial_sequence*, para que registre todos los datos recopilados durante el ensayo.

Ahora mismo, nuestro WCST no registra ningún dato. ¡Hora de solucionar eso!

### Extra 2 (fácil): Inspeccionar el archivo de datos

*Requiere haber completado el Extra 1*.

Realiza una prueba corta del experimento. Ahora inspecciona el archivo de registro en un programa como Excel, LibreOffice Calc o JASP. Identifica las variables relevantes y piensa en cómo podrías analizar los resultados.

__Pro-tip:__ Establece el valor de repetición del *block_loop* en 0.1 para reducir la cantidad de ensayos durante las pruebas.

### Extra 3 (fácil): Agregar instrucciones y pantalla de despedida

Un buen experimento viene con instrucciones claras. Y un experimento educado se despide de los participantes cuando terminan. Puedes usar un SKETCHPAD para hacer esto.

### Extra 4 (medio): Establecer la respuesta correcta y la regla de coincidencia a través del script Python INLINE_SCRIPT

Para incluir scripts de Python en OpenSesame, puedes usar el elemento INLINE_SCRIPT.

Hasta ahora, la regla de coincidencia siempre es coincidir por forma. Para cambiar esto, agrega un elemento INLINE_SCRIPT al comienzo del experimento y usa el siguiente script (en la fase *prepare*) para establecer aleatoriamente la variable `matching_rule` en 'forma', 'número' o 'color'.

```python
import random

matching_rule = random.choice(['forma', 'número', 'color'])
```

Ahora agrega otro elemento INLINE_SCRIPT al comienzo de *trial_sequence*. En la fase *prepare*, agrega un script para establecer la variable `correct_response` en 'a', 'b', 'c' o 'd'. Para hacerlo, necesitas una serie de declaraciones `if`, que primero miren la regla de coincidencia y luego vean qué forma corresponde a la forma de respuesta (para la regla de coincidencia de forma) o qué color corresponde al color de respuesta (para la regla de coincidencia de color) etc.

Para comenzar, aquí hay una parte de la solución (¡pero debe completarse!):

```python
if matching_rule == 'forma':
    if shape1 == response_shape:
        correct_response = 'a'
    # No terminado todavía
# No terminado todavía

# Imprimamos información en la ventana de depuración
print('matching_rule = {}'.format(matching_rule))
print('correct_response = {}'.format(correct_response))
```

### Extra 5 (difícil): Cambiar periódicamente la regla de coincidencia

Hasta ahora, la regla de coincidencia se determina al azar al comienzo del experimento, pero luego permanece constante durante todo el experimento. En un WCST real, la regla de coincidencia cambia periódicamente, normalmente después de que el participante haya hecho un número fijo de respuestas correctas.

Para implementar esto, necesitas otro INLINE_SCRIPT. Aquí hay algunos consejos para comenzar:

- Usa una variable de contador que se incrementa en 1 después de una respuesta correcta y se reinicia a 0 después de una respuesta incorrecta.
- Al cambiar la regla de coincidencia, asegúrate de que no se establezca (por coincidencia) en la misma regla de coincidencia nuevamente.

### Extra 6 (muy difícil): Restringir la tarjeta de respuesta

Ahora mismo, la tarjeta de respuesta puede superponerse con una tarjeta de estímulo en varias dimensiones. Por ejemplo, si una de las tarjetas de estímulo es un círculo azul único, la tarjeta de respuesta podría ser dos círculos azules, superponiéndose tanto en color como en forma. En un WCST real, la tarjeta de respuesta debe superponerse con cada tarjeta de estímulo en no más de una dimensión.

Esta vez te toca a ti. ¡No hay pistas!

## Soluciones

Puedes descargar el experimento completo, incluidas las soluciones a las tareas adicionales, aquí:

- <https://osf.io/f5er2/>