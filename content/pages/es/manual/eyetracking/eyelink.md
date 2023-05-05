title: Eyelink
hash: c9635275665d7dc2d7c42f6f480e386381284e31750ff4cd7cbaab5fb4522ee5
locale: es
language: Spanish

[TOC]

## Acerca de EyeLink

La serie de rastreadores de ojos EyeLink, producida por SR Research, es uno de los rastreadores de ojos más utilizados en la investigación psicológica. SR Research proporciona enlaces de Python para EyeLink (llamado PyLink), que son utilizados por PyGaze. La licencia de PyLink es incompatible con la licencia utilizada por OpenSesame. Por esa razón, PyLink no está incluido en la distribución predeterminada de OpenSesame y debe instalarse por separado.

## Foro de SR Research

Necesitarás descargar algún software del foro de SR Research. Este es un foro cerrado, pero puedes registrarte de forma gratuita.

- <https://www.sr-support.com/>


## Windows

### Instalación del Kit de Desarrollo EyeLink

El EyeLink Developers Kit (a veces llamado Display Software) proporciona las bibliotecas necesarias para comunicarse con el PC EyeLink. Puedes encontrarlo aquí:

- <https://www.sr-support.com/thread-13.html>

Si extraes el archivo .zip y luego ejecutas el instalador .exe, el visor EyeLink se instalará en una de las siguientes carpetas (dependiendo de la versión de tu sistema Windows:

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

En esta carpeta, hay una subcarpeta `libs`, que debes agregar al camino del sistema (es posible que se haya agregado al camino automáticamente, pero verifica para asegurarte). Puedes hacer esto abriendo "Mi PC", haciendo clic en "Ver información del sistema", abriendo la pestaña "Avanzado", haciendo clic en "Variables de entorno" y añadiendo `;C:\Program Files\SR Research\EyeLink\libs` o (dependiendo de tu sistema) `;C:\Program Files (x86)\SR Research\EyeLink\libs` a la variable Path (en las variables del sistema).


### Instalación de PyLink

PyLink es la biblioteca Python para soporte EyeLink. PyLink se incluye con versiones recientes del software de visualización EyeLink (descrito anteriormente) y puedes encontrarlo en una de las siguientes carpetas (dependiendo de tu versión de Windows):

```
C:\Program Files\SR Research\EyeLink\SampleExperiments\Python
C:\Program Files (x86)\SR Research\EyeLink\SampleExperiments\Python
```

Alternativamente, puedes descargar Pylink desde aquí:

- <https://www.sr-support.com/thread-13.html>

Para instalar PyLink en OpenSesame, simplemente copia la carpeta con el PyLink en la carpeta del programa OpenSesame o en la subcarpeta `Lib\site-packages`. En algunos casos, la carpeta `pylink` tiene un nombre como `pylink27-amd64`, en cuyo caso debes cambiar el nombre a `pylink`.

__Importante:__ La versión de Python de PyLink debe coincidir con la versión de Python de tu instalación de OpenSesame. En la mayoría de los casos, esto significa que necesitas PyLink para Python 3.7.


## Ubuntu

El software de visualización EyeLink se puede instalar directamente desde un repositorio. Esto también instala PyLink y varias herramientas convenientes, como el convertidor `edf2asc`.

```bash
sudo add-apt-repository "deb http://download.sr-support.com/software SRResearch main"
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Para obtener más información, visita:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Después de haber instalado el software de visualización EyeLink y PyLink según las instrucciones anteriores, ¡puedes usar EyeLink con PyGaze! Consulta:

- %link:pygaze%