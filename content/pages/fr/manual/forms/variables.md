title: Variables de formulaire
hash: 5699e805a79ad2de0de21343a912e41c96c96935e89844f6af55864fcb4864cc
locale: fr
language: French

[TOC]

## À propos des variables de formulaire

Lorsque vous présentez un formulaire avec plusieurs `checkbox`, vous voulez généralement savoir quelle `checkbox` l'utilisateur a coché. De même, lorsque vous présentez un formulaire avec deux `button`s, vous voulez savoir quel `button` l'utilisateur a cliqué. Cette information est disponible via des variables qui sont automatiquement définies lorsque l'utilisateur interagit avec un formulaire. Vous pouvez spécifier vous-même quelles variables de réponse doivent être utilisées. La manière dont cela se fait dépend de la manière dont vous avez créé votre formulaire.

### Dans les plugins de formulaire prêts à l'emploi

Lorsque vous utilisez l'un des plugins de formulaire prêts à l'emploi, tels que FORM_TEXT_INPUT, vous pouvez spécifier le nom de la variable de réponse directement dans les contrôles du plugin.

### Dans les formulaires personnalisés

Vous pouvez utiliser le mot-clé `var` pour indiquer quelle variable doit être utilisée. Par exemple, le script OpenSesame suivant, que vous pouvez entrer dans un plugin FORM_BASE, indique que la réponse d'un widget `text_input` doit être stockée dans une variable appelée `my_response_var` :

```python
widget 0 0 1 1 text_input var=my_response_var
```

Le code Python équivalent est :

~~~ .python
my_widget = TextInput(var='my_response_var')
~~~

Voir aussi :

- %link:manuel/forms/widgets%

## Informations spécifiques au widget

Chaque widget utilise sa variable de réponse d'une manière légèrement différente.

### button

Le widget `button` définit la variable de réponse sur 'yes' s'il a été cliqué et sur 'no' s'il ne l'a pas été.

### checkbox

Le widget `checkbox` définit la variable de réponse sur une liste séparée par des points-virgules du texte de toutes les cases à cocher qui ont été cochées (pour cette variable), ou sur 'no' si aucune `checkbox` n'a été cochée (pour cette variable). Cela peut sembler un peu compliqué, donc voyons quelques exemples.

```python
widget 0 0 1 1 checkbox group="1" text="A" var="my_response_var"
widget 1 0 1 1 checkbox group="1" text="B" var="my_response_var"
widget 1 1 1 1 button text="Suivant"
```

Ici, il y a deux `checkbox` avec le texte 'A' et 'B'. Les deux font partie du même groupe, appelé '1'. Les deux ont la même variable de réponse, appelée `my_response_var`. Si 'A' est cochée, `my_response_var` sera 'A'. Si 'B' est cochée, `my_response_var` sera 'B'. Si aucune n'est cochée, `my_response_var` sera 'no'. Notez que seulement une `checkbox` dans le même groupe peut être cochée, donc `my_response_var` ne sera *jamais* 'A;B' dans cet exemple.

Considerons maintenant le même script, avec la seule différence que les deux `checkbox` ne font pas partie d'un groupe :

```python
widget 0 0 1 1 checkbox text="A" var="my_response_var"
widget 1 0 1 1 checkbox text="B" var="my_response_var"
widget 1 1 1 1 button text="Suivant"
```

Dans ce cas, la situation est beaucoup comme décrit ci-dessus, à l'exception que les deux `checkbox` peuvent être cochées en même temps, auquel cas `my_response_var` sera définie sur 'A;B'.

Vous ne pouvez pas utiliser la même variable de réponse pour les `checkbox` dans différents groupes.

### image

Les variables ne sont pas applicables au widget `image`.

### image_button

Le widget `image_button` définit la variable de réponse sur 'yes' s'il a été cliqué et sur 'no' s'il ne l'a pas été.

### label

Les variables ne sont pas applicables au widget `label`.

### rating_scale

Le widget `rating_scale` définit la variable de réponse sur le numéro de l'option qui a été cliquée, où '0' est la première option (indexation à partir de zéro). Si aucune option n'a été sélectionnée, la variable de réponse est définie sur 'None'.

### text_input

Le widget `text_input` définit la variable de réponse sur le texte saisi.