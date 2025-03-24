title: Descargar
hash: 48b36f28d46849599cac6b02aa148d9b70d6476758c8b21e016736aed881ea59
locale: es
language: Spanish

<script>
function startDownload(url) {
	document.getElementById('click-here').href = url
	window.location.href = url
	document.getElementById('download-started').style.display = 'block'
	document.getElementById('download-started').scrollIntoView()
}
</script>

<div class="info-box" id="download-started" markdown="1" style="display:none;">

<h3>¡Tu descarga debería comenzar en breve!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Suscribirse a SigmundAI.eu
</a>

Mejor que ChatGPT para preguntas de OpenSesame. Tu suscripción de €9/mes apoya a OpenSesame.

Haz clic <a id="click-here">aquí</a> si la descarga no comienza.

</div>


## Información general

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Todas las opciones de descarga

La última versión de $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

El paquete de Windows se basa en Python 3.11 para sistemas de 64 bits. El instalador y los paquetes `.zip` son idénticos, excepto por la instalación. La mayoría de las personas descargan el paquete del instalador (botón verde).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Estándar</b> Instalador de Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Estándar</b> Windows sin instalación requerida (.zip)
</a>


### Mac OS

[Este artículo](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) en el sitio de soporte de Mac OS explica cómo anular los ajustes de seguridad de Mac OS que por defecto impedirán que OpenSesame se inicie. La primera vez que inicies OpenSesame tomará mucho tiempo antes de que la aplicación comience; los lanzamientos posteriores irán mucho más rápido.

El paquete a continuación está construido para procesadores Intel pero también se ejecuta en procesadores ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Python 3 para Intel x64</b> Paquete de Mac OS (.dmg)
</a>

Para instalar OpenSesame con [Homebrew](https://brew.sh/), ejecuta el siguiente comando en una terminal:

```bash
brew install --cask opensesame
```


### Ubuntu

Los paquetes se desarrollan y prueban en Ubuntu 24.04 Jammy Jellyfish. Tu experiencia puede variar en otras versiones de Ubuntu.

Si tienes OpenSesame 3.X instalado, primero desinstala todos los paquetes. Esto es necesario para evitar conflictos de paquetes debido a una ligera renombración de algunos paquetes en OpenSesame 4.0.

```bash
# Si es necesario: desinstalar OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Luego, para agregar los repositorios requeridos a tus fuentes de software e instalar OpenSesame (y Rapunzel), ejecuta los siguientes comandos en una terminal:

```bash
# Agregar repositorio para paquetes estables
sudo add-apt-repository ppa:smathot/cogscinl
# Agregar repositorio para paquetes de desarrollo
sudo add-apt-repository ppa:smathot/milgram
# Instalar paquetes OpenSesame 4.X más extensiones útiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Algunos paquetes comúnmente usados no están disponibles a través del PPA. Puedes instalarlos a través de `pip`:

```bash
# Instalar paquetes opcionales que sólo están disponibles a través de pip
pip install --break-system-packages --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy es mejor instalarlo a través de pip, porque el paquete de Ubuntu actualmente está roto.

```bash
# Primero instala una versión personalizada de wxPython, que es necesaria para PsychoPy
pip install --break-system-packages https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04/wxPython-4.2.2-cp312-cp312-linux_x86_64.whl
# Luego instala psychopy e ignora el requisito para Python <=3.11, porque Ubuntu 24.04 usa Python 3.12
pip install --break-system-packages --ignore-requires-python psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (multiplataforma)

Todos los paquetes se pueden instalar con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

También puede ser necesario instalar PyQt5 y QtWebEngine, que proporcionan el conjunto de herramientas GUI:

```bash
pip install pyqt5 pyqtwebengine
```


Una vez hayas instalado todos los paquetes, puedes ejecutar OpenSesame simplemente (después de haber activado el entorno correcto) ejecutando:

```bash
opensesame
```

O para el editor de código Rapunzel:

```bash
rapunzel
```


### Anaconda (multiplataforma)

Primero, crea un nuevo entorno de Python para OpenSesame (opcional):

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Luego, añade los canales relevantes (`cogsci`) y (`conda-forge`) e instala todos los paquetes relevantes. Asegúrate de que `pyqode.core` y `pyqode.python` son >= 3.2 del canal `cogsci`, y no las versiones más antiguas del canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Algunos paquetes no están disponibles a través de conda. Puedes usar `pip install` para estos. (Se sabe que PsychoPy falla en la instalación en algunos sistemas, por lo que se instala por separado a continuación).

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Una vez hayas instalado todos los paquetes, puedes ejecutar OpenSesame simplemente (después de haber activado el entorno correcto) ejecutando:

```bash
opensesame
```

O para el editor de código Rapunzel:

```bash
rapunzel
```


### Versiones anteriores

Versiones anteriores se pueden descargar desde los lanzamientos de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame actualmente se construye y prueba con Python 3.11. Otras versiones de Python >=3.7 funcionan pero no se prueban extensamente. Python 2 ya no es compatible. La última versión que incluyó un paquete de Python 2 fue la 3.3.12, que todavía se puede descargar desde el [archivo de lanzamientos](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la última versión de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estás recopilando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollar y probar.


### Actualización manual de paquetes

OpenSesame es un entorno Python regular, y puedes actualizar los paquetes con `pip` o `conda` como se describe aquí:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Consejos para administradores del sistema

- Cuando se lanza una nueva versión importante de OpenSesame (con un número de versión que termina en 0, por ejemplo, 3.1.0), generalmente es seguida rápidamente por una o dos versiones de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que abordan errores importantes. Por lo tanto, si vas a instalar OpenSesame en sistemas que no actualizas con frecuencia, es mejor esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De esa manera minimizas el riesgo de implementar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows te permite instalar OpenSesame de manera silenciosa usando el modificador `/S`.