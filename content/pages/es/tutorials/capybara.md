title: Gatos, perros y capibaras
uptodate: false
hash: 66f26fecbe543127ecd03e1ed499f5e5ab9f112189ee97bc58925aeb119dddac
locale: es
language: Spanish

%--
figura:
 id: FigCapybara
 fuente: capybara.png
 leyenda: |
  Un capibara.
--%


[TOC]


## Acerca de

Crearemos una tarea simple de integración multisensorial llena de animales, en la que los participantes ven una imagen de un perro, un gato o un capibara. Se reproduce un maullido o un ladrido mientras se muestra la imagen. El participante informa si se muestra un perro o un gato, haciendo clic con el mouse en un botón de respuesta en la pantalla. No se debe dar ninguna respuesta cuando se muestra un capibara: esas son pruebas de control.

Hacemos dos predicciones simples:

- Los participantes deberían ser más rápidos para identificar perros cuando se reproduce un ladrido, y más rápidos para identificar gatos cuando se reproduce un maullido. En otras palabras, esperamos un efecto de congruencia multisensorial.
- Cuando los participantes ven un capibara, es más probable que informen que vieron un perro cuando escuchan un ladrido y es más probable que informen que vieron un gato cuando escuchan un maullido. En otras palabras, las falsas alarmas están sesgadas por el sonido.


## Tutorial

### Paso 1: Descargar e iniciar OpenSesame

OpenSesame está disponible para Windows, Linux, Mac OS y Android (solo tiempo de ejecución). Este tutorial está escrito para OpenSesame 3.3.X. Puede descargar OpenSesame desde aquí:

- %link:download%

Cuando inicie OpenSesame, se le dará a elegir plantillas de experimentos y (si corresponde) una lista de experimentos abiertos recientemente (ver %FigStartUp).

%--
figura:
 id: FigStartUp
 fuente: start-up.png
 leyenda: |
  La ventana de OpenSesame al inicio.
--%

La *Plantilla ampliada* proporciona un buen punto de partida para crear experimentos basados en pruebas. Sin embargo, en este tutorial crearemos todo el experimento desde cero. Por lo tanto, continuaremos con la 'plantilla predeterminada', que ya está cargada cuando se lanza OpenSesame (%FigDefaultTemplate). Por lo tanto, simplemente cierre las pestañas '¡Comencemos!' y (si se muestra) '¡Bienvenido!'.

%--
figura:
 id: FigDefaultTemplate
 fuente: default-template.png
 leyenda: |
  La estructura de la 'Plantilla predeterminada' vista en el área de descripción general.
--%

<div class='info-box' markdown='1'>

**Recuadro de información 1: Conceptos básicos**

Los experimentos de OpenSesame son colecciones de *ítems*. Un ítem es un pequeño fragmento de funcionalidad que, por ejemplo, se puede utilizar para presentar estímulos visuales (el ítem SKETCHPAD) o para registrar pulsaciones de teclas (el ítem KEYBOARD_RESPONSE). Los ítems tienen un tipo y un nombre. Por ejemplo, podrías tener dos elementos del tipo KEYBOARD_RESPONSE con los nombres *t1_response* y *t2_response*. Para aclarar la distinción entre tipos de ítems y nombres de ítems, utilizaremos ESTE_ESTILO para los tipos y *este estilo* para los nombres.

Para dar estructura a su experimento, dos tipos de ítems son especialmente importantes: el LOOP y la SECUENCIA. Comprender cómo puedes combinar LOOPs y SECUENCIAs para construir experimentos es quizás la parte más complicada de trabajar con OpenSesame, así que vamos a aclarar eso primero.

Un LOOP es donde, en la mayoría de los casos, se definen sus variables independientes. En un LOOP, puedes crear una tabla en la que cada columna corresponde a una variable y cada fila corresponde a una única ejecución del 'ítem a ejecutar'. Para hacer esto más concreto, consideremos el siguiente *block_loop* (no relacionado con este tutorial):

%--
figura:
 id: FigLoopTable
 fuente: loop-table.png
 leyenda: |
  Un ejemplo de variables definidas en una tabla de bucles. (Este ejemplo no está relacionado con el experimento creado en este tutorial.)
--%

