title: Tiempo
reviewed: false
hash: 220d36e32fac1e6b240a9d60c9d1a9e560276d629ba1cf584425ef078b5c3c85
locale: es
language: Spanish

Esta página describe varios problemas relacionados con el tiempo y proporciona resultados de referencia y consejos para probar su propio sistema. Si experimenta problemas con el tiempo, tómese el tiempo para leer esta página. Muchos problemas se resuelven teniendo en cuenta cosas como la preparación de estímulos y las propiedades de su monitor.

[TOC]

## ¿OpenSesame es capaz de cronometrar con precisión de milisegundos?

La respuesta corta es: sí. La respuesta larga es el resto de esta página.

## Consideraciones importantes para experimentos críticos de tiempo

### ¡Comprobar su tiempo!

OpenSesame le permite controlar el tiempo de su experimento de manera muy precisa. Pero esto no garantiza un tiempo preciso en cada experimento específico. Por diversas razones, muchas de las cuales se describen en esta página, puede experimentar problemas de tiempo. Por lo tanto, en experimentos críticos de tiempo, siempre debe verificar si el tiempo en su experimento es el previsto. La forma más fácil de hacer esto es comprobando las marcas de tiempo de visualización informadas por OpenSesame.

Cada elemento SKETCHPAD tiene una variable llamada `time_[sketchpad name]` que contiene la marca de tiempo de la última vez que se mostró el SKETCHPAD. Por lo tanto, si desea que el *target* SKETCHPAD se muestre durante 100 ms, seguido del SKETCHPAD *mask*, debe verificar que `time_mask` - `time_target` sea efectivamente 100. Al usar código en línea de Python, puede aprovechar el hecho de que `canvas.show()` devuelve la marca de tiempo de visualización.

### Entender su monitor

Los monitores de computadora se actualizan periódicamente. Por ejemplo, si la frecuencia de actualización de su monitor es de 100 Hz, la pantalla se actualiza cada 10 ms (1000 ms / 100 Hz). Esto significa que un estímulo visual siempre se presenta durante una duración que es múltiplo de 10 ms, y no podrá presentar un estímulo por, por ejemplo, 5 o 37 ms. La tasa de actualización más común es de 60 Hz (= ciclo de actualización de 16.67 ms), aunque a veces se utilizan monitores con tasas de actualización mucho más altas para sistemas experimentales.

En %VidRefresh puede ver cómo se ve una actualización del monitor en cámara lenta. En los monitores CRT (es decir, no pantalla plana, central) la actualización es un píxel único que va de izquierda a derecha y de arriba a abajo. Por lo tanto, solo un píxel está encendido a la vez, por lo que los monitores CRT parpadean levemente. En los monitores LCD o TFT (pantallas planas, izquierda y derecha) la actualización es un 'relleno de inundación' de arriba a abajo. Por lo tanto, los monitores LCD y TFT no parpadean. (A menos que presente un estímulo parpadeante, por supuesto).

%--
video:
 id: VidRefresh
 source: vimeo
 videoid: 24216910
 width: 640
 height: 240
 caption: Un video en cámara lenta del ciclo de actualización en monitores CRT (centro) y LCD / TFT. Video cortesía de Jarik den Hartog y el personal de soporte técnico de la Universidad VU de Ámsterdam.
--%

Si se presenta un estímulo nuevo mientras que el ciclo de actualización está a mitad de camino, observará un "desgarro". Es decir, la mitad superior del monitor mostrará la pantalla antigua, mientras que la parte inferior mostrará la nueva pantalla. Esto generalmente se considera indeseable, y, por lo tanto, se debe presentar una nueva pantalla en el momento exacto en que el ciclo de actualización comienza desde la parte superior. Esto se llama "sincronización con la actualización vertical" o simplemente "v-sync". Cuando el v-sync está habilitado, el desgarro ya no es visible, porque el desgarro coincide con el borde superior del monitor. Sin embargo, el v-sync no cambia nada sobre el hecho de que un monitor no se actualiza instantáneamente y, por lo tanto, siempre mostrará, durante algún tiempo, tanto la pantalla antigua como la nueva.

