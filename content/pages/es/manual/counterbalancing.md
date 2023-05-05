title: Contrapeso
hash: f746c6dcc8ded61b700e84340fafff7a9ab6a1c217365d1ff9b97ab344438cd2
locale: es
language: Spanish

El contrapeso es una forma de eliminar factores de confusión de un experimento al tener tareas ligeramente diferentes para diferentes grupos de participantes. Esto suena abstracto, así que consideremos dos ejemplos.

[TOC]

### Ejemplo 1: Contrapeso de reglas de respuesta

Considera un experimento de decisión léxica en el cual los participantes clasifican palabras como verbos presionando 'z' con la mano izquierda, o como sustantivos presionando 'm' con la mano derecha. Este diseño tiene un problema: si descubres que los participantes responden más rápido a los sustantivos que a los verbos, esto podría ser porque se procesan más rápido los sustantivos que los verbos, o porque los participantes responden más rápido con la mano derecha que con la izquierda. Puedes solucionar este problema contrapesando la regla de respuesta.

Para números pares de participantes:

- verbo → z
- sustantivo → m

Para números impares de participantes:

- verbo → m
- sustantivo → z

### Ejemplo 2: Rotación de condiciones de estímulo

Considera un experimento de priming enmascarado en el cual los participantes leen en voz alta las palabras objetivo. En cada ensayo, la palabra objetivo va precedida de uno de los tres tipos de palabras de priming:

- Un prime no relacionado, por ejemplo, primar con 'berry' para el objetivo 'house'.
- Un prime ortográficamente relacionado, por ejemplo, primar con 'mouse' para el objetivo 'house'
- Un prime semánticamente relacionado, por ejemplo, primar con 'garden' para el objetivo 'house'

Para evitar efectos de repetición, solo quieres mostrar palabras objetivo una vez por participante. Por lo tanto, creas tres conjuntos diferentes de palabras objetivo, uno para cada tipo de prime. Este es un diseño entre palabras, que tiene menos potencia estadística que un diseño dentro de palabras, en el cual cada palabra objetivo ocurre en cada condición. (Por la misma razón que los diseños entre sujetos son menos potentes que los diseños dentro de sujetos.)

Puedes utilizar el contrapeso para cambiar este experimento a un diseño dentro de palabras 'rotando' la condición en la que cada palabra ocurre entre los participantes. Tenemos tres condiciones y, por lo tanto, tres grupos de participantes:

- Participantes 1, 4, 7, etc.
    - Palabra A en condición 1
    - Palabra B en condición 2
    - Palabra C en condición 3
- Participantes 2, 5, 8, etc.
    - Palabra A en condición 2
    - Palabra B en condición 3
    - Palabra C en condición 1
- Participantes 3, 6, 9, etc.
    - Palabra A en condición 3
    - Palabra B en condición 1
    - Palabra C en condición 2

## Implementación del contrapeso

### Usando el número de sujeto

Cuando ejecutas un experimento en OpenSesame en el escritorio, se te solicita un número de sujeto. Cuando ejecutas un experimento en línea, se selecciona aleatoriamente un número de sujeto de la lista de posibles números de sujeto que has especificado en la [extensión OSWeb](%url:osweb). (Esto significa que para los experimentos en línea no puedes asegurar que el número de participantes sea exactamente igual para las diferentes condiciones que deseas contrapesar, al menos no si confías en el número de sujeto).

Este número de sujeto está disponible como la variable experimental `subject_nr`. Además, la variable experimental `subject_parity` tiene el valor 'odd' o 'even', según si el número de sujeto es impar o par. Ahora, supongamos que deseas contrapesar la regla de respuesta como en el Ejemplo 1, podrías agregar el siguiente INLINE_SCRIPT al inicio del experimento.

```python
if subject_parity == 'odd':
    verb_response = 'z'
    noun_response = 'm'
else:
    verb_response = 'm'
    noun_response = 'z'
```

