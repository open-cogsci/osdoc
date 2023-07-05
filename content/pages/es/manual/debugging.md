title: Depuración
hash: 183510524112a0f1a17d60669acd2273f06aa15f0b358eb9d3fdaac1002810c0
locale: es
language: Spanish

Al diseñar un nuevo experimento, inevitablemente te encontrarás con bugs. Los bugs pueden manifestarse como fallos acompañados de mensajes de error, o como comportamientos inesperados sin ningún mensaje de error explícito.

La depuración, el arte y la habilidad de diagnosticar y rectificar estos errores y comportamientos inesperados, es una parte crítica del proceso de diseño experimental.

[TOC]


## Depuración en la interfaz de usuario

### Usando el inspector de variables

El Inspector de Variables en OpenSesame proporciona una visión general de todas las variables que están actualmente activas dentro de tu experimento. Esto incluye:

- Variables definidas explícitamente en la interfaz de usuario, normalmente en un ítem LOOP.
- Variables de respuesta, que son establecidas por varios ítems de respuesta como un ítem KEYBOARD_RESPONSE.
- Variables que se definen usando ítems INLINE_SCRIPT Python.

Cuando un experimento está en ejecución, el Inspector de Variables se actualiza dinámicamente, proporcionando una visión en tiempo real de las variables y sus valores. Esta función te permite monitorizar el comportamiento de tu experimento en tiempo real, ayudándote a identificar posibles problemas o bugs.

Por ejemplo, considera una situación en la que has definido una variable `left_letter` para definir qué letra debe aparecer en el lado izquierdo de un SKETCHPAD. Sin embargo, durante la ejecución, notas un desajuste en el Inspector de Variables: `left_letter` está siendo mostrada en realidad en el lado derecho de tu pantalla. Esto indica un bug en el que has colocado mal las letras derecha e izquierda en el SKETCHPAD.

%--
figure:
 id: FigVariableInspector
 source: variable-inspector.png
 caption: Puedes usar el inspector de variables para verificar si tu experimento se comporta como debería. En este ejemplo, hay un bug en el que la letra que se define a través de la variable `left_letter` aparece en realidad a la derecha y viceversa.
--%

Usar regularmente el Inspector de Variables para monitorizar las variables ayuda a asegurar que tu experimento se comporta como se esperaba y ayuda a identificar problemas desde el principio.


### Imprisión de mensajes de depuración en la consola IPython/ Jupyter

La función Python `print()` es una herramienta de depuración simple pero poderosa cuando se usa dentro de los ítems INLINE_SCRIPT, y sirve para un propósito similar al del Inspector de Variables. Por ejemplo, puedes imprimir los valores de las variables `left_letter` y `right_letter` durante la fase Prepare de un INLINE_SCRIPT al principio de cada prueba.

Para ver estos mensajes de depuración, abre la consola Jupyter/ IPython y monitoriza la salida mientras se ejecuta el experimento. De este modo, puedes verificar si la salida que se muestra en la consola se alinea con el comportamiento real del experimento.

%--
figure:
 id: FigPrintingOutput
 source: printing-output.png
 caption: La función Python `print()` puede ser utilizada para emitir mensajes de depuración a la consola.
--%

En el ejemplo anterior, se hace evidente que la letra asignada a la variable `left_letter` (que se espera aparezca a la izquierda) está apareciendo realmente a la derecha, y viceversa.


### Interpretando mensajes de error de la interfaz de usuario

Cuando un bug en tu experimento provoca un fallo, OpenSesame muestra un mensaje de error, también conocido como 'Excepción'. Un mensaje de error normalmente consta de los siguientes componentes:

- **Tipo de error:** Indica la clase general de error. En el ejemplo a continuación, este es un `FStringError`.
- **Descripción:** Proporciona una explicación más específica de lo que desencadenó el error. En este caso, 'No se pudo evaluar ...'.
- **Fuente:** Especifica el elemento que desencadenó el error y si ocurrió durante las fases de Ejecución o Preparación.  
- **Rastreo:** Un detallado mensaje de error de Python. Esta información solo se muestra si el error ocurrió al evaluar el código Python personalizado, que incluye elementos de INSTRUCCIÓN EN LÍNEA, pero también expresiones condicionales (por ejemplo, expresiones si-se-ejecutará), y texto con referencias de variables incorporadas.
- **Aprende más sobre este error:** Un botón interactivo en el que puedes hacer clic para obtener información más detallada sobre el mensaje de error.

Veamos un ejemplo para entender mejor estos componentes y aprender cómo corregir un error común:

%--
figure:
 id: FigFStringError
 source: fstring-error.png
 caption: An `FStringError` indicates an issue when trying to evaluate a text string containing a Python expression.
--%

Este es un `FStringError`, lo que significa que hubo un problema al interpretar una cadena de texto que incluye una expresión de Python. En este ejemplo, el texto problemático es `{right_leter}`. Todo lo que se incluye entre llaves es interpretado como una expresión de Python, y por lo tanto en este caso la expresión de Python es `right_leter`, que es simplemente un nombre de variable. Tratar de evaluar la expresión de Python `right_leter` desencadenó un `NameError` porque `right_leter` no está definida.

