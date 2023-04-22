<div class="ClassDoc YAMLDoc" markdown="1">

# instance __srbox__

Si vous insérez le plugin srbox au début de votre expérience, une
instance de SRBOX fait automatiquement partie de l'objet d'expérimentation
et
peut être accessible dans un élément de script en ligne sous SRBOX.

__Note importante 1 :__

Si vous ne spécifiez pas de périphérique, le plugin essayera de détecter automatiquement
le
port SR Box. Cependant, sur certains systèmes, cela fige l'expérience, il
est donc préférable de spécifier explicitement un périphérique.

__Note importante 2 :__

Vous
devez appeler [srbox.start] pour mettre la SR Box en mode envoi,
avant
d'appeler [srbox.get_button_press] pour collecter une pression de bouton.

__Exemple :__
~~~ .python
t0 = clock.time()
srbox.start()
button, t1 = srbox.get_button_press(allowed_buttons=[1, 2],
                                    require_state_change=True)
if button == 1:
    response_time = t1 - t0
print(f'Le bouton 1 a été pressé en {response_time} ms !')
srbox.stop()
~~~
[TOC]

## get_button_press(allowed_buttons=None, timeout=None, require_state_change=False)

Collecte une pression de bouton de la SR Box.


__Paramètres__

- **allowed_buttons**: Une liste de boutons acceptés ou `None` pour accepter tous
les boutons. Les boutons valides sont des entiers de 1 à 8.
- **timeout**: Une valeur d'expiration en millisecondes ou `None` pour aucune expiration.
- **require_state_change    Indique si un bouton déjà pressé doit être accepté**: (False), ou si seulement un changement d'état de non pressé à pressé
est accepté (True).

__Renvoie__

- Un tuple `(button_list, timestamp)`. `button_list` est `None` si aucun
bouton n'a été pressé (c'est-à-dire si un délai d'expiration est survenu).


## send(ch)

Envoie un seul caractère à la SR Box. Envoyez '`' pour éteindre toutes
les lumières, 'a' pour allumer la lumière 1, 'b' pour allumer la lumière 2, 'c' pour les lumières
1 et 2 allumées, etc.


__Paramètres__

- **ch**: Le caractère à envoyer. Si une `str` est passée, elle est codée en
`bytes` en utilisant l'encodage utf-8.


## start(self)

Active le mode d'envoi, de sorte que la SR Box commence à envoyer des sorties.
La SR Box doit être en mode d'envoi lorsque vous appelez
[srbox.get_button_press].




## stop(self)

Désactive le mode d'envoi, de sorte que la SR Box cesse de fournir des sorties.




</div>