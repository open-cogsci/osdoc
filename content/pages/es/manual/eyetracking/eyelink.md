title: Eyelink
hash: 446281a464dd40eabe3f55f650572a8894359598a77c99f0c8eb20fe31cad1fc
locale: es
language: Spanish

[TOC]

## Acerca de EyeLink

La serie Eyelink de rastreadores oculares, producida por SR Research, es una de las más utilizadas en la investigación psicológica. SR Research proporciona bindings de Python para el Eyelink (llamados PyLink), los cuales son usados por PyGaze. La licencia de PyLink es incompatible con la licencia que utiliza OpenSesame. Por esa razón, PyLink no se incluye en la distribución predeterminada de OpenSesame y debe instalarse por separado.


## Windows

### Instalando el EyeLink Developers Kit

El Eyelink Developers Kit (a veces llamado Display Software) proporciona las bibliotecas necesarias para comunicarte con el PC de Eyelink. Puedes encontrarlo aquí (requiere registro gratuito):

- <https://www.sr-research.com/support/thread-13.html>

Si extraes el archivo `.zip` y luego ejecutas el instalador `.exe`, el display de EyeLink se instalará en una de las siguientes carpetas (dependiendo de tu versión de Windows):

```
C:\Program Files\SR Research\EyeLink\
C:\Program Files (x86)\SR Research\EyeLink
```

En esta carpeta hay una subcarpeta llamada `libs`, que deberás añadir a la variable Path del sistema (es posible que se agregue automáticamente, pero revisa para asegurarte). Puedes hacerlo abriendo "Mi PC", haciendo clic en "Ver información del sistema", abriendo la pestaña "Avanzado", haciendo clic en "Variables de entorno" y agregando `;C:\Program Files\SR Research\EyeLink\libs` o (dependiendo de tu sistema) `;C:\Program Files (x86)\SR Research\EyeLink\libs` a la variable Path (bajo Variables del sistema).


### Instalando OpenSesame con PyLink

`pylink` es la biblioteca de Python para soporte de EyeLink. Actualmente, `pylink` solo es compatible con Python 3.12 y versiones anteriores, mientras que los paquetes estándar de OpenSesame se construyen con Python 3.13. Por lo tanto, debes usar el paquete de OpenSesame para Python 3.12 (o anterior) disponible en [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases).

Luego, puedes instalar `pylink` desde el repositorio PyPi de SR Research con `pip install`:

```
pip install --index-url=https://pypi.sr-research.com sr-research-pylink
```

Importante: *no* intentes instalar `pylink` ejecutando `pip install pylink`. ¡Hacerlo instalará un paquete completamente diferente!

Puedes encontrar más información sobre `pylink` en el foro de SR Research (requiere registro gratuito):

- <https://www.sr-research.com/support/thread-8291.html>


## Ubuntu

El software display de EyeLink puede instalarse directamente desde un repositorio. Esto también instalará PyLink y varias herramientas útiles, como el conversor `edf2asc`.

```bash
sudo add-apt-repository 'deb [arch=amd64] https://apt.sr-research.com SRResearch main'
sudo apt-key adv --fetch-keys https://apt.sr-research.com/SRResearch_key
sudo apt-get update
sudo apt-get install eyelink-display-software
```

Para más información, visita:

- <https://www.sr-support.com/thread-13.html>


## PyGaze

Después de instalar el display de EyeLink y PyLink como se indicó arriba, ¡puedes usar el EyeLink con PyGaze! Consulta:

- %link:pygaze%


## Plugin eyelink de SR Research

SR Research también ofrece sus propios complementos de EyeLink para OpenSesame. Son algo similares a (y originalmente basados en) los complementos de PyGaze, pero ofrecen algunas funcionalidades que no están disponibles a través de PyGaze. Para instalar estos complementos, ejecuta:

```
pip install opensesame-plugin-eyelink
```

Para más información, visita:

- <https://www.sr-research.com/support/thread-52.html>
