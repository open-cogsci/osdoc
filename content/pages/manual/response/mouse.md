title: Mouse responses

Mouse responses are collected with the MOUSE_RESPONSE item. The MOUSE_RESPONSE is primarily intended to collect individual mouse clicks. If you want to collect mouse-cursor trajectories, take a look at the MOUSETRAP plugins:

- %link:mousetracking%

[TOC]

## Mouse-button names

Mouse buttons have a number (`1`, etc.) as well as a name (`left_button`, etc.). Both can be used to specify correct and allowed responses, but numbers will be used for logging.

- `left_button` corresponds to `1`
- `middle_button` corresponds to `2`
- `right_button` corresponds to `3`
- `scroll_up` corresponds to `4`
- `scroll_down` corresponds to `5`

%--include: include/correct_response.md--%

%--include: include/allowed_responses.md--%

%--include: include/timeout.md--%

## Collecting mouse responses in Python

You can use the `mouse` object to collect mouse responses in Python:

- %link:manual/python/mouse%
