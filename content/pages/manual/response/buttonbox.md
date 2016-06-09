title: Button box

There are many different types of button boxes, and they all work in different ways. Therefore, there is no single OpenSesame item that works with all button boxes. (This is different from keyboards, which are standard devices that all work with the KEYBOARD_RESPONSE item.)

Common types of button boxes:

- Some button boxes *emulate keypresses*. This is easy, because you can use the normal KEYBOARD_RESPONSE item.
	- %link:manual/response/keyboard%
- Some button boxes *emulate a joystick*. This is also easy, because you can use the JOYSTICK plugin.
	- %link:joystick%
- Some button boxes are compatible with the *Serial Response Box* that is developed by Psychology Software Tools. These button boxes are supported by the SRBOX plugin.
	- %link:srbox%
- Some button boxes have their own Python libaries. In this case, you should be able to find example scripts of how to use the button box in Python, that is, in an OpenSesame INLINE_SCRIPT item.
