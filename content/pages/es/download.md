title: Descargar
hash: 70d7d3aa0db9c3d49b6e9a94cd6d92a1dd50ec0dc94bc9bfc9e076703ab3dd3a
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

Mejor que ChatGPT para preguntas sobre OpenSesame. Tu suscripción de 9 €/mes apoya el desarrollo de OpenSesame.

Haz clic <a id="click-here">aquí</a> si la descarga no inicia.

</div>


## Descripción general

%--
toc:
 exclude: [Overview]
 mindepth: 2
 maxdepth: 3
--%


## Todas las opciones de descarga

La versión más reciente $status$ es $version$ *$codename$* ([notas de la versión](http://osdoc.cogsci.nl/$branch$/notes/$notes$)).


### Windows

El paquete para Windows está basado en Python 3.13 para sistemas de 64 bits. El instalador y los paquetes `.zip` son idénticos, excepto por el método de instalación. La mayoría de las personas descarga el paquete instalador (botón verde).

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-windows-exe-py3$')">
	<b>Instalador estándar</b> de Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Windows estándar</b> sin necesidad de instalación (.zip)
</a>


### Mac OS

Los paquetes para Mac OS aún no están disponibles para OpenSesame 4.1. El enlace de descarga a continuación todavía apunta a la versión 4.0.
{.page-notification}

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquete para Mac OS (.dmg)
</a>


### Linux / Ubuntu

Copia y pega la línea siguiente en una terminal. Esto descargará y ejecutará un script de instalación. El script requiere virtualenv, que en Ubuntu puede instalarse con `sudo apt install python3-venv`.

```bash
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/4.1/linux-installer.sh) --install
```

OpenSesame se desarrolla y prueba en Ubuntu 24.04. La compatibilidad puede variar en otras distribuciones de Linux y otras versiones de Ubuntu.


### PyPi (multiplataforma)

Todos los paquetes pueden instalarse con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

Dependencias principales de OpenSesame:

```bash
# Dependencias principales de OpenSesame
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy para el backend (por defecto) psycho. Dependiendo de tu sistema operativo y versión de Python, puede que PsychoPy no se instale correctamente. Si esto sucede, busca ayuda en el foro de soporte o utiliza uno de los paquetes/preinstaladores disponibles.

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

Una vez que hayas instalado todos los paquetes, puedes ejecutar OpenSesame simplemente usando:

```bash
opensesame
```

O para Sigmund Analyst (editor de código):

```bash
sigmund-analyst
```


### Anaconda (multiplataforma)

Primero, crea un nuevo entorno de Python para OpenSesame (opcional):

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

A continuación, sigue las instrucciones de instalación de PyPi anteriores. Ya no se proporcionan paquetes dedicados para Anaconda.


### Versiones antiguas

Las versiones antiguas se pueden descargar desde GitHub releases:

- <https://github.com/open-cogsci/OpenSesame/releases>


### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame se construye y prueba actualmente con Python 3.13. Otras versiones de Python >=3.10 funcionan pero no han sido probadas exhaustivamente. Python 2 ya no es compatible. La última versión que incluyó un paquete para Python 2 fue la 3.3.12, que todavía se puede descargar desde el [archivo de lanzamientos](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualiza mientras desarrollas y pruebas tu experimento; siempre es mejor utilizar la versión más reciente de OpenSesame.
- No actualices mientras ejecutas un experimento; es decir, no actualices mientras estés recolectando datos.
- Ejecuta un experimento con la misma versión de OpenSesame que usaste para desarrollarlo y probarlo.


### Actualización manual de paquetes

OpenSesame es un entorno de Python estándar y puedes ejecutar comandos `pip install` en la consola de Jupyter.


### Consejos para administradores de sistemas

- Cuando se lanza una nueva versión principal de OpenSesame (con un número de versión terminado en 0, por ejemplo 3.1.0), generalmente le siguen una o dos versiones de mantenimiento (por ejemplo 3.1.1 y 3.1.2) que corrigen errores importantes. Por lo tanto, si vas a instalar OpenSesame en sistemas que no actualizas con frecuencia, lo mejor es esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo 3.0.2, 3.1.3, etc.). Así minimizas el riesgo de instalar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows te permite instalar OpenSesame de manera silenciosa usando el indicador `/S`.