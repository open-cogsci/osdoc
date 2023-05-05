title: Script de OpenSesame
reviewed: false
hash: 73e219615747fe9d3e0d6444db9859ce306004221b08c7ff0f63e555f160cfa2
locale: es
language: Spanish

[TOC]

## Acerca del guion de OpenSesame

El guion de OpenSesame es un lenguaje definicional simple que define un experimento. No es un lenguaje de programación completo y no incluye características como bucles `for`. El guion de OpenSesame es interpretado por un entorno de tiempo de ejecución de OpenSesame.

El guion de OpenSesame es diferente de los scripts de Python que se utilizan en los elementos de inline_script. Python es un lenguaje de programación real con toda la flexibilidad y complejidades que esto implica. En contraste, el guion de OpenSesame se utiliza para definir experimentos de una manera simple y fácil de leer.

## Observaciones generales

### Palabras clave

Algunos elementos, como form_base y sketchpad aceptan palabras clave. Las palabras clave son de la forma `palabra_clave=valor`. Las palabras clave son opcionales y deben regresar a un valor predeterminado.

### Comentarios

Las cadenas precedidas por un símbolo de almohadilla deben interpretarse como comentarios.

*Ejemplo*

	# Esto es un comentario

### Citación

No es necesario citar, excepto en las cadenas que contienen espacios u otras formas de puntuación. Por lo tanto, las siguientes líneas deben interpretarse como idénticas:

	set my_var 'my_value'
	set my_var "my_value"
	set my_var my_value

Sin embargo, las siguientes líneas no lo son. De hecho, la primera línea no es válida porque tiene un tercer parámetro inesperado.

	set my_var my value
	set my_var "my value"

### Tipos

No hay tipos. No se hace distinción entre cadenas, enteros, etc.

### Sintaxis específica del elemento

Algunos elementos tienen una sintaxis específica. Esto se indica en la sección "Applies to" para cada una de las palabras clave mencionadas a continuación.

### Solución de nombres de ruta

TODO

## Declaración *define*

Empieza la definición de un elemento. Después de una declaración define, todas las líneas se sangran con un tabulador único. El fin de la definición del elemento es la primera cadena que ya no está sangrada. No se permiten declaraciones de definición anidadas.

*Applies to*

Todos los elementos

*Formato*

	define [nombre del elemento] [tipo de elemento]
		[definición del elemento]

*Parámetros*

|`nombre del elemento`	|el nombre del elemento	|
|`tipo de elemento`	|el tipo del elemento	|

*Ejemplo*

	define get_key keyboard_response
		set allowed_responses "a;x"
		set description "Recolección de respuestas de teclado"
		set timeout "infinite"
		set flush "yes"

## Declaración *draw*

Define un elemento visual de un elemento sketchpad o feedback.

*Applies to*

sketchpad, feedback

*Formato*

El formato depende del elemento.

	draw ellipse [left] [top] [width] [height] [keywords]
	draw circle [x] [y] [radius] [keywords]
	draw line [left] [right] [top] [bottom] [keywords]
	draw arrow [left] [right] [top] [bottom] [keywords]
	draw textline [x] [y] [text]
	draw image [x] [y] [path]
	draw gabor [x] [y]
	draw noise [x] [y]
	draw fixdot [x] [y]

*Parámetros*

|`left` 		|la coordenada x más a la izquierda	|
|`right`		|la coordenada x más a la derecha	|
|`top`			|la coordenada y superior			|
|`bottom`		|la coordenada y inferior			|
|`x` 			|la coordenada x					|
|`y`			|la coordenada y					|
|`text` 		|cadena de texto					|
|`path` 		|la ruta hacia un archivo de imagen	|

*Keywords*

TODO

*Ejemplo*

	draw fixdot 0 0

## Declaración *log*

Indica que una variable debe escribirse en el archivo de registro.

*Applies to*

logger

*Formato*

	log [nombre de la variable]

*Parámetros*

|`nombre de la variable`		|el nombre de una variable	|

*Ejemplo*

	log response_time

## Declaración *run*

Indica que se debe ejecutar un elemento. En el caso de la secuencia, el orden de las declaraciones de ejecución determina el orden en que se llaman a los elementos. En el caso del complemento de coroutines, todos los elementos se llaman al mismo tiempo.

*Applies to*

sequence

*Formato*

	run [nombre del elemento] [opcional: condición] [opcional: deshabilitado]

*Parámetros*

|`nombre del elemento`			|el nombre del elemento a ejecutar	|
|`condición` (opcional)	|la declaración condicional, que determina si se llama al elemento. Si no se proporciona ninguna condición, el elemento siempre se llama.|

*Ejemplo*

	run correct_feedback '[correct] = 1'

## Declaración *set*

Define variables de una sola línea.

*Applies to*

Todos los elementos

*Formato*

	set [nombre de la variable] [valor]

*Parámetros*

|`nombre de variable`	|el nombre de la variable	|
|`valor`			|el valor de la variable	|

*Ejemplo*

	set timeout 1000

*Notas*

Las variables de varias líneas se definen utilizando la notación `__[nombre de variable]__`. Esto es útil principalmente para los elementos que requieren grandes bloques de texto. Dentro de la definición de un elemento, cada línea va precedida de un tabulador único, que no debe interpretarse como parte del texto. `__end__` indica el final de la variable.

*Por ejemplo:*

	__mi_variable__
	Esta es la primera línea.
	Esta es la segunda línea.
	__end__

## *sentencia setcycle*

Similar a la declaración "set" regular, pero establece una variable solo durante un ciclo específico de un bucle. Esto es el equivalente de script a la tabla de bucle.

*Aplicable a*

Loop

*Formato*

	setcycle [ciclo #] [nombre de variable] [valor de variable]

*Parámetros*

|`Ciclo #`			|el número del ciclo, donde 0 es el primero	|
|`nombre de variable` 	|el nombre de la variable							|
|`valor`			|el valor de la variable							|

*Ejemplo*

	setcycle 0 cue valid

## *sentencia widget*

Agrega un widget (botones, etiquetas, etc.) a un formulario. Las palabras clave válidas dependen del tipo de widget. La declaración del widget no es estrictamente parte de la sintaxis básica de OpenSesame, sino que es utilizada por el complemento form_base.

*Aplicable a*

form_base (complemento)

*Formato*

	widget [columna] [fila] [extensión de columna] [extensión de fila] [tipo de widget] [palabras clave]

*Parámetros*

|`columna`		|la posición de columna del widget en el formulario, donde 0 es el más a la izquierda								|
|`fila`			|la posición de fila del widget en el formulario, donde 0 es la parte superior										|
|`extensión de columna`	|el número de columnas que ocupa el widget												|
|`extensión de fila`		|el número de filas que ocupa el widget												|
|`tipo de widget`	|'button', 'checkbox', 'image', 'image_button', 'label', 'rating_scale' o 'text_input'	|

*Palabras clave*

TODO

*Ejemplo*

	widget 0 0 1 1 label text='Esta es una etiqueta'