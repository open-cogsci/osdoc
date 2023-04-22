title: Degrés d'angle visuel
hash: b9febd85c8491dfed24e738cf632d1d0051f391ed1835b760f8fbf04f7846eef
locale: fr
language: French

Vous verrez souvent que la taille des stimuli visuels est exprimée en degrés d'angle visuel (°). Les degrés visuels expriment l'angle entre les lignes droites des extrémités du stimulus jusqu'à la lentille de l'œil. Par conséquent, l'angle visuel est lié à la taille qu'un stimulus sous-tend sur la rétine, mais seulement indirectement : c'est un angle mesuré à partir de la lentille de l'œil, comme illustré dans %FigEye

[TOC]

%--
figure:
 id: FigEye
 source: fig-eye.png
 caption: Une illustration schématique des degrés d'angle visuel. (Image adaptée de [WikiMedia Commons](http://commons.wikimedia.org/wiki/File:Schematic_diagram_of_the_human_eye.svg).)
--%

La raison d'utiliser cette mesure de taille quelque peu étrange est qu'elle reflète la taille perçue d'un stimulus, qui dans les expériences psychologiques est souvent plus importante que sa taille réelle. Par exemple, si vous présentez une image avec une largeur réelle de 100 pixels sur le moniteur, l'angle visuel peut correspondre à 3°. Si vous éloignez le moniteur, l'angle visuel de l'image diminuera à, disons, 2°. L'angle visuel reflète ainsi que la distance entre un stimulus et un observateur est importante.

Voir aussi :

- <http://en.wikipedia.org/wiki/Visual_angle>

## Convertir les pixels en degrés visuels

Vous devez connaître trois choses pour convertir les pixels en degrés visuels :

- `h` est la hauteur du moniteur en centimètres, que vous pouvez mesurer avec une règle. (par exemple, 25cm)
- `d` est la distance entre le participant et le moniteur en centimètres, que vous pouvez mesurer avec une règle. (par exemple, 60cm)
- `r` est la résolution verticale du moniteur en pixels, que vous pouvez trouver dans les paramètres d'affichage de votre système d'exploitation (par exemple, 768 px)

Vous pouvez calculer la taille angulaire de votre stimulus comme indiqué ci-dessous. Vous pouvez exécuter ce script dans la fenêtre de débogage d'OpenSesame. Bien sûr, vous devez remplacer toutes les valeurs pour qu'elles correspondent à votre configuration. Notez qu'un degré visuel unique correspond généralement à 30 - 60 pixels, selon la distance et la taille du moniteur. Inversement, un seul pixel correspond généralement à 0,01 à 0,03 degrés visuels. Si vous obtenez des valeurs qui sont bien en dehors de cette plage, vous avez probablement commis une erreur.

```python
from math import atan2, degrees

h = 25           # Hauteur du moniteur en cm
d = 60           # Distance entre le moniteur et le participant en cm
r = 768          # Résolution verticale du moniteur
size_in_px = 100 # La taille du stimulus en pixels
# Calculez le nombre de degrés qui correspondent à un seul pixel. Cela sera
# généralement une valeur très petite, quelque chose comme 0,03.
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'{deg_per_px} degrés correspondent à un seul pixel')
# Calculez la taille du stimulus en degrés
size_in_deg = size_in_px * deg_per_px
print(f'La taille du stimulus est de {size_in_px} pixels et {size_in_deg} degrés visuels')
```

## Convertir les degrés visuels en pixels

Convertir les degrés visuels en pixels est simplement l'inverse de la procédure décrite ci-dessus et peut être fait comme suit :

```python
from math import atan2, degrees
h = 25           # Hauteur du moniteur en cm
d = 60           # Distance entre le moniteur et le participant en cm
r = 768          # Résolution verticale du moniteur
size_in_deg = 3. # La taille du stimulus en pixels
# Calculez le nombre de degrés qui correspondent à un seul pixel. Cela sera
# généralement une valeur très petite, quelque chose comme 0,03.
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'{deg_per_px} degrés correspondent à un seul pixel')
# Calculez la taille du stimulus en degrés
size_in_px = size_in_deg / deg_per_px
print(f'La taille du stimulus est de {size_in_px} pixels et {size_in_deg} degrés visuels')
```
