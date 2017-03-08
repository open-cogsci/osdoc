<div class="ClassDoc YAMLDoc" id="keyboard" markdown="1">

# class __keyboard__

The `keyboard` class is used to collect keyboard responses.

__Example:__

~~~ .python
# Wait for a 'z' or 'x' key with a timeout of 3000 ms
my_keyboard = keyboard(keylist=['z', 'x'], timeout=3000)
start_time = clock.time()
key, end_time = my_keyboard.get_key()
var.response = key
var.response_time = end_time - start_time
~~~

[TOC]

## Things to know

### Key names

- Key names may differ between backends.
- Keys can be identified either by character or name, and are
  case-insentive. For example:
  - The key 'a' is represented by 'a' and 'A'
  - The up arrow is represented by 'up' and 'UP'
  - The '/' key is represented by '/', 'slash', and 'SLASH'
  - The spacebar is represented by 'space' and 'SPACE'
- To find out the name of key, you can:
  - Click on the 'list available keys' button of the
    KEYBOARD_RESPONSE item.
  - Collect a key press with a KEYBOARD_RESPONSE item, and display
    the key name through a FEEDBACK item with the text 'You
    pressed [response]' in it.

### Response keywords

Functions that accept `**resp_args` take the following keyword
arguments:

- `timeout` specifies a timeout value in milliseconds, or is set to
  `None` to disable the timeout.
- `keylist` specifies a list of keys that are accepted, or is set to
  `None` accept all keys.

~~~ .python
# Get a left or right arrow press with a timeout of 3000 ms
my_keyboard = keyboard()
key, time = my_keyboard.get_key(keylist=[u'left', u'right'],
        timeout=3000)
~~~

Response keywords only affect the current operation (except when passed
to [keyboard.\_\_init\_\_][__init__]). To change the behavior for all
subsequent operations, set the response properties directly:

~~~ .python
# Get two key A or B presses with a 5000 ms timeout
my_keyboard = keyboard()
my_keyboard.keylist = [u'a', u'b']
my_keyboard.timeout = 5000
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

Or pass the response options to [keyboard.\_\_init\_\_][__init__]:

~~~ .python
# Get two key A or B presses with a 5000 ms timeout
my_keyboard = keyboard(keylist=[u'a', u'b'], timeout=5000)
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

<div class="FunctionDoc YAMLDoc" id="keyboard-__init__" markdown="1">

## function __keyboard\.\_\_init\_\___\(experiment, \*\*resp\_args\)

Constructor to create a new `keyboard` object. You do not generally
call this constructor directly, but use the `keyboard()` function,
which is described here: [/python/common/]().

__Example:__

~~~ .python
my_keyboard = keyboard(keylist=['z', 'm'], timeout=2000)
~~~

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment

__Keyword dict:__

- `**resp_args`: Optional [response keywords] (`timeout` and `keylist`) that will be used as the default for this `keyboard` object.

</div>

[keyboard.__init__]: #keyboard-__init__
[__init__]: #keyboard-__init__

<div class="FunctionDoc YAMLDoc" id="keyboard-flush" markdown="1">

## function __keyboard\.flush__\(\)

Clears all pending keyboard input, not limited to the keyboard.

__Returns:__

True if a key had been pressed (i.e., if there was something to flush) and False otherwise.

- Type: bool

</div>

[keyboard.flush]: #keyboard-flush
[flush]: #keyboard-flush

<div class="FunctionDoc YAMLDoc" id="keyboard-get_key" markdown="1">

## function __keyboard\.get\_key__\(\*\*resp\_args\)

Collects a single key press.

__Example:__

~~~ .python
my_keyboard = keyboard()
response, timestamp = my_keyboard.get_key(timeout=5000)
if response is None:
        print(u'A timeout occurred!')
~~~

__Keyword dict:__

- `**resp_args`: Optional [response keywords] (`timeout` and `keylist`) that will be used for this call to [keyboard.get_key] this does not affect subsequent operations.

__Returns:__

A `(key, timestamp)` tuple. `key` is None if a timeout occurs.

- Type: tuple

</div>

[keyboard.get_key]: #keyboard-get_key
[get_key]: #keyboard-get_key

<div class="FunctionDoc YAMLDoc" id="keyboard-get_mods" markdown="1">

## function __keyboard\.get\_mods__\(\)

Returns a list of keyboard moderators (e.g., shift, alt, etc.) that are currently pressed.

__Example:__

~~~ .python
my_keyboard = keyboard()
moderators = my_keyboard.get_mods()
if u'shift' in moderators:
        print(u'The shift-key is down!')
~~~

__Returns:__

A list of keyboard moderators. An empty list is returned if no moderators are pressed.

- Type: list

</div>

[keyboard.get_mods]: #keyboard-get_mods
[get_mods]: #keyboard-get_mods

<div class="FunctionDoc YAMLDoc" id="keyboard-show_virtual_keyboard" markdown="1">

## function __keyboard\.show\_virtual\_keyboard__\(visible=True\)

Shows or hides a virtual keyboard if this is supported by the
back-end. This function is only necessary if you want the virtual
keyboard to remain visible while collecting multicharacter
responses. Otherwise, [keyboard.get_key] will implicitly shown and
hide the keyboard for a single-character response.

This function does nothing for back-ends that do not support virtual
keyboards.

__Example:__

~~~ .python
my_keyboard = keyboard()
my_keyboard.show_virtual_keyboard(True)
response1, timestamp2 = my_keyboard.get_key()
response2, timestamp2 = my_keyboard.get_key()
my_keyboard.show_virtual_keyboard(False)
~~~

__Keywords:__

- `visible` -- True if the keyboard should be shown, False otherwise.
	- Type: bool
	- Default: True

</div>

[keyboard.show_virtual_keyboard]: #keyboard-show_virtual_keyboard
[show_virtual_keyboard]: #keyboard-show_virtual_keyboard

</div>

[keyboard]: #keyboard

