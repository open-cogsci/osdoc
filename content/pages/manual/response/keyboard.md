title: Keyboard responses

Keyboard responses are collected with the KEYBOARD_RESPONSE item.

[TOC]


## Response variables

The KEYBOARD_RESPONSE sets the standard response variables as described here:

- %link:manual/variables%

## Key names

Keys are generally identified by their character and/ or their description (depending on which is applicable). For example:

- The `/` key is named 'slash' and '/'. You can use either of the two names.
- The `a` is named 'a'.
- The left-arrow key is named 'left'.

If you don't know what a particular key is named, you can:

- Click on the 'List available keys' button; or
- Create a simple experiment in which a KEYBOARD_RESPONSE is immediately followed by a FEEDBACK item with the text '[response]' on it. This will show the name of the previously collected response.


## Correct response

The *Correct response* field indicates which response is considered correct. After a correct response, the `correct` variable is automatically set to 1; after an incorrect response (i.e. everything else), `correct` is set to 0; if no correct response is specified, `correct` is set to 'undefined'.

You can indicate the correct response in three main ways:

- *Leave the field empty.* If you leave the *Correct response* field empty, OpenSesame will automatically check if a variable called `correct_response` has been defined, and, if so, use this variable for the correct response.
- *Enter a literal value.* You can explicitly enter a response, such as 'left' in the case of a KEYBOARD_RESPONSE item. This is only useful if the correct response is fixed.
- *Enter a variable name.* You can enter a variable, such as '[cr]'. In this case, this variable will be used for the correct response.


## Allowed responses

The *Allowed responses* field indicates a list of allowed responses. All other responses will be ignored, except for 'Escape', which will pause the experiment. The allowed responses should be a semicolon-separated list of responses, such as 'a;left;/' for a KEYBOARD_RESPONSE. To accept all responses, leave the *Allowed responses* field empty.


%--include: include/timeout.md--%

## Collecting keyboard responses in Python

You can use the `keyboard` object to collect keyboard responses in Python:

- %link:manual/python/keyboard%
