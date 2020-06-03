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

If your experiment uses only supported functionality and runs normally in OpenSesame, then you can use the browser console to see JavaScript error messages. These are much less informative than OpenSesame's error messages, but they can still be helpful. Each browser has a different way to access the console. In Chrome, you can access the console by right-clicking somewhere, selecting Inspect (`Ctrl+Shift+I`), and then switching to the Console tab (see %FigChromeConsole). In Firefox, you can access the console by clicking on the Menu icon in the top right and then selecting Web Developer → Web Console (`Ctrl+Shift+K`).


%--
figure:
 id: FigChromeConsole
 source: chrome-console.png
 caption: Chrome's browser console.
--%



## Supported functionality

You can check whether your experiment is compatible with OSWeb using the Compatibility Check (%FigOSWebExtension). This compatibility check is fairly superficial. A more complete overview of supported functionality:

- `advanced_delay`
- `feedback`
    - Unsupported: named elements
- `inline_javascript`
- `keyboard`
    - Unsupported: key release
    - Unsupported: HSV, HSL, and CIELab color spaces
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
    - Unsupported: panning, pitch, stop after, and fade in
- `sequence`
- `sketchpad`
    - Unsupported: named elements
    - Unsupported: HSV, HSL, and CIELab color spaces
- `touch_response`

__Important note regarding linked copies:__ Having multiple linked copies of an item as part of the same SEQUENCE can result in the experiment freezing. This is a [known issue](https://github.com/smathot/osweb/issues/16), and we're working on this.


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

```
!conda update opensesame-extension-osweb -c cogsci -c conda-forge -y
```

See also:

- %link:environment%
