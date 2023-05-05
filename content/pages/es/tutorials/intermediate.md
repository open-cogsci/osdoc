title: Tutorial intermedio (Python) búsqueda visual
hash: bc6a941f73aa734c08871ddf1fd8ffcd188aed4dde8ec8200b599a033ffa1de4
locale: es
language: Spanish

[TOC]

## Acerca de OpenSesame

OpenSesame es un programa fácil de usar para el desarrollo de experimentos conductuales en psicología, neurociencia y economía experimental. Para principiantes, OpenSesame cuenta con una interfaz gráfica completa, de apuntar y hacer clic. Para usuarios avanzados, OpenSesame admite Python (solo escritorio) y JavaScript (escritorio y navegador).

OpenSesame está disponible gratuitamente bajo la [Licencia Pública General v3][gpl].

## Acerca de este tutorial

Este tutorial muestra cómo crear un experimento básico de búsqueda visual usando OpenSesame [(Mathôt, Schreij y Theeuwes, 2012)][references]. Usaremos tanto la interfaz gráfica como la secuencia de comandos en Python para desarrollar un experimento que puede ejecutar en el escritorio en un entorno de laboratorio tradicional. Se recomienda algo de experiencia con OpenSesame y Python. Este tutorial dura aproximadamente una hora.

También hay disponible una versión basada en JavaScript de este tutorial. Si desea ejecutar sus experimentos en línea en un navegador (con OSWeb), entonces el tutorial de JavaScript es lo que necesita:

- %link:tutorials/intermediate-javascript%

## Recursos

- __Descargar__ — Este tutorial supone que está ejecutando la versión 4.0.0 de OpenSesame o posterior. Puede descargar la versión más reciente de OpenSesame desde:
	- %link:download%
- __Documentación__ — Se puede encontrar un sitio web de documentación dedicado en:
	- <http://osdoc.cogsci.nl/>
- __Foro__ — Se puede encontrar un foro de soporte en:
	- <http://forum.cogsci.nl/>

## El experimento

En este tutorial, creará un experimento básico de búsqueda visual. El experimento se asemeja a los estudios clásicos de búsqueda visual de [Treisman y Gelade (1980)][references], pero no es idéntico.

En este experimento, los participantes buscan un objeto objetivo, que puede ser un cuadrado amarillo, un círculo amarillo, un cuadrado azul o un círculo azul; la identidad del objetivo varía entre bloques de ensayos. Los participantes indican si el objetivo está presente o no presionando la flecha derecha (presente) o izquierda (ausente).

Además del objetivo, se muestran cero o más objetos distractores. Hay tres condiciones y la condición determina qué tipo de distractores hay:

- En la condición de *Conjunción*, los distractores pueden tener cualquier forma y color, con la única restricción de que los distractores no pueden ser idénticos al objetivo. Entonces, por ejemplo, si el objetivo es un cuadrado amarillo, entonces los distractores son círculos amarillos, círculos azules y cuadrados azules.
- En la condición de *Característica de forma*, los distractores tienen una forma diferente del objetivo, pero pueden tener cualquier color. Entonces, por ejemplo, si el objetivo es un cuadrado amarillo, entonces los distractores son círculos amarillos y círculos azules.
- En la condición de *Característica de color*, los distractores pueden tener cualquier forma, pero tienen un color diferente al objetivo. Entonces, por ejemplo, si el objetivo es un cuadrado amarillo, entonces los distractores son cuadrados azules y círculos azules.

Se muestra una retroalimentación inmediata después de cada ensayo: un punto verde después de una respuesta correcta y un punto rojo después de una respuesta incorrecta. Se muestra una retroalimentación detallada sobre los tiempos de respuesta promedio y la precisión después de cada bloque de ensayos.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg
 caption: |
  El experimento de búsqueda visual que implementarás en este tutorial.
--%

Experimentos como este muestran dos hallazgos típicos:

- Lleva más tiempo encontrar el objetivo en la condición de Conjunción que en las dos condiciones de Característica.
- En la condición de Conjunción, los tiempos de respuesta aumentan a medida que aumenta el número de distractores. Esto sugiere que las personas buscan el objetivo un elemento a la vez; esto se llama *búsqueda en serie*.
- En las condiciones de Característica (tanto de forma como de color), los tiempos de respuesta no aumentan, o apenas aumentan, a medida que aumenta el número de distractores. Esto sugiere que las personas procesan toda la pantalla a la vez; esto se llama *búsqueda en paralelo*.

