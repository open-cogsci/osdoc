title: Cambios importantes en OpenSesame 3
hash: 5ff5aa4ddc6076985d2733031a24955084f95edb98e5b60980505b16b020ae44
locale: es
language: Spanish

[TOC]


## Cambios en 3.3

OpenSesame 3.3 presenta varias mejoras importantes que facilitan aún más el desarrollo de experimentos. OpenSesame 3.3 es totalmente compatible con la versión 3.2.


### Rapunzel: un nuevo editor de código

Rapunzel es un editor de código centrado en el cálculo numérico con Python y R. Técnicamente, Rapunzel es un conjunto de extensiones para OpenSesame. Sin embargo, se ve y se comporta como un programa independiente. ¡Feliz codificación!

- <https://rapunzel.cogsci.nl/>


### Un nuevo editor de inline_script

Relacionado con el desarrollo de Rapunzel: El elemento INLINE_SCRIPT ahora utiliza una biblioteca diferente (`PyQode`) para el editor de código. Como resultado, el editor de código ahora admite muchas de las características que esperarías de un editor de código moderno, incluida la introspección de código y la verificación estática de código.


### Más espacios de color

OpenSesame ahora admite de forma nativa los espacios de color HSV, HSL y CIElab.

- %link:manual/python/canvas%


### Nuevo backend de sonido basado en PsychoPy

El backend predeterminado ahora es *psycho*. Una de las ventajas de este backend es que la temporización de la presentación de sonido debería ser mejor. Si experimenta tartamudeo (reproducción de sonido con clics), aún puede volver al backend *psycho_legacy*, que utiliza el antiguo sistema de sonido basado en PyGame.


### Soporte para elementos de inline_script en coroutines

Ahora puede utilizar elementos `inline_script` en `coroutines`. Esto facilita la combinación de scripts de Python con corutinas, en comparación con el antiguo método de escribir una función generadora personalizada.

- %link:coroutines%



### OpenSesame: 


## Cambios en 3.2

OpenSesame 3.2 presenta varias mejoras importantes que facilitan aún más el desarrollo de experimentos. OpenSesame 3.2 es totalmente compatible con la versión 3.1.


### Una mejor API de Python compatible con PEP-8

PEP-8 es una guía de estilo para Python. Gran parte del software moderno de Python sigue las pautas de PEP-8, pero, por razones históricas, OpenSesame no lo hizo. A partir de 3.2, la API pública ahora sigue la pauta de que los nombres de las clases (y las funciones de fábrica que generan clases) deben ser `CamelCase`, mientras que los nombres de los objetos y funciones deben ser `underscore_case`. En términos prácticos, esto significa que ahora crea objetos `Canvas` de la siguiente manera:

~~~ .python
my_canvas = Canvas() # ¡Fijate en la C mayúscula!
my_canvas.fixdot()
my_canvas.show())
~~~

Por supuesto, los antiguos nombres en `underscore_case` todavía están disponibles como alias, por lo que se mantiene la compatibilidad con versiones anteriores.

La API para formularios también se ha simplificado. Ya no es necesario importar `libopensesame.widgets`, y ya no es necesario pasar `exp` como primer argumento:

~~~ .python
form = Form()
button = Button(text=u'Ok!')
form.set_widget(button, (0, 0))
form._exec()
~~~


### Mejoras en el sketchpad y Canvas

#### Acceso y modificación de elementos del Canvas

Los elementos de un `Canvas` ahora son objetos que se pueden nombrar, acceder y modificar. Esto significa que ya no es necesario volver a dibujar un canvas completo para cambiar un solo elemento. Por ejemplo, puede dibujar un brazo giratorio de la siguiente manera:

~~~ .python
my_canvas = Canvas()
my_canvas['arm'] = Line(0, 0, 0, 0)
for x, y in xy_circle(n=100, rho=100):
    my_canvas['arm'].ex = x
    my_canvas['arm'].ey = y
    my_canvas.show()
    clock.sleep(10)
~~~

SKETCHPAD también permite nombrar elementos.

Para obtener más información, consulte:

- %link:manual/python/canvas%


#### Soporte mejorado para HTML y escritura no latina

El texto ahora es renderizado por Qt, que es una biblioteca moderna (la misma biblioteca que también se utiliza para la interfaz gráfica). Esto significa que ahora puedes usar HTML real en tu texto. Esto también significa que el texto de izquierda a derecha y otros scripts no latinos se representan mucho mejor.


#### Las imágenes se pueden rotar

Las imágenes ahora se pueden rotar. Esto funciona tanto en elementos SKETCHPAD como en objetos `Canvas`.


#### Trabajar con coordenadas polares

Si hace clic derecho en elementos SKETCHPAD, puede seleccionar 'Especificar coordenadas polares'. Esto le permite calcular coordenadas cartesianas (x, y) basadas en coordenadas polares, lo cual es especialmente útil si desea crear configuraciones circulares.

### Mejoras en los formularios

#### Mejora del rendimiento de los formularios

