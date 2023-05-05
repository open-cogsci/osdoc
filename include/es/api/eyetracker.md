<div class="ClassDoc YAMLDoc" id="eyetracker" markdown="1">

# clase __eyetracker__

Una biblioteca genérica de Python para seguimiento ocular.

<div class="FunctionDoc YAMLDoc" id="eyetracker-calibrate" markdown="1">

## función __eyetracker.calibrar__()

Calibra el sistema de seguimiento ocular. El comportamiento real de esta
función depende del tipo de seguidor ocular y se describe a continuación.

__EyeLink:__

Esta función activará la pantalla de configuración de la cámara, que permite
ajustar la cámara y realizar un procedimiento de calibración/validación.
Al presionar 'q' saldrá de la rutina de configuración. Al presionar
'escape' primero se activará un cuadro de diálogo de confirmación y luego, tras
la confirmación, se generará una Excepción.

__EyeTribe:__

Activa una rutina de calibración simple.

__Devuelve:__

Devuelve Verdadero si la calibración tuvo éxito, o Falso si no; además, un registro de calibración se agrega al archivo de registro y se actualizan algunas propiedades (es decir, los umbrales para los algoritmos de detección).

- Tipo: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-close" markdown="1">

## función __eyetracker.cerrar__()

Cierra ordenadamente la conexión con el rastreador. Guarda los datos y establece
`self.connected` en Falso.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-connected" markdown="1">

## función __eyetracker.conectado__()

Verifica si el rastreador está conectado.

__Devuelve:__

Verdadero si la conexión está establecida, Falso si no; establece
`self.connected` en el mismo valor.

- Tipo: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_calibration_target" markdown="1">

## función __eyetracker.dibujar_objetivo_de_calibración__(x, y)

Dibuja un objetivo de calibración.

__Argumentos:__

- `x` -- La coordenada X
	- Tipo: int
- `y` -- La coordenada Y
	- Tipo: int

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-draw_drift_correction_target" markdown="1">

## función __eyetracker.dibujar_objetivo_de_corrección_de_deriva__(x, y)

Dibuja un objetivo de corrección de deriva.

__Argumentos:__

- `x` -- La coordenada X
	- Tipo: int
- `y` -- La coordenada Y
	- Tipo: int

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-drift_correction" markdown="1">

## función __eyetracker.corrección_de_deriva__(pos=None, fix\_triggered=False)

Realiza un procedimiento de corrección de deriva. El comportamiento exacto de esta
función en el tipo de seguidor ocular se describe a continuación. Debido a que
la corrección de deriva puede fallar, generalmente llamará a esta función en
un bucle.

__EyeLink:__

Presionar 'q' durante la corrección de deriva activará la pantalla de configuración
de la cámara. Desde allí, presionar 'q' nuevamente hará que la corrección de deriva
falle inmediatamente. Presionar 'escape' dará la opción de abortar
el experimento, en cuyo caso se genera una Excepción.

__Palabras clave:__

- `pos` -- posición (x, y) del punto de fijación o Ninguna para una fijación central.
	- Tipo: tupla, NoneType
	- Predeterminado: None
- `fix_triggered` -- Booleano que indica si la verificación de deriva se debe realizar en función de la posición de la mirada (Verdadero) o espacio presionado (Falso).
	- Tipo: bool
	- Predeterminado: False

__Devuelve:__

Un booleano que indica si la verificación de deriva está bien (Verdadero) o no (Falso).

- Tipo: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-fix_triggered_drift_correction" markdown="1">

## función __eyetracker.corrección_de_deriva_activada_por_fijación__(pos=None, min\_samples=30, max\_dev=60, reset\_threshold=10)

Realiza una corrección de deriva activada por fijación al recopilar
un número de muestras y calcular la distancia media desde la posición de
fijación

__Palabras clave:__

- `pos` -- posición (x, y) del punto de fijación o Ninguna para una fijación central.
	- Tipo: tupla, NoneType
	- Predeterminado: None
- `min_samples` -- La cantidad mínima de muestras después de las cuales se calcula una desviación media.
	- Tipo: int
	- Predeterminado: 30
- `max_dev` -- La desviación máxima de la fijación en píxeles.
	- Tipo: int
	- Predeterminado: 60
- `reset_threshold` -- Si la distancia horizontal o vertical en píxeles entre dos muestras consecutivas es mayor que este umbral, la colección de muestras se reinicia.
	- Tipo: int
	- Predeterminado: 10

__Devoluciones:__

Un booleano que indica si la verificación de deriva está bien (True) o no (False).

- Tipo: bool

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-get_eyetracker_clock_async" markdown="1">

## función __eyetracker\.get\_eyetracker\_clock\_async__\(\)

Devuelve la diferencia entre el tiempo del rastreador y el tiempo de PyGaze, que se puede utilizar para sincronizar el tiempo

__Devoluciones:__

La diferencia entre el tiempo del rastreador de ojos y el tiempo de PyGaze.

- Tipo: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log" markdown="1">

