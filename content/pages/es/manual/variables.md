title: Variables
hash: 87f8069d56f529c53b29b95555f8d096d7d742f9b355ff6689a0d6e7cb2b8654
locale: es
language: Spanish

[TOC]

## ¿Qué es una variable experimental en OpenSesame?

Las variables experimentales en OpenSesame son aquellas variables que:

- Puede referenciar en la interfaz de usuario con la sintaxis '{variable_name}'.
- Están disponibles como variables globales en un INLINE_SCRIPT de Python.
- Están disponibles como variables globales en un INLINE_JAVASCRIPT de JavaScript.
- Contienen cosas como:
	- Las variables que ha definido en un elemento LOOP.
	- Las respuestas que ha recopilado.
	- Varias propiedades del experimento.
	- Etc.

## El inspector de variables

El inspector de variables (`Ctrl+I`) proporciona una visión general de las variables disponibles (%FigVariableInspector). Cuando el experimento no está en ejecución, esta visión general se basa en una suposición de qué variables estarán disponibles durante el experimento. Sin embargo, cuando el experimento está en ejecución, el inspector de variables muestra una visión general en vivo de las variables y sus valores. Esto es útil para depurar su experimento.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: El inspector de variables proporciona una visión general de todas las variables que OpenSesame conoce.
--%

## Definiendo variables

La forma más sencilla de definir una variable es a través del elemento LOOP. Por ejemplo, %FigLoop muestra cómo definir una variable llamada `gaze_cue`. En este ejemplo, el elemento *trial_sequence* se llama cuatro veces mientras `gaze_cue` es 'left' y otras cuatro veces mientras 'gaze_cue' es 'right'.

%--
figure:
 id: FigLoop
 source: defining-variables-in-a-loop.png
 caption: La forma más común de definir variables independientes es utilizando la tabla LOOP.
--%

## Variables incorporadas

Las siguientes variables siempre están disponibles:

### Variables del experimento

|Nombre de variable      |Descripción|
|-----------------------|-----------|
|`title`                |El título del experimento|
|`description`          |La descripción del experimento|
|`foreground`           |El color de primer plano predeterminado. Ej., 'white' o '#FFFFFF'.|
|`background`           |El color de fondo predeterminado. Ej., 'black' o '#000000'.|
|`height`               |La parte de la altura de la resolución de pantalla. Ej., '768'|
|`width`                |La parte del ancho de la resolución de pantalla. Ej., '1024'|
|`subject_nr`           |El número del sujeto, que se pregunta cuando se inicia el experimento.|
|`subject_parity`       |Es 'odd' si `subject_nr` es impar y 'even' si `subject_nr` es par. Útil para el contrapeso.|
|`experiment_path`      |La carpeta del experimento actual, sin el nombre de archivo del experimento en sí. Si el experimento no se ha guardado, tiene el valor `None`.|
|`pool_folder`          |La carpeta donde se han extraído los contenidos del grupo de archivos. Generalmente es una carpeta temporal.|
|`logfile`              |La ruta al archivo de registro.|

### Variables del elemento

También hay variables que hacen un seguimiento de todos los elementos del experimento.

|Nombre de variable      |Descripción|
|-----------------------|-----------|
|`time_[item_name]`     |Contiene una marca de tiempo de cuándo se ejecutó el elemento por última vez. Para los elementos SKETCHPAD, esto se puede utilizar para verificar la sincronización de la presentación en pantalla.|
|`count_[item_name]`    |Es igual al número de veces menos uno (comenzando en 0, en otras palabras) que se ha llamado a un elemento. Esto puede, por ejemplo, usarse como un contador de ensayos o bloques.|

### Variables de respuesta

Cuando usa elementos estándar de respuesta, como KEYBOARD_RESPONSE y MOUSE_RESPONSE, se establece un número de variables según la respuesta del participante.

