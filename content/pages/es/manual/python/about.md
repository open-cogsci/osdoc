title: Acerca de Python
hash: 99b67bfe88b7ad764c9bc1c2a5da5b4114e573e6c0e442ff7f88dc080051e6b2
locale: es
language: Spanish

En OpenSesame puedes crear experimentos complejos utilizando solo la interfaz gráfica de usuario (GUI). Pero a veces te encontrarás con situaciones en las que la funcionalidad proporcionada por la GUI es insuficiente. En estos casos, puedes agregar código Python a tu experimento.

Python no es compatible con experimentos en línea con OSWeb. Si necesitas ejecutar tu experimento en línea, debes usar [JavaScript](%url:manual/javascript/about%) en su lugar.

[TOC]

## Aprendiendo Python

Puedes encontrar un conjunto de tutoriales básicos y ejercicios para comenzar con Python en <https://pythontutorials.eu/>.

## Python en la GUI de OpenSesame

### Un único espacio de trabajo Python

Todo el código Python se ejecuta en un único espacio de trabajo Python. Esto significa que las variables que se han definido en un INLINE_SCRIPT son accesibles en todos los otros INLINE_SCRIPTs, así como en las declaraciones de Python que están incrustadas en las declaraciones de ejecución si (run-if) y en cadenas de texto. El mismo principio se aplica a los módulos: una vez que se `import`an, están disponibles en todas partes.

Por ejemplo, puedes construir simplemente el `Canvas` en un INLINE_SCRIPT ...

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
~~~

... y mostrarlo en otro INLINE_SCRIPT ...

~~~ .python
my_canvas.show()
~~~

### Elementos Inline_script

Para usar código Python, debes agregar un elemento INLINE_SCRIPT a tu experimento. Puedes hacer esto arrastrando el icono de Python (el ícono azul/amarillo) desde la barra de herramientas de elementos en la secuencia del experimento. Después de hacer esto, verás algo como %FigInlineScript.

%--
figure:
 id: FigInlineScript
 source: inline-script.png
 caption: El elemento INLINE_SCRIPT.
--%

Como puedes ver, el elemento INLINE_SCRIPT consta de dos pestañas: una para la fase de Preparación (Prepare) y otra para la fase de Ejecución (Run). La fase de Preparación se ejecuta primero, para permitir que los elementos se preparen para la fase de ejecución crítica por tiempo. Es una buena práctica construir objetos `Canvas`, objetos `Sampler`, etc. durante la fase de Preparación, de modo que puedan presentarse sin demora durante la fase de Ejecución. Pero esto es solo una convención; puedes ejecutar código Python arbitrario durante ambas fases.

Para obtener más información sobre la estrategia de preparación-ejecución, consulta:

- %link:prepare-run%

### Expresiones condicionales ("if")

Puedes usar expresiones de Python de una sola línea en expresiones condicionales. Por ejemplo, puedes usar el siguiente código de Python como una expresión de ejecución si (run-if) (ver también %FigRunIf):

~~~ .python
correct == 1 and response_time < 1000
~~~

%--
figure:
 id: FigRunIf
 source: run-if.png
 caption: Usar el código de Python en la declaración de ejecución si (run-if) de un elemento SEQUENCE.
--%

Para obtener más información sobre las expresiones condicionales ("if"), consulta:

- %link:manual/variables%

### Python en cadenas de texto

Puedes incrustar declaraciones de Python en cadenas de texto usando la sintaxis {...}. Esto funciona para referencias de variables simples, así como para expresiones de una sola línea. Por ejemplo, podrías agregar el siguiente texto en un SKETCHPAD:

```text
La resolución es {width} x {height} px, lo que es un total de {width * height} píxeles
```

Dependiendo de la resolución de tu experimento, esto podría evaluarse como:

```text
La resolución es 1024 x 768 px, lo que es un total de 786432 píxeles
```

Para obtener más información sobre variables y texto, consulta:

- %link:manual/variables%
- %link:manual/stimuli/text%

### La consola de Jupyter (ventana de depuración)

OpenSesame redirige la salida estándar a la consola (o ventana de depuración), que puedes activar utilizando Control + D o a través del menú (Menú -> Ver -> Mostrar ventana de depuración; ver %FigDebugNormal). Puedes imprimir en la consola usando `print()`.

~~~ .python
print('¡Esto aparecerá en la ventana de depuración!')
~~~

