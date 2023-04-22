<div class="ClassDoc YAMLDoc" markdown="1">

# instance __responses__

L'objet `responses` contient l'historique des réponses qui ont été
collectées lors de l'expérience.

Un objet `responses` est créé automatiquement lorsque l'expérience commence.

En plus des fonctions listées ci-dessous, les sémantiques suivantes sont
prises en charge :

__Exemple__

~~~ .python
# Parcourir toutes les réponses, où les dernières réponses données apparaissent en premier
# Chaque réponse a des attributs corrects, réponse, temps_de_réponse, élément, et retour d'information.
for response in responses:
    print(response.correct)
# Imprimer les deux dernières réponses données
print('deux_dernières réponses :')
print(responses[:2])
~~~

[TOC]

## add(response=None, correct=None, response_time=None, item=None, feedback=True)

Ajoute une réponse.


__Paramètres__

- **réponse**: La valeur de la réponse, par exemple, 'espace' pour la barre d'espace, 0 pour le bouton 0 du joystick, etc.
- **correct**: La justesse de la réponse.
- **response_time**: Le temps de réponse.
- **item**: L'élément qui a collecté la réponse.
- **feedback**: Indique si la réponse doit être incluse dans les commentaires sur
la précision et le temps de réponse moyen.

__Exemple__

~~~ .python
responses.add(response_time=500, correct=1, response='gauche')
~~~



## clear(self)

Efface toutes les réponses.



__Exemple__

~~~ .python
responses.clear()
~~~



## reset_feedback(self)

Met l'état des commentaires de toutes les réponses à False, de sorte que seul
les nouvelles réponses seront incluses dans les commentaires.



__Exemple__

~~~ .python
responses.reset_feedback()
~~~



</div>