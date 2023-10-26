title: Puerto paralelo (disparadores EEG)
reviewed: false
hash: 173d67c1a3fbe4fb17b8a936fe30584d71443f518bf86bd65c9ad6da21c4e229
locale: es
language: Spanish

En los estudios EEG/ERP es común enviar disparadores para marcar el intervalo de tiempo para eventos significativos (por ejemplo, el inicio de un ensayo, la presentación de un estímulo particular, etc.). Los disparadores suelen ser bytes que se envían a través del puerto paralelo al aparato EEG.

[TOC]


## Usando el plugin `parallel_port_trigger`

Parallel_port_trigger es un plugin de terceros y no está mantenido por el equipo de OpenSesame.
{: .page-notification}

Un plugin de OpenSesame para enviar disparadores de sincronización de estímulos a través del puerto paralelo a sistemas de adquisición de datos.

- <https://github.com/dev-jam/opensesame-plugin-parallel_port_trigger/>

Puede instalar el plugin `parallel_port_trigger` desde PyPi:

```
pip install pip install opensesame-plugin-parallel-port-trigger
```


## Usando `dportio.dll` en un Script Python inline (solo para Windows)

En lugar de usar el plugin `parallel_port_trigger`, también es posible enviar disparadores con `dlportio.dll` a través de un script Python inline. Este método solo sirve para Windows. Para hacerlo, primero agregue un INLINE_SCRIPT al inicio del experimento con el siguiente código en la fase de preparación:

~~~ .python
try:
	from ctypes import windll
	global io
	io = windll.dlportio # requires dlportio.dll !!!
except:
	print('El puerto paralelo no pudo ser abierto')
~~~

Esto cargará `dlportio.dll` como un objeto global llamado `io`. Nota que un fallo no colapsará el experimento, así que asegúrate de verificar la ventana de depuración para los mensajes de error!

Ahora utilice el siguiente código en un INLINE_SCRIPT en cualquier parte del experimento para enviar un disparador:

~~~ .python
global io
disparador = 1
puerto = 0x378
try:
	io.DlPortWritePortUchar(puerto, disparador)
except:
	print('¡Falló el envío del disparador!')
~~~

Nota que este envía el disparador 1 al puerto 0x378 (=888). Cambie estos valores de acuerdo a su configuración.

## Obteniendo acceso al puerto paralelo

### Linux

En Linux usamos el módulo `parport_pc` (probado en Debian Wheezy) y necesitamos proporcionarnos permisos para hacerlo. Podemos lograr esto ejecutando los siguientes comandos:

	sudo rmmod lp
	sudo rmmod parport_pc
	sudo modprobe parport_pc
	sudo adduser [usuario] lp

Aquí, `[usuario]` debe ser reemplazado por su nombre de usuario. Después, cierre sesión e ingrese de nuevo, ¡y estará listo para empezar!

### Windows XP y Windows Vista (32 bit)

1. Descargue el controlador DLPortIO de 32 bits desde [aquí][win32-dll] y descomprima el archivo zip.
2. Vaya a la carpeta `DriverLINX/drivers` y copie `dlportio.dll` y `dlportio.sys` a la carpeta `install`. Esta es la carpeta donde se encuentra `install.exe`. Luego ejecute `install.exe`
3. Necesita copiar `dlportio.dll` en la carpeta de OpenSesame (es decir, la misma carpeta que contiene `opensesame.exe`).

### Windows 7 (32 y 64 bit)