Esta *block_loop* ejecutará *trial_sequence* cuatro veces. Una vez mientras `soa` es 100 y `target` es 'F', una vez mientras `soa` es 100 y `target` es 'H', etc. El orden en el que se recorren las filas es aleatorio por defecto, pero también se puede configurar de forma secuencial en la parte superior derecha de la pestaña.

Una SECUENCIA consta de una serie de elementos que se ejecutan uno tras otro. Una SECUENCIA prototípica es *trial_sequence*, que corresponde a un solo ensayo. Por ejemplo, una *trial_sequence* básica podría consistir en un SKETCHPAD, para presentar un estímulo, un KEYBOARD_RESPONSE, para recopilar una respuesta, y un LOGGER, para escribir la información del ensayo en el archivo de registro.

%--
figure:
 id: FigExampleSequence
 source: example-sequence.png
 caption: |
  Un ejemplo de un artículo de SECUENCIA utilizado como secuencia de prueba. (Este ejemplo no está relacionado con el experimento creado en este tutorial.)
--%

Puede combinar LOOPs y SEQUENCEs de manera jerárquica, para crear bloques de ensayo y fases de práctica y experimentales. Por ejemplo, *trial_sequence* es llamado por el *block_loop*. Juntos, estos corresponden a un solo bloque de ensayos. Un nivel más arriba, *block_sequence* es llamado por el *practice_loop*. Juntos, estos corresponden a la fase de práctica del experimento.

</div>


### Paso 2: Añadir un block_loop y trial_sequence

La plantilla predeterminada comienza con tres elementos: un NOTEPAD llamado *getting_started*, un SKETCHPAD llamado *welcome* y una SECUENCIA llamada *experiment*. No necesitamos *getting_started* y *welcome*, así que eliminémoslos de inmediato. Para hacerlo, haga clic con el botón derecho en estos elementos y seleccione 'Eliminar'. No elimine *experiment*, porque es la entrada para el experimento (es decir, el primer elemento que se llama cuando se inicia el experimento).

Nuestro experimento tendrá una estructura muy simple. En la parte superior de la jerarquía se encuentra un LOOP, al que llamaremos *block_loop*. El *block_loop* es el lugar donde definiremos nuestras variables independientes (ver también el recuadro 1 de antecedentes). Para agregar un LOOP a tu experimento, arrastra el ícono LOOP desde la barra de herramientas del artículo al artículo *experiment* en el área de descripción general.

Un artículo LOOP necesita otro artículo para ejecutarse; generalmente, y en este caso también, esto es una SECUENCIA. Arrastre el artículo SECUENCIA desde la barra de herramientas del artículo hasta el artículo *new_loop* en el área de descripción general. OpenSesame preguntará si desea insertar la SECUENCIA en o después del LOOP. Seleccione "Insertar en new_loop".

Por defecto, los elementos tienen nombres como *new_sequence*, *new_loop*, *new_sequence_2*, etc. Estos nombres no son muy informativos y es una buena práctica cambiarlos. Los nombres de los elementos deben consistir en caracteres alfanuméricos y/o guiones bajos. Para cambiar el nombre de un elemento, haga doble clic en el elemento en el área de descripción general. Cambie el nombre de *new_sequence* a *trial_sequence* para indicar que corresponderá a un solo ensayo. Cambie el nombre de *new_loop* a *block_loop* para indicar que corresponderá a un bloque de ensayos.

El área general de nuestro experimento ahora se ve como en %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: |
  El área general al final del Paso 2.
--%

<div class='info-box' markdown='1'>

**Recuadro de antecedentes 3: Elementos no utilizados**

__Consejo__ — Los elementos eliminados siguen estando disponibles en la papelera de elementos no utilizados, hasta que seleccione 'Eliminar permanentemente elementos no utilizados' en la pestaña Elementos no utilizados. Puede volver a agregar elementos eliminados a su experimento arrastrándolos fuera de la papelera de elementos no utilizados en una SECUENCIA o LOOP.

</div>

### Paso 3: Importar imágenes y archivos de sonido

Para este experimento, utilizaremos imágenes de gatos, perros y capibaras. También utilizaremos muestras de sonido de maullidos y ladridos. Puede descargar todos los archivos necesarios desde aquí:

- %static:attachments/cats-dogs-capybaras/stimuli.zip%

