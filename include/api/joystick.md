<div class="ClassDoc YAMLDoc" markdown="1">

# instance __joystick__

If you insert the JOYSTICK plugin at the start of your experiment, a
JOYSTICK object automatically becomes part of the experiment object
and can be used within an INLINE_SCRIPT item as `joystick`.

{% set arg_joybuttonlist = "A list of buttons that are accepted or " +
"`None` to accept all buttons." %}
{% set arg_timeout = "A timeout value in milliseconds or `None` for no " +
"timeout." %}

[TOC]

## flush(self)

Clears all pending input, not limited to the joystick.



__Returns__

- True if joyinput was pending (i.e., if there was something to
flush) and False otherwise.


## get_joyaxes(timeout=None)

Waits for joystick axes movement.


__Parameters__

- **timeout**: A timeout value in milliseconds or `None` to use default timeout.

__Returns__

- A `(position, timestamp)` tuple. `position` is `None` if a timeout
occurs. Otherwise, `position` is an `(x, y, z)` tuple.


## get_joyballs(timeout=None)

Waits for joystick trackball movement.


__Parameters__

- **timeout**: A timeout value in milliseconds or `None` to use default timeout.

__Returns__

- A `(position, timestamp)` tuple. The position is `None` if a
timeout occurs.


## get_joybutton(joybuttonlist=None, timeout=None)

Collects joystick button input.


__Parameters__

- **joybuttonlist**: A list of buttons that are accepted or `None` to default
joybuttonlist.
- **timeout**: A timeout value in milliseconds or `None` to use default timeout.

__Returns__

- A (joybutton, timestamp) tuple. The joybutton is `None` if a
timeout occurs.


## get_joyhats(timeout=None)

Waits for joystick hat movement.


__Parameters__

- **timeout**: A timeout value in milliseconds or `None` to use default timeout.

__Returns__

- A `(position, timestamp)` tuple. `position` is `None` if a timeout
occurs. Otherwise, `position` is an `(x, y)` tuple.


## get_joyinput(joybuttonlist=None, timeout=None)

Waits for any joystick input (buttons, axes, hats or balls).


__Parameters__

- **joybuttonlist**: A list of buttons that are accepted or `None` to default
joybuttonlist.
- **timeout**: A timeout value in milliseconds or `None` to use default timeout.

__Returns__

- A (event, value, timestamp) tuple. The value is `None` if a timeout
occurs. `event` is one of `None`, 'joybuttonpress',
'joyballmotion', 'joyaxismotion', or 'joyhatmotion'


## input_options(self)

Generates a list with the number of available buttons, axes, balls
and hats.



__Returns__

- A list with number of inputs as: [buttons, axes, balls,
hats].


## set_joybuttonlist(joybuttonlist=None)

Sets a list of accepted buttons.


__Parameters__

- **joybuttonlist**: {{arg_joybuttonlist}}


## set_timeout(timeout=None)

Sets a timeout.


__Parameters__

- **timeout**: {{arg_timeout}}


</div>

