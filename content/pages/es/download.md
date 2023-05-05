title: Descargar
hash: 159033a35d46f15bbe0bbe825928221de5d0278c55011bbe8be3bb7707958892
locale: es
language: Spanish

<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('descarga-iniciada').style.display = 'block'
	document.getElementById('descarga-iniciada').scrollIntoView()
}
</script>

<div class="info-box" id="descarga-iniciada" markdown="1" style="display:none;">

<h3>¡Tu descarga debería comenzar en breve!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://www.buymeacoffee.com/cogsci">
<span class="glyphicon glyphicon-heart" aria-hidden="true"></span>
¡Ayúdanos a mantenernos enfocados y cómpranos un café!
</a>

El café nos mantiene despiertos para que podamos desarrollar software gratuito y responder a tus preguntas en el foro de soporte.

Haz clic <a id="click-here">aquí</a> si tu descarga no comienza.
</div>


## Resumen

%--
toc:
 exclude: [Resumen]
 mindepth: 2
 maxdepth: 3
--%


## Todas las opciones de descarga

La última versión de $status$ es $version$ *$codename$*, lanzada el $release-date$ ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

El paquete de Windows se basa en Python 3.11 para sistemas de 64 bits. Los instaladores y paquetes `.zip` son idénticos, excepto por la instalación. La mayoría de las personas descargan el paquete instalador (botón verde).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Estándar</b> Instalador Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Estándar</b> Windows sin instalación requerida (.zip)
</a>


### Mac OS

Actualmente no hay paquetes preliminares de OpenSesame 4.0 para Mac OS. Por favor, utiliza conda o pip.
{: .page-notification}

[Este artículo](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) en el sitio de soporte de Mac OS explica cómo anular la configuración de seguridad de Mac OS que por defecto impedirá el lanzamiento de OpenSesame.

El paquete a continuación está diseñado para procesadores Intel pero también funciona en procesadores ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 para Intel x64</b> Paquete Mac OS (.dmg)
</a>

Para instalar OpenSesame con [Homebrew](https://brew.sh/), ejecute el siguiente comando en una terminal:

```bash
brew install --cask opensesame
```


### Ubuntu

Los paquetes se desarrollan y prueban en Ubuntu 22.04 Jammy Jellyfish. Los paquetes solo están disponibles para 22.04 y 22.10.

Si tienes OpenSesame 3.X instalado, primero desinstala todos los paquetes . Esto es necesario para evitar conflictos de paquetes debido al ligero cambio de nombre de algunos paquetes en OpenSesame 4.0.

```bash
# Si es necesario: desinstalar OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

A continuación, para agregar los repositorios requeridos a sus fuentes de software e instalar OpenSesame (y Rapunzel), ejecute los siguientes comandos en una terminal:

```bash
# Agregar repositorio para paquetes estables
sudo add-apt-repository ppa:smathot/cogscinl
# Agregar repositorio para paquetes de desarrollo
sudo add-apt-repository ppa:smathot/milgram
# Instalar paquetes OpenSesame 4.X más extensiones útiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Algunos paquetes de uso común no están disponibles a través del PPA. Puedes instalarlos a través de `pip`:

```bash
# Instalar paquetes opcionales que solo están disponibles a través de pip
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy se instala mejor a través de pip, ya que el paquete de Ubuntu está actualmente roto.

```bash
# Instalar psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (multiplataforma)

Todos los paquetes se pueden instalar con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Una vez que hayas instalado todos los paquetes, simplemente puedes ejecutar OpenSesame (después de haber activado el entorno correcto) ejecutando:

```bash
opensesame
```

O para el editor de código Rapunzel:

```bash
rapunzel
```


### Anaconda (multiplataforma)

Primero, crea un nuevo entorno Python para OpenSesame (opcional):

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

A continuación, agregar los canales pertinentes (`cogsci`) y (`conda-forge`) e instalar todos los paquetes relevantes. Asegúrate de que `pyqode.core` y `pyqode.python` sean >= 3.2 del canal `cogsci`, y no las versiones anteriores del canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze
```

Algunos paquetes no están disponibles a través de conda. Puedes usar `pip install` para estos.

```bash
pip install soundfile pygame psychopy psychopy-sounddevice http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

Una vez que hayas instalado todos los paquetes, simplemente puedes ejecutar OpenSesame (después de haber activado el entorno correcto) ejecutando:

```bash
opensesame
```

O para el editor de código Rapunzel:

```bash
rapunzel
```


### Versiones anteriores

Las versiones anteriores se pueden descargar de los lanzamientos de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame se construye y prueba actualmente con Python 3.11.0. Otras versiones de Python >=3.7 funcionan pero no se prueban exhaustivamente. Python 2 ya no es compatible. La última versión que incluyó un paquete de Python 2 fue la 3.3.12, que aún se puede descargar desde el [archivo de lanzamientos](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor utilizar la última versión de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estás recopilando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que utilizaste para desarrollar y probar.


### Actualización manual de paquetes

OpenSesame es un entorno Python regular, y puedes actualizar paquetes con `pip` o `conda` como se describe aquí:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Consejos para administradores de sistemas

- Cuando se lanza una nueva versión principal de OpenSesame (con una versión que termina en 0, por ejemplo, 3.1.0), generalmente es seguida rápidamente por uno o dos lanzamientos de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que abordan errores importantes. Por lo tanto, si estás instalando OpenSesame en sistemas que no actualizas a menudo, es mejor esperar hasta el segundo o tercer lanzamiento de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De esta manera, minimizas el riesgo de implementar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows te permite instalar OpenSesame en silencio utilizando la opción `/S`.