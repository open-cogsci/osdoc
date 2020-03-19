title: Running experiments online


[TOC]


## OSWeb

### About OSWeb

[OSWeb] is an online runtime for OpenSesame experiments. That is, it is a JavaScript library that interprets and executes OpenSesame experiments.


### The OSWeb extension

The [OSWeb extension for OpenSesame] (%FigOSWebExtension) allows you to test experiments in a browser, and to export experiments in a format that you can import into JATOS (desribed below).

The extension is pre-installed in the Windows and Mac OS packages of OpenSesame 3.2.6 and later.

Alternatively, you can install the extension manually. It is available on PyPi as `opensesame-extension-osweb` and can be installed as described here:

- %link:environment%


%--
figure:
 id: FigOSWebExtension
 source: osweb-extension.png
 caption: The OSWeb extension for OpenSesame.
--%


### Testing in a browser

- In OpenSesame, open the OSWeb extension (Menu → Tools → OSWeb).
- The extension will perform a simple (and incomplete) check to see if your experiment appears to be compatible with OSWeb.
- If no problems are detected, click 'Test experiment in external browser', or click on the corresponding button in the main toolbar.
- This will open the experiment in your default browser so that you can check if the experiment runs as expected (%FigTestRun).
- You can also click the 'Run in browser' button in the main toolbar (Alt+Ctrl+W)


%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: The welcome screen of OSWeb when testing the experiment in a browser.
--%


### Debugging

First, make sure that your experiment only uses supported functionality, as described below. Next, run the experiment in the traditional (non-browser) way in OpenSesame. This will give you the most informative error messages that you can use for debugging.

If your experiment uses only supported functionality and runs normally in OpenSesame, then you can use the browser console to see JavaScript error messages. These are much less informative than OpenSesame's error messages, but they can still be helpful. Each browser has a different way to access the console. In Chrome, you can access the console by right-clicking somewhere, selecting Inspect (`Ctrl+Shift+I`), and then switching to the Console tab (see %FigChromeConsole). In Firefox, you can access the console by clicking on the Menu icon in the top right and then selecting Web Developer → Web Console (`Ctrl+Shift+K`).


%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: Chrome's browser console.
--%



### Supported functionality

The following items are supported by OSWeb:

- `advanced_delay`
- `feedback`
    - Unsupported: named elements
- `inline_javascript`
- `keyboard`
    - Unsupported: key release
- `logger`
- `loop`
    - Unsupported: resume after break
    - Unsupported: evaluate on first cycle
    - Unsupported: file source
    - Unsupported: constraints (pseudorandomization)
- `mouse`
    - Unsupported: mouse release
    - Unsupported: linked sketchpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
- `sequence`
- `sketchpad`
    - Unsupported: named elements
- `synth`
- `touch_response`


### Inline JavaScript

The `inline_javascript` item works similarly to the regular `inline_script` item, except that it runs JavaScript instead of Python code. Important considerations:

- You can get and set experimental variables using the `vars` object, which works similarly to the `var` object in Python.
- You cannot create `Canvas`, `Keyboard` objects, etc.
- The JavaScript workspace is not persistent. That is, if you define a variable in one script, it will not be accessible in another script. The only exception is the `vars` object, which is persistent.

Example:

``` .javascript
if (vars.subject_nr % 2 == 0) {
  vars.target_color = 'blue'
} else {
  vars.target_color = 'red'
}
```


### Upgrading OSWeb

OSWeb is under active development. If you want to make sure that you're running the latest version, you can upgrade the OSWeb extension, which is called `opensesame-extension-osweb`. As of OpenSesame 3.3, you can do this by running the following command in the console:

```
!conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

See also:

- %link:environment%


### Supported browsers

The following browsers are supported:

- Edge >= 17
- Firefox >= 52
- Google Chrome >= 49
- Internet Explorer >= 11
- Opera >= 56
- Safari >= 10

Certain extensions, such as Ad blockers or Script blockers, may prevent OSWeb from running.


## JATOS


<div class="alert alert-info" role="info">
Currently, you need to host your own JATOS installation to manage experiments.
</div>


### About JATOS

[JATOS] is a system for managing online experiments. It allows you to create accounts for experimenters, upload experiments, and generate links that you can distribute to participants. JATOS needs to be installed on your own web server. However, for testing purposes, you can use the [JATOS test server](https://www.jatos.org/JATOS-Tryout-Server.html) (%FigJatos1).

### Exporting your experiment to a JATOS study

- In OpenSesame, open the OSWeb extension (Menu → Tools → OSWeb)
- Click on 'Export experiment as JATOS study'
- Save your experiment as a `.zip` file

### Importing your experiment in JATOS

- In JATOS, click on 'Import study' (%FigJatos2)
- Select the `.zip` file that you have exported from OpenSesame
- Once the file has been uploaded to the server, JATOS will ask you to confirm that you want to import the study
- Click on 'Import' to confirm
- The study now appears in the list of studies on the left-hand side (%FigJatos3)

%--
figure:
 id: FigJatos1
 source: jatos-1.png
 caption: For testing purposes, you can use the JATOS test server.
--%


%--
figure:
 id: FigJatos2
 source: jatos-2.png
 caption: Click on 'Import study' and select the `.zip` file that you have exported with the OSWeb extension.
--%


%--
figure:
 id: FigJatos3
 source: jatos-3.png
 caption: Once the experiment has been successfully imported in JATOS, it appears in the list of experiments.
--%


## Downloading and converting data

If you have collected data with OSWeb through JATOS, you can download this data in JATOS by navigating to your experiment, clicking on Results, and then selecting Export Results → All (see %FigJatosExportResults).


%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: Exporting results collecting with OSWeb through JATOS.
--%


You will then download a file that has a name similar to `jatos_results_20190429113807.txt`. This file contains mostly JSON data, but may also contain fragments of data that render the file invalid as a regular JSON string. However, you can easily convert the data to a `.csv` or `.xlsx` file with 'Convert JATOS results to csv/ xlsx' option in the OSWeb extension (see %FigOSWebExtension).

## Sona Systems

Sona Systems is an online tool that many universities use for recruiting participants, granting course credit to student participants, etc. There is currently no direct way to integrate OSWeb with Sona Systems such that credits are automatically granted when a participant finishes the study. (We're working on this, and the documentation will be updated as soon as a solution is in place.) For now, the best options is to create a General Multiple Worker link in JATOS (see above), and have participants enter their student or Sona ID (or some other identifying feature) at the start of the experiment (see [this forum post](https://forum.cogsci.nl/discussion/5876/)).


## Tutorials

### Wisconsin Card Sorting Test

Learn how to implement the Wisconsin Card Sorting Test with OSWeb:

- %link:wcst%


### Video tutorial

%--
video:
 source: youtube
 id: OSWeb
 videoid: 0448NeoUaqU
 width: 644
 height: 362
 caption: |
  Run your OpenSesame experiment online!
--%


## Example experiments

- [Attentional capture](https://jatos.cogsci.nl/publix/20/start?batchId=50&generalMultiple)
- [Lexical decision](https://jatos.cogsci.nl/publix/39/start?batchId=54&generalMultiple)

A common question is how to collect multiple character input, for example to ask for a student number at the start of the experiment. See this forum discussion for a solution:

- <https://forum.cogsci.nl/discussion/5876/>


[jatos]: https://www.jatos.org/
[osweb]: http://github.com/shyras/osweb
[OSWeb extension for OpenSesame]: https://github.com/smathot/opensesame-extension-osweb
