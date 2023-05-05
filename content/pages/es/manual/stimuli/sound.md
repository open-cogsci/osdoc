title: Sonido
hash: 2a7ee6fde847af9407b8719c0f7ddecc8711cf1e09f8a2c6db320088aa8d67f1
locale: es
language: Spanish

La forma más común de reproducir sonido es utilizando el elemento SAMPLER, para la reproducción de archivos de audio, o el elemento SYNTH, para la reproducción de pitidos simples, etc.

[TOC]

## El sampler

El SAMPLER reproduce un único archivo de sonido, generalmente del grupo de archivos.

Los archivos de sonido siempre se reproducen a la velocidad de muestreo utilizada por el backend del sampler de OpenSesame. Si tu muestra parece estar acelerada (tono alto) o desacelerada (tono bajo), puedes ajustar la velocidad de muestreo de tu archivo de sonido en un editor de sonido, o cambiar la velocidad de muestreo utilizada por el backend del sampler de OpenSesame (en 'Mostrar configuraciones e información del backend' en la pestaña General).

El SAMPLER tiene algunas opciones:

- *Sound file* indica el archivo que será reproducido.
- *Volume* entre 0 (silencio) y 1 (volumen normal).
- *Pan* baja el canal derecho (valores negativos) o izquierdo (valores positivos). Para un panoramización completa, ingrese 'izquierda' o 'derecha'.
- *Pitch* indica la velocidad de reproducción, donde 1 corresponde a la velocidad original.
- *Stop after* indica cuánto tiempo se debe reproducir el archivo de sonido. Por ejemplo, un valor de 100 ms significa que la reproducción se detendrá después de 100 ms, sin importar la duración del archivo de sonido. Un valor de 0 ms significa que el archivo de sonido se reproducirá por completo.
- *Fade in* indica el tiempo de fundido de entrada para el archivo de sonido. Por ejemplo, un valor de 100 ms significa que el archivo de sonido comenzará en silencio y aumentará al valor máximo en 100 ms.
- *Duration* indica la duración del elemento sampler, antes de que se presente el siguiente elemento. Esto no necesita coincidir con la duración del archivo de sonido. Por ejemplo, si la duración del sampler se establece en 0 ms, OpenSesame avanzará directamente al elemento siguiente al SAMPLER (por ejemplo, un sketchpad), *mientras el archivo de sonido continúa reproduciéndose en segundo plano*. Además de un valor numérico, puedes establecer la duración en:
	- 'keypress' para esperar una pulsación de tecla
	- 'mouseclick' para esperar un clic del mouse
	- 'sound' para esperar hasta que el sampler haya terminado de reproducir.

## El synth

El SYNTH es un sintetizador de sonido básico.

Puedes especificar una serie de opciones:

- *Waveform* se puede configurar en seno, diente de sierra, cuadrado o ruido blanco
- *Attack* es el tiempo que tarda el sonido en alcanzar el volumen máximo (es decir, desvanecerse).
- *Decay* es el tiempo que tarda el sonido en desaparecer (es decir, desvanecerse). Ten en cuenta que la decadencia ocurre dentro de la duración del sonido.
- *Volume* entre 0 y 100%
- *Pan* baja el canal derecho (valores negativos) o izquierdo (valores positivos). Establecer el pan en -20 o 20 silencia completamente el canal derecho o izquierdo, respectivamente.
- *Length* indica la duración del sonido (en milisegundos).
- *Duration* indica la duración del elemento SYNTH, antes de que se presente el siguiente elemento. Esto no necesita coincidir con la duración del sonido. Por ejemplo, la duración del SYNTH puede establecerse en 0 ms para avanzar directamente al siguiente elemento (por ejemplo, un SKETCHPAD) mientras el sonido continúa reproduciéndose en segundo plano. Además de un valor numérico, puedes establecer la duración en 'keypress' para esperar una pulsación de tecla, 'mouseclick' para esperar un clic del mouse o 'sound' para esperar hasta que el SYNTH haya terminado de reproducir.

## Reproducción de sonido en Python

Puedes utilizar el objeto SAMPLER y la función SYNTH para presentar estímulos visuales en Python:

- %link:sampler%
- %link:manual/python/common%


## Plugins de baja latencia de audio

El objetivo principal de los plugins de baja latencia de audio, desarrollados por Bob Rosbag, es reproducir y grabar audio con latencias mínimas y predecibles para lograr una alta precisión y exactitud. El paquete `PyAlsaAudio`, que utiliza el sistema de audio ALSA de Linux, proporcionó los mejores resultados dentro de Python. `PortAudio` y `sounddevice` son multiplataforma y funcionan tanto en Windows como en Linux.

Los plugins no están instalados de forma predeterminada, pero pueden instalarse a través de pip:

```bash
pip install opensesame-plugin-audio-low-latency
```

Consulta también:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>