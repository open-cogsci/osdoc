title: Estímulos visuales
hash: 4ead1768298a015dc8af358675db670a71ea61876c2803a8998223c3509860c5
locale: es
language: Spanish

La forma más común de presentar estímulos visuales es utilizando el elemento SKETCHPAD o, para estímulos no críticos en tiempo, el elemento FEEDBACK .

[TOC]

## Uso de los elementos sketchpad y feedback

Los elementos SKETCHPAD y FEEDBACK ofrecen herramientas básicas de dibujo de lo que ves es lo que obtienes (%FigSketchpad).

%--
figura:
 id: FigSketchpad
 fuente: sketchpad.png
 leyenda: El SKETCHPAD proporciona herramientas de dibujo incorporadas.
--%

## La diferencia entre los elementos sketchpad y feedback

Los elementos SKETCHPAD y FEEDBACK son idénticos en la mayoría de los aspectos, excepto por dos diferencias importantes.

### Los elementos Sketchpad se preparan con anticipación, los elementos feedback no.

El contenido de un SKETCHPAD se prepara durante la fase de preparación de la SECUENCIA en la que forma parte. Esto es necesario para garantizar un tiempo preciso: permite que el SKETCHPAD se muestre de inmediato durante la fase de ejecución, sin demoras debido a la preparación del estímulo. Sin embargo, el inconveniente es que el contenido de un SKETCHPAD no puede depender de lo que suceda durante la SECUENCIA en la que forma parte. Por ejemplo, no puede usar un SKETCHPAD para proporcionar comentarios inmediatos sobre el tiempo de respuesta recopilado por un elemento KEYBOARD_RESPONSE (suponiendo que el SKETCHPAD y KEYBOARD_RESPONSE formen parte de la misma secuencia).

En contraste, el contenido de un elemento FEEDBACK solo se prepara cuando se muestra, es decir, durante la fase de ejecución de la SECUENCIA en la que forma parte. Esto permite proporcionar retroalimentación sobre cosas que acaban de suceder, de ahí el nombre. Sin embargo, el elemento FEEDBACK no debe usarse para presentar estímulos críticos en tiempo, ya que tiene retrasos debido a la preparación del estímulo.

Para obtener más información sobre la estrategia de preparación-ejecución, consulte:

- %link:prepare-run%

### Las variables de retroalimentación se restablecen (por defecto) por los elementos de retroalimentación

El elemento FEEDBACK tiene una opción "Restablecer variables de retroalimentación". Cuando esta opción está activada (lo está por defecto), las variables de retroalimentación se restablecen cuando se muestra el elemento FEEDBACK.

Para obtener más información sobre las variables de retroalimentación, consulte:

- %link:manual/variables%

## Presentación de estímulos visuales en un script Python en línea

### Acceso a un SKETCHPAD en Python

Puede acceder al objeto "Canvas" de un SKETCHPAD como propiedad "canvas" del elemento. Por ejemplo, suponga que su SKETCHPAD se llama * my_sketchpad * y contiene elementos de imagen con el nombre "my_image". Entonces, podría hacer que esta imagen gire con el siguiente script:

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~

### Crear un Canvas en Python

Puede usar el objeto "Canvas" para presentar estímulos visuales en Python:

- %link:manual/python/canvas%