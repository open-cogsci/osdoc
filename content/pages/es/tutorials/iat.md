title: Tarea de Asociación Implícita
uptodate: false
hash: d71135886d1eab5c8ea213f440c31193dc6e9c150ad7be41af10263195d05180
locale: es
language: Spanish

## Tarea de Asociación Implícita

La tarea de asociación implícita mide la fuerza de las asociaciones entre conceptos (p. ej., personas jóvenes y personas mayores) y evaluaciones (p. ej., bueno y malo). La idea es que hacer una respuesta es más fácil (y por lo tanto *más rápido*) cuando los elementos relacionados comparten la misma tecla de respuesta.

Aquí, mediremos la asociación entre jóvenes y viejos, y bueno y malo. Hipotetizamos que los participantes jóvenes (subconscientemente) asocian palabras positivas con caras jóvenes en lugar de con caras viejas.


## Tutorial en screencast

Este tutorial también está disponible en formato screencast:

%--
video:
 source: youtube
 id: Screencast
 videoid: zd-nxgGOGlE
 width: 640
 height: 360
 caption: |
  Una screencast del tutorial de TIPI.
--%



## Jerarquía experimental

Para probar esta predicción, los participantes realizan cuatro bloques de ensayos (%Task)

- __Bloque 1__ - Los participantes clasifican *palabras* como *POSITIVAS* o *NEGATIVAS*. Los nombres de las categorías aparecen en la parte superior izquierda y superior derecha de la pantalla, y los participantes presionan un botón con su mano izquierda o derecha para indicar a qué categoría pertenece una palabra presentada centralmente.
- __Bloque 2__ - Los participantes clasifican *rostros* como *VIEJOS* o *JÓVENES*, nuevamente haciendo una respuesta con la mano izquierda o derecha.
- __Bloque 3__ - Es una combinación del bloque 1 y 2. En este ejemplo, las palabras *POSITIVO* y *JÓVEN* aparecen en la parte superior izquierda, mientras que las palabras *NEGATIVO* y *VIEJO* aparecen en la parte superior derecha. Debido a que suponemos que los participantes (jóvenes) tienen una actitud más positiva hacia las caras jóvenes, llamamos a esto mapeo *congruente*
- __Bloque 4__ - Es nuevamente una combinación del bloque 1 y 2, pero esta vez el mapeo es *incongruente*

%--
figure:
 id: Task
 source: IAT-task.png
 caption: |
  Resumen de los cuatro bloques de la tarea de asociación implícita.
--%

## Predicción

La predicción es que los participantes tienen una preferencia por las personas jóvenes en comparación con las personas mayores, de tal manera que es más fácil clasificar las palabras cuando lo joven y positivo comparten una tecla de respuesta, y lo viejo y negativo comparten una tecla de respuesta (en comparación con el mapeo inverso). Esto debería resultar en respuestas *más rápidas* en el bloque congruente que en el bloque incongruente (%Prediction).

%--
figure:
 id: Prediction
 source: prediction.png
 caption: |
  Pronosticamos que los participantes encuentran más fácil clasificar las palabras y las caras si se combinan las categorías *POSITIVO/JÓVEN* y *NEGATIVO/VIEJO* (en comparación con lo inverso).
--%


## Secuencia de ensayo

Para probar esta predicción, vamos a crear la siguiente secuencia de ensayo (%TrialSequence):

- Cada ensayo comienza con un __punto de fijación__ (500 ms)
- A continuación, aparecen los __dos nombres de categoría__ en la parte superior izquierda y derecha de la pantalla.
- El estímulo a __clasificar__ aparece en el centro
- Los participantes indican con una __pulsación de tecla__ si el estímulo pertenece a la categoría de la izquierda o de la derecha
- Las variables del ensayo actual se __registran__

%--
figure:
 id: TrialSequence
 source: trial_sequence.png
 caption: |
  Representación esquemática de una secuencia típica de ensayo del (primer bloque del) TIPI.
