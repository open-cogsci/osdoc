title: Mouse responses

Mouse responses are collected with the MOUSE_RESPONSE item. The MOUSE_RESPONSE is primarily intended to collect individual mouse clicks. If you want to collect mouse-cursor trajectories, take a look at the MOUSETRAP plugins:

- %link:mousetracking%

[TOC]


## Response variables

The MOUSE_RESPONSE sets the standard response variables as described here:

- %link:manual/variables%


## Mouse-button names

Mouse buttons have a number (`1`, etc.) as well as a name (`left_button`, etc.). Both can be used to specify correct and allowed responses, but the `response` variable will be set to a number.

- `left_button` corresponds to `1`
- `middle_button` corresponds to `2`
- `right_button` corresponds to `3`
- `scroll_up` corresponds to `4`
- `scroll_down` corresponds to `5`


## Correct response

The *Correct response* field indicates which response is considered correct. After a correct response, the `correct` variable is automatically set to 1; after an incorrect response or a timeout (i.e. everything else), `correct` is set to 0; if no correct response is specified, `correct` is set to 'undefined'.

You can indicate the correct response in three main ways:

- *Leave the field empty.* If you leave the *Correct response* field empty, OpenSesame will automatically check if a variable called `correct_response` has been defined, and, if so, use this variable for the correct response.
- *Enter a literal value.* You can explicitly enter a response, such as 1. This is only useful if the correct response is fixed.
- *Enter a variable name.* You can enter a variable, such as '{cr}'. In this case, this variable will be used for the correct response.


## Allowed responses

The *Allowed responses* field indicates a list of allowed responses. All other responses will be ignored, except for 'Escape', which will pause the experiment. The allowed responses should be a semicolon-separated list of responses, such as '1;3' to allow the left and right mouse buttons. To accept all responses, leave the *Allowed responses* field empty.


%--include: include/timeout.md--%

## Coordinates and regions of interest (ROIs)

The `cursor_x` and `cursor_y` variables hold the location of the mouse click.

If you indicate a linked SKETCHPAD, the variable `cursor_roi` will hold a comma-separated list of names of elements that contain the clicked coordinate. In other words, elements on the SKETCHPAD automatically serve as regions of interest for the mouse click.

%--
video:
 source: youtube
 id: VidMouseROI
 videoid: 21cgX_zHDiA
 width: 640
 height: 360
 caption: |
  Collecting mouse clicks and using regions of interest.
--%

## Collecting mouse responses in Python

You can use the `mouse` object to collect mouse responses in Python:

- %link:manual/python/mouse%
