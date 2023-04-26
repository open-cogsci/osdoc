title: Ein Plugin erstellen
hash: d1fa28a6fa30fd06e613cb36e47efbafb5f2b52b7276950343c65e3556ff3f8c
locale: de
language: German

[TOC]

## Was ist ein OpenSesame Plugin?

*Plugins* sind zusätzliche Elemente, die in der OpenSesame-Elementleiste erscheinen. Plugins fügen Funktionen hinzu, die Sie bei der Erstellung von Experimenten nutzen können. (Um zusätzliche Funktionen zur OpenSesame-Benutzeroberfläche hinzuzufügen, benötigen Sie eine [*Erweiterung*](%url:extension%).)

## Relevante Dateien

Ein oder mehrere Plugins werden in einem Plugin-Paket zusammengefasst, das immer ein Unter-Paket von `opensesame_plugins` ist (welches selbst ein sogenanntes implizites Namensraum-Paket ist, aber das ist ein technisches Detail, das nicht sehr wichtig ist). Nehmen wir an, Ihr Plugin-Paket heißt `example`, und es enthält ein einzelnes Plugin (es können auch mehrere sein) namens `example_plugin`. Dies würde der folgenden Datei- und Ordnerstruktur entsprechen:

```
opensesame_plugins/
    example/
        __init__.py                  # kann leer sein, muss aber existieren
        example_plugin/
            __init__.py              # enthält Plugin-Informationen
            example_plugin.py        # enthält Plugin-Klasse
            example_plugin.png       # 16 x 16 Symbol (optional)
            example_plugin_large.png # 32 x 32 Symbol (optional)
            example_plugin.md        # Hilfe-Datei im Markdown-Format (optional)
```

## Symbole

Jedes Plugin benötigt ein Symbol, das auf eine von zwei Arten angegeben werden kann:

- Zwei Symbol-Dateien im Plugin-Ordner enthalten, wie oben gezeigt:
    - Eine 16x16px große png-Datei namens `[plugin_name].png`; und
    - Eine 32x32px große png-Datei namens `[plugin_name]_large.png`.
- Oder einen Symbolnamen in den Plugin-Informationen (`__init__.py`) angeben. Wenn Sie dies tun, wird das Plugin-Symbol aus dem Symbolthema entnommen.

## Hilfedatei

Sie können eine Hilfedatei im Markdown- oder HTML-Format bereitstellen. Um eine Markdown-Hilfedatei hinzuzufügen, erstellen Sie einfach eine Datei namens `[plugin_name].md` im Plugin-Ordner. Für eine HTML-Hilfedatei erstellen Sie eine Datei namens `[plugin_name].html`. Markdown-Format wird bevorzugt, da es leichter zu lesen ist. Streng genommen ist die Hilfedatei optional, und Ihr Plugin funktioniert auch ohne sie. Eine informative Hilfedatei ist jedoch ein wesentlicher Bestandteil eines guten Plugins.

## Definieren der Benutzeroberfläche

Die Plugin-Informationen (`__init__.py`) definieren mindestens einen Docstring, eine `category` Variable und eine `controls` Variable.

Die `controls` Variable ist eine Liste von `dict` Elementen, die die GUI-Steuerungen definieren. Die wichtigsten Felder sind:

- `type` gibt den Typ der Steuerung an. Mögliche Werte:
	- `checkbox` ist ein ankreuzbares Kästchen (`QtGui.QCheckBox`)
	- `color_edit` ist ein Farbauswahl-Widget (`libqtopensesame.widgets.color_edit.ColorEdit`)
	- `combobox` ist ein Dropdown-Feld mit mehreren Optionen (`QtGui.QComboBox`)
	- `editor` ist ein mehrzeiliger Texteditor (verwendet PyQode)
	- `filepool` ist ein Dateiauswahl-Widget (`QtGui.QLineEdit`)
	- `line_edit` ist eine Eingabe für eine einzelne Textzeile (`QtGui.QLineEdit`)
	- `spinbox` ist eine textbasierte numerische Wertauswahl (`QtGui.QSpinBox`)
	- `slider` ist eine Schieberegler für numerische Werte (`QtGui.QSlider`)
	- `text` ist eine nicht interaktive Textanzeige (`QtGui.QLabel`)
- `var` gibt den Namen der Variablen an, die mit der Steuerung gesetzt werden soll (nicht zutreffend, wenn `type` `text` ist).
- `label` gibt die Textbeschriftung für die Steuerung an.
- `name` (optional) gibt den Namen an, unter dem das Widget dem Plugin-Objekt hinzugefügt werden soll, damit darauf als `self.[name]` verwiesen werden kann.
- `tooltip` (optional) ein informativer Tooltip.

```python
"""Ein Docstring mit einer Beschreibung des Plugins"""

# Die Kategorie bestimmt die Gruppe für das Plugin in der Elementleiste
category = "Visuelle Reize"
# Definiert die GUI-Steuerungen
controls = [
    {
        "type": "checkbox",
        "var": "checkbox",
        "label": "Beispiel Checkbox",
        "name": "checkbox_widget",
        "tooltip": "Ein Beispiel für eine Checkbox"
    }, {
        "type": "color_edit",
        "var": "color",
        "label": "Farbe",
        "name": "color_widget",
        "tooltip": "Ein Beispiel für eine Farbbearbeitung"
    }
]
```