## función __eyetracker\.log__\(msg\)

Escribe un mensaje en el archivo de registro.

__Argumentos:__

- `msg` -- Un mensaje.
	- Tipo: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-log_var" markdown="1">

## función __eyetracker\.log\_var__\(var, val\)

Escribe el nombre y valor de una variable en el archivo de registro

__Argumentos:__

- `var` -- Un nombre de variable.
	- Tipo: str, unicode
- `val` -- Un valor de variable

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-pupil_size" markdown="1">

## función __eyetracker\.pupil\_size__\(\)

Devuelve la muestra de tamaño de pupila más reciente; el tamaño puede medirse como el diámetro o el área de la pupila, dependiendo de su configuración (tenga en cuenta que el tamaño de la pupila en su mayoría se proporciona en unidades arbitrarias).

__Devoluciones:__

Devuelve el tamaño de la pupila para el ojo que se está rastreando actualmente (según lo especificado por self.eye_used) o -1 cuando no se pueden obtener datos.

- Tipo: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-sample" markdown="1">

## función __eyetracker\.sample__\(\)

Devuelve la posición de mirada más reciente disponible.

__Devoluciones:__

Una tupla (x, y) o una (-1, -1) en caso de error.

- Tipo: tupla

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-send_command" markdown="1">

## función __eyetracker\.send\_command__\(cmd\)

Envía directamente un comando al rastreador de ojos (no compatible con todas las marcas; podría producir un mensaje de advertencia si su configuración no admite comandos directos).

__Argumentos:__

- `cmd` -- El comando que se enviará al rastreador de ojos.
	- Tipo: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_detection_type" markdown="1">

## función __eyetracker\.set\_detection\_type__\(eventdetection\)

Establece el tipo de detección de eventos en algoritmos PyGaze u
algoritmos nativos proporcionados por el fabricante (solo si
disponibles: el tipo de detección predeterminará a PyGaze si no hay funciones nativas
disponibles)

__Argumentos:__

- `eventdetection` -- Una cadena que indica qué tipo de detección
debe emplearse: 'pygaze' para
Algoritmos de detección de eventos PyGaze o
'nativo' para algoritmos de fabricantes (solo
si está disponible; predeterminará a 'pygaze' si no
la detección de eventos nativos está disponible)
	- Tipo: str, unicode

__Devoluciones:__

Tipo de detección para sacudidas, fijaciones y parpadeos en una tupla, por ejemplo ('pygaze','native','native') cuando se pasó 'native', pero la detección nativa no estaba disponible para la detección de sacudidas.

- Tipo: tupla

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_calibration_target_func" markdown="1">

## función __eyetracker\.set\_draw\_calibration\_target\_func__\(func\)

Especifica una función personalizada para dibujar el objetivo de calibración. Esta función anulará el [draw_calibration_target] predeterminado.

__Argumentos:__

- `func` -- La función para dibujar un objetivo de calibración. Esta función debe aceptar dos parámetros, para las coordenadas x e y del objetivo.
	- Tipo: función

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_draw_drift_correction_target_func" markdown="1">

## función __eyetracker\.set\_draw\_drift\_correction\_target\_func__\(func\)

Especifica una función personalizada para dibujar el objetivo de corrección de deriva. Esta función anulará el [draw_drift_correction_target] predeterminado.

__Argumentos:__

- `func` -- La función para dibujar un objetivo de corrección de deriva. Esta función debe aceptar dos parámetros, para las coordenadas x e y del objetivo.
	- Tipo: función

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-set_eye_used" markdown="1">

## función __eyetracker.set_eye_used__()

Registra la variable `eye_used`, según el ojo especificado (si se rastrean ambos ojos, se utiliza el ojo izquierdo). No devuelve nada.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-start_recording" markdown="1">

## función __eyetracker.start_recording__()

Comienza la grabación. Establece `self.recording` en `True` cuando la grabación se inicia con éxito.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-status_msg" markdown="1">

## función __eyetracker.status_msg__(msg)

Envía un mensaje de estado al rastreador ocular, que se muestra en la GUI del rastreador (solo disponible para configuraciones de EyeLink).

__Argumentos:__

- `msg` -- Una cadena que se mostrará en la PC del experimentador,
por ejemplo: "ensayo actual: %d" % trialnr.
	- Tipo: str, unicode

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-stop_recording" markdown="1">

## función __eyetracker.stop_recording__()

Detiene la grabación. Establece `self.recording` en `False` cuando la grabación se detiene con éxito.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_end" markdown="1">

## función __eyetracker.wait_for_blink_end__()

