title: Use guided generation to create any experiment with SigmundAI

[TOC]


## About this tutorial

In this tutorial, you will learn how to build any experiment with SigmundAI. This is not a step-by-step tutorial focused on a specific experiment. Rather, it outlines a general workflow, which you can adjust based on your needs.

Don't expect miracles! If you have a complex experiment, Sigmund will likely struggle when left completely to its own devices. You often need to work actively together with Sigmund to implement an experiment.

I refer to this as *guided generation*, because you guide Sigmund through the process.

If you haven't worked with Sigmund yet, I recommend first completing [the beginner tutorial for SigmundAI](%url:beginner-sigmund%).


## What you'll learn

By the end of this tutorial, you'll know how to:

- 💡 Give Sigmund clear, effective instructions
- 💡 Break the process of building a complete experiment from scratch into manageable steps
- 💡 Fix mistakes that Sigmund may make while building an experiment.


## Which model should I use?

Most steps do not require a particularly powerful model. I mostly use Z.ai GLM 5.2, which at the time of writing provides a good balance between intelligence and cost. However, the final implementation step is pushing the limits of what most AI models can do. Therefore, at this point you can switch to a more powerful model, such as Claude Sonnet 5. Do consider that more powerful models are also (much) more expensive.

In practice, try out different models to see what gives the best results for your specific experiments.


## Workflow

Here's what we're going to do:

1. Describe the experiment you want to build in clear language.
2. Ask Sigmund to develop your description into a comprehensive narrative description that specifies the experiment in full detail.
3. Review the comprehensive description. If necessary, discuss and adjust it.
4. Ask Sigmund to develop a JSON specification (a human-readable technical format) that describes the experimental structure.
5. Review the JSON specification. If necessary, discuss and adjust it.
6. Ask Sigmund to build the entire experiment at once.
7. Test and polish the experiment.

This tutorial is about communicating effectively with Sigmund. We're going to help Sigmund to subdivide the complex task of building an experiment into manageable subtasks, and provide concrete instructions of what to do when.

__Important:__ You need to talk to Sigmund through the chat panel inside OpenSesame. If you use the web interface, Sigmund will not be able to control OpenSesame.


## Developing a comprehensive narrative description of the experiment

Here's the experiment description we'll use for this example:

💬 **Description:**

```text
A typical visual-working-memory task where circles of different colors need to be remembered. One circle is probed by presenting a circle of either the same or a different color at the original circle's location. The participant responds with a same/different judgment. Set size is varied.
```

We start by asking Sigmund to flesh out a detailed description of an experiment based on this description. In your experiment description, provide as many details as you can, because this helps Sigmund come up with a design that matches what you have in mind. For example, if you think the trial logic should be implemented with an `inline_script`, indicate this.

We include this description in a prompt that provides clear instructions to Sigmund:

💬 **Prompt:**

```text
I have a challenging task for you! We're going to implement an OpenSesame experiment from scratch. We'll break the process down in a few steps to make things manageable. In the current step, your task is to expand the description of the experimental task so that it contains all the details that we need to implement it.

Here are some things to consider for the trial structure:

- The way in which participants respond
- The timing of the stimuli
- The appearance of the stimuli
- The layout of the stimuli
- Whether participant feedback is provided and if so how
- Any stimuli that are not explicitly mentioned but that should be included
- Blank or fixation displays in between stimuli (if there is a fixation dot, it is usually shown throughout the trial)

Here are some things to consider for the experiment structure:

- Independent and dependent variables
- Whether or not there is practice phase
- Whether or not the trials are subdivided into blocks of trials
- The number of trials and (if applicable) blocks
- Any welcome, instruction, and goodbye screens

Please also include any additional information that you think is relevant.

<experimental_task_description>
A typical visual-working-memory task where circles of different colors need to be remembered. One circle is probed by presenting a circle of either the same or a different color at the original circle's location. The participant responds with a same/different judgment. Set size is varied.
</experimental_task_description>

Please reply with a comprehensive description. Do not save it as a note yet, because we are first going to review it.
```

Sigmund will reply with an elaborate description of the experiment. Review it and provide corrections if necessary. If you're happy, ask Sigmund to make a note of it.


💬 **Prompt:**

```text
Awesome! Please save the comprehensive description as a persistent note so you don't forget. Do not summarize it, but save it in full.
```


## Developing a JSON specification for the experimental structure

Now we're going to ask Sigmund to design the experimental structure. This specifies which items make up the experiment and how they are connected.

The second point of the prompt mentions which item types can be used. To help Sigmund, remove item types that you know won't be necessary. For example, if participants are not going to use the mouse to respond, you can remove the `mouse_response` item type.


💬 **Prompt:**

