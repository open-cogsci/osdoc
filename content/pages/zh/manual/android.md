title: Android 运行时
hash: 136526a89cab3d65e4d472dd3bc53e6fa2aa96bee7e901397e246e2ceed57ed6
locale: zh
language: Chinese

__重要提示：__ OpenSesame的安卓运行时基于他人开发的不再维护的软件。因此，我们无法确保运行时能够与最新版本的安卓系统兼容。搭载英特尔处理器的Windows 10平板电脑是个不错的替代方案。
{: .alert .alert-warning}

[TOC]

## OpenSesame安卓运行时

### 下载

您可以通过谷歌商店下载OpenSesame的安卓运行时：

<a href="https://play.google.com/store/apps/details?id=nl.cogsci.opensesame" style="border:none;">
  <img alt="Get it on Google Play"
       src="https://developer.android.com/images/brand/en_generic_rgb_wo_45.png" />
</a>

### 使用方法

启动OpenSesame运行时时，系统会询问您的实验文件位置。默认情况下，OpenSesame认为它们位于`/sdcard/`文件夹或（如果存在）`/sdcard/Experiments/`文件夹中。如果您的设备上没有实验文件，在按下“enter”时会显示与`.apk`捆绑的示例实验。

“返回”按钮的功能与常规系统上的“Escape”键相同，用于退出OpenSesame。

### 支持的设备

OpenSesame以Nexus 4和9为参考设备进行开发。通常情况下，任何运行安卓2.2. “Froyo”或更高版本的设备均可使用。

### 禁用自动更新

如果您在生产环境中使用OpenSesame安卓运行时（例如，运行实验时），建议至少为OpenSesame禁用谷歌商店的自动更新功能。这可以防止应用更新导致潜在的行为更改。如果您需要降级到旧版本的安卓运行时，可以在此处找到用于以前发布版本的`.apk`文件[此处](https://github.com/smathot/OpenSesame/releases)。

### 自动启动实验

如果您希望在启动OpenSesame安卓运行时时直接启动特定实验，可以在设备的`/sdcard/`文件夹中创建名为`opensesame-autorun.yml`的文件。这是一个YAML文件，其结构如下：

~~~
experiment: /sdcard/experiments/my_experiment.opensesame
subject_nr: 3
logfile: /sdcard/data/subject03.csv
~~~

## 为安卓开发实验

### 后端

OpenSesame安卓运行时需要*droid*后端。

### 设计提示

通过MOUSE_RESPONSE项目或TOUCH_RESPONSE插件实现大多数用户交互。通常情况下，屏幕触摸会被注册为鼠标点击。使用键盘输入也可以工作，但每输入一个键，虚拟键盘会显示和隐藏一次，这看起来很混乱。

DROID后端的分辨率固定为1280x800（横屏）。在安卓上，您的实验会根据设备的分辨率自动进行缩放，但您设计时的分辨率始终为1280x800。

### 调试

调试输出将写入`/sdcard/opensesame-debug.txt`。

### 限制

- SYNTH项目和`openexp.synth`模块不起作用。
- SAMPLER项目和`openexp.sampler`模块会忽略声像和音高。

## 已知问题：虚拟键盘冻结或行为异常

在某些设备上，默认的虚拟键盘无响应（即显示但不响应敲击）或响应不正常。这似乎发生在安卓版本较新的手机上。为解决此问题，您可以安装第三方键盘。已知能用的键盘包括：

- [GO键盘](https://play.google.com/store/apps/details?id=com.jb.emoji.gokeyboard&hl=en)
- [智能键盘试用版](https://play.google.com/store/apps/details?id=net.cdeguet.smartkeyboardtrial&hl=en)

## 可用的Python模块

以下是安卓OpenSesame运行时中应可用的Python模块列表。（此列表已从pgs4a现已停用的网站上复制。）

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
[forum]: http://forum.cogsci.nl/index.php?p=/discussion/333/一个关于在安卓手机原生运行开放芝麻程序的视频
[droid]: /backends/droid
[pgs4a]: http://pygame.renpy.org/