Descarga `stimuli.zip` y extráelo en algún lugar (en tu escritorio, por ejemplo). A continuación, en OpenSesame, haz clic en el botón 'Mostrar archivo de recursos' de la barra de herramientas principal (o: Menú → Ver → Mostrar archivo de recursos). Esto mostrará el archivo de recursos, por defecto en el lado derecho de la ventana. La forma más fácil de agregar los estímulos al archivo de recursos es arrastrándolos desde el escritorio (o donde hayas extraído los archivos) al archivo de recursos. Alternativamente, puedes hacer clic en el botón '+' en el archivo de recursos y agregar archivos utilizando el cuadro de selección de archivos que aparece. El archivo de recursos se guardará automáticamente con tu experimento.

Después de haber agregado todos los estímulos, tu archivo de recursos se ve como en %FigStep4.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: |
  El archivo de recursos al final del Paso 3.
--%

### Paso 4: Define las variables experimentales en el block_loop

Conceptualmente, nuestro experimento tiene un diseño 3×2 completamente cruzado: tenemos tres tipos de estímulos visuales (gatos, perros y capibaras) que ocurren en combinación con dos tipos de estímulos auditivos (maullidos y ladridos). Sin embargo, tenemos cinco ejemplares para cada tipo de estímulo: cinco sonidos de maullido, cinco imágenes de capibara, etc. Desde un punto de vista técnico, por lo tanto, tiene sentido tratar nuestro experimento como un diseño 5×5×3×2, en el cual el número de imágenes y el número de sonidos son factores con cinco niveles.

OpenSesame es muy bueno generando diseños factoriales completos. Primero, abre *block_loop* haciendo clic en él en el área de descripción general. A continuación, haz clic en el botón Diseño Factorial Completo. Esto abrirá un asistente para generar diseños factoriales completos, que funciona de una manera sencilla: cada columna corresponde a una variable experimental (es decir, un factor). La primera fila es el nombre de la variable, las filas debajo contienen todos los posibles valores (es decir, niveles). En nuestro caso, podemos especificar nuestro diseño 5×5×3×2 como se muestra en %FigLoopWizard.

%--
figure:
 id: FigLoopWizard
 source: loop-wizard.png
 caption: |
  El asistente de bucles genera diseños factoriales completos.
--%

Después de hacer clic en 'Aceptar', verás que ahora hay una tabla LOOP con cuatro filas, una para cada variable experimental. Hay 150 ciclos (=5×5×3×2), lo que significa que tenemos 150 ensayos únicos. Tu tabla LOOP ahora se ve como en %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: |
  La tabla LOOP al final del Paso 4.
--%

### Paso 5: Agregar elementos a la secuencia de prueba

Abre *trial_sequence*, que aún está vacía. ¡Es hora de agregar algunos elementos! Nuestra *trial_sequence* básica es:

1. Un SKETCHPAD para mostrar un punto de fijación central durante 500 ms
2. Un SAMPLER para reproducir un sonido de animal
3. Un SKETCHPAD para mostrar una imagen de un animal
4. Un MOUSE_RESPONSE para recopilar una respuesta
5. Un LOGGER para escribir los datos en el archivo

Para agregar estos elementos, simplemente arrástralos uno por uno desde la barra de elementos hasta la *trial_sequence*. Si accidentalmente sueltas elementos en el lugar equivocado, puedes simplemente reorganizarlos arrastrándolos y soltándolos. Una vez que todos los elementos estén en el orden correcto, dales a cada uno de ellos un nombre razonable. El área de descripción general ahora se ve como en %FigStep6.

%--
figure:
 id: FigStep6
 source: step6.png
 caption: |
  El área de descripción general al final del Paso 5.
--%

### Paso 6: Define el punto de fijación central

Haz clic en *fixation_dot* en el área de descripción general. Esto abre una pizarra básica que puedes usar para diseñar tus estímulos visuales. Para dibujar un punto de fijación central, primero haz clic en el ícono de la mira, y luego haz clic en el centro de la pantalla, es decir, en la posición (0, 0).

También necesitamos especificar cuánto tiempo es visible el punto de fijación. Para hacerlo, cambia la duración de 'keypress' a 495 ms, para especificar una duración de 500 ms. (Consulta el recuadro de antecedentes 4 para obtener una explicación).

