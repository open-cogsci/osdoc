# How to update packages in OpenSesame

To update OpenSesame, take the following steps:

1. Launch OpenSesame. An automatic updater will starting checking for updates in the background. This may take a few minutes.
2. If no updates are available, nothing will happen.
3. If updates are available, a green update button marked "Install updates …" will appear in the main toolbar.
3. Click the green update button to open the automatic updater.
4. Within the automatic updater, review the script that indicates which packages will be updated. If necessary, modify the script.
5. Click the 'Run update script' button to perform the updates. The updates will be executed in the OpenSesame console.
6. Once the updates have been completed, restart OpenSesame.

# How to create an animated Canvas with Python inline_script

To create an animated Canvas with Python inline_script, you can dynamically update the properties of Canvas elements in between subsequent calls to `show()`. For example, to create an animation of a moving circle, you could use the following script:

```python
animated_canvas = Canvas()
animated_canvas['circle'] = Circle(x=-100, y=0, r=10)
for x in range(-100, 101):
    animated_canvas['circle'].x = x
    animated_canvas.show()
    clock.sleep(10)
```

# How to avoid the last display of a trial from being shown for too long

If a visual stimulus is shown at the end of a trial, it is not automatically removed when the trial ends. Rather, it stays on the screen until a new display is shown at the start of the next trial, which due to intertrial preparation time may take a while. As a result, if a trial ends with a KEYBOARD_RESPONSE, the experiment can seem not react to the key press. To avoid this, simply add a blank SKETCHPAD at the end of the trial. This will ensure that the trial ends with a blank display, and avoid the experiment from feeling sluggish or delayed to the participantl.


# How to register key presses continuously while presenting a series of sketchpad items

If you want to register key pressed continuously, while at the same presenting a series of sketchpad items, you need to use a `coroutines` item. This allows you to run multiple items (seemingly) in parallel. For example:

1. Insert a `coroutines` item into the trial sequence.
2. Set the duration of the `coroutines`, for example to 5000 ms.
3. Add a `keyboard_response` to the `coroutines` and let it run for the entire duration of the `coroutines` by setting the start time to 0 and the end time to 5000 ms.
4. Add multiple `sketchpad` items to the `coroutines` and use the start times for these items to show them at the appropriate moments.


# How to create a Run-Only File in OpenSesame

In some cases, you want to provide participants with a file that they can execute directly in order to start the experiment. There are a few ways to do this:

- Export the experiment to HTML using the OSWeb and JATOS control panel. This will generate a single HTML file that participants can double-click to launch it in a browser. This requires that the experiment is compatible with OSWeb.
- Create a Windows batch file that uses opensesamerun to launch the experiment directly. This requires that the participant is running Windows. The best way to do this is to create your own version of the 'no installation required' `zip` package of OpenSesame, and include the batch file in this package.
   ```
    opensesamerun your_experiment.osexp -s 1 -l your-logfile.csv -f
   ```
- Create a Python script that launches the experiment directly using OpenSesame as a Python module. This requires a Python environment with OpenSesame installed, and a way to easily launch the Python script.
   ```
    from libopensesame.python_workspace_api import Experiment
    exp, win, clock, log = Experiment(osexp_path='my_experiment.osexp', subject_nr=2)
    exp.run()
    ```

In all cases, provide clear instructions to the participant on how they can launch the experiment!

# How to run OpenSesame on Windows 7

The last version of Python to support Windows 7 was Python 3.8. Because the OpenSesame packages for Windows are built using Python 3.11, they do not run on Windows 7. To run OpenSesame on Windows 7:

- Download the last version of Anaconda (2019.10) that supports Windows 7 from here: <https://docs.anaconda.com/free/anaconda/install/old-os/>
- In Anaconda, create a Python 3.8 environment:
    ```
    conda create -n opensesame_py38 python=3.8
    ```
- Inside this Anaconda environment, install OpenSesame as explained on the download page: <https://osdoc.cogsci.nl/4.0/download/#anaconda-cross-platform>
- You can now start OpenSesame from this Anaconda environment.


# How to give feedback on the participant's accuracy

Understanding the meaning of the variables `acc`, `accuracy`, `correct`, and `correct_response`:

- The correct response is stored in the variable `correct_response`. This variable needs to be defined in the experiment, for example in the table of the BLOCK_LOOP, and contains for example the name of the key that the participant is supposed to press on a trial. If `correct_response` is defined, response items such as the KEYBOARD_RESPONSE, will automatically determine whether a response is correct.
- The participant's accuracy is stored in the variable `acc` and `accuracy` (which are aliases) as a percentage value between 0 and 100.
- The participant's accuracy is a running average since the last reset of feedback variables.
- Feedback variables can be reset by the FEEDBACK and RESET_FEEDBACK items.
- The correctness of the participant's last response is stored as the variable `correct` as 1 (correct) or 0 (incorrect).