O, al crear un experimento de OSWeb, agregue el siguiente INLINE_JAVASCRIPT al inicio del experimento:

```javascript
if (subject_parity === 'odd') {
    verb_response = 'z'
    noun_response = 'm'
} else {
    verb_response = 'm'
    noun_response = 'z'
}
```

Ahora, en tu *block_loop*, en lugar de establecer `correct_response` en un valor fijo, lo estableces en una variable: `{verb_response}` o `{noun_response}`. Puedes ver el ejemplo de *tarea de decisión léxica* para ver cómo funciona esto (Menú -> Herramientas -> Experimentos de ejemplo).

### Usando datos de sesión por lotes (solo JATOS y OSWeb)

Al ejecutar un experimento de OSWeb alojado en JATOS, puedes utilizar [Datos de Sesión por Lote](https://www.jatos.org/jatos.js-Reference.html#functions-to-access-the-batch-session). Estos son datos compartidos entre todas las sesiones experimentales que forman parte del mismo lote de trabajadores. Por lo tanto, puedes utilizar estos datos para definir una lista de condiciones que se distribuyan entre los participantes. Al comienzo de cada sesión experimental, se elimina una condición de esta lista y se utiliza para la sesión actual. Esta es la forma más sofisticada de implementar la contrabalanceación para experimentos de OSWeb alojados en JATOS.

Puedes descargar un experimento de plantilla aquí:

- %static:attachments/counterbalancing-osweb-jatos.osexp%

Al ejecutarlo desde JATOS, el experimento obtiene una única condición de los Datos de Sesión por Lote (ver más abajo) y registra esto como la variable experimental `condition`. Al realizar una prueba, `condition` se establece en un valor predeterminado especificado al final de *init_condition*.

El experimento en sí debe implementarse en la SECUENCIA *experiment*, que en la plantilla contiene solo el SKETCHPAD *show_condition* (ver %FigCounterbalancingOSWebJATOS).

%--
figure:
    source: counterbalancing-osweb-jatos.png
    id: FigCounterbalancingOSWebJATOS
    caption: |
        El área de descripción general del experimento de plantilla para implementar contrabalancing con Datos de sesión por lote de JATOS.
--%

Al importar el experimento a JATOS, todas las condiciones deben especificarse en los Datos de Sesión por Lote como la lista `pending` (en Administrador de trabajadores y lotes; ver %FigBatchSessionData). Cada condición de `pending` corresponde a una única sesión experimental; por lo tanto, si la condición `a` debe usarse para dos sesiones experimentales, entonces `a` debe aparecer dos veces en la lista `pending`. Las condiciones se utilizan en el orden en que están definidas.

%--
figure:
    source: batch-session-data.png
    id: FigBatchSessionData
    caption: |
        Las condiciones deben especificarse en los Datos de Sesión por Lote en JATOS.
--%

Al comienzo de una sesión experimental, una única condición se mueve de `pending` a `started`. (Cuando la lista `pending` está vacía, se informa al participante que ya no puede participar en el experimento). Al final de la sesión experimental, la condición se añade a la lista `finished`.

Para hacer esto más concreto, digamos que has definido los Datos de Sesión por Lote como se muestra en %FigBatchSessionData. Luego, se inician cuatro sesiones experimentales, pero la segunda sesión experimental, con la condición `a`, nunca termina, por ejemplo porque el participante cierra el navegador a mitad del experimento. Los Datos de Sesión por Lote se verán como en %FigBatchSessionAfter:

%--
figure:
    source: batch-session-data-after.png
    id: FigBatchSessionAfter
    caption: |
        Los Datos de Sesión por Lote después de que todas las condiciones hayan sido consumidas. Una sesión, con la condición `a`, nunca terminó.
--%

Puedes ver en los Datos de Sesión por Lote que una sesión experimental comenzó con la condición `a` pero nunca terminó. Para colectar una sesión experimental con esta condición, debes agregar manualmente una nueva `a` a la lista `pending` y obtener una nueva sesión.