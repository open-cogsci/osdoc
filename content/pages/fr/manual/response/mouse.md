title: Réponses de souris et tactiles
hash: d6f7dcf58a399be886fd23f0ed29e9898c1beae44c3c8f6d076e26f96471d4f0
locale: fr
language: French

Les réponses de souris sont collectées avec l’item MOUSE_RESPONSE. Le MOUSE_RESPONSE est principalement destiné à collecter des clics de souris individuels. Sur les appareils tactiles, les réponses tactiles (item TOUCH_RESPONSE) sont généralement enregistrées de la même manière que les clics du bouton-1 de la souris aux coordonnées touchées ; le même item et la même logique peuvent donc souvent être utilisés à la fois pour les entrées souris et tactiles. Si vous souhaitez collecter des trajectoires du curseur de la souris, jetez un œil aux plugins MOUSETRAP :

- %link:mousetracking%

[TOC]


## Variables de réponse

Le MOUSE_RESPONSE définit les variables de réponse standard comme décrit ici :

- %link:manual/variables%

En outre, les variables suivantes sont pertinentes pour les réponses de souris et tactiles :

| Variable | Description |
|---|---|
| `response` | Le bouton de la souris sur lequel on a cliqué. Cette valeur est stockée sous forme de nombre (`1` = bouton gauche, `2` = bouton du milieu, `3` = bouton droit, `4` = défilement vers le haut, `5` = défilement vers le bas). En cas de timeout, `response` est définie sur `None`. |
| `response_time` | Le temps de réponse en millisecondes, ou le temps de timeout enregistré si aucune réponse n’a été donnée. |
| `correct` | Définie automatiquement en fonction de la justesse du bouton : `1` pour une réponse correcte du bouton de souris, `0` pour une réponse incorrecte du bouton de souris ou un timeout, et `undefined` si aucune réponse correcte n’est spécifiée. |
| `cursor_x` | La coordonnée x du clic ou du toucher. |
| `cursor_y` | La coordonnée y du clic ou du toucher. |
| `cursor_roi` | Une liste, séparée par des points-virgules, des noms des éléments de sketchpad qui contiennent les coordonnées cliquées. Si des éléments se chevauchent, plusieurs noms peuvent être listés. Cette variable indique où le clic a eu lieu ; elle ne détermine pas automatiquement `correct`. |


## Noms des boutons de la souris

Les boutons de la souris ont un numéro (`1`, etc.) ainsi qu’un nom (`left_button`, etc.). Les deux peuvent être utilisés pour spécifier les réponses correctes et autorisées, mais la variable `response` sera définie sur un nombre.

- `left_button` correspond à `1`
- `middle_button` correspond à `2`
- `right_button` correspond à `3`
- `scroll_up` correspond à `4`
- `scroll_down` correspond à `5`


## Réponse correcte

Le champ *Correct response* indique quelle réponse est considérée comme correcte. Après une réponse correcte, la variable `correct` est automatiquement définie sur 1 ; après une réponse incorrecte ou un timeout (c.-à-d. tout le reste), `correct` est définie sur 0 ; si aucune réponse correcte n’est spécifiée, `correct` est définie sur 'undefined'.

Vous pouvez indiquer la réponse correcte de trois manières principales :

- *Laissez le champ vide.* Si vous laissez le champ *Correct response* vide, OpenSesame vérifiera automatiquement si une variable appelée `correct_response` a été définie et, si c’est le cas, utilisera cette variable comme réponse correcte.
- *Saisissez une valeur littérale.* Vous pouvez saisir explicitement une réponse, comme 1. Cela n’est utile que si la réponse correcte est fixe.
- *Saisissez un nom de variable.* Vous pouvez saisir une variable, telle que '{cr}'. Dans ce cas, cette variable sera utilisée comme réponse correcte.

Notez que la réponse correcte se rapporte au bouton de la souris sur lequel on a cliqué, et non à la région d’intérêt cliquée (ROI). Si la justesse dépend de l’emplacement cliqué plutôt que du bouton de la souris, vous devez déterminer vous-même la justesse sur la base de `cursor_roi` ; voir la section ci-dessous pour plus d’informations sur les ROI.


## Réponses autorisées

Le champ *Allowed responses* indique une liste de réponses autorisées. Toutes les autres réponses seront ignorées, à l’exception de 'Escape', qui mettra l’expérience en pause. Les réponses autorisées doivent être une liste de réponses séparées par des points-virgules, comme '1;3' pour autoriser les boutons gauche et droit de la souris. Pour accepter toutes les réponses, laissez le champ *Allowed responses* vide.

Notez que les réponses autorisées se rapportent au bouton de la souris qui peut être cliqué, et non à la région d’intérêt qui peut être cliquée (ROI) ; voir la section ci-dessous pour plus d’informations sur les ROI.


%--include: include/timeout.md--%

## Coordinates and regions of interest (ROIs)</notranslate>

Les variables `cursor_x` et `cursor_y` contiennent l’emplacement du clic de souris.

