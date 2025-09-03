title: Descargar
hash: e832cf1e1be9442432bd3d542053f2fe1b63fb4c9693f37b64cda1907e87dba6
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

Tu copiloto de IA para OpenSesame. Tu suscripción de €9/mes apoya a OpenSesame.

Haz clic <a id="click-here">aquí</a> si tu descarga no comienza.
</div>


## Descripción general

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Opciones de instalación estándar

La última versión $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Instalador estándar</b> de Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows estándar</b> sin instalación requerida (.zip)
</a>

La mayoría de las personas descargan el paquete instalador `.exe`. Si no tienes privilegios de administrador, o si necesitas ejecutar múltiples versiones de OpenSesame al mismo tiempo, descarga el paquete `.zip` en su lugar.

Basado en Python 3.13 para sistemas de 64 bits. Probado en Windows 11.

Algunos dispositivos externos, como los rastreadores oculares [EyeLink](%url:eyelink%) y [Tobii](%url:tobii%), requieren una versión diferente de Python. Consulta las páginas de documentación respectivas para obtener más información.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquete Mac OS (.dmg)
</a>

Cuando inicies OpenSesame por primera vez, el sistema operativo lo bloqueará porque la aplicación no es de un desarrollador confiable. Encontrarás la opción 'Abrir de todos modos' en Configuración > Privacidad y Seguridad. Esta opción aparece después de que la aplicación ha sido bloqueada.

Basado en Python 3.13 para sistemas intel de 64 bits. Probado en Mac OS X Sequoia.

Algunos dispositivos externos, como los rastreadores oculares [EyeLink](%url:eyelink%) y [Tobii](%url:tobii%), requieren una versión diferente de Python. Consulta las páginas de documentación respectivas para obtener más información.


### Linux / Ubuntu

Copia y pega las siguientes líneas en una terminal. Esto descargará y ejecutará un script de instalación.

```bash
# Estos paquetes deben estar instalados en Ubuntu 24.04.
# Los paquetes equivalentes deben instalarse en otras
# distribuciones Linux.
sudo apt install curl python3-venv libxcb-cursor0
# Descarga y ejecuta el script de instalación de OpenSesame.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Probado en Ubuntu 24.04 (Python 3.12).


## Opciones de instalación avanzadas


### PyPi (multiplataforma)

Todos los paquetes pueden instalarse con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

Dependencias principales de OpenSesame:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy para el backend (por defecto) psycho. Dependiendo de tu sistema operativo y versión de Python, es posible que PsychoPy no se instale correctamente. Si esto ocurre, pide ayuda en el foro de soporte o utiliza uno de los paquetes/ instaladores preconstruidos.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze para el registro ocular:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment para el backend xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Una vez hayas instalado todos los paquetes, puedes ejecutar OpenSesame simplemente ejecutando:

```bash
opensesame
```

O para Sigmund Analyst (editor de código):

```bash
sigmund-analyst
```


### Anaconda (multiplataforma)

Primero, crea un nuevo entorno de Python para OpenSesame (opcional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Luego, sigue las instrucciones de instalación de PyPi mencionadas arriba. Ya no se proporcionan paquetes dedicados para Anaconda.


### Versiones anteriores de OpenSesame y otras versiones de Python

Versiones anteriores de OpenSesame, así como paquetes construidos con diferentes versiones de Python (3.10, 3.11 y 3.12), están disponibles en los lanzamientos de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>



### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame se desarrolla y prueba actualmente con Python 3.13. Otras versiones de Python >=3.10 funcionan pero no han sido probadas exhaustivamente. Python 2 ya no es compatible. La última versión que incluyó un paquete para Python 2 fue la 3.3.12, que aún puede descargarse desde el [archivo de lanzamientos](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la última versión de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estás recopilando datos.
- Ejecuta un experimento con la misma versión de OpenSesame con la que lo desarrollaste y probaste.


### Actualización manual de paquetes

OpenSesame es un entorno de Python normal y puedes ejecutar comandos `pip install` en la consola de Jupyter.


### Consejos para administradores de sistemas

- Cuando se lanza una nueva versión mayor de OpenSesame (con una versión terminada en 0, por ejemplo 3.1.0), generalmente le siguen una o dos versiones de mantenimiento (por ejemplo 3.1.1 y 3.1.2) que corrigen errores importantes. Por lo tanto, si vas a instalar OpenSesame en sistemas que no actualizas frecuentemente, lo mejor es esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo 3.0.2, 3.1.3, etc.). Así minimizas el riesgo de desplegar una versión de OpenSesame que contenga errores graves.
- El instalador de Windows te permite instalar OpenSesame de manera silenciosa usando el flag `/S`.