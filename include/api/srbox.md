<div class="ClassDoc YAMLDoc" id="srbox" markdown="1">

# class __srbox__

If you insert the srbox plugin at the start of your experiment, an
instance of `srbox` automatically becomes part of the experiment
object and can be accessed within an inline_script item as `srbox`.

__Important note 1:__

If you do not specify a device, the plug-in will try to autodetect the
SR Box port. However, on some systems this freezes the experiment, so
it is better to explicitly specify a device.

__Important note 2:__

You need to call [srbox.start] to put the SR Box in sending mode,
before calling [srbox.get_button_press] to collect a button press.

__Example:__

~~~ .python
t0 = clock.time()
srbox.start()
button, t1 = srbox.get_button_press(allowed_buttons=[1,2],
        require_state_change=True)
if button == 1:
        response_time = t1 - t0
        print('Button 1 was pressed in %d ms!' % response_time)
srbox.stop()
~~~

<div class="FunctionDoc YAMLDoc" id="srbox-__init__" markdown="1">

## function __srbox\.\_\_init\_\___\(experiment, dev=None\)

Constructor. An `srbox` object is created automatically by the `srbox` plug-in, and you do not generally need to call the constructor yourself.

__Arguments:__

- `experiment` -- An Opensesame experiment.
	- Type: experiment

__Keywords:__

- `dev` -- No description
	- Default: None

</div>

[srbox.__init__]: #srbox-__init__
[__init__]: #srbox-__init__

<div class="FunctionDoc YAMLDoc" id="srbox-close" markdown="1">

## function __srbox\.close__\(\)

Closes the connection to the srbox. This is done automatically by the `srbox` plugin when the experiment finishes.

</div>

[srbox.close]: #srbox-close
[close]: #srbox-close

<div class="FunctionDoc YAMLDoc" id="srbox-get_button_press" markdown="1">

## function __srbox\.get\_button\_press__\(allowed\_buttons=None, timeout=None, require\_state\_change=False\)

Collects a button press from the SR box.

__Keywords:__

- `allowed_buttons` -- A list of buttons that are accepted or `None` to accept all buttons. Valid buttons are integers 1 through 8.
	- Type: list, NoneType
	- Default: None
- `timeout` -- A timeout value in milliseconds or `None` for no timeout.
	- Type: int, float, NoneType
	- Default: None
- `require_state_change` -- Indicates whether already pressed button should be accepted (False), or whether only a state change from unpressed to pressed is accepted (True).
	- Default: False

__Returns:__

A button_list, timestamp tuple. button_list is None if no button was pressed (i.e. a timeout occurred).

- Type: tuple

</div>

[srbox.get_button_press]: #srbox-get_button_press
[get_button_press]: #srbox-get_button_press

<div class="FunctionDoc YAMLDoc" id="srbox-send" markdown="1">

## function __srbox\.send__\(ch\)

Sends a single character to the SR Box. Send '`' to turn off all lights, 'a' for light 1 on, 'b' for light 2 on,'c' for lights 1 and 2 on etc.

__Arguments:__

- `ch` -- The character to send.
	- Type: str

</div>

[srbox.send]: #srbox-send
[send]: #srbox-send

<div class="FunctionDoc YAMLDoc" id="srbox-start" markdown="1">

## function __srbox\.start__\(\)

Turns on sending mode, so that the SR Box starts to send output. The SR Box must be in sending mode when you call [srbox.get_button_press].

</div>

[srbox.start]: #srbox-start
[start]: #srbox-start

<div class="FunctionDoc YAMLDoc" id="srbox-stop" markdown="1">

## function __srbox\.stop__\(\)

Turns off sending mode, so that the SR Box stops giving output.

</div>

[srbox.stop]: #srbox-stop
[stop]: #srbox-stop

</div>

[srbox]: #srbox

