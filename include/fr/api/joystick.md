<div class="ClassDoc YAMLDoc" markdown="1">

# instance __joystick__

Si vous insérez le plugin JOYSTICK au début de votre expérience, un
objet JOYSTICK fait automatiquement partie de l'objet expérience
et peut être utilisé dans un élément INLINE_SCRIPT sous le nom `joystick`.

{% set arg_joybuttonlist = "Une liste de boutons acceptés ou " +
"`None` pour accepter tous les boutons." %}
{% set arg_timeout = "Une valeur de délai d'attente en millisecondes ou `None` pour ne pas avoir " +
"de délai d'attente." %}

[TOC]

## flush(self)

Efface toutes les entrées en attente, sans se limiter au joystick.



__Renvoie__

- True si l'entrée joyinput était en attente (c'est-à-dire s'il y avait quelque chose à
vider) et False sinon.


## get_joyaxes(timeout=None)

Attend le mouvement des axes du joystick.


__Paramètres__

- **timeout**: Une valeur de délai d'attente en millisecondes ou `None` pour utiliser le délai d'attente par défaut.

__Renvoie__

- Un tuple `(position, timestamp)`. `position` est `None` si un délai d'attente
se produit. Sinon, `position` est un tuple `(x, y, z)`.


## get_joyballs(timeout=None)

Attend le mouvement des boules de commande du joystick.


__Paramètres__

- **timeout**: Une valeur de délai d'attente en millisecondes ou `None` pour utiliser le délai d'attente par défaut.

__Renvoie__

- Un tuple `(position, timestamp)`. La position est `None` si un
délai d'attente se produit.


## get_joybutton(joybuttonlist=None, timeout=None)

Collecte les entrées des boutons du joystick.


__Paramètres__

- **joybuttonlist**: Une liste de boutons acceptés ou `None` pour la liste joybutton par défaut.
- **timeout**: Une valeur de délai d'attente en millisecondes ou `None` pour utiliser le délai d'attente par défaut.

__Renvoie__

- Un tuple (joybutton, timestamp). Le joybutton est `None` si un
délai d'attente se produit.


## get_joyhats(timeout=None)

Attend le mouvement des chapeaux du joystick.


__Paramètres__

- **timeout**: Une valeur de délai d'attente en millisecondes ou `None` pour utiliser le délai d'attente par défaut.

__Renvoie__

- Un tuple `(position, timestamp)`. `position` est `None` si un délai d'attente
se produit. Sinon, `position` est un tuple `(x, y)`.


## get_joyinput(joybuttonlist=None, timeout=None)

Attend n'importe quelle entrée de joystick (boutons, axes, chapeaux ou boules).


__Paramètres__

- **joybuttonlist**: Une liste de boutons acceptés ou `None` pour la liste joybutton par défaut.
- **timeout**: Une valeur de délai d'attente en millisecondes ou `None` pour utiliser le délai d'attente par défaut.

__Renvoie__

- Un tuple (event, value, timestamp). La valeur est `None` si un délai d'attente
se produit. `event` est l'un des `None`, 'joybuttonpress',
'joyballmotion', 'joyaxismotion' ou 'joyhatmotion'


## input_options(self)

Génère une liste avec le nombre de boutons, axes, boules
et chapeaux disponibles.



__Renvoie__

- Une liste avec le nombre d'entrées comme suit : [boutons, axes, boules,
chapeaux].


## set_joybuttonlist(joybuttonlist=None)

Définit une liste de boutons acceptés.


__Paramètres__

- **joybuttonlist**: {{arg_joybuttonlist}}


## set_timeout(timeout=None)

Définit un délai d'attente.


__Paramètres__

- **timeout**: {{arg_timeout}}


</div>