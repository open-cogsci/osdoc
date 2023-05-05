title: Motores de fondo
hash: 1447d1754e76a00442c1709babb3c8b9ef77f76eb2aeb0c1e6bb57c9a232512c
locale: es
language: Spanish

El *backend* es la capa de software que se encarga de la entrada (entrada de teclado, entrada de mouse, etc.) y la salida (presentación en pantalla, reproducción de sonido, etc.). Hay muchas bibliotecas que ofrecen este tipo de funcionalidad y OpenSesame podría, en principio, utilizar cualquiera de ellas. Por esta razón, OpenSesame es independiente del backend, en el sentido de que puedes elegir qué backend se debe usar. Actualmente hay cuatro backends: *legacy*, *psycho*, *xpyriment* y *osweb*.

[TOC]

## Diferencias y algunos consejos

Por lo general, no notarás qué backend se está utilizando. Las diferencias entre los backends son en gran parte técnicas y, siempre que se utilice la interfaz gráfica de usuario, todos los backends funcionan más o menos de la misma manera. Sin embargo, hay algunas razones para preferir un backend sobre otro:

- Si deseas ejecutar el experimento en un navegador, debes seleccionar el backend *osweb*.
- Los backends difieren en [precisión temporal](%link:timing%).
	- Consejo: Si te preocupa la precisión temporal en milisegundos, usa *xpyriment* o *psycho*.
- Los backends difieren en cuánto tiempo lleva preparar el estímulo.
	- Consejo: Si los [formularios](%link:manual/forms/about%) son lentos, usa *legacy*.
	- Consejo: Si el intervalo entre ensayos es largo (debido a la preparación del estímulo), usa *legacy*.
- Puedes utilizar funciones específicas del backend al escribir código Python.
	- Consejo: Si deseas utilizar la funcionalidad de PsychoPy, usa *psycho*.
	- Consejo: Si deseas utilizar la funcionalidad de Expyriment, usa *xpyriment*.
	- Consejo: Si deseas utilizar la funcionalidad de PyGame, usa *legacy*.
- Algunos backends no están disponibles en todas las plataformas.

## Seleccionar un backend

Puedes seleccionar un backend en las propiedades generales del experimento (%FigSelect).

%--
figure:
 id: FigSelect
 source: fig-select.png
 caption: "Seleccionando un backend"
--%

Si ves el script general (selecciona "Mostrar editor de scripts"), verás que en realidad hay seis backends distintos: canvas, keyboard, mouse, sampler, color y clock. El método combobox selecciona automáticamente una combinación adecuada y predefinida de backends, pero en teoría podrías mezclar y combinar.

Por ejemplo, si seleccionas el backend *xpyriment*, se generará el siguiente código:

	set sampler_backend legacy
	set mouse_backend xpyriment
	set keyboard_backend legacy
	set color_backend legacy
	set clock_backend legacy
	set canvas_backend xpyriment

## xpyriment

El backend *xpyriment* se basa en [Expyriment][], una biblioteca diseñada para crear experimentos psicológicos. Es un backend acelerado por hardware de peso ligero con excelentes propiedades de sincronización. Si te preocupa la precisión temporal, pero no tienes la intención de generar estímulos complejos (es decir, parches Gabor, rejillas de puntos aleatorios, etc.), *xpyriment* es una buena opción.

### Usar Expyriment directamente

Puedes encontrar una amplia documentación sobre Expyriment en <http://www.expyriment.org/doc>. El siguiente fragmento de código muestra una línea de texto:

~~~ .python
from expyriment import stimuli
text = stimuli.TextLine('¡Esto es expyriment!')
text.present()
~~~

### Citación

Aunque Expyriment está incluido en las distribuciones binarias de OpenSesame, es un proyecto independiente. Cuando sea apropiado, proporciona la siguiente cita además de citar OpenSesame:

