title: Durée d'exécution pour Android
hash: 136526a89cab3d65e4d472dd3bc53e6fa2aa96bee7e901397e246e2ceed57ed6
locale: fr
language: French

__Note importante :__ Le temps d'exécution d'OpenSesame pour Android est basé sur des logiciels développés par d'autres qui ne sont plus en développement. En conséquence, nous ne pouvons pas garantir que le temps d'exécution fonctionne avec les versions récentes d'Android. Les tablettes Windows 10 avec processeurs Intel sont une bonne alternative.
{: .alert .alert-warning}

[TOC]

## Temps d'exécution d'OpenSesame pour Android

### Téléchargement

Vous pouvez télécharger le temps d'exécution d'OpenSesame pour Android via le Google Play Store :

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Get it on Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

### Utilisation

Lorsque vous démarrez le temps d'exécution d'OpenSesame, on vous demandera où se trouvent vos expériences. Par défaut, OpenSesame suppose qu'elles se trouvent dans le dossier `/sdcard/` ou (s'il existe) dans le dossier `/sdcard/Experiments/`. Si vous n'avez pas d'expériences sur votre appareil, appuyer sur `entrée` affichera les expériences exemples incluses dans le fichier `.apk`.

Le bouton `Retour` sert de touche `Échap` sur les systèmes classiques et permet de quitter OpenSesame.

### Appareils pris en charge

OpenSesame est développé avec les Nexus 4 et 9 comme appareils de référence. En général, tout appareil fonctionnant avec Android 2.2 "Froyo" ou ultérieur semble fonctionner.

### Désactivation des mises à jour automatiques

Si vous utilisez le temps d'exécution d'OpenSesame pour Android dans un environnement de production (par exemple, pendant que vous réalisez une expérience), il est recommandé de désactiver la fonction de mise à jour automatique du Google Play Store, au moins pour OpenSesame. Cela évitera que l'application soit mise à jour et change potentiellement son comportement. Si vous avez besoin de revenir à une version précédente du temps d'exécution Android, vous pouvez trouver les fichiers `.apk` des versions précédentes [ici](https://github.com/smathot/OpenSesame/releases).

### Démarrage automatique d'une expérience

Si vous souhaitez lancer directement une expérience spécifique au démarrage du temps d'exécution d'OpenSesame pour Android, vous pouvez créer un fichier appelé `opensesame-autorun.yml` dans le dossier `/sdcard/` de votre appareil. Il s'agit d'un fichier YAML avec la structure suivante :

~~~
experiment: /sdcard/experiments/my_experiment.opensesame
subject_nr: 3
logfile: /sdcard/data/subject03.csv
~~~

## Développement d'expériences pour Android

### Backend

Le temps d'exécution d'OpenSesame pour Android nécessite le backend *droid*.

### Conseils de conception

Mettez en œuvre la plupart des interactions utilisateur grâce à l'élément MOUSE_RESPONSE ou au plugin TOUCH_RESPONSE. En général, les actions sur l'écran sont enregistrées comme des clics de souris. L'utilisation de l'entrée au clavier fonctionnera également, mais cela affichera et masquera le clavier virtuel après chaque touche saisie, ce qui semble désordonné.

La résolution pour le backend DROID est fixée à 1280x800 (paysage). Sur Android, votre expérience sera automatiquement mise à l'échelle en fonction de la résolution de l'appareil, mais la résolution que vous concevez est toujours de 1280x800.

### Débogage

La sortie de débogage est écrite dans `/sdcard/opensesame-debug.txt`.

### Limitations

- L'élément SYNTH et le module `openexp.synth` ne sont pas fonctionnels.
- L'élément SAMPLER et le module `openexp.sampler` ignoreront les panoramiques et les hauteurs.

## Problème connu : Clavier virtuel gelé ou défaillant

Sur certains appareils, le clavier virtuel par défaut ne répond pas (c'est-à-dire qu'il s'affiche mais ne répond pas aux appuis) ou ne répond pas normalement. Cela semble se produire sur les téléphones avec des versions récentes d'Android. Pour contourner ce problème, vous pouvez installer un clavier tiers. Les claviers qui ont été signalés comme fonctionnant sont :

- [GO Keyboard](https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard&hl=fr)
- [Smart Keyboard Trial](https://play.google.com/store/apps/details?id=net.cdeguet.smartkeyboardtrial&hl=fr)

## Modules Python disponibles

Voici une liste des modules Python qui devraient être disponibles dans le temps d'exécution d'OpenSesame pour Android. (Cette liste est copiée depuis le site Web maintenant obsolète de pgs4a.)

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
calendrier
cmath
codecs
collections
compileall
contextlib
copie
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
mot-clé
linecache
math
md5
mimetools
opcode
optparse
os
opérateur
parser
pickle
plate-forme
posix
posixpath
pprint
py_compile
pwd
Queue
aléatoire
repr
re
rfc822
sélectionner
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
chaîne
struct
subprocess
symbole
symtable
strop
tarfile
tempfile
textwrap
_threading_local
threading
temps
tokenize
token
traceback
types
urllib
urllib2
urlparse
UserDict
avertissements
weakref
navigateur Web
zipfile
zipimport
zlib
~~~

[google-play]: https://play.google.com/store/apps/details?id=nl.cogsci.opensesame
[forum]: http://forum.cogsci.nl/index.php?p=/discussion/333/a-video-of-opensesame-running-natively-on-android
[droid]: /backends/droid
[pgs4a]: http://pygame.renpy.org/