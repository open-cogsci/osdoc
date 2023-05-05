<div class="ClassDoc YAMLDoc" markdown="1">

# clase __Mouse__

La clase `Mouse` se utiliza para recopilar la entrada del mouse. Generalmente, se crea un objeto
`Mouse` con la función de fábrica `Mouse()`, como se describe en la sección [Crear un Mouse](#creating-a-mouse).

__Ejemplo__

~~~ .python
# Dibujar un 'punto de fijación del cursor del mouse' hasta que se haga clic en un botón
mi_mouse = Mouse()
mi_canvas = Canvas()
while True:
    boton, posicion, marca_temporal = mi_mouse.get_click(timeout=20)
    if boton is not None:
        break
    (x,y), tiempo = mi_mouse.get_pos()
    mi_canvas.clear()
    mi_canvas.fixdot(x, y)
    mi_canvas.show()
~~~

[TOC]

## Cosas que debes saber

### Crear un Mouse

Generalmente, se crea un `Mouse` con la función de fábrica `Mouse()`:

~~~ .python
mi_mouse = Mouse()
~~~

Opcionalmente, puedes pasar [Palabras clave de respuesta](#response-keywords) a `Mouse()`
para establecer el comportamiento predeterminado:

~~~ .python
mi_mouse = Mouse(timeout=2000)
~~~

### Coordenadas

- Cuando *Coordenadas uniformes* está configurado en 'sí', las coordenadas son relativas al
  centro de la pantalla. Es decir, (0,0) es el centro. Este es el predeterminado a partir de
  OpenSesame 3.0.0.
- Cuando *Coordenadas uniformes* está configurado en 'no', las coordenadas son relativas a la
  parte superior izquierda de la pantalla. Es decir, (0,0) es la parte superior izquierda. Este fue el predeterminado en
  OpenSesame 2.9.X y versiones anteriores.

### Números de botón

Los botones del mouse están numerados de la siguiente manera:

1. Botón izquierdo
2. Botón central
3. Botón derecho
4. Desplazar hacia arriba
5. Desplazar hacia abajo

### Pantallas táctiles

Al trabajar con una pantalla táctil, un toque se registra como el botón 1
(botón izquierdo).

### Palabras clave de respuesta

Las funciones que aceptan `**resp_args` toman los siguientes argumentos de palabras clave:

- `timeout` especifica un valor de tiempo de espera en milisegundos, o se establece en `None` para
  desactivar el tiempo de espera.
- `buttonlist` especifica una lista de botones que se aceptan, o se establece en
  `None` aceptar todos los botones.
- `visible` indica si el cursor del mouse se vuelve visible cuando se recopila un clic (`True` o `False`). Para cambiar inmediatamente la visibilidad del cursor, use
  `Mouse.show_cursor()`.

~~~ .python
# Obtener un clic izquierdo o derecho con un tiempo de espera de 3000 ms
mi_mouse = Mouse()
botón, tiempo = mi_mouse.get_click(buttonlist=[1,3], timeout=3000)
~~~

Las palabras clave de respuesta solo afectan la operación actual (excepto cuando se pasan a
`Mouse()` al crear el objeto). Para cambiar el comportamiento de todas las operaciones posteriores, establezca las propiedades de respuesta directamente:

~~~ .python
# Obtener dos clics izquierdos o derechos con un tiempo de espera de 5000 ms
mi_mouse = Mouse()
mi_mouse.buttonlist = [1,3]
mi_mouse.timeout = 5000
boton1, tiempo1 = mi_mouse.get_click()
boton2, tiempo2 = mi_mouse.get_click()
~~~

O pase las palabras clave de respuesta a `Mouse()` al crear el objeto:

~~~ .python
# Obtener dos clics izquierdos o derechos con un tiempo de espera de 5000 ms
mi_mouse = Mouse(buttonlist=[1,3], timeout=5000)
boton1, tiempo1 = mi_mouse.get_click()
boton2, tiempo2 = mi_mouse.get_click()
~~~

## flush(self)

Limpia toda la entrada pendiente, no limitada al mouse.

__Devuelve__

- Verdadero si se había hecho clic en un botón (es decir, si había algo que
vaciar) y Falso en caso contrario.

__Ejemplo__

~~~ .python
mi_mouse = Mouse()
mi_mouse.flush()
boton, posicion, marca_temporal = mi_mouse.get_click()
~~~


## get_click(\*arglist, \*\*kwdict)

Recopila un clic del mouse.

__Parámetros__

- **\*\*resp_args**: Opcional [palabras clave de respuesta](#response-keywords) que se utilizarán
para esta llamada a `Mouse.get_click()`. Esto no afecta
las operaciones posteriores.

__Devuelve__

- Una tupla (botón, posición, marca_temporal). El botón y la posición son
`None` si ocurre un tiempo de espera. La posición es una tupla (x, y) en
coordenadas de pantalla.

__Ejemplo__

~~~ .python
mi_mouse = Mouse()
boton, (x, y), marca_temporal = mi_mouse.get_click(timeout=5000)
if boton is None:
        print('¡Ocurrió un tiempo de espera!')
~~~


## get_click_release(\*arglist, \*\*kwdict)

*Nuevo en v3.2.0*

Recopila una liberación de clic del mouse.

*Importante:* Esta
función actualmente no está implementada en el
backend *psycho*.

__Parámetros__

- **\*\*resp_args**: Opcional [palabras clave de respuesta](#response-keywords) que serán utilizadas
para esta llamada a `Mouse.get_click_release()`. Esto no afecta
operaciones posteriores.

__Devuelve__

- Una tupla (botón, posición, marca de tiempo). El botón y la posición son
`None` si ocurre un tiempo de espera. La posición es una tupla (x, y) en
coordenadas de pantalla.

__Ejemplo__

~~~ .python
my_mouse = Mouse()
boton, (x, y), marca_de_tiempo = my_mouse.get_click_release(timeout=5000)
if button is None:
        print('¡Ocurrió un tiempo de espera!')
~~~



## get_pos(self)

Devuelve la posición actual del cursor.

__Devuelve__

- Una tupla (posición, marca de tiempo).

__Ejemplo__

~~~ .python
my_mouse = Mouse()
(x, y), marca_de_tiempo = my_mouse.get_pos()
print('El cursor estaba en (%d, %d)' % (x, y))
~~~



## get_pressed(self)

Devuelve el estado actual de los botones del ratón. Un valor Verdadero significa
que el botón está siendo presionado actualmente.

__Devuelve__

- Una tupla de valores booleanos (botón1, botón2, botón3).

__Ejemplo__

~~~ .python
my_mouse = Mouse()
botones = my_mouse.get_pressed()
b1, b2, b3 = botones
print('Botones del ratón presionados actualmente: (%d,%d,%d)' % (b1,b2,b3))
~~~



## set_pos(pos=(0, 0))

Establece la posición del cursor del ratón.

__Advertencia:__ `set_pos()` es
poco confiable y fallará silenciosamente en
algunos sistemas.

__Parámetros__

- **pos**: Una tupla (x, y) para las nuevas coordenadas del ratón.

__Ejemplo__

~~~ .python
my_mouse = Mouse()
my_mouse.set_pos(pos=(0,0))
~~~



## show_cursor(show=True)

Cambia inmediatamente la visibilidad del cursor del ratón.

__Nota:__
En la mayoría de los casos, querrás utilizar la palabra clave `visible`,
la cual
cambia la visibilidad durante la recopilación de respuestas,
es decir, mientras
`mouse.get_click()` es llamado. Llamar a
`show_cursor()` no cambiará
implícitamente el valor de `visible`,
lo cual puede llevar a un
comportamiento algo no intuitivo de que el cursor
se oculte tan pronto como
`get_click()` es llamado.

__Parámetros__

- **show**: Indica si el cursor se muestra (Verdadero) u oculto (Falso).


## synonyms(button)

Proporciona una lista de sinónimos para un botón del ratón. Por ejemplo, 1 y
'left_button' son sinónimos.

__Parámetros__

- **button**: Un valor de botón.

__Devuelve__

- Una lista de sinónimos.


</div>
