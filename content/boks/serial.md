---
layout: osdoc
title: Serial port communication
group: Boks
permalink: /serial/
---

If you are using software that cannot make use of the Boks Python module, you can interact directly with the Boks through via the serial port. Communication occurs by sending a single command byte to the Boks. Depending on the command, the command byte should be followed by one or more bytes that serve as parameters. Depending on the command, the Boks responds by sending zero or more bytes in response. The command bytes are indicated in decimal notation in the square brackets.

#### Timestamps

All timestamps are in microseconds. Only the `CMD_WAIT_SLEEP` command will fall back to millisecond precision when the timeout has been set to more than 16 milliseconds.

#### Serial port settings

The Boks is connected via USB as a virtual serial port device. The baudrate is `115200`.

#### `CMD_RESET` [001]

Resets the Boks to the initial state.

#### `CMD_IDENTIFY` [002]

Returns a sequence of 21 bytes, which should be interpreted as two ASCII strings. The first string is 5 bytes and contains the firmware version of the Boks. The second string is 16 bytes and contains the model description, optionally right-padded with whitespace.

Return example:

	'0.1.0dev.boks        '

#### `CMD_WAIT_PRESS` [003]

A single byte that corresponds to the button that is pressed, i.e. `1`, `2`, `3`, or `4`. If a timeout occurs (see `CMD_SET_TIMEOUT`), `255` is returned. Depending on whether the device is in continuous or discontinuous mode (see `CMD_SET_CONTINUOUS`), pressed buttons are returned immediate (continuous) or only buttons that are pressed after the command has been sent are returned (discontinuous)

#### `CMD_WAIT_RELEASE` [004]

Returns a single byte that corresponds to the button that is released. For more information, see `CMD_WAIT_PRESS`.

#### `CMD_WAIT_SLEEP` [005]

Waits for the interval specified by `CMD_SET_TIMEOUT`.

#### `CMD_BUTTON_STATE` [006]

Returns a single byte that contains the state for each of the buttons. The first bit (rightmost) indicates the state of the first button, the second bit indicates the state of the second button, etc.

Return example (binary):

	00001111 # All buttons pressed
	00000010 # Button 2 pressed

#### `CMD_SET_T1` [007]

Sets the `T1` (Timestamp 1) of the Boks to the current time in microseconds, as measured by the Boks' internal clock. Does not return a value.

#### `CMD_SET_T2` [008]

Sets the `T2`. For more information, see `CMD_SET_T1`.

#### `CMD_SET_TIMEOUT` [009]

Sets the timeout value, which is used by `CMD_WAIT_PRESS`, `CMD_WAIT_RELEASE`, and `CMD_SLEEP`. The command byte should be followed by an unsigned long (4 bytes) that indicates the timeout in microseconds. The value `0` disables the timeout.

#### `CMD_SET_BUTTONS` [010]

Sets the buttons that should be polled by `CMD_WAIT_PRESS` and `CMD_WAIT_RELEASE`. The command byte should be followed by a single byte that indicates which buttons should be pressed. The first (rightmost) bit corresponds to the first button, etc. To prevent deadlocks, you cannot turn off all buttons. If you try do this, by sending a 0-byte, all buttons will be switched on instead.

Parameter example (binary):

	00001111 # Turn on all buttons, except photodiode
	00000011 # Only poll buttons one and two
	00000000 # Turn on all buttons, except photodiode (special case!)
	10000000 # Turn on photodiode

#### `CMD_GET_T1` [011]

Returns `T1` as an unsigned long (4 bytes).

#### `CMD_GET_T2` [012]

Returns `T2` as an unsigned long (4 bytes).

#### `CMD_GET_TD` [013]

Returns the difference between `T2` and `T1` (`T2` – `T1`) as an unsigned long (4 bytes).

#### `CMD_GET_TIME` [014]

Returns the current time according to the Boks' internal clock as an unsigned long (4 bytes).

#### `CMD_GET_TIMEOUT` [015]

Returns the timeout value as set by `CMD_SET_TIMEOUT` as an unsigned long (4 bytes).

#### `CMD_GET_BUTTONS` [0016]

Returns the active buttons as set by `CMD_SET_BUTTONS` as a single byte. For more information, see `CMD_SET_BUTTONS`.

#### `CMD_LED_ON` [18]

Turns the led on.

#### `CMD_LED_OFF` [19]

Turns the led off.

#### `CMD_GET_BTNCNT` [20]

Returns the number of buttons on the Boks (including photodiode) as a single byte.

##### `CMD_GET_SID` [21]

Returns the serial id of the Boks as a 6 character string.

##### `CMD_LINK_LED` [22]

Puts the Boks into link-led mode, such that the LED will turn on when the photodiode is activated. Link-led mode is aborted when a non-0 byte is sent to the Boks.
