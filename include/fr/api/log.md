<div class="ClassDoc YAMLDoc" markdown="1">

# instance __log__

L'objet `log` permet l'enregistrement des données. Un objet `log` est créé automatiquement lorsque l'expérience commence.

__Exemple__

~~~ .python
# Écrire une ligne de texte
log.write('Mon message personnalisé')
# Écrire toutes les variables
log.write_vars()
~~~

[TOC]

## close(self)

Ferme le journal actuel.



__Exemple__

~~~ .python
log.close()
~~~



## open(path)

Ouvre le journal actuel. Si un journal était déjà ouvert, il est fermé
automatiquement et rouvert.


__Paramètres__

- **path**: Le chemin d'accès vers le journal actuel. Dans la plupart des cas (sauf) si un système d'enregistrement personnalisé est utilisé, ce sera un nom de fichier.

__Exemple__

~~~ .python
# Ouvrir un nouveau journal
log.open('/path/to/new/logfile.csv')
~~~



## write(msg, newline=True)

Écrire un message dans le journal.


__Paramètres__

- **msg**: Un message texte. Lors de l'utilisation de Python 2, cela doit être soit
  `unicode` ou un `str` encodé en utf-8. Lors de l'utilisation de Python 3, cela
  doit être soit `str` ou `bytes` encodé en utf-8.
- **newline**: Indique si un saut de ligne doit être écrit après le message.

__Exemple__

~~~ .python
# Écrire une seule chaîne de texte
log.write(f'time = {clock.time()}')
~~~



## write_vars(var_list=None)

Écrit les variables dans le journal.


__Paramètres__

- **var_list**: Une liste de noms de variables à écrire, ou None pour écrire toutes les variables
  qui existent dans l'expérience.

__Exemple__

~~~ .python
# Écrire toutes les variables dans le fichier journal
log.write_vars()
~~~



</div>