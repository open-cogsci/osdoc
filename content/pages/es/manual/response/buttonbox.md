title: Caja de botones
hash: 0bc151c594d9ecc7e386d138f7aa3b43b072aee2019b7106e4c17ae302f91c67
locale: es
language: Spanish

Hay muchos tipos diferentes de cajas de botones y todos funcionan de diferentes maneras. Por lo tanto, no hay un solo elemento de OpenSesame que funcione con todas las cajas de botones. (Esto es diferente de los teclados, que son dispositivos estándar que funcionan con el elemento KEYBOARD_RESPONSE).

Tipos comunes de cajas de botones:

- Algunas cajas de botones *emulan pulsaciones de teclas*. Esto es fácil, porque puedes usar el elemento KEYBOARD_RESPONSE normal.
	- %link:manual/response/keyboard%
- Algunas cajas de botones *emulan un joystick*. Esto también es fácil, porque puedes usar el complemento JOYSTICK.
	- %link:joystick%
- Algunas cajas de botones son compatibles con el *Serial Response Box* desarrollado por Psychology Software Tools. Estas cajas de botones son compatibles con el complemento SRBOX.
	- %link:srbox%
- Algunas cajas de botones tienen sus propias librerías de Python. En este caso, deberías poder encontrar ejemplos de scripts de cómo usar la caja de botones en Python, es decir, en un elemento INLINE_SCRIPT de OpenSesame.