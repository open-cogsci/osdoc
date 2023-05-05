title: Tutorial intermedio (JavaScript): búsqueda visual
hash: be4398c1389153b66026511513743b6e43fb856b7f7a0dac63fc2069a8be95bb
locale: es
language: Spanish

[TOC]

## Acerca de OpenSesame

OpenSesame es un programa fácil de usar para el desarrollo de experimentos de comportamiento en psicología, neurociencia y economía experimental. Para principiantes, OpenSesame tiene una interfaz gráfica completa, de apuntar y hacer clic. Para usuarios avanzados, OpenSesame admite Python (solo escritorio) y JavaScript (escritorio y navegador).

OpenSesame está disponible gratuitamente bajo la [Licencia Pública General v3][gpl].

## Acerca de este tutorial

Este tutorial muestra cómo crear un experimento básico de búsqueda visual utilizando OpenSesame [(Mathôt, Schreij y Theeuwes, 2012)][references]. Utilizaremos tanto la interfaz gráfica como JavaScript para desarrollar un experimento que puedas ejecutar en línea en un navegador. Se recomienda tener experiencia con OpenSesame y JavaScript. Este tutorial dura aproximadamente una hora.

También está disponible una versión de este tutorial basada en Python. Si no necesitas ejecutar tus experimentos en línea, entonces el tutorial de Python es probablemente lo que necesitas:

- %link:tutorials/intermediate%

## Recursos

- __Descargar__ — Este tutorial supone que estás ejecutando OpenSesame versión 4.0.0 o posterior y OSWeb 2.0 o posterior. Puedes descargar la versión más reciente de OpenSesame desde:
	- %link:download%
- __Documentación__ — Un sitio web dedicado a la documentación se encuentra en:
	- <http://osdoc.cogsci.nl/>
- __Foro__ — Un foro de soporte se encuentra en:
	- <http://forum.cogsci.nl/>

## El experimento

En este tutorial, crearás un experimento básico de búsqueda visual. El experimento se asemeja a los estudios clásicos de búsqueda visual de [Treisman y Gelade (1980)][references], pero no es idéntico.

Antes de comenzar a *construir* el experimento por ti mismo, ya puedes *participar* en él. Esto te dará una buena idea de lo que estás trabajando en este tutorial.

<a role="button" class="btn btn-success btn-align-left" href="https://jatos.mindprobe.eu/publix/1938/start?batchId=2191&generalMultiple">¡Participa en el experimento!</a>

En este experimento, los participantes buscan un objeto objetivo, que puede ser un cuadrado amarillo, un círculo amarillo, un cuadrado azul o un círculo azul; la identidad del objetivo varía entre bloques de ensayos. Los participantes indican si el objetivo está presente o no presionando la flecha derecha (presente) o izquierda (ausente).

Además del objetivo, se muestran cero o más objetos distractores. Hay tres condiciones, y la condición determina qué tipo de distractores hay:

- En la condición *Conjunción*, los distractores pueden tener cualquier forma y color, con la única restricción de que los distractores no pueden ser idénticos al objetivo. Entonces, por ejemplo, si el objetivo es un cuadrado amarillo, los distractores serán círculos amarillos, círculos azules y cuadrados azules.
- En la condición *Característica de forma*, los distractores tienen una forma diferente que el objetivo, pero pueden tener cualquier color. Entonces, por ejemplo, si el objetivo es un cuadrado amarillo, los distractores serán círculos amarillos y círculos azules.
- En la condición *Característica de color*, los distractores pueden tener cualquier forma, pero tienen un color diferente al objetivo. Entonces, por ejemplo, si el objetivo es un cuadrado amarillo, los distractores serán cuadrados azules y círculos azules.

Se muestra comentarios inmediatos después de cada ensayo: un punto verde después de una respuesta correcta y un punto rojo después de una respuesta incorrecta. Se muestra información detallada sobre los tiempos de respuesta promedio y la precisión después de cada bloque de ensayos.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  El experimento de búsqueda visual que implementarás en este tutorial.
--%

Los experimentos como este muestran dos hallazgos típicos:

- Se tarda más tiempo en encontrar el objetivo en la condición de Conjunción que en las dos condiciones de Característica.
- En la condición de Conjunción, los tiempos de respuesta aumentan a medida que aumenta el número de distractores. Esto sugiere que las personas buscan el objetivo un elemento a la vez; esto se llama *búsqueda en serie*.
- En las condiciones de Característica (tanto en forma como en color), los tiempos de respuesta no aumentan, o apenas lo hacen, a medida que aumenta el número de elementos. Esto sugiere que las personas procesan toda la pantalla a la vez; esto se llama *búsqueda en paralelo*.

Según la teoría de la integración de características de Treisman y Gelade, estos resultados reflejan que la condición de Conjunción requiere que combines, o *vincules*, el color y la forma de cada objeto. Esta vinculación requiere atención, y por lo tanto, necesitas desplazar tu atención de un objeto a otro; esto es lento y explica por qué los tiempos de respuesta dependen de cuántos objetos hay. En contraste, en las condiciones de Característica, el color y la forma no necesitan ser vinculadas, y por lo tanto, toda la pantalla se puede procesar de un solo vistazo sin dirigir la atención a cada objeto.

## Diseño experimental

Este diseño:

- Es *intra-sujeto*, porque todos los participantes realizan todas las condiciones
- Es *totalmente cruzado* (o factorial completo), porque todas las combinaciones de condiciones ocurren
- Tiene tres condiciones (o factores):
	- Variado dentro de los bloques:
		- `set_size` con tres niveles (1, 5, 15), o SS<sub>3</sub>
		- `condition` con tres niveles (conjunction, feature_shape, feature_color), o CN<sub>3</sub>
		- `target_present` con dos niveles (presente, ausente), o TP<sub>2</sub>
	- Variado entre bloques:
		- `target_shape` con dos niveles (cuadrado, círculo), o TS<sub>2</sub>
		- `target_color` con dos niveles (amarillo, azul), o TC<sub>2</sub>
- Tiene N sujetos, o <u>S</u><sub>N</sub>

Puedes escribir este diseño como <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

Para obtener más información sobre esta notación para el diseño experimental, consulta:

- %link:experimentaldesign%

## Paso 1: Crear la estructura básica del experimento

Abre OpenSesame y, en la pestaña '¡Comenzar!', selecciona la plantilla Extendida. Esta plantilla proporciona la estructura básica que es común a muchos experimentos de psicología cognitiva, como el que crearemos aquí.

La plantilla Extendida contiene algunos elementos que no necesitamos. Elimina los siguientes elementos:

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Cuando hayas eliminado estos elementos, todavía son visibles en el contenedor de 'elementos no utilizados'. Para eliminar permanentemente estos elementos, haz clic en el contenedor de 'elementos no utilizados' y luego haz clic en el botón 'Eliminar permanentemente elementos no utilizados'.

Finalmente, dale al experimento un buen título, como 'Búsqueda visual'. Para hacer esto, abre la pestaña de propiedades generales (haciendo clic en 'Plantilla extendida' en el área de descripción general) y haz clic en el nombre del experimento para editarlo.

También configura OpenSesame para ejecutar el experimento en un navegador, en lugar de en el escritorio.

El área de descripción general debería verse como %FigStep1:

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  El área de descripción general al final del paso 1.
--%


## Paso 2: Definir las variables experimentales que varían entre bloques

Como se describió anteriormente, dos variables varían entre bloques en nuestro experimento: `target_shape` y `target_color`. Por lo tanto, necesitamos definir estas variables en el *experimental_loop*. Para entender por qué, considera la estructura mostrada en %FigStep1, comenzando desde abajo (es decir, el nivel más indentado).

- *trial_sequence* corresponde a un solo intento
- *block_loop* corresponde a un bloque de intentos
	- Por lo tanto, las variables definidas aquí varían para cada ejecución de *trial_sequence*; en otras palabras, las variables definidas en *block_loop* varían __dentro de los bloques__.
- *block_sequence* corresponde a un bloque de intentos, precedido por un reinicio de las variables de comentarios, y seguido por retroalimentación del participante
- *experimental_loop * corresponde a varios bloques de intentos
	- Por lo tanto, las variables definidas aquí varían para cada ejecución de *block_sequence*; en otras palabras, las variables definidas en *experimental_loop* varían __entre bloques__.
- *experiment* corresponde a todo el experimento, que es una pantalla de instrucciones, seguida de varios bloques de intentos, seguida de una pantalla de fin de experimento

