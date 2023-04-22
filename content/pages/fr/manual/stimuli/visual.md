title: Stimuli visuels
hash: 4ead1768298a015dc8af358675db670a71ea61876c2803a8998223c3509860c5
locale: fr
language: French

La façon la plus courante de présenter des stimuli visuels est d'utiliser l'élément SKETCHPAD, ou, pour les stimuli non critiques en termes de temps, l'élément FEEDBACK.

[TOC]

## Utilisation des éléments sketchpad et feedback

Les éléments SKETCHPAD et FEEDBACK offrent des outils de dessin basiques de type "ce que vous voyez est ce que vous obtenez" (%FigSketchpad).

%--
figure :
 id: FigSketchpad
 source: sketchpad.png
 caption: Le SKETCHPAD fournit des outils de dessin intégrés.
--%

## La différence entre les éléments sketchpad et feedback

Les éléments SKETCHPAD et FEEDBACK sont identiques à bien des égards, à l'exception de deux différences importantes.

### Les éléments Sketchpad sont préparés à l'avance, les éléments feedback ne le sont pas

Le contenu d'un SKETCHPAD est préparé pendant la phase de préparation de la SEQUENCE à laquelle il appartient. Cela est nécessaire pour garantir un timing précis : il permet au SKETCHPAD d'être affiché immédiatement pendant la phase d'exécution, sans aucun retard dû à la préparation du stimulus. Cependant, l'inconvénient de cela est que le contenu d'un SKETCHPAD ne peut pas dépendre de ce qui se passe pendant la SEQUENCE à laquelle il appartient. Par exemple, vous ne pouvez pas utiliser un SKETCHPAD pour fournir un retour immédiat sur le temps de réponse collecté par un élément KEYBOARD_RESPONSE (en supposant que le SKETCHPAD et le KEYBOARD_RESPONSE font partie de la même séquence).

En revanche, le contenu d'un élément FEEDBACK n'est préparé que lorsqu'il est effectivement affiché, c'est-à-dire pendant la phase d'exécution de la SEQUENCE à laquelle il appartient. Cela permet de fournir un retour d'information sur les événements qui viennent de se produire - d'où le nom. Cependant, l'élément FEEDBACK ne doit pas être utilisé pour présenter des stimuli critiques en termes de temps, car il souffre de retards dus à la préparation du stimulus.

Pour plus d'informations sur la stratégie de préparation-exécution, voir :

- %link:prepare-run%

### Les variables de retour d'information sont (par défaut) réinitialisées par les éléments feedback

L'élément FEEDBACK a une option "Réinitialiser les variables de feedback". Lorsque cette option est activée (elle l'est par défaut), les variables de feedback sont réinitialisées lorsque l'élément FEEDBACK est affiché.

Pour plus d'informations sur les variables de feedback, voir :

- %link:manual/variables%

## Présenter des stimuli visuels dans un script Python en ligne

### Accéder à un SKETCHPAD en Python

Vous pouvez accéder à l'objet `Canvas` pour un SKETCHPAD en tant que propriété `canvas` de l'élément. Par exemple, disons que votre SKETCHPAD s'appelle *my_sketchpad* et contient un élément image nommé 'my_image'. Vous pourriez alors faire pivoter cette image avec le script suivant :

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~

### Créer un Canvas en Python

Vous pouvez utiliser l'objet `Canvas` pour présenter des stimuli visuels en Python :

- %link:manual/python/canvas%