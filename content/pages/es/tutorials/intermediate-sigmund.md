title: Tutorial de SigmundAI: Tarea de búsqueda visual
hash: 2662b1ce900715b74ee381b68acb991140b33a5656bfb23c5b7bee6cd4c44cec
locale: es
language: Spanish

[TOC]

## Acerca de este tutorial

Este tutorial muestra cómo crear un experimento clásico de búsqueda visual en OpenSesame usando SigmundAI, el copiloto de IA, integrado directamente en la interfaz de OpenSesame. En lugar de construir el experimento completamente a mano, aprenderás a colaborar con Sigmund para construir la estructura experimental completa, definir diseños factoriales e implementar la generación dinámica de estímulos mediante lógica programada.


## Lo que aprenderás

Al final de este tutorial, sabrás cómo:

- 💡 Dar a Sigmund instrucciones claras y eficaces
- 💡 Dividir tareas complejas en pasos simples
- 💡 Detectar y corregir los errores de Sigmund (sí, ¡la IA comete errores!)
- 💡 Construir estructuras de experimentos rápidamente
- 💡 Escribir scripts con Sigmund
- 💡 Trabajar eficientemente con un copiloto de IA

## Conectar OpenSesame con Sigmund 

Sigmund es un asistente de IA diseñado específicamente para OpenSesame. A diferencia de chatbots generales como ChatGPT, Sigmund:

- Conoce OpenSesame a fondo
- Funciona directamente dentro de la interfaz de OpenSesame
- Puede hacer cambios en tu experimento automáticamente

