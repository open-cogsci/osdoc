title: Lecture vidéo
hash: 135ac06d95735a29df2450dc840b4ab283182095a768134d3d35e7c85f031901
locale: fr
language: French

[TOC]


## plugin media_player_mpy

Le plugin [MEDIA_PLAYER_MPY](https://github.com/open-cogsci/opensesame-plugin-mediaplayer) est basé sur MoviePy. Il est inclus par défaut avec OpenSesame. (Si vous disposez d’un environnement personnalisé, vous pouvez l’obtenir en installant le paquet `opensesame-plugin-media_player_mpy`.)


## OpenCV

OpenCV est une bibliothèque puissante de vision par ordinateur, qui contient (entre autres) des routines pour lire des fichiers vidéo.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

L’exemple suivant montre comment lire un fichier vidéo tout en dessinant un carré rouge par-dessus la vidéo. Cet exemple suppose que vous utilisez le backend hérité.

```python
import cv2
import numpy
import pygame
# Chemin complet vers le fichier vidéo dans la banque de fichiers
path = pool['myvideo.avi']
# Ouvre la vidéo
video = cv2.VideoCapture(path)
# Une boucle pour lire le fichier vidéo. Il peut aussi s’agir d’une boucle while jusqu’à ce qu’une touche
# soit pressée, etc.
for i in range(100):
    # Obtient une image
    retval, frame = video.read()
    # Tourne l’image, car sinon elle apparaît retournée pour une raison quelconque.
    frame = numpy.rot90(frame)
    # La vidéo utilise des couleurs BGR et PyGame a besoin de RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Crée une surface PyGame
    surf = pygame.surfarray.make_surface(frame)
    # Vous pouvez maintenant dessiner ce que vous voulez sur la surface PyGame !
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # Affichez la surface PyGame !
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
```
