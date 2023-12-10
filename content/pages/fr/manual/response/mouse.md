title: Réponses de la souris
hash: 047288a3fddc3e00aa932fe2d7d9f62628bd9d8e5e6d54ceac2b7b5a836e6f0f
locale: fr
language: French

Les réponses de la souris sont collectées avec l'élément `mouse_response`. Le `mouse_response` est principalement destiné à collecter des clics de souris individuels. Si vous voulez collecter les trajectoires du curseur de la souris, jetez un œil aux plugins MOUSETRAP :

- %link:mousetracking%

[TOC]


## Variables de réponse

Le `mouse_response` définit les variables de réponse standard comme décrit ici :

- %link:manual/variables%


## Noms des boutons de la souris

Les boutons de la souris ont un numéro (`1`, etc.) ainsi qu'un nom (`left_button`, etc.). Les deux peuvent être utilisés pour spécifier les réponses correctes et autorisées, mais la variable `response` sera définie avec un numéro.

- `left_button` correspond à `1`
- `middle_button` correspond à `2`
- `right_button` correspond à `3`
- `scroll_up` correspond à `4`
- `scroll_down` correspond à `5`


## Réponse correcte

Le champ *Correct response* indique quelle réponse est considérée comme correcte. Après une réponse correcte, la variable `correct` est automatiquement mise à 1 ; après une réponse incorrecte ou un délai d'attente (c'est-à-dire tout le reste), `correct` est mise à 0 ; si aucune réponse correcte n'est spécifiée, `correct` est mise à 'undefined'.

Vous pouvez indiquer la réponse correcte de trois manières principales :

- *Laissez le champ vide.* Si vous laissez le champ *Correct response* vide, OpenSesame vérifiera automatiquement si une variable appelée `correct_response` a été définie, et si c'est le cas, utilisera cette variable pour la réponse correcte.
- *Entrez une valeur littérale.* Vous pouvez saisir explicitement une réponse, telle que 1. Ceci est utile seulement si la réponse correcte est fixe.
- *Entrez un nom de variable.* Vous pouvez entrer une variable, telle que '{cr}'. Dans ce cas, cette variable sera utilisée pour la réponse correcte.

Notez que la réponse correcte se réfère au bouton de souris qui a été cliqué, et non à la région d'intérêt qui a été cliquée (ROI) ; voir la section ci-dessous pour plus d'informations sur les ROI.

## Réponses autorisées

Le champ *Allowed responses* indique une liste des réponses autorisées. Toutes les autres réponses seront ignorées, sauf 'Escape', qui mettra le jeu en pause. Les réponses autorisées doivent être une liste de réponses séparées par des points-virgules, telles que '1;3' pour autoriser les boutons gauche et droit de la souris. Pour accepter toutes les réponses, laissez le champ *Allowed responses* vide.

Notez que les réponses autorisées se réfèrent au bouton de souris qui peut être cliqué, et non à la région d'intérêt qui peut être cliquée (ROI) ; voir la section ci-dessous pour plus d'informations sur les ROI.


include: include/timeout.md--

## Coordonnées et régions d'intérêt (ROI)

Les variables `cursor_x` et `cursor_y` contiennent l'emplacement du clic de souris.

Si vous indiquez un SKETCHPAD lié, la variable `cursor_roi` tiendra une liste de noms d'éléments séparés par des virgules qui contiennent la coordonnée cliquée. En d'autres termes, les éléments du SKETCHPAD servent automatiquement de régions d'intérêt pour le clic de la souris.

Si la correction d'une réponse dépend de la ROI qui a été cliquée, vous ne pouvez pas utiliser la variable `correct_response` pour cela, car cela se réfère actuellement uniquement au bouton de souris qui a été cliqué. Au lieu de cela, vous devez utiliser un script simple.

Dans un script Python INLINE_SCRIPT, vous pouvez faire cela comme suit :

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('correct!')
    correct = 1
else:
    print('incorrect!')
    correct = 0
```

Avec OSWeb en utilisant un INLINE_JAVASCRIPT, vous pouvez faire cela comme suit :

```js
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('correct!')
    correct = 1
} else {
    console.log('incorrect!')
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
  Collecte de clics de souris et utilisation des régions d'intérêt.

## Collecte de réponses de souris en Python

Vous pouvez utiliser l’objet `mouse` pour collecter des réponses de souris en Python :

- %link:manual/python/mouse%