Otro concepto importante es el de 'bloqueo en el repintado vertical' o el 'volteo bloqueante'. Por lo general, cuando envías un comando para mostrar una nueva pantalla, la computadora aceptará este comando de inmediato y colocará la pantalla a mostrar en una cola. Sin embargo, la pantalla puede no aparecer en el monitor hasta un tiempo después, típicamente hasta el inicio del siguiente ciclo de actualización (suponiendo que v-sync esté habilitado). Por lo tanto, no sabes exactamente cuándo apareció la pantalla, porque tu marca de tiempo refleja el momento en que la pantalla se puso en cola, en lugar del momento en que se presentó. Para solucionar este problema, puedes utilizar un llamado 'volteo bloqueante'. Esto básicamente significa que cuando envías un comando para mostrar una nueva pantalla, la computadora se congelará hasta que aparezca la pantalla. Esto te permite obtener marcas de tiempo de pantalla muy precisas, a costa de una pérdida de rendimiento significativa debido a que la computadora está congelada durante gran parte del tiempo mientras espera que se muestre una pantalla. Pero para el propósito de los experimentos, un volteo bloqueante se considera generalmente la estrategia óptima.

Finalmente, los monitores LCD pueden sufrir de 'retraso de entrada'. Esto significa que hay un retraso adicional y, a veces, variable entre el momento en que la computadora 'cree' que aparece una pantalla y el momento en que realmente aparece. Este retraso se debe a varias formas de procesamiento digital realizadas por el monitor, como corrección de color o suavizado de imágenes. Hasta donde sé, el retraso de entrada no es algo que se pueda resolver mediante programación, y debes evitar los monitores con un retraso de entrada significativo para experimentos críticos en tiempo.

Para una discusión relacionada, consulte:

- <http://docs.expyriment.org/Timing.html#visual>

### Cumplir con el plazo de actualización

Imagina que llegas a una estación de tren a las 10:30. Tu tren sale a las 11:00, lo que te da exactamente 30 minutos para tomar un café. Sin embargo, si tomas café durante exactamente 30 minutos, llegarás de vuelta a la plataforma justo a tiempo para ver partir tu tren y tendrás que esperar al siguiente. Por lo tanto, si tienes 30 minutos de espera, debes tomar un café durante un poco menos de 30 minutos, como 25 minutos.

La situación es análoga al especificar intervalos para la presentación de estímulos visuales. Digamos que tienes un monitor de 100 Hz (1 actualización cada 10 ms) y quieres presentar un estímulo objetivo durante 100 ms, seguido de una máscara. Tu primera inclinación podría ser especificar un intervalo de 100 ms entre el objetivo y la máscara, porque eso es lo que deseas. Sin embargo, especificar un intervalo de exactamente 100 ms probablemente hará que la máscara 'no cumpla con el plazo de actualización' y la máscara se presentará solo en el siguiente ciclo de actualización, que es 10 ms más tarde (suponiendo que v-sync esté habilitado). Entonces, si especificas un intervalo de 100 ms, ¡en la mayoría de los casos terminarás con un intervalo de 110 ms!

La solución es simple: debes especificar un intervalo que sea un poco más corto de lo que estás buscando, como 95 ms. No te preocupes por que el intervalo sea demasiado corto, porque en un monitor de 100 Hz, el intervalo entre dos pantallas de estímulo necesariamente es un múltiplo de 10 ms. Por lo tanto, 95 ms se convertirá en 100 ms (10 cuadros), 1 ms se convertirá en 10 ms (1 cuadro), etc. Dicho de otra manera, los intervalos se redondearán hacia arriba (¡y nunca hacia abajo!) al intervalo más cercano que sea consistente con la velocidad de actualización del monitor.

### Deshabilitar efectos de escritorio

Muchos sistemas operativos modernos utilizan efectos gráficos de escritorio. Estos proporcionan, por ejemplo, los efectos de transparencia y los efectos de minimización y maximización suave de ventanas que se ven en la mayoría de los sistemas operativos modernos. Aunque el software que subyace a estos efectos difiere de un sistema a otro, generalmente forman una capa adicional entre tu aplicación y la pantalla. Esta capa adicional puede impedir que OpenSesame se sincronice con la actualización vertical y/ o que implemente un volteo bloqueante.