To provide feedback on the participant's accuracy (percentage correct) after several trials:

- Add a RESET_FEEDBACK item at the point from which you want to provide feedback. This can for example be at the start of each block, as the first item in the *block_sequence*, in case you want to provide feedback per block.
- At the end of each block, add a FEEDBACK item with the text: `Your accuracy was {acc}%`.

To provide feedback on the participant's correctness (correct vs incorrect) after each trial:

- Add two SKETCHPAD items to the end of the *trial_sequence*.
- Rename one SKETCHPAD to *correct_sketchpad* and add content that you want to show after a correct response, such as a green fixation dot.
- Rename the other SKETCHPAD to *incorrect_sketchpad* and add content that you want to show after an error, such as a red fixation dot.
- In the *trial_sequence*, use run-if expressions to show the correct SKETCHPAD depending on the participants response. For *correct_sketchpad* this should be `correct == 1`. For *incorrect_sketchpad* this should be `correct == 0`.


# How to log variables that are defined in a Python INLINE_SCRIPT item

The LOGGER item determines which variables are logged the first time that it is executed. The LOGGER cannot automatically detect variables that will be defined later on in a Python INLINE_SCRIPT. Therefore, if you define a new variable in a Python INLINE_SCRIPT item after a LOGGER item has already been executed, this new variable will not be included in the log file. To work around this, you can add an initializing script to the start of the experiment and already assign a dummy value to the variable there, so that the LOGGER will be aware that the variable exists:
    ```python
    my_future_variable = 'some dummy value'
    ```


# How to change the language in OpenSesame

To change the language of the user interface in OpenSesame:

1. Go to Menu → Tools → Preferences.
2. In the Preferences window, select the 'Common settings' tab.
3. In the section 'Application appearance', under 'Language', choose your desired language from the dropdown menu.
4. The '[Default]' language corresponds to the language of the operating system.
5. Restart OpenSesame to have the change take effect.


# How to debug errors when running an experiment in a browser with OSWeb

When an OSWeb experiment doesn't run as expected, there are a few things that you can do:

1. Make sure that you are running the latest versions of OpenSesame and OSWeb. OpenSesame 4 has an automatic updater, which will notify you of any available updates. This notification may take a few minutes to appear after you have started OpenSesame.
2. Check for error messages in the browser console. See also: <https://osdoc.cogsci.nl/4.0/manual/debugging/>
3. Make sure that your experiment is compatible with OSWeb. See also: <https://osdoc.cogsci.nl/4.0/manual/osweb/osweb/>


# How to give feedback by showing an image after a response, with the specific image depending on which key was pressed

To provide feedback by showing an image after a response:

1. Insert a KEYBOARD_RESPONSE item in the *trial_sequence* to collect a key press.
2. In the "Allowed responses" field of the KEYBOARD_RESPONSE, specify which keys should be accepted. This should be a semicolon-separated list, for example "left;right".
3. After the KEYBOARD_RESPONSE, insert one SKETCHPAD item for each feedback image that might be presented. For example, you might create a *left_sketchpad* item that shows the image `left_feedback.png`, and a *right_sketchpad* item that shows the image `right_feedback.png`. The image files should be in the file pool.
4. In the *trial_sequence*, use Run-If expressions to determine which item should be run on a given trial: `response == "left"` for *left_sketchpad* and `response == "right"` for *right_sketchpad*. The `response` variable is automatically set by the KEYBOARD_RESPONSE item.


# How to use a pandas DataFrame for the loop table

The data structure used by LOOP items is a DataMatrix, which is an alternative to pandas DataFrame and a bit more light-weight and intuitive. If you want to use a pandas DataFrame to populate a LOOP table, you first need to convert it to a DataMatrix, and then assign it to the `dm` property of the LOOP item. You need to do this in the Prepare phase of an INLINE_SCRIPT that comes before the LOOP item that it modifies.

```python
import pandas as pd
from datamatrix import convert as cnv

# Create a dummy DataFrame with two rows and one column called `cond`
df = pd.DataFrame(data=dict(cond=['a', 'b']))
# Convert the DataFrame to a DataMatrix and assign it to the loop table of
# the block_loop item
items['block_loop'].dm = cnv.from_pandas(df)
```


# How to fix a blank screen or "Your browser does not support WebGL" message when starting an OSWeb experiment in a browser

OSWeb requires WebGL, which is a technology for rendering visual stimuli in a browser. If your browser or operating system does not support WebGL, the experiment will not run. Usually, you will see an error message stating that "Your browser does not support WebGL". Sometimes you will simply see a blank screen, in which case you can check the browser console for specific error messages.


# How to convert Python inline_script to inline_javascript for OSWeb

When converting Python inline_script from a lab-based experiment to inline_javascript for an OSWeb experiment in a browser, a few things are important:

