title: Grabación de sonido
hash: 541c85146b0c2948e62bcae0056f831ddb9cf3e2d2a3025254b3d54dac2e5f46
locale: es
language: Spanish

[TOC]


## Complementos de Audio de Baja Latencia

Los complementos de Audio de Baja Latencia, desarrollados por Bob Rosbag, son la forma recomendada de grabar la entrada de sonido. El objetivo principal de este conjunto de complementos es reproducir y grabar audio con latencias mínimas y predecibles para lograr una alta precisión y exactitud. El paquete `PyAlsaAudio`, que utiliza el sistema de audio ALSA de Linux, proporcionó los mejores resultados dentro de Python. `PortAudio` y `sounddevice` son multiplataforma y funcionan tanto en Windows como en Linux.

Los complementos no están instalados por defecto, pero se pueden instalar a través de pip:

```bash
pip install opensesame-plugin-audio-low-latency
```

Ver también:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>


## Complementos de grabadora de sonido

Los complementos de la grabadora de sonido, desarrollados por Daniel Schreij, ya no están bajo desarrollo activo y, por lo tanto, ya no se recomiendan. Puede encontrar más información sobre este conjunto de complementos en la versión anterior de esta página:

- <https://osdoc.cogsci.nl/3.2/manual/response/soundrecording/>