La consola también es un intérprete interactivo de Python impulsado por [project Jupyter](https://jupyter.org).

## Cosas que debes saber

### Funciones comunes

Muchas funciones comunes están disponibles directamente en un elemento INLINE_SCRIPT, sin necesidad de importar nada. Por ejemplo:

~~~ .python
# `Canvas()` es una función de fábrica que devuelve un objeto `Canvas`
fixdot_canvas = Canvas()
if sometimes(): # A veces el fixdot es verde
    fixdot_canvas.fixdot(color='green')
else: # A veces es rojo
    fixdot_canvas.fixdot(color='red')
fixdot_canvas.show()
~~~

Para obtener una lista de funciones comunes, consulte:

- %link:manual/python/common%


### El objeto `var`: acceso a las variables experimentales

__Nota de versión__ A partir de OpenSesame 4.0, todas las variables experimentales están disponibles como globales. Esto significa que ya no necesita el objeto `var`.
{:.page-notification}

Puede acceder a las variables experimentales a través del objeto `var`:

~~~ .python
# Obtener una variable experimental
print('my_variable es: %s' % var.my_variable)
# Establecer una variable experimental
var.my_variable = 'my_value'
~~~

Una descripción completa del objeto `var` se puede encontrar aquí:

- %link:manual/python/var%


### El objeto `clock`: funciones de tiempo

Las funciones básicas de tiempo están disponibles a través del objeto `clock`:

~~~ .python
# Obtener la marca de tiempo actual
t = clock.time()
# Esperar 1 s
clock.sleep(1000)
~~~

Una descripción completa del objeto `clock` se puede encontrar aquí:

- %link:manual/python/clock%


### El objeto `log`: registro de datos

El registro de datos está disponible a través del objeto `log`:

~~~ .python
# Escribir una línea de texto
log.write('Mi mensaje de registro personalizado')
# Escribir todas las variables
log.write_vars()
~~~

Una descripción completa del objeto `log` se puede encontrar aquí:

- %link:manual/python/log%


### El objeto `pool`: acceso al grupo de archivos

Puede obtener la ruta completa a un archivo en el grupo de archivos a través del objeto `pool`:

~~~ .python
# Mostrar una imagen del grupo de archivos
path = pool['img.png']
my_canvas = Canvas()
my_canvas.image(path)
my_canvas.show()
~~~

Una descripción completa del objeto `pool` se puede encontrar aquí:

- %link:manual/python/pool%


### El objeto `responses`: acceso a las respuestas de los participantes

El objeto `responses` realiza un seguimiento de todas las respuestas de los participantes que se han recopilado durante el experimento. Por ejemplo, para enumerar la corrección de todas las respuestas hasta ahora:

~~~ .python
for response in responses:
	print(response.correct)
~~~

Una descripción completa del objeto `responses` se puede encontrar aquí:

- %link:manual/python/responses%


### La clase `Canvas`: presentación de estímulos visuales

La clase `Canvas` se utiliza para presentar estímulos visuales. Por ejemplo, puede mostrar un punto de fijación de la siguiente manera:

~~~ .python
my_canvas = Canvas()
my_canvas.fixdot()
my_canvas.show()
~~~

Una descripción completa de la clase `Canvas` se puede encontrar aquí:

- %link:manual/python/canvas%


### La clase `Keyboard`: recopilación de pulsaciones de teclas

La clase `Keyboard` se utiliza para recopilar pulsaciones de teclas. Por ejemplo, para recopilar una pulsación de tecla con un tiempo de espera de 1000 ms:

~~~ .python
my_keyboard = Keyboard(timeout=1000)
key, time = my_keyboard.get_key()
~~~

Una descripción completa de la clase `Keyboard` se puede encontrar aquí:

- %link:manual/python/keyboard%


### La clase `Mouse`: recopilación de clics del mouse y toques en la pantalla

La clase `Mouse` se utiliza para recopilar clics del mouse y toques en la pantalla. (OpenSesame no hace distinción entre los dos.) Por ejemplo, para recopilar un clic del mouse con un tiempo de espera de 1000 ms:

~~~ .python
my_mouse = Mouse(timeout=1000)
button, position, time = my_mouse.get_click()
~~~

Una descripción completa de la clase `Mouse` se puede encontrar aquí:

- %link:manual/python/mouse%


### La clase `Sampler`: reproducción de sonido

La clase `Sampler` se utiliza para reproducir muestras de sonido. Por ejemplo, para reproducir un simple pitido:

~~~ .python
my_sampler = Sampler()
my_sampler.play()
~~~

Una descripción completa de la clase `Sampler` se puede encontrar aquí:

- %link:manual/python/sampler%


## Módulos alternativos para la presentación de pantalla, recopilación de respuestas, etc.


### `psychopy`

Si está utilizando el backend *psycho*, puede utilizar directamente los diversos módulos de [PsychoPy]. Para obtener más información, consulte:

- %link:backends%


### `expyriment`

Si está utilizando el backend *xpyriment*, puede utilizar directamente los diversos módulos de [Expyriment]. Para obtener más información, consulte:

- %link:backends%

### `pygame`

Si está utilizando el backend *legacy*, *droid* o *xpyriment* (solo con "Usar OpenGL" establecido en "no"), puede usar directamente los diversos módulos de [PyGame]. Para obtener más información, consulte:

- %link:backends%


[python]: http://www.python.org/
[backends]: /backends/about-backends
[ipython]: http://ipython.org/
[swaroop]: http://www.swaroopch.com/notes/Python
[swaroop-direct]: http://www.ibiblio.org/swaroopch/byteofpython/files/120/byteofpython_120.pdf
[downey]: http://www.greenteapress.com/thinkpython/
[downey-direct]: http://www.greenteapress.com/thinkpython/thinkpython.pdf
[opensesamerun]: /usage/opensesamerun/
[psychopy]: http://www.psychopy.org/
[expyriment]: http://www.expyriment.org/
[pygame]: http://www.pygame.org/