title: About JavaScript

In OpenSesame you can create complex experiments using only the graphical user interface (GUI). But you will sometimes encounter situations in which the functionality provided by the GUI is insufficient. In these cases you can add JavaScript code to your experiment.

JavaScript is for experiments that run in a browser with OSWeb. If you need to run your experiment on the desktop, you need to use [Python](%url:manual/python/about%) instead of JavaScript.

__Version note:__ Desktop support for JavaScript was removed in OpeSesame 4.0. This is because JavaScript support on the desktop was incomplete and was perceived by users as confusing without adding much benefit.
{: .page-notification}

[TOC]


## Learning JavaScript

There are many JavaScript tutorials available online. One good resource is Code Academy:

- <https://www.codecademy.com/learn/introduction-to-javascript>


## JavaScript in the OpenSesame GUI


### Inline_javascript items

In order to use JavaScript code you need to add an INLINE_JAVASCRIPT item to your experiment. After you have done this you will see something like %FigInlineJavaScript.

%--
figure:
 id: FigInlineJavaScript
 source: inline-javascript.png
 caption: The INLINE_JAVASCRIPT item.
--%

As you can see, the INLINE_JAVASCRIPT item consists of two tabs: one for the Prepare phase and one for the Run phase. The Prepare phase is executed first, to allow items to prepare for the time-critical run phase. It is good practice to construct `Canvas` objects during the Prepare phase, so that they can be presented without delay during the Run phase. But this is only convention; you can execute arbitrary JavaScript code during both phases.

For more information about the prepare-run strategy, see:

- %link:prepare-run%


### Printing output to the console

You can print to the console with the `console.log()` command:

```js
console.log('This will appear in the console!')
```

When running on the desktop, the output will appear in the OpenSesame console (or: debug window). When running in a browser, the output will appear in the browser console.


## Things to know

### Common functions

Many common functions are directly available in an INLINE_JAVASCRIPT item. For example:

```js
// `Canvas()` is a factory function that returns a `Canvas` object
let fixdotCanvas = Canvas()
if (sometimes()) {  // Sometimes the fixdot is green
    fixdotCanvas.fixdot({color: 'green'})
} else {  // Sometimes it is red
    fixdotCanvas.fixdot({color: 'red'})
}
fixdotCanvas.show()
```

For a list of common functions, see:

- %link:manual/javascript/common%


### Declaring variables (let and var)

INLINE_JAVASCRIPT items are executed in non-strict (or: sloppy) mode. This means that you can assign a value to a variable that was not explicitly declared. When you do this, the variable is implicitly declared using `var` if it wasn't already declared.

```js
my_variable = 'my value'  // implicitly declared using var
```

Variables that are declared implicitly or explicitly using `var` are global, which primarily means that they may be logged by a LOGGER. Variables that are declared using `let` are not global, which primarily means that they are not logged by a LOGGER.

```js
this_is_a_global_variable = 'my value'
var this_is_also_a_global_variable = 'my value'
let this_is_not_a_global_variable = 'my value'
```


### The `persistent` object: preserving objects across scripts

__Version note__ As of OSWeb 2.0, all JavaScript code is executed in the same workspace and objects are therefore preserved across scripts. This means that you no longer need the `persistent` object.
{:.page-notification}

Each INLINE_JAVASCRIPT item is executed in its own workspace. This means—and this is different from Python INLINE_SCRIPT items!—that you cannot use variables or functions that you've declared in one script in another script. As a workaround, you can attach variables or functions as properties to the `persistent` object, which serves as a container of things that you want to preserve across scripts.

This way you can construct a `Canvas` in one INLINE_JAVASCRIPT ...

```js
persistent.myCanvas = Canvas()
persistent.myCanvas.fixdot()
```

.. and show it in another INLINE_JAVASCRIPT:

```js
persistent.myCanvas.show()
```


### The `vars` object: Access to experimental variables

__Version note__ As of OSWeb 2.0, all experimental variables are available as globals. This means that you no longer need the `vars` object.
{:.page-notification}

You can access experimental variables through the `vars` object:

```js
// OSWeb <= 1.4 (with vars object)
// Get an experimental variable
console.log('my_variable is: ' + vars.my_variable)
// Set an experimental variable
vars.my_variable = 'my_value'

// OSWeb >= 2.0 (without vars object)
// Get an experimental variable
console.log('my_variable is: ' + my_variable)
// Set an experimental variable
my_variable = 'my_value'
```


### The `pool` object: Access to the file pool

You access 'files' from the file pool through the `pool` object. The most obvious use of this is to parse CSV files, for example with experimental conditions, from the file pool using the `csv-parse` library (described in more detail below).

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

You can also play sound files from the file pool directly. Assuming that there is a file called `bark.ogg` in the file pool, you can play it like so:

```js
pool['bark.ogg'].data.play()
```


### The `Canvas` class: Presenting visual stimuli

The `Canvas` class is used to present visual stimuli. For example, you can show a fixation dot as follows:

```js
let myCanvas = Canvas()
myCanvas.fixdot()
myCanvas.show()
```

A full overview of the `Canvas` class can be found here:

- %link:manual/javascript/canvas%

## Available JavaScript libraries

The following JavaScript libraries are included by default:

- [random functions (`random-ext`)](%url:manual/javascript/random%)
- [Color-conversion functions (`color-convert`)](%url:manual/javascript/color-convert%)
- [CSV functions (`csv-parse`)](%url:manual/javascript/csv%)
- [Python-like iterators (`pythonic`)](%url:manual/javascript/pythonic%)

You can include additional JavaScript libraries by URLs to the libraries in the 'External JavaScript' libraries field of the OSWeb control panel.


## Debugging

See:

- %link:debugging%