Haz clic en experimental_loop y define:

- `target_shape`, que puede ser 'square' (cuadrado) o 'circle' (círculo); y
- `target_color`, que puede ser 'yellow' (amarillo) o 'blue' (azul).

Tenemos un diseño factorial completo, lo que significa que todas las combinaciones 2 × 2 = 4 deben ocurrir. La tabla de *experimental_loop* ahora debería verse como %FigStep2:

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  La tabla de *experimental_loop* al final del paso 2.
--%

## Paso 3: Dar instrucciones al comienzo de cada bloque

Ahora mismo, el experimento comienza con una sola pantalla de *instrucciones*. En nuestro caso, queremos dar instrucciones antes de cada bloque de intentos para decirle al participante qué objetivo buscar (porque la identidad del objetivo varía entre bloques).

__Mueva las instrucciones a block_sequence__

Por lo tanto, toma el elemento *instructions* y arrástralo a *block_sequence*. Aparecerá una ventana emergente, preguntándote si deseas:

- Insertar el elemento en *block_sequence*, en cuyo caso *instructions* se convertiría en el primer elemento de *block_sequence*; o
- Insertar el elemento después de *block_sequence*, en cuyo caso *instructions* se movería a una posición después de *block_sequence*.

Selecciona la primera opción ('Insertar en'). Ahora *block_sequence* comienza con una pantalla de instrucciones, que es lo que queremos.

__Agregar texto instructivo__

Haz clic en *instructions* para abrirlo y agrega un buen texto instructivo, como:

```text
INSTRUCCIONES

Busca el {target_color} {target_shape}

Presiona la tecla de flecha a la derecha si lo encuentras
Presiona la tecla de flecha a la izquierda si no lo haces

Presiona cualquier tecla para comenzar
```

Los corchetes rizados alrededor de '{target_color}' y '{target_shape}' indican que estos no son textos literales, sino que se refieren a las variables que hemos definido en *experimental_loop*. Cuando se ejecuta el experimento, los valores de estas variables aparecerán aquí y el participante verá (por ejemplo), 'Busca el círculo amarillo'.

__Dar una vista previa visual del objetivo__

También es bueno mostrar al participante el estímulo real que necesita encontrar. Para hacer esto:

- Dibuja un círculo lleno en el centro de la pantalla (asegúrate de que no se superponga con el texto);
- Cambia el color del círculo a '{target_color}'. Esto significa que el color del círculo depende del valor de la variable `target_color`; y
- Cambia la expresión show-if a `target_shape == 'circle'`. Esta es una expresión de Python que verifica si la variable `target_shape` tiene el valor 'circle'. Ten en cuenta que aunque *no puedes* usar `inline_script` de Python completo al ejecutar experimentos en un navegador, *puedes* usar Python para estas expresiones condicionales simples.

En otras palabras, hemos dibujado un círculo cuyo color está determinado por `target_color`; además, este círculo solo se muestra cuando la variable `target_shape` tiene el valor 'circle'. Para obtener más información sobre variables y declaraciones show-if, consulte:

- %link:manual/variables%

Usamos el mismo truco para dibujar un cuadrado:

- Dibuja un cuadrado lleno en el centro de la pantalla;
- Cambia el color del cuadrado a '{target_color}'; y
- Cambia la declaración show-if a `target_shape == 'square'`

La pantalla *instructions* ahora debería verse como %FigStep3:

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  La pantalla de *instructions* al final del paso 3.
--%


## Paso 4: Definir las variables experimentales que varían dentro de los bloques

Tres variables varían dentro de los bloques en nuestro experimento: `condition`, `set_size` y `target_present`. Como se describió en el Paso 2, necesitamos definir estas variables en el *block_loop* para que varíen en cada ejecución de *trial_sequence*.

Las tres variables hacen un total de 3 × 3 × 2 = 18 combinaciones diferentes. Podemos escribirlos manualmente en la tabla, pero como tenemos un diseño factorial completo, también podemos usar el asistente de diseño factorial completo. Para hacer esto, primero abra *block_loop* y haga clic en el botón 'Full-factorial design'.

En la tabla que aparece, coloque los nombres de las variables en la primera fila y los valores en las filas siguientes, como se muestra en %FigFullFactorial.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  La pantalla de *instructions* al final del paso 3.
--%

