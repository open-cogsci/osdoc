title: Respuestas de teclado
hash: 23ed6413bd7bc9180b1e3a384c25c3f89c817414a4460a00260be06f5698474a
locale: es
language: Spanish

Las respuestas del teclado se recopilan con el elemento KEYBOARD_RESPONSE.

[TOC]


## Variables de respuesta

KEYBOARD_RESPONSE establece las variables de respuesta estándar como se describe aquí:

- %link:manual/variables%

## Nombres de teclas

Las teclas generalmente se identifican por su carácter y / o su descripción (dependiendo de cuál sea aplicable). Por ejemplo:

- La tecla `/` se llama 'slash' y '/'. Puedes usar cualquiera de los dos nombres.
- La `a` se llama 'a'.
- La tecla de flecha izquierda se llama 'left'.

Si no sabes cómo se llama una tecla en particular, puedes:

- Hacer clic en el botón 'List available keys'; o
- Crear un experimento simple en el que un KEYBOARD_RESPONSE se siga inmediatamente de un ítem de FEEDBACK con el texto '{response}' en él. Esto mostrará el nombre de la respuesta recolectada anteriormente.


## Respuesta correcta

El campo *Correct response* indica cuál respuesta se considera correcta. Después de una respuesta correcta, la variable `correct` se establece automáticamente en 1; después de una respuesta incorrecta (es decir, todo lo demás), `correct` se establece en 0; si no se especifica una respuesta correcta, `correct` se establece en 'undefined'.

Puede indicar la respuesta correcta de tres formas principales:

- *Dejar el campo vacío.* Si deja vacío el campo *Correct response*, OpenSesame verificará automáticamente si se ha definido una variable llamada `correct_response` y, si es así, utilizará esta variable para la respuesta correcta.
- *Introducir un valor literal.* Puede ingresar explícitamente una respuesta, como 'left' en el caso de un elemento KEYBOARD_RESPONSE. Esto solo es útil si la respuesta correcta es fija.
- *Introducir un nombre de variable.* Puedes ingresar una variable, como '{cr}'. En este caso, esta variable se utilizará para la respuesta correcta.


## Respuestas permitidas

El campo *Allowed responses* indica una lista de respuestas permitidas. Todas las demás respuestas serán ignoradas, excepto 'Escape', que pausará el experimento. Las respuestas permitidas deben ser una lista de respuestas separadas por punto y coma, como 'a;left;/' para un KEYBOARD_RESPONSE. Para aceptar todas las respuestas, deje vacío el campo *Allowed responses*.


%--include: include/timeout.md--%

## Recopilando respuestas del teclado en Python

Puedes usar el objeto `keyboard` para recopilar respuestas del teclado en Python:

- %link:manual/python/keyboard%