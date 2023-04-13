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
// Get an experimental variable
console.log('my_variable is: ' + vars.my_variable)
// Set an experimental variable
vars.my_variable = 'my_value'
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

Several convenient JavaScript libraries are bundled with OSWeb.


### random-ext: advanced randomization


The `random-ext` library is available as `random`. This library provides many convenient, higher-level functions for randomization.

__Example:__

Draw eight circle with a random color and a location that is randomly sampled from a five by five grid:

```js
let positions = xy_grid(5, 50)
positions = random.subArray(positions, 8)
const cnv = Canvas()
cnv.fixdot()
for (const [x, y] of positions) {
    cnv.circle({x: x, y: y, r: 20, fill: true, color: random.color()})
}
cnv.show()
```

For an overview, see:

- <https://www.npmjs.com/package/random-ext>


### pythonic: Python-like functions for iterating over arrays

The `pythonic` library provides Python-like functions for iterating over arrays. Available functions are: `range()`, `enumerate()`, `items()`, `zip()`, and `zipLongest()`.

__Example:__

Draw a five by five grid of incrementing numbers:

```js
let positions = xy_grid(5, 50)
const cnv = Canvas()
for (const [i, [x, y]] of enumerate(positions)) {
    cnv.text({text: i, x: x, y: y})
}
cnv.show()
```

For an overview, see:

- <https://www.npmjs.com/package/pythonic>


### color-convert: color conversion utilities

The `color-convert` library is available as `convert`. It provides convenient high level functions for converting from one color specification to another.

__Example:__

```js
console.log('The RGB values for blue are ' + convert.keyword.rgb('blue'))
```

For an overview, see:

- <https://www.npmjs.com/package/color-convert>


### csv-parse: parse CSV-formatted text into an Object

The synchronous `parse()` function from the `csv-parse` library is available. This allows you to parse CSV-formatted text, for example from a CSV file in the file pool, into an Object.

__Example:__

```js
const conditions = csvParse(
    pool['attentional-capture-jobs.csv'].data,
    {columns: true}
)
for (const trial of conditions) {
    console.log(trial.distractor)
}
```

For an overview, see:

- <https://csv.js.org/parse/api/sync/#sync-api>


## Debugging

Most modern browsers, especially Chrome and Firefox, have a powerful built-in debugger. You can activate the debugger by adding a line that simply states `debugger` to your script (%FigDebuggerInlineJavaScript).

%--
figure:
 id: FigDebuggerInlineJavaScript
 source: debugger-inline-javascript.png
 caption: Activating the debugger from an INLINE_JAVASCRIPT item.
--%


Then start the experiment and show the debugger (or: Dev tools in Chrome, or: Web Developer Tools in Firefox) as soon as the OSWeb welcome screen appears. The debugger will then pause the experiment when it encounters the `debugger` statement. At this point, you can use the Console to interact with the JavaScript workspace, or you can inspect variables using the Scope tool (%FigDebuggerChrome).

%--
figure:
 id: FigDebuggerChrome
 source: debugger-chrome.png
 caption: Inspecting the variable scope in Chrome.
--%

See also:

- %link:manual/osweb/osweb%