El elemento *fixation_dot* ahora se ve como en %FigStep7.

%--
figure:
 id: FigStep7
 source: step7.png
 caption: |
  El elemento *fixation_dot* al final del Paso 6.
--%

<div class='info-box' markdown='1'>

**Caja de antecedentes 4: Seleccionar la duración correcta**

¿Por qué especificar una duración de 495 si queremos una duración de 500 ms? La razón es que la duración real de la presentación en pantalla siempre se redondea hacia arriba a un valor que sea compatible con la tasa de refresco del monitor. Esto puede sonar complicado, pero para la mayoría de los propósitos, las siguientes reglas básicas son suficientes:

1. Elija una duración que sea posible dada la tasa de refresco de su monitor. Por ejemplo, si la tasa de refresco de su monitor es de 60 Hz, esto significa que cada fotograma dura 16,7 ms (= 1000 ms/60 Hz). Por lo tanto, en un monitor de 60 Hz, siempre debe seleccionar una duración que sea múltiplo de 16,7 ms, como 16,7, 33,3, 50, 100, etc.
2. En el campo de duración del SKETCHPAD, especifique una duración que sea unos milisegundos más corta de lo que busca. Entonces, si desea presentar un SKETCHPAD durante 50 ms, elija una duración de 45. Si desea presentar un SKETCHPAD durante 1000 ms, elija una duración de 995. Etcétera.

Para una discusión detallada sobre el tiempo experimental, vea:

- %link:timing%

</div>

### Paso 7: Definir el sonido del animal

Abra *animal_sound*. El elemento SAMPLER ofrece varias opciones, siendo la más importante el archivo de sonido que se reproducirá. Haga clic en el botón de explorar para abrir el cuadro de diálogo de selección del archivo, y seleccione uno de los archivos de sonido, como `bark1.ogg`.

¡Por supuesto, no queremos reproducir el mismo sonido una y otra vez! En su lugar, queremos seleccionar un sonido basado en las variables `sound` y `sound_nr` que hemos definido en el *block_loop* (Paso 5). Para hacer esto, simplemente reemplace la parte de la cadena que desea que dependa de una variable por el nombre de esa variable entre corchetes. Más específicamente, 'bark1.ogg' se convierte en '[sound][sound_nr].ogg', porque queremos reemplazar 'bark' por el valor de la variable `sound` y '1' por el valor de `sound_nr`.

También necesitamos cambiar la duración del SAMPLER. De forma predeterminada, la duración es 'sonido', lo que significa que el experimento se pausará mientras se reproduce el sonido. Cambie la duración a 0. Esto no significa que el sonido se reproducirá solo por 0 ms, sino que el experimento avanzará de inmediato al siguiente elemento, mientras el sonido continúa reproduciéndose en segundo plano. El elemento *animal_sound* ahora se muestra como en %FigStep8.

%--
figure:
 id: FigStep8
 source: step8.png
 caption: |
  El elemento *animal_sound* al final del Paso 7.
--%

<div class='info-box' markdown='1'>

**Recuadro informativo 5: Variables**

Para obtener más información sobre el uso de variables, consulte:

- %link:manual/variables%

</div>


### Paso 8: Definir la imagen del animal

Abra *animal_picture*. Seleccione la herramienta de imagen haciendo clic en el botón con el icono de paisaje. Haga clic en el centro (0, 0) de la pantalla. En el cuadro de diálogo de File Pool que aparece, seleccione `capybara1.png`. La mirada de soslayo del capibara ahora lo mirará perezosamente desde el centro de la pantalla. Pero, por supuesto, no siempre queremos mostrar el mismo capibara. En su lugar, queremos que la imagen dependa de las variables `animal` y `pic_nr` que hemos definido en el *block_loop* (Paso 4).

Podemos usar esencialmente el mismo truco que hicimos para *animal_sound*, aunque las cosas funcionan de manera un poco diferente para las imágenes. Primero, haga clic con el botón derecho en el capibara y seleccione 'Edit script'. Esto le permite editar la siguiente línea de script de OpenSesame que corresponde a la imagen del capibara:

```python
draw image center=1 file="capybara1.png" scale=1 show_if=always x=0 y=0 z_index=0
```

Ahora cambie el nombre del archivo de imagen de 'capybara.png' a '[animal][pic_nr].png':

