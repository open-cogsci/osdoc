title: Grados de ángulo visual
hash: b9febd85c8491dfed24e738cf632d1d0051f391ed1835b760f8fbf04f7846eef
locale: es
language: Spanish

A menudo verá que el tamaño de los estímulos visuales se expresa en grados de ángulo visual (°). Los grados visuales expresan el ángulo entre las líneas rectas desde las extremidades del estímulo hasta la lente del ojo. Por lo tanto, el ángulo visual está relacionado con el tamaño que un estímulo abarca en la retina, pero solo de manera indirecta: es un ángulo medido desde la lente del ojo, como se ilustra en %FigEye

[TOC]

%--
figure:
 id: FigEye
 source: fig-eye.png
 caption: Una ilustración esquemática de grados de ángulo visual. (Imagen adaptada de [WikiMedia Commons](http://commons.wikimedia.org/wiki/File:Schematic_diagram_of_the_human_eye.svg).)
--%

La razón para usar esta medida algo extraña del tamaño es que refleja el tamaño percibido de un estímulo, que en los experimentos psicológicos a menudo es más importante que su tamaño real. Por ejemplo, si presenta una imagen con un ancho real de 100 píxeles en el monitor, el ángulo visual puede corresponder a 3°. Si aleja el monitor, el ángulo visual de la imagen disminuirá a, digamos, 2°. El ángulo visual, por lo tanto, refleja que la distancia entre un estímulo y un observador es importante.

Ver también:

- <http://en.wikipedia.org/wiki/Visual_angle>

## Convertir píxeles a grados visuales

Necesitará conocer tres cosas para convertir píxeles en grados visuales:

- `h` es la altura del monitor en centímetros, que puede medir con una regla. (por ejemplo, 25 cm)
- `d` es la distancia desde el participante hasta el monitor en centímetros, que puede medir con una regla. (por ejemplo, 60 cm)
- `r` es la resolución vertical del monitor en píxeles, que puede encontrar en la configuración de pantalla de su sistema operativo (por ejemplo, 768 px)

Puede calcular el tamaño angular de su estímulo como se muestra a continuación. Puede ejecutar este script en la ventana de depuración de OpenSesame. Por supuesto, necesita sustituir todos los valores para que correspondan a su configuración. Tenga en cuenta que un solo grado visual generalmente corresponde a 30 - 60 píxeles, dependiendo de la distancia y el tamaño del monitor. A la inversa, un solo píxel generalmente corresponde a 0,01 a 0,03 grados visuales. Si obtiene valores fuera de este rango, probablemente haya cometido un error.

```python
from math import atan2, degrees

h = 25           # Altura del monitor en cm
d = 60           # Distancia entre el monitor y el participante en cm
r = 768          # Resolución vertical del monitor
size_in_px = 100 # El tamaño del estímulo en píxeles
# Calcule la cantidad de grados que corresponden a un solo píxel. Esto será
# generalmente un valor muy pequeño, algo así como 0.03.
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'{deg_per_px} grados corresponden a un solo píxel')
# Calcular el tamaño del estímulo en grados
size_in_deg = size_in_px * deg_per_px
print(f'El tamaño del estímulo es {size_in_px} píxeles y {size_in_deg} grados visuales')
```

## Convertir grados visuales a píxeles

Convertir grados visuales a píxeles es simplemente la inversa del procedimiento descrito anteriormente y se puede hacer de la siguiente manera:

```python
from math import atan2, degrees
h = 25           # Altura del monitor en cm
d = 60           # Distancia entre el monitor y el participante en cm
r = 768          # Resolución vertical del monitor
size_in_deg = 3. # El tamaño del estímulo en píxeles
# Calcule la cantidad de grados que corresponden a un solo píxel. Esto será
# generalmente un valor muy pequeño, algo así como 0.03.
deg_per_px = degrees(atan2(.5 * h, d)) / (.5 * r)
print(f'{deg_per_px} grados corresponden a un solo píxel')
# Calcular el tamaño del estímulo en grados
size_in_px = size_in_deg / deg_per_px
print(f'El tamaño del estímulo es {size_in_px} píxeles y {size_in_deg} grados visuales')
```