Aunque los efectos de escritorio *pueden* causar problemas, generalmente no lo hacen. Esto parece variar de un sistema a otro y de una tarjeta de video a otra. Sin embargo, cuando el sistema operativo lo permite, es mejor desactivar los efectos de escritorio en los sistemas que se utilizan para pruebas experimentales.

Algunos consejos sobre los efectos de escritorio en los diferentes sistemas operativos:

- En *Windows XP* no hay efectos de escritorio en absoluto.
- En *Windows 7* los efectos de escritorio se pueden desactivar seleccionando cualquiera de los temas enumerados en "Temas básicos y de alto contraste" en la sección de "Personalización".
- En *Windows 10* no hay forma de desactivar completamente los efectos de escritorio.
- En *Ubuntu y otras distribuciones de Linux que usan Gnome 3* no hay forma de desactivar completamente los efectos de escritorio.
- En *distribuciones de Linux que usan KDE* puedes desactivar los efectos de escritorio en la sección "Efectos de escritorio" de la configuración del sistema.
- En *Mac OS* aparentemente no hay forma de desactivar completamente los efectos de escritorio.

### Teniendo en cuenta el tiempo de preparación del estímulo/la estructura de preparar-ejecutar

Si te preocupa la precisión del tiempo durante la presentación del estímulo visual, debes preparar tus estímulos con anticipación. De esta manera, no tendrás demoras impredecibles debido a la preparación del estímulo durante las partes críticas de tiempo en tu experimento.

Primero consideremos un script (puedes pegarlo en un ítem INLINE_SCRIPT) que incluye el tiempo de preparación del estímulo en el intervalo entre `canvas1` y `canvas2` (%LstStimPrepBad). El intervalo especificado es de 95 ms, por lo que, teniendo en cuenta la regla de "redondeo hacia arriba" descrita en [Cumpliendo el plazo de actualización], esperarías un intervalo de 100 ms en mi monitor de 60 Hz. Sin embargo, en mi sistema de prueba, el script a continuación da como resultado un intervalo de 150 ms, que corresponde a 9 cuadros en un monitor de 60 Hz. Se trata de un retraso inesperado de 50 ms, o 3 cuadros, debido a la preparación de `canvas2`.

%--
código:
 id: LstStimPrepBad
 sintaxis: python
 fuente: stimulus-preparation-bad.py
 leyenda: "En este script, la duración entre `canvas1` y `canvas2` está confundida por el tiempo de preparación del estímulo."
--%

Ahora consideremos una variación simple del script anterior (%LstStimPrepGood). Esta vez, primero preparamos `canvas1` y `canvas2` y luego los presentamos. En mi sistema de prueba, esto da como resultado un intervalo constante de 100 ms, ¡tal como debería ser!

%--
código:
 id: LstStimPrepGood
 sintaxis: python
 fuente: stimulus-preparation-good.py
 leyenda: "En este script, la duración entre `canvas1` y `canvas2` no está confundida por el tiempo de preparación del estímulo."
--%

Al usar la interfaz gráfica, se aplican las mismas consideraciones, pero OpenSesame te ayuda automáticamente manejando la mayoría de la preparación del estímulo por adelantado. Sin embargo, debes tener en cuenta que esta preparación ocurre a nivel de elementos SEQUENCE y no a nivel de elementos LOOP. En términos prácticos, esto significa que el tiempo *dentro* de un SEQUENCE no se ve afectado por el tiempo de preparación del estímulo. Pero el tiempo *entre* SEQUENCE sí lo está.

Para hacer esto más concreto, consideremos la estructura que se muestra a continuación (%FigStimPrepBad). Supongamos que la duración del ítem SKETCHPAD está establecida en 95 ms, apuntando así a una duración de 100 ms, o 6 cuadros en un monitor de 60 Hz. En mi sistema de prueba, la duración real es de 133 ms, o 8 cuadros, debido a que el tiempo se ve afectado por la preparación del ítem SKETCHPAD, que ocurre cada vez que se ejecuta la secuencia. Entonces, este es un ejemplo de cómo *no* debes implementar partes críticas de tiempo en tu experimento.