--%

## Iniciar OpenSesame

Cuando inicie OpenSesame, verá una pestaña de '¡Empezar!', que le muestra una lista de plantillas y experimentos recientemente abiertos (%GetStarted). Para ahorrar tiempo, utilizaremos la 'Plantilla extendida'.

%--
figure:
 id: GetStarted
 source: get-started.png
 caption: |
  Ventana de bienvenida de OpenSesame. Aquí, utilizamos la 'Plantilla extendida'.
--%

Después de abrir la plantilla extendida, guardamos nuestro experimento. Para hacerlo, haga clic en *Archivo* -> *Guardar* (atajo: `Ctrl+S`), vaya a la carpeta correspondiente y asigne un nombre significativo a su experimento.


## Área de descripción general

El *área de descripción general* muestra la estructura jerárquica de nuestro experimento. Para simplificar nuestra estructura, comenzamos eliminando el bloque de práctica. Para hacerlo:

- Haga clic derecho en el elemento llamado *practice loop*
- Haga clic en 'Eliminar' (acceso directo: `Del`)
- Haz lo mismo con el elemento *end_of_practice*

El área de descripción general de su experimento ahora debería verse así:

%--
figure:
 id: Overview
 source: overview.png
 caption: |
  El área de descripción general de tu experimento.
--%

## Bloque 1: categorización de palabras

### Paso 1: Modificar el bucle del bloque

Comenzamos creando el primer bloque del IAT (Bloque 1 en %Task) en el cual los participantes deben categorizar palabras como positivas o negativas. Como crearemos más de un bloque, el nombre *block_loop* no es tan informativo. Entonces lo renombramos:

- Haga clic derecho en el elemento *block_loop*, elija cambiar el nombre (acceso directo: `F2`) y llámelo *words_block_loop*

A continuación, queremos definir las siguientes tres variables en el *block_loop item*:

- __stimulus__ -- La palabra a categorizar
- __category__ -- La categoría a la que pertenece la palabra
- __correct_response__ -- La respuesta que se supone que deben dar los participantes

Para crear estas variables:

- Abra la pestaña del *words_block_loop* haciendo clic en ella en el área de descripción general
- Inicialmente verás una tabla vacía
- Haga doble clic en el encabezado de la primera columna (inicialmente llamada 'empty_column') y llámela 'stimulus'
- Llene la primera columna con seis palabras positivas y seis negativas, una por fila
- Cree una segunda columna con el encabezado 'category' e indique a qué categoría (*POSITIVE* o *NEGATIVE*) pertenece cada estímulo
- Cree una tercera columna, llámela *correct_response* e indique la respuesta correcta para cada estímulo
- Para determinar la regla de respuesta, digamos que:
    - La palabra *POSITIVE* aparecerá en el lado izquierdo de la pantalla, mientras que la palabra *NEGATIVE* aparecerá en el lado derecho
    - Para indicar que una palabra pertenece al lado izquierdo, los participantes deben presionar 'e', mientras que para el lado derecho, deben presionar 'i'.

<div class='info-box' markdown='1'>

__Consejo__ -- *correct_response* es una variable integrada que permite que OpenSesame realice un seguimiento del rendimiento de los participantes, como 'acc' (para precisión o porcentaje correcto).

</div>

El contenido de su *words_block_loop* debería verse algo como esto:

%--
figure:
 id: Overview
 source: words_block_loop.png
 caption: |
  La tabla de bucle del primer bloque del IAT contiene las tres variables experimentales y sus valores.
--%


### Paso 2: Modificar la secuencia de prueba

Como se muestra en %TrialSequence, en cada prueba queremos:

1. Mostrar un punto de fijación
2. Mostrar el estímulo en el centro y las dos categorías a cada lado superior de la pantalla
3. Recopilar una respuesta de tecla presionada
4. Guardar las variables en el archivo de salida