```python
draw image center=1 file="[animal][pic_nr].png" scale=1 show_if=always x=0 y=0 z_index=0
```

Haga clic en 'Aceptar' para aplicar el cambio. El capibara ha desaparecido, reemplazado por una imagen de marcador de posición, y OpenSesame le indica que un objeto no se muestra, porque está definido usando variables. ¡No se preocupe, se mostrará durante el experimento!

También agregamos dos círculos de respuesta:

- Un círculo con el nombre 'perro' en el lado izquierdo de la pantalla. (Para recordar al participante la regla de respuesta, puedes agregar un elemento de texto con el texto 'perro' al círculo. Esto es puramente visual).
- Un círculo con el nombre 'gato' en el lado derecho de la pantalla. (Para recordar al participante la regla de respuesta, puedes agregar un elemento de texto con el texto 'gato' al círculo).

Vamos a utilizar estos círculos como *regiones de interés* para nuestras respuestas del ratón. Más específicamente, como hemos dado nombres a los círculos, nuestro elemento *mouse_response* podrá verificar si el clic del ratón cae dentro de uno de estos círculos. Volveremos a esto en el Paso 9.

Finalmente, establece el campo 'Duración' en '0'. Esto no significa que la imagen se presente solo por 0 ms, sino que el experimento avanzará al siguiente elemento (*respuesta*) de inmediato. Dado que *respuesta* espera una respuesta pero no cambia lo que está en la pantalla, el objetivo seguirá siendo visible hasta que se haya dado una respuesta.

%--
figure:
 id: FigStep9
 source: step9.png
 caption: |
  The *animal_picture* SKETCHPAD at the end of Step 8.
--%

<div class='info-box' markdown='1'>

**Caja de fondo 6: Formatos de imagen**

__Consejo__: OpenSesame puede manejar una amplia variedad de formatos de imágenes. Sin embargo, se sabe que algunos formatos de `.bmp` (no estándar) causan problemas. Si descubres que una imagen `.bmp` no se muestra, es posible que desees considerar usar un formato diferente, como `.png`. Puedes convertir imágenes fácilmente con herramientas gratuitas como [GIMP].

</div>


### Paso 9: Definir la respuesta

Abre el elemento *mouse_response*. Este es un elemento MOUSE_RESPONSE, que recopila un solo clic del ratón (o suelta). Hay algunas opciones:

- __Respuesta correcta__ - aquí es donde puedes indicar qué botón del ratón es la respuesta correcta. Sin embargo, determinaremos si una respuesta es correcta en función de dónde haga clic el participante, y no en función del botón que se haga clic, por lo que podemos dejar este campo vacío.
- __Respuestas permitidas__ es una lista separada por puntos y comas de los botones del ratón que se aceptan. Configurémoslo en 'left_button'.
- __Tiempo límite__ indica una duración después de la cual la respuesta se establecerá en 'Ninguna' y el experimento continuará. Un tiempo límite es importante en nuestro experimento, porque los participantes deben tener la oportunidad de *no* responder cuando ven una capibara. Así que establezcamos el tiempo límite en 2000.
- __SKETCHPAD vinculado__ indica un SKETCHPAD del cual se deben utilizar los elementos como regiones de interés. Seleccionaremos *animal_picture*. Ahora, si hacemos clic en el elemento con el nombre 'gato', la variable `cursor_roi` se establecerá automáticamente en 'gato'.
- __Cursor del ratón visible__ - Indica que el cursor del ratón debe mostrarse durante la recolección de la respuesta. Debemos habilitar esto, para que los participantes puedan ver dónde hacen clic.
- __Descartar clics del ratón pendientes__ indica que solo debemos aceptar nuevos clics del ratón. Es mejor dejarlo habilitado (lo está por defecto).

%--
figure:
 id: FigStep10
 source: step10.png
 caption: |
  The *mouse_response* MOUSE_RESPONSE at the end of Step 9.
--%


### Paso 10: Definir el logger

No necesitamos configurar el LOGGER porque su configuración predeterminada está bien. Pero echemos un vistazo de todos modos. Haz clic en *logger* en el área de descripción general para abrirlo. Verás que la opción 'Registrar todas las variables (recomendado)' está seleccionada. Esto significa que OpenSesame registra todo, lo cual está bien.