Para conectarte, simplemente inicia sesión en [sigmundai.eu](https://sigmundai.eu). El panel de Sigmund en OpenSesame se conectará automáticamente:

<video controls width ="100%"> 
    <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>
<p align="center"><em>Vídeo 1. Conectar OpenSesame con Sigmund.</em></p>


## El experimento 

En este tutorial, crearás un experimento básico de búsqueda visual. El experimento se parece a los estudios clásicos de búsqueda visual de [Treisman and Gelade (1980)][references], pero no es idéntico.

En este experimento, los participantes buscan un objeto objetivo, que puede ser un cuadrado amarillo, un círculo amarillo, un cuadrado azul o un círculo azul; la identidad del objetivo varía entre bloques de ensayos. Los participantes indican si el objetivo está presente o no presionando la tecla de flecha derecha (presente) o izquierda (ausente).

Además del objetivo, se muestran cero o más objetos distractores. Hay tres condiciones, y la condición determina qué tipo de distractores hay:

- En la condición de *Conjunction*, los distractores pueden tener cualquier forma y color, con la única restricción de que los distractores no pueden ser idénticos al objetivo. Así, por ejemplo, si el objetivo es un cuadrado amarillo, entonces los distractores son círculos amarillos, círculos azules y cuadrados azules.

- En la condición de *Shape Feature*, los distractores tienen una forma diferente de la del objetivo, pero pueden tener cualquier color. Así, por ejemplo, si el objetivo es un cuadrado amarillo, entonces los distractores son círculos amarillos y círculos azules.

- En la condición de *Color Feature*, los distractores pueden tener cualquier forma, pero tienen un color diferente del objetivo. Así, por ejemplo, si el objetivo es un cuadrado amarillo, entonces los distractores son cuadrados azules y círculos azules.

Se muestra retroalimentación inmediata después de cada ensayo: un punto verde después de una respuesta correcta y un punto rojo después de una respuesta incorrecta. Se muestra retroalimentación detallada sobre los tiempos de respuesta medios y la precisión después de cada bloque de ensayos.

%--
figure:
 id: FigVisualSearch
 source: visual-search.svg.png
 caption: The visual-search experiment that you will implement in this tutorial.
--%


Experimentos como este muestran dos hallazgos típicos:

- Se tarda más tiempo en encontrar el objetivo en la condición de Conjunction que en las dos condiciones de Feature.
- En la condición de Conjunction, los tiempos de respuesta aumentan a medida que aumenta el número de distractores. Esto sugiere que las personas buscan el objetivo un elemento a la vez; esto se llama *búsqueda serial*.
- En las condiciones de Feature (tanto de forma como de color), los tiempos de respuesta no aumentan, o apenas aumentan, a medida que aumenta el número de distractores. Esto sugiere que las personas procesan toda la pantalla de una sola vez; esto se llama *búsqueda paralela*.

De acuerdo con la teoría de integración de características de Treisman y Gelade, estos resultados reflejan que la condición Conjunction requiere que combines, o *bind*, el color y la forma de cada objeto. Esta unión requiere atención, y por lo tanto necesitas desplazar tu atención de un objeto al siguiente; esto es lento, y explica por qué los tiempos de respuesta dependen de cuántos objetos hay. En contraste, en las condiciones Feature, el color y la forma no necesitan unirse, y por lo tanto toda la pantalla puede procesarse en una sola pasada sin que la atención se dirija a todos y cada uno de los objetos.

## Paso 1: Construir la estructura principal  

Antes de empezar a construir un experimento, ayuda entender cómo se organizan los experimentos en OpenSesame. 
En OpenSesame un experimento está compuesto por items que controlan qué ocurre y en qué orden. 
Primero queremos definir esta estructura para que Sigmund pueda construir sobre ella. 

El marco básico de nuestro experimento incluye:

1. La secuencia experimental principal – Esta contiene todo el experimento
2. Un lugar para las instrucciones generales – Los participantes necesitarán instrucciones antes de que comience el experimento.
3. Un loop que define los diferentes bloques experimentales – Un loop repite parte del experimento varias veces. En nuestro caso, cada repetición corresponderá a un bloque experimental.
4. Una sequence que define lo que ocurre dentro de cada bloque – Esta sequence contendrá más adelante los ensayos y la lógica específica del bloque.
5. Y una pantalla final – Para que los participantes sepan cuándo ha terminado el experimento.

Usar una estructura clara como esta nos mantiene organizados tanto a nosotros como a Sigmund. Si intentamos hacer que Sigmund construya todo de una vez, será más probable que cometa errores y nos resultará más difícil detectar los fallos y corregirlos. 

¡Así que primero hagamos el marco, y luego completamos los detalles!


💬 **Prompt:**

```text
Hi Sigmund! I’d like to build a visual search experiment. Please create this structure without adding content yet:

- experiment (sequence)
  - instructions (sketchpad)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_message (sketchpad)
```

Cuando Sigmund haya terminado, el área de resumen debería verse como %FigStep1: 

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area after creating the main structure.
--%


Antes de continuar, deberíamos pedirle a Sigmund que le dé a nuestro experimento un nombre adecuado y elimine cualquier item innecesario: 


💬 **Prompt:**
```text
Please remove unnecessary default items and give the experiment a clear title.
```

%--
figure:
 id: FigStep1b
 source: step1b.png
 caption: |
  The overview area at the end of Step 1.
--%


## Paso 2: Construir block_sequence 

El experimento de búsqueda visual es jerárquico. Eso significa que el experimento contiene bloques y que los propios bloques contienen ensayos. En cada bloque, los participantes completarán múltiples ensayos buscando el mismo objetivo. ¡Es importante que no confundamos estos niveles, de lo contrario los objetivos podrían variar entre ensayos! 


El siguiente paso es construir la estructura de un solo bloque. Cada bloque debe tener: 

1. Instrucciones que le digan al participante cuál es el objetivo
2. Un loop que ejecute todos los ensayos de ese bloque 
3. Una pantalla de feedback del bloque

💬 **Prompt:**

```text
Now create the block_sequence contents. It should look like this:

- block_sequence (sequence)
  - block_instructions (sketchpad)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)
  
Just build the structure for now.
```

Tu área de resumen ahora debería verse como %FigStep2.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%


## Paso 3: Definir las variables entre bloques

Los objetivos tienen dos características, forma y color, que cambian entre bloques. Por lo tanto, Sigmund necesita definirlas en el loop externo (experimental_loop).  
Si en cambio definimos estas variables dentro del loop de ensayos, el objetivo cambia en cada ensayo en lugar de en cada bloque.

Ahora le indicamos a Sigmund que defina variables en experimental_loop para crear todas las combinaciones de círculo/cuadrado y azul/amarillo.


💬 **Prompt:**

```text
Please define the variables in experimental_loop so that all combinations of:

  1. target_shape (circle/square)
  2. target_color (blue/yellow)

occur equally often across blocks.
```

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The table of experimental_loop at the end of step 3."
--%


## Paso 4: Definir las condiciones de ensayo

Dentro de cada bloque, tres factores varían de un ensayo a otro:

1. La condición (conjunction / shape / color)
2. El número de estímulos (1 / 5 / 15)
3. Si el objetivo está presente o no.

Queremos que Sigmund genere condiciones de ensayo para todas las combinaciones, un diseño factorial completo.
3 condiciones x 3 tamaños de conjunto x 2 niveles de presencia = 18 tipos de ensayo

💬 **Prompt:**

```text
Now define the block_loop variables. This should be a full factorial design with:

- condition: conjunction, feature_shape, feature_color
- set_size: 1, 5, 15
- target_present: present, absent

Please create all combinations.
```

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The table of block_loop at the end of step 4."
--%


## Paso 5: Construir la secuencia de ensayo

Ahora necesitamos definir qué ocurre en un único ensayo. Primero creemos los ítems; añadiremos contenido en los siguientes pasos.
Durante un único ensayo:

1. Mostramos un punto de fijación 
2. Mostramos la pantalla principal de búsqueda (esto requiere un inline script de Python)
3. Obtenemos la respuesta del participante 
4. Registramos los datos que necesitamos 
5. Damos retroalimentación al participante


💬 **Prompt:**

```text
Please add items to trial_sequence in this order:

- fixation (sketchpad)
- search_display_script (inline_script)
- keyboard_response (keyboard_response)
- logger (logger)
- green_feedback (sketchpad)
- red_feedback (sketchpad)

Only create the items for now, don’t add content yet.
```

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The trial_sequence at the end of Step 5."
--%


## Paso 6: Pantalla de fijación

¡Empecemos a añadir contenido! Haz que Sigmund dibuje un punto de fijación en el centro del sketchpad: 

💬 **Prompt:**

```text
Please draw a central fixation dot in the fixation item and set its duration to 500 ms.
```

%--
figure:
 id: FigStep6
 source: step6.png
 caption: "The fixation display"
--%


## Paso 7: Generar la pantalla de búsqueda visual

Generar la pantalla de búsqueda visual va más allá de lo que la interfaz gráfica de OpenSesame puede hacer. Necesitamos generación dinámica de estímulos, colocación aleatoria y lógica condicional. OpenSesame ofrece la opción de hacerlo usando Python (`inline_script`) o JavaScript (`inline_javscript`). En nuestro caso, usaremos Python. Ya añadimos un inline script (vacío) a la secuencia de ensayo en el Paso 5.

Pero ¿qué pasa si no podemos o no queremos escribir un script nosotros mismos? ¡Sigmund puede hacerlo por nosotros! Dile a Sigmund que escriba el script que necesitamos: 

💬 **Prompt:**

```text
Now implement the search display using the inline script. It should:

- create a canvas
- generate random non-overlapping positions
- draw the target if present
- draw distractors based on the condition:
  - conjunction: any shape/color except target combination
  - feature_shape: shape must differ from target
  - feature_color: color must differ from target
- use the set_size variable for the number of items
- raise an error if invalid values occur

The script should show the canvas.
```

Como esta tarea es un poco más compleja, Sigmund a veces comete errores. Sin embargo, ¡puede que Sigmund sea capaz de corregirlos por sí mismo! Intenta ejecutar el experimento y, si devuelve un error, pide a Sigmund que lo corrija.

Un ejemplo de un error común es que Sigmund a veces olvida importar una biblioteca de Python, como `random`. Si notas esto, ¡puedes señalarlo y pedirle a Sigmund que lo arregle!

💬 **Prompt:**

```text
Parece que olvidaste importar random. ¡Por favor arréglalo!
```

Si todo salió bien, ahora puedes ejecutar el experimento (aunque todavía esté incompleto) y mostrará una pantalla como esta:

%--
figure:
 id: FigStep7
 source: step7.png
 caption: "A visual search display."
--%


## Step 8: Definir la respuesta correcta

El elemento keyboard_response que Sigmund puso antes comprueba las respuestas con una variable llamada correct_response. Así que debemos definir cuál es la respuesta correcta antes de que se recoja la respuesta. Podemos pedirle a Sigmund que lo haga con un inline script:

💬 **Prompt:**

```text
Añade lógica para que el experimento sepa cuál es la respuesta correcta.

- Si target_present está presente → correct_response es la tecla de flecha derecha.
- Si target_present está ausente → correct_response es la tecla de flecha izquierda.

Por favor, impleméntalo usando un nuevo inline script colocado antes del elemento keyboard_response.
```

## Step 9: Configurar la respuesta de teclado

Solo las teclas de flecha izquierda y derecha son respuestas válidas, así que restringimos a los participantes a usar solo esas. También podemos pedirle a Sigmund que avance automáticamente al siguiente ensayo después de una cantidad fija de tiempo si el participante no responde dentro de un tiempo razonable (es decir, un timeout).

💬 **Prompt:**

```text
Por favor configura la keyboard_response de modo que:

- el timeout sea de 3000 ms
- solo se permitan las teclas de flecha izquierda y derecha
```

## Step 10: Crear las pantallas de feedback

A continuación queremos dar a los participantes feedback sobre si identificaron correctamente la presencia del objetivo en un ensayo. Dile a Sigmund que establezca dinámicamente la pantalla de feedback:

💬 **Prompt:**

```text
Ahora configura los sketchpads de feedback:

- green_feedback debe mostrar un punto de fijación verde durante 500 ms
- red_feedback debe mostrar un punto de fijación rojo durante 500 ms

Muestra verde solo después de respuestas correctas y rojo solo después de respuestas incorrectas.
```

## Step 11: Instrucciones del bloque

¡Los participantes necesitan saber qué están buscando! Pídele a Sigmund que cree la pantalla de instrucciones y muestre una representación del objetivo actual:

💬 **Prompt:**

```
Por favor añade instrucciones a block_instructions que indiquen a los participantes qué objetivo buscar, basándose en la forma y el color del objetivo del bloque actual. Muestra visualmente cómo es el objetivo.
```

%--
figure:
 id: FigStep11
 source: step11.png
 caption: "The instruction display."
--%


## Step 12: Feedback del bloque

Después de cada bloque damos a los participantes feedback sobre qué tan bien lo hicieron basándonos en la precisión y el tiempo de respuesta. Dejemos que Sigmund haga la pantalla por nosotros:

💬 **Prompt:**

```text
Configura el elemento de feedback para que muestre la precisión media y el tiempo de respuesta del bloque.
```

%--
figure:
 id: FigStep12
 source: step12.png
 caption: "The block feedback display."
--%


## Step 13: Mensaje de cierre

Por último, añadimos un mensaje de cierre.

💬 **Prompt:**

```text
Establece un mensaje de fin del experimento en end_message.
```

## Terminado

¡Enhorabuena, el experimento está completo! Puedes hacer una ejecución de prueba haciendo clic en el botón azul de doble flecha (atajo: Ctrl+W).

Aquí tienes cómo se ve un bloque de búsqueda visual completado:

<video controls width="100%">
  <source src="/video/visual-search-demo.mp4" type="video/mp4">
</video>

<p align="center"><em>Vídeo 2. Demostración de un bloque de búsqueda visual completado.</em></p>

Para asegurarte de que el experimento funciona bien, comprueba si reconoces los siguientes elementos:

1. Cada bloque comienza con instrucciones que muestran la forma y el color del objetivo actual
2. Cada ensayo tiene un punto de fijación y el feedback correcto se muestra inmediatamente después de cada ensayo
3. A lo largo de los ensayos, varían los tamaños de conjunto y la presencia del objetivo
4. Después de cada bloque hay un resumen del rendimiento

Si notas pequeños bugs o errores, no te preocupes. Sigmund a menudo puede corregirlos por sí solo. Intenta ejecutar el experimento y, si aparece un error, simplemente describe el problema a Sigmund y pídele que lo corrija. Por ejemplo, Sigmund normalmente puede corregir imports faltantes, nombres de variables incorrectos o pequeños errores de lógica cuando se los señalas. Aprender a probar tu experimento y a pedirle iterativamente a Sigmund correcciones específicas es una parte importante de trabajar de forma eficiente con un copiloto de IA.

## Referencias

<div class='reference' markdown='1'>
Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, *12*(1), 97–136. doi:10.1016/0010-0285(80)90005-5
</div>

[references]: #references