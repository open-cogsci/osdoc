title: Création d'un plugin
hash: d1fa28a6fa30fd06e613cb36e47efbafb5f2b52b7276950343c65e3556ff3f8c
locale: fr
language: French

[TOC]

## Qu'est-ce qu'un plugin OpenSesame ?

Les *Plugins* sont des éléments supplémentaires qui apparaissent dans la barre d'outils des éléments OpenSesame. Les plugins ajoutent des fonctionnalités que vous pouvez utiliser dans les expérimentations. (Pour ajouter des fonctionnalités à l'interface utilisateur d'OpenSesame, vous avez besoin d'une [*extension*](%url:extension%).)

## Fichiers pertinents

Un ou plusieurs plugins sont regroupés dans un package de plugins, qui est toujours un sous-paquet de `opensesame_plugins` (qui est lui-même un soi-disant paquet de noms implicite, mais c'est un détail technique qui n'est pas très important). Disons que votre package de plugins s'appelle `example`, et qu'il contient un seul plugin (il peut y en avoir plus) appelé `example_plugin`. Ceci correspondrait à la structure de fichiers et de dossiers suivante :

```
opensesame_plugins/
    example/
        __init__.py                  # peut être vide mais doit exister
        example_plugin/
            __init__.py              # contient les informations sur le plugin
            example_plugin.py        # contient la classe du plugin
            example_plugin.png       # icône 16 x 16 (facultatif)
            example_plugin_large.png # icône 32 x 32 (facultatif)
            example_plugin.md        # fichier d'aide au format Markdown (facultatif)
```

## Icônes

Chaque plugin a besoin d'une icône, que vous pouvez spécifier de deux façons :

- Inclure deux fichiers d'icônes dans le dossier du plugin comme indiqué ci-dessus :
    - Un fichier png de 16x16 px appelé `[plugin_name].png` et ;
    - Un fichier png de 32x32 px appelé `[plugin_name]_large.png`.
- Ou spécifier un nom d'`icône` dans les informations du plugin (`__init__.py`). Si vous faites cela, l'icône du plugin sera prise dans le thème des icônes.

## Fichier d'aide

Vous pouvez fournir un fichier d'aide au format Markdown ou HTML. Pour ajouter un fichier d'aide au format Markdown, créez simplement un fichier appelé `[plugin_name].md` dans le dossier du plugin. Pour un fichier d'aide en HTML, créez un fichier appelé `[plugin_name].html`. Le format Markdown est préféré, car il est plus facile à lire. Strictement parlant, le fichier d'aide est facultatif, et votre plugin fonctionnera sans lui. Cependant, un fichier d'aide informatif est une partie essentielle d'un bon plugin.

## Définir l'interface graphique

Les informations sur le plugin (`__init__.py`) définissent (au moins) une chaîne de caractères, une variable `category` et une variable `controls`.

La variable `controls` est une liste d'éléments `dict` qui définissent les contrôles de l'interface graphique. Les champs les plus importants sont :

- `type` spécifie le type de contrôle. Valeurs possibles :
	- `checkbox` est une case à cocher (`QtGui.QCheckBox`)
	- `color_edit` est un widget de sélection de couleur (`libqtopensesame.widgets.color_edit.ColorEdit`)
	- `combobox` est une boîte déroulante avec plusieurs options (`QtGui.QComboBox`)
	- `editor` est un éditeur de texte sur plusieurs lignes (utilisant PyQode)
	- `filepool` est un widget de sélection de fichier (`QtGui.QLineEdit`)
	- `line_edit` est une entrée de texte sur une seule ligne (`QtGui.QLineEdit`)
	- `spinbox` est un sélecteur de valeur numérique basé sur du texte (`QtGui.QSpinBox`)
	- `slider` est un sélecteur de valeur numérique glissant (`QtGui.QSlider`)
	- `text` est une chaîne de texte non interactive (`QtGui.QLabel`)
- `var` spécifie le nom de la variable qui doit être définie à l'aide du contrôle (non applicable si `type` est `text`).
- `label` spécifie l'étiquette de texte pour le contrôle.
- `name` (facultatif) spécifie sous quel nom le widget doit être ajouté à l'objet plugin, de sorte qu'il puisse être référencé en tant que `self.[name]`.
- `tooltip` (facultatif) un tooltip informatif.

```python
"""A docstring with a description of the plugin"""

# La catégorie détermine le groupe pour le plugin dans la barre d'outils de l'item
category = "Stimuli visuels"
# Définit les contrôles de l'interface graphique
controls = [
    {
        "type": "checkbox",
        "var": "checkbox",
        "label": "Exemple de case à cocher",
        "name": "widget_checkbox",
        "tooltip": "Un exemple de case à cocher"
    }, {
        "type": "color_edit",
        "var": "color",
        "label": "Couleur",
        "name": "widget_color",
        "tooltip": "Un exemple de modification de couleur"
    }
]
```

