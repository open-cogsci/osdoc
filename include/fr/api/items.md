<div class="ClassDoc YAMLDoc" markdown="1">

# instance __items__

L'objet `items` offre un accès de type dict aux éléments. Il est principalement
utile pour exécuter des éléments de manière programmatique.

Un objet `items` est créé automatiquement lorsque l'expérience commence.

En plus des fonctions répertoriées ci-dessous, les fonctionnalités suivantes sont
pris en charge:

__Exemple__

~~~ .python
# Préparer et exécuter un élément sketchpad de manière programmatique.
items.execute('mon_sketchpad')
# Vérifier si un élément existe
if 'mon_sketchpad' in items:
    print('mon_sketchpad existe')
# Supprimer un élément
del items['mon_sketchpad']
# Parcourir tous les noms d'éléments
for item_name in items:
    print(item_name)
~~~

[TOC]

## execute(name)

Exécute les phases de préparation et d'exécution d'un élément et met à jour le
pile d'éléments.

__Paramètres__

- **name**: Un nom d'élément.

__Exemple__

~~~ .python
items.execute('target_sketchpad')
~~~



## new(_type, name=None, script=None, allow_rename=True)

Crée un nouvel élément.

__Paramètres__

- **_type**: Le type d'élément.
- **name**: Le nom de l'élément, ou None pour choisir un nom unique basé sur le type d'élément.
- **script**: Un script de définition, ou None pour démarrer avec un élément vierge.
- **allow_rename**: Indique si OpenSesame peut utiliser un nom différent de celui
fourni en tant que `name` pour éviter les noms en double, etc.

__Renvoie__

- L'élément nouvellement généré.

__Exemple__

~~~ .python
items.new('sketchpad', name = 'mon_sketchpad')
items['mon_sketchpad'].prepare()
items['mon_sketchpad'].run()
~~~



## prepare(name)

Exécute la phase de préparation d'un élément et met à jour la pile d'éléments.

__Paramètres__

- **name**: Un nom d'élément.

__Exemple__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## run(name)

Exécute la phase d'exécution d'un élément et met à jour la pile d'éléments.

__Paramètres__

- **name**: Un nom d'élément.

__Exemple__

~~~ .python
items.prepare('target_sketchpad')
items.run('target_sketchpad')
~~~



## valid_name(item_type, suggestion=None)

Génère un nom unique qui est valide et ressemble au nom souhaité.

__Paramètres__

- **item_type**: Le type de l'élément pour lequel suggérer un nom.
- **suggestion**: Le nom souhaité, ou None pour choisir un nom basé sur le type de l'élément.

__Renvoie__

- Un nom unique.

__Exemple__

~~~ .python
valid_name = items.valid_name('sketchpad', 'un nom invalide')
~~~



</div>