Ahora haga clic en 'Ok' para generar el diseño completo. La tabla de *block_loop* ahora debería verse como en %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  La tabla de *block_loop* al final del paso 4.
--%

## Paso 5: Crear la secuencia de prueba y agregar un script de inicialización

Queremos que nuestra secuencia de prueba se vea de la siguiente manera:

- Un punto de fijación, para lo cual usaremos un SKETCHPAD.
- Un display de búsqueda, que crearemos en JavaScript con un INLINE_JAVASCRIPT personalizado.
- Recopilación de respuestas, para lo cual usaremos KEYBOARD_RESPONSE.
- Registro de datos, para lo cual utilizaremos LOGGER.
- (También queremos retroalimentación inmediata después de cada prueba, pero esto lo veremos más adelante.)

Entonces, lo único que falta en *trial_sequence* es un INLINE_JAVASCRIPT.

- Inserte un nuevo INLINE_JAVASCRIPT después de *sketchpad* y cambie su nombre a *search_display_script*.
- Cambie el nombre de *sketchpad* a *fixation_dot*, para que su función quede clara; y
- Cambie la duración de *fixation_dot* a 500, de modo que el punto de fijación se muestre durante 500 ms. (Ya debe haber un punto de fijación dibujado; si no, dibuje uno en el centro de *fixation_dot*).

También necesitamos agregar un script de inicialización al comienzo del experimento. Solo lo usaremos para definir (usando `let`) una variable que contendrá el objeto `Canvas` en el que dibujaremos. En JavaScript, debes definir una variable exactamente una vez, y es por eso que no podemos hacerlo en la secuencia *trial*.

- Inserte un nuevo INLINE_JAVASCRIPT en la parte superior de la secuencia *experiment* y cambie su nombre a *init*.

El área de descripción general ahora debe verse como en %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  El área de descripción general al final del paso 5.
--%

## Paso 6: Generar el display de búsqueda

__Programación de arriba hacia abajo y defensiva__

Ahora las cosas se pondrán interesantes: comenzaremos a programar en JavaScript. Utilizaremos dos principios rectores: la programación *de arriba hacia abajo* y la programación *defensiva*.

- La *programación de arriba hacia abajo* significa que comenzamos con la lógica más abstracta, sin preocuparnos por cómo se implementa esta lógica. Una vez que la lógica más abstracta esté en su lugar, nos moveremos hacia abajo a una lógica ligeramente menos abstracta, y así sucesivamente, hasta que lleguemos a los detalles de la implementación. Esta técnica ayuda a mantener estructurado el código.
- La programación *defensiva* significa que asumimos que cometemos errores. Por lo tanto, para protegernos de nosotros mismos, incluimos controles de cordura en el código.

*Nota:* La explicación a continuación supone que estás algo familiarizado con JavaScript. Si conceptos como `Array`, bucle `for` y funciones no significan nada para ti, entonces es mejor que repases un tutorial de JavaScript introductorio. Puedes encontrar enlaces a tutoriales de JavaScript aquí:

- %link:manual/javascript/about%

La lógica del código se muestra en %FigHierarchy. Los números indican el orden en que implementaremos la funcionalidad, comenzando por el nivel abstracto.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  La lógica del código para dibujar una pantalla de búsqueda visual.
--%

__Declarando variables con let, var y const__

En JavaScript, tienes que 'declarar' una variable antes de poder usarla. (En Python, esto no es necesario). En nuestro caso, usaremos una variable llamada `c`, que por lo tanto necesitamos declarar. Para hacerlo, abre la pestaña Preparar del script *init* y usa la palabra clave `let` para declarar la variable `c`:

```js
let c
```

Hay tres formas diferentes de declarar variables:

- Usando `let`, como lo hemos hecho aquí. En OpenSesame, esto hace que la variable esté disponible en JavaScript pero no como una variable experimental en la interfaz de usuario.
- Usando `var`. En OpenSesame, esto hace que la variable también esté disponible como una variable experimental en la interfaz de usuario. (Haremos eso más tarde para la variable `correct_response`).
- Usando `const`. Esto es similar a `var` con la diferencia importante de que la variable no se puede reasignar más tarde.

__ Las fases de Preparar y Ejecutar__

Abre *search_display_script* y cambia a la pestaña Preparar. OpenSesame distingue dos fases de ejecución:

- Durante la fase de Preparar, se le da la oportunidad a cada ítem de prepararse; lo que esto significa depende del ítem: para un SKETCHPAD, significa dibujar un lienzo (pero no mostrarlo); para un SAMPLER, significa cargar un archivo de sonido (pero no reproducirlo); etc.
- Durante la fase de Ejecutar, cada ítem se ejecuta realmente; nuevamente, lo que esto significa depende del ítem: para un SKETCHPAD, significa mostrar el lienzo preparado previamente; para un SAMPLER, significa reproducir un archivo de sonido cargado previamente.

Para un INLINE_JAVASCRIPT, debes decidir tú mismo qué poner en la fase de Preparar y qué poner en la fase de Ejecutar. La distinción suele ser bastante clara: en nuestro caso, ponemos el código para dibujar el lienzo en la fase de Preparar y el código para mostrar el lienzo (que es pequeño) en la fase de Ejecutar.

Ver también:

- %link:prepare-run%

__Implementar el nivel abstracto__

Comenzamos en el nivel más abstracto: definiendo una función que dibuja una pantalla de búsqueda visual. No especificamos *cómo* se hace esto; simplemente suponemos que hay una función que lo hace y nos preocupamos por los detalles más tarde, eso es la programación de arriba hacia abajo.

En la pestaña Preparar, ingresa el siguiente código:

```js
c = draw_canvas()
```

¿Qué sucede aquí? Nosotros...

- Llamamos a `draw_canvas()`, que devuelve un objeto `Canvas` que almacenamos como `c`; en otras palabras, `c` es un objeto `Canvas` que corresponde a la pantalla de búsqueda. Esto supone que hay una función `draw_canvas()`, aunque aún no la hemos definido.

Un objeto `Canvas` es una única pantalla; es, en cierto sentido, el equivalente en JavaScript de un SKETCHPAD. Ver también:

- %link:manual/javascript/canvas%

Ahora vamos un paso más abajo definiendo `draw_canvas()` (por encima del resto del código hasta ahora):

```js
/**
 * Dibuja el lienzo de búsqueda.
 * @return Un Canvas
 **/
function draw_canvas() {
    let c = Canvas()
    let xy_list = xy_random(set_size, 500, 500, 75)
    if (target_present === 'present') {
        let [x, y] = xy_list.pop()
        draw_target(c, x, y)
    } else if (target_present !== 'absent') {
        throw 'Valor no válido para target_present ' + target_present
    }
    for (let [x, y] of xy_list) {
        draw_distractor(c, x, y)
    }
    return c
}
```

¿Qué sucede aquí? Nosotros...

- Crear un lienzo vacío, `c`, usando la función de fábrica `Canvas()`.
- Generar un array de coordenadas aleatorias `x, y`, llamado `xy_list`, usando otra función común, `xy_random()`. Este array determina dónde se muestran los estímulos. Las ubicaciones se toman de un área de 500 × 500 px con un espacio mínimo de 75 px.
- Verificar si la variable experimental `target_present` tiene el valor 'present'; de ser así, `pop()` una tupla `x, y` de `xy_list`, y dibujar el objetivo en esta ubicación. Esto supone que hay una función `draw_target()`, aunque aún no la hemos definido.
- Si `target_present` no es ni 'present' ni 'absent', lanzamos un error; esto es programación defensiva y nos protege de errores tipográficos (por ejemplo, si hubiéramos ingresado accidentalmente 'presenr' en lugar de 'present').
- Recorrer todos los valores restantes de `x, y` y dibujar un distractor en cada posición. Esto supone que hay una función `draw_distractor()`, aunque aún no la hemos definido.
- Devolver `c`, que ahora tiene el panel de búsqueda dibujado en él.

Hay varias funciones comunes, como `Canvas()` y `xy_random()`, que siempre están disponibles en un elemento INLINE_JAVASCRIPT. Ver:

- %link:manual/javascript/common%

Las variables experimentales son variables globales. Es por eso que puedes referirte a `set_size`, que se define en *block_loop*, aunque la variable `set_size` nunca se define explícitamente en el guion. Lo mismo ocurre con `target_shape`, `target_color`, `condition`, etc. Ver:

- %link:var%

__Implementar el nivel intermedio__

