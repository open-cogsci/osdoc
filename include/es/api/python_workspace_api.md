<div class="ClassDoc YAMLDoc" markdown="1">

## Canvas(auto_prepare=True, \*\*style_args)

Una función de fábrica que crea un nuevo objeto `Canvas`. Para una
descripción de las posibles palabras clave, consulte:

- %link:manual/python/canvas%


__Devuelve__

- Un objeto `Canvas`.

__Ejemplo__

~~~ .python
my_canvas = Canvas(color=u'red', penwidth=2)
my_canvas.line(-10, -10, 10, 10)
my_canvas.line(-10, 10, 10, -10)
my_canvas.show()
~~~



## Experiment(osexp_path=None, log_path='defaultlog.csv', fullscreen=False, subject_nr=0, \*\*kwargs)

Una función de fábrica que crea un nuevo objeto `Experiment`. Esto es solo
útil al implementar un experimento completamente a través de un script Python,
en lugar de a través de la interfaz de usuario.


__Parámetros__

- **osexp_path**: Si se especifica una ruta a un archivo `.osexp`, este archivo se abrirá y
se puede ejecutar directamente llamando a `Experiment.run()`. Si no se especifica ningún archivo
de experimento, se inicializa un experimento vacío.
- **log_path**: 
- **fullscreen**: 
- **subject_nr**: 
- **kwargs**: Argumentos opcionales de palabras clave que se interpretan como variables experimentales.
Un uso principal de esto es especificar el backend a través de
la palabra clave `canvas_backend`.

__Devuelve__

- Una tupla (exp, win, clock, log) que corresponde a los objetos Experiment,
manipulador de ventana (específico del backend), Clock y Log.

__Ejemplo__

Para implementar un experimento completamente programáticamente:

~~~ .python
from libopensesame.python_workspace_api import (
    Experiment, Canvas, Text, Keyboard)
exp, win, clock, log = Experiment(canvas_backend='legacy')
c = Canvas()
c += Text('Presione cualquier tecla')
c.show()
kb = Keyboard()
kb.get_key()
exp.end()
~~~

Para cargar un archivo de experimento y ejecutarlo:

~~~ .python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
~~~



## Form(\*args, \*\*kwargs)

Una función de fábrica que crea un nuevo objeto `Form`. Para una
descripción
de las posibles palabras clave, consulte:

- %link:manual/forms/widgets%


__Devuelve__

- Un objeto `Form`.

__Ejemplo__

~~~ .python
form = Form()
label = Label(text='etiqueta')
button = Button(text='Aceptar')
form.set_widget(label, (0,0))
form.set_widget(button, (0,1))
form._exec()
~~~



## Keyboard(\*\*resp_args)

Una función de fábrica que crea un nuevo objeto `Keyboard`. Para una
descripción de las posibles palabras clave, consulte:

- %link:manual/python/keyboard%


__Devuelve__

- Un objeto `Keyboard`.

__Ejemplo__

~~~ .python
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key, time = my_keyboard.get_key()
~~~



## Mouse(\*\*resp_args)

Una función de fábrica que crea un nuevo objeto `Mouse`. Para una
descripción
de las posibles palabras clave, consulte:

- %link:manual/python/mouse%


__Devuelve__

- Un objeto `mouse`.

__Ejemplo__

~~~ .python
my_mouse = Mouse(keylist=[1,3], timeout=5000)
button, time = my_mouse.get_button()
~~~



## Sampler(src, \*\*playback_args)

Una función de fábrica que crea un nuevo objeto `Sampler`. Para una
descripción de las posibles palabras clave, consulte:

- %link:manual/python/sampler%


__Devuelve__

- Un objeto SAMPLER.

__Ejemplo__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~



## Synth(osc='sine', freq=440, length=100, attack=0, decay=5)

Una función de fábrica que sintetiza un sonido y lo devuelve como un
objeto `Sampler`.


__Parámetros__

- **osc**: Oscilador, puede ser "sine", "saw", "square" o "white_noise".
- **freq**: Frecuencia, ya sea un valor entero (valor en hercios) o una cadena ("A1",
"eb2", etc.).
- **length**: La duración del sonido en milisegundos.
- **attack**: El tiempo de ataque (fade-in) en milisegundos.
- **decay**: El tiempo de decaimiento (fade-out) en milisegundos.

__Devuelve__

- Un objeto SAMPLER.

__Ejemplo__

~~~ .python
my_sampler = Synth(freq=u'b2', length=500)
~~~



## copy_sketchpad(name)

Devuelve una copia del lienzo de un `sketchpad`.


__Parámetros__

- **name**: El nombre del `sketchpad`.

__Devuelve__

- Una copia del lienzo del `sketchpad`.

__Ejemplo__

~~~ .python
my_canvas = copy_sketchpad('my_sketchpad')
my_canvas.show()
~~~

## pause()

Pausa el experimento.

## register_cleanup_function(fnc)

Registra una función de limpieza, que se ejecuta cuando el experimento
termina. Las funciones de limpieza se ejecutan al final, después de cerrar la pantalla,
dispositivo de sonido y archivo de registro. Las funciones de limpieza también
se ejecutan cuando el experimento se bloquea.

__Ejemplo__

~~~ .python
def my_cleanup_function():
        print(u'¡El experimento ha terminado!')
register_cleanup_function(my_cleanup_function)
~~~

## reset_feedback()

Reinicia todas las variables de retroalimentación a su estado inicial.

__Ejemplo__

~~~ .python
reset_feedback()
~~~

## set_subject_nr(nr)

