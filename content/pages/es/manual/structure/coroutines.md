title: Haciendo cosas en paralelo
hash: 355690924feb930d7fef825b28269bb20c28adb8e20b8c2a86de761222d40d95
locale: es
language: Spanish

Las corrutinas ejecutan múltiples elementos en paralelo, o para ser más exactos, ejecutan elementos en rápida alternancia de una manera que parece paralela. No todos los elementos admiten corrutinas.

[TOC]

## Usando corrutinas

Puedes usar corrutinas a través del complemento COROUTINES (ver %FigCoroutinesInterface).

%--
figure:
 source: FigCoroutinesInterface.png
 caption: La interfaz del complemento de corrutinas.
 id: FigCoroutinesInterface
--%

Como puedes ver, el complemento COROUTINES se parece al elemento SEQUENCE, pero tiene algunas opciones adicionales:

- *Duration* indica la duración total de las corrutinas.
- *End after item (optional)* indica que las corrutinas deben finalizar cuando un elemento específico haya terminado. Esto te permite, por ejemplo, indicar que las corrutinas deben terminar cuando se haya recopilado una pulsación de tecla, seleccionando un elemento KEYBOARD_RESPONSE aquí.
- Cada elemento tiene un *Start time*. La mayoría de los elementos también tienen un *End time*. El tiempo de finalización no se aplica a los elementos de una sola vez; por ejemplo, los SKETCHPAD muestran una pantalla y finalizan de inmediato, por lo que no tienen tiempo de finalización.

Específicamente, el ejemplo de %FigCoroutinesInterface (del ejemplo de tarea stop-signal) hace lo siguiente:

- Muestra una pantalla de objetivo de inmediato.
- Si la variable `stop_after` no está vacía, muestra la pantalla de stop_signal después de un intervalo especificado por la variable `stop_after`.
- Durante todo el intervalo (2000 ms), se recopila una respuesta de teclado.

El flujo temporal está controlado por el complemento COROUTINES. Por lo tanto, no se utilizan los valores de tiempo de espera y duración especificados en los elementos. Por ejemplo, en %FigCoroutinesInterface, el KEYBOARD_RESPONSE se ejecutará durante 2000 ms, independientemente del tiempo de espera especificado en el elemento.

## Elementos compatibles

Actualmente, los siguientes elementos son compatibles (esta lista puede no ser exhaustiva):

- FEEDBACK
- INLINE_SCRIPT
- KEYBOARD_RESPONSE
- LOGGER
- MOUSE_RESPONSE
- SAMPLER
- SYNTH
- SKETCHPAD

## Usando elementos inline_script en corrutinas

Cuando utilizas un elemento INLINE_SCRIPT en una COROUTINES, la fase Run funciona de manera un poco diferente de lo que podrías estar acostumbrado. Específicamente, la fase Run se ejecuta en cada iteración de las COROUTINES. Además, la fase Run debe contener solo código que tarde muy poco tiempo en ejecutarse; esto se debe a que las operaciones que consumen mucho tiempo bloquearán las COROUTINES, interfiriendo así con el tiempo de otros elementos en las COROUTINES. Para finalizar las COROUTINES, puedes generar una excepción `AbortCoroutines()`.

Por ejemplo, supongamos que tienes una COROUTINES con dos elementos KEYBOARD_RESPONSE, *kb1* y *kb2*, y deseas ejecutar las COROUTINES hasta que se hayan recopilado dos pulsaciones de tecla, con un tiempo de espera de 5000 ms. Entonces podrías crear la siguiente estructura de COROUTINES:

%--
figure:
 source: FigCoroutinesTwoResponses.png
 caption: Un corrutinas que recopila dos respuestas de pulsación de tecla
 id: FigCoroutinesTwoResponses
--%

El INLINE_SCRIPT *check_responses* primero establecería ambas variables de respuesta en una cadena vacía en la fase Prepare:

```python
# Esto se ejecuta al comienzo de las corrutinas
response_kb1 = ''
response_kb2 = ''
```

Y luego, en la fase Run, verifica si ambas variables han sido establecidas y aborta las corrutinas si ese es el caso:

```python
# Los valores que no son una cadena vacía son True para Python
# ¡Este código se ejecutará muchas veces!
if response_kb1 and response_kb2:
    raise AbortCoroutines()
```

## Expresiones Run-if

El comportamiento de las expresiones run-if en COROUTINES es un poco diferente al de los elementos SEQUENCE. Específicamente, las expresiones run-if en COROUTINES se evalúan durante la fase de preparación. Consulta también:

- %link:prepare-run%