Los formularios ahora son mucho más rápidos al usar los backends *psycho* y *xpyriment*. Esto se debe a que los elementos `Canvas` ahora pueden actualizarse individualmente, como se describe arriba.

#### Validación de entrada de formulario

Ahora puede validar la entrada de un formulario; es decir, puede evitar que un formulario se cierre hasta que se cumplan ciertos criterios. Además, puede excluir caracteres como entrada de los widgets` TextInput`.

Para más información, consulte:

- %link:manual/forms/validation%

### Mejoras en el teclado

#### Soporte para eventos de liberación de teclas

El objeto `Keyboard()` ahora tiene una función `get_key_release()`, que le permite recopilar liberaciones de teclas. Debido a las limitaciones de las bibliotecas subyacentes, la función tiene dos limitaciones importantes:

- La tecla` key` devuelta puede ser incorrecta en teclados que no son QWERTY
- La función no se ha implementado para el backend *psycho*

Para más información, consulte:

- %link:manual/response/keyboard%

### Mejoras en el mouse

#### Soporte para eventos de liberación de clic del mouse

El objeto `Mouse()` ahora tiene una función `get_click_release()`, que le permite recolectar liberaciones de clic del mouse. Esta función actualmente no está implementada para el backend *psycho*.

Para más información, consulte:

- %link:manual/response/mouse%

#### Usar sketchpads para definir regiones de interés

Ahora puede definir un SKETCHPAD vinculado en un elemento de `mouse_response`. Si lo hace, los nombres de los elementos en el SKETCHPAD se utilizarán automáticamente como regiones de interés (ROI) para los clics del mouse.

### Terminar a la fuerza su experimento

Ahora puede terminar a la fuerza su experimento haciendo clic en el botón Kill en la barra de herramientas principal. ¡Esto significa que ya no necesita abrir un administrador de procesos/tareas para finalizar experimentos incontrolados!

### Mejor soporte para Mac OS

Los paquetes de Mac OS han sido reconstruidos desde cero por %-- github: {user: dschreij} --%. La experiencia en Mac OS ahora debería ser mucho más fluida, rápida y con menos bloqueos.

### Traducción al turco

Una traducción completa al turco ha sido aportada por %-- github: {user: aytackarabay} --%. Esto significa que OpenSesame ahora está completamente traducido al francés, alemán y turco. Una traducción parcial está disponible en varios otros idiomas.

## Cambios en la versión 3.1

OpenSesame 3.1 trae muchas mejoras que facilitan aún más el desarrollo de experimentos. OpenSesame 3.1 es totalmente compatible con la versión 3.0.

### ¡Un nuevo aspecto!

