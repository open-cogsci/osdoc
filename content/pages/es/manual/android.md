title: Tiempo de ejecución para Android
hash: 136526a89cab3d65e4d472dd3bc53e6fa2aa96bee7e901397e246e2ceed57ed6
locale: es
language: Spanish

__Nota importante:__ El tiempo de ejecución de OpenSesame para Android se basa en software de terceros que ya no se desarrolla. Como resultado, no podemos asegurar que el tiempo de ejecución funcione con versiones recientes de Android. Las tabletas con Windows 10 y procesadores Intel son una buena alternativa.
{: .alert .alert-warning}

[TOC]

## Tiempo de ejecución de OpenSesame para Android

### Descarga

Puedes descargar el tiempo de ejecución de OpenSesame para Android a través de Google Play Store:

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Consíguelo en Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

### Uso

Cuando inicies el tiempo de ejecución de OpenSesame, se te preguntará dónde se encuentran tus experimentos. Por defecto, OpenSesame asume que están en la carpeta `/sdcard/` o (si existe) en la carpeta `/sdcard/Experiments/`. Si no tienes experimentos en tu dispositivo, presionar `enter` mostrará los experimentos de ejemplo incluidos con el archivo `.apk`.

El botón `Atrás` tiene el mismo propósito que la tecla `Escape` en sistemas regulares y saldrá de OpenSesame.

### Dispositivos compatibles

OpenSesame se desarrolla con Nexus 4 y 9 como dispositivos de referencia. En general, parece funcionar cualquier dispositivo que ejecute Android 2.2. 'Froyo' o posterior.

### Desactivar actualizaciones automáticas

Si estás utilizando el tiempo de ejecución de OpenSesame para Android en un entorno de producción (por ejemplo, mientras ejecutas un experimento), se recomienda desactivar la función de actualización automática de Google Play Store, al menos para OpenSesame. Esto evitará que la aplicación se actualice y cambie potencialmente su comportamiento. En caso de que necesites volver a una versión anterior del tiempo de ejecución de Android, puedes encontrar los archivos `.apk` para versiones anteriores [aquí](https://github.com/smathot/OpenSesame/releases).

### Iniciar automáticamente un experimento

Si deseas lanzar directamente un experimento específico al iniciar el tiempo de ejecución de OpenSesame en Android, puedes crear un archivo llamado `opensesame-autorun.yml` en la carpeta `/sdcard/` de tu dispositivo. Este es un archivo YAML con la siguiente estructura:

~~~
experiment: /sdcard/experiments/my_experiment.opensesame
subject_nr: 3
logfile: /sdcard/data/subject03.csv
~~~

## Desarrollar experimentos para Android

### backend

El tiempo de ejecución de OpenSesame para Android requiere el backend *droid*.

### Consejos de diseño

Implementa la mayoría de las interacciones del usuario mediante el elemento MOUSE_RESPONSE o el complemento TOUCH_RESPONSE. En general, los toques de pantalla se registran como clics del mouse. El uso de la entrada del teclado también funcionará, pero mostrará y ocultará el teclado virtual después de cada tecla que se ingrese, lo que se ve desordenado.

La resolución para el backend DROID está fijada en 1280x800 (horizontal). En Android, tu experimento se escalará automáticamente hacia arriba o hacia abajo según la resolución del dispositivo, pero la resolución con la que trabajas es siempre de 1280x800.

### Depuración

La salida de depuración se escribe en `/sdcard/opensesame-debug.txt`.

### Limitaciones

- El ítem SYNTH y el módulo `openexp.synth` no son funcionales.
- El ítem SAMPLER y el módulo `openexp.sampler` ignorarán el panoramizado y el ajuste de tono.

## Problema conocido: Teclado virtual congelado o con mal funcionamiento

En algunos dispositivos, el teclado virtual predeterminado no responde (es decir, se muestra pero no responde a los toques) o no responde normalmente. Esto parece ocurrir en teléfonos con versiones recientes de Android. Para solucionar este problema, puedes instalar un teclado de terceros. Los teclados que se ha informado que funcionan son:

- [GO Keyboard](https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard&hl=es)
- [Smart Keyboard Trial](https://play.google.com/store/apps/details?id=net.cdeguet.smartkeyboardtrial&hl=es)

## Módulos Python disponibles

A continuación, se muestra una lista de módulos de Python que deben estar disponibles en el tiempo de ejecución de OpenSesame para Android. (Esta lista se copia del sitio web ya descontinuado de pgs4a.)

~~~
pygame
pygame.base
pygame.bufferproxy
pygame.colordict
pygame.color
pygame.compat
pygame.constants
pygame.cursors
pygame.display
pygame.draw
pygame.event
pygame.fastevent
pygame.font
pygame.gfxdraw
pygame.imageext
pygame.image
pygame.joystick
pygame.key
pygame.locals
pygame.mask
pygame.mouse
pygame.overlay
pygame.rect
pygame.rwobject
pygame.sprite
pygame.surface
pygame.surflock
pygame.sysfont
pygame.time
pygame.transform
pygame.version
_abcoll
abc
aliases
array
ast
atexit
base64
bisect
binascii
calendar
cmath
codecs
collections
compileall
contextlib
copy
copy_reg
cStringIO
cPickle
datetime
difflib
dis
dummy_threading
dummy_thread
encodings
encodings.raw_unicode_escape
encodings.utf_8
encodings.zlib_codec
errno
fcntl
fnmatch
functools
__future__
genericpath
getopt
glob
gzip
hashlib
heapq
httplib
inspect
itertools
keyword
linecache
math
md5
mimetools
opcode
optparse
os
operator
parser
pickle
platform
posix
posixpath
pprint
py_compile
pwd
Queue
random
repr
re
rfc822
select
sets
shlex
shutil
site
socket
sre_compile
sre_constants
sre_parse
ssl
stat
StringIO
string
struct
subprocess
symbol
symtable
strop
tarfile
tempfile
textwrap
_threading_local
threading
time
tokenize
token
traceback
types
urllib
urllib2
urlparse
UserDict
warnings
weakref
webbrowser
zipfile
zipimport
zlib
~~~

[google-play]: https://play.google.com/store/apps/details?id=nl.cogsci.opensesame
[forum]: http://forum.cogsci.nl/index.php?p=/discussion/333/a-video-of-opensesame-running-natively-on-android
[droid]: /backends/droid
[pgs4a]: http://pygame.renpy.org/