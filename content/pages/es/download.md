title: Descargar
hash: 38128d277ebe6e5684caf8cc54f9d14c8497654ad399028843668298333d7df4
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
 &#128150; Suscríbete a SigmundAI.eu
</a>

Mejor que ChatGPT para preguntas sobre OpenSesame. Tu suscripción de €9/mes apoya a OpenSesame.

Haz clic <a id="click-here">aquí</a> si tu descarga no comienza.
</div>


## Resumen


## Todas las opciones de descarga

La última versión $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

El paquete para Windows se basa en Python 3.11 para sistemas de 64 bits. Los paquetes instalador y `.zip` son idénticos, excepto por la instalación. La mayoría de las personas descargan el paquete instalador (botón verde).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Instalador</b> estándar para Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows</b> sin necesidad de instalación (.zip)
</a>


### Mac OS

[Este artículo](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) en el sitio de soporte de Mac OS explica cómo anular la configuración de seguridad de Mac OS que, por defecto, prevendrá que OpenSesame se ejecute. La primera vez que inicies OpenSesame tardará mucho tiempo antes de que la aplicación comience; los inicios subsiguientes son mucho más rápidos.

El paquete a continuación está construido para procesadores Intel pero también funciona en procesadores ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Paquete para Mac OS con Python 3</b> para Intel x64 (.dmg)
</a>

Para instalar OpenSesame con [Homebrew](https://brew.sh/), ejecuta el siguiente comando en un terminal:

```bash
brew install --cask opensesame
```


### Ubuntu

Los paquetes son desarrollados y probados en Ubuntu 22.04 Jammy Jellyfish. Solo están disponibles para 22.04 y 22.10.

Si tienes OpenSesame 3.X instalado, primero desinstala todos los paquetes. Esto es necesario para evitar conflictos de paquetes debido al ligero cambio de nombre de algunos paquetes en OpenSesame 4.0.

```bash
# Si es necesario: desinstala OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

A continuación, para agregar los repositorios necesarios a tus fuentes de software e instalar OpenSesame (y Rapunzel), ejecuta los siguientes comandos en un terminal:

```bash
# Agrega un repositorio para paquetes estables
sudo add-apt-repository ppa:smathot/cogscinl
# Agrega un repositorio para paquetes de desarrollo
sudo add-apt-repository ppa:smathot/milgram
# Instala paquetes OpenSesame 4.X más extensiones útiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Algunos paquetes comúnmente usados no están disponibles a través del PPA. Puedes instalarlos mediante `pip`:

```bash
# Instala paquetes opcionales que solo están disponibles a través de pip
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy es mejor instalarlo a través de pip, ya que el paquete de Ubuntu está actualmente roto.

```bash
# Instala psychopy
pip install psychopy psychopy_sounddevice python-bidi arabic_reshaper
```


### PyPi (multiplataforma)

Todos los paquetes se pueden instalar con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

```bash
pip install --pre opensesame-core rapunzel opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy
pip install psychopy psychopy_sounddevice pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

También puede que necesites instalar PyQt5 y QtWebEngine, que proporcionan el kit de herramientas de la GUI:

```bash
pip install pyqt5 pyqtwebengine
```

Una vez que hayas instalado todos los paquetes, puedes simplemente ejecutar OpenSesame (después de haber activado el entorno correcto) ejecutando:

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

Luego, agrega los canales relevantes (`cogsci`) y (`conda-forge`) e instala todos los paquetes relevantes. Asegúrate de que `pyqode.core` y `pyqode.python` sean >= 3.2 del canal `cogsci`, y no las versiones más antiguas del canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Algunos paquetes no están disponibles a través de conda. Puedes usar `pip install` para estos. (Se sabe que PsychoPy falla al instalarse en algunos sistemas, por lo que se instala por separado a continuación).

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Una vez que hayas instalado todos los paquetes, puedes simplemente ejecutar OpenSesame (después de haber activado el entorno correcto) ejecutando:

```bash
opensesame
```

O para el editor de código Rapunzel:

```bash
rapunzel
```


### Versiones anteriores

Las versiones anteriores se pueden descargar desde los lanzamientos de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame actualmente está construido y probado con Python 3.11. Otras versiones de Python >=3.7 funcionan, pero no se prueban extensamente. Python 2 ya no es compatible. La última versión que incluyó un paquete de Python 2 fue la 3.3.12, que aún puede descargarse del [archivo de versiones](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la última versión de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estás recopilando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollar y probar.


### Actualización manual de paquetes

OpenSesame es un entorno regular de Python, y puedes actualizar paquetes con `pip` o `conda` como se describe aquí:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Consejos para administradores de sistemas

- Cuando se lanza una nueva versión principal de OpenSesame (con una versión que termina en 0, por ejemplo, 3.1.0), generalmente es seguida rápidamente por uno o dos lanzamientos de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que abordan errores importantes. Por lo tanto, si estás instalando OpenSesame en sistemas que no actualizas a menudo, es mejor esperar hasta el segundo o tercer lanzamiento de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De esa manera, minimizas el riesgo de desplegar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows te permite instalar OpenSesame silenciosamente usando el flag `/S`.