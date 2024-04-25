title: Descargar
hash: fd00279bec39b52c5cf277e973c6f314758b571714fbc3b1fb8730ac172aa061
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


## Visión general

%--
toc:
 exclude: [Visión general]
 mindepth: 2
 maxdepth: 3
--%


## Todas las opciones de descarga

La última versión $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

El paquete de Windows está basado en Python 3.11 para sistemas de 64 bits. Los paquetes de instalador y `.zip` son idénticos, a excepción de la instalación. La mayoría descarga el paquete de instalador (botón verde).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Instalador</b> estándar de Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows</b> sin necesidad de instalación (.zip) estándar
</a>


### Mac OS

[Este artículo](https://support.apple.com/en-in/guide/mac-help/mh40616/mac) en el sitio de soporte de Mac OS explica cómo anular la configuración de seguridad de Mac OS, que por defecto previene la ejecución de OpenSesame. La primera vez que inicies OpenSesame se tardará mucho tiempo en arrancar la aplicación; los lanzamientos subsiguientes son mucho más rápidos.

El paquete a continuación está construido para procesadores Intel pero también funciona en procesadores ARM (M1).

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	<b>Paquete</b> Mac OS para Python 3 para Intel x64 (.dmg)
</a>

Para instalar OpenSesame con [Homebrew](https://brew.sh/), ejecuta el siguiente comando en un terminal:

```bash
brew install --cask opensesame
```


### Ubuntu

Los paquetes se desarrollan y prueban en Ubuntu 22.04 Jammy Jellyfish. Los paquetes están disponibles solo para las versiones 22.04 y 22.10.

Si tienes instalado OpenSesame 3.X, primero desinstala todos los paquetes. Esto es necesario para evitar conflictos de paquetes debido al ligero cambio de nombre de algunos paquetes en OpenSesame 4.0.

```bash
# Si es necesario: desinstalar OpenSesame 3.X
sudo apt remove python3-opensesame python3-pyqode.python python3-pyqode.core python3-rapunzel python3-opensesame-extension* python3-opensesame-plugin*
```

Luego, para añadir los repositorios necesarios a tus fuentes de software e instalar OpenSesame (y Rapunzel), ejecuta los siguientes comandos en un terminal:

```bash
# Añadir repositorio para los paquetes estables
sudo add-apt-repository ppa:smathot/cogscinl
# Añadir repositorio para los paquetes de desarrollo
sudo add-apt-repository ppa:smathot/milgram
# Instalar los paquetes de OpenSesame 4.X más extensiones útiles
sudo apt install python3-opensesame python3-rapunzel python3-opensesame-extension-updater python3-pygaze python3-pygame python3-opensesame-extension-language-server
```

Algunos paquetes comúnmente usados no están disponibles a través del PPA. Puedes instalarlos mediante `pip`:

```bash
# Instalar paquetes opcionales que solo están disponibles a través de pip
pip install --pre opensesame-extension-osweb opensesame-plugin-psychopy opensesame-plugin-media_player_mpy http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
```

PsychoPy se instala mejor mediante pip, ya que el paquete de Ubuntu actualmente está roto.

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

Primero, crea un nuevo entorno de Python para OpenSesame (opcional):

```bash
conda create -n opensesame-py3
conda activate opensesame-py3
```

Luego, añade los canales relevantes (`cogsci`) y (`conda-forge`) e instala todos los paquetes relevantes. Asegúrate de que `pyqode.core` y `pyqode.python` sean >= 3.2 del canal `cogsci`, y no las versiones antiguas del canal `conda-forge`.

```bash
conda config --add channels conda-forge --add channels cogsci
conda install opensesame opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy rapunzel pygaze qtconsole pyqtwebengine wxpython
```

Algunos paquetes no están disponibles a través de conda. Puedes usar `pip install` para estos. (Se sabe que PsychoPy falla al instalarse en algunos sistemas, por eso se instala por separado a continuación).

```bash
pip install soundfile pygame http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl
pip install psychopy psychopy-sounddevice
```

Una vez que hayas instalado todos los paquetes, simplemente puedes ejecutar OpenSesame (después de haber activado el entorno correcto) ejecutando:

```bash
opensesame
```

O para el editor de código Rapunzel:

```bash
rapunzel
```


### Versiones antiguas

Las versiones anteriores se pueden descargar de los lanzamientos en GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame actualmente se construye y se prueba con Python 3.11 Otras versiones de Python >=3.7 funcionan pero no están probadas extensivamente. Python 2 ya no está soportado. La última versión que incluyó un paquete de Python 2 fue la 3.3.12, que aún se puede descargar del [archivo de lanzamientos](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la última versión de OpenSesame.
- No actualices mientras estés ejecutando un experimento; es decir, no actualices mientras estés recolectando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollar y probar.


### Actualizando paquetes manualmente

OpenSesame es un entorno de Python regular, y puedes actualizar paquetes con `pip` o `conda` como se describe aquí:

- <https://rapunzel.cogsci.nl/manual/environment/>


### Consejos para administradores de sistemas

- Cuando se lanza una nueva versión principal de OpenSesame (con una versión que termina en 0, por ejemplo, 3.1.0), generalmente es seguida rápidamente por una o dos versiones de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que abordan errores importantes. Por lo tanto, si estás instalando OpenSesame en sistemas que no actualizas a menudo, es mejor esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De esa manera minimizas el riesgo de implementar una versión de OpenSesame que contenga errores graves.
- El instalador de Windows te permite instalar OpenSesame silenciosamente utilizando la bandera `/S`.
