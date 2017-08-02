title: Runtime for Android


__Important note:__ The OpenSesame runtime for Android is based on software by others that is no longer developed. As a result, we are unable to make sure that the runtime works with recent versions of Android. Windows 10 tablets with Intel processors are a good alternative.
{: .alert .alert-warning}


[TOC]


## OpenSesame runtime for Android

### Download

You can download the OpenSesame runtime for Android through the Google Play Store:

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Get it on Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

### Usage

When you start the OpenSesame runtime, you will be asked where your experiments are located. By default, OpenSesame assumes that they are in the `/sdcard/` folder, or (if it exists) in the `/sdcard/Experiments/` folder. If you have no experiments on your device, pressing `enter` will show the example experiments that are bundled with the `.apk`.

The `Back` button serves the same purpose as the `Escape` key on regular systems, and will exit OpenSesame.

### Supported devices

OpenSesame is developed with the Nexus 4 and 9 as reference devices. In general, any device that runs Android 2.2. 'Froyo' or later appears to work.

### Disabling automatic updates

If you are using the OpenSesame runtime for Android in a production environment (e.g., while you are running an experiment), it is recommended to disable the Auto-update feature of the Google Play Store, at least for OpenSesame. This will prevent the app from being updated and potentially changing its behavior. In case you need to downgrade to a previous version of the Android runtime, you can find the `.apk` files for previous releases [here](https://github.com/smathot/OpenSesame/releases).

### Automatically start an experiment

If you want to directly launch a specific experiment when the OpenSesame runtime for Android is started, you can create a file called `opensesame-autorun.yml` in the `/sdcard/` folder of your device. This is a YAML file with the following structure:

~~~
experiment: /sdcard/experiments/my_experiment.opensesame
subject_nr: 3
logfile: /sdcard/data/subject03.csv
~~~

## Developing experiments for Android

### backend

The OpenSesame runtime for Android requires the *droid* backend.

### Design tips

Implement most user interactions through the MOUSE_RESPONSE item or TOUCH_RESPONSE plugin. In general, screen touches are registered as mouse clicks. Using keyboard input will work as well, but it will show and hide the virtual keyboard after every key that is entered, which looks messy.

The resolution for the DROID backend is fixed at 1280x800 (landscape). On Android, your experiment will be automatically scaled up or down depending on the resolution of the device, but the resolution that you design with is always 1280x800.

### Debugging

Debug output is written to `/sdcard/opensesame-debug.txt`.

### Limitations

- The SYNTH item and `openexp.synth` module are not functional.
- The SAMPLER item and `openexp.sampler` module will ignore panning and pitching.

## Know issue: Frozen or misbehaving virtual keyboard

On some devices, the default virtual keyboard is unresponsive (i.e. it shows but doesn't respond to taps) or doesn't respond normally. This appears to happen on phones with recent versions of Android. To work around this issue, you can install a third-party keyboard. Keyboards that have been reported to work are:

- [GO Keyboard](https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard&hl=en)
- [Smart Keyboard Trial](https://play.google.com/store/apps/details?id=net.cdeguet.smartkeyboardtrial&hl=en)

## Available Python modules

Below is a list of Python modules that should be available in the OpenSesame runtime for android. (This list is copied from the pgs4a now-defunct website.)

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
