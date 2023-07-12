title: OpenSesame as a Python library (no GUI)

You can also write experiments fully programmatically by using OpenSesame as a Python module. This is mainly suited for people who prefer coding over using a graphical user interface.

Using OpenSesame as a Python module works much the same way as using Python `inline_script` items in the user interface, with two notable exceptions:

- Functions and classes need to be explicitly imported from `libopensesame.python_workspace_api`. All functions and classes described under [Common functions](%url:manual/python/common%) are available.
- An `experiment` object needs to be explicitly created using the `Experiment()` factory function.

A simple Hello World experiment looks like this:

```python
from libopensesame.python_workspace_api import \
  Experiment, Canvas, Keyboard, Text

# Initialize the experiment window using the legacy backend
exp, win, clock, log = Experiment(canvas_backend='legacy')
# Prepare a stimulus canvas and a keyboard
cnv = Canvas()
cnv += Text('Hello world')
kb = Keyboard()
# Show the canvas, wait for a key press, and then end the experiment
cnv.show()
kb.get_key()
exp.end()
```

You can also programmatically open a `.osexp` experiment file and execute it:

```python
from libopensesame.python_workspace_api import Experiment
exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp',
                                  subject_nr=2)
exp.run()
```
