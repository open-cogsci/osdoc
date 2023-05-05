<div class="ClassDoc YAMLDoc" markdown="1">

# clase __Keyboard__

La clase `Keyboard` se utiliza para recopilar respuestas del teclado. Generalmente, creas
un objeto `Keyboard` con la función de fábrica `Keyboard ()`, como se describe en la
sección [Creando un Keyboard](#creando-un-teclado).

__Ejemplo__

~~~ .python
# Espera una tecla 'z' o 'x' con un tiempo de espera de 3000 ms
my_keyboard = Keyboard(keylist=['z', 'x'], timeout=3000)
start_time = clock.time()
key, end_time = my_keyboard.get_key()
response = key
response_time = end_time - start_time
~~~

[TOC]

## Cosas a saber

### Creando un Keyboard

Por lo general, creas un `Keyboard` con la función de fábrica `Keyboard()`:

~~~ .python
my_keyboard = Keyboard()
~~~

Opcionalmente, puedes pasar [Palabras clave de respuesta](#palabras-clave-de-respuesta) a `Keyboard()`
para establecer el comportamiento predeterminado:

~~~ .python
my_keyboard = Keyboard(timeout=2000)
~~~

### Nombres de teclas

- Los nombres de las teclas pueden variar entre los backends.
- Las teclas se pueden identificar por carácter o nombre y no distinguen entre mayúsculas y minúsculas.
  Por ejemplo:
  - La tecla 'a' está representada por 'a' y 'A'
  - La flecha hacia arriba está representada por 'up' y 'UP'
  - La tecla '/' está representada por '/', 'slash' y 'SLASH'
  - La barra espaciadora está representada por 'space' y 'SPACE'
- Para averiguar el nombre de la tecla, puedes:
  - Haz clic en el botón 'listar teclas disponibles' del elemento KEYBOARD_RESPONSE.
  - Recopila una pulsación de tecla con un elemento KEYBOARD_RESPONSE, y muestra el nombre de la tecla
    a través de un elemento FEEDBACK con el texto 'Presionaste [response]' en él.

### Palabras clave de respuesta

Las funciones que aceptan `**resp_args` toman los siguientes argumentos de palabras clave:

- `timeout` especifica un valor de tiempo de espera en milisegundos, o se establece en `None` para
  desactivar el tiempo de espera.
- `keylist` especifica una lista de teclas que se aceptan, o se establece en `None`
  para aceptar todas las teclas.

~~~ .python
# Obtén una pulsación de flecha izquierda o derecha con un tiempo de espera de 3000 ms
my_keyboard = Keyboard()
key, time = my_keyboard.get_key(keylist=[u'left', u'right'], timeout=3000)
~~~

Las palabras clave de respuesta solo afectan la operación actual (excepto cuando se pasan a
`Keyboard()`). Para cambiar el comportamiento para todos los posteriores
operaciones, establezca las propiedades de respuesta directamente:

~~~ .python
# Obtén dos pulsaciones de teclas A o B con un tiempo de espera de 5000 ms
my_keyboard = Keyboard()
my_keyboard.keylist = [u'a', u'b']
my_keyboard.timeout = 5000
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

O pasa las opciones de respuesta a [keyboard.__init__][__init__]:

~~~ .python
# Obtén dos pulsaciones de teclas A o B con un tiempo de espera de 5000 ms
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

## flush(self)

Borra toda la entrada de teclado pendiente, no limitada al teclado.



__Devuelve__

- Verdadero si se había presionado una tecla (es decir, si había algo que
drenar) y Falso en caso contrario.


## get_key(\*arglist, \*\*kwdict)

Recopila una sola pulsación de tecla.


__Parámetros__

- **\*\*resp_args**: Opcional [palabras clave de respuesta](#palabras-clave-de-respuesta) (`timeout` y
`keylist`) que se utilizará para esta llamada a `Keyboard.get_key()`.
Esto no afecta las operaciones posteriores.

__Devuelve__

- Una tupla `(clave, marca de tiempo)`. `clave` es None si se produce un tiempo de espera.

__Ejemplo__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key(timeout=5000)
if response is None:
        print(u'¡Se produjo un tiempo de espera!')
~~~



## get_key_release(\*arglist, \*\*kwdict)

*Nuevo en v3.2.0*

Recopila una sola liberación de tecla.

*Importante:* Este
función actualmente asume un diseño de teclado QWERTY
(unlike
`Keyboard.get_key()`). Esto significa que la tecla devuelta puede ser
incorrecto en los diseños de teclado no QWERTY. Además,
esta función no
está implementado para el backend *psycho*.

__Parámetros__

- **\*\*resp_args**: Opcional [palabras clave de respuesta](#palabras-clave-de-respuesta) (`timeout` y
`keylist`) que se utilizará para esta llamada a
`Keyboard.get_key_release()`. Esto no afecta las operaciones posteriores.

__Devuelve__

- Una tupla `(key, timestamp)`. `key` es None si ocurre un tiempo de espera.

__Ejemplo__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key_release(timeout=5000)
if response is None:
        print(u'¡Ocurrió un tiempo de espera!')
~~~



## get_mods(self)

Devuelve una lista de moderadores de teclado (p. ej., shift, alt, etc.) que
están actualmente presionados.



__Returns__

- Una lista de moderadores de teclado. Se devuelve una lista vacía si no
se presionan moderadores.

__Ejemplo__

~~~ .python
my_keyboard = Keyboard()
moderators = my_keyboard.get_mods()
if u'shift' in moderators:
        print(u'¡La tecla shift está presionada!')
~~~



## show_virtual_keyboard(visible=True)

Muestra u oculta un teclado virtual si esto es compatible con el
back-end. Esta función solo es necesaria si desea que el teclado virtual permanezca visible mientras se recopilan respuestas de varios caracteres. De lo contrario, `Keyboard.get_key()` mostrará y
ocultará implícitamente el teclado para una respuesta de un solo carácter.

Esta función no hace nada para los back-ends que no admiten teclados virtuales.

__Parámetros__

- **visible**: Verdadero si se debe mostrar el teclado, Falso en caso contrario.

__Ejemplo__

~~~ .python
my_keyboard = Keyboard()
my_keyboard.show_virtual_keyboard(True)
response1, timestamp2 = my_keyboard.get_key()
response2, timestamp2 = my_keyboard.get_key()
my_keyboard.show_virtual_keyboard(False)
~~~



## synonyms(key)

Proporciona una lista de sinónimos para una tecla, ya sea códigos o nombres. Los sinónimos
incluyen todas las variables como tipos y como cadenas Unicode (si corresponde).



__Returns__

- Una lista de sinónimos


## valid_keys(self)

Intenta adivinar qué nombres de teclas son aceptados por el back-end. Para
uso interno.



__Returns__

- Una lista de nombres de teclas válidos.


</div>