Eso es bastante técnico, ¿pero qué fue exactamente lo que salió mal aquí en términos simples? El problema surge al referirse a una variable inexistente: `right_leter`. Mirando el nombre de la variable, parece probable que haya un error tipográfico: la variable pretendida seguramente es `right_letter`, con una doble 't'.

¿Dónde deberíamos corregir este error? El mensaje de error indica que la fuente del error es un elemento llamado *target*, que es un SKETCHPAD. Para resolver el error, necesitamos abrir *target* y cambiar el texto de '{right_leter}' a '{right_letter}'.


### Interpretando mensajes de error de Python

En Python, los errores se dividen en dos categorías: errores de sintaxis y excepciones (o errores en tiempo de ejecución).


#### Errores de sintaxis de Python

Un error de sintaxis ocurre cuando el intérprete de Python no puede analizar el código porque viola las reglas de sintaxis de Python. Esto podría ser debido a paréntesis desparejados, comas faltantes, indentación incorrecta, y así sucesivamente. En OpenSesame, esto resulta en un `PythonSyntaxError`.

%--
figure:
 id: FigPythonSyntaxError
 source: python-syntax-error.png
 caption: A `PythonSyntaxError` is triggered when the code violates Python's syntax rules and cannot be parsed.
--%

El mensaje de error de arriba indica que ha ocurrido un error de sintaxis en la línea 16 de la fase de Preparación de un elemento llamado *constants*. Aquí está la línea problemática:

```python
target_orientations = [('z', 0), ('/', 90]
```

El mensaje también insinúa que los paréntesis desparejados podrían ser la fuente potencial del error. Teniendo eso en cuenta, podemos solucionar el problema añadiendo una paréntesis que falta `)` antes del corchete de cierre `]`:

```python
target_orientations = [('z', 0), ('/', 90)]
```


#### Excepciones de Python

Cuando el código de Python es sintácticamente correcto pero encuentra un problema durante su ejecución, se levanta una excepción. En OpenSesame, tales excepciones resultan en un `PythonError`.

%--
figure:
 id: FigPythonError
 source: python-error.png
 caption: A `PythonError` is triggered when an exception is raised during the execution of syntactically correct Python code.
--%

El mensaje de error de arriba indica que se ha levantado un `NameError` en la línea 2 de la fase de Ejecución de un elemento llamado *trial_script*. Específicamente, el identificador 'clock_sleep' no es reconocido. Mirando la línea que causó el error, es evidente que hemos usado un guion bajo (`_`) en lugar de un punto (`.`), implicando incorrectamente que `clock_sleep()` es una función.

```python
clock_sleep(495)
```

Para solucionar esto, deberíamos referenciar correctamente la función `sleep()` como parte del objeto `clock`:

```python
clock.sleep(495)
```

## Depuración en un navegador web (OSWeb)

### Imprimir salida en la consola del navegador

La función JavaScript `console.log()` es una herramienta de depuración sencilla y poderosa cuando se usa dentro de los elementos INLINE_JAVASCRIPT. Cumple una función similar a la función Python `print()` y al Inspector de Variables, ninguno de los cuales están disponibles en OSWeb. Por ejemplo, puedes imprimir los valores de las variables `left_letter` y `right_letter` durante la fase de preparación de un INLINE_SCRIPT al inicio de cada prueba.

Para ver estos mensajes de depuración, necesitas abrir la consola del navegador. Aquí te explicamos cómo hacerlo en Chrome, Firefox y Edge:

- **Google Chrome:** Presiona Ctrl + Shift + J (Windows / Linux) o Cmd + Option + J (Mac).
- **Mozilla Firefox:** Presiona Ctrl + Shift + K (Windows / Linux) o Cmd + Option + K (Mac).
- **Microsoft Edge:** Presiona F12 para abrir las herramientas de desarrollador, luego selecciona la pestaña "Consola".

Una vez que la consola está abierta, puedes monitorear la salida mientras ejecutas el experimento, lo que te permite comprobar si la salida mostrada en la consola se alinea con el comportamiento real del experimento.

%--
figure:
 id: FigPrintingOutputOSWeb
 source: printing-output-osweb.png
 caption: La función JavaScript `console.log()` se puede utilizar para imprimir mensajes de depuración en la consola del navegador.
--%

En el ejemplo anterior, se hace evidente que la letra asignada a la variable `left_letter` (que debería aparecer a la izquierda) en realidad aparece a la derecha, y viceversa.

### Entendiendo los mensajes de error

Cuando tu experimento basado en navegador se bloquea, OSWeb mostrará un mensaje de error en el navegador. Un mensaje de error normalmente consta de los siguientes componentes:

