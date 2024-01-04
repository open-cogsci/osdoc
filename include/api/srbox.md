<div class="ClassDoc YAMLDoc" markdown="1">

# instance __srbox__

If you insert the srbox plugin at the start of your experiment, an
instance of SRBOX automatically becomes part of the experiment
object and
can be accessed within an inline_script item as SRBOX.

__Important note1:__

If you do not specify a device, the plug-in will try to autodetect
the
SR Box port. However, on some systems this freezes the experiment, so
it is better to explicitly specify a device.

__Important note 2:__

You
need to call [srbox.start] to put the SR Box in sending mode,
before
calling [srbox.get_button_press] to collect a button press.

__Example:__
~~~ .python
t0 = clock.time()
srbox.start()
button, t1 = srbox.get_button_press(allowed_buttons=[1, 2],
                                    require_state_change=True)
if button == 1:
    response_time = t1 - t0
print(f'Button 1 was pressed in {response_time} ms!')
srbox.stop()
~~~
[TOC]

## get_button_press(allowed_buttons=None, timeout=None, require_state_change=False)

Collects a button press from the SR box.


__Parameters__

- **allowed_buttons**: A list of buttons that are accepted or `None` to accept all
buttons. Valid buttons are integers 1 through 8.
- **timeout**: A timeout value in milliseconds or `None` for no timeout.
- **require_state_change    Indicates whether already pressed button should be accepted**: (False), or whether only a state change from unpressed to pressed
is accepted (True).

__Returns__

- A `(button_list, timestamp)` tuple. `button_list` is `None` if no 
button was pressed (i.e. a timeout occurred).


## send(ch)

Sends a single character to the SR Box. Send '`' to turn off all
lights, 'a' for light 1 on, 'b' for light 2 on,'c' for lights
1 and 2 on etc.


__Parameters__

- **ch**: The character to send. If a `str` is passed, it is encoded to
`bytes` using utf-8 encoding.


## start()

Turns on sending mode, so that the SR Box starts to send output.
The SR Box must be in sending mode when you call
[srbox.get_button_press].




## stop()

Turns off sending mode, so that the SR Box stops giving output.




</div>

