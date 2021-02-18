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
