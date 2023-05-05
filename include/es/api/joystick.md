<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __joystick__

Si inserta el complemento JOYSTICK al inicio de su experimento, un
objeto JOYSTICK automáticamente se convierte en parte del objeto de experimento
y se puede utilizar dentro de un artículo INLINE_SCRIPT como `joystick`.

{% set arg_joybuttonlist = "Una lista de botones que se aceptan o " +
"`None` para aceptar todos los botones." %}
{% set arg_timeout = "Un valor de tiempo de espera en milisegundos o `None` para no " +
"tiempo de espera." %}

[TOC]

## flush(self)

Borra toda la entrada pendiente, no limitado al joystick.



__Devuelve__

- Verdadero si estaba pendiente la entrada del joystick (es decir, si había algo que
vaciar) y Falso en caso contrario.


## get_joyaxes(timeout=None)

Espera el movimiento de los ejes del joystick.


__Parámetros__

- **timeout**: Un valor de tiempo de espera en milisegundos o `None` para usar el tiempo de espera predeterminado.

__Devuelve__

- Una tupla `(posición, marca de tiempo)`. `posición` es `None` si se produce un tiempo de espera.
De lo contrario, `posición` es una tupla `(x, y, z)`.


## get_joyballs(timeout=None)

Espera el movimiento de la bola de seguimiento del joystick.


__Parámetros__

- **timeout**: Un valor de tiempo de espera en milisegundos o `None` para usar el tiempo de espera predeterminado.

__Devuelve__

- Una tupla `(posición, marca de tiempo)`. La posición es `None` si se produce un tiempo de espera.


## get_joybutton(joybuttonlist=None, timeout=None)

Recopila la entrada del botón del joystick.


__Parámetros__

- **joybuttonlist**: Una lista de botones que se aceptan o `None` para la lista predeterminada.
- **timeout**: Un valor de tiempo de espera en milisegundos o `None` para usar el tiempo de espera predeterminado.

__Devuelve__

- Una tupla (joybutton, timestamp). El joybutton es `None` si se produce un
tiempo de espera.


## get_joyhats(timeout=None)

Espera el movimiento del sombrero del joystick.


__Parámetros__

- **timeout**: Un valor de tiempo de espera en milisegundos o `None` para usar el tiempo de espera predeterminado.

__Devuelve__

- Una tupla `(posición, marca de tiempo)`. `posición` es `None` si se produce un timeout
de lo contrario, `posición` es una tupla `(x, y)`.


## get_joyinput(joybuttonlist=None, timeout=None)

Espera cualquier entrada de joystick (botones, ejes, sombreros o pelotas).


__Parámetros__

- **joybuttonlist**: Una lista de botones que se aceptan o `None` para la lista predeterminada.
- **timeout**: Un valor de tiempo de espera en milisegundos o `None` para usar el tiempo de espera predeterminado.

__Devuelve__

- Una tupla (evento, valor, marca de tiempo). El valor es `None` si se produce un tiempo de espera
de lo contrario, `evento` es uno de `None`, 'joybuttonpress',
'joyballmotion', 'joyaxismotion', o 'joyhatmotion'


## input_options(self)

Genera una lista con el número de botones, ejes, bolas
y sombreros disponibles.



__Devuelve__

- Una lista con el número de entradas como: [botones, ejes, bolas,
sombreros].


## set_joybuttonlist(joybuttonlist=None)

Establece una lista de botones aceptados.


__Parámetros__

- **joybuttonlist**: {{arg_joybuttonlist}}


## set_timeout(timeout=None)

Establece un tiempo de espera.


__Parámetros__

- **timeout**: {{arg_timeout}}


</div>