Si vous indiquez un SKETCHPAD lié, la variable `cursor_roi` contiendra une liste, séparée par des points-virgules, des noms des éléments qui contiennent la coordonnée cliquée. Autrement dit, les éléments du SKETCHPAD servent automatiquement de régions d’intérêt pour le clic de souris.

La variable `cursor_roi` indique où le clic a eu lieu, tandis que `response` indique quel bouton de la souris a été cliqué. Si plusieurs éléments nommés se chevauchent à l’emplacement cliqué, `cursor_roi` peut contenir plusieurs noms d’éléments.

Si la correction d’une réponse dépend du ROI qui a été cliqué, vous ne pouvez pas utiliser la variable `correct_response` pour cela, car elle renvoie uniquement au bouton de souris qui a été cliqué. À la place, vous devez utiliser un script simple pour déterminer la correction sur la base de `cursor_roi` et, si nécessaire, remplacer `correct`.

Dans un Python INLINE_SCRIPT, vous pouvez faire ceci comme suit :

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

Avec OSWeb en utilisant un INLINE_JAVASCRIPT, vous pouvez faire ceci comme suit :

```javascript
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

Ici, `'my_roi'` est simplement un nom d’exemple d’un élément de sketchpad. Dans une expérience réelle, remplacez-le par le nom du ROI qui doit être considéré comme correct. Pour éviter toute ambiguïté, les éléments nommés doivent être uniques dans un sketchpad.


## Réponses tactiles

Sur les appareils tactiles, chaque appui est généralement enregistré comme une réponse mouse-button-1 aux coordonnées touchées. Cela signifie que l’item MOUSE_RESPONSE peut souvent être utilisé à la fois pour les clics de souris et les appuis tactiles sans autre modification.

En pratique, cela signifie qu’une réponse tactile se comporte comme suit :

- Le bouton est généralement enregistré comme `1`
- L’emplacement du toucher est stocké dans `cursor_x` et `cursor_y`
- Si un sketchpad est lié, les éléments touchés peuvent être identifiés via `cursor_roi`

Cela peut être utile pour les expériences qui doivent fonctionner à la fois sur des ordinateurs de bureau et sur des appareils à écran tactile.

### Exemple : réponses tactiles avec MOUSE_RESPONSE

Par exemple, considérons une tâche de choix simple dans laquelle deux grands éléments de sketchpad sont affichés sur les côtés gauche et droit de l’écran. Si le participant touche l’élément de gauche sur un écran tactile :

- `response` sera généralement défini sur `1`
- `cursor_x` et `cursor_y` contiendront les coordonnées du toucher
- `cursor_roi` peut contenir le nom de l’élément touché, par exemple `left_option`

Cela signifie que l’entrée tactile peut être gérée de la même manière qu’une entrée souris. Si la correction dépend de l’élément touché plutôt que du bouton, vous pouvez utiliser la même logique `cursor_roi` décrite ci-dessus.

### Exemple : utilisation du plug-in `touch_response`

Pour les expériences où vous souhaitez diviser l’écran en régions de réponse discrètes (par ex. une grille de boutons), le plug-in `touch_response` offre une approche plus simple et plus pratique que le travail avec des coordonnées brutes. Il divise l’affichage en une grille de lignes et de colonnes, et encode chaque réponse comme un nombre unique, en comptant de gauche à droite et de haut en bas.

Par exemple, avec 2 colonnes et 3 lignes, l’affichage est divisé comme suit :

| | Colonne 1 | Colonne 2 |
|---|---|---|
| **Ligne 1** | 1 | 2 |
| **Ligne 2** | 3 | 4 |
| **Ligne 3** | 5 | 6 |

Ainsi, si vous spécifiez 2 colonnes et 1 ligne, l’affichage est divisé en deux régions de réponse :

| Moitié gauche | Moitié droite |
|---|---|
| `1` | `2` |

Dans une tâche simple oui/non, vous pourriez attribuer :

- `1` = Oui
- `2` = Non

Si la bonne réponse est Oui, définissez le champ *Correct response* sur `1`. OpenSesame définira alors automatiquement `correct` sur 1 lorsque le participant touche la moitié gauche de l’écran.

> [!NOTE]
> Le plug-in `touch_response` n’utilise pas d’éléments sketchpad nommés ni `cursor_roi`. Les réponses sont encodées uniquement comme positions de grille.

> [!NOTE]
> Le comportement exact de l’entrée tactile peut dépendre de la plateforme et du backend utilisés pour exécuter l’expérience.

> [!NOTE]
> L’item MOUSE_RESPONSE ne capture qu’une seule réponse tactile. Si plusieurs doigts touchent l’écran simultanément, une seule réponse est enregistrée.


%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Collecting mouse clicks and using regions of interest.
--%

## Recueillir les réponses de la souris en Python

Vous pouvez utiliser l’objet `mouse` pour recueillir les réponses de la souris en Python :

- %link:manual/python/mouse%