<div class="ClassDoc YAMLDoc" markdown="1">

# class __Keyboard__

The `Keyboard` class is used to collect keyboard responses. You generally create
a `Keyboard` object with the `Keyboard()` factory function, as described in the
section [Creating a Keyboard](#creating-a-keyboard).

__Example__

~~~ .python
# Wait for a 'z' or 'x' key with a timeout of 3000 ms
my_keyboard = Keyboard(keylist=['z', 'x'], timeout=3000)
start_time = clock.time()
key, end_time = my_keyboard.get_key()
response = key
response_time = end_time - start_time
~~~

[TOC]

## Things to know

### Creating a Keyboard

You generally create a `Keyboard` with the `Keyboard()` factory function:

~~~ .python
my_keyboard = Keyboard()
~~~

Optionally, you can pass [Response keywords](#response-keywords) to `Keyboard()`
to set the default behavior:

~~~ .python
my_keyboard = Keyboard(timeout=2000)
~~~

### Key names

- Key names may differ between backends.
- Keys can be identified either by character or name, and are case-insensitive.
  For example:
  - The key 'a' is represented by 'a' and 'A'
  - The up arrow is represented by 'up' and 'UP'
  - The '/' key is represented by '/', 'slash', and 'SLASH'
  - The spacebar is represented by 'space' and 'SPACE'
- To find out the name of key, you can:
  - Click on the 'list available keys' button of the KEYBOARD_RESPONSE item.
  - Collect a key press with a KEYBOARD_RESPONSE item, and display the key name
    through a FEEDBACK item with the text 'You pressed [response]' in it.

### Response keywords

Functions that accept `**resp_args` take the following keyword arguments:

- `timeout` specifies a timeout value in milliseconds, or is set to `None` to
  disable the timeout.
- `keylist` specifies a list of keys that are accepted, or is set to `None`
  accept all keys.

~~~ .python
# Get a left or right arrow press with a timeout of 3000 ms
my_keyboard = Keyboard()
key, time = my_keyboard.get_key(keylist=[u'left', u'right'], timeout=3000)
~~~

Response keywords only affect the current operation (except when passed to
`Keyboard()`). To change the behavior for all subsequent
operations, set the response properties directly:

~~~ .python
# Get two key A or B presses with a 5000 ms timeout
my_keyboard = Keyboard()
my_keyboard.keylist = [u'a', u'b']
my_keyboard.timeout = 5000
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

Or pass the response options to [keyboard.__init__][__init__]:

~~~ .python
# Get two key A or B presses with a 5000 ms timeout
my_keyboard = Keyboard(keylist=[u'a', u'b'], timeout=5000)
key1, time1 = my_keyboard.get_key()
key2, time2 = my_keyboard.get_key()
~~~

## flush()

Clears all pending keyboard input, not limited to the keyboard.



__Returns__

- True if a key had been pressed (i.e., if there was something to
flush) and False otherwise.


## get_key(\*arglist, \*\*kwdict)

Collects a single key press.


__Parameters__

- **\*\*resp_args**: Optional [response keywords](#response-keywords) (`timeout` and
`keylist`) that will be used for this call to `Keyboard.get_key()`.
This does not affect subsequent operations.

__Returns__

- A `(key, timestamp)` tuple. `key` is None if a timeout occurs.

__Example__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key(timeout=5000)
if response is None:
        print(u'A timeout occurred!')
~~~



## get_key_release(\*arglist, \*\*kwdict)

*New in v3.2.0*

Collects a single key release.

*Important:* This
function currently assumes a QWERTY keyboard
layout (unlike
`Keyboard.get_key()`). This means that the returned
`key` may be
incorrect on non-QWERTY keyboard layouts. In addition,
this function is
not implemented for the *psycho* backend.

__Parameters__

- **\*\*resp_args**: Optional [response keywords](#response-keywords) (`timeout` and
`keylist`) that will be used for this call to
`Keyboard.get_key_release()`. This does not affect subsequent
operations.

__Returns__

- A `(key, timestamp)` tuple. `key` is None if a timeout occurs.

__Example__

~~~ .python
my_keyboard = Keyboard()
response, timestamp = my_keyboard.get_key_release(timeout=5000)
if response is None:
        print(u'A timeout occurred!')
~~~



## get_mods()

Returns a list of keyboard moderators (e.g., shift, alt, etc.) that
are currently pressed.



__Returns__

- A list of keyboard moderators. An empty list is returned if no
moderators are pressed.

__Example__

~~~ .python
my_keyboard = Keyboard()
moderators = my_keyboard.get_mods()
if u'shift' in moderators:
        print(u'The shift-key is down!')
~~~



## show_virtual_keyboard(visible=True)

Shows or hides a virtual keyboard if this is supported by the
back-end. This function is only necessary if you want the virtual
keyboard to remain visible while collecting multicharacter
responses. Otherwise, `Keyboard.get_key()` will implicitly show and
hide the keyboard for a single-character response.

This function does nothing for back-ends that do not support virtual
keyboards.

__Parameters__

- **visible**: True if the keyboard should be shown, False otherwise.

__Example__

~~~ .python
my_keyboard = Keyboard()
my_keyboard.show_virtual_keyboard(True)
response1, timestamp2 = my_keyboard.get_key()
response2, timestamp2 = my_keyboard.get_key()
my_keyboard.show_virtual_keyboard(False)
~~~



## synonyms(key)

Gives a list of synonyms for a key, either codes or names. Synonyms
include all variables as types and as Unicode strings (if applicable).



__Returns__

- A list of synonyms


## valid_keys()

Tries to guess which key names are accepted by the back-end. For
internal use.



__Returns__

- A list of valid key names.


</div>

