title: PyGaze (seguimiento ocular)
hash: 80766dbbeccf44569af795eddea4817ca3fd7e30726a50587814ffbfd94c5c8a
locale: es
language: Spanish

[TOC]

## Acerca de

PyGaze es una biblioteca Python para seguimiento ocular. Un conjunto de complementos te permiten utilizar PyGaze dentro de OpenSesame. Para obtener más información sobre PyGaze, visita:

- <http://www.pygaze.org/>

Por favor, cita PyGaze como:

Dalmaijer, E., Mathôt, S., & Van der Stigchel, S. (2014). PyGaze: An open-source, cross-platform toolbox for minimal-effort programming of eyetracking experiments. *Behavior Research Methods*. doi:10.3758/s13428-013-0422-2
{: .reference}

## Eye trackers compatibles

PyGaze es compatible con los siguientes eye trackers:

- [EyeLink](%link:eyelink%)
- [EyeTribe](%link:eyetribe%)

Para los siguientes eye trackers, hay soporte experimental:

- [EyeLogic](%link:eyelogic%)
- [GazePoint / OpenGaze](%link:gazepoint%)
- [SMI](%link:smi%)
- [Tobii](%link:tobii%)

También puedes realizar seguimiento ocular básico en experimentos en línea con WebGazer.js:

- [WebGazer.js](%link:webgazer%)

PyGaze también incluye dos eye trackers simulados para propósitos de prueba:

- __Simple dummy__ — No hace nada.
- __Advanced dummy__ — Simulación de movimientos oculares con el mouse.

## Instalando PyGaze

### Windows

Si usas el paquete oficial de Windows de OpenSesame, PyGaze ya está instalado.

### Ubuntu

Si utilizas Ubuntu, puedes obtener PyGaze desde el PPA de Cogsci.nl:

```
sudo add-apt-repository ppa:smathot/cogscinl
sudo apt-get update
sudo apt-get install python-pygaze
```

O, si está utilizando Python 3, cambia el último comentario a:

```
sudo apt-get install python3-pygaze
```

## pip install (todas las plataformas)

Puedes instalar PyGaze con `pip`:

```
pip install python-pygaze
```

### Anaconda (todas las plataformas)

```
conda install python-pygaze -c cogsci
```

## Complementos de PyGaze para OpenSesame

Los siguientes complementos de PyGaze están disponibles:

- PYGAZE_INIT — Inicializa PyGaze. Este complemento se inserta generalmente al inicio del experimento.
- PYGAZE_DRIFT_CORRECT — Implementa un procedimiento de corrección de desplazamiento.
- PYGAZE_START_RECORDING — Pone a PyGaze en modo de grabación.
- PYGAZE_STOP_RECORDING — Saca a PyGaze del modo de grabación.
- PYGAZE_WAIT — Pausa hasta que ocurra un evento, como el inicio de un sacádico.
- PYGAZE_LOG — Registra variables experimentales y texto arbitrario.

## Ejemplo

Para ver un ejemplo de cómo utilizar los complementos de PyGaze, consulta la plantilla de PyGaze incluida en OpenSesame.

A continuación se muestra un ejemplo de cómo utilizar PyGaze en un INLINE_SCRIPT de Python:

~~~ .python
# Crea un objeto de teclado y un objeto de lienzo
my_keyboard = Keyboard(timeout=0)
my_canvas = Canvas()
my_canvas['dot'] = Circle(x=0, y=0, r=10, fill=True)
# Bucle...
while True:
	# ... hasta que se presione la barra espaciadora
	key, timestamp = my_keyboard.get_key()
	if key == 'space':
		break
	# Obtiene la posición de la mirada de pygaze ...
	x, y = eyetracker.sample()
	# ... ¡y dibuja un punto de fijación dependiente de la mirada!
	my_canvas['dot'].x = x + my_canvas.left
	my_canvas['dot'].y = y + my_canvas.top
	my_canvas.show()
~~~

## Resumen de funciones

Para inicializar PyGaze en OpenSesame, inserta el complemento PYGAZE_INIT en tu experimento. Una vez que hayas hecho esto, un objeto `eyetracker` estará disponible, que ofrece las siguientes funciones:

%-- include: include/api/eyetracker.md --%