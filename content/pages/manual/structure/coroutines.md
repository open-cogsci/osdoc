title: Doing things in parallel


Coroutines run multiple items in parallel—or, to be more exact, they run items in rapid alternation in a way that looks parallel. Not all items support coroutines.


[TOC]


## Using coroutines

You can use coroutines through the COROUTINES plugin (see %FigCoroutinesInterface).


%--
figure:
 source: FigCoroutinesInterface.png
 caption: The interface of the coroutines plugin.
 id: FigCoroutinesInterface
--%


As you can see, the COROUTINES plugin looks similar to the SEQUENCE item, but has a few extra options:

- *Duration* indicates the total duration of the coroutines.
- *End after item (optional)* indicates that the coroutines should end when a specific item has ended. This allows you, for example, to indicate that the coroutines should end when a key press has been collected, by selecting a KEYBOARD_RESPONSE item here.
- Each item has a *Start time*. Most items also have an *End time*. The end time does not apply to one-shot items; for example, SKETCHPADs show a display and terminate immediately, so they have no end time.

Specifically, the example from %FigCoroutinesInterface (from the stop-signal-task example) does the following:

- It shows a target display immediately.
- If the `stop_after` variable is not empty, it shows the stop_signal display after an interval specified by the `stop_after` variable.
- During the entire (2000 ms) interval, a keyboard response is collected.

The temporal flow is controlled by the COROUTINES plugin. Therefore, the timeout and duration values specified in the items are not used. For example, in %FigCoroutinesInterface, the KEYBOARD_RESPONSE will run for 2000 ms, regardless of the timeout that is specified in the item.


## Supported items

Currently, the following items are supported (this list may not be exhaustive):

- FEEDBACK
- INLINE_SCRIPT
- KEYBOARD_RESPONSE
- LOGGER
- MOUSE_RESPONSE
- SAMPLER
- SYNTH
- SKETCHPAD


## Using inline_script items in coroutines

When you use an INLINE_SCRIPT item in a COROUTINES, the Run phase works a little differently from what you might be used to. Specifically, the Run phase is executed on every iteration of the COROUTINES. In addition, the Run phase should only contain code that takes very little time to execute; this is because time-consuming operations will block the COROUTINES, thus interfering with the timing of other items in the COROUTINES as well. To end the COROUTINES, you can raise an `AbortCoroutines()` exception.

For example, say that you have a COROUTINES with two KEYBOARD_RESPONSE items, *kb1* and *kb2*, and you want to run the COROUTINES until two key presses have been collected, with a timeout of 5000 ms. You could then create the following COROUTINES structure:


%--
figure:
 source: FigCoroutinesTwoResponses.png
 caption: A coroutines that collects two keypress responses
 id: FigCoroutinesTwoResponses
--%

The *check_responses* INLINE_SCRIPT would then first set both responses variables to an empty string in the Prepare phase:

```python
# This is executed at the start of the coroutines
response_kb1 = ''
response_kb2 = ''
```

And then, in the Run phase, check if both variables have been set, and abort the coroutines if this is the case:

```python
# Values that are not an empty string are True for Python
# This code will be executed many times!
if response_kb1 and response_kb2:
    raise AbortCoroutines()
```

## Run-if expressions

The behavior of run-if expressions in COROUTINES is a bit different from that in SEQUENCE items. Specifically, run-if expressions in COROUTINES are evaluated during the prepare phase. See also:

- %link:prepare-run%
