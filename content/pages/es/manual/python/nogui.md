title: OpenSesame como una biblioteca Python (sin GUI)
hash: f402b6dd5bcb95ef27e11fded05dd0fb27ec738f984dad3ea0c2ccc950ffbe1e
locale: es
language: Spanish

También puedes escribir experimentos completamente de forma programática usando OpenSesame como un módulo de Python. Esto es principalmente adecuado para personas que prefieren la codificación en lugar de usar una interfaz gráfica de usuario.

Usar OpenSesame como un módulo de Python funciona de manera muy similar a usar elementos de `inline_script` de Python en la interfaz de usuario, con dos excepciones notables:

- Las funciones y clases deben ser importadas explícitamente desde `libopensesame.python_workspace_api`. Todas las funciones y clases descritas en [Funciones comunes](%url:manual/python/common%) están disponibles.
- Un objeto `experiment` debe ser creado explícitamente utilizando la función de fábrica `Experiment()`.

Un experimento simple de Hello World se ve así:

```python
from libopensesame.python_workspace_api import \
  Experiment, Canvas, Keyboard, Text

# Inicializar la ventana del experimento usando el backend legacy
exp, win, clock, log = Experiment(canvas_backend='legacy')
# Preparar un lienzo de estímulo y un teclado
cnv = Canvas()
cnv += Text('Hola mundo')
kb = Keyboard()
# Mostrar el lienzo, esperar una presión de tecla y luego terminar el experimento
cnv.show()
kb.get_key()
exp.end()
```

También puedes abrir un archivo de experimento `.osexp` de forma programática y ejecutarlo:

```python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='mi_experimento.osexp',
                                  subject_nr=2)
exp.run()
```