figura:
 id: FigStimPrepBad
 fuente: stimulus-preparation-incorrect.png
 leyenda: "Un ejemplo de una estructura experimental en la que el tiempo entre presentaciones sucesivas de SKETCHPAD está confundido por el tiempo de preparación del estímulo. La secuencia de eventos en este caso es la siguiente: preparar SKETCHPAD (2 fotogramas), mostrar SKETCHPAD (6 fotogramas), preparar SKETCHPAD (2 fotogramas), mostrar SKETCHPAD (6 fotogramas), etc."

Ahora consideremos la estructura que se muestra a continuación (%FigStimPrepGood). Supongamos que la duración de `sketchpad1` se establece en 95 ms, apuntando así a un intervalo de 100 ms entre `sketchpad1` y `sketchpad2`. En este caso, ambos elementos se muestran como parte de la misma SECUENCIA y el tiempo no será confuso debido al tiempo de preparación del estímulo. En mi sistema de prueba, el intervalo real entre `sketchpad1` y `sketchpad2` es, de hecho, 100 ms o 6 fotogramas en un monitor de 60 Hz.

Tenga en cuenta que esto solo se aplica al intervalo entre `sketchpad1` y `sketchpad2`, porque se ejecutan en ese orden como parte de la misma secuencia. El intervalo entre `sketchpad2` en la ejecución *i* y `sketchpad1` en la ejecución *i+1* está nuevamente confundido por el tiempo de preparación del estímulo.

figura:
 id: FigStimPrepGood
 fuente: stimulus-preparation-correct.png
 leyenda: "Un ejemplo de una estructura experimental en la que el tiempo entre la presentación de `sketchpad1` y `sketchpad2` no está confundido por el tiempo de preparación del estímulo. La secuencia de eventos en este caso es la siguiente: preparar `sketchpad1` (2 fotogramas), preparar `sketchpad2` (2 fotogramas), mostrar `sketchpad1` (6 fotogramas), mostrar `sketchpad2` (6 fotogramas), preparar `sketchpad1` (2 fotogramas), preparar `sketchpad2` (2 fotogramas), mostrar `sketchpad1` (6 fotogramas), mostrar `sketchpad2` (6 fotogramas), etc."

Para obtener más información, consulte:

- [usage/prepare-run]

### Diferencias entre backends

OpenSesame no está vinculado a una forma específica de controlar la pantalla, el temporizador del sistema, etc. Por lo tanto, OpenSesame *per se* no tiene propiedades de tiempo específicas, porque estas dependen del backend que se utilice. Las características de rendimiento de los diversos backends no están perfectamente correlacionadas: Es posible que en algún sistema el backend [psycho] funcione mejor, mientras que en otro sistema el backend [xpyriment] funcione mejor. Por lo tanto, ¡una de las grandes cosas de OpenSesame es que puedes elegir qué backend funciona mejor para ti!

En general, los backends [xpyriment] y [psycho] son preferibles para experimentos críticos en el tiempo, porque utilizan un volteo bloqueante. Por otro lado, el backend [legacy] es un poco más estable y también considerablemente más rápido al usar [forms].

En circunstancias normales, los tres backends actuales de OpenSesame tienen las propiedades mostradas en %TblBackendInfo.

tabla:
 id: TblBackendInfo
 fuente: backend-info.csv
 leyenda: propiedades del backend.

Consulte también:

- [backends]

## Resultados de referencia y consejos para probar su propio sistema

### Comprobando si v-sync está habilitado

Como se describió en [Understanding your monitor], la presentación de una nueva pantalla debería coincidir idealmente con el inicio de un nuevo ciclo de actualización (es decir, 'v-sync'). Puede probar si este es el caso presentando pantallas de diferentes colores en rápida alternancia. Si v-sync no está habilitado, observará claramente líneas horizontales que atraviesan el monitor (es decir, 'desgarro'). Para realizar esta prueba, ejecute un experimento con el siguiente script en un elemento INLINE_SCRIPT (%LstVSync):