Espera el final de un parpadeo y devuelve el tiempo de finalización del parpadeo.
Detección basada en Dalmaijer et al. (2013) si EVENTDETECTION está configurado
para 'pygaze', o utilizando funciones de detección nativas si EVENTDETECTION
está configurado para 'nativo' (NOTA: ¡no todos los sistemas tienen funcionalidad nativa;
volverá a ;pygaze' si 'native' no está disponible!)

__Devuelve:__

Tiempo de finalización del parpadeo en milisegundos, medido desde el inicio del experimento.

- Tipo: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_blink_start" markdown="1">

## función __eyetracker.wait_for_blink_start__()

Espera el inicio de un parpadeo y devuelve el tiempo de inicio del parpadeo.
Detección basada en Dalmaijer et al. (2013) si EVENTDETECTION está configurado
para 'pygaze', o utilizando funciones de detección nativas si EVENTDETECTION
está configurado para 'nativo' (NOTA: ¡no todos los sistemas tienen funcionalidad nativa;
volverá a ;pygaze' si 'native' no está disponible!)

__Devuelve:__

Tiempo de inicio del parpadeo en milisegundos, medido desde el inicio del experimento

- Tipo: int, float

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_event" markdown="1">

## función __eyetracker.wait_for_event__(event)

Espera un evento.

__Argumentos:__

- `event` -- Un código de evento entero, uno de los siguientes:

- 3 = STARTBLINK
- 4 = ENDBLINK
- 5 = STARTSACC
- 6 = ENDSACC
- 7 = STARTFIX
- 8 = ENDFIX
	- Tipo: int

__Devuelve:__

Se llama a un método `self.wait_for_*`, según el evento especificado; se devuelve el valor de retorno del método correspondiente.

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_end" markdown="1">

## función __eyetracker.wait_for_fixation_end__()

Devuelve el tiempo y la posición de la mirada cuando termina una fijación;
la función supone que una 'fijación' ha terminado cuando se detecta una desviación
de más de self.pxfixtresh desde la posición inicial de fijación (self.pxfixtresh se crea en self.calibration,
basado en self.fixtresh, una propiedad definida en self.__init__).
Detección basada en Dalmaijer et al. (2013) si EVENTDETECTION está configurado
para 'pygaze', o utilizando funciones de detección nativas si EVENTDETECTION
está configurado para 'nativo' (NOTA: ¡no todos los sistemas tienen funcionalidad nativa;
volverá a ;pygaze' si 'native' no está disponible!)

__Devuelve:__

Una tupla `time, gazepos`. Time es el tiempo final en milisegundos (desde expstart), gazepos es una tupla de posición de la mirada (x,y) de la posición desde la cual se inició la fijación.

- Tipo: tupla

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_fixation_start" markdown="1">

## función __eyetracker.wait_for_fixation_start__()

Devuelve el tiempo de inicio y posición cuando comienza una fijación;
la función asume que una 'fijación' ha comenzado cuando la posición de la mirada
permanece razonablemente estable (es decir, cuando la mayoría de las muestras más desviadas se encuentran
dentro de self.pxfixtresh) durante cinco muestras seguidas (self.pxfixtresh
se crea en self.calibration, basado en self.fixtresh, una propiedad
definida en self.__init__).
Detección basada en Dalmaijer et al. (2013) si EVENTDETECTION está configurado
en 'pygaze' o utilizando funciones de detección nativas si EVENTDETECTION
está configurado en 'native' (NOTA: ¡no todos los sistemas tienen funcionalidad nativa;
volverá a 'pygaze' si 'native' no está disponible!)

__Devuelve:__

Una tupla `tiempo, gazepos`. El tiempo es el tiempo de inicio en milisegundos (desde expstart), gazepos es una tupla de posición de la mirada (x,y) desde la cual se inició la fijación.

- Tipo: tupla

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_end" markdown="1">

## función __eyetracker\.wait\_for\_saccade\_end__\(\)

Devuelve el tiempo de finalización, la posición inicial y final cuando termina un sacádico;
basado en el algoritmo de detección de sacádicos en línea de Dalmaijer et al. (2013) si EVENTDETECTION está configurado en 'pygaze', o utilizando funciones de detección nativas si EVENTDETECTION está configurado en 'native' (NOTA: no todos los sistemas tienen funcionalidad nativa; volverá a 'pygaze' si 'native' no está disponible!)

__Devuelve:__

Una tupla de `endtime, startpos, endpos`. Endtime en milisegundos (desde expbegintime); startpos y endpos son tuplas de posición de la mirada (x,y).

- Tipo: tupla

</div>

<div class="FunctionDoc YAMLDoc" id="eyetracker-wait_for_saccade_start" markdown="1">

## función __eyetracker\.wait\_for\_saccade\_start__\(\)

Devuelve el tiempo de inicio y la posición inicial cuando comienza un sacádico;
basado en el algoritmo de detección de sacádicos en línea de Dalmaijer et al. (2013) si EVENTDETECTION está configurado en 'pygaze', o utilizando funciones de detección nativas si EVENTDETECTION está configurado en 'native' (NOTA: no todos los sistemas tienen funcionalidad nativa; volverá a 'pygaze' si 'native' no está disponible!)

__Devuelve:__

Una tupla de `endtime, startpos`. Endtime en milisegundos (desde expbegintime); startpos es una tupla de posición de la mirada (x,y).

- Tipo: tupla

</div>

</div>