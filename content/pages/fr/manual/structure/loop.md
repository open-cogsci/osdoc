title: Bouclage et variables indépendantes
hash: f52d2b6f370a4abedc40605527622cea0ff9e57163ef51e6d8d4e39ff35789ec
locale: fr
language: French

L'élément LOOP a deux fonctions importantes :

- Il exécute un autre élément plusieurs fois.
- C'est là que vous définissez généralement vos variables indépendantes ; c'est-à-dire les variables que vous manipulez dans votre expérience.

[TOC]

## L'élément à exécuter

Un LOOP est toujours connecté à un autre élément : l'élément à exécuter. Vous sélectionnez l'élément à exécuter dans la case étiquetée "Exécuter". Dans la plupart des cas, l'élément à exécuter est une SEQUENCE, qui exécute plusieurs éléments séquentiellement.

Deux structures SEQUENCE-LOOP courantes sont :

- Si une SEQUENCE correspond à un seul essai (par convention appelé *trial_sequence*), alors un LOOP connecté à cette séquence correspond à plusieurs essais, ou un bloc (par convention appelé *block_loop*).
- Si une SEQUENCE correspond à un bloc d'essais suivis d'un affichage de feedback (par convention appelé *block_sequence*), alors un loop connecté à cette séquence correspond à plusieurs blocs, ou une session expérimentale complète (par convention appelée *experimental_loop*).

## Définition des variables indépendantes

Le tableau de loop est un moyen simple et puissant de définir des variables indépendantes. Chaque colonne du tableau correspond à une variable; chaque ligne correspond à un cycle, c'est-à-dire un niveau de la variable. Par exemple, une boucle simple avec une variable (`animal`) comportant deux cycles ("chat" et "chien") ressemble à ceci :

animal |
------ |
chat    |
chien    |

Le loop a quelques options importantes :

*Répéter* indique combien de fois chaque cycle doit être exécuté. Dans l'exemple ci-dessus, répéter est réglé sur 2, ce qui signifie que *trial_sequence* est appelé deux fois alors que la variable `animal` a la valeur "chat", et deux fois alors que `animal` a la valeur "chien" (quatre fois en tout).

*Ordre* indique si les cycles doivent être exécutés séquentiellement ou dans un ordre aléatoire. La randomisation est complète, dans le sens où la liste complète des essais nombre-de-cycles × répétition est randomisée.

## Lecture des variables indépendantes à partir d'un fichier

Si vous souhaitez lire des variables indépendantes à partir d'un fichier plutôt que de les entrer dans le tableau de loop, vous pouvez procéder comme suit :

- Réglez *Source* sur *fichier*.
- Sélectionnez un fichier Excel (`.xlsx`) ou CSV (`.csv`) dans l'entrée *Fichier*.

Le fichier source suit les mêmes conventions que le tableau de loop ; c'est-à-dire que chaque colonne correspond à une variable et chaque ligne correspond à un cycle.

Les fichiers CSV doivent être au format suivant :

- texte brut
- séparés par des virgules
- entre guillemets doubles (les guillemets doubles littéraux sont échappés par des barres obliques inverses)
- encodé en UTF-8

## Interrompre la boucle

Si vous souhaitez interrompre la boucle avant que tous les cycles aient été exécutés, vous pouvez spécifier une expression break-if. Cette expression break-if suit la même syntaxe que les autres expressions conditionnelles, telles que décrites sur :

- %link:manual/variables%

Par exemple, l'instruction break-if suivante interromprait la boucle dès qu'une réponse correcte est donnée :

```python
correct == 1
```

L'option *Évaluer au premier cycle* indique si l'instruction break-if doit être évaluée avant le premier cycle, auquel cas aucun cycle peut ne pas être exécuté du tout, ou seulement avant le deuxième cycle, auquel cas au moins un cycle est toujours exécuté. Dans certains cas, l'instruction break-if fera référence à une variable qui n'est définie qu'après le premier cycle, auquel cas vous devez désactiver l'option 'Évaluer au premier cycle' pour éviter une erreur 'Variable does not exist'.

## Génération d'un plan factoriel complet

En cliquant sur le *Plan factoriel complet*, vous ouvrez un assistant qui vous permet de générer facilement un plan factoriel complet, c'est-à-dire un plan dans lequel chaque combinaison de facteurs se produit.

## Pseudorandomisation

Vous pouvez ajouter des contraintes de pseudorandomisation au script de l'élément loop. Cela permet de mélanger les lignes, même si l'ordre est réglé sur séquentiel. (Actuellement, cela n'est pas possible via l'interface graphique.)

Exemple : Assurez-vous que les répétitions du même mot (donné par la variable `word`) sont séparées par au moins 4 cycles :

```python
constrain word mindist=4
```

Exemple: Assurez-vous que le même mot n'est pas répété:

```python
constrain word maxrep=1
```

Les commandes `constrain` doivent venir *après* les commandes `setcycle`.

## Opérations avancées sur les boucles

Les commandes pour les opérations avancées sur les boucles doivent venir *après* les commandes `constrain` et `setcycle`.

### fullfactorial

L'instruction `fullfactorial` traite la table de boucle comme l'entrée pour un plan factoriel complet. Par exemple, la table de boucle suivante:

cue   | duration
----- | --------
left  | 0
right | 100
      | 200

Donnera comme résultat:

cue   | duration
----- | --------
left  | 0
left  | 100
left  | 200
right | 0
right | 100
right | 200

### shuffle

`shuffle` sans argument mélange toute la table. Lorsqu'un nom de colonne est spécifié (`shuffle cue`), seule cette colonne est mélangée.

### shuffle_horiz

`shuffle_horiz` mélange toutes les colonnes horizontalement. Lorsque plusieurs colonnes sont spécifiées, seules ces colonnes sont mélangées horizontalement.

Par exemple, lorsque `shuffle_horiz word1 word2` est appliqué à la table suivante :

word1 | word2 | word3
----- | ----- | -----
cat   | dog   | bunny
cat   | dog   | bunny
cat   | dog   | bunny

Le résultat pourrait être (c'est-à-dire que les valeurs sont échangées de manière aléatoire entre `word1` et `word2`, mais pas `word3`):

word1 | word2 | word3
----- | ----- | -----
dog   | cat   | bunny
dog   | cat   | bunny
cat   | dog   | bunny

### slice

`slice [from] [to]` sélectionne une partie de la boucle. Il nécessite un indice de début et de fin, où 0 est la première ligne et les valeurs négatives sont comptées à partir de la fin vers l'arrière. (Comme dans le découpage de liste en Python, en d'autres termes.)

Par exemple, lorsque `slice 1 -1` est appliqué à la table suivante :

word  |
----- |
cat   |
dog   |
bunny |
horse |

Le résultat serait:

word  |
----- |
dog   |
bunny |

### sort

`sort [column]` trie une seule colonne, sans modifier les autres colonnes.

### sortby

`sortby [column]` trie la table entière par une seule colonne.

### reverse

` reverse` inverse l'ordre de toute la table. Si un nom de colonne est spécifié (par exemple, `reverse word`), seule cette colonne est inversée, sans changer les autres colonnes.

### roll

` roll [value]` fait avancer (pour les valeurs positives) ou reculer (pour les valeurs négatives) toute la table. Si un nom de colonne est spécifié (par exemple, `roll 1 word`), seule cette colonne est décalée, sans changer les autres colonnes.

Par exemple, si `roll 1` est appliqué à la table suivante :

word  |
----- |
cat   |
dog   |
bunny |
horse |

Le résultat serait:

word  |
----- |
horse |
cat   |
dog   |
bunny |

### weight

` weight [column]` répète chaque ligne en fonction d'une valeur de pondération spécifiée dans une colonne.

Par exemple, si `weight w` est appliqué à la table suivante :

word  | w
----- | -
cat   | 0
dog   | 0
bunny | 2
horse | 1

Le résultat serait:

word  | w
----- | -
bunny | 2
bunny | 2
horse | 1

## Aperçu de la boucle

Si vous avez spécifié des contraintes ou utilisé des opérations avancées sur les boucles, il est conseillé de vérifier que le résultat est celui attendu. Pour ce faire, vous pouvez générer un aperçu de la table de boucle telle qu'elle sera (ou pourrait être, en cas de randomisation) lorsque vous exécuterez l'expérience.

Pour générer un aperçu, cliquez sur le bouton *Aperçu*.

## Accéder à la table de boucle dans un script Python en ligne

La table LOOP d'origine, telle que vous la voyez dans l'interface utilisateur d'OpenSesame, est un objet [`DataMatrix`](http://datamatrix.cogsci.nl/) appelé `dm`, et est une propriété de l'élément LOOP.

Cette table LOOP d'origine est généralement transformée de diverses manières ; par exemple, l'ordre des lignes peut être randomisé, et les lignes peuvent être répétées plusieurs fois. La LOOP transformée est également un objet `DataMatrix`, et s'appelle `live_dm`. `live_dm` est créé juste avant l'exécution de la boucle et est défini à `None` lorsque la boucle est terminée ; c'est-à-dire que `live_dm` est disponible uniquement pendant la phase *run* de la LOOP.

Enfin, l'indice de la ligne courante est stocké dans la variable expérimentale `live_row`. C'est-à-dire que `live_row` indique la ligne active de `live_dm`.

Alors, disons que nous avons une LOOP appelée *block_loop*. Nous pourrions alors accéder à la table LOOP dans un script Python en ligne comme suit :

~~~ .python
print("La table originale de la boucle :")
print(items['block_loop'].dm)

print("La table de boucle transformée :")
print(items['block_loop'].live_dm)

print("La ligne actuelle :")
print(items['block_loop'].live_dm[var.live_row])
~~~

Vous pouvez même définir la table LOOP de manière programmatique. Vous devez le faire dans la phase de préparation d'un INLINE_SCRIPT qui précède la LOOP.

```python
from datamatrix import DataMatrix

items['block_loop'].dm = DataMatrix(length=4)
items['block_loop'].dm.cue_side = 'gauche', 'droite', 'gauche', 'droite'
items['block_loop'].dm.cue_validity = 'valide', 'valide', 'invalide', 'invalide'
```

Les objets `DataMatrix` sont des structures puissantes pour travailler avec des données tabulaires. Pour plus d'informations, consultez :

- <https://pydatamatrix.eu/>