Según la teoría de integración de características de Treisman y Gelade, estos resultados reflejan que la condición de Conjunción requiere que combines, o *vincules*, el color y la forma de cada objeto. Este enlace requiere atención, y por lo tanto necesitas desplazar tu atención de un objeto a otro; esto es lento y explica por qué los tiempos de respuesta dependen de cuántos objetos hay. En contraste, en las condiciones de Característica, el color y la forma no necesitan ser vinculados, y por lo tanto, toda la pantalla se puede procesar en un solo barrido sin que la atención se dirija a cada objeto en particular.

## Diseño experimental

Este diseño:

- Es *dentro de sujetos*, porque todos los participantes realizan todas las condiciones
- Está *completamente cruzado* (o completo-factorial), porque todas las combinaciones de condiciones ocurren
- Tiene tres condiciones (o factores):
	- Variadas dentro de los bloques:
		- `set_size` con tres niveles (1, 5, 15), o SS<sub>3</sub>
		- `condition` con tres niveles (conjunción, feature_shape, feature_color), o CN<sub>3</sub>
		- `target_present` con dos niveles (presente, ausente), o TP<sub>2</sub>
	- Variadas entre bloques:
		- `target_shape` con dos niveles (cuadrado, círculo), o TS<sub>2</sub>
		- `target_color` con dos niveles (amarillo, azul), o TC<sub>2</sub>
- Tiene N sujetos, o <u>S</u><sub>N</sub>

Puede escribir este diseño como <u>S</u><sub>N</sub>×SS<sub>3</sub>×CN<sub>3</sub>×TP<sub>2</sub>×TS<sub>2</sub>×TC<sub>2</sub>

Para más información sobre esta notación para el diseño experimental, consulte:

- %link:diseñoexperimental%

## Paso 1: Crear la estructura básica del experimento

Abra OpenSesame y, en la pestaña '¡Comenzar!', seleccione la plantilla Extended (Extendida). Esta plantilla proporciona la estructura básica que es común en muchos experimentos de psicología cognitiva, como el que crearemos aquí.

La plantilla Extended contiene algunos elementos que no necesitamos. Elimine los siguientes elementos:

- *about_this_template*
- *practice_loop*
- *end_of_practice*

Cuando haya eliminado estos elementos, seguirán siendo visibles en el contenedor de 'Elementos no utilizados'. Para eliminar de forma permanente estos elementos, haga clic en el contenedor de 'Elementos no utilizados' y luego haga clic en el botón 'Eliminar permanentemente elementos no utilizados'.

Finalmente, dale al experimento un buen título, como 'Búsqueda visual'. Para hacerlo, abra la pestaña de propiedades generales (haciendo clic en 'Plantilla extendida' en el área de descripción general) y haga clic en el nombre del experimento para editarlo.

El área de descripción general debería verse ahora como %FigStep1:

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  El área de descripción general al final del paso 1.
--%

## Paso 2: Definir las variables experimentales que varían entre bloques

Como se describió anteriormente, dos variables varían entre bloques en nuestro experimento: `target_shape` y `target_color`. Por lo tanto, necesitamos definir estas variables en el *experimental_loop*. Para comprender por qué, considere la estructura mostrada en %FigStep1, comenzando desde la parte inferior (es decir, el nivel más sangrado).

- *trial_sequence* corresponde a un solo ensayo
- *block_loop* corresponde a un bloque de ensayos
	- Por lo tanto, las variables definidas aquí varían para cada ejecución de *trial_sequence*; en otras palabras, las variables definidas en *block_loop* se varían __dentro de bloques__.
- *block_sequence* corresponde a un bloque de ensayos, precedido por el reinicio de las variables de feedback, y seguido por el feedback del participante
- *experimental_loop* corresponde a múltiples bloques de ensayos
	- Por lo tanto, las variables definidas aquí varían para cada ejecución de *block_sequence*; en otras palabras, las variables definidas en *experimental_loop* varían __entre bloques__.
- *experiment* se corresponde con el experimento completo, que es una pantalla de instrucciones, seguida de bloques múltiples de ensayos, y seguida de una pantalla de fin de experimento

Haga clic en el loop experimental y defina:

- `target_shape`, que puede ser 'cuadrado' o 'círculo'; y
- `target_color`, que puede ser 'amarillo' o 'azul'.