- **Tipo de error:** Indica la clase general de error. En el ejemplo a continuación, este es un `ReferenceError`.
- **Descripción:** Proporciona una explicación más específica de lo que desencadenó el error. En este caso, 'right_leter no está definido'.
- **Origen:** Especifica el elemento que desencadenó el error y si ocurrió durante la fase de ejecución o preparación.
- **Script de origen:** El código JavaScript que causó el error. Esta información solo se muestra si el error ocurrió mientras se evaluaba JavaScript personalizado, que incluye elementos INLINE_JAVASCRIPT, pero también expresiones condicionales (por ejemplo, expresiones de ejecución si), y texto con referencias de variable incrustadas.

Vamos a ver un ejemplo para entender mejor estos componentes y aprender cómo corregir un error común:

%--
figure:
 id: FigOSWebError
 source: osweb-error.png
 caption: Un `ReferenceError` indica una referencia a una variable inexistente u otro objeto inexistente.
--%

Esto es un `ReferenceError`, que indica que el experimento se refiere a una variable inexistente u otro objeto inexistente. En este ejemplo, el error proviene del texto `${right_leter}`. Algo encerrado entre llaves y precedido por un `$` se interpreta como una expresión de JavaScript, y en este caso, la expresión JavaScript es `right_leter`, que simplemente es un nombre de variable. Intentar evaluar la expresión de JavaScript `right_leter` desencadenó un `ReferenceError` porque `right_leter` no está definido.

Eso es bastante técnico, pero ¿qué salió exactamente mal aquí en términos simples? El problema surge al referirse a una variable inexistente: `right_leter`. Observando el nombre de la variable, parece probable que exista un error tipográfico: la variable intencionada probablemente sea `right_letter`, con una doble 't'.

¿Dónde deberíamos corregir este error? El mensaje de error indica que la fuente del error es un elemento llamado *target*, que es un SKETCHPAD. Para resolver el error, necesitamos abrir *target* y cambiar el texto de '{right_leter}' a '{right_letter}'.

### Usar la declaración `debugger` en los elementos INLINE_JAVASCRIPT

La declaración `debugger` de JavaScript es una herramienta poderosa para depurar elementos `INLINE_JAVASCRIPT` en experimentos de OpenSesame/OSWeb. Te permite insertar puntos de interrupción en tu código, provocando que la ejecución de JavaScript del navegador se detenga en ese punto. Esto te permite inspeccionar el estado actual del espacio de trabajo de JavaScript.

Usar la declaración `debugger` es sencillo. Simplemente inserta la declaración `debugger` en la línea donde quieras pausar la ejecución. Por ejemplo:

```javascript
console.log(`left_letter = ${left_letter}`)
console.log(`right_letter = ${right_letter}`)
debugger // La ejecución se pausará aquí
```

Una vez que hayas insertado la declaración `debugger` en tu código, necesitas abrir la consola del navegador como se explicó anteriormente. Después de abrir la consola del navegador, ejecuta tu experimento. Cuando el intérprete de JavaScript llegue a la declaración `debugger`, pausará la ejecución y las herramientas del desarrollador cambiarán a la pestaña "Sources" (Chrome/Edge) o "Debugger" (Firefox), resaltando la línea de interrupción.

%--
figure:
 id: FigJavaScriptDebugger
 source: javascript-debugger.png
 caption: When the JavaScript interpreter reaches the `debugger` statement, it will pause execution and allow you to inspect the JavaScript workspace. The `debugger` statement only works when the browser console is open.
--%

Mientras la ejecución está en pausa, puedes inspeccionar los valores de las variables, avanzar a través del código línea por línea e investigar la pila de llamadas para comprender mejor el estado de tu programa en el punto de interrupción.

Recuerda eliminar o comentar las declaraciones `debugger` cuando hayas terminado de depurar, ya que dejarlas puede interferir con la operación normal de tu experimento.

## Manejo de errores de ExperimentProcessDied 

De vez en cuando, podrías encontrarte con un error de `ExperimentProcessDied` durante un experimento.

%--
figure:
 id: FigExperimentProcessDied
 source: experiment-process-died.png
 caption: El error `ExperimentProcessDied` generalmente indica un problema con el proceso de Python subyacente o las bibliotecas asociadas, no con el código de tu experimento.
--%

Este error implica que el proceso de Python en el que se estaba ejecutando el experimento terminó inesperadamente. Por lo general, no indica un error en tu experimento, sino que sugiere un problema en alguna de las bibliotecas de bajo nivel utilizadas por OpenSesame, o incluso un error en Python mismo.

Determinar la causa exacta de este error puede ser desafiante y solucionarlo puede ser aún más difícil. Sin embargo, hay algunas soluciones alternativas que puedes probar para mitigar el problema:

- **Cambiar el backend:** Selecciona un backend diferente en 'Run Experiment' en las propiedades del experimento. Esto podría resolver el problema ya que los diferentes backends utilizan diferentes conjuntos de bibliotecas de bajo nivel.
- **Actualizar OpenSesame y paquetes relevantes:** La actualización regular de OpenSesame y todos los paquetes asociados puede potencialmente resolver este problema, ya que los errores se solucionan rutinariamente en las nuevas versiones.