- Certain classes objects and objects are not available in inline_jascript. Specifically, there is no javascript equivalent of `Keyboard`, `Mouse`, `Sampler`, and `clock`. Therefore, equivalent GUI items must be used instead. For example, you cannot Python inline_script that uses a Keyboard object to an inline_javascript object; instead, you have to use the KEYBOARD_RESPONSE item in the GUI.
- JavaScript is asynchronous, which means it is not possible to implement function calls that block or pause execution.


# How to run an OSWeb experiment without an internet connection

OSWeb experiments are typically run online using a JATOS server such as MindProbe.eu. However, it is also possible to run an OSWeb experiment without an internet connection (offline):

- Make sure that the experiment is compatible with OSWeb
- Open Menu -> Tools -> OSWeb and JATOS control panel
- Click 'Export to HTML'
- Save the resulting HTML file somewhere
- Open the HTML experiment file in a browser to start it
- When the experiment is done, the data will appear as a download in the browser


# How to pass variables as URL parameters to an OSWeb experiment

You can pass variables to an OSWeb experiment that runs online in a browser as URL parameters. If the experiment is hosted on a JATOS server, the parameter is available in `jaros.urlQueryParameters`. If the experiment is running as a standalone HTML file (e.g. during testing), the parameter is available through the `URLSearchParams` class.

The example below shows how you can get the `task` URL parameter in a way that works both when running the experiment through JATOS and when running it standalone.

```js
// Check if the task was passed a url parameter through JATOS
if ((typeof jatos !== 'undefined') && ('task' in jatos.urlQueryParameters)) {
    task = Number(jatos.urlQueryParameters['task'])
    console.log(`task ${task} was specified as a JATOS URL query`)
// Else check if it was passed as a regular parameter (for testing)
// and fall back to 0 if no parameter was specified.
} else {
    const urlParams = new URLSearchParams(window.location.search)
    task = Number(urlParams.get('task') || 0)
    if (task === 0) {
        console.log('no task was specified')
    } else {
        console.log(`task ${task} was specified as a regular URL query`)
    }
}
```


# How to pass variables from an OSWeb experiment to another URL

If you are hosting an OSWeb experiment on a JATOS server, you can specify an end-redirect URL. This URL is a link that is opened when the experiment is successfully completed. This is generally used to communicate to a participant platform such as Prolific, MTurk, or Sona Systems that the participant has completed the experiment. You can also include URL parameters in this link like this: `https://endredirect.url/?task=[task]`. In this example, `task` is assumed to be a URL query parameter that was passed to JATOS when the experiment was launched, and is automatically included in the end-redirect url.


# How to draw onto a SKETCHPAD's Canvas using INLINE_JAVASCRIPT in OSWeb

Each SKETCHPAD in OSWeb has a canvas property. It is possible to draw onto this using INLINE_JAVASCRIPT. However, this requires hacking into the OSWeb internals. So this may break in the future, and you should only do this if any other solution is impractical!

The trick is to create an empty Canvas in an inline_javascript item, and then change it's internal _canvas property to the canvas of a sketchpad . You would need to do this after the sketchpad has been prepared, but before it has actually been shown. Here's the general idea (using the canvas from *my_sketchpad*):

```js
sketchpadItem = 'my_sketchpad'  \\ the name of the sketchpad item
myCanvas = Canvas()
myCanvas._canvas = runner._itemStore._items[sketchpadItem].canvas
myCanvas.text({'text': 'Some additional text!'})
```


# How to make sure that whitespace is taken into account when calculating text size

Whitespace at the end or start of a text string is not normally taken into account when calculating text size, because the size is based on the visible part of the text. 

A trick to work around this is by using a visible character, and then give this character the color of the background. For example, the text string below would appear as though there is a space between 'before' and 'after', altough really it's an underscore that's not visible because it has the background color. The main reason to do this is to make sure that trailing or starting whitespace is taken into account when calculating the text size.

```
before<span style="color:{background};">_</span>after
```


# How to fix problems when trying to update packages using conda

The automatic updater generates a `conda` command to update a selection of relevant packages. You can also manually use `conda` to update packages in the OpenSesame environment, which is really an Anaconda environment. If problems occurs during updating, then this may happen for a number of reasons. For example, the Anaconda environment may be corrupted, or there may be dependency issues (conflicts) between packages. Points to consider:

- `conda` often recommends updating `conda` itself. If update problems only happens when you try to manually update the `conda` package itself, then you can usually ignore this. There is usually no reason to update `conda` itself.
- If update problems also happen when you try to perform the update script that is suggested by the automatic updater of OpenSesame itself, then that's problematic because you won't be able to update important packages. In that case, you can consider redownloading OpenSesame so that you can start from a clean environment.
- The error message often contains useful information. Including this in your question is helpful.


# How to check for updates

It often takes a long time before update notifications appear after starting OpenSesame. However, the updater always starts checking immediately when OpenSesame is started. The reason that it takes so long for is that conda, which manages the packages (together with pip ), is very slow. For this reason, there's no option to deliberately check for updates.
