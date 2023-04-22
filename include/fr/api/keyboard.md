<div class="ClassDoc YAMLDoc" markdown="1">

# classe __Keyboard__

La classe `Keyboard` est utilisée pour collecter les réponses au clavier. Vous créez généralement
un objet `Keyboard` avec la fonction usine `Keyboard()`, comme décrit dans la section [Créer un clavier](#creating-a-keyboard).

__Exemple__

~~~ .python
# Attendre une touche 'z' ou 'x' avec un délai d'attente de 3000 ms
my_keyboard = Keyboard(keylist=['z', 'x'], timeout=3000)
start_time = clock.time()
key, end_time = my_keyboard.get_key()
response = key
response_time = end_time - start_time
~~~

[TOC]

## Choses à savoir

### Créer un clavier

Vous créez généralement un `Keyboard` avec la fonction usine `Keyboard()`:

~~~ .python
my_keyboard = Keyboard()
~~~

Facultativement, vous pouvez passer des [Mots-clés de réponse](#response-keywords) à `Keyboard()`
pour définir le comportement par défaut:

~~~ .python
my_keyboard = Keyboard(timeout=2000)
~~~

### Noms de touches

- Les noms de touches peuvent varier entre les interfaces.
- Les touches peuvent être identifiées soit par caractère soit par nom, et ne sont pas sensibles à la casse.
  Par exemple :
  - La touche 'a' est représenté par 'a' et 'A'
  - La flèche vers le haut est représentée par 'up' et 'UP'
  - La touche '/' est représentée par '/', 'slash', et 'SLASH'
  - La barre d'espace est représentée par 'space' et 'SPACE'
- Pour connaître le nom d'une touche, vous pouvez :
  - Cliquer sur le bouton "lister les touches disponibles" de l'élément KEYBOARD_RESPONSE.
  - Collecter une pression de touche avec un élément KEYBOARD_RESPONSE, et afficher le nom de la touche
    à travers un élément FEEDBACK avec le texte 'Vous avez appuyé sur [response]' dedans.

### Mots-clés de réponse

Les fonctions qui acceptent `**resp_args` prennent les arguments de mots-clés suivants :

- `timeout` spécifie une valeur de délai d'attente en millisecondes ou est défini sur `None` pour
  désactiver le délai d'attente.
- `keylist` spécifie une liste de touches acceptées, ou est défini sur `None`
  pour accepter toutes les touches.

~~~ .python
# Obtenir une pression de la flèche gauche ou droite avec un délai d'attente de 3000 ms
my_keyboard = Keyboard()
key, time = my_keyboard.get_key(keylist=[u'left', u'right'], timeout=3000)
~~~

Les mots-clés de réponse n'affectent que l'opération en cours (sauf lorsqu'ils sont passés à
`Keyboard()`). Pour changer le comportement pour toutes les opérations ultérieures, définissez directement les propriétés de la réponse :

~~~ .python
# Obtenir deux pressions de touche A ou B avec un délai d'attente de 5000 ms
my_keyboard = Keyboard()
my_keyboard.keylist = [u'a', u'b']
my_keyboard.timeout = 5000
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

Ou passez les options de réponse à [keyboard.__init__][__init__]:

~~~ .python
# Obtenir deux pressions de touche A ou B avec un délai d'attente de 5000 ms
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

## flush(self)

Efface toute entrée clavier en attente, sans se limiter au clavier.

__Renvoie__

- True si une touche a été appuyée (c'est-à-dire s'il y avait quelque chose à
vider) et False sinon.

## get_key(\*arglist, \*\*kwdict)

Collecte une seule pression de touche.

__Paramètres__

- **\*\*resp_args**: Facultatif [mots-clés de réponse](#response-keywords) (`timeout` et
`keylist`) qui seront utilisés pour cet appel à `Keyboard.get_key()`.
Cela n'affecte pas les opérations ultérieures.

__Renvoie__

- Un tuple `(key, timestamp)`. `key` est None si un délai d'attente se produit.

__Exemple__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key(timeout=5000)
if response is None:
        print(u'Un délai d\'attente s\'est produit!')
~~~



## get_key_release(\*arglist, \*\*kwdict)

*Nouveau dans v3.2.0*

Collecte une seule libération de touche.

*Important:* Cette
fonction suppose actuellement une disposition de clavier QWERTY
contrairement à
`Keyboard.get_key()`. Cela signifie que la touche retournée
peut être
incorrecte sur les dispositions de clavier non-QWERTY. De plus, cette fonction n'est
pas implémentée pour le backend *psycho*.

__Paramètres__

- **\*\*resp_args**: Facultatif [mots-clés de réponse](#response-keywords) (`timeout` et
`keylist`) qui seront utilisés pour cet appel à
`Keyboard.get_key_release()`. Cela n'affecte pas les opérations ultérieures.

__Renvoie__

- Un tuple `(key, timestamp)`. `key` est None si un délai d'attente se produit.

__Exemple__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key_release(timeout=5000)
if response is None:
        print(u'Un délai d'attente est survenu!')
~~~



## get_mods(self)

Renvoie une liste des modificateurs de clavier (par exemple, shift, alt, etc.) qui
sont actuellement enfoncés.



__Retourne__

- Une liste de modificateurs de clavier. Une liste vide est renvoyée si aucune
  modificateur n'est enfoncé.

__Exemple__

~~~ .python
my_keyboard = Keyboard()
moderateurs = my_keyboard.get_mods()
if u'shift' in moderateurs:
        print(u'La touche majuscule est enfoncée!')
~~~



## show_virtual_keyboard(visible=True)

Affiche ou masque un clavier virtuel si cela est pris en charge par l'arrière-plan. Cette fonction est uniquement nécessaire si vous souhaitez que le clavier virtuel reste visible lors de la collecte de réponses multicharactères. Sinon, `Keyboard.get_key()` montrera et masquera implicitement le clavier pour une réponse à un seul caractère.

Cette fonction ne fait rien pour les back-ends qui ne prennent pas en charge les claviers virtuels.

__Paramètres__

- **visible**: True si le clavier doit être affiché, False sinon.

__Exemple__

~~~ .python
my_keyboard = Keyboard()
my_keyboard.show_virtual_keyboard(True)
response1, timestamp1 = my_keyboard.get_key()
response2, timestamp2 = my_keyboard.get_key()
my_keyboard.show_virtual_keyboard(False)
~~~



## synonyms(key)

Donne une liste de synonymes pour une clé, soit des codes ou des noms. Les synonymes
incluent toutes les variables en tant que types et en tant que chaînes Unicode (le cas échéant).



__Retourne__

- Une liste de synonymes


## valid_keys(self)

Tente de deviner quels noms de clés sont acceptés par l'arrière-plan. Pour
usage interne.



__Retourne__

- Une liste de noms de clés valides.


</div>