Tenemos un diseño factorial completo, lo que significa que deben ocurrir todas las 2 × 2 = 4 combinaciones. La tabla de *experimental_loop* debería verse ahora como en %FigStep2:

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  La tabla de *experimental_loop* al final del paso 2.
--%

## Paso 3: Dar instrucciones al inicio de cada bloque

En este momento, el experimento comienza con una única pantalla de *instrucciones*. En nuestro caso, queremos dar instrucciones antes de cada bloque de ensayos, para indicarle al participante qué objetivo buscar (porque la identidad del objetivo varía entre bloques).

__Mueva las instrucciones a la secuencia de bloques__

Por lo tanto, tome el elemento *instrucciones* y arrástrelo a *block_sequence*. Aparecerá una ventana emergente, preguntándole si desea:

- Insertar el elemento en *block_sequence*, en cuyo caso *instrucciones* se convertiría en el primer elemento de *block_sequence*; o
- Insertar el elemento después de *block_sequence*, en cuyo caso *instrucciones* se movería a una posición después de *block_sequence*.

Seleccione la primera opción ('Insertar en'). Ahora *block_sequence* comienza con una pantalla de instrucciones, que es lo que queremos.

__Agregar texto de instrucción__

Haga clic en *instrucciones* para abrirlo y agregue un buen texto de instrucción, como:

```text
INSTRUCCIONES

Busca el {target_color} {target_shape}

Presiona la tecla de flecha derecha si lo encuentras
Presiona la tecla de flecha izquierda si no

Presiona cualquier tecla para comenzar
```

Los corchetes de llaves '{}' alrededor de '{target_color}' y '{target_shape}' indican que no se trata de texto literal, sino que se refieren a las variables que hemos definido en *experimental_loop*. Cuando se ejecuta el experimento, los valores de estas variables aparecerán aquí y el participante verá (por ejemplo), 'Busca el círculo amarillo'.

__Proporcione una vista previa visual del objetivo__

También es bueno mostrar al participante el estímulo real que necesita encontrar. Para hacer esto:

- Dibuje un círculo lleno en el centro de la pantalla (asegúrese de que no se superponga con el texto);
- Cambie el color del círculo a '{target_color}'. Esto significa que el color del círculo depende del valor de la variable `target_color`; y
- Cambie la expresión show-if a `target_shape == 'circle'`. Esta es una expresión Python que verifica si la variable `target_shape` tiene el valor 'círculo'.

En otras palabras, hemos dibujado un círculo cuyo color está determinado por `target_color`; además, este círculo solo se muestra cuando la variable `target_shape` tiene el valor 'círculo'. Para obtener más información sobre variables y declaraciones show-if, consulte:

- %link:manual/variables%

Usamos el mismo truco para dibujar un cuadrado:

- Dibuje un cuadrado lleno en el centro de la pantalla;
- Cambie el color del cuadrado a '{target_color}'; y
- Cambie la declaración show-if a `target_shape == 'square'`

La pantalla de *instrucciones* ahora debería verse como en %FigStep3:

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  La pantalla *instrucciones* al final del paso 3.
--%

## Paso 4: Definir variables experimentales que varían dentro de los bloques

Tres variables varían dentro de los bloques en nuestro experimento: `condition`, `set_size` y `target_present`. Como se describe en el Paso 2, necesitamos definir estas variables en el *block_loop* para que varíen en cada ejecución de *trial_sequence*.

Las tres variables hacen un total de 3 × 3 × 2 = 18 combinaciones diferentes. Podemos escribirlos manualmente en la tabla, pero, como tenemos un diseño factorial completo, también podemos usar el asistente de diseño factorial completo. Para hacer esto, primero abra *block_loop* y haga clic en el botón 'Diseño factorial completo'.

En la tabla que aparece, coloque los nombres de las variables en la primera fila y los valores en las filas siguientes, como se muestra en %FigFullFactorial.

%--
figure:
 id: FigFullFactorial
 source: fullfactorial.png
 caption: |
  La pantalla *instrucciones* al final del paso 3.
--%

Ahora haga clic en 'Aceptar' para generar el diseño completo. La tabla de *block_loop* debería verse ahora como en %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  La tabla de *block_loop* al final del paso 4.
--%

## Paso 5: Crear la secuencia del ensayo

Queremos que nuestra secuencia de ensayo sea como sigue:

- Un punto de fijación, para lo cual usaremos un SKETCHPAD.
- Una pantalla de búsqueda, que crearemos en Python con un INLINE_SCRIPT personalizado.
- Recopilación de respuestas, para lo cual usaremos un KEYBOARD_RESPONSE.
- Registro de datos, para lo cual usaremos un LOGGER.
- (También queremos retroalimentación inmediata después de cada ensayo, pero volveremos a esto más tarde.)

Entonces, lo único que falta es un INLINE_SCRIPT.

- Inserte un nuevo INLINE_SCRIPT después de *sketchpad* y cámbiele el nombre a *search_display_script*.
- Cambie el nombre de *sketchpad* a *fixation_dot*, para que sea clara su función; y
- Cambie la duración de *fixation_dot* a 500, para que el punto de fijación se muestre durante 500 ms. (Ya debería haber un punto de fijación dibujado; si no, dibuje uno en el centro de *fixation_dot*.)

El área de descripción general ahora debería verse como en %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  El área de descripción general al final del paso 5.
--%

## Paso 6: Generar la pantalla de búsqueda

__Programación de arriba hacia abajo y defensiva__

Ahora las cosas se pondrán interesantes: comenzaremos a programar en Python. Usaremos dos principios guía: la programación *de arriba hacia abajo* y *defensiva*.

- La programación *de arriba hacia abajo* significa que comenzamos con la lógica más abstracta, sin preocuparnos por cómo se implementa esta lógica. Una vez que la lógica más abstracta está en su lugar, avanzamos hacia una lógica menos abstracta, y así sucesivamente, hasta llegar a los detalles de la implementación. Esta técnica ayuda a mantener el código estructurado.
- La programación *defensiva* significa que asumimos que cometemos errores. Por lo tanto, para protegernos de nosotros mismos, incorporamos verificaciones de cordura en el código.

*Nota:* La explicación a continuación supone que estás un poco familiarizado con el código en Python. Si conceptos como `list`, `tuple` y funciones no significan nada para ti, entonces es mejor pasar primero por un tutorial introductorio de Python, como este:

- <https://pythontutorials.eu/>

La lógica del código se muestra en %FigHierarchy. Los números indican el orden en que implementaremos la funcionalidad, comenzando por el nivel abstracto.

%--
figure:
 id: FigHierarchy
 source: hierarchy.svg
 caption: |
  La lógica del código para dibujar un visualizador de búsqueda.
--%

__Las fases de Preparación y Ejecución__

Abre *search_display_script* y cambia a la pestaña Prepare. OpenSesame distingue dos fases de ejecución:

- Durante la fase de Preparación, se le da la oportunidad a cada elemento de prepararse; lo que esto significa depende del elemento: para un SKETCHPAD, significa dibujar un canvas (pero no mostrarlo); para un SAMPLER, significa cargar un archivo de sonido (pero no reproducirlo); etc.
- Durante la fase de Ejecución, cada elemento se ejecuta realmente; de nuevo, lo que esto significa depende del elemento: para un SKETCHPAD, significa mostrar el canvas previamente preparado; para un SAMPLER, significa reproducir un archivo de sonido previamente cargado.

Para un INLINE_SCRIPT, tienes que decidir tú mismo qué poner en la fase de Preparación y qué poner en la fase de Ejecución. La distinción suele ser bastante clara: en nuestro caso, ponemos el código para dibujar el canvas en la fase de Preparación, y el código para mostrar el canvas (que es pequeño) en la fase de Ejecución.

Ver también:

- %link:prepare-run%

__Implementar el nivel abstracto__

Comenzamos en el nivel más abstracto: definiendo una función que dibuja una pantalla de búsqueda visual. No especificamos *cómo* se hace esto; simplemente suponemos que hay una función que lo hace, y nos preocuparemos por los detalles más tarde, eso es programación de arriba hacia abajo.

En la pestaña Prepare, ingresa el siguiente código:

~~~ .python
c = draw_canvas()
~~~

¿Qué pasa aquí? Nosotros …

- Llama a `draw_canvas()`, que devuelve un objeto `Canvas` que almacenamos como `c`; en otras palabras, `c` es un objeto `Canvas` que corresponde a la pantalla de búsqueda. Esto supone que hay una función `draw_canvas()`, aunque aún no la hayamos definido.

Un objeto `Canvas` es una sola pantalla; es, en cierto sentido, el homólogo en Python de un SKETCHPAD. Vea también:

- %link:manual/python/canvas%