Estos cuatro pasos se llaman *eventos*, y los vamos a realizar utilizando *items* en la *secuencia de prueba*. Pero primero, debido a que la secuencia de prueba será ligeramente diferente para cada bloque del experimento (ver %Task), renombrémosla a *words_trial_sequence*.

Para los dos primeros eventos, utilizaremos eventos de `sketchpad`. La plantilla avanzada ya contiene un artículo de sketchpad. Para agregar un segundo:

- Tome un artículo `sketchpad` de la *barra de herramientas de elementos*
- Arrástrelo y suéltelo en la *words_trial_sequence*

%--
video:
 source: youtube
 id: DragDrop
 videoid: vvJewWTjlts
 width: 640
 height: 360
 caption: |
  Arrastrando y soltando elementos.
--%


<div class='info-box' markdown='1'>

__Consejo__ -- Para hacer que un elemento dado aparezca *después* de otro elemento, suéltelo *sobre* este otro elemento.

</div>



De forma predeterminada, OpenSesame asigna nombres a sus elementos como *sketchpad*, *new_sketchpad* y *new_sketchpad_1*. Debido a que estos nombres no son informativos, renombramos los elementos a algo más significativo. Para hacerlo:

- Haga clic derecho en el elemento en el área de descripción general (acceso directo: `F2`)
- Elija 'Renombrar'
- Llame respectivamente a los dos elementos `sketchpad` *fixation* y *word*

Los dos últimos eventos de la secuencia de ensayo (recopilación de la respuesta y guardado de los datos) ya están representados por el elemento `keyboard_response` y el elemento `logger`, respectivamente.

El área de descripción general ahora debería verse así:

%--
figura:
 id: OverviewWordBlock
 fuente: overview_words_block.png
 leyenda: |
  Nueva descripción general de (la primera parte de) el experimento.
--%

### Paso 3: Modificar los elementos en la secuencia de ensayo

#### Fijación

El siguiente paso es agregar contenido a los elementos en la secuencia de ensayo. Comenzamos con el `sketchpad` que representa el punto de fijación al comienzo de cada ensayo.

- Abre la pestaña *fijación* haciendo clic en ella en el área de descripción general. Debido a que elegimos la "Plantilla extendida", OpenSesame ya creó un punto de fijación para nosotros. Lo único que necesitamos cambiar es cuánto tiempo permanecerá el punto de fijación en pantalla
- Haz clic en el cuadro 'Duración' y cambia su valor a 500

#### Palabra

__Dibujar los nombres de las categorías__

Después de que desaparezca el punto de fijación, queremos mostrar los dos nombres de categoría en la parte superior izquierda y derecha de la pantalla (ver %TrialSequence). Para hacerlo,

- Abre la pestaña *palabra* haciendo clic en ella en el área de descripción general
- Selecciona el elemento `Draw textline` (Dibujar línea de texto) de la barra de herramientas en blanco y negro
- Haz clic en alguna parte del cuadrante superior izquierdo del sketchpad
- Escribe 'POSITIVO'
- Repite este procedimiento para hacer que la palabra 'NEGATIVO' aparezca en el lado opuesto

__Dibujar el estímulo__

A continuación, queremos mostrar el estímulo a ser categorizado en el centro de la pantalla. Es importante destacar que el estímulo es _*variable*_. Esto significa que la palabra que se muestra depende de qué línea del *words_block_loop* se ejecute actualmente. Para informar a OpenSesame que puede encontrar el valor de la variable de la palabra en el bucle de bloque, usamos la *sintaxis de corchetes*. Para hacerlo:

- Selecciona el elemento `draw textline` (dibujar línea de texto) del sketchpad
- Haz clic en el centro de la pantalla
- Escribe:

~~~ .python
[estímulo]
~~~

<div class='info-box' markdown='1'>