<div class='info-box' markdown='1'>

**Caja de fondo 8: ¡Siempre revisa tus datos!**

__El consejo que lo gobierna todo__ - ¡Siempre verifica tres veces si todas las variables necesarias se registran en tu experimento! La mejor manera de verificar esto es ejecutar el experimento e investigar los archivos de registro resultantes.

</div>

### Paso 11: ¡Terminado! (Más o menos…)

Ahora deberías poder ejecutar tu experimento. Todavía hay mucho espacio para mejorar, y trabajarás en pulir el experimento como parte de las asignaciones adicionales a continuación. ¡Pero la estructura básica está ahí!

Haz clic en el botón 'Ejecutar en pantalla completa' (`Control+R`) en la barra de herramientas principal para realizar una prueba.

<div class='info-box' markdown='1'>

**Caja de fondo 11: Ejecución rápida**

__Consejo__ — Una prueba se ejecuta aún más rápido haciendo clic en el botón naranja 'Ejecutar en ventana', que no te pregunta cómo guardar el archivo de registro (y, por lo tanto, solo debe usarse con fines de prueba).

</div>


## Tareas adicionales

Las tareas adicionales a continuación son para que las resuelvas por tu cuenta. Las soluciones a estas tareas se pueden encontrar en el [archivo del experimento](https://osf.io/2gr3a/). ¡Pero la mejor manera de aprender es resolverlas por ti mismo!


### Fácil: Añadir una pantalla de instrucciones y despedida

- Los elementos SKETCHPAD y FORM_TEXT_DISPLAY pueden presentar texto
- Las buenas instrucciones son breves y concretas


### Fácil: Inspeccionar los datos

- Realiza el experimento una vez en ti mismo. Puedes reducir el número de pruebas estableciendo el valor de Repetir del *block_loop* a menos de uno.
- Abre el archivo de datos en Excel, LibreOffice o JASP


### Intermedio: Proporcionar retroalimentación en cada prueba

- Para hacer esto, ¡debes haber definido ya una respuesta correcta! (Ver más abajo.)
- Una forma discreta de proporcionar retroalimentación es presentar brevemente un punto rojo después de una respuesta incorrecta y un punto verde después de una respuesta correcta
- ¡Usa declaraciones Run If!


### Intermedio: Contrarrestar la regla de respuesta

- La variable `subject_parity` es 'even' (par) o 'odd' (impar)
- Utiliza dos elementos diferentes de SKETCHPAD y MOUSE_RESPONSE de imágenes de animales para participantes pares e impares


### Intermedio: No repetir la misma imagen de animal

- Puedes especificar las restricciones de aleatorización como operaciones avanzadas de bucle


### Difícil: Determinar si la respuesta fue correcta

- Esto requiere un INLINE_SCRIPT
- Establece la variable `correct` en 0 para una respuesta incorrecta y en 1 para una respuesta correcta
- Si se produce un tiempo de espera, la variable `response` es la cadena 'None'
- De lo contrario, la variable `cursor_roi` contiene una lista separada por punto y coma de todos los nombres de los elementos (del SKETCHPAD vinculado) en los que se hizo clic. Es posible hacer clic en más de un elemento, por ejemplo, si la imagen del animal y el círculo de respuesta se superponen


### Difícil: Dividir las pruebas en varios bloques

- Agrega un SKETCHPAD al final de la trial_sequence que invite a los participantes a tomar un breve descanso
- Utiliza una declaración Run If para ejecutar este SKETCHPAD solo después de cada 15 pruebas
- Necesitarás el operador módulo (`%`) para hacer esto, así como la variable `count_trial_sequence`


### Difícil: Adaptar el experimento para ejecutarlo en línea

- Esto requiere un INLINE_JAVASCRIPT
- Actualmente, OSWeb no admite vincular un MOUSE_RESPONSE a un SKETCHPAD. Esto significa que necesitas usar la variable `cursor_x` para determinar dónde hizo clic el participante y si la respuesta fue correcta.
- OSWeb no admite elementos INLINE_SCRIPT


## Referencias

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: Un constructor de experimentos de código abierto y gráfico para las ciencias sociales. *Behavior Research Methods*, *44*(2), 314–324. doi:10.3758/s13428-011-0168-7
{: .reference}