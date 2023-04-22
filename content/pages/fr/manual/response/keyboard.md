title: Réponses au clavier
hash: 23ed6413bd7bc9180b1e3a384c25c3f89c817414a4460a00260be06f5698474a
locale: fr
language: French

Les réponses au clavier sont collectées avec l'élément KEYBOARD_RESPONSE.

[TOC]


## Variables de réponse

Le KEYBOARD_RESPONSE définit les variables de réponse standard comme décrit ici :

- %link:manual/variables%

## Noms de touches

Les touches sont généralement identifiées par leur caractère et/ou leur description (selon le cas). Par exemple :

- La touche `/` est nommée 'slash' et '/'. Vous pouvez utiliser l'un ou l'autre des deux noms.
- La touche `a` est nommée 'a'.
- La touche flèche gauche est nommée 'left'.

Si vous ne savez pas comment s'appelle une touche particulière, vous pouvez :

- Cliquer sur le bouton 'Liste des touches disponibles' ; ou
- Créer une expérience simple dans laquelle un KEYBOARD_RESPONSE est immédiatement suivi d'un élément FEEDBACK avec le texte '{response}' dessus. Cela montrera le nom de la réponse précédemment collectée.


## Réponse correcte

Le champ *Réponse correcte* indique quelle réponse est considérée comme correcte. Après une réponse correcte, la variable `correct` est automatiquement définie sur 1 ; après une réponse incorrecte (c'est-à-dire autre chose), `correct` est défini sur 0 ; si aucune réponse correcte n'est spécifiée, `correct` est défini sur 'undefined'.

Vous pouvez indiquer la réponse correcte de trois manières principales :

- *Laissez le champ vide.* Si vous laissez le champ *Réponse correcte* vide, OpenSesame vérifiera automatiquement si une variable appelée `correct_response` a été définie et, le cas échéant, utilisera cette variable pour la réponse correcte.
- *Entrez une valeur littérale.* Vous pouvez entrer explicitement une réponse, comme 'left' dans le cas d'un élément KEYBOARD_RESPONSE. Cela n'est utile que si la réponse correcte est fixe.
- *Entrez un nom de variable.* Vous pouvez entrer une variable, comme '{cr}'. Dans ce cas, cette variable sera utilisée pour la réponse correcte.


## Réponses autorisées

Le champ *Réponses autorisées* indique une liste de réponses autorisées. Toutes les autres réponses seront ignorées, sauf 'Échap', qui mettra en pause l'expérience. Les réponses autorisées doivent être une liste de réponses séparées par des points-virgules, comme 'a;left;/' pour un KEYBOARD_RESPONSE. Pour accepter toutes les réponses, laissez le champ *Réponses autorisées* vide.

%--include: include/timeout.md--%

## Collecter des réponses au clavier en Python

Vous pouvez utiliser l'objet `keyboard` pour collecter des réponses au clavier en Python :

- %link:manual/python/keyboard%