title: OSWeb


[TOC]


## About OSWeb

OSWeb is an online runtime for OpenSesame experiments. That is, it is a JavaScript library that interprets and executes OpenSesame experiments.


## The OSWeb extension

The OSWeb extension for OpenSesame (%FigOSWebExtension) allows you to test experiments in a browser, and to export experiments in a format that you can import into [JATOS](%url:jatos%).


%--
figure:
 id: FigOSWebExtension
 source: osweb-extension.png
 caption: The OSWeb extension for OpenSesame.
--%


## Testing in a browser

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


## Debugging

First, make sure that your experiment only uses supported functionality, as described below. Next, run the experiment in the traditional (non-browser) way in OpenSesame. This will give you the most informative error messages that you can use for debugging.

If your experiment uses only supported functionality and runs normally in OpenSesame, then you can use the browser console to see JavaScript error messages. These are much less informative than OpenSesame's error messages, but they can still be helpful. Each browser has a different way to access the console. In Chrome, you can access the console by right-clicking somewhere, selecting Inspect (`Ctrl+Shift+I`), and then switching to the Console tab (see %FigChromeConsole). In Firefox, you can access the console by clicking on the Menu icon in the top right and then selecting Web Developer → Web Console (`Ctrl+Shift+I`).

If you're using INLINE_JAVASCRIPT items in your experiment, the browser console is also a powerful way to debug your scripts, as described here:

- %link:manual/javascript/about%


%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: Chrome's browser console.
--%



## Supported functionality

You can check whether your experiment is compatible with OSWeb using the Compatibility Check (%FigOSWebExtension). This compatibility check is fairly superficial. A more complete overview of supported functionality can be found below.

__Important__: A lot of supported functionality was added in OSWeb 1.4. Therefore, check your version of OSWeb against the version notes in the list below.

- `advanced_delay`
- `feedback`
    - See `sketchpad`
- `form_consent` (unsupported <= v1.3)
- `form_text_display` (unsupported <= v1.3)
- `form_text_input` (unsupported <= v1.3)
- `form_multiple_choice` (unsupported <= v1.3)
- `inline_html` (unsupported <= v1.3)
- `inline_javascript`
- `keyboard`
    - Unsupported: key release
    - Unsupported: HSV, HSL, and CIELab color spaces
- `logger`
- `loop`
    - Unsupported: resume after break
    - Unsupported: Disabling of evaluate on first cycle
    - Unsupported: constraints (pseudorandomization)
    - Unsupported <= v1.3: file source
- `mouse`
    - Unsupported: mouse release
    - Unsupported: linked sketchpad
- `notepad`
- `repeat_cycle`
- `reset_feedback`
- `sampler`
    - Unsupported: panning, pitch, stop after, and fade in
- `sequence`
- `sketchpad`
    - Unsupported: named elements
    - Unsupported <= v1.3: image rotation
    - Unsupported: HSV, HSL, and CIELab color spaces
- `touch_response`


The compatibility check may also indicate errors of the following type:

```bash
The prepare phase for item new_logger is called multiple times in a row
The run phase for item new_logger is called multiple times in a row
```

This error results from how the experiment is structured, and specifically the use of linked copies. It's not always easy to understand where this error comes from, but you can read more about the prepare-run strategy in [this article](%url:prepare-run%). As a workaround, you can put the problematic items in a dummy LOOP, that is, a LOOP that simply calls the item once.


## Supported browsers

The following browsers are supported:

- Edge >= 17
- Firefox >= 52
- Google Chrome >= 49
- Internet Explorer >= 11
- Opera >= 56
- Safari >= 10

Certain extensions, such as Ad blockers or Script blockers, may prevent OSWeb from running.


## Upgrading OSWeb

OSWeb is under active development. If you want to make sure that you're running the latest version, you can upgrade the OSWeb extension, which is called `opensesame-extension-osweb`. As of OpenSesame 3.3, you can do this by running the following command in the console:

```bash
conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

Or:

```bash
pip install opensesame-extension-osweb --upgrade
```

See also:

- %link:environment%