Voir le plugin [exemple](#examples) pour une liste de tous les contrôles et options.

## Écrire le code du plugin

Le code principal du plugin est placé dans `[nom_du_plugin].py`. Ce fichier contient généralement une seule classe nommée `[NomDuPlugin].py`, c'est-à-dire une classe avec l'équivalent CamelCase du nom du plugin, qui hérite de `libopensesame.item.Item`. Une classe de plugin de base ressemble à ceci :

```python
from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from openexp.canvas import Canvas

class ExemplePlugin(Item):
    """Un exemple de plugin qui affiche un simple canevas. Le nom de la classe
    doit être la version CamelCase du nom_du_dossier et du nom_du_fichier. Ainsi, dans
    ce cas, le dossier du plugin (qui est un package Python) et le 
    fichier .py (qui est un module Python) sont tous deux appelés exemple_plugin, tandis que
    la classe est appelée ExemplePlugin.
    """
    def reset(self):
        """Réinitialise le plug-in aux valeurs initiales."""
        # Ici, nous fournissons des valeurs par défaut pour les variables qui sont spécifiées
        # dans __init__.py. Si vous ne fournissez pas de valeurs par défaut, le plug-in
        # fonctionnera, mais les variables seront indéfinies lorsqu'elles ne sont pas
        # explicitement définies dans l'interface graphique.
        self.var.checkbox = 'yes'  # yes = coché, no = décoché
        self.var.color = 'white'
        self.var.option = 'Option 1'
        self.var.file = ''
        self.var.text = 'Texte par défaut'
        self.var.spinbox_value = 1
        self.var.slider_value = 1
        self.var.script = 'print(10)'

    def prepare(self):
        """La phase de préparation du plug-in se fait ici."""
        # Appelez le constructeur parent.
        super().prepare()
        # Ici, préparez simplement un canevas avec un point de fixation.
        self.c = Canvas(self.experiment)
        self.c.fixdot()

    def run(self):
        """La phase d'exécution du plug-in se fait ici."""
        # self.set_item_onset() définit la variable time_[nom de l'élément]. En option,
        # vous pouvez passer un horodatage, tel que renvoyé par canvas.show().
        self.set_item_onset(self.c.show())
```

Si vous souhaitez implémenter des contrôles d'interface graphique personnalisés pour votre plugin, vous devez également implémenter une classe `Qt[NomDuPlugin]` dans le même fichier. Ceci est illustré dans le plugin [exemple](#exemples). Si vous n'implémentez pas cette classe, une interface graphique par défaut sera créée sur la base des contrôles tels que définis dans `__init__.py`.

## Variables expérimentales

Les variables expérimentales sont des propriétés de l'objet `var`. Un exemple est `self.var.my_line_edit_var` de l'exemple ci-dessus. Ces variables qui définissent le plugin, et sont analysées vers et depuis le script OpenSesame. Voir aussi :

- %link:manuel/variables%

## Construire un paquet et le télécharger sur pypi

La manière la plus simple de construire un paquet pour votre plugin est de définir un fichier `pyproject.toml` et d'utiliser `poetry` pour construire le paquet et le télécharger sur `pypi`.

- <https://python-poetry.org/>

Un exemple de fichier `pyproject.toml` est le suivant :

```toml
[tool.poetry]
name = "opensesame-plugin-example"
version = "0.0.1"
description = "Un exemple de plugin pour OpenSesame"
authors = ["Sebastiaan Mathôt <s.mathot@cogsci.nl>"]
readme = "readme.md"
packages = [
    {include = "opensesame_plugins"},
]

[tool.poetry.dependencies]
python = ">= 3.7"
opensesame-core = ">= 4.0.0a0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Une fois que vous avez ajouté ce fichier au dossier racine de votre code de plugin, vous pouvez construire un paquet `.whl` en exécutant :

```bash
poetry build
```

Une fois que vous avez construit avec succès un paquet, créez un compte sur <https://pypi.org/>, créez un jeton API pour votre compte, et authentifiez `poetry` comme ceci :

```bash
poetry config pypi-token.pypi [api_token]
```

Une fois cela fait, vous pouvez publier votre paquet sur PyPi en exécutant la commande suivante :

```bash
poetry publish
```

Vos utilisateurs pourront maintenant installer votre plugin avec pip !

```bash
pip install opensesame-plugin-example
```

## Exemples

Pour un exemple fonctionnel, voir :

- <https://github.com/open-cogsci/opensesame-plugin-example>

D'autres exemples peuvent être trouvés dans le dossier `opensesame_plugins` du code source d'OpenSesame :

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_plugins/core>