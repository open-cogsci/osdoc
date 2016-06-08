title: Keyboard responses
reviewed: false

Keyboard responses are collected with the KEYBOARD_RESPONSE item.

[TOC]

## Key names

Keys are generally identified by their character and/ or their description (depending on which is applicable). For example:

- The `/` key is named 'slash' and '/'. You can use either of the two names.
- The `a` is named 'a'.
- The left-arrow key is named 'left'.

If you don't know what a particular key is named, you can:

- Click on the 'List available keys' button; or
- Create a simple experiment in which a KEYBOARD_RESPONSE is immediately followed by a FEEDBACK item with the text '[response]' on it. This will show the name of the previously collected response.

%--include: include/correct_response.md--%

%--include: include/allowed_responses.md--%

%--include: include/timeout.md--%

## Collecting keyboard responses in Python

You can use the `keyboard` object to collect keyboard responses in Python:

- %link:manual/python/keyboard%