__Consejo__ -- La palabra que escribes entre corchetes debe corresponder exactamente al encabezado de columna que creaste en el *word_block_loop*.

</div>

Este método es muy conveniente, porque evita tener que hacer sketchpads separados para cada palabra positiva y negativa.

__Cambiar la duración__

Por último, cambiamos la duración del sketchpad actual a 0. Esto no significa que el sketchpad actual se mostrará solo por 0 ms. En cambio, como un elemento `keyboard_response` sigue justo después de él, permanecerá en pantalla hasta que el participante presione una tecla.

Tu sketchpad debería verse así ahora:

%--
figura:
 id: SketchpadWord
 fuente: sketchpad-word.png
 leyenda: |
  El elemento `sketchpad` que se utiliza para dibujar los nombres de categoría y el estímulo en la pantalla.
--%

Es una buena práctica intentar ejecutar tu experimento a menudo, de tal manera que puedas depurarlo de inmediato. En este punto, hagamos una prueba ejecutando una de las tres flechas de "ejecutar".

<div class='info-box' markdown='1'>

__Consejo__ -- Si deseas realizar una prueba rápida de tu experimento, es posible que no tengas que ejecutar todos los elementos de un bloque determinado. Para acortar el número de ensayos, puedes hacer lo siguiente:

- Abre la tabla de bucle de bloques
- Cambia el valor en el cuadro 'Repetir' a algo más pequeño que 1,00 (por ejemplo, 0,1)
- (En algunos sistemas, los decimales están indicados por una coma en lugar de un punto)
- En nuestro ejemplo, esto significa que OpenSesame solo ejecutará *una* fila (seleccionada al azar) en lugar de las 12
- No olvides volver a poner 'Repetir' en 1,00 cuando hayas terminado de probar

</div>


## Jerarquía experimental

El IAT contiene más bloques que el actual. También contiene un bloque en el que las imágenes de rostros deben clasificarse como jóvenes o viejos, y dos bloques que contienen ambas tareas intercaladas (ver %Task). Esto significa que tendremos que crear otros tres bloques de pruebas, cada uno con su propia secuencia de pruebas. La estructura jerárquica del experimento se ve de la siguiente manera (y cuando terminemos de programar, nuestra área de descripción general debe parecerse a esto):

%--
figure:
 id: Hierarchy
 source: hierarchy.png
 caption: |
  La jerarquía experimental del IAT.
--%

## Bloque 2: categorización de rostros

Primero, concéntrate en la tarea de categorizar rostros. Más precisamente, lo que haremos es:

- Crear un bucle de bloque adicional y una secuencia de pruebas
- Reutilizar todo lo que podamos reutilizar de la parte anterior del experimento
- Añadir nuevas variables y eventos específicos para la tarea de categorización de rostros

### Paso 4: Crear un bucle adicional block_loop

- Toma un elemento `loop` de la `item toolbar`
- Arrastra y suelta en el área de descripción general
- Para hacer que el nuevo bloque aparezca después del primero, suéltalo *sobre* el elemento `words_block_loop` (ver %AppendLoopAndSequence)
- OpenSesame te pregunta si deseas insertar el elemento actual *dentro* de `words_block_loop` o *después*. Elige este último

<div class='info-box' markdown='1'>

__Tip__ -- Si accidentalmente colocas el nuevo elemento *dentro* del bucle block loop, siempre puedes deshacerlo presionando `Ctrl+Alt+Z`).

</div>

- Asigna un nombre significativo al nuevo bucle, por ejemplo, *faces_block_loop*

### Paso 5: Añadir una nueva secuencia de pruebas

Aunque la secuencia de pruebas de la tarea de categorización de rostros tiene cierta superposición con la tarea de categorización de palabras, no son idénticas. Por lo tanto, no podemos reutilizar la secuencia de pruebas que hicimos anteriormente.

Para crear uno nuevo:

- Toma un elemento `sequence` de la item toolbar
- Suelta *en* el *faces_block_loop*
- Elige "insertar en" esta vez (ver %AppendLoopAndSequence)
- Renombra el elemento como *faces_trial_sequence*

%--
video:
 source: youtube
 id: AppendLoopAndSequence
 videoid: PVcXdAN3rjM
 width: 640
 height: 360
 caption: |
  Pasos 5 y 6: Agregar el bloque 2 y su correspondiente secuencia de prueba al experimento.
--%


### Paso 6: Elegir los estímulos de rostros


__Descarga los estímulos de rostros__

En el equivalente de rostros de la tarea, necesitamos imágenes de seis rostros jóvenes y seis viejos. Para evitar que los sesgos de género influyan en nuestros resultados, parece mejor usar un número igual de rostros masculinos y femeninos por categoría (aquí: tres).

Puedes descargar un conjunto de ejemplos de estímulos (en formato JPG) aquí:

- %static:attachments/iat/face-stimuli.zip%

En la mayoría de los navegadores web, puedes hacer clic derecho en el enlace y elegir "Guardar enlace como" o una opción similar. Después de haber descargado estos archivos (en tu carpeta Descargas, por ejemplo), puedes descomprimirlos.

__Agregar los archivos JPG al archivo pool__

- Si el archivo pool no está visible (de forma predeterminada en el lado derecho de la ventana), haz clic en el botón "Mostrar archivo pool" en la barra de herramientas principal (atajo: `Ctrl+P`).
- Haz clic en el signo de más para agregar archivos
- Navega hasta tu carpeta Descargas (o donde guardaste y descomprimiste la carpeta *face-stimuli*) y agrega los 12 archivos JPG.

El archivo pool debe verse similar a %FacesBlockLoop

### Paso 7: Contenido de la tabla de bucles

Al igual que en la parte anterior del experimento (ver Paso 1), necesitamos tres columnas para definir las variables experimentales: *stimulus*, *category* y *correct_response*. La única diferencia es que esta vez los estímulos son los archivos JPG que acabamos de agregar al archivo pool.

En cuanto a la correct_response, digamos que:

- La categoría *YOUNG* aparece en el lado izquierdo de la pantalla, mientras que la categoría *OLD* aparece en la derecha
- La regla de respuesta es la misma que antes

Crea las columnas mencionadas anteriormente y asegúrate de que tu bucle de bloque termine pareciéndose a esto:

%--
figure:
 id: FacesBlockLoop
 source: faces_block_loop.png
 caption: |
  Contenido del grupo de archivos y la tabla del bucle correspondiente al bloque 2 (categorizando rostros) del IAT.
--%

<div class='info-box' markdown='1'>

__Consejo__ - Los valores en la columna *estímulo* deben corresponder exactamente a los nombres de los archivos en los grupos de archivos. De lo contrario, OpenSesame no podrá encontrar los JPG si vamos a referenciarlos más adelante.

</div>

### Paso 8: modificar la secuencia del ensayo

En este momento, nuestra nueva secuencia de ensayo aún está vacía. Necesitamos llenarla con los siguientes eventos (consulta %TrialSequence):

1. Mostrar un punto de fijación durante 500 ms
2. Mostrar una imagen de un rostro, junto con los dos nombres de categorías (*VIEJO* y *JOVEN*)
3. Recolectar una respuesta del teclado
4. Escribir todas las variables en el archivo de salida

__Copiar elementos reutilizables__

Los eventos 1, 3 y 4 son idénticos a la parte de la palabra del experimento. Por lo tanto, podemos reutilizar los elementos correspondientes copiándolos. Para hacer esto:

- Haz clic derecho en *fijación* (como parte de la *secuencia_ensayo_palabras*) en el área de descripción general
- Elige 'copiar (vinculado)', porque queremos crear otra aparición del mismo elemento
- Haz clic derecho en *secuencia_ensayo_rostros* (es decir, la nueva secuencia)
- Elige 'Pegar'
- Elige 'Insertar en...'
- Repite este procedimiento para los elementos *respuesta_teclado* y *registrador* (consulta %LinkedCopies)


<div class='info-box' markdown='1'>

__Consejo__ - Si el orden de los elementos en la secuencia está desordenado, puedes corregirlo arrastrando y soltando.

__Consejo__ - Si accidentalmente soltaste una copia en otro lugar del área de descripción general (es decir, fuera de la secuencia del ensayo a la que apuntabas), siempre puedes deshacer esto presionando `Ctrl+Alt+Z`

</div>


%--
video:
 source: youtube
 id: LinkedCopies
 videoid: _vDGpPsSqIY
 width: 640
 height: 360
 caption: |
  Usando copias vinculadas.
--%

### Paso 9: crear la visualización del rostro

Finalmente, necesitamos crear un nuevo elemento `sketchpad` para mostrar los estímulos faciales. Para hacerlo:

- Toma un elemento `sketchpad` del área de descripción general
- Colócalo en la *secuencia_ensayo_rostros*
- Asegúrate de que aparezca justo después del punto de fijación
- Cambia el nombre del elemento a *rostro*

En este momento, tu área de descripción general debe parecerse a esto:


%--
figure:
 id: OverviewBlock1-2.png
 source: overview-area-with-face-block.png
 caption: |
  Área de descripción general después de haber agregado todos los elementos a la *secuencia_ensayo_rostros*.
--%

### Paso 10: configurar el contenido del sketchpad de rostro

__Dibujar los nombres de las categorías__

- Como antes, muestre las dos categorías (aquí: *JOVEN* en la parte superior izquierda y *VIEJO* en la parte superior derecha del cuadrante) utilizando el elemento `Draw textline`
- Ajusta la duración del sketchpad a 0 ms

__Mostrar el estímulo facial__

A continuación, queremos mostrar una imagen de un rostro en el centro de la pantalla. Como antes, el estímulo es *variable*, de modo que qué rostro se muestra depende de la fila en el bucle de bloque que se está ejecutando actualmente. Por lo tanto, utilizaremos la `sintaxis de corchetes` nuevamente. Pero primero:

- Selecciona el elemento 'Draw image' del sketchpad
- Haz clic en el centro
- Selecciona uno de los archivos jpg

Luego, queremos hacer que el archivo jpg sea variable en lugar de estático. Para hacer esto, debemos hacer un pequeño ajuste en el *script* del elemento sketchpad:

- Haz clic en el botón 'Seleccionar vista' en la parte superior derecha de la pestaña *rostro* y selecciona 'Ver script'. Ahora verás el script que corresponde al sketchpad que acabamos de crear:

~~~ .python
set duration 0
set description "Displays stimuli"
draw image center=1 file="of1.jpg" scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text="JOVEN<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text=VIEJO x=320 y=-192 z_index=0
~~~


- Lo único que tenemos que hacer es reemplazar la cadena 'of1.jpg' con `[stimulus]`. Esto significa que OpenSesame usa la variable `[stimulus]` (que contiene todos los nombres de JPG) para determinar qué imagen debe mostrarse.

~~~ .python
set duration 0
set description "Muestra estímulos"
draw image center=1 file=[stimulus] scale=1 show_if=always x=0 y=0 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text="JOVEN<br />" x=-320 y=-192 z_index=0
draw textline center=1 color=white font_bold=no font_family=mono font_italic=no font_size=30 html=yes show_if=always text=VIEJO x=320 y=-192 z_index=0
~~~

- Haz clic en "apply and close"

A continuación, es hora de probar si tu experimento funciona hasta este punto.

## Los bloques mixtos

### Asignación congruente

