title: Inline JavaScript


The INLINE_JAVASCRIPT item works similarly to the regular INLINE_SCRIPT item, except that it runs JavaScript instead of Python code. The functionality is also more limited.

- You can get and set experimental variables using the `vars` object, which works similarly to the `var` object in Python.
- You can print debug messages with `console.log()`. On the desktop, these messages will appear in the debug window. In a browser, they will appear in the browser console (see the Debugging section in [OSWeb](%url:osweb%)).
- You cannot create `Canvas`, `Keyboard` objects, etc.
- The JavaScript workspace is not persistent. That is, if you define a variable in one script, it will not be accessible in another script. Exceptions are the `vars` object and other variables that are globally available in JavaScript (e.g. `window`).
- When running on the desktop (i.e. in a window rather than in a browser), JavaScript is executed using [Js2Py](https://github.com/PiotrDabkowski/Js2Py), which supports ECMAScript 5.1, an outdates version of JavaScript. This limitation does not apply when you test the experiment in a browser, in which case you can use the version of JavaScript that is supported by the browser, which is generally ECMA 6.


Example:


``` .javascript
if (vars.subject_nr % 2 == 0) {
  vars.target_color = 'blue'
} else {
  vars.target_color = 'red'
}
console.log('target_color = ' + vars.target_color)
```