Ahora vamos un paso más abajo definiendo `draw_canvas()` (encima del resto del script hasta ahora):

~~~ .python
def draw_canvas():
    """Dibuja el lienzo de búsqueda.

    Devoluciones
    -------
    Canvas
    """
    c = Canvas()
    xy_list = xy_random(n=set_size, width=500, height=500, min_dist=75)
    if target_present == 'present':
        x, y = xy_list.pop()
        draw_target(c, x, y)
    elif target_present != 'absent':
        raise Exception(f'Valor no válido para target_present: {target_present}')
    for x, y in xy_list:
        draw_distractor(c, x, y)
    return c
~~~


¿Qué ocurre aquí? Nosotros …

- Creamos un lienzo vacío, `c`, utilizando la función de fábrica `Canvas()`.
- Generamos una lista de coordenadas `x, y` aleatorias, llamada `xy_list`, utilizando otra función común, `xy_random()`. Esta lista determina dónde se muestran los estímulos.
- Verificamos si la variable experimental `target_present` tiene el valor 'present'; si es así, hacemos `pop()` a una tupla `x, y` de `xy_list` y dibujamos el objetivo en esta ubicación. Esto supone que hay una función `draw_target()`, aunque aún no la hayamos definido.
- Si `target_present` no es 'present' ni 'absent', generamos una `Exception`; esto es programación defensiva y nos protege de errores tipográficos (por ejemplo, si hubiéramos ingresado accidentalmente 'presenr' en lugar de 'present').
- Recorremos todas las tuplas `x, y` restantes y dibujamos un distractor en cada posición. Esto supone que hay una función `draw_distractor()`, aunque aún no la hayamos definido.
- Devolvemos `c`, que ahora tiene la pantalla de búsqueda dibujada en él.

Hay varias funciones comunes, como `Canvas()` y `xy_random()`, que siempre están disponibles. Ver:

- %link:manual/python/common%

Las variables experimentales son variables globales. Por eso puede referirse a `set_size`, que se define en *block_loop*, aunque la variable `set_size` nunca se define explícitamente en el script. Lo mismo es cierto para `target_shape`, `target_color`, `condition`, etc. Ver:

- %link:var%

__Implementar el nivel intermedio__

Ahora vamos un paso más abajo definiendo `draw_target` (encima del resto del script hasta ahora):

~~~ .python
def draw_target(c, x, y):
    """Dibuja el objetivo.

    Parámetros
    ----------
    c: Canvas
    x: int
    y: int
    """
    draw_shape(c, x, y, color=target_color, shape=target_shape)
~~~

¿Qué ocurre aquí? Nosotros …

- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma que deben dibujarse. Esto supone que hay una función `draw_shape()`, aunque aún no la hayamos definido.

También definimos `draw_distractor` (encima del resto del script hasta ahora):

~~~ .python
def draw_distractor(c, x, y):
    """Dibuja un único distractor.

    Parámetros
    ----------
    c: Canvas
    x: int
    y: int
    """
    if condition == 'conjunction':
        draw_conjunction_distractor(c, x, y)
    elif condition == 'feature_shape':
        draw_feature_shape_distractor(c, x, y)
    elif condition == 'feature_color':
        draw_feature_color_distractor(c, x, y)
    else:
        raise Exception(f'Condición no válida: {condition}')
~~~

¿Qué ocurre aquí? Nosotros …

- Llamamos a otra función para dibujar un distractor más específico según la Condición.
- Verificamos si `condition` tiene alguno de los valores esperados. Si no, generamos una `Exception`. ¡Esto es programación defensiva! Sin esta verificación, si cometemos un error tipográfico en algún lugar, el distractor podría simplemente no mostrarse sin generar un mensaje de error.

Ahora definimos la función que dibuja distractores en la condición de Conjunction (encima del resto del script hasta ahora):

~~~ .python
import random

def draw_conjunction_distractor(c, x, y):
    """Dibuja un solo distractor en la condición de conjunción: un objeto que
    puede tener cualquier forma y color, pero no puede ser idéntico al objetivo.

    Parámetros
    ----------
    c: Canvas
    x: int
    y: int
    """
    conjunciones = [('amarillo', 'círculo'),
                    ('azul',   'círculo'),
                    ('amarillo', 'cuadrado'),
                    ('azul',   'cuadrado')]
    conjunciones.remove((target_color, target_shape))
    color, forma = random.choice(conjunciones)
    draw_shape(c, x, y, color=color, shape=forma)
