<div class="ClassDoc YAMLDoc" markdown="1">

# instance __horloge__

L'objet `horloge` offre des fonctions de temps de base. Un objet `horloge` est
créé automatiquement lorsque l'expérience commence.

__Exemple__

~~~ .python
# Obtenez le timestamp avant et après avoir dormi pendant 1000 ms
t0 = horloge.temps()
horloge.dors(1000)
t1 = horloge.temps()
temps_passé = t1 - t0
print(f'Ceci doit être égal à 1000 : {temps_passé}')
~~~

[TOC]

## boucle_pour(ms, régulateur=None, t0=None)

*Nouveau dans la v3.2.0*

Un itérateur qui boucle pendant un temps fixe.

__Paramètres__

- **ms**: Le nombre de millisecondes à boucler.
- **régulateur**: Une période de sommeil entre chaque itération.
- **t0**: Un temps de départ. Si `None`, le temps de départ est le moment où 
l'itération commence.

__Renvoie__

-

__Exemple__  

~~~ .python
for ms in horloge.boucle_pour(100, régulateur=10):
    print(ms)
~~~


## de_temps_en_temps(ms=1000)

*Nouveau dans la v3.2.0*

Renvoie périodiquement `Vrai`. Ceci est principalement utile
pour exécuter
du code (par exemple, dans une boucle `for`) qui ne devrait être
exécuté que 
de temps en temps.

__Paramètres__

- **ms**: La période minimale d'attente.

__Renvoie__

- `Vrai` après (au moins) la période minimale d'attente depuis
le dernier appel à `Horloge.de_temps_en_temps()`, ou
`Faux` sinon.

__Exemple__

~~~ .python
for i in range(1000000):
    if horloge.de_temps_en_temps(ms=50):
        # Exécutez ce code seulement une fois toutes les 50 ms
        print(horloge.temps())
~~~



## dors(ms)

Dort (fait une pause) pendant une période.


__Paramètres__

- **ms**: Le nombre de millisecondes pour dormir.

__Exemple__

~~~ .python
# Créez deux objets canvas ...
mon_canvas1 = Canvas()
mon_canvas1.texte('1')
mon_canvas2 = Canvas()
mon_canvas2.texte('2')
# ... Montrez-les avec un intervalle de 1 s
mon_canvas1.montre()
horloge.dors(1000)
mon_canvas2.montre()
~~~



## temps(self)

Donne un horodatage actuel en millisecondes. La signification absolue de l'horodatage (c'est-à-dire quand il était à 0) dépend du backend.



__Renvoie__

- Un horodatage.

__Exemple__

~~~ .python
t = horloge.temps()
print(f'Le temps actuel est {t}')
~~~



</div>