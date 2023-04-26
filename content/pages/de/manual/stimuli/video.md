title: Videowiedergabe
hash: a3addf316f97e40c4be8ba9a0bcb131cf86555b8bcc9616dfd23957587f38442
locale: de
language: German

[TOC]

## media_player_mpy-Plugin

Das MEDIA_PLAYER_MPY-Plugin basiert auf MoviePy. Es ist standardmäßig in den Windows- und Mac OS-Paketen von OpenSesame enthalten. Wenn es nicht installiert ist, können Sie es durch Installieren des `opensesame-plugin-media-player-mpy`-Pakets erhalten, wie hier beschrieben:

- <https://rapunzel.cogsci.nl/manual/environment/>

Der Quellcode ist hier zu finden:

- <https://github.com/dschreij/opensesame-plugin-mediaplayer>


## OpenCV

OpenCV ist eine leistungsstarke Computer-Vision-Bibliothek, die (unter anderem) Routinen zum Lesen von Videodateien enthält.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

Das folgende Beispiel zeigt, wie ein Videodatei abgespielt wird, während ein rotes Quadrat auf dem Video gezeichnet wird. Dieses Beispiel setzt voraus, dass Sie das Legacy-Backend verwenden.

~~~ .python
import cv2
import numpy
import pygame
# Vollständiger Pfad zur Videodatei im Dateipool
path = pool['myvideo.avi']
# Video öffnen
video = cv2.VideoCapture(path)
# Eine Schleife, um die Videodatei abzuspielen. Dies kann auch eine While-Schleife sein, bis eine Taste
# gedrückt wird usw.
for i in range(100):
    # Einzelbild holen
    retval, frame = video.read()
    # Drehen, weil es sonst aus irgendeinem Grund gespiegelt erscheint.
    frame = numpy.rot90(frame)
    # Das Video verwendet BGR-Farben und PyGame benötigt RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Eine PyGame-Oberfläche erstellen
    surf = pygame.surfarray.make_surface(frame)
    # Jetzt können Sie auf die PyGame-Oberfläche zeichnen, was immer Sie möchten!
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # Die PyGame-Oberfläche anzeigen!
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
~~~