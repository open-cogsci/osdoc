title: Reproducción de video
hash: a3addf316f97e40c4be8ba9a0bcb131cf86555b8bcc9616dfd23957587f38442
locale: es
language: Spanish

[TOC]

## complemento media_player_mpy

El complemento MEDIA_PLAYER_MPY está basado en MoviePy. Está incluido por defecto en los paquetes de Windows y Mac OS de OpenSesame. Si no está instalado, puedes obtenerlo instalando el paquete `opensesame-plugin-media-player-mpy`, tal como se describe aquí:

- <https://rapunzel.cogsci.nl/manual/environment/>

El código fuente está alojado en:

- <https://github.com/dschreij/opensesame-plugin-mediaplayer>


## OpenCV

OpenCV es una potente biblioteca de visión por computadora que contiene (entre muchas otras cosas) rutinas para leer archivos de video.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

El siguiente ejemplo muestra cómo reproducir un archivo de video mientras se dibuja un cuadrado rojo encima del video. Este ejemplo supone que estás utilizando el backend heredado.

~~~ .python
import cv2
import numpy
import pygame
# Ruta completa al archivo de video en el grupo de archivos
path = pool['myvideo.avi']
# Abrir el video
video = cv2.VideoCapture(path)
# Un bucle para reproducir el archivo de video. Esto también puede ser un bucle while hasta que se presione una tecla.
for i in range(100):
    # Obtener un fotograma
    retval, frame = video.read()
    # Rotarlo, porque por alguna razón aparece volteado de lo contrario.
    frame = numpy.rot90(frame)
    # El video utiliza colores BGR y PyGame necesita RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Crear una superficie PyGame
    surf = pygame.surfarray.make_surface(frame)
    # ¡Ahora puedes dibujar lo que quieras en la superficie de PyGame!
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # ¡Mostrar la superficie de PyGame!
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
~~~