title: Estímulos visuales
hash: 88ce873464207508e0ba22cecad7bdf4c51299ae1bf089ba96618c35389e13c2
locale: es
language: Spanish

La forma más común de presentar estímulos visuales es utilizando el elemento SKETCHPAD, o, para estímulos no críticos en cuanto a tiempo, el elemento FEEDBACK.


[TOC]


## Uso de los elementos sketchpad y feedback

Los elementos SKETCHPAD y FEEDBACK ofrecen herramientas de dibujo básicas lo-que-ves-es-lo-que-obtienes (%FigSketchpad).

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: El SKETCHPAD proporciona herramientas de dibujo incorporadas.
--%


## Uso de expresiones show-if

Puedes usar expresiones show-if para determinar si un elemento particular debe ser mostrado o no. Por ejemplo, si tienes una imagen de una cara feliz que solo debe mostrarse cuando la variable `valence` tiene el valor 'positivo', entonces puedes establecer la expresión show-if para el elemento de imagen correspondiente a:

```python
valence == 'positive'
```

Si dejas una expresión show-if vacía o ingresas `True`, el elemento siempre se mostrará. Las expresiones show-if utilizan la misma sintaxis que otras expresiones condicionales. Para más información, ver:

- %link:manual/variables%

Las expresiones show-if se evalúan en el momento en que se prepara la visualización. Esto significa que para los elementos SKETCHPAD, se evalúan durante la fase de preparación, mientras que para los elementos FEEDBACK, se evalúan durante la fase de ejecución (ver también la sección de abajo).


## La diferencia entre los elementos sketchpad y feedback

Los elementos SKETCHPAD y FEEDBACK son idénticos en la mayoría de los aspectos, excepto por dos diferencias importantes.


### Los elementos sketchpad se preparan con anticipación, los elementos feedback no

El contenido de un SKETCHPAD se prepara durante la fase de preparación de la SEQUENCE de la que forma parte. Esto es necesario para asegurar una sincronización precisa: permite que el SKETCHPAD se muestre inmediatamente durante la fase de ejecución, sin ningún retraso debido a la preparación del estímulo. Sin embargo, la desventaja de esto es que el contenido de un SKETCHPAD no puede depender de lo que sucede durante la SEQUENCE de la que forma parte. Por ejemplo, no puedes usar un SKETCHPAD para proporcionar retroalimentación inmediata sobre el tiempo de respuesta obtenido por un elemento KEYBOARD_RESPONSE (asumiendo que el SKETCHPAD y KEYBOARD_RESPONSE son parte de la misma secuencia).

En contraste, el contenido de un elemento FEEDBACK solo se prepara cuando realmente se muestra, es decir, durante la fase de ejecución de la SEQUENCE de la que forma parte. Esto permite proporcionar retroalimentación sobre cosas que acaban de suceder, de ahí el nombre. Sin embargo, el elemento FEEDBACK no debería usarse para presentar estímulos críticos en tiempo, ya que sufre retrasos debido a la preparación del estímulo.

Para más información sobre la estrategia de preparación-ejecución, ver:

- %link:prepare-run%


### Las variables de feedback son (por defecto) reiniciadas por los elementos feedback

El elemento FEEDBACK tiene una opción 'Restablecer variables de feedback'. Cuando esta opción está habilitada (y está habilitada por defecto), las variables de feedback se restablecen cuando se muestra el elemento FEEDBACK.

Para más información sobre las variables de feedback, ver:

- %link:manual/variables%


## Presentación de estímulos visuales en el script Python en línea

### Accediendo a un SKETCHPAD en Python

Puedes acceder al objeto `Canvas` de un SKETCHPAD a través de la propiedad `canvas` de los ítems. Por ejemplo, digamos que tu SKETCHPAD se llama *my_sketchpad,* y contiene un elementos de imagen con el nombre 'my_image'. Podrías hacer rotar esta imagen con el siguiente script:

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~


### Creando un Canvas en Python

Puedes usar el objeto `Canvas` para presentar estímulos visuales en Python:

- %link:manual/python/canvas%