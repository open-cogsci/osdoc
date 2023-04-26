title: Eine Erweiterung erstellen
hash: 91a79a763c57d0445f9ee814ec6e513ab04f651b716fdd1fe99937052b85df97
locale: de
language: German

[TOC]

## Was ist eine OpenSesame-Erweiterung?

*Erweiterungen* fügen der OpenSesame-Benutzeroberfläche beliebige Funktionen hinzu. Zum Beispiel kann eine Erweiterung einen neuen Eintrag in der Hauptwerkzeugleiste oder der Menüleiste hinzufügen. (Um Funktionen hinzuzufügen, die Sie in Experimenten verwenden können, benötigen Sie ein [Plugin](%url:plugin%).)

## Relevante Dateien

Eine oder mehrere Erweiterungen werden in einem Erweiterungspaket zusammengefasst, das immer ein Unterpaket von `opensesame_extensions` ist (das selbst ein sogenanntes implizites Namespace-Paket ist, aber das ist ein technisches Detail, das nicht sehr wichtig ist). Nehmen wir an, Ihr Erweiterungspaket heißt `example`, und es enthält eine einzelne Erweiterung (es können mehr sein) namens `example_extension`. Dies würde der folgenden Datei- und Verzeichnisstruktur entsprechen:

```
opensesame_extensions/
    example/
        __init__.py               # kann leer sein, muss aber vorhanden sein
        example_extension/
            __init__.py           # enthält Erweiterungsinformationen
            example_extension.py  # enthält Erweiterungsklasse
```

## Erweiterungsinformationen

Erweiterungsinformationen sind in der `__init__.py` des Erweiterungsmoduls definiert, also in unserem Beispiel ist das `opensesesame_extensions/example/example_extension/__init__.py`.

```python
"""Ein Docstring mit einer Beschreibung der Erweiterung"""

# Ein Standard-Icon-Name
# - <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>
icon = 'applications-accessories'
# Das Label und der Tooltip werden verwendet, um die Standardaktion zu erstellen, die
# im Menü und/oder der Werkzeugleiste (oder keiner von beiden) eingefügt wird
label = "Beispiel-Erweiterung"
tooltip = "Beispiel-Tooltip"
menu = {
    "index": -1,
    "separator_before": True,
    "separator_after": True,
    "submenu": "Beispiel"
}
toolbar = {
    "index": -1,
    "separator_before": True,
    "separator_after": True
}
# Einstellungen werden dauerhaft im cfg-Objekt gespeichert
settings = {
    "example_setting": "example value"
}
```

Eine Erweiterung kann im Menü oder in der Hauptwerkzeugleiste von OpenSesame erscheinen. Dazu müssen Sie mehrere Felder in `__init__.py` definieren, wie oben gezeigt:

- Das `label` ist der Text, der im Menü erscheinen wird.
- Das `icon` ist ein [freedesktop-konformer Icon-Name][icon-spec], der das Icon angibt, das im Menü und/oder in der Werkzeugleiste erscheinen wird.
- Der `index` gibt die Position der Erweiterung im Menü/der Werkzeugleiste an und funktioniert wie ein `list`-Index. Das heißt, negative Werte beziehen sich auf den letzten Eintrag, wobei -1 Ihre Erweiterung am Ende platziert.

Um Ihre Erweiterung auf Menü-/Werkzeugleistenaktivierung zu reagieren, implementieren Sie die `activate()`-Methode, wie unten in dem Erweiterungscode gezeigt.


## Schreiben des Erweiterungscodes

Der Haupterweiterungscode befindet sich in `[extension_name].py`. Diese Datei enthält in der Regel nur eine einzige Klasse mit dem Namen `[ExtensionName].py`, also eine Klasse mit dem CamelCase-Äquivalent des Plugin-Namens, die von `libqtopensesame.extensions.BaseExtension` erbt. Eine grundlegende (nicht funktionale) Erweiterungsklasse sieht also so aus:

~~~ .python
from libopensesame.py3compat import *
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class ExampleExtension(BaseExtension):
    """Eine Beispiel-Erweiterung, die mehrere häufige Ereignisse auflistet. Der Klassenname
    sollte die CamelCase-Version des folder_name und file_name sein. Also in
    diesem Fall sind sowohl der Erweiterungsordner (der ein Python-Paket ist) als auch die
    .py-Datei (die ein Python-Modul ist) mit example_extension benannt, während
    die Klasse ExampleExtension genannt ist.
    """

    def activate(self):
        oslogger.debug('example_extension Erweiterung aktiviert')

    def event_save_experiment(self, path):
        oslogger.debug(f'Ereignis ausgelöst: save_experiment(path={path})')

    # Weitere Ereignislistener finden Sie im Beispiel-Code von example_extension
~~~

## Lauschen auf Ereignisse

OpenSesame löst Ereignisse aus, wenn etwas Wichtiges passiert. Zum Beispiel wird das Ereignis `save_experiment` ausgelöst, wenn ein Experiment gespeichert wird. Um Ihre Erweiterung auf ein Ereignis hören zu lassen, implementieren Sie einfach eine Methode mit dem Namen `event_[event name]`, wie oben gezeigt.

Beachten Sie, dass einige Ereignisse Schlüsselwortargumente verwenden, wie `path` im Falle von `save_experiment`. Die Schlüsselwortsygnatur Ihrer Funktion muss der erwarteten Schlüsselwortsygnatur entsprechen. Siehe die Ereignisübersicht unten für eine vollständige Liste der Ereignisse und erwarteten Schlüsselwörter.

## Ein Paket erstellen und auf pypi hochladen

Ein Extension-Paket erstellen und auf `pypi` hochladen funktioniert genauso wie für Plugins:

- %link:plugin%
- <https://github.com/open-cogsci/opensesame-extension-example>

## Beispiele

Für ein funktionierendes Beispiel siehe:

- <https://github.com/open-cogsci/opensesame-extension-example>

Weitere Beispiele finden Sie im Ordner `opensesame_extensions` des OpenSesame-Quellcodes:

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_extensions/core>

[example]: https://github.com/open-cogsci/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html

## Ereignisübersicht

In dieser Übersicht sind alle Ereignisse aufgeführt, die irgendwo im Code ausgelöst werden und auf die Ihre Erweiterung daher hören kann, indem sie die entsprechenden `event_[eventname]()` Funktionen implementiert.

%-- include: include/events.md --%