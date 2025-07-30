title: Descargar
hash: acf8377b52efc30d1c3f5f4f459cb00a79f09028ca118806c6cf122c7a3e9925
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

Mejor que ChatGPT para preguntas sobre OpenSesame. Tu suscripción de 9 €/mes apoya a OpenSesame.

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

La versión $status$ más reciente es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

El paquete de Windows está basado en Python 3.13 para sistemas de 64 bits. El instalador y los paquetes `.zip` son idénticos, salvo por la instalación. La mayoría de las personas descarga el paquete instalador (botón verde).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Instalador estándar</b> de Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows estándar</b> sin instalación requerida (.zip)
</a>

OpenSesame es desarrollado y probado en Windows 11. Tu experiencia puede variar en otras versiones de Windows.


### Mac OS

Los paquetes de Mac OS aún no están disponibles para OpenSesame 4.1. El enlace de descarga de abajo apunta aún a la versión 4.0.
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquete para Mac OS (.dmg)
</a>


### Linux / Ubuntu

Copia y pega la siguiente línea en una terminal. Esto descargará y ejecutará un script de instalación. El script de instalación requiere curl y virtualenv. En Ubuntu pueden instalarse con `sudo apt install curl python3-venv`.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame es desarrollado y probado en Ubuntu 24.04. Tu experiencia puede variar en otras distribuciones de Linux y otras versiones de Ubuntu.


## Opciones avanzadas de instalación


### PyPi (multiplataforma)

Todos los paquetes se pueden instalar con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

Dependencias principales de OpenSesame:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy para el backend (por defecto) psycho. Dependiendo de tu sistema operativo y versión de Python, puede que PsychoPy no se instale correctamente. Si esto sucede, busca ayuda en el foro de soporte o usa uno de los paquetes instaladores ya hechos.

```bash
pip install psychopy psychopy_sounddevice psychopy_visionscience 
```

PyGaze para seguimiento ocular:

```bash
pip install https://github.com/smathot/PyGaze/releases/download/prerelease%2F0.8.0a3/python_pygaze-0.8.0a3-py3-none-any.whl
```

Expyriment para el backend xpyriment

```bash
pip install http://files.cogsci.nl/expyriment-0.10.0+opensesame2-py3-none-any.whl 
```

Una vez instalados todos los paquetes, simplemente puedes ejecutar OpenSesame con:

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

Luego, sigue las instrucciones de instalación de PyPi indicadas arriba. Ya no se proveen paquetes Anaconda dedicados.


### Versiones antiguas

Las versiones anteriores pueden descargarse desde los lanzamientos de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

Actualmente, OpenSesame se construye y prueba con Python 3.13. Otras versiones de Python >=3.10 funcionan pero no han sido probadas exhaustivamente. Python 2 ya no es compatible. La última versión que incluyó un paquete para Python 2 fue la 3.3.12, que aún puede descargarse desde el [archivo de versiones](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la última versión de OpenSesame.
- No actualices mientras estás ejecutando un experimento; es decir, no actualices mientras estás recogiendo datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollar y probar.


### Actualizar paquetes manualmente

OpenSesame es un entorno Python normal, y puedes ejecutar comandos `pip install` en la consola de Jupyter.


### Consejos para administradores de sistemas

- Cuando se publica una nueva versión mayor de OpenSesame (con un número de versión terminado en 0, por ejemplo 3.1.0), generalmente le siguen rápidamente una o dos versiones de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que corrigen errores importantes. Por lo tanto, si vas a instalar OpenSesame en sistemas que no se actualizan frecuentemente, lo mejor es esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De este modo, minimizarás el riesgo de desplegar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows te permite instalar OpenSesame de forma silenciosa utilizando la bandera `/S`.