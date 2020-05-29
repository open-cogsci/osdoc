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


## Prolific

[Prolific](https://prolific.co/) is a commercial tool for recruiting participants for research. To run OSWeb experiments on Prolific, you need to follow the steps below:


### Create a study on JATOS

First, import your experiment into JATOS, as described above. Next, go the Worker & Batch Manager, activate the General Multiple Worker, get a URL by clicking on Get Link, and copy it (%FigJatosURL).


%--
figure:
 id: FigJatosURL
 source: jatos-url.png
 caption: Get a study URL from JATOS.
--%



### Create a study on Prolific

Next, create a study on Prolific. Under Study Details (%FigProlific), insert the JATOS study URL in the field labeled "What is the URL of your study?". This will tell Prolific how to start the experiment. Importantly, add the following to the end of the URL (this will pass important information from Prolific to your experiment):

```
&PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
```

When the experiment is finished, Prolific needs to know about it. For this purpose, Prolific uses an End Redirect URL, which is listed in the field labeled "To prove that participants have completed your study …". Copy this End Redirect URL. Also check the box labeled "I've set up my study to redirect to this url at the end".

%--
figure:
 id: FigProlific
 source: prolific.png
 caption: Study details on Prolific.
--%



### Set an End Redirect URL in JATOS

Now go back to JATOS, and open the Properties of your study (%FigJatosProperties). There, paste the End Redirect URL that you have copied from Prolific in the field labeled "End Redirect URL". This will tell JATOS that the participant should be redirected back to Prolific when the experiment is finished, so that Prolific knows that the participant completed the experiment.


%--
figure:
 id: FigJatosProperties
 source: jatos-properties.png
 caption: Set the End Redirect URL in JATOS.
--%


### Register Prolific information in your experiment

Every participant from Prolific is identified by a unique ID. It's important to log this ID in your experiment, because this allows you to tell which participant from Prolific corresponds to which entry in the JATOS results. You can do this by adding the script below in the Prepare phase of an `inline_javascript` item at the very start of your experiment.

When running the experiment through Prolific, this will make the Prolific ID available as the experimental variable `prolific_participant_id`. When the running the experiment in any other way (e.g. during testing), the variable `prolific_participant_id` will be set to -1. The same logic applied to the Prolific Study ID (`prolific_study_id`) and the Prolific Session ID (`prolific_session_id`).


```javascript
if (window.jatos && jatos.urlQueryParameters.PROLIFIC_PID) {
    console.log('Prolific information is available')
    vars.prolific_participant_id = jatos.urlQueryParameters.PROLIFIC_PID
    vars.prolific_study_id = jatos.urlQueryParameters.STUDY_ID
    vars.prolific_session_id = jatos.urlQueryParameters.SESSION_ID
} else {
    console.log('Prolific information is not available (setting values to -1)')
    vars.prolific_participant_id = -1
    vars.prolific_study_id = -1
    vars.prolific_session_id = -1
}
console.log('prolific_participant_id = ' + vars.prolific_participant_id)
console.log('prolific_study_id = ' + vars.prolific_study_id)
console.log('prolific_session_id = ' + vars.prolific_session_id)
```


### Test the study

Go back to the Study Details page on Prolific. At the bottom of the page, there is a Preview button. This allows you to test the experiment by acting as a participant yourself. Don't forget to check the JATOS results to make sure that the experiment has successfully finished, and that all the necessary information (including the Prolific information) has been logged!


## Sona Systems

Sona Systems is an online tool that many universities use for recruiting participants, granting course credit to student participants, etc. There is currently no direct way to integrate OSWeb with Sona Systems such that credits are automatically granted when a participant finishes the study. (We're working on this, and the documentation will be updated as soon as a solution is in place.) For now, the best options is to create a General Multiple Worker link in JATOS (see above), and have participants enter their student or Sona ID (or some other identifying feature) at the start of the experiment (see [this forum post](https://forum.cogsci.nl/discussion/5876/)).


## Downloading and converting data

If you have collected data with OSWeb through JATOS, you can download this data in JATOS by navigating to your experiment, clicking on Results, and then selecting Export Results → All (see %FigJatosExportResults).


%--
figure:
 id: FigJatosExportResults
 source: jatos-export-results.png
 caption: Exporting results collecting with OSWeb through JATOS.
--%


You will then download a file that has a name similar to `jatos_results_20190429113807.txt`. This file contains mostly JSON data, but may also contain fragments of data that render the file invalid as a regular JSON string. However, you can easily convert the data to a `.csv` or `.xlsx` file with 'Convert JATOS results to csv/ xlsx' option in the OSWeb extension (see %FigOSWebExtension).


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
