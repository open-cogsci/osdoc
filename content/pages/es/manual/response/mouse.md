title: Respuestas de ratón y táctiles
hash: d6f7dcf58a399be886fd23f0ed29e9898c1beae44c3c8f6d076e26f96471d4f0
locale: es
language: Spanish

Las respuestas del ratón se recopilan con el elemento MOUSE_RESPONSE. El MOUSE_RESPONSE está destinado principalmente a recopilar clics individuales del ratón. En dispositivos con pantalla táctil, las respuestas táctiles (elemento TOUCH_RESPONSE) generalmente se registran de la misma manera que los clics del botón 1 del ratón en las coordenadas tocadas, por lo que a menudo se puede usar el mismo elemento y la misma lógica tanto para la entrada del ratón como para la táctil. Si quieres recopilar trayectorias del cursor del ratón, echa un vistazo a los plugins MOUSETRAP:

- %link:mousetracking%

[TOC]


## Variables de respuesta

El MOUSE_RESPONSE establece las variables de respuesta estándar tal como se describe aquí:

- %link:manual/variables%

Además, las siguientes variables son relevantes para las respuestas de ratón y táctiles:

| Variable | Descripción |
|---|---|
| `response` | El botón del ratón en el que se hizo clic. Esto se almacena como un número (`1` = botón izquierdo, `2` = botón central, `3` = botón derecho, `4` = desplazamiento hacia arriba, `5` = desplazamiento hacia abajo). En caso de timeout, `response` se establece en `None`. |
| `response_time` | El tiempo de respuesta en milisegundos, o el tiempo de timeout registrado si no se realizó ninguna respuesta. |
| `correct` | Se establece automáticamente en función de la corrección del botón: `1` para una respuesta correcta del botón del ratón, `0` para una respuesta incorrecta del botón del ratón o timeout, y `undefined` si no se especifica una respuesta correcta. |
| `cursor_x` | La coordenada x del clic o toque. |
| `cursor_y` | La coordenada y del clic o toque. |
| `cursor_roi` | Una lista separada por punto y coma de los nombres de los elementos de sketchpad que contienen las coordenadas del clic. Si los elementos se superponen, se pueden listar varios nombres. Esta variable informa dónde ocurrió el clic; no determina automáticamente `correct`. |


## Nombres de los botones del ratón

Los botones del ratón tienen un número (`1`, etc.) así como un nombre (`left_button`, etc.). Ambos se pueden usar para especificar respuestas correctas y permitidas, pero la variable `response` se establecerá en un número.

- `left_button` corresponde a `1`
- `middle_button` corresponde a `2`
- `right_button` corresponde a `3`
- `scroll_up` corresponde a `4`
- `scroll_down` corresponde a `5`


## Respuesta correcta

El campo *Correct response* indica qué respuesta se considera correcta. Después de una respuesta correcta, la variable `correct` se establece automáticamente en 1; después de una respuesta incorrecta o un timeout (es decir, cualquier otra cosa), `correct` se establece en 0; si no se especifica ninguna respuesta correcta, `correct` se establece en 'undefined'.

Puedes indicar la respuesta correcta de tres maneras principales:

- *Deja el campo vacío.* Si dejas vacío el campo *Correct response*, OpenSesame comprobará automáticamente si se ha definido una variable llamada `correct_response` y, de ser así, usará esta variable como respuesta correcta.
- *Introduce un valor literal.* Puedes introducir explícitamente una respuesta, como 1. Esto solo es útil si la respuesta correcta es fija.
- *Introduce un nombre de variable.* Puedes introducir una variable, como '{cr}'. En este caso, esta variable se usará como respuesta correcta.

Ten en cuenta que la respuesta correcta se refiere a qué botón del ratón se pulsó, no a qué región de interés se pulsó (ROI). Si la corrección depende de la ubicación pulsada en lugar del botón del ratón, necesitas determinarla tú mismo basándote en `cursor_roi`; consulta la sección siguiente para obtener más información sobre los ROI.


## Respuestas permitidas

El campo *Allowed responses* indica una lista de respuestas permitidas. Todas las demás respuestas serán ignoradas, excepto 'Escape', que pausará el experimento. Las respuestas permitidas deben ser una lista de respuestas separadas por punto y coma, como '1;3' para permitir los botones izquierdo y derecho del ratón. Para aceptar todas las respuestas, deja vacío el campo *Allowed responses*.

Ten en cuenta que las respuestas permitidas se refieren a qué botón del ratón se puede pulsar, no a qué región de interés se puede pulsar (ROI); consulta la sección siguiente para obtener más información sobre los ROI.


%--include: include/timeout.md--%

## Coordenadas y regiones de interés (ROI)

Las variables `cursor_x` y `cursor_y` contienen la ubicación del clic del ratón.

