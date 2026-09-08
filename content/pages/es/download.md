title: Descargar
hash: 43af7638374babac965b68a0a316b0487bd9a9f780ffb4e0674e0c7e015f026e
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

<h3>¡Tu descarga debería iniciarse en breve!</h3>

<a role="button" class="btn btn-success btn-align-left" href="https://sigmundai.eu">
 &#128150; Suscríbete a SigmundAI.eu
</a>

Tu copiloto de IA para OpenSesame. Tu suscripción de 9 €/mes apoya a OpenSesame.

Haz clic <a id="click-here">aquí</a> si tu descarga no se inicia.
</div>


## Resumen

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
	<b>Estándar</b> Instalador de Windows (.exe)
</a>

<a role="button" class="btn btn-default btn-align-left" onclick="startDownload('$url-windows-zip-py3$')">
	<b>Estándar</b> Windows sin necesidad de instalación (.zip)
</a>

La mayoría de las personas descarga el paquete instalador `.exe`. Si no tienes privilegios de administrador o si necesitas ejecutar varias versiones de OpenSesame en paralelo, descarga el paquete `.zip`.

Basado en Python 3.13 para sistemas de 64 bits. Probado en Windows 11.

Algunos dispositivos externos, como los rastreadores oculares [Tobii](%url:tobii%), requieren una versión diferente de Python. Visita las páginas de documentación correspondientes para obtener más información.


### Mac OS

<a role="button" class="btn btn-success btn-align-left" onclick="startDownload('$url-osx-dmg-x64-py3$')">
	Paquete para Mac OS (.dmg)
</a>

Cuando inicias OpenSesame por primera vez, el sistema operativo lo bloquea porque la aplicación no procede de un desarrollador de confianza. Encontrarás la opción «Abrir de todos modos» en Configuración > Privacidad y seguridad. Esta opción aparece después de que se bloquee la aplicación.

Basado en Python 3.13 para sistemas intel de 64 bits. Probado en Mac OS X Sequoia.

Algunos dispositivos externos, como los rastreadores oculares [Tobii](%url:tobii%), requieren una versión diferente de Python. Visita las páginas de documentación correspondientes para obtener más información.


### Linux / Ubuntu

Copia y pega las líneas siguientes en una terminal. Esto descargará y ejecutará un script de instalación.

```bash
# These packages need to be installed on Ubuntu 24.04.
# Equivalent packages need to be installed on other
# Linux distributions.
sudo apt install curl python3-dev python3-venv libxcb-cursor0
# Download and run the OpenSesame installation script.
bash <(curl -L https://github.com/open-cogsci/OpenSesame/raw/refs/heads/nightingale/linux-installer.sh) --install
```

Probado en Ubuntu 24.04 (Python 3.12).


## Opciones avanzadas de instalación


### PyPi (multiplataforma)

Todos los paquetes se pueden instalar con pip. Ten en cuenta que OpenSesame se llama `opensesame-core` en PyPi.

Dependencias principales de OpenSesame:

```bash
pip install --pre opensesame-core opensesame-extension-sigmund opensesame-extension-osweb opensesame-extension-updater opensesame-plugin-psychopy opensesame-plugin-media_player_mpy pygame
```

PsychoPy para el backend psycho (predeterminado). Dependiendo de tu sistema operativo y versión de Python, es posible que PsychoPy no se instale correctamente. Si esto ocurre, busca ayuda en el foro de soporte o utiliza uno de los paquetes/instaladores prediseñados.

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

Una vez que hayas instalado todos los paquetes, puedes ejecutar OpenSesame simplemente ejecutando:

```bash
opensesame
```

O para Sigmund Analyst (editor de código):

```bash
sigmund-analyst
```


### Anaconda (multiplataforma)

Primero, cree un nuevo entorno de Python para OpenSesame (opcional)

```bash
conda create -n opensesame-41 python=3.13
conda activate opensesame-41
```

A continuación, siga las instrucciones de instalación de PyPi anteriores. Ya no se proporcionan paquetes dedicados de Anaconda.


### Versiones anteriores de OpenSesame y otras versiones de Python

Las versiones anteriores de OpenSesame, así como los paquetes compilados con diferentes versiones de Python (3.10, 3.11 y 3.12), están disponibles en las publicaciones de GitHub:

- <https://github.com/open-cogsci/OpenSesame/releases>



### Código fuente

El código fuente de OpenSesame está disponible en [GitHub](https://github.com/open-cogsci/OpenSesame).


## Consejos


### ¿Qué versión de Python usar?

OpenSesame se compila y prueba actualmente con Python 3.13. Otras versiones de Python >=3.10 funcionan, pero no se prueban exhaustivamente. Python 2 ya no es compatible. La última versión que incluía un paquete de Python 2 fue la 3.3.12, que todavía puede descargarse del [archivo de versiones](https://github.com/open-cogsci/OpenSesame/releases/tag/release%2F3.3.12).


### ¿Cuándo (no) actualizar?

- Actualice mientras desarrolla y prueba su experimento; siempre es mejor utilizar la versión más reciente de OpenSesame.
- No actualice mientras ejecuta un experimento; es decir, no actualice mientras recopila datos.
- Ejecute un experimento con la misma versión de OpenSesame que utilizó para desarrollarlo y probarlo.


### Actualización manual de paquetes

OpenSesame es un entorno de Python normal, y puede ejecutar comandos `pip install` en la consola de Jupyter.


### Consejos para administradores de sistemas

- Cuando se publica una nueva versión principal de OpenSesame (con una versión que termina en 0, por ejemplo, 3.1.0), generalmente le siguen rápidamente una o dos versiones de mantenimiento (por ejemplo, 3.1.1 y 3.1.2) que corrigen errores importantes. Por lo tanto, si está instalando OpenSesame en sistemas que no actualiza con frecuencia, es mejor esperar hasta la segunda o tercera versión de mantenimiento (por ejemplo, 3.0.2, 3.1.3, etc.). De este modo, minimiza el riesgo de implementar una versión de OpenSesame que contenga errores importantes.
- El instalador de Windows permite instalar OpenSesame de forma silenciosa utilizando la opción `/S`.