OpenSesame tiene un nuevo tema de iconos, basado en [Moka](https://snwh.org/moka) de Sam Hewitt. Además, la interfaz de usuario se ha rediseñado basándose en pautasconsistentes de interfaz humana. ¡Esperamos que le guste el nuevo aspecto tanto como a nosotros!

### Un bucle rediseñado

El LOOP ahora es más fácil de usar y le permite restringir la aleatorización; esto hace posible, por ejemplo, evitar que el mismo estímulo ocurra dos veces seguidas.

Para más información, consulte:

- %link:loop%

### Corrutinas: hacer cosas en paralelo

El complemento COROUTINES ahora está incluido por defecto. COROUTINES le permite ejecutar varios elementos en paralelo; esto hace posible, por ejemplo, recopilar continuamente pulsaciones de teclas mientras se presenta una serie de SKETCHPADs.

Para más información, consulte:

- %link:coroutines%

### Integración con Open Science Framework

Ahora puede iniciar sesión en [Open Science Framework](http://osf.io) (OSF) desde OpenSesame, y sincronizar de forma fácil experimentos y datos entre su computadora y OSF. ¡Gracias al [Centro de Ciencia Abierta](http://cos.io/) por apoyar esta funcionalidad!

Para más información, consulte:

- %link:osf%

### Un objeto de respuestas

Hay un nuevo objeto estándar de Python: `responses`. Lleva un registro de todas las respuestas que se han recopilado durante el experimento.

Para obtener más información, consulte:

- %link:responses%

## Cambios en 3.0

OpenSesame 3.0 ha traído muchas mejoras que facilitan aún más el desarrollo de experimentos. La mayoría de los cambios son compatibles con versiones anteriores. Es decir, aún puede hacer las cosas de la manera antigua. Sin embargo, algunos cambios no son compatibles con versiones anteriores y es importante tenerlos en cuenta.

### Cambios incompatibles con versiones anteriores

#### Propiedades del Sampler

El objeto SAMPLER tiene varias propiedades que antes eran funciones. Esto concierne:

- `sampler.fade_in`
- `sampler.pan`
- `sampler.pitch`
- `sampler.volume`

Para obtener más información, consulte:

- %link:sampler%

#### Colores compatibles con CSS3

Ahora puede usar especificaciones de colores compatibles con CSS3, como se describe aquí:

- %link:manual/python/canvas%

Si utiliza nombres de colores (por ejemplo, 'rojo', 'verde', etc.), esto puede resultar en colores ligeramente diferentes. Por ejemplo, según CSS3, 'verde' es`#008000` en lugar de (como era el caso anteriormente) `#00FF00`.

### Nuevo formato de archivo (.osexp)

OpenSesame ahora guarda los experimentos en formato `.osexp`. Por supuesto, aún puede abrir los formatos antiguos (`.opensesame` y `.opensesame.tar.gz`). Para obtener más información, consulte:

- %link:fileformat%

### API de Python simplificada

#### No más self y exp

Ya no es necesario utilizar el prefijo `self.` o `exp.` al llamar a funciones comúnmente utilizadas. Por ejemplo, esto establecerá programáticamente el número de sujetos en 2:

~~~ .python
set_subject_nr(2)
~~~

Para obtener una lista de funciones comunes, consulte:

- %link:manual/python/common%

#### El objeto `var`: Facilitar la obtención y configuración de variables experimentales

La antigua forma de usar `self.get()` para obtener y `exp.set()` para establecer variables experimentales ha sido reemplazada por una sintaxis más simple. Por ejemplo, para establecer la variable `condition`, de modo que pueda hacer referencia a ella como `[condition]` en los SKETCHPADs, etc.:

~~~ .python
var.condition = 'facil`'
~~~

Y para obtener una variable experimental `condition` que, por ejemplo, se definió en un LOOP:

~~~ .python
print('La condición es %s' % var.condition)
~~~

Para obtener más información, consulte:

- %link:var%

#### El objeto `clock`: Funciones de tiempo

Las funciones de tiempo ahora están disponibles a través del objeto `clock`:

~~~ .python
print('Marca de tiempo actual: %s' % clock.time())
clock.sleep(1000) # Dormir durante 1 s
~~~

Para obtener más información, consulte:

- %link:clock%

#### El objeto `pool`: Acceso al repositorio de archivos

El repositorio de archivos ahora es accesible a través del objeto `pool`, que admite una interfaz similar a `dict` (pero no es realmente un `dict` de Python):

~~~ .python
path = pool['image.png']
print('El camino completo a image.png es: %s' % path)
~~~

Para obtener más información, consulte:

- %link:pool%

#### No más de importación from openexp.* import *

Ya no es necesario importar las clases `openexp` y pasar `exp` como primer argumento. En cambio, para crear un objeto `canvas`, simplemente puede hacer:

~~~ .python
my_canvas = canvas()
~~~

Hay funciones similares de fábrica (como se llaman) para `keyboard`, `mouse` y SAMPLER.

Para obtener más información, consulte:

- %link:manual/python/common%

#### El sintetizador ahora es un sampler

El SYNTH ya no es una clase por sí solo. En cambio, es una función que devuelve un objeto SAMPLER que ha sido llenado con una muestra sintetizada.

### Mejoras en la interfaz de usuario

#### Una ventana de depuración IPython

IPython, un terminal interactivo de Python para computación científica, ahora se usa para la ventana de depuración.

#### Un inspector de variables en vivo

El inspector de variables ahora muestra los valores reales de sus variables mientras su experimento se está ejecutando y después de que su experimento haya finalizado.

#### Deshacer

¡Finalmente puedes deshacer acciones!

#### Un nuevo esquema de colores

El esquema de colores predeterminado ahora es *Monokai*. Nuevamente, un esquema de colores oscuro, pero con un contraste más alto que el predeterminado anterior, *Solarized*. Este aumento debe aumentar la legibilidad. ¡Y se ve bien!

### Coordenadas consistentes

Anteriormente, OpenSesame usaba coordenadas de pantalla mixtas e inconsistentes: `0,0` era la esquina superior izquierda de la pantalla al usar el código Python, y el centro de la pantalla al trabajar en elementos de SKETCHPAD, etc. A partir de la versión 3.0, el centro de la pantalla siempre es `0,0`, también en código Python.

Si desea volver al comportamiento anterior, puede desactivar la opción 'Coordenadas uniformes' en la pestaña general. Para mantener la compatibilidad con versiones anteriores, las 'Coordenadas uniformes' se desactivan automáticamente al abrir un experimento antiguo.

### Usando Python en cadenas de texto

Ahora puede incrustar Python en cadenas de texto utilizando la sintaxis `[=...]`. Por ejemplo, la siguiente cadena de texto en un SKETCHPAD:

~~~
Dos veces dos es igual a [=2*2]
~~~

... mostrará:

~~~
Dos veces dos es igual a 4
~~~

Para obtener más información, consulte:

- %link:text%

### Soporte para Python 3

OpenSesame ahora es compatible con Python >= 3.4. Sin embargo, muchas de las dependencias de OpenSesame, especialmente PsychoPy y Expyriment, son exclusivas de Python 2. Por lo tanto, Python 2.7 sigue siendo la versión predeterminada de Python.