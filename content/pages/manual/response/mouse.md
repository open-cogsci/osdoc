title: Mouse and touch responses

Mouse responses are collected with the MOUSE_RESPONSE item. The MOUSE_RESPONSE is primarily intended to collect individual mouse clicks. On touch-enabled devices, touch responses (TOUCH_RESPONSE item) are generally registered in the same way as mouse-button-1 clicks at the touched coordinates, so the same item and logic can often be used for both mouse and touch input. If you want to collect mouse-cursor trajectories, take a look at the MOUSETRAP plugins:

- %link:mousetracking%

[TOC]


## Response variables

The MOUSE_RESPONSE sets the standard response variables as described here:

- %link:manual/variables%

In addition, the following variables are relevant for mouse and touch responses:

| Variable | Description |
|---|---|
| `response` | The mouse button that was clicked. This is stored as a number (`1` = left button, `2` = middle button, `3` = right button, `4` = scroll up, `5` = scroll down). On timeout, `response` is set to `None`. |
| `response_time` | The response time in milliseconds, or the registered timeout time if no response was made. |
| `correct` | Automatically set based on button correctness: `1` for a correct mouse-button response, `0` for an incorrect mouse-button response or timeout, and `undefined` if no correct response is specified. |
| `cursor_x` | The x coordinate of the click or touch. |
| `cursor_y` | The y coordinate of the click or touch. |
| `cursor_roi` | A semicolon-separated list of names of sketchpad elements that contain the clicked coordinates. If elements overlap, multiple names can be listed. This variable reports where the click occurred; it does not automatically determine `correct`. |


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

Note that the correct response refers to which mouse button was clicked, not to which region of interest was clicked (ROI). If correctness depends on the clicked location rather than on the mouse button, you need to determine correctness yourself based on `cursor_roi`; see the section below for more information about ROIs.


## Allowed responses

The *Allowed responses* field indicates a list of allowed responses. All other responses will be ignored, except for 'Escape', which will pause the experiment. The allowed responses should be a semicolon-separated list of responses, such as '1;3' to allow the left and right mouse buttons. To accept all responses, leave the *Allowed responses* field empty.

Note that the allowed responses refer to which mouse button can be clicked, not to which region of interest can be clicked (ROI); see the section below for more information about ROIs.


%--include: include/timeout.md--%

## Coordinates and regions of interest (ROIs)

The `cursor_x` and `cursor_y` variables hold the location of the mouse click.

If you indicate a linked SKETCHPAD, the variable `cursor_roi` will hold a semicolon-separated list of names of elements that contain the clicked coordinate. In other words, elements on the SKETCHPAD automatically serve as regions of interest for the mouse click.

The `cursor_roi` variable indicates where the click occurred, whereas `response` indicates which mouse button was clicked. If multiple named elements overlap at the clicked position, `cursor_roi` can contain multiple element names.

If the correctness of a response depends on which ROI was clicked, you cannot use the `correct_response` variable for this, because this refers only to which mouse button was clicked. Instead you need to use a simple script to determine correctness based on `cursor_roi`, and, if necessary, overwrite `correct`.

In a Python INLINE_SCRIPT you can do this as follows:

```python
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if correct_roi in clicked_rois:
    print('correct!')
    correct = 1
else:
    print('incorrect!')
    correct = 0
```

With OSWeb using an INLINE_JAVASCRIPT you can do this as follows:

```javascript
clicked_rois = cursor_roi.split(';')
correct_roi = 'my_roi'
if (clicked_rois.includes(correct_roi)) {
    console.log('correct!')
    correct = 1
} else {
    console.log('incorrect!')
    correct = 0
}
```

Here, `'my_roi'` is simply an example name of a sketchpad element. In a real experiment, replace it with the name of the ROI that should count as correct. To avoid ambiguity, named elements should be unique within a sketchpad.


## Touch responses

On touch-enabled devices, each tap is generally registered as a mouse-button-1 response at the touched coordinates. This means that the MOUSE_RESPONSE item can often be used for both mouse clicks and touch taps without further modification.

In practice, this means that a touch response behaves as follows:

- The button is typically registered as `1`
- The location of the touch is stored in `cursor_x` and `cursor_y`
- If a sketchpad is linked, touched elements can be identified through `cursor_roi`

This can be useful for experiments that should run on both desktop and touchscreen devices.

### Example: touch responses with MOUSE_RESPONSE

For example, consider a simple choice task in which two large sketchpad elements are shown on the left and right side of the screen. If the participant taps the left element on a touchscreen:

- `response` will typically be set to `1`
- `cursor_x` and `cursor_y` will contain the touch coordinates
- `cursor_roi` may contain the name of the touched element, such as `left_option`

This means that touch input can be handled in the same way as mouse input. If correctness depends on the touched element rather than on the button, you can use the same `cursor_roi` logic described above.

### Example: using the `touch_response` plug-in

For experiments where you want to divide the screen into discrete response regions (e.g., a grid of buttons), the `touch_response` plug-in offers a simpler and more convenient approach than working with raw coordinates. It divides the display into a grid of rows and columns, and encodes each response as a single number, counting left-to-right and top-down.

For example, with 2 columns and 3 rows, the display is divided as follows:

| | Column 1 | Column 2 |
|---|---|---|
| **Row 1** | 1 | 2 |
| **Row 2** | 3 | 4 |
| **Row 3** | 5 | 6 |

So, if you specify 2 columns and 1 row, the display is divided into two response regions:

| Left half | Right half |
|---|---|
| `1` | `2` |

In a simple yes/no task, you could assign:

- `1` = Yes
- `2` = No

If the correct answer is Yes, set the *Correct response* field to `1`. OpenSesame will then automatically set `correct` to 1 when the participant taps the left half of the screen.

> [!NOTE]
> The `touch_response` plug-in does not use named sketchpad elements or `cursor_roi`. Responses are encoded only as grid positions.

> [!NOTE]
> The exact behavior of touch input may depend on the platform and backend that is used to run the experiment.

> [!NOTE]
> The MOUSE_RESPONSE item only captures a single touch response. If multiple fingers touch the screen simultaneously, only one response is registered.


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