Establece el número de sujeto y paridad (par / impar). Esta función es llamada
automáticamente cuando se inicia un experimento, por lo que solo necesita llamarlo
usted mismo si sobrescribe el número de sujeto que se especificó cuando se
lanzó el experimento.

__Parámetros__

- **nr**: El número de sujeto.

__Ejemplo__

~~~ .python
set_subject_nr(1)
print('Núm. de sujeto = %d' % var.subject_nr)
print('Paridad del sujeto = %s' % var.subject_parity)
~~~

## sometimes(p=0.5)

Devuelve True con cierta probabilidad. (Para una aleatorización más avanzada, use el módulo `random` de Python).

__Parámetros__

- **p**: La probabilidad de devolver True.

__Devuelve__

- Verdadero o falso

__Ejemplo__

~~~ .python
if sometimes():
        print('A veces ganas')
else:
        print('A veces pierdes')
~~~

## xy_circle(n, rho, phi0=0, pole=(0, 0))

Genera una lista de puntos (coordenadas x, y) en un círculo. Esto puede ser
utilizado para dibujar estímulos en una disposición circular.

__Parámetros__

- **n**: La cantidad de coordenadas x, y a generar.
- **rho**: La coordenada radial, también distancia o excentricidad, del primer
punto.
- **phi0**: La coordenada angular para la primera coordenada. Esta es una
rotación antihoraria en grados (es decir, no en radianes), donde 0 es
directamente a la derecha.
- **pole**: El punto de referencia.

__Devuelve__

- Una lista de tuplas de coordenadas (x, y).

__Ejemplo__

~~~ .python
# Dibujar 8 rectángulos alrededor de un punto central de fijación
c = Canvas()
c.fixdot()
for x, y in xy_circle(8, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

## xy_distance(x1, y1, x2, y2)

Da la distancia entre dos puntos.

__Parámetros__

- **x1**: La coordenada x del primer punto.
- **y1**: La coordenada y del primer punto.
- **x2**: La coordenada x del segundo punto.
- **y2**: La coordenada y del segundo punto.

__Devuelve__

- La distancia entre los dos puntos.

## xy_from_polar(rho, phi, pole=(0, 0))

Convierte coordenadas polares (distancia, ángulo) en coordenadas cartesianas
(x, y).

__Parámetros__

- **rho**: La coordenada radial, también distancia o excentricidad.
- **phi**: La coordenada angular. Esto refleja una rotación en sentido horario en grados
(es decir, no en radianes), donde 0 es directamente a la derecha.
- **pole**: El punto de referencia.

__Devuelve__

- Una tupla de coordenadas (x, y).

__Ejemplo__

~~~ .python
# Dibujar una cruz
x1, y1 = xy_from_polar(100, 45)
x2, y2 = xy_from_polar(100, -45)
c = Canvas()
c.line(x1, y1, -x1, -y1)
c.line(x2, y2, -x2, -y2)
c.show()
~~~

## xy_grid(n, spacing, pole=(0, 0))

Genera una lista de puntos (coordenadas x, y) en una cuadrícula. Esto puede ser
utilizado para dibujar estímulos en una disposición de cuadrícula.

__Parámetros__

- **n**: Un `int` que indica el número de columnas y filas, de modo que `n=2`
indica una cuadrícula 2x2, o una tupla (n_col, n_row), de modo que `n=(2,3)`
indica una cuadrícula 2x3.
- **spacing**: Un valor numérico que indica el espacio entre celdas, o un
tupla (col_spacing, row_spacing).
- **pole**: El punto de referencia.

__Devuelve__

- Una lista de tuplas de coordenadas (x, y).

__Ejemplo__

~~~ .python
# Dibujar una cuadrícula 4x4 de rectángulos
c = Canvas()
c.fixdot()
for x, y in xy_grid(4, 100):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

## xy_random(n, width, height, min_dist=0, pole=(0, 0))

Genera una lista de puntos aleatorios (coordenadas x, y) con un mínimo
espaciamiento entre cada par de puntos. Esta función generará una
Excepción cuando la lista de coordenadas no pueda generarse, típicamente porque
hay demasiados puntos, la min_dist está establecida demasiado alta, o el ancho o la altura están establecidos demasiado bajos.

__Parámetros__

- **n**: El número de puntos a generar.
- **width**: El ancho del campo con puntos aleatorios.
- **height**: La altura del campo con puntos aleatorios.
- **min_dist**: La distancia mínima entre cada punto.
- **pole**: El punto de referencia.

__Devuelve__

- Una lista de tuplas de coordenadas (x, y).

__Ejemplo__

~~~ .python
# Dibuja 50 rectángulos en una cuadrícula aleatoria
c = Canvas()
c.fixdot()
for x, y in xy_random(50, 500, 500, min_dist=40):
        c.rect(x-10, y-10, 20, 20)
c.show()
~~~

## xy_to_polar(x, y, pole=(0, 0))

Convierte coordenadas Cartesianas (x, y) en coordenadas polares (distancia,
ángulo).

__Parámetros__

- **x**: La coordenada X.
- **y**: La coordenada Y.
- **pole**: El punto de referencia.

__Devuelve**

- Una tupla de coordenadas (rho, phi). Aquí, `rho` es la coordenada radial,
también distancia o excentricidad. `phi` es la coordenada angular en
grados (es decir, no radianes) y refleja una rotación antihoraria,
donde 0 está completamente a la derecha.

__Ejemplo__

~~~ .python
rho, phi = xy_to_polar(100, 100)
~~~

</div>