El tercer bloque es una mezcla de los bloques 1 y 2, de tal manera que los participantes tienen que categorizar tanto palabras como caras. La asignación es *congruente*, de tal manera que las palabras *POSITIVAS* y las caras *JÓVENES* requieren una respuesta con la mano izquierda, mientras que las palabras *NEGATIVAS* y las caras *VIEJAS* requieren una respuesta con la mano derecha (ver %Task).

### Paso 11: Crear un tercer bucle de bloques y secuencia de ensayos

Para crear el tercer bloque del IAT, necesitamos:

- Crear un nuevo bucle de bloques (y cambiarle el nombre a *congruent_block_loop*) (cf. Paso 4)
- Crear una nueva secuencia de ensayos (dentro del nuevo bucle de bloques) y llamarla *congruent_trial_sequence* (cf. Paso 5).

Tu vista general del experimento debería verse así (%OverviewWithCongruent):

%--
figure:
 id: OverviewWithCongruent
 source: overview_with_congruent_loop.png
 caption: |
  Vista general del experimento después de haber insertado un tercer bucle de bloques y secuencia de ensayos.
--%

### Paso 12: Rellenar el *congruent_block_loop*

El contenido del bucle de bloques congruentes es muy similar al bucle de bloques de palabras y caras, excepto que ahora contiene ambos tipos de estímulos. Por lo tanto:

- Copia y pega el contenido del *word_block_loop* en el congruent_block_loop. Esto ocupará las filas del 1 al 12
- Haz lo mismo con el contenido del *faces_block_loop*. Esto ocupará las filas del 13 al 24
- (Asegúrate de no copiar los encabezados de las columnas dos veces)

### Paso 13: Rellenar el *congruent_trial_sequence*

- Como en el paso 8, copia los elementos *fixation*, *keyboard_response* y *logger* en la nueva secuencia de ensayos
- Desafortunadamente, no podemos utilizar copias del *word* sketchpad y *face* sketchpad porque queremos mostrar *ambas* categorías (es decir, POSITIVO vs NEGATIVO y JÓVENES vs VIEJAS) en el lado izquierdo y derecho de la pantalla
- Por lo tanto, agregamos un nuevo elemento de `sketchpad` a la congruent_trial_sequence y lo llamamos *congruent_stimulus*
- Asegúrate de que el nuevo sketchpad aparezca justo después del punto de fijación y antes del `keyboard_response item`

Tu vista general del experimento debería verse así (%OverviewWithCongruent):

%--
figure:
 id: OverviewWithCongruent
 source: overview_congruent_filled_in.png
 caption: |
  Vista general del experimento después de haber llenado la secuencia de ensayos del bloque congruente.
--%

### Paso 14: Ajustar el contenido del *congruent_sketchpad*

Abre la pestaña del *congruent_stimulus* sketchpad y cambia su duración a 0 en lugar de 'keypress'.

__Nombres de categoría__

- Asegúrate de que ambos nombres de categoría aparezcan en la parte superior izquierda y derecha de la pantalla (ver %Task). Utiliza la siguiente asignación:
    - Los nombres de las categorías *POSITIVE* y *YOUNG* aparecen en el lado izquierdo
    - *NEGATIVE* y *OLD* aparecen en el lado derecho

__Estímulos de palabras__

Dibuja el estímulo de la palabra en el centro de la pantalla de la misma manera que lo hicimos para el bloque 1 (ver Paso 3). Utiliza la `square-bracket syntax`.

__Estímulos de caras__

Dibuja el estímulo de la cara en el centro de la pantalla de la misma manera que lo hicimos para el bloque 2 (ver Paso 9).

<div class='info-box' markdown='1'>

__Consejo__ -- No te preocupes si tu sketchpad se ve desordenado. Nos ocuparemos de eso en breve.

</div>


## Paso 15: Usando declaraciones Show-if

En la parte mixta del experimento, queremos que OpenSesame determine si debe mostrar una cara o una palabra. Podemos hacer esto utilizando *Declaraciones Show-if*. Más precisamente, queremos que el stimulus_sketchpad:

