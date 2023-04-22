title: Faire les choses en parallèle
hash: 355690924feb930d7fef825b28269bb20c28adb8e20b8c2a86de761222d40d95
locale: fr
language: French

Les coroutines exécutent plusieurs éléments en parallèle, ou, pour être plus précis, elles exécutent des éléments en rapide alternance d'une manière qui semble parallèle. Tous les éléments ne prennent pas en charge les coroutines.

[TOC]

## Utiliser des coroutines

Vous pouvez utiliser des coroutines grâce au plugin COROUTINES (voir %FigCoroutinesInterface).

%--
figure:
 source: FigCoroutinesInterface.png
 caption: L'interface du plugin coroutines.
 id: FigCoroutinesInterface
--%

Comme vous pouvez le voir, le plugin COROUTINES ressemble à l'élément SEQUENCE, mais présente quelques options supplémentaires :

- *Duration* indique la durée totale des coroutines.
- *End after item (optional)* indique que les coroutines doivent se terminer lorsqu'un élément spécifique est terminé. Cela vous permet, par exemple, d'indiquer que les coroutines doivent se terminer lorsqu'une touche a été recueillie, en sélectionnant un élément KEYBOARD_RESPONSE ici.
- Chaque élément a un *Start time*. La plupart des éléments ont également un *End time*. Le temps de fin ne s'applique pas aux éléments à tir unique; par exemple, les SKETCHPAD affichent un écran et se terminent immédiatement, donc ils n'ont pas de temps de fin.

Plus précisément, l'exemple de %FigCoroutinesInterface (de l'exemple de tâche de signal d'arrêt) fait ce qui suit :

- Il montre une cible immédiatement.
- Si la variable `stop_after` n'est pas vide, il affiche l'écran stop_signal après un intervalle spécifié par la variable `stop_after`.
- Pendant tout l'intervalle (2000 ms), une réponse au clavier est recueillie.

Le flux temporel est contrôlé par le plugin COROUTINES. Par conséquent, les valeurs de délai d'expiration et de durée spécifiées dans les éléments ne sont pas utilisées. Par exemple, dans %FigCoroutinesInterface, le KEYBOARD_RESPONSE s'exécutera pendant 2000 ms, quel que soit le délai d'expiration spécifié dans l'élément.

## Éléments pris en charge

Actuellement, les éléments suivants sont pris en charge (cette liste peut ne pas être exhaustive) :

- FEEDBACK
- INLINE_SCRIPT
- KEYBOARD_RESPONSE
- LOGGER
- MOUSE_RESPONSE
- SAMPLER
- SYNTH
- SKETCHPAD

## Utiliser des éléments inline_script dans les coroutines

Lorsque vous utilisez un élément INLINE_SCRIPT dans une COROUTINES, la phase Run fonctionne un peu différemment de ce à quoi vous pourriez être habitué. Plus précisément, la phase Run est exécutée à chaque itération des COROUTINES. De plus, la phase Run ne doit contenir que du code qui prend très peu de temps à exécuter ; en effet, les opérations longues bloqueront les COROUTINES, interférant ainsi avec le minutage des autres éléments des COROUTINES. Pour mettre fin aux COROUTINES, vous pouvez lever une exception `AbortCoroutines()`.

Par exemple, disons que vous avez une COROUTINES avec deux éléments KEYBOARD_RESPONSE, *kb1* et *kb2*, et que vous voulez exécuter les COROUTINES jusqu'à ce que deux touches aient été recueillies, avec un délai d'expiration de 5000 ms. Vous pourriez alors créer la structure COROUTINES suivante :

%--
figure:
 source: FigCoroutinesTwoResponses.png
 caption: Une coroutines qui recueille deux réponses par pression de touche
 id: FigCoroutinesTwoResponses
--%

L'élément INLINE_SCRIPT *check_responses* définira d'abord les deux variables de réponse sur une chaîne vide dans la phase de préparation :

```python
# Ceci est exécuté au début des coroutines
response_kb1 = ''
response_kb2 = ''
```

Et ensuite, dans la phase Run, vérifiez si les deux variables ont été définies, et abandonnez les coroutines si c'est le cas :

```python
# Les valeurs qui ne sont pas une chaîne vide sont vraies pour Python
# Ce code sera exécuté plusieurs fois !
if response_kb1 and response_kb2:
    raise AbortCoroutines()
```

## Expressions run-if

Le comportement des expressions run-if dans les COROUTINES est un peu différent de celui des éléments SEQUENCE. Plus précisément, les expressions run-if dans les COROUTINES sont évaluées pendant la phase de préparation. Voir aussi :

- %link:prepare-run%