```text
Moving on! Here's your next task:

- Draft a JSON specification based on the narrative description of the experiment that you just saved as a note.
- Each dict in the JSON should correspond to a single OpenSesame item. You can use the following items: [loop, sequence, sketchpad, feedback, synth, sampler, keyboard_response, mouse_response, logger, inline_script, inline_javascript, form_multiple_choice, form_text_display, form_text_input, reset_feedback]
- Sketchpad items are prepared in advance, and can therefore not take into account variables that are defined after their prepare phase. Therefore, to show displays with variable content, you often want to use feedback items instead, but only for displays that are not time-critical.
- Do not use multiple unlinked logger items, because this will result in messy log files. Instead, use linked copies of the same logger.
- Do not put reset_feedback items in the main experiment sequence, because this is not compatible with OSWeb.
- Don't include any implementation details for the items. We'll get to that later. For now, just provide a description, name, and type. For items that are part of a sequence, you can also provide a run-if expression. For items that are linked copies of items that occur elsewhere, provide details for the first occurrence only, and provide only the name for subsequent occurrences (items with the same name are linked copies).
- Items that have child items have an additional 'items' field. A loop always has a single sequence as a child item. A sequence generally has multiple child items of various types.
- Please use linked copies of items whenever possible. To indicate that an item is a linked copy of another item, simply re-use the same name and add a `linked` field that is set to `true`.
- The example JSON specification below shows the general idea, but is highly simplified. Your JSON specification will likely be much more elaborate.

<json_example>
{
  "name": "experiment",
  "type": "sequence",
  "description": "A one line description of the task",
  "items": [
    {
      "name": "task_description",
      "type": "notepad",
      "description": "The full narrative description of the task goes here."
    },
    {
      "name": "welcome",
      "type": "sketchpad",
      "description": "Brief welcome message"
    },
    {
      "name": "block_loop",
      "type": "loop",
      "description": "A block of trials. Independent variables are defined here as well.",
      "items": [
        {
          "name": "trial_sequence",
          "type": "sequence",
          "description": "Sequence for a single trial",
          "items": [
            {
              "name": "fixation",
              "type": "sketchpad",
              "description": "Shows black fixation cross (+) for 500 ms"
            },
            {
              "name": "target_display",
              "type": "sketchpad",
              "description": "Shows target stimulus while the fixation cross remains visible"
            },
            {
              "name": "keyboard_response",
              "type": "keyboard_response",
              "description": "Collects participant response to target stimulus"
            },
            {
              "name": "correct_feedback",
              "type": "sketchpad",
              "description": "Shows green fixation dot for 500 ms after correct response",
              "run_if": "correct == 1"
            },
            {
              "name": "fixation",
              "linked": true
            },
            {
              "name": "logger",
              "type": "logger",
              "description": "Logs all trial data"
            }
          ]
        }
      ]
    }
  ]
}
</json_example>

Please reply with the JSON specification for the narrative description of the experiment. Do not save the JSON specification as a note yet, because we are first going to review it.
```

Sigmund will now provide a detailed JSON specification, which is essentially a technical view of the overview area in OpenSesame. Review the specification and provide feedback if necessary. If you're happy, ask Sigmund to make a note of it.

💬 **Prompt:**

```text
Beautiful, well done Sigmund! Please save this as another persistent note so you don't forget. Do not summarize it, but save it in full.
```


## Implementing the experiment

Now we're good to go! This final step pushes the limits of what most AI models can do. If you find that Sigmund consistently fails, try switching to a more powerful model. I have had success with Claude Sonnet 5.

💬 **Prompt:**

```text
We're now ready to implement the experiment. A few pointers:

- Save these instructions as a persistent note so you don't forget.
- Do *not* inspect items of the current experiment. They're not relevant, because we're going to completely overwrite the current experiment.
- Do *not* inspect the general script of the current experiment for the same reason.
- Before writing the experiment script, call `opensesame_get_syntax_documentation` with `save_as="note"` to get all relevant documentation.
- Finally, write the new experiment as a single complete general script and pass it to `opensesame_update_general_script`.

This is a challenging task, but I know you can do it. Let's go!
```

Sigmund manages to succesfully implement the visual-working-memory experiment used as an example. However, not all experiments will go smoothly.

If Sigmund notices that it made a syntax error in generating the experiment, it will try to fix it. Sigmund may get stuck in an infinite loop while trying to make things work. When this happens, abort the conversation.

If the experiment is succesfully generated, it may still contain mistakes or imperfections. Carefully test and polish it!


## Examples of experiments created with guided generation

For all of the examples below, the initial steps were done using Z.ai GLM 5.2, and the final implementation step was done using Claude Sonnet 5. I didn't provide any feedback on the comprehensive description or JSON specification. However, I did polish the final experiment as described in the notes below.


### Visual Working Memory

💬 **Description:**

```text
A typical visual-working-memory task where circles of different colors need to be remembered. One circle is probed by presenting a circle of either the same or a different color at the original circle's location. The participant responds with a same/different judgment. Set size is varied.
```

Notes:

- Sigmund used the deprecated `[square_brackets_syntax]` to refer to variables in SKETCHPAD items. This works, but I changed it to the preferred `{curly_brackets_syntax}`.
- Sigmund used Python INLINE_SCRIPT for this experiment. Therefore, it cannot be run in a browser.

Try the experiment:

- %static:attachments/sigmund/sigmund-visual-working-memory.osexp%


### Posner cuing

💬 **Description:**

```text
A Posner cuing paradigm with a central cue and a letter-discrimination task.
```

Notes:

- Sigmund used unicode markers (e.g. `\u2190`) for arrow cues. These are not rendered by OpenSesame, and needed to be replaced by the actual characters (e.g. '←').
- Sigmund used the deprecated `[square_brackets_syntax]` to refer to variables in SKETCHPAD items. This works, but I changed it to the preferred `{curly_brackets_syntax}`.

Try the experiment:

- %static:attachments/sigmund/sigmund-posner-cuing.osexp%
- [Run in browser](https://jatos.mindprobe.eu/publix/QgymMCSRYzL)


### AX continuous performance

💬 **Description:**

```text
An AX continuous performance task.
```

Notes:

- Sigmund forgot to set which items to run in the various `sequence` items. This needed to be manually fixed.

Try the experiment:

- %static:attachments/sigmund/sigmund-axcpt.osexp%
- [Run in browser](https://jatos.mindprobe.eu/publix/5s8TbGLx0bZ)