|Nombre de variable					|Descripción|
|-------------------------------|-----------|
|`response`						|Contiene la última respuesta que se ha dado.|
|`response_[nombre_de_elemento]`			|Contiene la última respuesta para un elemento de respuesta específico. Esto es útil en caso de que haya varios elementos de respuesta.|
|`response_time`				|Contiene el intervalo en milisegundos entre el inicio del intervalo de respuesta y la última respuesta.|
|`response_time_[nombre_de_elemento]`	|Contiene el tiempo de respuesta para un elemento de respuesta específico.|
|`correct`						|Se establece en '1' si la última `response` coincide con la variable `correct_response`, '0' si no, y 'undefined' si no se ha establecido la variable `correct_response`.|
|`correct_[nombre_de_elemento]`			|Como `correct` pero para un elemento de respuesta específico.|

### Variables de retroalimentación

Las variables de retroalimentación mantienen un promedio en curso de la precisión y los tiempos de respuesta.

|Nombre de variable					|Descripción|
|-------------------------------|-----------|
|`average_response_time`		|El tiempo de respuesta promedio. Esta variable es útil para presentar retroalimentación al participante.|
|`avg_rt`						|Sinónimo para `average_response_time`|
|`accuracy`						|El porcentaje promedio de respuestas correctas. Esta variable es útil para presentar retroalimentación al participante.|
|`acc`							|Sinónimo para `accuracy`|


## Uso de variables en la interfaz de usuario

Dondequiera que vea un valor en la interfaz de usuario, puede reemplazar ese valor por una variable utilizando la notación '{nombre_de_variable}'. Por ejemplo, si ha definido una variable `soa` en un elemento LOOP, puede usar esta variable para la duración de un sketchpad como se muestra en %FigSketchpad.

%--
figure:
 id: FigSketchpad
 source: variable-duration.png
 caption: La duración '{soa}' indica que la duración del SKETCHPAD depende de la variable `soa`.
--%

Esto funciona en toda la interfaz de usuario. Por ejemplo, si ha definido una variable `my_freq`, puede usar esta variable como la frecuencia en un elemento SYNTH, como se muestra en %FigSynth.

%--
figure:
 id: FigSynth
 source: variable-frequency.png
 caption: La frecuencia '{my_freq}' indica que la frecuencia del SYNTH depende de la variable `my_freq`.
--%

A veces, la interfaz de usuario no le permite escribir texto arbitrario. Por ejemplo, los elementos de un SKETCHPAD se muestran visualmente, y no puede cambiar directamente una coordenada X a una variable. Sin embargo, puede hacer clic en el botón *Seleccionar vista → Ver script* en la parte superior derecha y editar el script directamente.

Por ejemplo, puede cambiar la posición de un punto de fijación desde el centro:

```text
draw fixdot x=0 y=0
```

... a una posición definida por las variables `xpos` e `ypos`:

```text
draw fixdot x={xpos} y={ypos}
```

## Uso de expresiones Python en la interfaz de usuario

