title: Descargar
hash: 4c609d80d00e5704f1e59d0daf4820641810168b01ec87f556a20c226969d520
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

La última versión $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Instalador estándar</b> para Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows estándar</b> sin instalación requerida (.zip)
</a>

La mayoría de las personas descarga el paquete instalador `.exe`. Si no tienes privilegios de administrador, o si necesitas ejecutar múltiples versiones de OpenSesame en paralelo, descarga el paquete `.zip` en su lugar.

Basado en Python 3.13 para sistemas de 64 bits. Probado en Windows 11.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquete para Mac OS (.dmg)
</a>

Cuando inicies OpenSesame por primera vez, el sistema operativo lo bloqueará porque la app no proviene de un desarrollador de confianza. Encontrarás la opción 'Abrir de todas formas' en Ajustes > Privacidad y seguridad. Esta opción aparece después de que la app es bloqueada.

Basado en Python 3.13 para sistemas intel de 64 bits. Probado en Mac OS X Sequoia.


### Linux / Ubuntu

Copia y pega la línea de abajo en una terminal. Esto descargará y ejecutará un script de instalación. El script requiere curl y virtualenv. En Ubuntu pueden instalarse con `sudo apt install curl python3-venv`.

```bash
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

PsychoPy para el backend (predeterminado) psycho. Dependiendo de tu sistema operativo y versión de Python, puede que PsychoPy no se instale correctamente. Si esto ocurre, solicita ayuda en el foro de soporte o usa uno de los paquetes/instaladores preparados.

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

Una vez instalados todos los paquetes, puedes ejecutar OpenSesame simplemente ejecutando:

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

Luego, sigue las instrucciones de instalación de PyPi anteriores. Ya no se ofrecen paquetes dedicados para Anaconda.


### Versiones anteriores

Las versiones anteriores pueden descargarse desde los lanzamientos de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

Actualmente, OpenSesame se construye y prueba con Python 3.13. Otras versiones de Python >=3.10 funcionan, pero no se prueban exhaustivamente. Python 2 ya no es compatible. La última versión que incluía un paquete para Python 2 fue la 3.3.12, que aún se puede descargar desde el [archivo de versiones](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor usar la versión más reciente de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estás recolectando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollar y probar.


### Actualización manual de paquetes

OpenSesame es un entorno Python regular, y puedes ejecutar comandos `pip install` en la consola de Jupyter.


### Consejos para administradores de sistemas

- Cuando se lanza una nueva versión mayor de OpenSesame (con un número de versión terminado en 0, por ejemplo 3.1.0), generalmente es seguida rápidamente por una o dos versiones de mantenimiento (por ejemplo 3.1.1 y 3.1.2) que corrigen errores importantes. Por lo tanto, si estás instalando OpenSesame en sistemas que no sueles actualizar con frecuencia, es mejor esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo 3.0.2, 3.1.3, etc.). Así minimizas el riesgo de implementar una versión de OpenSesame con errores importantes.
- El instalador de Windows permite instalar OpenSesame de forma silenciosa usando la bandera `/S`.