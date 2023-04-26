title: Laufzeit für Android
hash: 136526a89cab3d65e4d472dd3bc53e6fa2aa96bee7e901397e246e2ceed57ed6
locale: de
language: German

__Wichtiger Hinweis:__ Die OpenSesame-Laufzeitumgebung für Android basiert auf Software von Dritten, die nicht mehr weiterentwickelt wird. Daher können wir nicht garantieren, dass die Laufzeitumgebung auf neueren Versionen von Android funktioniert. Windows 10-Tablets mit Intel-Prozessoren sind eine gute Alternative.
{: .alert .alert-warning}

[TOC]

## OpenSesame-Laufzeitumgebung für Android

### Download

Sie können die OpenSesame-Laufzeitumgebung für Android über den Google Play Store herunterladen:

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Holen Sie es bei Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

### Nutzung

Wenn Sie die OpenSesame-Laufzeitumgebung starten, werden Sie gefragt, wo Ihre Experimente gespeichert sind. Standardmäßig geht OpenSesame davon aus, dass sie sich im Ordner `/sdcard/` oder (falls vorhanden) im Ordner `/sdcard/Experiments/` befinden. Wenn Sie keine Experimente auf Ihrem Gerät haben, zeigt das Drücken der `Enter`-Taste die Beispiel-Experimente, die mit der `.apk`-Datei gebündelt sind.

Die `Zurück`-Taste hat die gleiche Funktion wie die `Escape`-Taste auf herkömmlichen Systemen und beendet OpenSesame.

### Unterstützte Geräte

OpenSesame wird mit Nexus 4 und 9 als Referenzgeräte entwickelt. Im Allgemeinen scheint jedes Gerät, das Android 2.2. "Froyo" oder später ausführt, zu funktionieren.

### Automatische Updates deaktivieren

Wenn Sie die OpenSesame-Laufzeitumgebung für Android in einer Produktionsumgebung verwenden (z.B. während Sie ein Experiment durchführen), wird empfohlen, die Auto-Update-Funktion des Google Play Store zumindest für OpenSesame zu deaktivieren. Dies verhindert, dass die App aktualisiert wird und sich ihr Verhalten möglicherweise ändert. Falls Sie auf eine frühere Version der Android-Laufzeitumgebung zurückkehren müssen, finden Sie die `.apk`-Dateien früherer Versionen [hier](https://github.com/smathot/OpenSesame/releases).

### Automatisches Starten eines Experiments

Wenn Sie ein bestimmtes Experiment direkt beim Start der OpenSesame-Laufzeitumgebung für Android ausführen möchten, können Sie eine Datei namens `opensesame-autorun.yml` im `/sdcard/`-Ordner Ihres Geräts erstellen. Dies ist eine YAML-Datei mit der folgenden Struktur:

~~~
experiment: /sdcard/experiments/my_experiment.opensesame
subject_nr: 3
logfile: /sdcard/data/subject03.csv
~~~

## Experimente für Android entwickeln

### Backend

Die OpenSesame-Laufzeitumgebung für Android erfordert das *droid* Backend.

### Designtipps

Implementieren Sie die meisten Benutzerinteraktionen über das MOUSE_RESPONSE-Element oder das TOUCH_RESPONSE-Plugin. Im Allgemeinen werden Bildschirmberührungen als Mausklicks registriert. Die Verwendung von Tastatureingaben funktioniert ebenfalls, aber die virtuelle Tastatur wird nach jeder eingegebenen Taste ein- und ausgeblendet, was unordentlich aussieht.

Die Auflösung für das DROID-Backend ist auf 1280x800 (Landschaft) festgelegt. Auf Android wird Ihr Experiment automatisch abhängig von der Auflösung des Geräts skaliert, aber die Auflösung, mit der Sie arbeiten, beträgt immer 1280x800.

### Debugging

Debug-Ausgaben werden in `/sdcard/opensesame-debug.txt` geschrieben.

### Einschränkungen

- Das SYNTH-Element und das `openexp.synth` Modul sind nicht funktionsfähig.
- Das SAMPLER-Element und das `openexp.sampler` Modul ignorieren Panning und Pitching.

## Bekanntes Problem: Eingefrorene oder fehlerhafte virtuelle Tastatur

Auf einigen Geräten ist die standardmäßige virtuelle Tastatur nicht ansprechbar (d.h. sie wird angezeigt, reagiert aber nicht auf Berührungen) oder funktioniert nicht wie gewohnt. Dies scheint auf Telefonen mit neueren Versionen von Android zu geschehen. Um dieses Problem zu umgehen, können Sie eine Tastatur von Drittanbietern installieren. Tastaturen, von denen bekannt ist, dass sie funktionieren, sind:

- [GO Keyboard](https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard&hl=de)
- [Smart Keyboard Trial](https://play.google.com/store/apps/details?id=net.cdeguet.smartkeyboardtrial&hl=de)

## Verfügbare Python-Module

Im Folgenden finden Sie eine Liste der Python-Module, die in der OpenSesame-Laufzeitumgebung für Android verfügbar sein sollten. (Diese Liste wurde von der inzwischen nicht mehr existierenden pgs4a-Website kopiert.)

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
Kalender
cmath
codecs
collections
compileall
contextlib
Kopie
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
zufällig
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