Ahora damos un paso más, definiendo `draw_target` (encima del resto del guion hasta ahora):

```js
/**
 * Dibuja el objetivo.
 * @param c Un Canvas
 * @param x Una coordenada x
 * @param y Una coordenada y
 **/
function draw_target(c, x, y) {
    draw_shape(c, x, y, target_color, target_shape)
}
```

¿Qué ocurre aquí? Nosotros …

- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma que se deben dibujar. Esto supone que hay una función `draw_shape()`, aunque aún no la hemos definido.

También definimos `draw_distractor` (encima del resto del guion hasta ahora):

```js
/**
 * Dibuja un único distractor.
 * @param c Un Canvas
 * @param x Una coordenada x
 * @param y Una coordenada y
 **/
function draw_distractor(c, x, y) {
    if (condition === 'conjunction') {
        draw_conjunction_distractor(c, x, y)
    } else if (condition === 'feature_shape') {
        draw_feature_shape_distractor(c, x, y)
    } else if (condition === 'feature_color') {
        draw_feature_color_distractor(c, x, y)
    } else {
        throw 'Condición inválida: ' + condition
    }
}
```

¿Qué ocurre aquí? Nosotros …

- Llamamos a otra función para dibujar un distractor más específico dependiendo de la condición.
- Verificamos si la `condition` tiene alguno de los valores esperados. De lo contrario, lanzamos un error. ¡Esto es programación defensiva! Sin esta verificación, si cometemos un error tipográfico en algún lugar, el distractor podría simplemente no mostrarse sin causar un mensaje de error.

Ahora definimos la función que dibuja los distractores en la condición de Conjunción (encima del resto del guion hasta ahora):

```js
/**
 * Dibuja un único distractor en la condición de conjunción: un objeto que
 * puede tener cualquier forma y color, pero no puede ser idéntico al objetivo.
 * @param c Un Canvas.
 * @param x Una coordenada x.
 * @param y Una coordenada y.
 **/
function draw_conjunction_distractor(c, x, y) {
    let conjunctions = [
        ['amarillo', 'círculo'],
        ['azul', 'círculo'],
        ['amarillo', 'cuadrado'],
        ['azul', 'cuadrado']
    ]
    let [color, forma] = random.pick(conjunctions)
    while (color === target_color && forma === target_shape) {
        [color, forma] = random.pick(conjunctions)
    }
    draw_shape(c, x, y, color, forma)
}
```

¿Qué ocurre aquí? Nosotros …

- Definir una lista, `conjunctions`, de todas las posibles combinaciones de color y forma.
- Seleccionar aleatoriamente una de las combinaciones de color y forma de `conjunctions`.
- Verificar si el color y la forma seleccionados son iguales al color y la forma del objetivo. Si es así, seguir seleccionando un nuevo color y forma hasta que esto ya no ocurra. Después de todo, ¡el distractor no puede ser idéntico al objetivo!
- Llamar a otra función, `draw_shape()`, y especificar el color y la forma del distractor que se va a dibujar. Esto supone que hay una función `draw_shape()`, aunque aún no la hemos definido.

Además, nosotros …

- Usamos la biblioteca `random`, que corresponde al paquete `random-ext`. Esta biblioteca contiene funciones de aleatorización útiles (como `random.pick()`) y es una de las bibliotecas de JavaScript no estándar que se incluye con OSWeb.

Ahora definimos la función que dibuja distractores en la condición de Forma Característica (encima del resto del guion hasta ahora):

```js
/**
 * Dibuja un único distractor en la condición de forma-característica: un objeto que
 * tiene una forma diferente a la del objetivo, pero puede tener cualquier color.
 * @param c Un Canvas.
 * @param x Una coordenada x.
 * @param y Una coordenada y.
 **/
function draw_feature_shape_distractor(c, x, y) {
    let colors = ['amarillo', 'azul']
    let color = random.pick(colors)
    let shape
    if (target_shape === 'circle') {
        shape = 'square'
    } else if (target_shape === 'square') {
        shape = 'circle'
    } else {
        throw 'Invalid target_shape: ' + target_shape
    }
    draw_shape(c, x, y, color, shape)
}
```

¿Qué sucede aquí? Nosotros …

