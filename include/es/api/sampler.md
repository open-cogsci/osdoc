<div class="ClassDoc YAMLDoc" markdown="1">

# clase __Sampler__

La clase `Sampler` proporciona funcionalidad para reproducir muestras de sonido. Generalmente, se crea un objeto `Sampler` con la función de fábrica `Sampler()`, como se describe en la sección [Creando un Sampler](#creating-a-sampler).

__Ejemplo:__

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
my_sampler.play()
~~~

[TOC]

## Cosas que debes saber

### Creando un Sampler

Generalmente, se crea un `Sampler` con la función de fábrica `Sampler()`, que toma la ruta completa a un archivo de sonido como primer argumento.

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
~~~

Opcionalmente, puedes pasar [Palabras clave de reproducción](#playback-keywords) a `Sampler()`
para establecer el comportamiento predeterminado:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5)
~~~

### Velocidad de muestreo

Si encuentras que tu muestra se reproduce demasiado lentamente (tono bajo) o demasiado rápido (tono alto), asegúrate de que la velocidad de muestreo de tu muestra coincida con la velocidad de muestreo del back-end del sampler como se especifica en la configuración del back-end.

### Formatos de archivo compatibles

Se admiten archivos de sonido en formato `.wav`, `.mp3` y `.ogg`. Si necesitas
convertir muestras de un formato diferente, puedes usar
[Audacity](http://sourceforge.net/projects/audacity/).

### Palabras clave de reproducción

Las funciones que aceptan `**playback_args` toman los siguientes argumentos clave:

- `volume` especifica un volumen entre `0.0` (silencio) y `1.0` (máximo).
- `pitch` especifica un tono (o velocidad de reproducción), donde los valores > 1 indican un
  tono más alto, y los valores < 1 indican un tono más bajo.
- `pan` especifica un paneo, donde los valores < 0 indican paneo hacia la izquierda, y
  valores > 0 indican paneo hacia la derecha. Alternativamente, puedes establecer pan en
  'left' o 'right' para reproducir solo un canal.
- `duration` especifica la duración del sonido en milisegundos o se establece en
  `0` o `None` para reproducir el sonido completo.
- `fade_in` especifica el tiempo de entrada (o ataque) del sonido, o se establece en
  `0` o `None` para deshabilitar la entrada.
- `block` indica si el experimento debe bloquearse (`True`) durante
  reproducción o no (`False`).

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src)
my_sampler.play(volume=.5, pan='left')
~~~

Las palabras clave de reproducción solo afectan la operación actual (excepto cuando se pasan a
`Sampler()` al crear el objeto). Para cambiar el comportamiento para todos
operaciones posteriores, establece las propiedades de reproducción directamente:

~~~ .python
  src = pool['bark.ogg']
  my_sampler = Sampler(src)
  my_sampler.volume = .5
  my_sampler.pan = 'left'
  my_sampler.play()
~~~

O pasa las palabras clave de reproducción a `Sampler()` al crear el objeto:

~~~ .python
src = pool['bark.ogg']
my_sampler = Sampler(src, volume=.5, pan='left')
my_sampler.play()
~~~

## close_sound(experiment)

Cierra el mezclador después de que finalice el experimento.

__Parámetros__

- **experiment**: El objeto de experimento.

## init_sound(experiment)

Inicializa el mezclador de pygame antes de que comience el experimento.

__Parámetros__

- **experiment**: El objeto de experimento.

## is_playing(self)
  
Verifica si un sonido se está reproduciendo actualmente.

__Devuelve__

- Verdadero si se está reproduciendo un sonido, Falso si no lo está.

__Ejemplo__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
if my_sampler.is_playing():
        print('¡El sampler sigue reproduciendo!')
~~~



## pause(self)

Pausa la reproducción (si la hay).

__Ejemplo__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~



## play(\*arglist, \*\*kwdict)

Reproduce el sonido.

__Parámetros__

- **\*\*playback_args**: Opcional [palabras clave de reproducción](#playback-keywords) que se utilizarán
para esta llamada a `Sampler.play()`. Esto no afecta
operaciones posteriores.

__Ejemplo__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play(pitch=.5, block=True)
~~~



## resume(self) 


Reanuda la reproducción (si la hay).



__Ejemplo__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.pause()
sleep(100)
my_sampler.resume()
~~~



## set_config(\*\*cfg)

Actualiza las configurables.


__Parámetros__

- **\*\*cfg**: Las configurables a actualizar.


## stop(self)

Detiene el sonido que se está reproduciendo en este momento (si lo hay).



__Ejemplo__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
sleep(100)
my_sampler.stop()
~~~



## wait(self)

Bloquea hasta que el sonido haya terminado de reproducirse o retorna inmediatamente
si no se está reproduciendo ningún sonido.



__Ejemplo__

~~~ .python
src = pool['my_sound.ogg']
my_sampler = Sampler(src)
my_sampler.play()
my_sampler.wait()
print('¡El sampler ha terminado!')
~~~



</div>
