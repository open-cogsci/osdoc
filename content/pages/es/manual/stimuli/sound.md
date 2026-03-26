title: Sonido
hash: abc659dc7f36f6c760c6f029cd4e89ea9f3cf46e33e009701bc55bafd4f59b01
locale: es
language: Spanish

La forma más común de reproducir sonido es usando el ítem SAMPLER, para la reproducción de archivos de audio, o el ítem SYNTH, para la reproducción de pitidos simples, etc.

[TOC]

## El sampler

El SAMPLER reproduce un solo archivo de sonido, normalmente desde el file pool.

Los archivos de sonido siempre se reproducen con la frecuencia de muestreo que usa el backend de sampler de OpenSesame. Si tu muestra parece reproducirse demasiado rápido (tono alto) o demasiado lento (tono bajo), puedes ajustar la frecuencia de muestreo de tu archivo de sonido en un editor de sonido, o cambiar la frecuencia de muestreo usada por el backend de sampler de OpenSesame (en 'Show backend settings and info' en la pestaña General).

El SAMPLER tiene unas pocas opciones:

- *Archivo de sonido* indica el archivo que se va a reproducir.
- *Volumen* entre 0 (silencio) y 1 (volumen normal).
- *Pan* atenúa el canal derecho (valores negativos) o izquierdo (valores positivos). Para un paneo completo, introduce 'left' o 'right',
- *Tono* indica la velocidad de reproducción, donde 1 corresponde a la velocidad original.
- *Detener después de* indica durante cuánto tiempo debe reproducirse el archivo de sonido. Por ejemplo, un valor de 100 ms significa que la reproducción se detendrá después de 100 ms, independientemente de la duración del archivo de sonido. Un valor de 0 ms significa que el archivo de sonido se reproducirá por completo.
- *Fundido de entrada* indica el tiempo de fundido de entrada del archivo de sonido. Por ejemplo, un valor de 100 ms significa que el archivo de sonido comenzará en silencio y aumentará hasta el valor máximo en 100 ms.
- *Duración* indica la duración del ítem sampler, antes de que se presente el siguiente ítem. Esto no necesita coincidir con la duración del archivo de sonido. Por ejemplo, si la duración del sampler se establece en 0 ms, OpenSesame avanzará directamente al ítem que sigue al SAMPLER (p. ej., un sketchpad), *mientras el archivo de sonido sigue reproduciéndose en segundo plano*. Además de un valor numérico, puedes establecer la duración en:
	- 'keypress' para esperar una pulsación de tecla
	- 'mouseclick' para esperar un clic del ratón
	- 'sound' para esperar hasta que el sampler haya terminado de reproducirse.

## El synth

El SYNTH es un sintetizador de sonido básico.

Puedes especificar varias
opciones:

- *Forma de onda* puede establecerse en sine, sawtooth, square, o white noise
- *Attack* es el tiempo que tarda el sonido en alcanzar el volumen máximo (es decir, fundido de entrada).
- *Decay* es el tiempo que tarda el sonido en extinguirse (es decir, fundido de salida). Ten en cuenta que el decay ocurre dentro de la duración del sonido.
- *Volumen* entre 0 y 100%
- *Pan* atenúa el canal derecho (valores negativos) o izquierdo (valores positivos). Establecer pan en -20 o 20 silencia completamente el canal derecho o izquierdo, respectivamente.
- *Length* indica la duración del sonido (en milisegundos).
- *Duration* indica la duración del ítem SYNTH, antes de que se presente el siguiente ítem. Esto no necesita coincidir con la duración del sonido. Por ejemplo, la duración del SYNTH puede establecerse en 0 ms, para avanzar directamente al siguiente ítem (p. ej., un SKETCHPAD), mientras el sonido sigue reproduciéndose en segundo plano. Además de un valor numérico, puedes establecer la duración en 'keypress', para esperar una pulsación de teclado, 'mouseclick', para esperar un clic del ratón, o 'sound', para esperar hasta que el SYNTH haya terminado de reproducirse.

## Temporización del sonido en sampler y synth

Reproducir un sonido en OpenSesame implica dos controles independientes: uno que determina cuánto tiempo se reproduce el propio sonido, y otro que determina cuánto tiempo espera el experimento en el ítem actual antes de continuar. Comprender la diferencia entre estos dos controles es esencial para una temporización precisa de los estímulos.

### Dos controles independientes

#### Duración del sonido

| Item | Parameter | Description |
|---|---|---|
| **Sampler** | **Stop after** | Corta el archivo de audio después del número dado de ms. Establécelo en `0` para reproducir el archivo hasta su final natural. |
| **Synth** | **Length** | Establece directamente cuánto dura el tono generado (en ms). No hay un final natural más allá del valor especificado. |

#### Temporización del ítem

Tanto SAMPLER como SYNTH comparten el parámetro *Duration*, que controla cuánto tiempo permanece el experimento en el ítem antes de pasar al siguiente. No afecta directamente al sonido en sí.

| Valor de Duration | Comportamiento |
|---|---|
| `0` | Pasar inmediatamente |
| *number* (ms) | Esperar el número dado de ms y luego continuar |
| `sound` | Esperar hasta que el sonido haya terminado de reproducirse |


### Regla general

Que *sound length* se refiera a:
- *Stop after* para SAMPLER, o la duración natural del archivo si *Stop after* es `0`
- *Length* para SYNTH

Entonces se aplica lo siguiente:

| Condición | Resultado |
|---|---|
| *Duration* **<** sound length | El ítem termina antes que el sonido, por lo que el sonido continúa en el siguiente ítem |
| *Duration* = `sound` | El experimento espera hasta que el sonido termine |
| *Duration* **≥** sound length | El ítem dura más que el sonido, por lo que la reproducción ha terminado antes de que comience el siguiente ítem |

### Notas

- Para SAMPLER, el tiempo real de reproducción es la duración natural del archivo, a menos que *Stop after* sea mayor que `0`, en cuyo caso la reproducción se detiene después de la duración especificada.
- Para SYNTH, el tiempo real de reproducción siempre es igual a *Length*.
- Cuando *Duration* = `sound`, el experimento espera el tiempo real de reproducción, teniendo en cuenta *Stop after* para SAMPLER.

### El sonido continúa en el siguiente ítem

Un sonido puede seguir reproduciéndose después de que el ítem actual haya terminado si *Duration* es más corto que el tiempo real de reproducción. Esto puede ser intencional, por ejemplo cuando quieres que un sonido se reproduzca en segundo plano mientras se muestra el siguiente ítem. Pero también puede ocurrir de forma no intencional si *Duration* es más corto de lo esperado, en cuyo caso el sonido puede extenderse al siguiente elemento del ensayo.

## Reproducción de sonido en Python

Puedes usar el objeto SAMPLER y la función SYNTH para presentar estímulos visuales en Python:

- %link:sampler%
- %link:manual/python/common%


## Plugins de Audio Low Latency

El objetivo principal de los plugins de Audio Low Latency, desarrollados por Bob Rosbag, es reproducir y grabar audio con latencias mínimas y predecibles para lograr una alta exactitud y precisión. El paquete `PyAlsaAudio`, que utiliza el sistema de audio ALSA de Linux, proporcionó los mejores resultados dentro de Python. `PortAudio` y `sounddevice` son multiplataforma y funcionan tanto en Windows como en Linux.

Los plugins no se instalan de forma predeterminada, pero se pueden instalar mediante pip:

```bash
pip install opensesame-plugin-audio-low-latency
```

Véase también:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>