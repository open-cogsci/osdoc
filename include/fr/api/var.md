<div class="ClassDoc YAMLDoc" markdown="1">

# instance __var__

__Nouveau en 4.0.0__: À partir d'OpenSesame 4.0, toutes les variables expérimentales sont
également disponibles dans l'espace de travail Python. Cela signifie que vous n'avez donc
plus besoin de l'objet `var`.

L'objet `var` fournit un accès aux variables expérimentales.
Les variables expérimentales sont les variables qui se trouvent dans l'interface graphique et sont
communément définies en tant que variables indépendantes dans l'élément LOOP, mentionnées
en utilisant la notation des crochets (`{ma_variable}`), et enregistrées par
l'élément LOGGER.

Un objet `var` est automatiquement créé lorsque l'expérience commence.
En plus des fonctions listées ci-dessous, les sémantiques suivantes sont
prises en charge :

__Exemple__ :

~~~ .python
# Définir une variable expérimentale
var.ma_variable = u'ma_valeur'
# Obtenir une variable expérimentale
print(u'Numéro du sujet = %d' % var.subject_nr)
# Supprimer (définir) une variable expérimentale
del var.ma_variable
# Vérifier si une variable expérimentale existe
si
u'ma_variable' dans var:
    print(u'ma_variable existe !')
# Parcourir toutes les
variables expérimentales
pour var_name dans var:
        print(u'variable trouvée :
%s' % var_name)
~~~

[TOC]

## clear(preserve=[])

*Nouveau en 3.1.2*

Efface toutes les variables expérimentales.

__Paramètres__

- **conserver**: Une liste des noms de variables qui ne doivent pas être effacés.

__Exemple__

~~~ .python
var.clear()
~~~



## get(var, default=None, _eval=True, valid=None)

Obtient une variable expérimentale.

__Paramètres__

- **var**: La variable à récupérer.
- **default**: Une valeur par défaut si la variable n'existe pas, ou `None` pour
aucune valeur par défaut.
- **_eval**: Détermine si la valeur retournée doit être évaluée pour les références de variable.
- **valid**: Une liste de valeurs valides, ou `None` pour autoriser toutes les valeurs.

__Exemple__

~~~ .python
print('ma_variable = %s' % var.get(u'ma_variable'))
# Équivalent à :
print('ma_variable = %s' % var.ma_variable)
# Mais si vous voulez passer des arguments-clés, vous devez utiliser `get()` :
var.get(u'ma_variable', default=u'une_valeur_par_defaut')
~~~



## has(var)

Vérifie si une variable expérimentale existe.

__Paramètres__

- **var**: La variable à vérifier.

__Exemple__

~~~ .python
if var.has(u'ma_variable'):
        print(u'ma_variable a été définie !')
# Équivalent à :
if u'ma_variable' in var:
        print(u'ma_variable a été définie !')
~~~



## inspect(self)

Génère une description de toutes les variables expérimentales, à la fois vivantes
et hypothétiques.

__Résultats__

- Un dictionnaire où les noms de variables sont des clés, et les valeurs sont des dictionnaires avec
source, valeur, et clés vivantes.


## items(self)

Retourne une liste de tuples (nom_variable, valeur). Voir `var.vars()`
pour une note sur le caractère non exhaustif de cette fonction.

__Résultats__

- Une liste de tuples (nom_variable, valeur).

__Exemple__

~~~ .python
for nom_variable, valeur in var.items():
        print(nom_variable, valeur)
~~~



## set(var, val)

Définit une variable expérimentale.

__Paramètres__

- **var**: La variable à assigner.
- **val**: La valeur à assigner.

__Example__

~~~ .python
var.set(u'ma_variable', u'ma_valeur')
# Équivalent à
var.ma_variable = u'ma_valeur'
~~~



## unset(var)

Supprime une variable.

__Paramètres__

- **var**: La variable à supprimer.

__Exemple__

~~~ .python
var.unset(u'ma_variable')
# Équivalent à :
del var.ma_variable
~~~



## vars(self)

Retourne une liste de variables expérimentales. Parce que les variables expérimentales
peuvent être stockées à plusieurs endroits, cette liste peut ne pas être
exhaustive. Autrement dit, `u'ma_var' in var` peut renvoyer `True`, tandis que
u'ma_var' n'est pas dans la liste de variables renvoyées par cette fonction.

__Résultats__

- Une liste de noms de variables.

__Exemple__

~~~ .python
for nom_variable in var.vars():
        print(nom_variable)
~~~



</div>
