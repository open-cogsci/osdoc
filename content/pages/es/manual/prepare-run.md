title: La estrategia de preparación-ejecución
hash: e91e8e57fbac78eb05547ef89cd9bbb3ae1f177e7d96e295fb31c6e7da95965d
locale: es
language: Spanish

[TOC]

## Acerca de

Los experimentos generalmente consisten en intervalos cortos ('ensayos') durante los cuales los participantes perciben estímulos y realizan una tarea. El tiempo debe ser controlado durante un ensayo, pero cierta variación impredecible en la duración del intervalo entre ensayos es aceptable. Por lo tanto, una buena estrategia es realizar tareas que consumen tiempo antes de un ensayo y mantener al mínimo las operaciones que se realizan durante un ensayo.

OpenSesame hace esto llamando a cada elemento de un elemento SEQUENCE dos veces. Esta es la *estrategia de preparación-ejecución*:

- Durante la fase de Preparación, se les da la oportunidad a los elementos de prepararse. Por ejemplo, un SYNTH genera un sonido (pero no lo reproduce) y un SKETCHPAD dibuja un lienzo (pero no lo muestra).
- Durante la fase de Ejecución, los elementos hacen lo menos posible. Por ejemplo, un SYNTH reproduce un sonido preparado previamente y un SKETCHPAD muestra un lienzo preparado previamente.

Esto reduce el riesgo de errores de sincronización. La estrategia de preparación-ejecución se implementa a nivel de elementos SEQUENCE, que típicamente contiene las partes críticas en tiempo de un experimento. Esto significa que antes de que se inicie un SEQUENCE, hay cierta fluctuación temporal impredecible.

## Notas específicas de elementos

### Elementos loop

Un elemento LOOP no se prepara con anticipación. Es importante tener en cuenta esto al usar un LOOP para implementar partes críticas en tiempo. Por ejemplo, es posible que te sientas tentado a implementar un flujo RSVP usando un elemento LOOP de la siguiente manera:

~~~text
rsvp_loop elemento (4 ciclos)
- elemento_estimulo
~~~

En esta construcción, *elemento_estimulo* se preparará y ejecutará cuatro veces en alternancia, de la siguiente manera:

~~~text
preparar elemento_estimulo
ejecutar elemento_estimulo
preparar elemento_estimulo
ejecutar elemento_estimulo
preparar elemento_estimulo
ejecutar elemento_estimulo
preparar elemento_estimulo
ejecutar elemento_estimulo
~~~

Por lo tanto, debes verificar que la preparación de *elemento_estimulo* no cause fallas en la sincronización.

### Elementos sequence

Todos los elementos que forman parte de un SEQUENCE se preparan con anticipación. Por lo tanto, la siguiente construcción...

~~~text
secuencia_prueba
- sketchpad_fijacion
- sketchpad_objetivo
- respuesta_teclado
- registrador
~~~

... se ejecutará de la siguiente manera...

~~~text
preparar sketchpad_fijacion
preparar sketchpad_objetivo
preparar respuesta_teclado
preparar registrador
ejecutar sketchpad_fijacion
ejecutar sketchpad_objetivo
ejecutar respuesta_teclado
ejecutar registrador
~~~

### Elementos sketchpad y feedback

Los elementos SKETCHPAD y FEEDBACK difieren en cuándo se preparan. Para los SKETCHPAD, la preparación ocurre durante la fase de Preparación; para los elementos FEEDBACK, la preparación ocurre solo durante la fase de Ejecución.

Para obtener más información, consulte:

- %link:manual/stimuli/visual%

### Elementos synth y sampler

Para los elementos SYNTH y SAMPLER, el sonido se genera y precarga durante la fase de Preparación.

### Elementos inline_script

En un elemento INLINE_SCRIPT, puedes elegir cómo deseas implementar la estrategia de preparación y ejecución. En general, es una buena práctica seguir las siguientes pautas:

- La funcionalidad de preparación que consume tiempo va en la fase de Preparación. Por ejemplo, crear objetos de lienzo y generar sonidos.
- Se coloca una cantidad mínima de código en la fase de ejecución. Por ejemplo, solo mostrar un lienzo previamente preparado.

### Otros elementos y plugins

En general, los elementos deben seguir el principio de realizar la mayor cantidad posible de preparación que consume tiempo durante la fase de Preparación y minimizar la fase de Ejecución. Sin embargo, cada complemento se implementa de manera diferente. Si tiene dudas sobre un caso específico, publique una consulta en el foro.

## Expresiones condicionales (run if, show if, break if, etc.)

En los elementos SEQUENCE, la condición 'Run if' se evalúa en el último momento, durante la fase de ejecución. Por lo tanto, puedes usar una condición como `correct == 0` que depende de los resultados de un elemento KEYBOARD_RESPONSE que se ha llamado justo antes. Es importante tener en cuenta que la expresión 'Run if' se aplica *solo* a la fase de ejecución de un elemento: la fase de preparación siempre se ejecuta.

En los elementos COROUTINES, la condición "Run if" se evalúa durante la fase de Preparación. Por lo tanto, las condiciones no pueden depender de eventos que ocurran durante la ejecución de los COROUTINES.

En los elementos SKETCHPAD, la condición "Show if" se evalúa durante la fase de Preparación, cuando se construye el lienzo. En los elementos FEEDBACK, la condición "Show if" se evalúa durante la fase de Ejecución (porque el lienzo solo se construye en la fase de Ejecución).