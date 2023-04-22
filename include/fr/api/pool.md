<div class="ClassDoc YAMLDoc" markdown="1">

# instance __pool__

L'objet `pool` offre un accès de type dict au pool de fichiers. Lors
de la vérification de la présence d'un fichier dans le pool de fichiers, plusieurs dossiers sont
recherchés.
Pour plus de détails, voir `pool.folders()`.

Un objet `pool` est créé
automatiquement lorsque l'expérience démarre.

En plus des fonctions
répertoriées ci-dessous, les sémantiques suivantes sont
prises en charge :

__Exemples__

Utilisation de base :

~~~ .python
# Obtenir le chemin complet d'un fichier dans le pool de fichiers
print(f'Le chemin complet du fichier img.png est {pool["img.png"]}')
# Vérifier si un fichier est dans le pool de fichiers
if 'img.png' in pool:
    print('img.png est dans le pool de fichiers')
# Supprimer un fichier du pool de fichiers
del pool['img.png']
# Parcourir tous les fichiers du pool de fichiers. Ceci récupère les chemins complets.
for path in pool:
    print(path)
# Vérifier le nombre de fichiers dans le pool de fichiers
print(f'Il y a {len(pool)} fichiers dans le pool de fichiers')
~~~

Obtenir une image du pool de fichiers et utiliser un `Canvas` pour l'afficher.

~~~ .python
image_path = pool['img.png']
mon_canvas = Canvas()
mon_canvas.image(image_path)
mon_canvas.show()
~~~

[TOC]

## add(path, new_name=None)

Copie un fichier dans le pool de fichiers.

__Paramètres__

- **path**: Le chemin complet du fichier sur le disque.
- **new_name**: Un nouveau nom pour le fichier dans le pool, ou None pour utiliser le nom original du fichier.

__Exemple__

~~~ .python
pool.add('/home/username/Pictures/my_img.png')
~~~



## clean_up(self)

Supprime le dossier du pool.




## fallback_folder(self)

Le chemin complet du dossier de secours du pool, qui est le
sous-dossier `__pool__` du dossier de l'expérience en cours, ou
`None` si ce dossier n'existe pas. Le dossier de secours du pool
est surtout utile en combinaison avec un système de versionnement
tel que git, car il permet de sauvegarder l'expérience sous forme de fichier
texte brut, même lorsqu'il y a des fichiers
dans le pool de fichiers.

__Renvoie__

-

__Exemple__

~~~ .python
if pool.fallback_folder() is not None:
    print('Il y a un dossier de pool de secours !')
~~~



## files(self)

Renvoie tous les fichiers dans le pool de fichiers.

__Renvoie__

- Une liste de chemins complets.

__Exemple__

~~~ .python
for path in pool.files():
    print(path)
# Équivalent à :
for path in pool:
    print(path)
~~~



## folder(self)

Donne le chemin complet du dossier (principal) du pool. Il s'agit généralement d'un
dossier temporaire qui est supprimé lorsque l'expérience est terminée.

__Renvoie__

- Le chemin complet du dossier principal du pool.

__Exemple__

~~~ .python
print(f'Le dossier du pool se trouve ici: {pool.folder()}')
~~~



## folders(include_fallback_folder=True, include_experiment_path=False)

Donne une liste de tous les dossiers qui sont recherchés lors de la récupération du
chemin complet d'un fichier. Ceux-ci sont (par ordre d'apparition) :

1. Le dossier du pool de fichiers
lui-même, tel que renvoyé par `pool.folder()`.
2. Le dossier de l'expérience en cours (s'il existe)
3. Le dossier de secours du pool, tel que renvoyé par
`pool.fallback_folder()` (s'il existe)

__Paramètres__

- **include_fallback_folder**: Indique si le dossier de pool de secours doit être inclus s'il
existe.
- **include_experiment_path**: Indique si le dossier de l'expérience doit être inclus s'il
existe.

__Renvoie__

- Une liste de tous les dossiers.

__Exemple__

~~~ .python
print('Les dossiers suivants sont recherchés pour les fichiers :')
for dossier in pool.folders():
    print(dossier)
~~~



## in_folder(path)

Vérifie si le chemin est dans le dossier du pool. Ceci est différent de
la syntaxe `path in pool` en ce sens qu'elle vérifie uniquement le dossier principal du pool,
et non pas le dossier de secours du pool et le dossier de l'expérience.

__Paramètres__

- **path**: Un nom de fichier de base à vérifier.

__Renvoie__

-

__Exemple__

~~~ .python
print(pool.in_folder('cue.png'))
~~~



## rename(old_path, new_path)

Renomme un fichier dans le dossier du pool.

__Paramètres__

- **old_path**: L'ancien nom du fichier.
- **new_path**: Le nouveau nom du fichier.

__Exemple__

~~~ .python
pool.rename('my_old_img.png', 'my_new_img.png')
~~~



## size(self)

Obtient la taille combinée en octets de tous les fichiers du pool de fichiers.

__Renvoie__

-

__Exemple__

~~~ .python
print(f'La taille du pool de fichiers est de {pool.size()} octets')
~~~

</div>