~~~

¿Qué sucede aquí? Nosotros …

- Definimos una lista, `conjunciones`, de todas las posibles combinaciones de color y forma.
- Eliminamos el objetivo de esta lista; esto es necesario, porque el distractor no puede ser idéntico al objetivo.
- Elegimos aleatoriamente una de las combinaciones de color y forma de `conjunciones`.
- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma del distractor que se va a dibujar. Esto supone que existe una función `draw_shape()`, aunque aún no la hemos definido.

Además, nosotros …

- Añadimos la línea `import random` al comienzo del script. Esto es necesario para que podamos usar funciones que forman parte del módulo `random`, como `random.choice()`.

Ahora definimos la función que dibuja distractores en la condición Shape Feature (justo debajo de la declaración `import`):

~~~ .python
def draw_feature_shape_distractor(c, x, y):
    """Dibuja un solo distractor en la condición de característica de forma: un objeto que
    tiene una forma diferente a la del objetivo, pero puede tener cualquier color.

    Parámetros
    ----------
    c: Canvas
    x: int
    y: int
    """
    colores = ['amarillo', 'azul']
    color = random.choice(colores)
    if target_shape == 'circle':
        forma = 'cuadrado'
    elif target_shape == 'square':
        forma = 'círculo'
    else:
        raise Exception(f'Forma de objetivo no válida: {target_shape}')
    draw_shape(c, x, y, color=color, shape=forma)
~~~

¿Qué sucede aquí? Nosotros …

- Elegimos aleatoriamente un color.
- Elegimos una forma cuadrada si el objetivo es un círculo, y una forma circular si el objetivo es un cuadrado.
- Si `target_shape` no es ni 'circle' ni 'square', lanzamos una `Exception` - ¡más programación defensiva!
- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma del distractor que se va a dibujar. Esto supone que existe una función `draw_shape()`, aunque aún no la hemos definido.

Ahora definimos la función que dibuja distractores en la condición Color Feature (justo debajo de la declaración `import`):

~~~ .python
def draw_feature_color_distractor(c, x, y):
    """Dibuja un solo distractor en la condición de característica de color: un objeto que
    tiene un color diferente al del objetivo, pero puede tener cualquier forma.

    Parámetros
    ----------
    c: Canvas
    x: int
    y: int
    """
    formas = ['círculo', 'cuadrado']
    forma = random.choice(formas)
    if target_color == 'amarillo':
        color = 'azul'
    elif target_color == 'azul':
        color = 'amarillo'
    else:
        raise Exception(f'Color de objetivo no válido: {target_color}')
    draw_shape(c, x, y, color=color, shape=forma)
~~~

¿Qué sucede aquí? Nosotros …

- Elegimos aleatoriamente una forma.
- Elegimos un color azul si el objetivo es amarillo, y un color amarillo si el objetivo es azul.
- Si `target_color` no es ni 'amarillo' ni 'azul', lanzamos una `Exception` - ¡más programación defensiva!
- Llamamos a otra función, `draw_shape()`, y especificamos el color y la forma del distractor que se va a dibujar. Esto supone que existe una función `draw_shape()`, aunque aún no la hemos definido.

__Implementar el nivel detallado__

Ahora vamos hasta el fondo de los detalles definiendo la función que realmente dibuja una forma en el lienzo (justo debajo de la declaración `import`):

~~~ .python
def draw_shape(c, x, y, color, forma):
    """Dibuja una forma individual.

Parámetros
    ----------
    c: Canvas
    x: int
    y: int
    color: str
    shape: str
    """
    if shape == 'cuadrado':
        c += Rect(x=x-25, y=y-25, w=50, h=50, color=color, fill=True)
    elif shape == 'círculo':
        c += Circle(x=x, y=y, r=25, color=color, fill=True)
    else:
        raise Exception(f'Forma no válida: {shape}')
    if color not in ['amarillo', 'azul']:
        raise Exception(f'Color no válido: {color}')
~~~

¿Qué sucede aquí? Nosotros...

- Verificamos qué forma se debe dibujar. Para los cuadrados, añadimos un elemento `Rect()` al lienzo. Para los círculos, añadimos un elemento `Circle()`.
- Revisamos si la forma es un cuadrado o un círculo y, de no ser así, mostramos una `Exception`. ¡Este es otro ejemplo de programación defensiva! Nos aseguramos de no haber especificado accidentalmente una forma no válida.
- Revisamos si el color no es ni amarillo ni azul y, de no ser así, mostramos una `Exception`.