- Seleccionamos aleatoriamente un color.
- Elegimos una forma cuadrada si el objetivo es un círculo, y una forma circular si el objetivo es cuadrado.
- Si `target_shape` no es 'circle' ni 'square', mostramos un error, ¡más programación defensiva!
- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma del distractor que se va a dibujar. Esto supone que hay una función `draw_shape()`, aunque aún no la hemos definido.

Ahora definimos la función que dibuja distractores en la condición de Color Característico (encima del resto del guion hasta ahora):

```js
/**
 * Dibuja un único distractor en la condición de color-característico: un objeto que
 * tiene un color diferente al del objetivo, pero puede tener cualquier forma.
 * @param c Un Canvas.
 * @param x Una coordenada x.
 * @param y Una coordenada y.
 **/
function draw_feature_color_distractor(c, x, y) {
    let shapes = ['circle', 'square']
    let shape = random.pick(shapes)
    let color
    if (target_color === 'yellow') {
        color = 'blue'
    } else if (target_color === 'blue') {
        color = 'yellow'
    } else {
        throw 'Invalid target_color: ' + target_color
    }
    draw_shape(c, x, y, color, shape)
}
```

¿Qué sucede aquí? Nosotros …

- Seleccionamos aleatoriamente una forma.
- Elegimos un color azul si el objetivo es amarillo, y un color amarillo si el objetivo es azul.
- Si `target_color` no es 'yellow' ni 'blue', mostramos un error, ¡más programación defensiva!
- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma del distractor que se va a dibujar. Esto supone que hay una función `draw_shape()`, aunque aún no la hemos definido.

__Implementar el nivel detallado__

Ahora bajamos hasta los detalles definiendo la función que realmente dibuja una forma en el lienzo (encima del resto del guion hasta ahora):

```js
/**
 * Dibuja una figura única.
 * @param c Un Canvas.
 * @param x Una coordenada x.
 * @param y Una coordenada y.
 * @param color Un color (amarillo o azul)
 * @param figura Una figura (cuadrado o círculo)
 **/
function draw_shape(c, x, y, color, figura) {
    if (figura === 'cuadrado') {
        // ¡Los parámetros se pasan como un Objeto!
        c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
    } else if (figura === 'círculo') {
        // ¡Los parámetros se pasan como un Objeto!
        c.circle({x:x, y:y, r:25, color:color, fill:true})
    } else {
        throw 'Figura no válida: ' + figura
    }
    if (color !== 'amarillo' && color !== 'azul') {
        throw 'Color no válido: ' + color
    }
}
```

¿Qué sucede aquí? Nosotros …

- Verificamos qué figura debe dibujarse. Para los cuadrados, agregamos un elemento `rect()` al canvas. Para los círculos, agregamos un elemento `circle()`.
- Verificamos si la forma es un cuadrado o un círculo, y si no es así, lanzamos un error. ¡Este es otro ejemplo de programación defensiva! Nos aseguramos de no haber especificado accidentalmente una figura no válida.
- Verificamos si el color no es ni amarillo ni azul, y si no es así, lanzamos un error.

Es importante que las funciones de `Canvas` acepten un solo objeto (`{}`) que especifique todos los parámetros por nombre, de la siguiente manera:

```js
// Correcto: pasa un solo objeto que contiene todos los parámetros por nombre
c.rect({x:x-25, y:y-25, w:50, h:50, color:color, fill:true})
// Incorrecto: no pases parámetros por orden
// c.rect(x-25, y-25, 50, 50, color, true)
// Incorrecto: los parámetros con nombre no son compatibles con JavaScript
// c.rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=true)
```

__Implementar la fase de ejecución__

Debido a que hicimos todo el trabajo duro en la fase de preparación, la fase de ejecución es simplemente:

```js
c.show()
```

¡Eso es! Ahora has dibujado una presentación completa de búsqueda visual. Y, lo más importante, lo has hecho de una manera fácil de entender, debido a la programación de arriba hacia abajo, y segura, debido a la programación defensiva.

## Paso 7: Define la respuesta correcta

Para saber si el participante responde correctamente, necesitamos conocer la respuesta correcta. Puedes definir esto explícitamente en el *block_loop* (como se hizo en el tutorial para principiantes); pero aquí vamos a utilizar un simple JavaScript que verifica si el objetivo está presente o no y define la respuesta correcta en consecuencia.