Si indicas un SKETCHPAD vinculado, la variable `cursor_roi` contendrá una lista separada por punto y coma de los nombres de los elementos que contienen la coordenada en la que se hizo clic. En otras palabras, los elementos del SKETCHPAD sirven automáticamente como regiones de interés para el clic del ratón.

La variable `cursor_roi` indica dónde ocurrió el clic, mientras que `response` indica qué botón del ratón se pulsó. Si varios elementos con nombre se superponen en la posición en la que se hizo clic, `cursor_roi` puede contener varios nombres de elementos.

Si la corrección de una respuesta depende de qué ROI se pulsó, no puedes usar la variable `correct_response` para ello, porque esta se refiere únicamente a qué botón del ratón se pulsó. En su lugar, necesitas usar un script simple para determinar la corrección en función de `cursor_roi` y, si es necesario, sobrescribir `correct`.

En un Python INLINE_SCRIPT puedes hacerlo de la siguiente manera:

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('correct!')
    correct = 1
else:
    print('incorrect!')
    correct = 0
```

Con OSWeb usando un INLINE_JAVASCRIPT puedes hacerlo de la siguiente manera:

```javascript
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('correct!')
    correct = 1
} else {
    console.log('incorrect!')
    correct = 0
}
```

Aquí, `'my_roi'` es simplemente un nombre de ejemplo de un elemento de sketchpad. En un experimento real, sustitúyelo por el nombre de la ROI que debe contarse como correcta. Para evitar ambigüedades, los elementos con nombre deben ser únicos dentro de un sketchpad.


## Respuestas táctiles

En dispositivos con pantalla táctil, cada toque suele registrarse como una respuesta de botón 1 del ratón en las coordenadas tocadas. Esto significa que el elemento MOUSE_RESPONSE a menudo puede usarse tanto para clics de ratón como para toques en pantalla sin más modificaciones.

En la práctica, esto significa que una respuesta táctil se comporta de la siguiente manera:

- El botón normalmente se registra como `1`
- La ubicación del toque se almacena en `cursor_x` y `cursor_y`
- Si hay un sketchpad vinculado, los elementos tocados pueden identificarse mediante `cursor_roi`

Esto puede ser útil para experimentos que deban ejecutarse tanto en equipos de escritorio como en dispositivos con pantalla táctil.

### Ejemplo: respuestas táctiles con MOUSE_RESPONSE

Por ejemplo, considera una tarea de elección simple en la que se muestran dos elementos grandes de sketchpad en el lado izquierdo y derecho de la pantalla. Si el participante toca el elemento de la izquierda en una pantalla táctil:

- `response` normalmente se establecerá en `1`
- `cursor_x` y `cursor_y` contendrán las coordenadas del toque
- `cursor_roi` puede contener el nombre del elemento tocado, como `left_option`

Esto significa que la entrada táctil puede manejarse de la misma manera que la entrada del ratón. Si la corrección depende del elemento tocado en lugar del botón, puedes usar la misma lógica de `cursor_roi` descrita anteriormente.

### Ejemplo: usar el plug-in `touch_response`

Para experimentos en los que quieras dividir la pantalla en regiones de respuesta discretas (p. ej., una cuadrícula de botones), el plug-in `touch_response` ofrece un enfoque más simple y cómodo que trabajar con coordenadas sin procesar. Divide la pantalla en una cuadrícula de filas y columnas, y codifica cada respuesta como un único número, contando de izquierda a derecha y de arriba abajo.

Por ejemplo, con 2 columnas y 3 filas, la pantalla se divide de la siguiente manera:

| | Columna 1 | Columna 2 |
|---|---|---|
| **Fila 1** | 1 | 2 |
| **Fila 2** | 3 | 4 |
| **Fila 3** | 5 | 6 |

Así, si especificas 2 columnas y 1 fila, la pantalla se divide en dos regiones de respuesta:

| Mitad izquierda | Mitad derecha |
|---|---|
| `1` | `2` |

En una tarea simple de sí/no, podrías asignar:

- `1` = Sí
- `2` = No

Si la respuesta correcta es Sí, establece el campo *Correct response* en `1`. OpenSesame establecerá entonces automáticamente `correct` en 1 cuando el participante toque la mitad izquierda de la pantalla.

> [!NOTE]
> El plug-in `touch_response` no utiliza elementos de sketchpad con nombre ni `cursor_roi`. Las respuestas se codifican únicamente como posiciones de la cuadrícula.

> [!NOTE]
> El comportamiento exacto de la entrada táctil puede depender de la plataforma y del backend que se utilice para ejecutar el experimento.

> [!NOTE]
> El elemento MOUSE_RESPONSE solo captura una única respuesta táctil. Si varios dedos tocan la pantalla simultáneamente, solo se registra una respuesta.


%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Collecting mouse clicks and using regions of interest.
--%

## Recopilar respuestas del ratón en Python

Puede usar el objeto `mouse` para recopilar respuestas del ratón en Python:

- %link:manual/python/mouse%