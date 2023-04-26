title: Tastenfeld
hash: 0bc151c594d9ecc7e386d138f7aa3b43b072aee2019b7106e4c17ae302f91c67
locale: de
language: German

Es gibt viele verschiedene Arten von Tastenfeldern und sie alle funktionieren auf unterschiedliche Weise. Daher gibt es kein einzelnes OpenSesame-Element, das mit allen Tastenfeldern funktioniert. (Dies unterscheidet sich von Tastaturen, die Standardgeräte sind und alle mit dem KEYBOARD_RESPONSE-Element funktionieren.)

Gängige Arten von Tastenfeldern:

- Einige Tastenfelder *emulieren Tastendrücke*. Das ist einfach, denn Sie können das normale KEYBOARD_RESPONSE-Element verwenden.
	- %link:manual/response/keyboard%
- Einige Tastenfelder *emulieren einen Joystick*. Das ist auch einfach, denn Sie können das JOYSTICK-Plugin verwenden.
	- %link:joystick%
- Einige Tastenfelder sind kompatibel mit der *Serial Response Box*, die von Psychology Software Tools entwickelt wurde. Diese Tastenfelder werden vom SRBOX-Plugin unterstützt.
	- %link:srbox%
- Einige Tastenfelder verfügen über eigene Python-Bibliotheken. In diesem Fall sollten Sie Beispielskripte finden können, wie das Tastenfeld in Python verwendet wird, das heißt in einem OpenSesame INLINE_SCRIPT-Element.