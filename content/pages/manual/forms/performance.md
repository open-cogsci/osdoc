title: Slow performance and troubleshooting

[TOC]

## Performance issues

Forms can be slow, and this is especially noticeable if you are using text input on a slower system. If you find that forms are too slow, you can do a number of things:

- Switch to the *legacy* backend and set *Double buffering* to 'no' in the backend settings.
- Switch to the *xpyriment* backend and set *OpenGL* to 'no' in the backend settings. Important: This disables hardware acceleration and decrease the precision of the display-presentation timestamps.
- Reduce the number of elements on the form. The speed with which the form is rendered is directly proportional to the total surface of all its elements.

## Troubleshooting

- If you are using the *legacy* backend, you may find that the forms do not show: The screen is black, except for an occasional flicker when you click the mouse. This issue can be resolved by setting *Double buffering* to 'no' in the backend settings.
- If you are using the *legacy* backend, you may find that the mouse cursor is not visible. For a workaround, see:
 	- %link:backends%