- Muestre una palabra *solo* cuando el estímulo sea una palabra (es decir, cuando la celda actual en la columna del estímulo en el bucle de bloques sea una palabra)
- Muestre una cara *solo* cuando el estímulo sea una cara

Para lograr esto:

- Agrega una columna al *congruent_block_loop* y llámala *stimulus_type*
- Dale a las celdas el valor 'word' o 'face', según el estímulo (ver %CongrLoop)

%--
figure:
 id: CongrLoop
 source: congruent_block_loop.png
 caption: |
  Contenido del bucle de bloques de la parte congruente del experimento.
--%

A continuación, para hacer que el contenido del sketchpad *dependa* de los valores en la columna recién creada:

- Selecciona la flecha negra en la barra de herramientas de elementos del sketchpad
- Haz clic en el signo de interrogación (que indica el `Draw image element` que se encarga de la presentación de los archivos JPG)
- Haz clic en la casilla `Show if` que pertenece a este elemento, que por defecto está configurado como 'always'
- Usa la sintaxis de corchetes para indicar que esta parte del sketchpad solo debe dibujarse si el ensayo actual contiene una imagen de rostro escribiendo:

~~~ .python
[stimulus_type] = face
~~~

%--
video:
 source: youtube
 id: RunIf
 videoid: jqGFefCmn1k
 width: 640
 height: 360
 caption: |
  Usar una declaración Run-if en un elemento de `sketchpad`.
--%



- Haz lo mismo para el `Draw text element` que controla la presentación de las palabras escritas. Esta vez, la declaración Show-if debe ser

~~~ .python
[stimulus_type] = word
~~~

Prueba si los tres primeros bloques de tu experimento funcionan como se desea.

## Mapeo incongruente

## Paso 16: Crear el bloque incongruente del experimento

### Tarea

Utiliza lo que aprendiste en los pasos anteriores para construir la parte final e incongruente del experimento.

Algunos consejos:

- Dale nombres significativos a los nuevos elementos (por ejemplo, los nuevos elementos `loop` y `sequence`), como *incongruent_block_loop* y *incongruent_trial_sequence*
- Copia los elementos que son idénticos para cada bloque (es decir, el punto de fijación, la keyboard_response y el logger)
- No puedes copiar el sketchpad de estímulo, porque se debe intercambiar el mapeo de las categorías (que aparecen en la parte superior izquierda y derecha), de tal manera que:
    - El lado izquierdo muestre *POSITIVE* y *OLD*
    - El lado derecho muestre *NEGATIVE* y *YOUNG* (ver %Task)
- Los valores en la columna *correct_response* deben cambiarse en consecuencia


<div class='info-box' markdown='1'>

__Consejo__ Puedes usar una copia *desvinculada* del sketchpad *congruent_stimulus* para crear el sketchpad *incongruent_stimulus* (que es casi idéntico excepto que los nombres de las categorías *OLD* y *YOUNG* están intercambiados).

A diferencia de una copia *vinculada*, una copia *desvinculada* se verá inicialmente idéntica (excepto por su nombre), pero puedes editar el original sin afectar la copia desvinculada y viceversa.

</div>


## Tareas adicionales:

### Fácil: agregar una pantalla de instrucciones y despedida

- Los elementos `sketchpad` y `form_text_display` pueden presentar texto
- Las instrucciones buenas son cortas y concretas

### Intermedio: proporcionar retroalimentación en cada ensayo

- Utiliza la variable integrada *correct* que tiene
    - el valor 1 si el participante respondió correctamente
    - el valor 0 si el participante cometió un error
- Una forma fácil de proporcionar retroalimentación es presentar brevemente un punto rojo después de una respuesta incorrecta y un punto verde después de una respuesta correcta
- Utiliza declaraciones Show-if