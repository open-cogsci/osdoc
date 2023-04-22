title: Lecture vidéo
hash: a3addf316f97e40c4be8ba9a0bcb131cf86555b8bcc9616dfd23957587f38442
locale: fr
language: French

[TOC]

## plugin media_player_mpy

Le plugin MEDIA_PLAYER_MPY est basé sur MoviePy. Il est inclus par défaut avec les packages OpenSesame pour Windows et Mac OS. S'il n'est pas installé, vous pouvez l'obtenir en installant le package `opensesame-plugin-media-player-mpy`, comme décrit ici :

- <https://rapunzel.cogsci.nl/manual/environment/>

Le code source est hébergé à l'adresse suivante :

- <https://github.com/dschreij/opensesame-plugin-mediaplayer>


## OpenCV

OpenCV est une puissante bibliothèque de vision par ordinateur, qui contient (entre autres choses) des routines pour lire des fichiers vidéo.

- <http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html>

L'exemple suivant montre comment lire un fichier vidéo tout en dessinant un carré rouge par-dessus la vidéo. Cet exemple suppose que vous utilisez le backend hérité.

~~~ .python
import cv2
import numpy
import pygame
# Chemin d'accès complet au fichier vidéo dans la file d'attente
path = pool['myvideo.avi']
# Ouvrir la vidéo
video = cv2.VideoCapture(path)
# Une boucle pour jouer le fichier vidéo. Cela peut aussi être une boucle while jusqu'à ce qu'une touche
# soit pressée. etc.
for i in range(100):
    # Obtenir une image
    retval, frame = video.read()
    # Le retourner, car pour une raison quelconque, il apparaît autrement inversé.
    frame = numpy.rot90(frame)
    # La vidéo utilise des couleurs BGR et PyGame a besoin de RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Créer une surface PyGame
    surf = pygame.surfarray.make_surface(frame)
    # Maintenant, vous pouvez dessiner ce que vous voulez sur la surface PyGame !
    pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
    # Afficher la surface PyGame !
    exp.surface.blit(surf, (0, 0))
    pygame.display.flip()
~~~