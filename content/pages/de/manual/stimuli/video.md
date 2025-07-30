title: Videowiedergabe
hash: 135ac06d95735a29df2450dc840b4ab283182095a768134d3d35e7c85f031901
locale: de
language: German

[TOC]


## media_player_mpy-Plugin

Das [MEDIA_PLAYER_MPY](https://github.com/open-cogsci/opensesame-plugin-mediaplayer)-Plugin basiert auf MoviePy. Es ist standardmäßig in OpenSesame enthalten. (Wenn du eine eigene Umgebung verwendest, kannst du es durch Installation des `opensesame-plugin-media_player_mpy`-Pakets erhalten.)


## OpenCV

OpenCV ist eine leistungsstarke Computer-Vision-Bibliothek, die (unter anderem) Routinen zum Lesen von Videodateien enthält.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

Das folgende Beispiel zeigt, wie man eine Videodatei abspielt und dabei ein rotes Quadrat über das Video zeichnet. Dieses Beispiel geht davon aus, dass du das Legacy-Backend verwendest.

```python
import cv2
import numpy
import pygame
# Vollständiger Pfad zur Videodatei im Dateipool
path = pool['myvideo.avi']
# Video öffnen
video = cv2.VideoCapture(path)
# Eine Schleife, um die Videodatei abzuspielen. Dies kann auch eine while-Schleife sein,
# bis eine Taste gedrückt wird, usw.
for i in range(100):
    # Einen Frame holen
    retval, frame = video.read()
    # Rotieren, weil es aus irgendeinem Grund sonst gespiegelt erscheint.
    frame = numpy.rot90(frame)
    # Das Video verwendet BGR-Farben und PyGame benötigt RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Eine PyGame-Oberfläche erstellen
    surf = pygame.surfarray.make_surface(frame)
    # Jetzt kann man beliebiges auf die PyGame-Oberfläche zeichnen!
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # Die PyGame-Oberfläche anzeigen!
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
```