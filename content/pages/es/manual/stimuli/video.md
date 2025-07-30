title: Reproducción de video
hash: 135ac06d95735a29df2450dc840b4ab283182095a768134d3d35e7c85f031901
locale: es
language: Spanish

[TOC]


## plugin media_player_mpy

El [MEDIA_PLAYER_MPY](https://github.com/open-cogsci/opensesame-plugin-mediaplayer) plugin está basado en MoviePy. Se incluye por defecto con OpenSesame. (Si tienes un entorno personalizado, puedes obtenerlo instalando el paquete `opensesame-plugin-media_player_mpy`.)

## OpenCV

OpenCV es una poderosa librería de visión por computadora, que contiene (entre muchas otras cosas) rutinas para leer archivos de video.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

El siguiente ejemplo muestra cómo reproducir un archivo de video, dibujando un cuadrado rojo encima del video. Este ejemplo asume que estás usando el backend heredado.

```python
import cv2
import numpy
import pygame
# Ruta completa al archivo de vídeo en el grupo de archivos (file pool)
path = pool['myvideo.avi']
# Abrir el video
video = cv2.VideoCapture(path)
# Un bucle para reproducir el archivo de video. Esto también puede ser un bucle while
# hasta que se presione una tecla, etc.
for i in range(100):
    # Obtener un frame
    retval, frame = video.read()
    # Rotarlo, porque por alguna razón aparece volteado si no.
    frame = numpy.rot90(frame)
    # El video usa colores BGR y PyGame necesita RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Crear una superficie de PyGame
    surf = pygame.surfarray.make_surface(frame)
    # ¡Ahora puedes dibujar lo que quieras sobre la superficie de PyGame!
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # ¡Mostrar la superficie de PyGame!
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
```