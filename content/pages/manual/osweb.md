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


### Testing the experiment in a browser

- In OpenSesame, open the OSWeb extension (Menu → Tools → OSWeb).
- The extension will perform a simple (and incomplete) check to see if your experiment appears to be compatible with OSWeb.
- If no problems are detected, click 'Test experiment in external browser'.
- This will open the experiment in your default browser so that you can check if the experiment runs as expected (%FigTestRun).


%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: The welcome screen of OSWeb when testing the experiment in a browser.
--%


### Supported functionality

The following items are supported by OSWeb:

- `advanced_delay`
- `feedback` (named elements not supported)
- `inline_javascript`
- `keyboard` (key release not supported)
- `logger`
- `loop` (except 'Resume after break', 'Evaluate on first cycle', and 'file' source)
- `mouse` (mouse release not supported; linked sketchpad not supported)
- `notepad` (does nothing)
- `repeat_cycle`
- `reset_feedback`
- `sampler`
- `sequence`
- `sketchpad` (named elements not supported)
- `synth`
- `touch_response`


### Inline JavaScript

The `inline_javascript` item is available as of OSWeb 1.3
{: .page-notification}

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

OSWeb is under active development. If you want to make sure that you're running the latest version, you can upgrade the OSWeb extension by running the command below in the OpenSesame debug window. This may require you to run OpenSesame as administrator on Windows.

~~~
!pip install opensesame-extension-osweb --upgrade
~~~


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

## Video tutorial

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


[jatos]: https://www.jatos.org/
[osweb]: http://github.com/shyras/osweb
[OSWeb extension for OpenSesame]: https://github.com/smathot/opensesame-extension-osweb