código:
 id: LstVSync
 sintaxis: python
 fuente: v-sync-check.py
 leyenda: Un script que presenta pantallas amarillas y azules en rápida alternancia. La falta de sincronización con la actualización vertical se puede observar como líneas horizontales que atraviesan el monitor.

### Pruebas de precisión y exactitud del tiempo

El tiempo es preciso o consistente cuando puedes presentar estímulos visuales una y otra vez con el mismo tiempo. Las marcas de tiempo son precisas cuando reflejan con precisión cuándo aparecen los estímulos visuales en el monitor. El siguiente script muestra cómo puedes verificar la precisión y exactitud del tiempo. Esta prueba se puede realizar tanto con como sin un fotodiodo externo, aunque el uso de un fotodiodo proporciona una verificación adicional.

Para simplificar, supongamos que tu monitor funciona a 100 Hz, lo que significa que un solo fotograma tarda 10 ms. El script presenta entonces un lienzo blanco durante 1 fotograma (10 ms). A continuación, el script presenta un lienzo negro durante 9 fotogramas (90 ms). Tenga en cuenta que hemos especificado una duración de 85, que se redondea como se explica en [Haciendo la fecha límite de actualización]. Por lo tanto, esperamos que el intervalo entre los inicios de dos pantallas blancas consecutivas sea de 10 fotogramas o 100 ms (= 10 ms + 90 ms).

Podemos utilizar dos formas de verificar si el intervalo entre dos pantallas blancas es efectivamente de 100 ms:

1. Usando las marcas de tiempo informadas por OpenSesame. Este es el método más fácil y generalmente es preciso cuando el backend utiliza un flip bloqueante.
2. Usando un fotodiodo que responde a los inicios de las pantallas blancas y registra las marcas de tiempo de estos inicios en una computadora externa. Esta es la mejor manera de verificar el tiempo, ya que no se basa en la introspección del software. Ciertos problemas, como el retraso de entrada de TFT, discutidos anteriormente, sólo se revelarán mediante la medición externa del fotodiodo.

Como puede ver, los backends [xpyriment] y [psycho] muestran constantemente un intervalo de 100 ms. Esto es bueno y tal como esperaríamos. Sin embargo, el backend [legacy] muestra un intervalo de 90 ms. Esta discrepancia se debe al hecho de que el backend [legacy] no utiliza un flip bloqueante (ver [Entendiendo su monitor]), lo que lleva a cierta imprevisibilidad en el tiempo de visualización. También cabe destacar que existe un acuerdo cercano entre las marcas de tiempo registradas por el fotodiodo externo y las marcas de tiempo informadas por OpenSesame. Este acuerdo demuestra que las marcas de tiempo de OpenSesame son confiables, aunque, nuevamente, son ligeramente menos confiables para el backend [legacy] debido a la falta de un flip bloqueante.

## Expyriment pruebas y conjunto de pruebas

Un conjunto de pruebas muy interesante está disponible en el sitio web de Expyriment. Esta información es aplicable a los experimentos de OpenSesame que utilizan el backend [xpyriment].

- <http://docs.expyriment.org/Timing.html>

Expyriment incluye un conjunto de pruebas muy útil. Puedes iniciar este conjunto de pruebas ejecutando el experimento de ejemplo `test_suite.opensesame` o agregando un INLINE_SCRIPT simple a tu experimento con las siguientes líneas de código (%LstExpyrimentTestSuite):

Para obtener más información, visite:

- <http://docs.expyriment.org/Testsuite.html>

## PsychoPy pruebas y información relacionada con el tiempo

Alguna información sobre el tiempo está disponible en el sitio de documentación de PsychoPy. Esta información es aplicable a los experimentos de OpenSesame que utilizan el backend [psycho].

- <http://www.psychopy.org/general/timing/timing.html>

[psycho]: /backends/xpyriment/
[xpyriment]: /backends/xpyriment/
[legacy]: /backends/legacy/
[miscellaneous/clock-drift]: /miscellaneous/clock-drift
[usage/prepare-run]: /usage/prepare-run
[backends]: /backends
[forms]: /forms