__Implementar la fase Run__

Debido a que hemos realizado todo el trabajo difícil en la fase Prepare, la fase Run es simplemente:

~~~ .python
c.show()
~~~

¡Eso es todo! Ahora has dibujado una pantalla completa de búsqueda visual. Y, lo que es más importante, lo has hecho de una manera fácil de entender, gracias a la programación de arriba hacia abajo, y segura, debido a la programación defensiva.

## Paso 7: Definir la respuesta correcta

Para saber si el participante responde correctamente, necesitamos conocer la respuesta correcta. Puedes definir esto explícitamente en el *block_loop* (como se hace en el tutorial para principiantes); pero aquí vamos a utilizar un simple script de Python que verifica si el objetivo está presente o no, y define la respuesta correcta en consecuencia.

Para hacer esto, inserta un nuevo INLINE_SCRIPT al comienzo de *trial_sequence* y cambia su nombre a *correct_response_script*. En la fase Prepare (¡no en la fase Run!), ingresa el siguiente código:

~~~ .python
if target_present == 'present':
    correct_response = 'derecha'
elif target_present == 'ausente':
    correct_response = 'izquierda'
else:
    raise Exception(f'target_present debería ser ausente o presente, no {target}')
~~~

¿Qué sucede aquí? Nosotros...

- Verificamos si el objetivo está presente o no. Si el objetivo está presente, la respuesta correcta es 'derecha' (tecla de flecha derecha); si el objetivo está ausente, la respuesta correcta es 'izquierda' (tecla de flecha izquierda). La variable experimental (global) `correct_response` es automáticamente reconocida por *keyboard_response*; por lo tanto, no necesitamos indicar explícitamente que esta variable contiene la respuesta correcta.
- Comprobamos si el objetivo está presente o ausente y, de no ser así, mostramos una `Exception` — otro ejemplo de programación defensiva.

## Paso 8: Proporcionar retroalimentación por ensayo

La retroalimentación después de cada ensayo puede motivar a los participantes; sin embargo, la retroalimentación por ensayo no debe interferir con el flujo del experimento. Una buena manera de dar retroalimentación por ensayo es mostrar brevemente un punto de fijación verde después de una respuesta correcta y un punto de fijación rojo después de una respuesta incorrecta.

Para hacer esto:

- Inserta dos nuevos SKETCHPADs en *trial_sequence*, justo después de *keyboard_response*.
- Cambia el nombre de un SKETCHPAD a *green_dot*, dibuja un punto de fijación verde central en él y cambia su duración a 500.
- Cambia el nombre del otro SKETCHPAD a *red_dot*, dibuja un punto de fijación rojo central en él y cambia su duración a 500.

Por supuesto, solo uno de los dos puntos debe mostrarse en cada ensayo. Para lograr esto, especificaremos expresiones run-if en *trial_sequence*:

- Cambia la expresión run-if para *green_dot* a 'correct == 1', indicando que solo se debe mostrar después de una respuesta correcta.
- Cambia la expresión run-if para *red_dot* a 'correct == 0', indicando que solo se debe mostrar después de una respuesta incorrecta.

La variable `correct` se crea automáticamente si la variable `correct_response` está disponible; por eso definimos `correct_response` en el paso 7. Para obtener más información sobre variables y declaraciones run-if, consulta:

- %link:manual/variables%

El *trial_sequence* ahora debería verse como %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  La *secuencia_de_prueba* al final del paso 8.
--%

## ¡Terminado!

¡Felicitaciones, el experimento está completo! Puedes probarlo presionando el botón de flecha doble azul (atajo: `Ctrl+W`).

Si el experimento no funciona en el primer intento: No te preocupes y averigua con calma de dónde proviene el error. Los fallos son parte del proceso normal de desarrollo. Pero puedes ahorrarte mucho tiempo y dolores de cabeza trabajando de manera estructurada, como lo hemos hecho en este tutorial.

## Referencias

<div class='reference' markdown='1'>

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un creador de experimentos abierto y gráfico para las ciencias sociales. *Métodos de investigación en comportamiento*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Treisman, A. M., & Gelade, G. (1980). Una teoría de integración de características de atención. *Psicología cognitiva*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5

</div>

[referencias]: #references
[gpl]: http://www.gnu.org/licenses/gpl-3.0.en.html