title: Réponses de la souris
hash: 9e348c65c44cf1d0e1e152976c013b0a235f432d16ceeb3fff09001f8c9d0e7b
locale: fr
language: French

Les réponses de la souris sont collectées avec l'élément MOUSE_RESPONSE. Le MOUSE_RESPONSE est principalement destiné à collecter des clics de souris individuels. Si vous souhaitez collecter des trajectoires de curseur de souris, jetez un œil aux plugins MOUSETRAP :

- %link:mousetracking%

[TOC]

## Variables de réponse

Le MOUSE_RESPONSE définit les variables de réponse standard comme décrit ici :

- %link:manual/variables%

## Noms des boutons de la souris

Les boutons de la souris ont un numéro (`1`, etc.) ainsi qu'un nom (`left_button`, etc.). Les deux peuvent être utilisés pour spécifier des réponses correctes et autorisées, mais la variable `response` sera définie sur un nombre.

- `left_button` correspond à `1`
- `middle_button` correspond à `2`
- `right_button` correspond à `3`
- `scroll_up` correspond à `4`
- `scroll_down` correspond à `5`

## Réponse correcte

Le champ *Réponse correcte* indique quelle réponse est considérée comme correcte. Après une réponse correcte, la variable `correct` est automatiquement définie sur 1 ; après une réponse incorrecte ou un délai d'attente (c'est-à-dire tout le reste), `correct` est défini sur 0 ; si aucune réponse correcte n'est spécifiée, `correct` est défini sur "indéfini".

Vous pouvez indiquer la réponse correcte de trois manières principales :

- *Laissez le champ vide.* Si vous laissez le champ *Réponse correcte* vide, OpenSesame vérifiera automatiquement si une variable appelée `correct_response` a été définie et, si c'est le cas, utilisera cette variable pour la réponse correcte.
- *Entrez une valeur littérale.* Vous pouvez entrer explicitement une réponse, comme 1. Ceci n'est utile que si la réponse correcte est fixe.
- *Entrez un nom de variable.* Vous pouvez entrer une variable, comme '{cr}'. Dans ce cas, cette variable sera utilisée pour la réponse correcte.

## Réponses autorisées

Le champ *Réponses autorisées* indique une liste de réponses autorisées. Toutes les autres réponses seront ignorées, sauf "Escape", qui mettra en pause l'expérience. Les réponses autorisées doivent être une liste de réponses séparées par des points-virgules, comme "1;3" pour autoriser les boutons gauche et droit de la souris. Pour accepter toutes les réponses, laissez le champ *Réponses autorisées* vide.

%--include: include/timeout.md--%

## Coordonnées et régions d'intérêt (ROI)

Les variables `cursor_x` et `cursor_y` conservent l'emplacement du clic de la souris.

Si vous indiquez un SKETCHPAD lié, la variable `cursor_roi` contiendra une liste séparée par des virgules des noms des éléments qui contiennent la coordonnée cliquée. En d'autres termes, les éléments du SKETCHPAD servent automatiquement de régions d'intérêt pour le clic de souris.

%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Collecte des clics de souris et utilisation des régions d'intérêt.
--%

## Collecte des réponses de la souris en Python

Vous pouvez utiliser l'objet `mouse` pour collecter des réponses de souris en Python :

- %link:manual/python/mouse%
