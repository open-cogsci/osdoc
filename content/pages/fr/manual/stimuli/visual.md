title: Stimuli visuels
hash: 88ce873464207508e0ba22cecad7bdf4c51299ae1bf089ba96618c35389e13c2
locale: fr
language: French

La manière la plus courante de présenter des stimuli visuels est d'utiliser l'élément SKETCHPAD, ou, pour des stimuli non sensibles au temps, l'élément FEEDBACK.

[TOC]


## Utilisation des éléments sketchpad et feedback

Les éléments SKETCHPAD et FEEDBACK offrent des outils de dessin basiques what-you-see-is-what-you-get (%FigSketchpad).

%--
figure:
 id: FigSketchpad
 source: sketchpad.png
 caption: Le SKETCHPAD offre des outils de dessin intégrés.
--%


## Utilisation des expressions show-if

Vous pouvez utiliser des expressions show-if pour déterminer si un élément particulier doit être affiché ou non. Par exemple, si vous avez une image d'un visage joyeux qui ne doit être affichée que lorsque la variable `valence` a la valeur 'positive', alors vous pouvez définir l'expression show-if pour l'élément d'image correspondant à :

```python
valence == 'positive'
```

Si vous laissez une expression show-if vide ou entrez `True`, l'élément sera toujours affiché. Les expressions show-if utilisent la même syntaxe que les autres expressions conditionnelles. Pour plus d'informations, voir :

- %link:manual/variables%

Les expressions show-if sont évaluées au moment où l'affichage est préparé. Cela signifie que pour les éléments SKETCHPAD, elles sont évaluées pendant la phase de préparation, tandis que pour les éléments FEEDBACK, elles sont évaluées pendant la phase d'exécution (voir aussi la section ci-dessous).


## La différence entre les éléments sketchpad et feedback

Les éléments SKETCHPAD et FEEDBACK sont identiques à bien des égards, sauf pour deux différences importantes.


### Les éléments Sketchpad sont préparés à l'avance, les éléments feedback ne le sont pas

Le contenu d'un SKETCHPAD est préparé pendant la phase de préparation de la SEQUENCE dont il fait partie. Ceci est nécessaire pour assurer une synchronisation précise : Il permet au SKETCHPAD d'être affiché immédiatement pendant la phase d'exécution, sans aucun délai dû à la préparation du stimulus. Cependant, l'inconvénient de cela est que le contenu d'un SKETCHPAD ne peut pas dépendre de ce qui se passe pendant la SEQUENCE dont il fait partie. Par exemple, vous ne pouvez pas utiliser un SKETCHPAD pour fournir un retour d'information immédiat sur le temps de réponse recueilli par un élément KEYBOARD_RESPONSE (en supposant que le SKETCHPAD et le KEYBOARD_RESPONSE font partie de la même séquence.)

En revanche, le contenu d'un élément FEEDBACK est seulement préparé lorsqu'il est effectivement affiché, c'est-à-dire pendant la phase d'exécution de la SEQUENCE dont il fait partie. Cela permet de fournir un retour d'information sur des choses qui viennent de se produire - d'où son nom. Cependant, l'élément FEEDBACK ne devrait pas être utilisé pour présenter des stimuli sensibles au temps, car il souffre de retards dus à la préparation du stimulus.

Pour plus d'information sur la stratégie de préparation-exécution, voir :

- %link:prepare-run%


### Les variables de feedback sont (par défaut) réinitialisées par les éléments feedback

L'élément FEEDBACK a une option 'Reset feedback variables'. Lorsque cette option est activée (elle l'est par défaut), les variables de feedback sont réinitialisées lorsque l'élément FEEDBACK est affiché.

Pour plus d'informations sur les variables de feedback, voir :

- %link:manual/variables%


## Présentation des stimuli visuels en script Python inline

### Accéder à un SKETCHPAD en Python

Vous pouvez accéder à l'objet `Canvas` pour un SKETCHPAD comme la propriété `canvas` des items. Par exemple, disons que votre SKETCHPAD s'appelle *my_sketchpad*, et contient un élément d'image avec le nom 'my_image'. Vous pourriez alors faire tourner cette image avec le script suivant :

~~~ .python
my_canvas = items['my_sketchpad'].canvas
for angle in range(360):
	my_canvas['my_image'].rotation = angle
	my_canvas.show()
~~~


### Création d'un Canvas en Python

Vous pouvez utiliser l'objet `Canvas` pour présenter des stimuli visuels en Python :

- %link:manual/python/canvas%