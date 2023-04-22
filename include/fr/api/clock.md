<div class="ClassDoc YAMLDoc" markdown="1">

# instance __clock__

L'objet `clock` offre des fonctions de base liées au temps. Un objet `clock` est
créé automatiquement lorsque l'expérience commence.

__Exemple__

~~~ .python
# Obtenir le timestamp avant et après avoir dormi pendant 1000 ms
t0 = clock.time()
clock.sleep(1000)
t1 = clock.time()
temps_passé = t1 - t0
print(f'Ceci devrait être 1000: {temps_passé}')
~~~

[TOC]

## loop_for(ms, throttle=None, t0=None)

*Nouveau dans v3.2.0*

Un itérateur qui boucle pendant un temps fixe.

__Paramètres__

- **ms**: Le nombre de millisecondes pendant lesquelles la boucle doit se dérouler.
- **throttle**: Une période de sommeil entre chaque itération.
- **t0**: Un temps de départ. Si `None`, le temps de départ est le moment au
lequel l'itération commence.

__Renvoie__

- 

__Exemple__

~~~ .python
for ms in clock.loop_for(100, throttle=10):
    print(ms)
~~~



## once_in_a_while(ms=1000)

*Nouveau dans v3.2.0*

Renvoie périodiquement `True`. Ceci est principalement utile
pour exécuter
du code (par exemple, dans une boucle `for`) qui ne doit être
exécuté qu'une
fois de temps en temps.

__Paramètres__

- **ms**: La période d'attente minimale.

__Renvoie__

- `True` après (au moins) la période d'attente minimale écoulée depuis
le dernier appel à `Clock.once_in_a_while()`, ou
`False` sinon.

__Exemple__

~~~ .python
for i in range(1000000):
    if clock.once_in_a_while(ms=50):
        # Exécuter ce code seulement une fois toutes les 50 ms
        print(clock.time())
~~~



## sleep(ms)

Dort (fait une pause) pendant une période.

__Paramètres__

- **ms**: Le nombre de millisecondes pendant lesquelles dormir.

__Exemple__

~~~ .python
# Créer deux objets canvas ...
my_canvas1 = Canvas()
my_canvas1.text('1')
my_canvas2 = Canvas()
my_canvas2.text('2')
# ... et les afficher avec 1 s d'intervalle
my_canvas1.show()
clock.sleep(1000)
my_canvas2.show()
~~~


## time()

Donne un horodatage actuel en millisecondes. La signification absolue de
l'horodatage (c'est-à-dire quand il était à 0) dépend du backend.



__Renvoie__

- Un horodatage.

__Exemple__

~~~ .python
t = clock.time()
print(f'Le temps actuel est {t}')
~~~


</div>