Siehe das [Beispiel](#examples) Plugin für eine Liste aller Steuerungen und Optionen.

## Plugin-Code schreiben

Der Hauptcode des Plugins befindet sich in `[plugin_name].py`. Diese Datei enthält in der Regel nur eine einzige Klasse mit dem Namen `[PluginName].py`, also eine Klasse, deren CamelCase-Äquivalent des Plugin-Namens und die von `libopensesame.item.Item` erbt. Eine grundlegende Plugin-Klasse sieht folgendermaßen aus:

```python
from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from openexp.canvas import Canvas

class BeispielPlugin(Item):
    """Ein Beispiel-Plugin, das einen einfachen Canvas zeigt. Der Klassenname
    sollte die CamelCase-Version des folder_name und file_name sein. In
    diesem Fall sind sowohl der Plugin-Ordner (der ein Python-Paket ist) als auch
    die .py-Datei (die ein Python-Modul ist) example_plugin genannt, während 
    die Klasse ExamplePlugin heißt.
    """
    def reset(self):
        """Setzt das Plugin auf die Anfangswerte zurück."""
        # Hier stellen wir Standardwerte für die Variablen bereit, die in
        # __init__.py angegeben sind. Wenn Sie keine Standardwerte angeben,
        # wird das Plugin funktionieren, aber die Variablen werden undefiniert
        # sein, wenn sie nicht explizit in der GUI gesetzt sind.
        self.var.checkbox = 'yes'  # yes = aktiviert, no = deaktiviert
        self.var.color = 'weiß'
        self.var.option = 'Option 1'
        self.var.file = ''
        self.var.text = 'Standardtext'
        self.var.spinbox_value = 1
        self.var.slider_value = 1
        self.var.script = 'print(10)'

    def prepare(self):
        """Die Vorbereitungsphase des Plugins geht hier."""
        # Rufen Sie den übergeordneten Konstruktor auf.
        super().prepare()
        # Bereiten Sie hier einfach einen Canvas mit einem Fixationspunkt vor.
        self.c = Canvas(self.experiment)
        self.c.fixdot()

    def run(self):
        """Die Laufphase des Plugins geht hier."""
        # self.set_item_onset() setzt die Zeit_[item_name]-Variable. Optional können Sie
        # einem Zeitstempel übergeben, wie der von canvas.show() zurückgegebene.
        self.set_item_onset(self.c.show())
```

Wenn Sie benutzerdefinierte GUI-Steuerelemente für Ihr Plugin implementieren möchten, müssen Sie auch eine `Qt[PluginName]`-Klasse in der gleichen Datei implementieren. Dies wird im [Beispiel](#examples) Plugin illustriert. Wenn Sie diese Klasse nicht implementieren, wird eine Standard-GUI auf Basis der in `__init__.py` definierten Steuerelemente erstellt.

## Experimentelle Variablen

Experimentelle Variablen sind Eigenschaften des `var`-Objekts. Ein Beispiel ist `self.var.my_line_edit_var` aus dem obigen Beispiel. Diese Variablen, die das Plugin definieren, werden in das OpenSesame-Skript übertragen und daraus extrahiert. Siehe auch:

- %link:manual/variables%

## Erstellen eines Pakets und Hochladen auf pypi

Der einfachste Weg, ein Paket für Ihr Plugin zu bauen, besteht darin, eine `pyproject.toml`-Datei zu definieren und `poetry` zu verwenden, um das Paket zu bauen und auf `pypi` hochzuladen.

- <https://python-poetry.org/>

Ein Beispiel für eine `pyproject.toml`-Datei sieht folgendermaßen aus:

```toml
[tool.poetry]
name = "opensesame-plugin-example"
version = "0.0.1"
description = "Ein Beispiel-Plugin für OpenSesame"
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

Wenn Sie diese Datei zum Stammverzeichnis Ihres Plugin-Codes hinzufügen, können Sie ein `.whl`-Paket erstellen, indem Sie Folgendes ausführen:

```bash
poetry build
```

Wenn Sie ein Paket erfolgreich erstellt haben, erstellen Sie ein Konto auf <https://pypi.org/>, erstellen Sie einen API-Token für Ihr Konto und authentifizieren Sie `poetry` wie folgt:

```bash
poetry config pypi-token.pypi [api_token]
```

Wenn dies erledigt ist, können Sie Ihr Paket auf PyPi veröffentlichen, indem Sie den folgenden Befehl ausführen:

```bash
poetry publish
```

Ihre Benutzer können jetzt Ihr Plugin mit pip installieren!

```bash
pip install opensesame-plugin-example
```

## Beispiele

Für ein funktionierendes Beispiel, sehen Sie:

- <https://github.com/open-cogsci/opensesame-plugin-example>

Andere Beispiele finden sich im `opensesame_plugins` Ordner des OpenSesame-Quellcodes:

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_plugins/core>