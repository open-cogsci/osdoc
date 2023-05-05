title: Creando un complemento
hash: d1fa28a6fa30fd06e613cb36e47efbafb5f2b52b7276950343c65e3556ff3f8c
locale: es
language: Spanish

[TOC]

## ¿Qué es un complemento de OpenSesame?

Los *complementos* son elementos adicionales que aparecen en la barra de herramientas de elementos de OpenSesame. Los complementos agregan funcionalidad que puedes utilizar en experimentos. (Para agregar funcionalidad a la interfaz de usuario de OpenSesame, necesitas una [*extensión*](%url:extension%).)

## Archivos relevantes

Uno o más complementos se agrupan en un paquete de complementos, que siempre es un subpaquete de `opensesame_plugins` (que a su vez es un llamado paquete de espacio de nombres implícito, pero ese es un detalle técnico que no es muy importante). Digamos que tu paquete de complementos se llama `example` y que contiene un único complemento (puede haber más) llamado `example_plugin`. Esto correspondería a la siguiente estructura de archivos y carpetas:

```
opensesame_plugins/
    ejemplo/
        __init__.py                  # puede estar vacío pero debe existir
        example_plugin/
            __init__.py              # contiene información del complemento
            example_plugin.py        # contiene la clase del complemento
            example_plugin.png       # icono de 16 x 16 (opcional)
            example_plugin_large.png # icono de 32 x 32 (opcional)
            example_plugin.md        # Archivo de ayuda en formato Markdown (opcional)
```

## Iconos

Cada complemento necesita un icono, que puedes especificar de dos formas:

- Incluir dos archivos de icono en la carpeta del complemento como se muestra arriba:
    - Un archivo png de 16x16 px llamado `[plugin_name].png`; y
    - Un archivo png de 32x32 px llamado `[plugin_name]_large.png`.
- O especificar un nombre de `icono` en la información del complemento (`__init__.py`). Si haces esto, el icono del complemento se tomará del tema de iconos.

## Archivo de ayuda

Puedes proporcionar un archivo de ayuda en formato Markdown o HTML. Para agregar un archivo de ayuda de Markdown, simplemente crea un archivo llamado `[plugin_name].md` en la carpeta del complemento. Para un archivo de ayuda HTML, crea un archivo llamado `[plugin_name].html`. Se prefiere el formato Markdown, porque es más fácil de leer. Hablando estrictamente, el archivo de ayuda es opcional y tu complemento funcionará sin él. Sin embargo, un archivo de ayuda informativo es una parte esencial de un buen complemento.

## Definiendo la GUI

La información del complemento (`__init__.py`) define (al menos) una cadena de documentación, una variable `category` y una variable `controls`.

La variable `controls` es una lista de elementos `dict` que definen los controles de la GUI. Los campos más importantes son:

- `type` especifica el tipo de control. Valores posibles:
	- `checkbox` es una casilla verificable (`QtGui.QCheckBox`)
	- `color_edit` es un widget de selección de color (`libqtopensesame.widgets.color_edit.ColorEdit`)
	- `combobox` es una caja desplegable con múltiples opciones (`QtGui.QComboBox`)
	- `editor` es un editor de texto multilinea (usando PyQode)
	- `filepool` es un widget de selección de archivos (`QtGui.QLineEdit`)
	- `line_edit` es una entrada de texto de una sola línea (`QtGui.QLineEdit`)
	- `spinbox` es un selector de valor numérico basado en texto (`QtGui.QSpinBox`)
	- `slider` es un selector de valor numérico deslizante (`QtGui.QSlider`)
	- `text` es una cadena de texto no interactiva (`QtGui.QLabel`)
- `var` especifica el nombre de la variable que se debe establecer usando el control (no aplicable si `type` es `text`).
- `label` especifica la etiqueta de texto para el control.
- `name` (opcional) especifica bajo qué nombre debe agregarse el widget al objeto del complemento, de modo que se pueda hacer referencia como `self.[name]`.
- `tooltip` (opcional) una información sobre herramientas informativa.

```python
"""Una cadena de documentación con una descripción del complemento"""

# La categoría determina el grupo para el complemento en la barra de herramientas de elementos
category = "Estímulos visuales"
# Define los controles de la GUI
controls = [
    {
        "type": "checkbox",
        "var": "checkbox",
        "label": "Ejemplo de casilla",
        "name": "checkbox_widget",
        "tooltip": "Un ejemplo de casilla"
    }, {
        "type": "color_edit",
        "var": "color",
        "label": "Color",
        "name": "color_widget",
        "tooltip": "Un ejemplo de editor de color"
    }
]
```

