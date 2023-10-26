title: Eyelink
hash: 795cf5b31d90084e4fe773cb7002ad511f76aa023cfef172927e5544fd44ed44
locale: es
language: Spanish

[TOC]

## Acerca de EyeLink

La serie de rastreadores oculares Eyelink, producida por SR Research, es uno de los rastreadores oculares más utilizados en la investigación psicológica. SR Research proporciona enlaces de Python para EyeLink (llamado PyLink), que son utilizados por PyGaze. La licencia de PyLink es incompatible con la licencia utilizada por OpenSesame. Por esa razón, PyLink no está incluido en la distribución predeterminada de OpenSesame y debe instalarse por separado.


## Windows

### Instalación del kit de desarrollo EyeLink

El Kit de Desarrollo de EyeLink (a veces llamado Software de visualización) proporciona las librerías que se necesitan para comunicarse con el PC de EyeLink. Puedes encontrarlo aquí (se requiere registro gratuito):

- <https://www.sr-research.com/support/thread-13.html>

Si extraes el archivo `.zip` y luego ejecutas el instalador `.exe`, la visualización de EyeLink se instalará en una de las siguientes carpetas (dependiendo de tu versión de Windows:

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

En esta carpeta, hay una subcarpeta `libs`, que necesitas agregar al Path del sistema (esto puede haberse añadido automáticamente al Path, pero verifica para asegurarte). Puedes hacer esto abriendo "Mi PC", haciendo clic en "Ver información del sistema", abriendo la pestaña "Avanzado", haciendo clic en "Variables de entorno" y añadiendo `;C:\Program Files\SR Research\EyeLink\libs` o (dependiendo de tu sistema) `;C:\Program Files (x86)\SR Research\EyeLink\libs` a la variable Path (bajo las Variables de sistema).


### Instalación de OpenSesame con PyLink

PyLink es la biblioteca de Python para el soporte de EyeLink. A julio de 2023, PyLink soporta versiones de Python hasta 3.10, mientras que OpenSesame por defecto usa Python 3.11. Por lo tanto, hasta que PyLink se actualice para Python 3.11, la forma más sencilla de instalar OpenSesame con PyLink es construyendo un entorno Python 3.10 a través de Anaconda.

Esto suena complicado, pero en realidad no lo es. Para hacerlo, primero lee el procedimiento general para instalar OpenSesame a través de Anaconda como se describe en la página de Descargas:

- %link:download%

Luego, una vez que entiendas el procedimiento general, comienza por crear un entorno de Python 3.10, continúa con las instrucciones de la página de Descargas y luego instala PyLink:

```
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
```

Puedes encontrar más información sobre PyLink en el foro de SR Research (se requiere registro gratuito):

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

El software de visualización de EyeLink se puede instalar directamente desde un repositorio. Esto también instala PyLink y varias herramientas convenientes, como el convertidor `edf2asc`.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Para más información, por favor visita:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Después de haber instalado el software de visualización de EyeLink y PyLink según las instrucciones anteriores, ¡puedes usar EyeLink con PyGaze! Ver:

- %link:pygaze%
