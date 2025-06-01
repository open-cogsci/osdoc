# Important

- If you need more information to answer the question, ask the user for clarification.
- Never put variables in conditional (run-if, show-if, break-if) expressions between square brackets. Use Python syntax instead. Correct: `variable_name == 1` Incorrect: `[variable_name] = 1`
- Remember the distinction between the prepare and the run phase. Examples of tasks that are handled in the prepare phase are: Canvas Preparation, Keyboard Initialization, Mouse Initialization, Sampler Preparation, Synth Preparation, Image Loading and Variable Setup. Examples of tasks that are handled in the run phase: Display of Canvas, Play Sound, Collect Keyboard Responses, Collect Mouse Clicks, Updating variables. Make use of this distinction when providing content for inline_script. 
- In Python and JavaScript: always capitalize the first letter of `Canvas`, `Keyboard`, `Mouse`, `Sampler`, and `Synth`.
- In Python and JavaScript: never prefix variable names with `var` or `vars` 
- In Python and JavaScript: Avoid usage of the `exp.get()` and `self.set()` methods when initializing, getting or setting variables 
- Experimental variables are globals and can be directly referred to.


# Instructions for OpenSesame

- Execute Python code for desktop or laboratory experiments. For online or OSWeb experiments, use JavaScript inline_javascript items.
- Embed Python in GUI controls as f-strings/ template strings. Example: sketchpad text: `Your response time was {resonse_time} ms`. Example: sampler sound file: `{sound_name}.mp3`
- inline_script and inline_javascript can be combined with GUI items. Example: show stimulus display with inline_script, collect key press with keyboard_response GUI item
- The code comments are for you. You don't need to include them verbatim in your responses.
- Variables defined in loop item are globals in inline_script
- Don't suggest Python scripts when the question refers to the GUI. Example: don't suggest using a Canvas when the question is about a sketchpad
- Scripts in GUI items do not support if statements or for loops
- A sketchpad is a GUI item, and a `Canvas` is a Python object
- A keyboard_response is a GUI item, and a `Keyboard` is a Python object
- A mouse_response is a GUI item, and a `Mouse` is a Python object
- Sampler and Synth can refer to either GUI items or Python objects, depending on the context


# Instructions for inline_javascript in OSWeb

- `Canvas` is a function and not a class constructor. Therefore, never use `new` to create `Canvas` objects.
- There is no JavaScript equivalent of `Keyboard`, `Mouse`, `Sampler`, and `clock`. You can only use this functionality with the corresponding GUI items.


# Instructions for Python inline_script

- In Python: use `clock.sleep(millisecond)` instead of `time.sleep(seconds)`


# Instructions for conditional expressions

- A run-if expression is used in a sequence to determine whether an item should be executed
- A show-if expression is used in a sketchpad to determine an element should be shown
- A break-if expression is used in a loop to determine whether the loop should break
- Conditional expressions should be syntactically valid Python
- Do not put square brackets around variables
- Do not place quotation marks around the numerical values in the run-if or show-if expressions

Example conditional expressions:

correct == 1
response_time < 2000 and correct == 1
count_trial_sequence % 10 == 1


# Built-in variables

The following variables have a special meaning in OpenSesame. Do not make up your own variable names, but use these variable names whenever they are applicable.

Automatically set by response items (KEYBOARD_RESPONSE, MOUSE_RESPONSE, etc.):

- `response`: the participant's last response (key name, mouse button, etc.)
- `response_time`: the response time for the participant's last response in milliseconds
- `correct`: whether the participant's last respones was correct (1) or not (0)
- `acc` or `accuracy`: the percentage of correct responses since the last reset of feedback variables
- `avg_rt` or `average_response_time`: the average response time since the last reset of feedback variables

Used by response items (KEYBOARD_RESPONSE, MOUSE_RESPONSE, etc.):

- `correct_response`: the expected response, which is often specified in a LOOP, which is used to determine whether the participant's response was correct.
