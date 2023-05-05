<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __srbox__

Si insertas el complemento srbox al comienzo de tu experimento, una
instancia de SRBOX automáticamente pasa a formar parte del objeto del experimento
y
puede ser accedido dentro de un elemento de inline_script como SRBOX.

__Nota importante 1:__

Si no especificas un dispositivo, el complemento intentará autodetectar
el
puerto SR Box. Sin embargo, en algunos sistemas esto congela el experimento, por lo
que es mejor especificar explícitamente un dispositivo.

__Nota importante 2:__

Necesitas llamar a [srbox.start] para poner el SR Box en modo de envío,
antes de
llamar a [srbox.get_button_press] para recopilar una pulsación de botón.

__Ejemplo:__
~~~ .python
t0 = clock.time()
srbox.start()
button, t1 = srbox.get_button_press(allowed_buttons=[1, 2],
                                    require_state_change=True)
if button == 1:
    response_time = t1 - t0
print(f'¡El botón 1 fue presionado en {response_time} ms!')
srbox.stop()
~~~
[TOC]

## get_button_press(allowed_buttons=None, timeout=None, require_state_change=False)

Recopila una pulsación de botón desde el SR box.


__Parámetros__

- **allowed_buttons**: Una lista de botones que son aceptados o `None` para aceptar todos
los botones. Los botones válidos son enteros del 1 al 8.
- **timeout**: Un valor de tiempo de espera en milisegundos o `None` para no establecer un tiempo de espera.
- **require_state_change    Indica si se debe aceptar un botón ya presionado**: (False), o si se acepta solo un cambio de estado de no presionado a presionado
(True).

__Devuelve__

- Una tupla `(button_list, timestamp)`. La `button_list` es `None` si no se 
ha pulsado ningún botón (es decir, ocurrió un tiempo de espera).


## send(ch)

Envía un único caracter al SR Box. Envía '`' para apagar todas
las luces, 'a' para encender la luz 1, 'b' para la luz 2 encendida, 'c' para las luces
1 y 2 encendidas, etc.


__Parámetros__

- **ch**: El caracter a enviar. Si se pasa un `str`, se codifica en
`bytes` utilizando la codificación utf-8.


## start(self)

Activa el modo de envío, de modo que el SR Box comienza a enviar la salida.
El SR Box debe estar en modo de envío cuando llamas a
[srbox.get_button_press].




## stop(self)

Desactiva el modo de envío, de modo que el SR Box deja de dar salida.




</div>