Al referirse a las variables usando la notación `{my_var}`, de hecho está utilizando una [f-string](https://peps.python.org/pep-0498/), que es una forma de incrustar código Python en cadenas de texto. También puede usar f-strings para evaluar código Python arbitrario. Por ejemplo, puede multiplicar las variables `width` y `height` e incluir el resultado en un SKETCHPAD, como se muestra a continuación:

%--
figure:
 id: FigFString
 source: fstrings.png
 caption: Puede incrustar expresiones Python usando f-strings.
--%

Las f-strings son código Python y, por lo tanto, solo se admiten en el escritorio, pero vea a continuación una alternativa de JavaScript para experimentos en navegador.


## Uso de expresiones JavaScript en la interfaz de usuario

Cuando se utiliza OSWeb, las expresiones incluidas entre llaves se interpretan como [literales de plantilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). Esto es muy similar a las f-strings en Python, con la diferencia importante de que utiliza JavaScript.

En JavaScript normal, las expresiones dentro de literales de plantilla están precedidas por un `$`, así: `${expression}`. Esto está permitido en OpenSesame pero no es necesario: el prefijo se añade automáticamente para mejorar la compatibilidad entre experimentos de navegador y de escritorio. En la mayoría de los casos, como en la figura a continuación, la misma expresión exacta es válida como una cadena f en Python en el escritorio y un literal de plantilla en JavaScript en el navegador.

%--
figure:
 id: FigTempalteLiteral
 source: template-literals.png
 caption: Puedes incrustar expresiones de JavaScript usando literales de plantilla.
--%


## Usar variables en Python

En un INLINE_SCRIPT, las variables experimentales están disponibles como variables globales. Por ejemplo, si ha definido `example_variable` en un LOOP, lo siguiente imprimirá el valor `example_variable` en la ventana de depuración:

~~~ .python
print(example_variable)
~~~

Puede establecer la variable experimental `example_variable` al valor 'some value' de la siguiente manera:

~~~ .python
example_variable = 'some value'
~~~


## Usar variables en JavaScript

En un INLINE_JAVASCRIPT, las variables experimentales están disponibles como variables globales. Por ejemplo, si ha definido `example_variable` en un LOOP, lo siguiente imprimirá el valor `example_variable` en la consola del navegador:

```js
console.log(example_variable)
```

Puede establecer la variable experimental `example_variable` al valor 'some value' de la siguiente manera:

```js
example_variable = 'some value'
```


## Usar declaraciones condicionales ("if")

Las declaraciones condicionales, o 'declaraciones if', proporcionan una forma de indicar que algo debe ocurrir solo bajo circunstancias específicas, como cuando alguna variable tiene un valor específico. Las declaraciones condicionales son expresiones regulares de Python.

La declaración if más utilizada en OpenSesame es la declaración run-if de SEQUENCE, que permite especificar las condiciones bajo las cuales se ejecuta un elemento en particular. Si abre un elemento SEQUENCE, verá que cada elemento de la secuencia tiene una opción 'Ejecutar si …'. El valor predeterminado es 'always', lo que significa que el elemento siempre se ejecuta; pero también puede ingresar una condición aquí. Por ejemplo, si desea mostrar un punto de fijación verde después de una respuesta correcta y un punto de fijación rojo después de una respuesta incorrecta, puede crear una SEQUENCE como la siguiente (esto hace uso del hecho de que un elemento KEYBOARD_RESPONSE automáticamente establece la variable `correct`), como se muestra en %FigRunIf.

*Importante:* Las declaraciones Run-if solo se aplican a la fase Run de los elementos. La fase Prepare siempre se ejecuta. Consulte también [esta página](%link:prepare-run%).

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: |
  'Run if' se pueden usar para indicar que ciertos elementos de una SEQUENCE solo deben ejecutarse bajo circunstancias específicas.
--%

Puede usar condiciones más complejas también. Veamos algunos ejemplos:

```python
correct == 1 and response_time > 2000
correct != 1 or response_time > max_response_time or response_time < min_response_time
```

El mismo principio se aplica a los campos 'Show if' en los elementos SKETCHPAD. Por ejemplo, si desea dibujar una flecha hacia arriba y hacia la derecha solo si la variable `quadrant` se ha establecido en 'upper right', simplemente escriba la condición adecuada en el campo 'Show if ...' y dibuje la flecha, como en %FigShowIf. Asegúrese de dibujar la flecha después de haber establecido la condición.

%--
figure:
 id: FigShowIf
 source: show-if.png
 caption: "'Show if' se pueden usar para indicar que ciertos elementos de un artículo SKETCHPAD o FEEDBACK solo deben mostrarse bajo circunstancias específicas."
--%

Importante: El momento en el que se evalúa una declaración condicional puede afectar cómo funciona su experimento. Esto está relacionado con la estrategia de preparación-ejecución empleada por OpenSesame, que se explica aquí:

- %link:prepare-run%