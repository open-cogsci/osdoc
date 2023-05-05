title: Creando una extensión
hash: 91a79a763c57d0445f9ee814ec6e513ab04f651b716fdd1fe99937052b85df97
locale: es
language: Spanish

[TOC]


## ¿Qué es una extensión de OpenSesame?

Las *extensiones* agregan funcionalidad arbitraria a la interfaz de usuario de OpenSesame. Por ejemplo, una extensión puede agregar una nueva entrada a la barra de herramientas principal o al menú. (Para agregar funcionalidad que se pueda utilizar en experimentos, necesita un [plugin](%url:plugin%).)


## Archivos relevantes

Una o más extensiones se agrupan en un paquete de extensión, que siempre es un subpaquete de `opensesame_extensions` (que a su vez es un llamado paquete de espacio de nombres implícito, pero ese es un detalle técnico que no es muy importante). Supongamos que su paquete de extensión se llama `example` y que contiene una única extensión (puede haber más) llamada `example_extension`. Esto correspondería a la siguiente estructura de archivos y carpetas:

```
opensesame_extensions/
    example/
        __init__.py               # puede estar vacío pero debe existir
        example_extension/
            __init__.py           # contiene información de extensión
            example_extension.py  # contiene clase de extensión
```


## Información de extensión

La información de la extensión se define en el `__init__.py` del módulo de extensión, por lo que en nuestro ejemplo este es `opensesesame_extensions/example/example_extension/__init__.py`.

```python
"""Una cadena de documentación con una descripción de la extensión"""

# Un nombre de icono estándar
# - <https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>
icon = 'applications-accessories'
# La etiqueta y el tooltip se usan para crear la acción predeterminada, que es
# insertar en el menú y / o barra de herramientas (o ninguno)
label = "Extensión de ejemplo"
tooltip = "Ejemplo de información sobre herramientas"
menu = {
    "index": -1,
    "separator_before": True,
    "separator_after": True,
    "submenu": "Ejemplo"
}
toolbar = {
    "index": -1,
    "separator_before": True,
    "separator_after": True
}
# La configuración se almacena de forma persistente en el objeto cfg
settings = {
    "example_setting": "valor de ejemplo"
}
```

Una extensión puede aparecer en el menú o en la barra de herramientas principal de OpenSesame. Esto requiere que defina varios campos en `__init__.py` como se muestra arriba:

- La `label` es el texto que aparecerá en el menú.
- El `icon` es un [nombre de icono compatible con freedesktop][icon-spec] que especifica el icono que aparecerá en el menú y / o barra de herramientas.
- El `index` indica la posición de la extensión en el menú / barra de herramientas, y funciona como un índice de `list`. Es decir, los valores negativos son relativos a la última entrada, donde -1 coloca su extensión al final.

Para que su extensión responda a la activación del menú / barra de herramientas, implemente el método `activate()` como se muestra a continuación en el código de extensión.


## Escribiendo el código de extensión

El código principal de extensión se coloca en `[extension_name].py`. Este archivo generalmente contiene solo una clase llamada `[ExtensionName].py`, es decir, una clase con el equivalente CamelCase del nombre del plugin, que hereda `libqtopensesame.extensions.BaseExtension`. Entonces, una clase de extensión básica (no funcional) se ve así:

~~~ .python
from libopensesame.py3compat import *
from libopensesame.oslogging import oslogger
from libqtopensesame.extensions import BaseExtension


class ExampleExtension(BaseExtension):
    """Una extensión de ejemplo que enumera varios eventos comunes. El nombre de la clase
    debe ser la versión CamelCase del folder_name y file_name. Entonces, en
    este caso, tanto la carpeta de extensión (que es un paquete de Python) como el
    archivo .py (que es un módulo de Python) se llaman example_extension, mientras que
    la clase se llama ExampleExtension.
    """

    def activate(self):
        oslogger.debug('se activó la extensión example_extension')

    def event_save_experiment(self, path):
        oslogger.debug(f'Se disparó el evento: save_experiment(path={path})')

    # Vea el código fuente de example_extension para obtener más oyentes de eventos
~~~


## Escuchar eventos

OpenSesame dispara eventos cuando ocurre algo importante. Por ejemplo, el evento `save_experiment` se dispara cuando se guarda un experimento. Para que su extensión escuche un evento, simplemente implemente un método con el nombre `event_[nombre del evento]` como se muestra arriba.

Tenga en cuenta que algunos eventos toman argumentos de palabras clave, como `path` en el caso de `save_experiment`. La firma de palabras clave de su función debe coincidir con la firma de palabras clave esperada. Consulte la descripción general de eventos a continuación para obtener una lista completa de eventos y palabras clave esperadas.

## Creando un paquete y subiéndolo a pypi

Crear un paquete de extensión y cargarlo en `pypi` funciona de la misma manera que lo hace para los complementos:

- %link:plugin%
- <https://github.com/open-cogsci/opensesame-extension-example>

## Ejemplos

Para un ejemplo funcional, consulte:

- <https://github.com/open-cogsci/opensesame-extension-example>

Otros ejemplos se pueden encontrar en la carpeta `opensesame_extensions` del código fuente de OpenSesame:

- <https://github.com/open-cogsci/OpenSesame/tree/milgram/opensesame_extensions/core>

[example]: https://github.com/open-cogsci/OpenSesame/tree/master/extensions/example
[icon-spec]: http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html

## Resumen de eventos

Esta descripción general enumera todos los eventos que se disparan en algún lugar del código, y que su extensión puede escuchar implementando las funciones `event_[nombredelevento]()` correspondientes.

%-- include: include/events.md --%