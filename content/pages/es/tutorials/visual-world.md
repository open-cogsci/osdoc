title: Mundo visual
uptodate: false
hash: e4143940b8a35c6b31fa932649f55f5627564c01e4b0f042c0beede079fb612c
locale: es
language: Spanish

[TOC]

## Acerca de este tutorial

Este tutorial asume un conocimiento básico de OpenSesame y, para algunas partes, Python. Por lo tanto, si no estás familiarizado con OpenSesame o Python, te recomiendo que revises los tutoriales para principiantes e intermedios antes de continuar con este tutorial:

- %link:beginner%
- %link:intermediate%

En este tutorial, aprenderás lo siguiente:

- Seguimiento ocular con PyGaze
- Hacer cosas en paralelo con `coroutines`
- Uso de operaciones avanzadas de `loop`


## Acerca del experimento

En este tutorial, implementaremos un *paradigma del mundo visual*, que fue introducido por Cooper (1974; para una revisión, vea también Huettig, Rommers y Meyer, 2011). En este paradigma, los participantes escuchan una oración hablada mientras miran una pantalla con varios objetos. Usaremos cuatro objetos separados presentados en los cuatro cuadrantes de la pantalla (%FigParadigm).

%--
figure:
 id: FigParadigm
 source: visual-world-paradigm.svg
 caption: >
  Un esquema de nuestra secuencia de prueba. Este es un ejemplo de una prueba de coincidencia completa, porque el objeto objetivo (la manzana) se menciona directamente en la oración hablada. Estímulos tomados de los estímulos de [BOSS](https://sites.google.com/site/bosstimuli/) (Brodier et al., 2010).
--%

La oración hablada se refiere a uno o más de los objetos. Por ejemplo, se puede mostrar una manzana (el objeto objetivo) mientras se reproduce la oración hablada "en el desayuno, la niña comió una manzana". En este caso, el objetivo coincide completamente con la oración. La oración también puede referirse indirectamente a un objeto mostrado. Por ejemplo, se puede mostrar una manzana (de nuevo el objeto objetivo) mientras se reproduce la oración hablada "en el desayuno, la niña comió un plátano". En este caso, el objetivo coincide semánticamente con la oración, porque un plátano y una manzana son ambas frutas que una niña puede comer en el desayuno.

Durante el experimento, se registra la posición de los ojos y se mide la proporción de fijaciones en objetos objetivo y no objetivo a lo largo del tiempo. El hallazgo típico es entonces que los ojos se sienten atraídos hacia los objetos objetivo; es decir, los participantes miran principalmente los objetos que se mencionan directa o indirectamente en la oración hablada. Y cuanto más directa sea la referencia, más fuerte será este efecto.

Ahora hagamos esto más formal. Nuestro experimento tendrá el siguiente diseño:

- Un factor (Coincidencia de objetivo) con dos niveles (Completo o Semántico), variado entre sujetos. En la condición de coincidencia completa, el objeto objetivo se menciona directamente en la oración. En la condición de coincidencia semántica, el objeto objetivo está relacionado semánticamente con un objeto que se menciona en la oración.
- Tenemos 16 oraciones habladas y dieciséis objetos objetivo. Cada oración y cada objeto objetivo se muestra dos veces: una vez en la condición de coincidencia completa y otra en la condición de coincidencia semántica.
- Tenemos 16 × 3 = 48 objetos distractores, cada uno de los cuales (como los objetivos) se muestra dos veces.
- Cada prueba comienza con un punto de fijación durante 1 s, seguido de la presentación de los estímulos, seguido 1 s después del inicio de la oración hablada. La prueba termina 5 s después.


## El tutorial


### Paso 1: Descargar e iniciar OpenSesame

OpenSesame está disponible para Windows, Linux, Mac OS (experimental) y Android (solo tiempo de ejecución). Este tutorial está escrito para OpenSesame 3.2.X *Kafkaesque Koffka*. Para poder utilizar PyGaze, debes descargar la versión de Python 2.7 (que es la predeterminada). Puedes descargar OpenSesame desde aquí:

- %link:download%

(Si inicias OpenSesame por primera vez, verás una pestaña de bienvenida. Descarta esta pestaña). Al iniciar OpenSesame, se te dará la opción de experimentos con plantillas y, si corresponde, una lista de experimentos abiertos recientemente (ver %FigStartUp). Haz clic en 'Plantilla predeterminada' para comenzar con un experimento casi vacío.

%--
figure:
 id: FigStartUp
 source: start-up.png
 caption: |
  La ventana de OpenSesame en el inicio.
--%


### Paso 2: Construir la estructura principal del experimento

Por ahora, construye la siguiente estructura principal para tu experimento (ver también %FigMainStructure):

1. Comenzamos con una pantalla de instrucciones. Esto será un `sketchpad`.
2. Luego, ejecutamos un bloque de pruebas. Esto será una única `secuencia`, correspondiente a una sola prueba, dentro de un único `bucle`, correspondiente a un bloque de pruebas. ¡Puedes dejar vacía la secuencia de pruebas por ahora!
3. Finalmente, terminamos con una pantalla de despedida.

También necesitamos cambiar el color del primer plano del experimento a negro y el color del fondo a blanco. Esto se debe a que usaremos imágenes que tienen un fondo blanco, ¡y no queremos que estas imágenes resalten!

¡Y no olvides darle a tu experimento un nombre lógico, y guardarlo!


%--
figura:
 id: FigMainStructure
 fuente: main-structure.png
 leyenda: |
  La estructura principal del experimento.
--%


### Paso 3: Importar archivos al depósito de archivos

Para este experimento necesitamos estímulos: archivos de sonido para las frases habladas e imágenes para los objetos. Descarga estos archivos del siguiente enlace, extrae el archivo `zip` y coloca los estímulos en el depósito de archivos de tu experimento (ver también %FigFilePool).

- %static:attachments/visual-world/stimuli.zip%

%--
figura:
 id: FigFilePool
 fuente: file-pool.png
 leyenda: |
  El depósito de archivos de tu experimento después de agregar todos los estímulos.
--%


### Paso 4: Definir las variables experimentales en el block_loop

El *block_loop* es donde definimos las variables experimentales, ingresándolas en una tabla, donde cada fila corresponde a una prueba y cada columna corresponde a una variable experimental.

Por ahora, solo definimos la condición de coincidencia completa, en la que el objeto objetivo se menciona directamente en la oración hablada. (Agregaremos la condición de coincidencia semántica como parte de las Tareas adicionales).

Necesitamos las siguientes variables. Primero, simplemente añade columnas a la tabla del bucle, sin dar contenido a las filas.

- `pic1` — el nombre de la primera imagen (por ejemplo, 'apple.jpg')
- `pic2` — el nombre de la segunda imagen
- `pic3` — el nombre de la tercera imagen
- `pic4` — el nombre de la cuarta imagen
- `pos1` — la posición de la primera imagen (por ejemplo, 'arriba a la izquierda')
- `pos2` — la posición de la primera imagen
- `pos3` — la posición de la primera imagen
- `pos4` — la posición de la primera imagen
- `sound` — el nombre de un archivo de sonido que contiene una frase hablada (por ejemplo, 'apple.ogg').

El objeto objetivo siempre corresponderá a `pic1`. Tenemos los siguientes objetos objetivo; es decir, para los siguientes objetos, tenemos archivos de sonido que se refieren a ellos. Simplemente copia y pega la siguiente lista en la columna `pic1` de la tabla:

~~~
apple.jpg
armchair.jpg
banana.jpg
bear.jpg
card.jpg
cello.jpg
chicken.jpg
cookie.jpg
croissant.jpg
dice.jpg
egg.jpg
guitar.jpg
keyboard.jpg
mouse.jpg
sofa.jpg
wolf.jpg
~~~

Y haz lo mismo con los archivos de sonido:

~~~
apple.ogg
armchair.ogg
banana.ogg
bear.ogg
card.ogg
cello.ogg
chicken.ogg
cookie.ogg
croissant.ogg
dice.ogg
egg.ogg
guitar.ogg
keyboard.ogg
mouse.ogg
sofa.ogg
wolf.ogg
~~~

El resto de las imágenes son distracciones. Copia y pega la siguiente lista en las columnas `pic2`, `pic3` y `pic4`, de tal manera que cada columna tenga exactamente 16 filas. (Si accidentalmente haces que la tabla sea más larga de 16 filas, simplemente selecciona las filas excesivas, haz clic derecho y elimínalas).

~~~
basketball01.jpg
basketballhoop02.jpg
bathtub.jpg
battery02b.jpg
battleaxe.jpg
battleship.jpg
beachpaddle01a.jpg
belt03b.jpg
estanteria.jpg
tapondefrasco.jpg
cuenco01.jpg
guanteboxeo02a.jpg
camioncaja.jpg
pulsera01.jpg
modelocerebro.jpg
ladrillo.jpg
excavadora.jpg
cochechoque.jpg
busto.jpg
boton01.jpg
cactus.jpg
calculadora01.jpg
calendario.jpg
camara01b.jpg
cd.jpg
ventiladortecho02.jpg
telefono.jpg
guante04.jpg
monumento.jpg
luna.jpg
lanchamotora02.jpg
botellaaceitemotor03b.jpg
mrpotatocabeza.jpg
cortauñas03b.jpg
pinzadepuntafina03a.jpg
mesitanoche.jpg
nintendods.jpg
senalprohibidoaparcar.jpg
horno.jpg
chupete02a.jpg
bote_pintura01.jpg
pantalones.jpg
avionpapel.jpg
clipdepapel02.jpg
fuente_parque.jpg
sombrillaterraza.jpg
sacapuntas03b.jpg
molinodepimienta01a.jpg
~~~

Ahora necesitamos especificar las posiciones. Simplemente establezca:

- `pos1` en 'arribaizquierda'
- `pos2` en 'arribaderecha'
- `pos3` en 'abajoizquierda'
- `pos4` en 'abajoderecha'

Tu tabla de bucle ahora debería verse como %FigLoopTable.

%--
figure:
 id: FigLoopTable
 source: loop-table.png
 caption: |
  La tabla de `loop` después de que se han definido todas las variables experimentales.
--%


### Paso 5: Aplicar operaciones avanzadas de loop

Aunque ya has definido todas las variables experimentales, ¡la tabla de `loop` aún no está terminada! Veamos qué está mal:


__Posiciones__

`pos1` es siempre la parte superior izquierda, lo que significa que `pic1` (el objeto objetivo) siempre se presenta en la parte superior izquierda del visualizador. (Suponiendo que implementaremos nuestra secuencia de ensayos de tal manera que estas posiciones se utilicen de esa manera). Y lo mismo ocurre con `pos2`, `pos3` y `pos4`.

Podemos solucionar esto mezclando horizontalmente las columnas de `pos[x]`. Es decir, para cada fila, intercambiamos aleatoriamente los valores de estas filas, de modo que esto:

~~~
pos1        pos2         pos3        pos4
arribaizquierda     arribaderecha     abajoizquierda  abajoderecha
arribaizquierda     arribaderecha     abajoizquierda  abajoderecha
…
~~~

Se convierte (por ejemplo) en esto:

~~~
pos1        pos2         pos3        pos4
abajoizquierda  arribaizquierda      arribaderecha    abajoderecha
arribaderecha    abajoderecha  arribaderecha    abajoizquierda
…
~~~

Para hacer esto, vea el script de *block_loop* y agregue la siguiente línea de código al final del script:

~~~
shuffle_horiz pos1 pos2 pos3 pos4
~~~

Y haga clic en 'Aplicar y cerrar'. Si ahora hace clic en 'Vista previa', obtendrá una vista previa de cómo podría verse su tabla de bucle si el experimento se ejecutara realmente. ¡Y verá que las columnas de `pos[x]` están mezcladas horizontalmente, lo que significa que las imágenes se mostrarán en posiciones aleatorias!


__Distractores__

Las imágenes distractores siempre están vinculadas al mismo objeto objetivo. Por ejemplo, 'basketball01.jpg' siempre aparece junto con el objetivo 'apple.jpg'. ¡Pero esto no es lo que queremos! Más bien, queremos que el emparejamiento entre distractores y objetivos sea aleatorio y diferente para todos los participantes. (Excepto si por casualidad se produce un emparejamiento idéntico para dos participantes).

Podemos solucionar esto mezclando verticalmente las columnas `pic2`, `pic3` y `pic4`. Es decir, el orden de cada una de estas columnas se debe mezclar independiente. Para hacer esto, vea el script nuevamente y agregue las siguientes líneas al final del script:

~~~
shuffle pic2
shuffle pic3
shuffle pic4
~~~

Y haga clic en 'Aplicar y cerrar'. Si hace clic en 'Vista previa', verá que la tabla de `loop` está debidamente aleatorizada.

Para obtener más información sobre operaciones avanzadas de loop, consulte:

- %link:manual/structure/loop%


<div class='info-box' markdown='1'>

__Pregunta__

En este punto, puede que se pregunte por qué no también necesitamos mezclar horizontalmente las columnas `pic2`, `pic3` y `pic4`. ¡Pero no lo necesitamos! ¿Sabes por qué no?

</div>


### Paso 6: Crear la secuencia de prueba

Como se muestra en %FigParadigm, nuestra secuencia de prueba es simple y consta de:

- punto de fijación central (un `sketchpad`)
- Después de 1000 ms: visualización de estímulo (otro `sketchpad`)
- Después de 1000 ms: iniciar la reproducción del sonido (un `sampler`) mientras la pantalla de estímulo permanece en pantalla
- Después de 5000 ms: fin del ensayo

Por ahora, la secuencia del ensayo es puramente secuencial y podríamos implementarla usando solo una `sequence`, como hemos hecho en otros tutoriales. Sin embargo, como una de las tareas extra, queremos analizar la posición del ojo *durante* la secuencia de prueba; en otras palabras, más adelante querremos hacer dos cosas en paralelo, por lo que necesitamos un elemento `coroutines`. (Incluso si, por ahora, no haremos nada que lo requiera.)

Entonces, queremos tener la siguiente estructura:

- *trial_sequence* debe contener un elemento `coroutines` (llamémoslo *trial_coroutines*) seguido de un elemento `logger`.
- *trial_coroutines* debe tener una duración de 7000 ms y contener tres elementos:
  - Un `sketchpad` para el punto de fijación (llamémoslo *fixation_dot*) que se muestra después de 0 ms
  - Un `sketchpad` para el estímulo en pantalla (llamémoslo *objects*) que se muestra después de 1000 ms
  - Un `sampler` para el sonido (llamémoslo *spoken_sentence*) que se muestra después de 2000 ms

La estructura de tu experimento ahora debería verse como en %FigCoroutinesStructure.

%--
figure:
 id: FigCoroutinesStructure
 source: coroutines-structure.png
 caption: |
  La estructura del experimento después de definir la secuencia de prueba.
--%

### Paso 7: Define los estímulos visuales

__fixation_dot__

El *fixation_dot* se define fácilmente: simplemente dibuja un punto de fijación central en él.

Ten en cuenta que no es necesario especificar la duración del `sketchpad`, como normalmente deberías hacerlo; esto se debe a que el elemento es parte de *trial_coroutines* y el tiempo se especifica mediante el tiempo de inicio y finalización indicados allí.

__objects__

Para definir los *objects*, primero crea un prototipo de visualización, un ejemplo de cómo podría verse una pantalla en un ensayo en particular. Más específicamente, dibuja un punto de fijación central y dibuja imágenes arbitrarias en cada uno de los cuatro cuadrantes, como se muestra en %FigObjectsPrototype.

También asigna un nombre a cada uno de los cuatro objetos: `pic1`, `pic2`, `pic3` y `pic4`. Utilizaremos estos nombres en las tareas adicionales para realizar un análisis de regiones de interés (ROI).

%--
figure:
 id: FigObjectsPrototype
 source: objects-prototype.png
 caption: |
  Una pantalla de prototipo con un objeto arbitrario en cada uno de los cuatro cuadrantes.
--%


Por supuesto, no queremos mostrar los mismos objetos una y otra vez. Más bien, queremos que las variables `pic[x]` especifiquen qué objetos se muestran, y las variables `pos[x]` especifiquen dónde se muestran estos objetos. Comencemos con el primer objeto: el objeto en la parte superior izquierda, que en mi ejemplo es una manzana.

Ve al script y encuentra la línea que corresponde al primer objeto. En mi ejemplo, esta es la siguiente línea:

~~~ .python
draw image center=1 file="apple.jpg" scale=1 show_if=always x=-256 y=-192 z_index=0
~~~

Ahora cambia `file="apple.jpg"` a `file=[pic1]`. Esto garantizará que se muestre la imagen objetivo según lo especificado en la variable `pic1`, en lugar de siempre la misma manzana.

Entonces, ¿cómo podemos usar `pos1`, que tiene valores como 'topleft', 'bottomright', etc., para especificar las coordenadas X e Y de la imagen? Para hacerlo, hacemos uso del hecho de que podemos incluir expresiones de Python en el script de OpenSesame, utilizando la notación `[=python_expression]`:

- Cambia `x=-256` a `x="[=-256 if 'left' in var.pos1 else 256]"`
- Cambia `y=-192` a `y="[=-192 if 'top' in var.pos1 else 192]"`

Y haz lo mismo con las otras imágenes, hasta que el script se vea así:

~~~ .python
draw fixdot color=black show_if=support style=default x=0 y=0 z_index=0
draw image center=1 file="[pic1]" scale=1 show_if=siempre x="[=-256 si 'left' en var.pos1 else 256]" y="[=-192 si 'top' en var.pos1 else 192]" z_index=0
draw image center=1 file="[pic2]" scale=1 show_if=siempre x="[=-256 si 'left' en var.pos2 else 256]" y="[=-192 si 'top' en var.pos2 else 192]" z_index=0
draw image center=1 file="[pic3]" scale=1 show_if=siempre x="[=-256 si 'left' en var.pos3 else 256]" y="[=-192 si 'top' en var.pos3 else 192]" z_index=0
draw image center=1 file="[pic4]" scale=1 show_if=siempre x="[=-256 si 'left' en var.pos4 else 256]" y="[=-192 si 'top' en var.pos4 else 192]" z_index=0
~~~

<div class='info-box' markdown='1'>

__Pruébalo tú mismo: la expresión `if`__

Si no estás familiarizado con la expresión `if` de Python, que es un poco diferente de la declaración tradicional `if`, abre la ventana de depuración e ingresa la siguiente línea:

~~~ .python
print('Esto se muestra si es Verdadero' if True else 'Esto se muestra si es Falso')
~~~

¿Qué ves? Ahora cambia `if True else` a `if False else` y ejecuta la línea nuevamente. ¿Qué ves ahora? ¿Entiendes la lógica?

</div>


### Paso 8: Define el sonido

Definir el sonido es fácil: simplemente abre el elemento *spoken_sentence* e ingresa '[sound]' en el cuadro 'Archivo de sonido', indicando que la variable `sound` especifica el archivo de sonido.


### Paso 9: Añadir seguimiento ocular básico

El seguimiento ocular se realiza con los complementos [PyGaze](%url:manual/eyetracking/pygaze%), que se instalan de forma predeterminada en OpenSesame. El procedimiento general es el siguiente:

- Al comienzo del experimento, el seguimiento ocular se *inicializa y calibra* con el elemento `pygaze_init`. Aquí es donde indicas qué seguidor de ojos deseas utilizar. Durante el experimento, es conveniente seleccionar el rastreador de ojos ficticio avanzado, que te permite simular movimientos oculares con el mouse.
- Antes de cada ensayo, se realiza un procedimiento de *corrección de deriva* con el elemento `pygaze_drift_correct`. Durante la corrección de deriva, se muestra un punto en la pantalla y el participante lo mira. Esto permite al seguidor de ojos ver cuánto error de deriva hay en la medición de la posición de los ojos. Cómo se trata este error depende de tu dispositivo y configuración:
  - El error de deriva se utiliza para realizar una recalibración en un solo punto
  - O se realiza una simple comprobación para ver si el error de deriva no supera un cierto error máximo, dando la posibilidad de recalibrar si se excede el error máximo.
- A continuación, aún antes de cada ensayo, se le indica al seguidor de ojos que comience a recopilar datos con el elemento `pygaze_start_recording`. Puedes especificar un mensaje de estado para indicar el inicio de cada ensayo. Es conveniente incluir un número de ensayo en este mensaje de estado (por ejemplo, 'comenzar_ensayo [count_trial_sequence]').
- Al final de cada ensayo, los datos se envían al archivo de registro del seguidor de ojos con el elemento `pygaze_log`. Es conveniente habilitar la opción 'Detectar y registrar automáticamente todas las variables'.
- Finalmente, al final de cada ensayo, se le indica al seguidor de ojos que deje de grabar con el elemento `pygaze_stop_recording`.

La estructura de tu experimento debería verse ahora como en %FigEyeTrackingStructure.

%--
figure:
 id: FigEyeTrackingStructure
 source: eye-tracking-structure.png
 caption: |
  La estructura del experimento después de agregar elementos PyGaze para el seguimiento ocular.
--%

### Paso 10: Define las instrucciones y la pantalla de despedida

Ahora tenemos un experimento en funcionamiento, pero aún no hemos agregado contenido a los elementos *instrucciones* y *goodbye*. Entonces, antes de ejecutar el experimento, abre estos elementos y agrega texto.

### Paso 11: ¡Ejecuta el experimento!

Felicidades, ¡has implementado un paradigma de mundo visual! Ahora es el momento de probar rápidamente tu experimento haciendo clic en el botón naranja de reproducción (atajo: `Ctrl+Shift+W`).


## Tareas extra

### Extra 1: Define la condición de coincidencia semántica

Hasta ahora, solo hemos implementado la condición de Coincidencia Completa, en la que el objeto objetivo (por ejemplo, 'manzana') se menciona explícitamente en la oración hablada (por ejemplo, 'en el desayuno, la niña comió una manzana').

Ahora, también implementa la condición de Coincidencia Semántica, en la que cada objetivo (por ejemplo, 'manzana') se empareja con una oración hablada semánticamente relacionada (por ejemplo, 'en el desayuno, la niña comió un plátano'). Los estímulos se han creado de tal manera que hay una oración hablada semánticamente relacionada para cada objeto objetivo.

En todos los demás aspectos, la condición de Coincidencia Semántica debe ser idéntica a la condición de Coincidencia Completa.

¡Y no olvides crear una variable que indique la condición!

### Extra 2: Usa constantes de Python para definir coordenadas

En este momento, las coordenadas de los objetos se han codificado en el guión *objects*, en el sentido de que las coordenadas se han escrito directamente en el guión:

~~~ .python
x="[=-256 if 'left' in var.pos1 else 256]"
~~~

Es más elegante definir las coordenadas (`XLEFT`, `XRIGHT`, `YTOP` y `YBOTTOM`) como constantes en un `inline_script` al principio del experimento y luego hacer referencia a estas constantes en el guión *objects*.


<div class='info-box' markdown='1'>

__Constantes en Python__

En informática, una *constante* es una variable con un valor que no puedes cambiar. En Python, siempre puedes cambiar variables, por lo que las constantes no existen en sentido estricto en el lenguaje. Sin embargo, si tienes una variable que tratas como si fuera una constante (es decir, la defines una vez y nunca cambias su valor), generalmente lo indicas escribiendo el nombre de la variable en `MAYÚSCULAS`.

Estas convenciones de nombres se describen en las pautas de estilo PEP-8 de Python:

- <https://www.python.org/dev/peps/pep-0008/>

</div>


### Extra 3: Analizar la posición del ojo en línea (desafiante)

En *trial_coroutines*, puedes indicar el nombre de una función del generador (consulte a continuación para obtener una explicación de los generadores). Ingresemos el nombre `roi_analysis` aquí y también creemos un `inline_script` al principio del experimento en el que definamos esta función.

Aquí hay una función `roi_analysis()` parcialmente implementada. ¿Puedes terminar la lista de tareas pendientes?

~~~ .python
def roi_analysis():

	# sample_nr se utilizará para crear un nombre de variable diferente para cada
	# muestra de 500 ms
	sample_nr = 0
	# Este primer rendimiento indica que el generador ha terminado de preparar
	yield
	# Recupere el lienzo del bloc de notas de bocetos de objetos. Necesitamos hacer esto después
	# la declaración de rendimiento que señala el final de la preparación, porque eso es
	# seguro de que el objeto canvas se ha construido (que también sucede)
	# durante la preparación.
	canvas = items['objects'].canvas
	while True:
		# Solo queremos analizar una muestra de mirada una vez cada 500 ms. Esto es para
		# que no terminemos con demasiadas columnas en el archivo de registro. Si no es
		# hora de analizar una muestra de mirada, simplemente rinda y continúe.
		if not clock.once_in_a_while(ms=500):
			yield # para que otros elementos en las coroutines puedan ejecutarse
			continue
		#
		# TODO:
		#
		# - Obtenga una coordenada de posición del ojo del rastreador de ojos
		#   (Sugerencia: use eyetracker.sample())
		# - Verifique qué elementos del bloc de notas de bocetos están en esta coordenada (si los hay)
		#   (Sugerencia: use canvas.elements_at())
		# - Si pic1 (el objeto objetivo) se encuentra entre estos elementos, ajuste
		#   var.on_target_[sample_nr] a 1, de lo contrario a 0
		#   (Sugerencia: use var.set())
~~~

Ver también:

- %link:manual/structure/coroutines%

<div class='info-box' markdown='1'>

__Funciones generadoras en Python__

En Python, una función *generadora* es una función con una declaración `yield`. Una declaración `yield` es similar a una declaración `return`, en que detiene una función. Sin embargo, mientras que `return` detiene una función de forma permanente, `yield` simplemente suspende una función, y la función puede reanudarse más tarde desde el punto de `yield` en adelante.

</div>

## Descarga el experimento

Puedes descargar el experimento completo desde aquí:

- <https://osf.io/z27rt/>


## Referencias

Brodeur, M. B., Dionne-Dostie, E., Montreuil, T., Lepage, M., & Op de Beeck, H. P. (2010). The Bank of Standardized Stimuli (BOSS), un nuevo conjunto de 480 fotos normativas de objetos para ser utilizados como estímulos visuales en investigaciones cognitivas. *PloS ONE*, *5*(5), e10773. doi:10.1371/journal.pone.0010773
{: .reference}

Cooper, R. M. (1974). El control de la fijación ocular por el significado del lenguaje hablado: una nueva metodología para la investigación en tiempo real de la percepción del habla, la memoria y el procesamiento del lenguaje. *Cognitive Psychology*, *6*(1), 84–107. doi:10.1016/0010-0285(74)90005-X
{: .reference}

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: una caja de herramientas de código abierto y multiplataforma para la programación de experimentos de seguimiento ocular con el mínimo esfuerzo. *Behavior Research Methods*, *46*(4), 913–921. doi:10.3758/s13428-013-0422-2
{: .reference}

Huettig, F., Rommers, J., & Meyer, A. S. (2011). Usar el paradigma del mundo visual para estudiar el procesamiento del lenguaje: una revisión y evaluación crítica. *Acta Psychologica*, *137*(2), 151–171. doi:10.1016/j.actpsy.2010.11.003
{: .reference}

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: un generador de experimentos de código abierto y gráfico para las ciencias sociales. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}