title: Descargar
hash: 9beb2ebf584b530f7411227d288486a4076872b885ede71e4a690dd50ad929c9
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
	<b>Instalador estándar</b> para Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows estándar</b> sin instalación requerida (.zip)
</a>

La mayoría de las personas descargan el paquete instalador `.exe`. Si no tienes privilegios de administrador, o si necesitas ejecutar varias versiones de OpenSesame en paralelo, descarga el paquete `.zip` en su lugar.

Basado en Python 3.13 para sistemas de 64 bits. Probado en Windows 11.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquete para Mac OS (.dmg)
</a>

Cuando inicies OpenSesame por primera vez, el sistema operativo lo bloqueará porque la app no proviene de un desarrollador de confianza. Encontrarás la opción ‘Abrir de todas formas’ en Configuración > Privacidad y seguridad. Esta opción aparece después de que la app sea bloqueada.

Basado en Python 3.13 para sistemas Intel de 64 bits. Probado en Mac OS X Sequoia.


### Linux / Ubuntu

Copia y pega las siguientes líneas en una terminal. Esto descargará y ejecutará un script de instalación.

```bash
# Estos paquetes deben instalarse en Ubuntu 24.04.
# Los paquetes equivalentes deben instalarse en otras
# distribuciones de Linux.
sudo apt install curl python3-venv libxcb-cursor0
# Descarga y ejecuta el script de instalación de OpenSesame.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

Probado en Ubuntu 24.04 (Python 3.12).


## Opciones avanzadas de instalación


### PyPi (multiplataforma)

Todos los paquetes pueden instalarse usando pip. Ten en cuenta que OpenSesame se denomina `opensesame-core` en PyPi.

Dependencias principales de OpenSesame:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy para el backend (predeterminado) psycho. Dependiendo de tu sistema operativo y la versión de Python, es posible que PsychoPy no se instale correctamente. Si ocurre esto, busca ayuda en el foro de soporte o utiliza uno de los paquetes/instaladores preconstruidos.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze para el seguimiento ocular:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment para el backend xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Una vez que hayas instalado todos los paquetes, simplemente puedes ejecutar OpenSesame con:

```bash
opensesame
```

O Sigmund Analyst (editor de código):

```bash
sigmund-analyst
```


### Anaconda (multiplataforma)

Primero, crea un nuevo entorno de Python para OpenSesame (opcional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

Después, sigue las instrucciones de instalación por PyPi indicadas arriba. Ya no se proveen paquetes dedicados para Anaconda.


### Versiones anteriores

Las versiones anteriores se pueden descargar desde las publicaciones de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

Actualmente, OpenSesame se construye y prueba con Python 3.13. Otras versiones de Python >=3.10 funcionan pero no se han probado exhaustivamente. Python 2 ya no es compatible. La última versión que incluyó un paquete para Python 2 fue la 3.3.12, que todavía se puede descargar desde el [archivo de versiones](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la versión más reciente de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estás recolectando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollar y probar.


### Actualización manual de paquetes

OpenSesame es un entorno Python normal y puedes ejecutar comandos `pip install` en la consola de Jupyter.


### Consejos para administradores de sistemas

- Cuando se publica una nueva versión mayor de OpenSesame (con un número de versión que termina en 0, por ejemplo 3.1.0), generalmente le siguen rápidamente una o dos versiones de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que corrigen errores importantes. Por lo tanto, si vas a instalar OpenSesame en sistemas que no actualizas con frecuencia, es preferible esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De esa manera minimizas el riesgo de desplegar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows permite instalar OpenSesame de forma silenciosa usando el indicador `/S`.