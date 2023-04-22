title: Créer une extension
hash: 91a79a763c57d0445f9ee814ec6e513ab04f651b716fdd1fe99937052b85df97
locale: fr
language: French

[TOC]

## Qu'est-ce qu'une extension OpenSesame ?

Les *Extensions* ajoutent des fonctionnalités arbitraires à l'interface utilisateur d'OpenSesame. Par exemple, une extension peut ajouter une nouvelle entrée dans la barre d'outils principale ou dans la barre des menus. (Pour ajouter des fonctionnalités que vous pouvez utiliser dans des expériences, vous avez besoin d'un [plugin](%url:plugin%).)

## Fichiers pertinents

Une ou plusieurs extensions sont regroupées dans un paquet d'extension, qui est toujours un sous-paquet de `opensesame_extensions` (qui est en lui-même un paquet de noms de domaine implicite, mais c'est un détail technique qui n'est pas très important). Disons que votre paquet d'extension s'appelle `example`, et qu'il contient une seule extension (il peut y en avoir plus) appelée `example_extension`. Ceci correspondrait à la structure de fichiers et de dossiers suivante:

```
opensesame_extensions/
    example/
        __init__.py               # peut être vide mais doit exister
        example_extension/
            __init__.py           # contient des informations sur l'extension
            example_extension.py  # contient la classe d'extension
```

## Informations sur l'extension

Les informations sur l'extension sont définies dans le fichier `__init__.py` du module d'extension, donc dans notre exemple, il s'agit de `opensesesame_extensions/example/example_extension/__init__.py`.

```python
"""Une chaîne de caractères décrivant l'extension"""

# Un nom d'icône standard
# - <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>
icon = 'applications-accessories'
# Le label et l'info-bulle sont utilisés pour créer l'action par défaut, qui est
# insérée dans le menu et/ ou la barre d'outils (ou aucun des deux)
label = "Exemple d'extension"
tooltip = "Exemple d'info-bulle"
menu = {
    "index": -1,
    "separator_before": True,
    "separator_after": True,
    "submenu": "Exemple"
}
toolbar = {
    "index": -1,
    "separator_before": True,
    "separator_after": True
}
# Les paramètres sont stockés de manière persistante dans l'objet cfg
settings = {
    "exemple_setting": "valeur exemple"
}
```

Une extension peut apparaître dans le menu ou la barre d'outils principale d'OpenSesame. Cela nécessite de définir plusieurs champs dans `__init__.py` comme indiqué ci-dessus :

- Le `label` est le texte qui apparaîtra dans le menu.
- L'`icon` est un [nom d'icône conforme à freedesktop][icon-spec] qui spécifie l'icône qui apparaîtra dans le menu et/ ou la barre d'outils.
- L'`index` donne la position de l'extension dans le menu/ barre d'outils, et fonctionne comme un index `list`. C'est-à-dire que les valeurs négatives sont relatives à la dernière entrée, où -1 place votre extension à la fin.

Pour que votre extension réponde à l'activation du menu/ barre d'outils, implémentez la méthode `activate()` comme indiqué ci-dessous dans le code de l'extension ci-dessous.

## Écrire le code de l'extension

Le code principal de l'extension est placé dans `[extension_name].py`. Ce fichier contient généralement une seule classe nommée `[ExtensionName].py`, c'est-à-dire une classe avec l'équivalent CamelCase du nom du plugin, qui hérite de `libqtopensesame.extensions.BaseExtension`. Ainsi, une classe d'extension de base (non fonctionnelle) ressemble à ceci:

~~~ .python
from libopensesame.py3compat import *
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension

class ExampleExtension(BaseExtension):
    """Un exemple d'extension qui liste plusieurs événements communs. Le nom de la classe
    doit être la version CamelCase du folder_name et du file_name. Donc, dans
    ce cas, le dossier d'extension (qui est un paquet Python) et le
    fichier .py (qui est un module Python) sont appelés example_extension, alors que
    la classe est appelée ExampleExtension.
    """

    def activate(self):
        oslogger.debug("l'extension example_extension a été activée")

    def event_save_experiment(self, path):
        oslogger.debug(f"Événement déclenché: save_experiment(path={path})")

    # Voir le code source de example_extension pour plus d'écouteurs d'événements
~~~

## Écoute des événements

OpenSesame déclenche des événements chaque fois que quelque chose d'important se produit. Par exemple, l'événement `save_experiment` est déclenché lorsqu'une expérience est enregistrée. Pour que votre extension écoute un événement, il suffit d'implémenter une méthode avec le nom `event_[nom de l'événement]` comme indiqué ci-dessus.

Notez que certains événements prennent des arguments de mots-clés, comme `path` dans le cas de `save_experiment`. La signature de mots-clés de votre fonction doit correspondre à la signature de mots-clés attendue. Voir la vue d'ensemble des événements ci-dessous pour une liste complète des événements et des mots-clés attendus.

## Créer un package et le télécharger sur pypi

Créer un package d'extension et le télécharger sur `pypi` fonctionne de la même manière que pour les plugins :

- %link:plugin%
- <https://github.com/open-cogsci/opensesame-extension-example>

## Exemples

Pour un exemple fonctionnel, voir :

- <https://github.com/open-cogsci/opensesame-extension-example>

D'autres exemples peuvent être trouvés dans le dossier `opensesame_extensions` du code source d'OpenSesame :

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_extensions/core>

[example]: https://github.com/open-cogsci/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html

## Aperçu des événements

Cet aperçu répertorie tous les événements qui sont déclenchés quelque part dans le code et que votre extension peut donc écouter en implémentant les fonctions `event_[nomdelévénement]()` correspondantes.

%-- include: include/events.md --%