Krause, F., & Lindemann, O. (en prensa). Expyriment: una biblioteca de Python para experimentos cognitivos y neurocientíficos. *Behavior Research Methods*.
{: .reference}

## psycho

El backend psycho se basa en [PsychoPy][], una biblioteca diseñada para crear experimentos psicológicos. Está acelerado por hardware y proporciona rutinas de alto nivel para crear estímulos visuales complejos (rejillas en movimiento, etc.). Si te preocupa el tiempo y planeas crear estímulos complejos, Psycho es una buena opción.

### Usar PsychoPy directamente

Puede encontrar una amplia documentación sobre PsychoPy en <http://www.psychopy.org/>. Al usar PsychoPy en OpenSesame, es importante saber que la ventana principal se puede acceder como `self.experiment.window` o simplemente `win`. Entonces, el siguiente fragmento de código dibuja un parche Gabor:

~~~ .python
from psychopy import visual
gabor = visual.PatchStim(win, tex="sin", size=256, mask="gauss", sf=0.05, ori=45)
gabor.draw()
win.flip()
~~~

### Tutoriales

Un tutorial específico para usar PsychoPy desde OpenSesame:

- <http://www.cogsci.nl/blog/tutorials/211-a-bit-about-patches-textures-and-masks-in-psychopy>

Y un tutorial más general de PsychoPy:

- <http://gestaltrevision.be/wiki/coding>

### Citas

Aunque PsychoPy está incluido en las distribuciones binarias de OpenSesame, es un proyecto separado. Cuando corresponda, por favor cite los siguientes documentos además de citar a OpenSesame:

Peirce, J. W. (2007). PsychoPy: Psychophysics software in Python. *Journal of Neuroscience Methods*, *162*(1-2), 8-13. doi:10.1016/j.jneumeth.2006.11.017
{: .reference}

Peirce, J. W. (2009). Generating stimuli for neuroscience using PsychoPy. *Frontiers in Neuroinformatics*, *2*(10). doi:10.3389/neuro.11.010.2008
{: .reference}

## legacy

El backend legacy se basa en [PyGame][] en modo no-OpenGL. La desventaja de esto es que no hay aceleración de hardware y las propiedades de sincronización no son tan buenas como las de los backends psycho o xpyriment. La ventaja es que PyGame es muy fácil de usar, muy confiable y tiene un buen soporte en una amplia gama de plataformas.

### Visibilidad del cursor del ratón

En algunos sistemas, el cursor del ratón no es visible al usar el backend *legacy* en modo de pantalla completa. Puede solucionar esto de las siguientes maneras:

1. Abra la configuración del backend *legacy* y establezca "Doble almacenamiento en búfer" en "no".
	- *Nota:* Esto puede deshabilitar la sincronización vertical (v-sync), lo cual puede ser importante para experimentos críticos en tiempo, como se discute [aquí](%link:timing%).
2. Abra la configuración del backend *legacy* y establezca "Cursor personalizado" en "sí".
3. Cambie a otro backend.

### Usar PyGame directamente

PyGame está bien documentado y puede encontrar todo lo que necesita saber sobre cómo usar PyGame en <http://www.pygame.org/docs/>. Específico para OpenSesame es el hecho de que la superficie de visualización se almacena como `self.experiment.window` o simplemente `win`. Entonces, el siguiente fragmento de código, que podría pegar en un elemento INLINE_SCRIPT, dibuja un rectángulo rojo en la pantalla:

~~~ .python
import pygame # Importar el módulo PyGame
pygame.draw.rect(self.experiment.window, pygame.Color("red"),
	[20, 20, 100, 100]) # Dibujar un rectángulo rojo. Aún no se muestra ...
pygame.display.flip() # Actualizar la pantalla para mostrar el rectángulo rojo.
~~~


## osweb

El backend *osweb* se basa en OSWeb y permite ejecutar experimentos en un navegador. Para obtener más información, consulte:

- %link:manual/osweb/workflow%