Consulta el [ejemplo](#examples) de complemento para obtener una lista de todos los controles y opciones.

## Escribiendo el código del complemento

El código principal del complemento se coloca en `[plugin_name].py`. Este archivo generalmente contiene solo una clase llamada `[PluginName].py`, es decir, una clase con el equivalente CamelCase del nombre del complemento, que hereda de `libopensesame.item.Item`. Una clase básica de complemento se ve así:


```python
from libopensesame.py3compat import *
from libopensesame.item import Item
from libqtopensesame.items.qtautoplugin import QtAutoPlugin
from openexp.canvas import Canvas


class ExamplePlugin(Item):
    """Un ejemplo de complemento que muestra un canvas simple. El nombre de la clase
    debe ser la versión CamelCase de folder_name y file_name. Entonces en
    este caso, tanto la carpeta del complemento (que es un paquete de Python) como
    el archivo .py (que es un módulo de Python) se llaman example_plugin, mientras
    que la clase se llama ExamplePlugin.
    """
    def reset(self):
        """Reinicia el complemento a los valores iniciales."""
        # Aquí proporcionamos valores predeterminados para las variables que se especifican
        # en __init__.py. Si no proporciona valores predeterminados, el complemento
        # funcionará, pero las variables estarán indefinidas cuando no estén
        # explícitamente establecidas en la GUI.
        self.var.checkbox = 'yes'  # yes = marcado, no = sin marcar
        self.var.color = 'white'
        self.var.option = 'Opción 1'
        self.var.file = ''
        self.var.text = 'Texto predeterminado'
        self.var.spinbox_value = 1
        self.var.slider_value = 1
        self.var.script = 'print(10)'

    def prepare(self):
        """La fase de preparación del complemento va aquí."""
        # Llame al constructor principal.
        super().prepare()
        # Aquí simplemente prepara un canvas con un punto de fijación.
        self.c = Canvas(self.experiment)
        self.c.fixdot()

    def run(self):
        """La fase de ejecución del complemento va aquí."""
        # self.set_item_onset() establece la variable time_[item name]. Opcionalmente,
        # puede pasar una marca de tiempo, como la devuelta por canvas.show().
        self.set_item_onset(self.c.show())
```


Si desea implementar controles de interfaz gráfica de usuario personalizados para su complemento, también debe implementar una clase `Qt[PluginName]` en el mismo archivo. Esto se ilustra en el complemento [ejemplo](#examples). Si no implementa esta clase, se creará una interfaz gráfica de usuario predeterminada según los controles definidos en `__init__.py`.


## Variables experimentales

Las variables experimentales son propiedades del objeto `var`. Un ejemplo es `self.var.my_line_edit_var` del ejemplo anterior. Estas variables definen el complemento y se analizan desde y hacia el guión de OpenSesame. Ver también:

- %link:manual/variables%


## Crear un paquete y subirlo a PyPI

La forma más fácil de crear un paquete para su complemento es definiendo un archivo `pyproject.toml` y utilizando `poetry` para construir el paquete y subirlo a `pypi`.

- <https://python-poetry.org/>

Un ejemplo de archivo `pyproject.toml` es el siguiente:

```toml
[tool.poetry]
name = "opensesame-plugin-example"
version = "0.0.1"
description = "Un ejemplo de complemento para OpenSesame"
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

Una vez que haya agregado este archivo a la carpeta raíz de su código de complemento, puede construir un paquete `.whl` ejecutando:

```bash
poetry build
```

Una vez que haya construido con éxito un paquete, cree una cuenta en <https://pypi.org/>, cree un token de API para su cuenta y autentique `poetry` de esta manera:

```bash
poetry config pypi-token.pypi [api_token]
```

Una vez hecho esto, puede publicar su paquete en PyPi ejecutando el siguiente comando:

```bash
poetry publish
```


¡Ahora sus usuarios podrán instalar su complemento con pip!

```bash
pip install opensesame-plugin-example
```


## Ejemplos

Para ver un ejemplo funcional, consulte:

- <https://github.com/open-cogsci/opensesame-plugin-example>

Otros ejemplos se pueden encontrar en la carpeta `opensesame_plugins` del código fuente de OpenSesame:

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_plugins/core>