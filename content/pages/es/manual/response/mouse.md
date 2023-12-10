title: Respuestas del ratón
hash: 047288a3fddc3e00aa932fe2d7d9f62628bd9d8e5e6d54ceac2b7b5a836e6f0f
locale: es
language: Spanish

Las respuestas del ratón se recogen con el elemento MOUSE_RESPONSE. El MOUSE_RESPONSE está diseñado principalmente para recopilar clics individuales del ratón. Si quieres recoger trayectorias del cursor del ratón, echa un vistazo a los complementos MOUSETRAP:

- %link:mousetracking%

[TOC]


## Variables de respuesta

El MOUSE_RESPONSE establece las variables de respuesta estándar tal como se describen aquí:

- %link:manual/variables%


## Nombres de los botones del ratón

Los botones del ratón tienen un número (`1`, etc.) así como un nombre (`left_button`, etc.). Ambos pueden usarse para especificar respuestas correctas y permitidas, pero la variable `response` se configurará con un número.

- `left_button` corresponde a `1`
- `middle_button` corresponde a `2`
- `right_button` corresponde a `3`
- `scroll_up` corresponde a `4`
- `scroll_down` corresponde a `5`


## Respuesta correcta

El campo *Respuesta correcta* indica qué respuesta se considera correcta. Después de una respuesta correcta, la variable `correct` se establece automáticamente en 1; después de una respuesta incorrecta o un tiempo de espera (es decir, cualquier otra cosa), `correct` se establece en 0; si no se especifica una respuesta correcta, `correct` se establece en 'undefined'.

Puedes indicar la respuesta correcta de tres maneras principales:

- *Deja el campo vacío.* Si dejas el campo *Respuesta correcta* vacío, OpenSesame automáticamente verificará si se ha definido una variable llamada `correct_response` y, de ser así, utilizará esta variable para la respuesta correcta.
- *Introduce un valor literal.* Puedes introducir explícitamente una respuesta, como 1. Esto solo es útil si la respuesta correcta es fija.
- *Introduce el nombre de una variable.* Puedes introducir una variable, como '{cr}'. En este caso, esta variable se utilizará para la respuesta correcta.

Ten en cuenta que la respuesta correcta se refiere a qué botón del ratón se hizo clic, no a qué región de interés se hizo clic (ROI); consulta la sección siguiente para obtener más información sobre las ROI.

## Respuestas permitidas

El campo *Respuestas permitidas* indica una lista de respuestas permitidas. Cualquier otra respuesta será ignorada, excepto 'Escape', que pausará el experimento. Las respuestas permitidas deben ser una lista separada por punto y coma de respuestas, como '1;3' para permitir los botones izquierdo y derecho del ratón. Para aceptar todas las respuestas, deja el campo *Respuestas permitidas* vacío.

Ten en cuenta que las respuestas permitidas se refieren a qué botón del ratón se puede hacer clic, no a qué región de interés se puede hacer clic (ROI); consulta la sección siguiente para obtener más información sobre las ROI.

include: include/timeout.md--

## Coordenadas y regiones de interés (ROI)

Las variables `cursor_x` y `cursor_y` contienen la ubicación del clic del ratón.

Si indicas un SKETCHPAD vinculado, la variable `cursor_roi` contendrá una lista separada por comas de nombres de elementos que contienen la coordenada en la que se hizo clic. En otras palabras, los elementos en el SKETCHPAD sirven automáticamente como regiones de interés para el clic del ratón.

Si la corrección de una respuesta depende de qué ROI se hizo clic, no puedes usar la variable `correct_response` para esto, porque actualmente solo se refiere a qué botón del ratón se hizo clic. En su lugar, necesitas usar un script sencillo.

En un INLINE_SCRIPT de Python puedes hacer esto de la siguiente manera:

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('¡correcto!')
    correct = 1
else:
    print('¡incorrecto!')
    correct = 0
```

Con OSWeb utilizando un INLINE_JAVASCRIPT puedes hacer esto de la siguiente manera:

```js
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('¡correcto!')
    correct = 1
} else {
    console.log('¡incorrecto!')
    correct = 0
}
```

video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Recogiendo clics del ratón y utilización de regiones de interés.

## Recogiendo respuestas del ratón en Python

Puedes usar el objeto `mouse` para recoger respuestas del ratón en Python:

- %link:manual/python/mouse%