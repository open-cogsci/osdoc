title: Boîte de boutons
hash: 0bc151c594d9ecc7e386d138f7aa3b43b072aee2019b7106e4c17ae302f91c67
locale: fr
language: French

Il existe de nombreux types de boîtes à boutons différents, et ils fonctionnent tous de différentes manières. Par conséquent, il n'y a pas de seul élément OpenSesame qui fonctionne avec toutes les boîtes à boutons. (Ceci est différent des claviers, qui sont des dispositifs standard qui fonctionnent tous avec l'élément KEYBOARD_RESPONSE.)

Types de boîtes à boutons courants :

- Certaines boîtes à boutons *émulent des frappes*. C'est facile, car vous pouvez utiliser l'élément KEYBOARD_RESPONSE normal.
	- %link:manual/response/keyboard%
- Certaines boîtes à boutons *émulent un joystick*. C'est également facile, car vous pouvez utiliser le plugin JOYSTICK.
	- %link:joystick%
- Certaines boîtes à boutons sont compatibles avec le *Serial Response Box* développé par Psychology Software Tools. Ces boîtes à boutons sont prises en charge par le plugin SRBOX.
	- %link:srbox%
- Certaines boîtes à boutons ont leurs propres bibliothèques Python. Dans ce cas, vous devriez être en mesure de trouver des exemples de scripts sur la façon d'utiliser la boîte à boutons en Python, c'est-à-dire dans un élément INLINE_SCRIPT OpenSesame.