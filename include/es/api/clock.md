<div class="ClassDoc YAMLDoc" markdown="1">

# instancia __clock__

El objeto `clock` ofrece funciones básicas de tiempo. Se crea automáticamente un objeto de `clock` cuando comienza el experimento.

__Ejemplo__

~~~ .python
# Obtén la marca de tiempo antes y después de dormir durante 1000 ms
t0 = clock.time()
clock.sleep(1000)
t1 = clock.time()
tiempo_transcurrido = t1 - t0
print(f'Esto debería ser 1000: {tiempo_transcurrido}')
~~~

[TOC]

## loop_for(ms, throttle=None, t0=None)

*Nuevo en v3.2.0*

Un iterador que crea ciclos por un tiempo fijo.

__Parámetros__

- **ms**: La cantidad de milisegundos para hacer un ciclo.
- **throttle**: Un período para dormir entre cada iteración.
- **t0**: Un tiempo de inicio. Si es `None`, el tiempo de inicio es el momento en que comienza la iteración.

__Devuelve__

- 

__Ejemplo__

~~~ .python
for ms in clock.loop_for(100, throttle=10):
    print(ms)
~~~



## once_in_a_while(ms=1000)

*Nuevo en v3.2.0*

Periódicamente devuelve `True`. Esto es útil principalmente para ejecutar código (por ejemplo, dentro de un bucle `for`) que solo debe ejecutarse de vez en cuando.

__Parámetros__

- **ms**: El período mínimo de espera.

__Devuelve__

- `True` después de que, al menos, haya pasado el período mínimo de espera desde la última llamada a `Clock.once_in_a_while()`, o `False` en caso contrario.

__Ejemplo__

~~~ .python
for i in range(1000000):
    if clock.once_in_a_while(ms=50):
        # Ejecuta este código solo una vez cada 50 ms
        print(clock.time())
~~~



## sleep(ms)

Duerme (hace una pausa) por un período.

__Parámetros__

- **ms**: La cantidad de milisegundos para dormir.

__Ejemplo__

~~~ .python
# Crea dos objetos canvas ...
mi_canvas1 = Canvas()
mi_canvas1.text('1')
mi_canvas2 = Canvas()
mi_canvas2.text('2')
# ... y muéstralos con 1 s de por medio
mi_canvas1.show()
clock.sleep(1000)
mi_canvas2.show()
~~~



## time()

Proporciona una marca de tiempo actual en milisegundos. El significado absoluto de la marca de tiempo (es decir, cuándo era 0) depende del backend.

__Devuelve__

- Una marca de tiempo.

__Ejemplo__

~~~ .python
t = clock.time()
print(f'El tiempo actual es {t}')
~~~



</div>