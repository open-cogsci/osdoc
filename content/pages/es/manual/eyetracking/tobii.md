title: Tobii
hash: b29e3b34f4a2f2600b95bc2d17497c21e352fb3a5834b0f4061bd6cd27e4e3dd
locale: es
language: Spanish

## Instalación de Tobii research

`tobii-research` es la biblioteca de Python para el soporte de Tobii. Actualmente, `tobii-research` solo es compatible con Python 3.10 y anteriores, mientras que los paquetes estándar de OpenSesame están construidos con Python 3.13. Por lo tanto, debes usar el paquete de OpenSesame para Python 3.10 (o anterior) desde [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases).

Luego, se puede instalar `tobii-research`:

```
pip install tobii-research
```

Para más información, consulta:

- <http://www.tobii.com/en/eye-tracking-research/global/>


## PyGaze

Después de instalar `tobii-research`, ¡puedes utilizar Tobii con PyGaze! Consulta:

- %link:pygaze%


## Plugin de seguimiento ocular Titta

Bob Rosbag, Diederick C. Niehorster y Marcus Nyström han desarrollado sus propios plugins de Tobii para OpenSesame. Estos son algo similares a los plugins de PyGaze, pero ofrecen algunas funcionalidades que no están disponibles a través de PyGaze, y también pueden ser más estables. Para instalar estos plugins, ejecuta:

```
pip install opensesame-plugin-titta-eyetracking
```

Para más información, visita:

- <https://github.com/dev-jam/opensesame-plugin-titta_eyetracking>