Para hacer esto, primero necesitamos declarar la variable en la pestaña Preparar del script *init*, justo debajo de `let c`. Esta vez, usamos la palabra clave `var` para declarar `correct_response`, porque esto hace que la variable esté disponible en la interfaz de usuario (mientras que `let` no lo hace):

```js
var correct_response
```

A continuación, inserta un nuevo INLINE_JAVASCRIPT al comienzo de *trial_sequence* y cambia el nombre a *correct_response_script*. En la fase de preparación, ingresa el siguiente código:

```js
if (target_present === 'presente') {
    correct_response = 'derecha'
} else if (vars.target_present === 'ausente') {
    correct_response = 'izquierda'
} else {
    throw 'target_present debe ser ausente o presente, no ' + target
}
```

¿Qué sucede aquí? Nosotros …

- Verificamos si el objetivo está presente o no. Si el objetivo está presente, la respuesta correcta es 'derecha' (la tecla de flecha derecha); si el objetivo está ausente, la respuesta correcta es 'izquierda' (la tecla de flecha izquierda). La variable experimental `correct_response` es utilizada automáticamente por OpenSesame; por lo tanto, no necesitamos indicar explícitamente que esta variable contiene la respuesta correcta.
- Verificamos si el objetivo está presente o ausente, y si no es así, lanzamos un error, otro ejemplo de programación defensiva.

## Paso 8: Proporcionar información por ensayo

La retroalimentación después de cada ensayo puede motivar a los participantes; sin embargo, la retroalimentación por ensayo no debe interferir con el flujo del experimento. Una buena manera de proporcionar retroalimentación por ensayo es mostrar brevemente un punto de fijación verde después de una respuesta correcta y un punto de fijación rojo después de una respuesta incorrecta.

Para hacer esto:

- Inserta dos nuevos SKETCHPADs en *trial_sequence*, justo después de *keyboard_response*.
- Renombra un SKETCHPAD a *green_dot*, dibuja un punto de fijación verde central en él y cambia su duración a 500.
- Renombra el otro SKETCHPAD a *red_dot*, dibuja un punto de fijación rojo central en él y cambia su duración a 500.

Por supuesto, solo uno de los dos puntos debe mostrarse en cada ensayo. Para lograr esto, especificaremos declaraciones run-if en *trial_sequence*:

- Cambia la declaración run-if para *green_dot* a 'correct == 1', indicando que solo debe mostrarse después de una respuesta correcta.
- Cambia la declaración run-if para *red_dot* a 'correct == 0', indicando que solo debe mostrarse después de una respuesta incorrecta.

La variable `correct` se crea automáticamente si la variable `correct_response` está disponible; por eso definimos `correct_response` en el paso 7. Para obtener más información sobre las variables y las declaraciones run-if, consulta:

- %enlace:manual/variables%

El *trial_sequence* ahora debería verse como %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  El *trial_sequence* al final del paso 8.
--%


## Paso 9: Comprobando la compatibilidad

Cuando desees ejecutar un experimento en un navegador, no podrás utilizar toda la funcionalidad de OpenSesame. Para verificar si tu experimento puede ejecutarse en un navegador, puedes usar la compatibilidad de OSWeb yendo al menú → Herramientas → OSweb. Si has seguido todos los pasos de este tutorial, la verificación de compatibilidad será exitosa:

%--
figure:
 id: FigCompatibilityCheck
 source: compatibility-check.png
 caption: |
  La verificación de compatibilidad indica si el experimento es compatible con OSWeb.
--%

Para obtener una lista de las funciones compatibles con OSWeb, consulta:

- %enlace:manual/osweb/osweb%


## ¡Terminado!

¡Felicidades, el experimento está completo! Puedes probarlo presionando el botón de la barra de herramientas que muestra un círculo verde con un botón gris de reproducción en el interior (atajo: `Alt+Ctrl+W`).

Si el experimento no funciona a la primera: no te preocupes y calmadamente averigua de dónde proviene el error. Los bloqueos son parte del proceso normal de desarrollo. Pero puedes ahorrarte mucho tiempo y dolores de cabeza trabajando de manera estructurada, como lo hemos hecho en este tutorial.

## Referencias

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un generador de experimentos gráfico y de código abierto para las ciencias sociales. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). Una teoría de integración de características de la atención. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[referencias]: #referencias
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html