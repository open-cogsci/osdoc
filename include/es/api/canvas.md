<div class="ClassDoc YAMLDoc" markdown="1">

# clase __Canvas__

{% set arg_max_width = "El ancho máximo del texto en píxeles, " +
"antes de ajustar a una nueva línea, o `None` para ajustar al borde de la pantalla." %}

{% set arg_bgmode = "Especifica si el fondo es el promedio de " +
"col1 y col2 ('avg', correspondiente a un parche de Gabor típico), o " + 
"igual a col2 ('col2'), útil para mezclar con el fondo. Nota: " +
"este parámetro es ignorado por el backend psycho, que utiliza un aumento de " + 
"transparencia para el fondo." %}

{% set arg_style = "Palabras clave de [estilo opcional](#style-keywords) que " + 
"especifican el estilo de la operación de dibujo actual. Esto no " + 
"afecta las operaciones de dibujo posteriores." %}

{% set arg_center = "Un bool que indica si las coordenadas reflejan " + 
"el centro (`True`) o la parte superior izquierda (`False`) del texto." %}

La clase `Canvas` se utiliza para presentar estímulos visuales. Generalmente se crea un
objeto `Canvas` con la función de fábrica `Canvas()`, como se describe en la sección
[Crear un Canvas](#creating-a-canvas).

__Ejemplo__:

~~~ .python
# Crea y muestra un lienzo con un punto de fijación central
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

__Ejemplo__:

También puede agregar elementos de `Canvas` como objetos. Ver también la sección sobre [Nombrar,
acceder y modificar elementos](#naming-accessing-and-modifying-elements).

~~~ .python
# Crea un lienzo con un punto de fijación y un rectángulo
my_canvas = Canvas()
my_canvas['my_fixdot'] = FixDot()
my_canvas.show()
~~~

[TOC]

## Cosas a saber

### Crear un Canvas

Por lo general, crea un `Canvas` con la función de fábrica `Canvas()`:

~~~ .python
my_canvas = Canvas()
~~~

Opcionalmente, puede pasar [Palabras clave de estilo](#style-keywords) a `Canvas()` para configurar
el estilo predeterminado:

~~~ .python
my_canvas = Canvas(color='verde')
my_canvas.fixdot() # Será verde
~~~

### Palabras clave de estilo

Todas las funciones que aceptan `**style_args` toman los siguientes argumentos de palabras clave:

- `color` especifica el color de primer plano. Para especificaciones de color válidas, ver
  [colores](#colors).
- `background_color` especifica el color de fondo. Para especificaciones de color válidas, ver [colores](#colors).
- `fill` indica si los rectángulos, círculos, polígonos y elipses están
  llenos (`True`) o dibujados como un contorno (`False`).
- `penwidth` indica un ancho de pluma en píxeles y debe ser `int` o `float`.
- `html` indica si se interpretan las etiquetas HTML y debe ser `True` o
  `False`.
- `font_family` es el nombre de una familia de fuentes, como 'sans'.
- `font_size` es un tamaño de fuente en píxeles.
- `font_italic` indica si el texto debe ser en cursiva y debe ser `True` o
  `False`.
- `font_bold` indica si el texto debe ser en negrita y debe ser `True` o
  `False`.
- `font_underline` indica si el texto debe ser subrayado y debe ser
  `True` o `False`.

~~~ .python
# Dibujar un punto de fijación verde
my_canvas = Canvas()
my_canvas.fixdot(color='verde')
my_canvas.show()
~~~

Las palabras clave de estilo solo afectan la operación de dibujo actual (excepto cuando se pasa a
`Canvas()` al crear el `Canvas`). Para cambiar el estilo de todas las operaciones de dibujo posteriores, establecer propiedades de estilo, como `canvas.color`, directamente:

~~~ .python
# Dibujar una cruz roja con un ancho de pluma de 2px
my_canvas = Canvas()
my_canvas.color = 'rojo'
my_canvas.penwidth = 2
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

O pase las propiedades de estilo a `Canvas()`:

~~~ .python
# Dibujar una cruz roja con un ancho de pluma de 2px
my_canvas = Canvas(color='rojo', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~

### Colores

Puede especificar colores de las siguientes maneras. Esto incluye especificaciones de color tipo CSS3, pero también admite algunas especificaciones adicionales, como el espacio de color CIE l* a* b*.

__Nota de versión:__ Los espacios de color `hsv`, `hsl` y `lab` son nuevos en la v3.3.0.

- __Nombres de colores:__ 'red', 'black', etc. Una lista completa de nombres de colores válidos se puede
  encontrar [aquí](http://www.w3.org/TR/SVG11/types.html#ColorKeywords).
- __Cadenas hexadecimales de siete caracteres:__ `#FF0000`, `#000000`, etc. Aquí,
  los valores van desde `00` hasta `FF`, de modo que `#FF0000` es rojo brillante.
- __Cadenas hexadecimales de cuatro caracteres:__ `#F00`, `#000`, etc. Aquí, los valores
  van desde '0' hasta 'F' de modo que `#F00` es rojo brillante.
- __Cadenas RGB:__ `rgb(255,0,0)`, `rgb(0,0,0)`, etc. Aquí, los valores van desde
  0 hasta 255 de modo que `rgb(255,0,0)` es rojo brillante.
- __Cadenas de porcentaje RGB:__ `rgb(100%,0%,0%)`, `rgb(0%,0%,0%)`, etc. Aquí,
  los valores van desde 0% hasta 100% de modo que `rgb(100%,0%,0%)` es rojo brillante.
- __Tuplas RGB:__ `(255, 0, 0)`, `(0, 0 ,0)`, etc. Aquí, los valores van desde `0`
  hasta `255` de modo que `(255,0,0)` es rojo brillante.
- __Cadenas HSV:__ `hsv(120, 100%, 100%)`. En el espacio de color [HSV](https://en.wikipedia.org/
  wiki/HSL_and_HSV), el parámetro de tono es un ángulo de 0 a 359,
  y los parámetros de saturación y valor son porcentajes de 0% a 100%.
- __Cadenas HSL:__ `hsl(120, 100%, 50%)`. En el espacio de color [HSL](https://en.wikipedia.org/
  wiki/HSL_and_HSV), el parámetro de tono es un ángulo de 0 a 359,
  y los parámetros de saturación y luminosidad son porcentajes de 0% a 100%.
- __Cadenas LAB:__ `lab(53, -20, 0)`. En el espacio de color [CIELAB](https://en.wikipedia.org/
  wiki/CIELAB_color_space), los parámetros reflejan luminosidad (`l*`),
  eje verde-rojo (`a*`, negativo es verde) y eje azul-amarillo (`b*`, negativo
  es azul). Esto utiliza el punto blanco D65 y la función de transferencia sRGB, como
  se implementa [aquí](https://www.psychopy.org/_modules/psychopy/tools/
  colorspacetools.html).
- __Valores de luminancia:__  `255`, `0`, etc. Aquí, los valores van desde `0` hasta `255`
  de modo que `255` es blanco.

~~~ .python
# Varias formas de especificar verde
my_canvas.fixdot(color='green')  # Verde oscuro
my_canvas.fixdot(color='#00ff00')
my_canvas.fixdot(color='#0f0')
my_canvas.fixdot(color='rgb(0, 255, 0)')
my_canvas.fixdot(color='rgb(0%, 100%, 0%)')
my_canvas.fixdot(color='hsl(100, 100%, 50%)')
my_canvas.fixdot(color='hsv(0, 100%, 100%)')
my_canvas.fixdot(color='lab(53, -20, 0)')  # Verde oscuro
my_canvas.fixdot(color=(0, 255, 0))  # Especificar un valor de luminancia (blanco)
~~~

### Nombrar, acceder y modificar elementos

A partir de OpenSesame 3.2, el `Canvas` admite una interfaz basada en objetos que permite
nombrar elementos, y acceder y modificar elementos individualmente, sin
tener que redibujar todo el `Canvas`.

Por ejemplo, lo siguiente agregará un elemento `Line` rojo a un `Canvas`
y lo mostrará, luego cambiará el color de la línea a verde y lo mostrará nuevamente,
y luego eliminará la línea y mostrará el canvas nuevamente (que ahora está en blanco).
El nombre del elemento (`my_line`) se utiliza para referirse al elemento para todas las
operaciones.

~~~ .python
my_canvas = Canvas()
my_canvas['my_line'] = Line(-100, -100, 100, 100, color='red')
my_canvas.show()
clock.sleep(1000)
my_canvas['my_line'].color = 'green'
my_canvas.show()
clock.sleep(1000)
del my_canvas['my_line']
my_canvas.show()
~~~

También puede agregar un elemento sin proporcionar explícitamente un nombre para él. En ese
caso, se genera automáticamente un nombre (por ejemplo, `stim0`).

~~~ .python
my_canvas = Canvas()
my_canvas += FixDot()
my_canvas.show()
~~~

Si agrega una lista de elementos, se agruparán automáticamente, y
puede referirse al grupo entero por nombre.

~~~ .python
my_canvas = Canvas()
my_canvas['my_cross'] = [    Line(-100, 0, 100, 0),    Line(0, -100, 0, 100)]
my_canvas.show()
~~~

Para verificar si una coordenada `x,y` particular cae dentro del rectángulo delimitador
de un elemento, puede usar `in`:

~~~ .python
my_mouse = Mouse(visible=True)
my_canvas = Canvas()
my_canvas['rect'] = Rect(-100, -100, 200, 200)
my_canvas.show()
button, (x, y), time = my_mouse.get_click()
if (x, y) in my_canvas['rect']:
    print('Hizo clic en el rectángulo')
else:
    print('Hizo clic fuera del rectángulo')
~~~

También puede obtener una lista de los nombres de todos los elementos que contienen una coordenada `x, y`
utilizando la función `Canvas.elements_at()`, documentada a continuación.

## arrow(sx, sy, ex, ey, body_length=0.8, body_width=0.5, head_width=30, \*\*style_args)

Dibuja una flecha. Una flecha es un polígono que consta de 7 vértices,
con una punta de flecha apuntando a (ex, ey).

__Parámetros__

- **sx**: La coordenada X de la base de la flecha.
- **sy**: La coordenada Y de la base de la flecha.
- **ex**: La coordenada X de la punta de la flecha.
- **ey**: La coordenada Y de la punta de la flecha.
- **body_length**: Longitud proporcional del cuerpo de la flecha en relación con la flecha completa
[0-1].
- **body_width**: Ancho (grosor) proporcional del cuerpo de la flecha en relación con la
flecha completa [0-1].
- **head_width**: Ancho (grosor) de la cabeza de la flecha en píxeles.

## circle(x, y, r, \*\*style_args)

Dibuja un círculo.

__Parámetros__

- **x**: La coordenada X central del círculo.
- **y**: La coordenada Y central del círculo.
- **r**: El radio del círculo.
- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.circle(100, 100, 50, fill=True, color='red')
# Interfaz de elemento
my_canvas['my_circle'] = Circle(100, 100, 50, fill=True, color='red')
~~~

## clear(\*arglist, \*\*kwdict)

Limpia el lienzo con el color de fondo actual. Tenga en cuenta que
generalmente es más rápido utilizar un lienzo diferente para cada pantalla experimental que usar un solo lienzo y borrarlo y volver a dibujarlo repetidamente.

__Parámetros__

- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(color='green')
my_canvas.show()
clock.sleep(1000)
my_canvas.clear()
my_canvas.fixdot(color='red')
my_canvas.show()
~~~

## copy(canvas)

Convierte el `Canvas` actual en una copia del `Canvas` pasado.

__Advertencia:__

Copiar objetos `Canvas` puede resultar en un comportamiento impredecible. En muchos
casos, una mejor solución es recrear varios objetos `Canvas` desde
cero, y / o usar la interfaz de elementos para actualizar los elementos de `Canvas`
individualmente.

__Parámetros__

- **canvas**: El `Canvas` a copiar.

__Ejemplo__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot(x=100, color='green')
my_copied_canvas = Canvas()
my_copied_canvas.copy(my_canvas)
my_copied_canvas.fixdot(x=200, color="blue")
my_copied_canvas.show()
~~~

## elements_at(x, y)

*Nuevo en v3.2.0*

Obtiene los nombres de los elementos que contienen un
coordenada `x, y` particular.

__Parámetros__

- **x**: Una coordenada X.
- **y**: Una coordenada Y.

__Devuelve__

- Una `lista` de nombres de elementos que contienen la coordenada `x, y`.

__Ejemplo__

~~~ .python
# Crear y mostrar un lienzo con dos rectángulos parcialmente superpuestos
my_canvas = Canvas()
my_canvas['right_rect'] = Rect(x=-200, y=-100, w=200, h=200, color='red')
my_canvas['left_rect'] = Rect(x=-100, y=-100, w=200, h=200, color='green')
my_canvas.show()
# Recoger un clic del mouse e imprimir los nombres de los elementos que
# contienen el punto en el que se hizo clic
my_mouse = Mouse(visible=True)
button, pos, time = my_mouse.get_click()
if pos is not None:
    x, y = pos
    print('Hizo clic en los elementos: %s' % my_canvas.elements_at(x, y))
~~~

## ellipse(x, y, w, h, \*\*style_args)

Dibuja una elipse.

__Parámetros__

- **x**: La coordenada X izquierda.
- **y**: La coordenada Y superior.
- **w**: El ancho.
- **h**: La altura.
- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.ellipse(-10, -10, 20, 20, fill=True)
# Interfaz de elemento
my_canvas['my_ellipse'] = Ellipse(-10, -10, 20, 20, fill=True)
~~~

## fixdot(x=None, y=None, style='default', \*\*style_args)

Dibuja un punto de fijación. El estilo predeterminado es de tamaño medio y abierto.

- 'large-filled' es un círculo lleno con un radio de 16px.
- 'medium-filled' es un
círculo lleno con un radio de 8px.
- 'small-filled' es un círculo lleno
con un radio de 4px.
- 'large-open' es un círculo lleno con un radio de 16px
y un agujero de 2px.
- 'medium-open' es un círculo lleno con un radio de 8px
y un agujero de 2px.
- 'small-open' es un círculo lleno con un radio de 4px y
un agujero de 2px.
- 'large-cross' es una cruz de 16px.
- 'medium-cross' es una cruz de 8px
.
- 'small-cross' es una cruz de 4px.

__Parámetros__

- **x**: La coordenada X del centro del punto, o None para dibujar un punto centrado horizontalmente.
- **y**: La coordenada Y del centro del punto, o None para dibujar un punto centrado verticalmente.
- **style**: El estilo del punto de fijación. Uno de: default, large-filled,
medium-
filled, small-filled, large-open, medium-open,
small-open, large-
cross, medium-cross, o small-cross.
default es igual a medium-open.
- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.fixdot()
# Interfaz de elemento
my_canvas['my_fixdot'] = FixDot()
~~~



## gabor(x, y, orient, freq, env='gaussian', size=96, stdev=12, phase=0, col1='white', col2='black', bgmode='avg')

Dibuja un parche Gabor. Nota: La representación exacta del parche Gabor
depende del back-end.


__Parámetros__

- **x**: La coordenada X central.
- **y**: La coordenada Y central.
- **orient**: Orientación en grados [0 .. 360]. Esto se refiere a una
rotación en sentido horario desde una vertical.
- **freq**: Frecuencia en ciclos/px del sinusoidal.
- **env**: El sobre que determina la forma del parche. Puede ser
"gaussian", "linear", "circular" o "rectangular".
- **size**: Un tamaño en píxeles.
- **stdev**: Desviación estándar en píxeles del gaussiano. Solo aplicable a
sobres gaussianos.
- **phase**: Fase del sinusoidal [0.0 .. 1.0].
- **col1**: Un color para los picos.
- **col2**: Un color para los valles. Nota: El back-end psico
ignora este
parámetro y siempre usa el inverso de
`col1` para los valles.
- **bgmode**: {{arg_bgmode}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.gabor(100, 100, 45, .05)
# Interfaz de elemento
my_canvas['my_gabor'] = Gabor(100, 100, 45, .05)
~~~



## image(fname, center=True, x=None, y=None, scale=None, rotation=None)

Dibuja una imagen desde un archivo. Esta función no busca en el archivo
pool, sino que toma una ruta absoluta.


__Parámetros__

- **fname**: El nombre del archivo de la imagen. Al usar Python 2, esto debe ser
ya sea `unicode` o un `str` codificado en utf-8. Al usar Python 3,
esto debe ser `str` o un `bytes` codificados en utf-8.
- **center**: Un bool que indica si las coordenadas indican el centro (True) o
la parte superior izquierda (False).
- **x**: La coordenada X, o `None` para dibujar una imagen centrada horizontalmente.
- **y**: La coordenada Y, o `None` para dibujar una imagen centrada verticalmente.
- **scale**: El factor de escala de la imagen. `None` o 1 indica el tamaño original
. 2.0 indica un zoom del 200%, etc.
- **rotation**: La rotación de la imagen `None` o 0 indica la rotación original
. Los valores positivos indican una rotación en sentido horario en grados.

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Determine la ruta absoluta:
path = exp.pool['image_in_pool.png']
# Interfaz de función
my_canvas.image(path)
# Interfaz de elemento
my_canvas['my_image'] = Image(path)
~~~



## line(sx, sy, ex, ey, \*\*style_args)

Dibuja una línea.


__Parámetros__

- **sx**: La coordenada X izquierda.
- **sy**: La coordenada Y superior.
- **ex**: La coordenada X derecha.
- **ey**: La coordenada Y inferior.
- **\*\*style_args**: {{arg_style}}


## lower_to_bottom(element)

Baja un elemento al fondo, de modo que se lo dibuje primero; es
decir, se convierte en el fondo.


__Parámetros__

- **element**: Un elemento SKETCHPAD, o su nombre.


## noise_patch(x, y, env='gaussian', size=96, stdev=12, col1='white', col2='black', bgmode='avg')

Dibuja un parche de ruido, con un sobre. La representación exacta del
parche de ruido depende del back-end.


__Parámetros__

- **x**: La coordenada X central.
- **y**: La coordenada Y central.
- **env**: El sobre que determina la forma de la zona. Puede ser
"gaussian", "linear", "circular" o "rectangular".
- **size**: Un tamaño en píxeles.
- **stdev**: Desviación estándar en píxeles de la gaussiana. Solo aplicable a
sobres gaussianos.
- **col1**: El primer color.
- **col2**: El segundo color. Nota: El back-end psycho ignora este
parámetro
y siempre utiliza el inverso de `col1`.
- **bgmode**: {{arg_bgmode}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.noise_patch(100, 100, env='circular')
# Interfaz de elemento
my_canvas['my_noise_patch'] = NoisePatch(100, 100, env='circular')
~~~



## polygon(vertices, \*\*style_args)

Dibuja un polígono definido por una lista de vértices. Es decir, una forma de
puntos conectados por líneas.


__Parámetros__

- **vertices**: Una lista de tuplas, donde cada tupla corresponde a un vértice. Para
ejemplo, [(100,100), (200,100), (100,200)] dibujará un triángulo.
- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
n1 = 0,0
n2 = 100, 100
n3 = 0, 100
# Interfaz de función
my_canvas.polygon([n1, n2, n3])
# Interfaz de elemento
my_canvas['my_polygon'] = Polygon([n1, n2, n3])
~~~



## prepare(self)

Termina las operaciones pendientes del lienzo (si las hay), para que una llamada posterior
a [canvas.show] sea extra rápida. Solo es necesario llamar a esta
función si ha desactivado `auto_prepare` al inicializar el
`Canvas`.




## raise_to_top(element)

Eleva un elemento a la parte superior, para que se dibuje al final; es decir, se
convierte en el primer plano.


__Parámetros__

- **element**: Un elemento SKETCHPAD, o su nombre.


## rect(x, y, w, h, \*\*style_args)

Dibuja un rectángulo.


__Parámetros__

- **x**: La coordenada X izquierda.
- **y**: La coordenada Y superior.
- **w**: El ancho.
- **h**: La altura.
- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.rect(-10, -10, 20, 20, fill=True)
# Interfaz de elemento
my_canvas['my_rect'] = Rect(-10, -10, 20, 20, fill=True)
~~~



## rename_element(old_name, new_name)

Cambia el nombre de un elemento.




## show(self)

Muestra, o 'voltea', el lienzo en la pantalla.



__Devuelve__

- Una marca de tiempo del momento en que el lienzo apareció en
la pantalla, o una mejor suposición si no está disponible información temporal precisa. Para obtener más información sobre el tiempo, consulte </misc/timing>.
Dependiendo del back-end, el sello de tiempo es un `int` o un `float`.

__Ejemplo__

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
t = my_canvas.show()
exp.set('time_fixdot', t)
~~~



## text(text, center=True, x=None, y=None, max_width=None, \*\*style_args)

Dibuja texto.


__Parámetros__

- **text**: Una cadena de texto. Al usar Python 2, debe ser `unicode` o una cadena `str` codificada en utf-8. Al usar Python 3, debe ser `str` o `bytes` codificadas en utf-8.
- **center**: {{arg_center}}
- **x**: La coordenada X, o None para dibujar texto centrado horizontalmente.
- **y**: La coordenada Y, o None para dibujar texto centrado verticalmente.
- **max_width**: {{arg_max_width}}
- **\*\*style_args**: {{arg_style}}

__Ejemplo__

~~~ .python
my_canvas = Canvas()
# Interfaz de función
my_canvas.text('Algun texto con <b>negrita</b> e <i>cursiva</i>')
# Interfaz de elemento
my_canvas['my_text'] = Text('Algun texto con <b>negrita</b> e <i>cursiva</i>')
~~~



## text_size(text, center=True, max_width=None, \*\*style_args)

Determina el tamaño de una cadena de texto en píxeles.


__Parámetros__

- **text**: Una cadena de texto.
- **center**: {{arg_center}}
- **max_width**: {{arg_max_width}}
- **\*\*style_args**: {{arg_style}}

__Devuelve__

- Una tupla (ancho, alto) que contiene las dimensiones de la cadena de texto
.

__Ejemplo__

~~~ .python
my_canvas = Canvas()
w, h = my_canvas.text_size('Algun texto')
~~~



</div>