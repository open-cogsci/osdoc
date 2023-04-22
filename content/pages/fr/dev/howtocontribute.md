title: Comment contribuer
uptodate: false
hash: cdf0ef5efe4027ec45865c8235a04695c3ed9e91a1c8db4ffab4c5351d8c05d5
locale: fr
language: French

[TOC]

## Obtenir le dernier code source

Le code source d'OpenSesame est hébergé sur GitHub :

- <https://github.com/smathot/OpenSesame>.

GitHub offre un moyen simple de collaborer sur un projet. Si vous n'êtes pas familier avec GitHub, vous pouvez consulter leur site d'aide : <http://help.github.com/>.

La meilleure (et la plus simple) façon de contribuer au code est la suivante :

1. Créez un compte GitHub.
2. Créez un fork d'OpenSesame <https://github.com/smathot/OpenSesame>.
3. Modifiez votre fork.
4. Envoyez une "demande de tirage" (pull request), demandant que vos modifications soient fusionnées dans le dépôt principal.

Chaque version majeure d'OpenSesame a sa propre branche. Par exemple, la branche `ising` contient le code pour la version 3.0 *Interactive Ising*. La branche `master` contient le code pour la dernière version stable.

## Développer un plugin ou une extension

Pour le développement de plugin ou d'extension, voir :

- %link:dev/plugin%
- %link:dev/extension%

## Traduire l'interface utilisateur

Pour des instructions sur comment traduire l'interface utilisateur, voir :

- %link:dev/translate%

## Directives de style de codage

L'objectif est de maintenir une base de code lisible et cohérente. Par conséquent, veuillez prendre en compte les directives de style suivantes lors de la contribution au code :

### Gestion des exceptions

Les exceptions doivent être gérées via la classe `libopensesame.exceptions.osexception`. Par exemple :

~~~ .python
from libopensesame.exceptions import osexception
raise osexception(u'Une erreur est survenue')
~~~

### Affichage des informations de débogage

Les informations de débogage doivent être gérées via `libopensesame.debug.msg()` et sont affichées uniquement lorsque OpenSesame est lancé avec l'argument de ligne de commande `--debug`. Par exemple :

~~~ .python
from libopensesame import debug
debug.msg(u'Ceci sera affiché uniquement en mode débogage')
~~~

### Indentation

L'indentation doit être basée sur des tabulations. *C'est la directive de style la plus importante de toutes*, car une indentation mixte cause des problèmes et prend du temps à corriger.

### Noms, chaînes de documentation et enroulement de ligne

- Les noms doivent être en minuscules, avec des mots séparés par des traits de soulignement.
- Chaque fonction doit être accompagnée d'une chaîne de documentation informative, selon le format indiqué ci-dessous. Si une chaîne de documentation est redondante, par exemple parce qu'une fonction remplace une autre fonction qui possède une chaîne de documentation, veuillez indiquer où se trouve la chaîne de documentation complète.
- Veuillez ne pas avoir de lignes de code qui s'étendent au-delà de 79 caractères (où une tabulation compte pour 4 caractères), à l'exception des longues chaînes de caractères qui sont difficiles à fragmenter.

~~~ .python
def a_function(argument, mot_cle=None):

    """
    desc:
        Il s'agit d'une chaîne de documentation au format YAMLDoc, qui permet une
        spécification complète des arguments. Voir aussi <https://github.com/smathot/python-yamldoc>.
    
    arguments:
        argument:   Ceci est un argument.
    
    mots cles:
        mot_cle:   Ceci est un mot clé.
    
    renvoie:
        Cette fonction renvoie certaines valeurs.
    """
    
    pass
    
def a_simple_function():

    """Ceci est une chaîne de documentation simple"""

    pass

~~~

### Écriture de code compatible avec Python 2 et 3

Le code doit être compatible avec Python 2.7 et 3.4 et versions ultérieures. Pour faciliter l'écriture de code compatible Python 2 et 3, quelques astuces sont incluses dans le module `py3compat`, qui doit *toujours* être importé dans votre script de cette manière :

~~~ .python
from libopensesame.py3compat import *
~~~

Ce module :

- Revoie les types Python-2 `str` et `unicode` vers les types Python-3 `bytes` et `str` (approximativement équivalents). Par conséquent, vous devez utiliser des objets `str` dans la plupart des cas et des objets `bytes` dans des cas particuliers.
- Ajoute les fonctions suivantes :
  - `safe_decode(s, enc='utf-8', errors='strict')` transforme n'importe quel objet en un objet `str`
  - `safe_encode(s, enc='utf-8', errors='strict')` transforme n'importe quel objet en un objet `bytes`
- Ajoute une variable `py3`, qui est `True` lorsqu'elle est exécutée sur Python 3 et `False` lorsqu'elle est exécutée sur Python 2.
- Ajoute un objet `basestr` lorsqu'il est exécuté sur Python 3.

### Unicode et chaînes de caractères

Assurez-vous que toutes les fonctionnalités sont compatibles Unicode. Pour les nouveaux codes, utilisez *uniquement* les chaînes Unicode en interne.

~~~ .python
my_value = 'a string' # non préféré
my_value = u'a string' # préféré
~~~

Pour plus d'informations, voir :

- <http://docs.python.org/2/howto/unicode.html>

### Autre

À l'exception des directives présentées ci-dessus, veuillez respecter la norme suivante :

- <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>