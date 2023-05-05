title: Respuestas del ratón
hash: 9e348c65c44cf1d0e1e152976c013b0a235f432d16ceeb3fff09001f8c9d0e7b
locale: es
language: Spanish

Las respuestas del mouse se recopilan con el elemento MOUSE_RESPONSE. El MOUSE_RESPONSE está diseñado principalmente para recopilar clics individuales del mouse. Si desea recopilar trayectorias del cursor del mouse, eche un vistazo a los complementos MOUSETRAP:

- %link:mousetracking%

[TOC]


## Variables de respuesta

El MOUSE_RESPONSE establece las variables de respuesta estándar como se describe aquí:

- %link:manual/variables%


## Nombres de los botones del mouse

Los botones del ratón tienen un número (`1`, etc.) así como un nombre (`left_button`, etc.). Ambos se pueden usar para especificar respuestas correctas y permitidas, pero la variable `response` se establecerá en un número.

- `left_button` corresponde a `1`
- `middle_button` corresponde a `2`
- `right_button` corresponde a `3`
- `scroll_up` corresponde a `4`
- `scroll_down` corresponde a `5`


## Respuesta correcta

El campo *Respuesta correcta* indica cuál respuesta se considera correcta. Después de una respuesta correcta, la variable `correct` se establece automáticamente en 1; después de una respuesta incorrecta o tiempo agotado (es decir, todo lo demás), `correct` se establece en 0; si no se especifica una respuesta correcta, `correct` se establece como 'indefinido'.

Puede indicar la respuesta correcta de tres formas principales:

- *Dejar el campo vacío.* Si deja vacío el campo *Respuesta correcta*, OpenSesame verificará automáticamente si se ha definido una variable llamada `correct_response` y, en caso afirmativo, utilizará esta variable para la respuesta correcta.
- *Introduzca un valor literal.* Puede ingresar explícitamente una respuesta, como 1. Esto solo es útil si la respuesta correcta es fija.
- *Introduzca un nombre de variable.* Puede ingresar una variable, como '{cr}'. En este caso, se utilizará esta variable para la respuesta correcta.


## Respuestas permitidas

El campo *Respuestas permitidas* indica una lista de respuestas permitidas. Todas las demás respuestas serán ignoradas, excepto 'Escape', que pausará el experimento. Las respuestas permitidas deben ser una lista separada por puntos y comas de respuestas, como '1;3' para permitir los botones izquierdo y derecho del mouse. Para aceptar todas las respuestas, deje vacío el campo *Respuestas permitidas*.


%--include: include/timeout.md--%

## Coordenadas y regiones de interés (ROI)

Las variables `cursor_x` y `cursor_y` contienen la ubicación del clic del mouse.

Si indica un SKETCHPAD vinculado, la variable `cursor_roi` contendrá una lista separada por comas de nombres de elementos que contienen las coordenadas clicadas. En otras palabras, los elementos en el SKETCHPAD sirven automáticamente como regiones de interés para el clic del mouse.

%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Recopilación de clics del mouse y uso de regiones de interés.
--%

## Recopilación de respuestas del mouse en Python

Puede usar el objeto `mouse` para recopilar respuestas del mouse en Python:

- %link:manual/python/mouse%