1. Descarga el controlador DLPortIO de 32 bits o 64 bits [aquí][win7-dll] y descomprime el archivo zip.
2. Como Windows 7 tiene un sistema de seguridad reforzado (al menos en comparación con XP), no se puede instalar simplemente el controlador DLPortIO. Esto no funcionará, ya que Windows 7 bloqueará todos los intentos de instalar un controlador no oficialmente firmado (por Microsoft). Bueno para la seguridad de un usuario promedio, pero malo para nosotros. Para eludir esta restricción, se debe utilizar un pequeño programa llamado "Digital Signature Enforcement Overrider" (DSEO), que se puede descargar [aquí][dseo] (por supuesto, hay otras formas posibles de hacer esto, pero este programa se menciona en el archivo `readme.txt` de DLPortIO y no es necesario profundizar en las especialidades de la arquitectura de MS Windows 7).
3. Inicie DSEO con privilegios de administrador (haga clic derecho en `dseo13b.exe`, seleccione "Ejecutar como administrador"). Ahora aparece la ventana de DSEO. Solo presenta una lista de opciones de qué operación ejecutar a continuación.
4. Elija la opción "firmar driver/sys-file" y presione ok. Ahora aparece otra ventana donde debe escribir la ruta absoluta al archivo `DLPortIO.sys` (solo este, ¡no el dll!). Recuerde escapar de los espacios en la ruta si tiene alguno (no pregunte cuánto tiempo me llevó) de lo contrario, sus archivos no se encontrarán. Al presionar ok, se firmará el archivo sys.
5. De vuelta en la lista de DSEO, elija "habilitar modo de prueba" y presione ok. Luego elija "salir" y reinicie su PC. Windows 7 se queja incorrectamente de que DSEO podría no estar instalado correctamente; simplemente haga clic en "sí, el software está instalado correctamente".
6. Después de completar el inicio, verá que algo como "Windows 7 test mode built #número#" está escrito en el escritorio justo encima del reloj en la barra de inicio. Eso es necesario. Debes estar en modo de prueba para ejecutar este controlador con firma no oficial.
7. Ahora ejecute `DLPortIO_install.bat` con privilegios de administrador (en Windows Explorer, haga clic derecho en el archivo, ...). Responde "sí" si Windows te advierte sobre los cambios en el registro.
8. Reiniciar.
9. Copie `DLPortIO.dll` en la carpeta Opensesame, es decir, la misma carpeta que contiene `opensesame.exe`.

Fuente: [Publicación del foro por Absurd][post-3]

## Recomendaciones

- Comience su experimento con un disparador 'cero' para asegurarse de que todos los pines estén en cero.
- Se recomienda utilizar los backends [psycho] o [xpyriment] en lugar del backend [legacy] (usando PyGame) para experimentos críticos en tiempo. Esto se debe a que [psycho] y [xpyriment] tienen en cuenta la frecuencia de actualización del monitor al devolver marcas de tiempo, mientras que [legacy] no lo hace. Para obtener más información, consulte [miscellaneous/timing].
- Envíe el código de disparo justo después (en lugar de justo antes) de la presentación de su estímulo (suponiendo que es el inicio del estímulo que desea marcar). Al hacerlo, se asegurará de que la marca de tiempo sea lo más precisa posible y no sufrirá de una pequeña fluctuación aleatoria debido a la frecuencia de actualización de su monitor. [Fuente: lvanderlinden][post-2]

## Solución de problemas

Hay una serie de temas relevantes del foro en los que se discuten (y, en su mayoría, resuelven) problemas relacionados con el disparador.

- Una publicación sobre disparadores fantasma, es decir, disparadores no deseados que misteriosamente son registrados por el aparato EEG: [enlace][post-2]
- Una publicación con instrucciones detalladas de instalación para DLPortIO en Windows 7 ([Fuente: absurd][post-3]).

No dude en publicar preguntas en el foro o en informarnos de sus experiencias (buenas o malas).

[win32-dll]: http://files.cogsci.nl/misc/dlportio.zip
[win7-dll]: http://real.kiev.ua/avreal/download/#DLPORTIO_TABLE
[dseo]: http://www.ngohq.com/home.php?page=dseo
[post-2]: http://forum.cogsci.nl/index.php?p=/discussion/comment/780#Comment_780
[post-3]: http://forum.cogsci.nl/index.php?p=/discussion/comment/745#Comment_745
[miscellaneous/timing]: /miscellaneous/timing
[legacy]: /backends/legacy
[xpyriment]: /backends/xpyriment
[psycho]: /backends/psycho