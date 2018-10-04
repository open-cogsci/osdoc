title: Running experiments online


<div class="alert alert-warning" role="alert">
OSWeb is under active development and not ready for use in production
</div>


[TOC]


## OSWeb

### About OSWeb

[OSWeb] is an online runtime for OpenSesame experiments. That is, it is a JavaScript library that interprets and executes OpenSesame experiments.


### Installing the OSWeb extension

The [OSWeb extension for OpenSesame] allows you to test experiments in a browser, and to export experiments in a format that you can import into JATOS (desribed below). The extension is available on PyPi as `opensesame-extension-osweb` and can be installed as described here:

- %link:environment%


### Testing the experiment in a browser

- In OpenSesame, open the OSWeb extension (Menu → Tools → OSWeb).
- The extension will perform a simple (and incomplete) check to see if your experiment appears to be compatible with OSWeb.
- If no problems are detected, click 'Test experiment in external browser'.
- This will open the experiment in your default browser so that you can check if the experiment runs as expected.

### Supported functionality

The following items are supported by OSWeb:

- `advanced_delay`
- `feedback` (named elements not supported)
- `keyboard` (key release not supported)
- `logger`
- `loop`
- `mouse` (mouse release not supported; linked sketchpad not supported)
- `notepad` (does nothing)
- `repeat_cycle`
- `reset_feedback`
- `sampler`
- `sequence`
- `sketchpad` (named elements not supported)
- `synth`
- `touch_response`


## JATOS

### About JATOS

[JATOS] is a system for managing online experiments. It allows you to create accounts for experimenters, upload experiments, and generate links that you can distribute to participants. JATOS needs to be installed on your own web server. However, for testing purposes, you can use the [JATOS test server](https://www.jatos.org/JATOS-Tryout-Server.html).

### Exporting your experiment to a JATOS study

- In OpenSesame, open the OSWeb extension (Menu → Tools → OSWeb)
- Click on 'Export experiment as JATOS study'
- Save your experiment as a `.zip` file

### Importing your experiment in JATOS

- In JATOS, click on 'Import study'
- Select the `.zip` file that you have exported from OpenSesame
- Once the file has been uploaded to the server, JATOS will ask you to confirm that you want to import the study
- Click on 'Import' to confirm
- The study now appears in the list of studies on the left-hand side


[jatos]: https://www.jatos.org/
[osweb]: http://github.com/shyras/osweb
[OSWeb extension for OpenSesame]: https://github.com/smathot/opensesame-extension-osweb
