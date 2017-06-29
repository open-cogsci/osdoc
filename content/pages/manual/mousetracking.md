title: Mouse tracking

Mousetrap is a third-party plugin, and is not maintained by the OpenSesame team.
{: .alert .alert-info}

## About

Pascal Kieslich and Felix Henninger have developed the [mousetrap plugins](https://github.com/PascalKieslich/mousetrap-os) for OpenSesame [(Kieslich & Henninger, in press)](https://dx.doi.org/10.3758/s13428-017-0900-z). These plugins allow you to track the movement of the mouse cursor, which has been used to investigate the time course of cognitive processes in many psychological domains [(Freeman, Dale, & Farmer, 2011)](https://dx.doi.org/10.3389/fpsyg.2011.00059).

Mousetrap offers two plugins for mouse tracking in OpenSesame that can be included in the experiment via drag-and-drop.
The [mousetrap response plugin](https://github.com/PascalKieslich/mousetrap-os/blob/master/plugins/mousetrap_response/mousetrap_response.md) tracks mouse movements while another stimulus (e.g., a sketchpad) is shown, analogous to a keyboard or mouse response item.
The [mousetrap form plugin](https://github.com/PascalKieslich/mousetrap-os/blob/master/plugins/mousetrap_form/mousetrap_form.md) allows for tracking of mouse movements in [custom forms](%link:manual/forms/custom%).
Besides, both plugins also provide Python classes, which can be used in Python inline scripts for maximum customizability.

Once data have been collected with the plugins, the data can be processed, analyzed and visualized using the [mousetrap R package](https://github.com/PascalKieslich/mousetrap).

## Installation

Mousetrap is available [on the Python Package Index](https://pypi.python.org/pypi/opensesame-plugin-mousetrap). To install the latest release, please run the following commands in the OpenSesame [debug window](%link:manual/interface%):

~~~ .python
import pip
pip.main(['install', 'opensesame-plugin-mousetrap'])
~~~

You can also download the latest release of the plugins from the [GitHub release page](https://github.com/PascalKieslich/mousetrap-os/releases). More information about each plugin can be found in its respective helpfiles (linked above). A number of example experiments that demonstrate the basic features are available in the [examples folder](https://github.com/PascalKieslich/mousetrap-os/tree/master/examples#example-experiments) on GitHub.


See also:

- %link:environment%
