title: OSWeb


[TOC]


## About OSWeb

OSWeb is an online runtime for OpenSesame experiments. It is a JavaScript library that executes OpenSesame experiments in a browser. To use OSWeb, you need the `opensesame-extension-osweb` package, which comes pre-installed with the Windows and macOS distributions of OpenSesame.


## Executing an Experiment in a Web Browser

To run an experiment in a web browser using OSWeb, follow these steps:

1. Open the Experiment Properties and select 'In a browser with OSWeb (osweb)' in the 'Run experiment' section.
2. Click any of the 'Run' buttons to start the experiment.
3. If the experiment is not compatible with OSWeb, an error message will appear that details the compatibility issues. (Refer to the 'supported functionality' section for more details.)
4. If there are no compatibility issues, the experiment will open in a new browser window. Note that even though the experiment is running in a web browser, it is still executing locally on your own computer. To host the experiment online, you need to publish it to [JATOS](%url:jatos%).
5. When the experiment is finished, the data will be downloaded in `.json` format. This data file can then be [converted to `.xlsx` or `.csv` format](%url:manual/osweb/data%) for further analysis.


%--
figure:
 id: FigTestRun
 source: testrun.png
 caption: Open the Experiment Properties and select 'In a browser with OSWeb (osweb)' under 'Run experiment'.
--%


## OSWeb control panel

For more control over OSWeb experiments, you can access the OSWeb and JATOS control panel from the Tools menu. This panel offers a range of configuration options:

- **Possible subject numbers:** When running an experiment from within JATOS, a subject number is randomly selected from this list. You can specify individual numbers using commas (e.g., '1,2,3') or number ranges (e.g., '1-10'). When running an experiment from within OpenSesame, this option does not apply, as the subject number is specified when the experiment starts.
- **Make browser fullscreen:** This option determines whether the browser should switch to fullscreen mode when an experiment starts within JATOS. If you're running an experiment directly from OpenSesame, this option is ignored; instead, you can run the experiment fullscreen by using the regular Run button, while the Quick Run button does not enable fullscreen.
- **Show OSWeb Welcome Screen:** This toggle controls whether participants will see a welcome screen before the experiment starts. The welcome screen can convey crucial information to participants. Additionally, it serves a technical purpose—due to browser-security policies, media playback and certain functionality is only available if the experiment is initiated by a user action. Therefore, it is generally recommended to leave this option enabled.
- **Bypass Compatibility Check:** Enabling this option allows you to run the experiment even when the OSWeb compatibility check fails. Note that doing so will not automagically resolve compatibility issues!
- **Welcome Text:** This field allows you to customize the welcome message displayed to participants on the welcome screen.
- **External Libraries:** This field lets you specify any external libraries that should be loaded with your experiment. The use of external libraries is explained in more detail in the section below.


%--
figure:
 id: FigOSWebControlPanel
 source: osweb-control-panel.png
 caption: The OSWeb and JATOS control panel offers a range of configuration options for your OSWeb experiments.
--%


## Supported functionality

When you run the experiment from within OpenSesame, a compatibility check is automatically performed. However, this check is fairly superficial. A more complete overview of supported functionality can be found below.


- `advanced_delay`
- `feedback`
    - See `sketchpad`
- `form_consent` (supported >= v1.4)
- `form_text_display` (supported >= 1.4)
- `form_text_input` (supported >= 1.4)
    - Unsupported: fullscreen mode
- `form_multiple_choice` (supported >= 1.4)
- `inline_html` (supported >= 1.4)
- `inline_javascript`
- `keyboard`
    - Unsupported: key release
    - Unsupported: HSV, HSL, and CIELab color spaces
- `logger`
- `loop`
    - Unsupported: resume after break
    - Unsupported: Disabling of evaluate on first cycle
    - Unsupported: constraints (pseudorandomization)
    - Supported >= 1.4: file source
- `mouse`
    - Unsupported: mouse release
    - Unsupported: linked sketchpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Supported >= 1.4.12: panning, pitch, and fade in
    - Supported >= 1.4.12: Sound playback on Safari on Mac OS or any browser on iOS
    - Unsupported: stop after
- `sequence`
- `sketchpad`
    - Unsupported: named elements
    - Supported >= 1.4: image rotation
    - Unsupported: HSV, HSL, and CIELab color spaces
- `touch_response`


The compatibility check may also indicate errors of the following type:

> The prepare phase for item new_logger is called multiple times in a row

This error results from how the experiment is structured, and specifically the use of linked copies. It's not always easy to understand where this error comes from, but you can read more about the prepare-run strategy in [this article](%url:prepare-run%). As a workaround, you can put the problematic items in a dummy LOOP, that is, a LOOP that simply calls the item once.


## Including external JavaScript packages

You can include external JavaScript packages by entering URLs to these packages (one URL per line) in the input field labeled 'External JavaScript libraries'. These packages are then included with `<script>` tags in the head of the HTML.

For example, you can include [WebGazer](%url:webgazer%) for in-browser by entering the following link:

```
https://webgazer.cs.brown.edu/webgazer.js
```


## Debugging

See:

- %link:debugging%
