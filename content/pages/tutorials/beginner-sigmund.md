title: SigmundAI tutorial: gaze cuing

[TOC]


## About this tutorial

In this tutorial, you will learn how to use SigmundAI effectively as an OpenSesame copilot. This tutorial is based on the [the beginner tutorial](%url:beginner%).


## What you'll need

This tutorial assumes that you are running OpenSesame 4.1 with all the latest updates applied. If you see a notification that "Some packages can be updated (…)", click on the "Install updates …" button to open the update panel, and then on "Run update script" to perform the actual updates. After updating, restart OpenSesame.

AI does not replace human understanding! If you are new to OpenSesame, I recommend to start with the [beginner tutorial](%url:beginner%) before proceeding with this tutorial. The beginner tutorial provides you with the basic understanding of OpenSesame that is necessary to collaborate effectively with Sigmund.

This tutorial assumes that you have a subscription to [SigmundAI](https://sigmundai.eu/).


## Connecting OpenSesame to Sigmund

Sigmund is an AI research assistant, powered by the same state-of-the-art AI technology that is used by ChatGPT+, Anthropic Claude, and Mistral LeChat. Sigmund has expert knowledge of OpenSesame, and integrates with the OpenSesame user interface. Because of these features, it is a much more effective copilot for OpenSesame than other chatbots are.

To connect OpenSesame to Sigmund, simply log into [sigmundai.eu](https://sigmundai.eu). The Sigmund panel in OpenSesame will automatically connect:

<video controls width="100%">
  <source src="/video/sigmund-connect.mp4" type="video/mp4">
</video>


## The experiment

In this tutorial, you will create a gaze-cuing experiment as introduced by [Friesen and Kingstone (1998)][references]. In this experiment, a face is presented in the center of the screen (%FigGazeCuing). This face looks either to the right or to the left. A target letter (an 'F' or an 'H') is presented to the left or right of the face. A distractor stimulus (the letter 'X') is presented on the other side of the face. The task is to indicate as quickly as possible whether the target letter is an 'F' or an 'H'.

%--
figure:
 id: FigGazeCuing
 source: gaze-cuing.png
 caption: |
  The gaze-cuing paradigm [(Friesen and Kingstone, 1998)][references] that you will implement in this tutorial. This example depicts a trial in the incongruent condition, because the smiley looks at the distractor ('X') and not at the target ('F').
--%


## Step 1: Create the main sequence

The experiment consists of a practice and an experimental phase. Instruction screens are shown before and after each phase. Let's ask Sigmund to implement the basic structure of the experiment for us. Use a clear and concrete prompt that tells Sigmund exactly what you need! It is also important to tell Sigmund what you do *not* need; otherwise Sigmund may do more than you asked for, for example by adding content to an item when you only asked Sigmund to create the item.

💬 Prompt:

```text
Hi Sigmund! I would like to implement a gaze-cuing experiment together in OpenSesame. To get started, can you help me implement the basic structure of the experiment? It should look like this:

- experiment (sequence)
  - instructions (form_text_display)
  - practice_loop (loop)
    - block_sequence (sequence)
  - end_of_practice (form_text_display)
  - experimental_loop (loop)
    - block_sequence (sequence)
  - end_of_experiment (form_text_display)
  
Please don't add any content to the items yet. We'll get to that later!
```

When Sigmund has built the structure, we can ask him to make sure that there are no redundant items left. (Sigmund may already have removed the unnecessary items, in which case of course you don't need to ask it again!) And to give the experiment a useful name. It's best to ask this in a separate prompt, so that we don't overwhelm Sigmund with many separate instructions in a single prompt! Sigmund easily gets confused if you ask it to do too many things at once.

💬 Prompt:

```text
Great! Now please also remove any unnecessary items. And give the experiment a sensible title.
```

The overview area of your experiment now looks like %FigStep1. (The experiment title may be different).

%--
figure:
 id: FigStep1
 source: step1.png
 caption: |
  The overview area at the end of the step 1.
--%


<div class='info-box' markdown='1'>

__Keep Sigmund in check!__

At the bottom of the Sigmund panel, you can choose whether or not you want to explicitly review Sigmund's actions. When this option is enabled, you need to approve every action that Sigmund wants to take, such as selecting an item or changing an item's script. You can disable this for a smoother workflow. But remember that Sigmund makes mistakes, so it's important to double-check the results!

</div>


## Step 2: Create the block sequence

The *block_sequence* corresponds to a single block of trials. Each block of trials starts by resetting all feedback variables to avoid performance from previous blocks carrying over, followed by a loop with a trial sequence inside it, and ends with a feedback display. We can ask Sigmund to build this structure for us.

💬 Prompt:

```text
Awesome! Now I'd like to add content to the block_sequence. The block_sequence should be shared (i.e. a linked copy) between the practice and the experimental phase. I would like it to be structured as follows:

- block_sequence (sequence)
  - reset_feedback (reset_feedback)
  - block_loop (loop)
    - trial_sequence (sequence)
  - feedback (feedback)
  
Again, please don't add content to the items. We'll flesh those out later. Is that clear? If so, let's go!
```

The overview of your experiment now looks like %FigStep2.

%--
figure:
 id: FigStep2
 source: step2.png
 caption: |
  The overview area at the end of Step 2.
--%


## Step 3: Fill the block loop with independent variables

Independent variables, such as experimental conditions, are typically defined in the block loop (at least when they are varied from trial to trial). In our case, we have three independent variables:

- `gaze_cue`: left or right.
- `target_pos`: -300 or 300 (x-coordinate where 0 is the center and negative is left)
- `target_letter`: F or H
- `dist_pos`: opposite from `target_pos`
- `correct_response`: z when `target_letter` is F and m otherwise

To make sure that Sigmund understands what kind of experimental design we have in mind for the block loop, provide clear instructions.

💬 Prompt:

```text
Can you define the following variables in the block loop? Please consider that this is a 2 (left or right) by 2 (-300 or 300) by 2 (F or H) design, so that the loop should have 8 rows in total.

- `gaze_cue`: left or right.
- `target_pos`: -300 or 300 (x-coordinate where 0 is the center and negative is left)
- `target_letter`: F or H
- `dist_pos`: opposite from `target_pos`
- `correct_response`: z when `target_letter` is F and m otherwise

Clear? Go!
```

The *block_loop* now looks like %FigStep3.

%--
figure:
 id: FigStep3
 source: step3.png
 caption: "The *block_loop* at the end of Step 3."
--%


<div class='info-box' markdown='1'>

__Choose an AI model that works for you!__

Sigmund is not itself an AI model. Rather, it is an chatbot that is built on top of an AI model. And you can choose which AI model should be used. In the browser interface of Sigmund, you can select a range of AI models. This tutorial was tested with Claude 4.5 Sonnet and GPT-5 for conversations.

You can experiment with different models to see which works best for you. Consider that problem-solving models are slow, environmentally unfriendly, and provide only neglibable improvements on most tasks.

</div>


## Step 4: Add images and sound files to the file pool

For our stimuli, we will use images from file. In addition, we will play a sound if the participant makes an error. For this we need a sound file.

Download the required files and add them to the file pool (Sigmund cannot do this):

- [gaze_neutral.png](/img/beginner-tutorial/gaze_neutral.png)
- [gaze_left.png](/img/beginner-tutorial/gaze_left.png)
- [gaze_right.png](/img/beginner-tutorial/gaze_right.png)
- [incorrect.ogg](/img/beginner-tutorial/incorrect.ogg)


Your file pool now looks like %FigStep4. Remember to save your experiment regularly.

%--
figure:
 id: FigStep4
 source: step4.png
 caption: "The file pool at the end of Step 4."
--%


## Step 5: Fill the trial sequence with items

Now let's ask Sigmund to implement the trial sequence. We'll focus only on the general structure for now, and get back to the items later.

💬 Prompt:

```text
Now let's add items to the trial sequence.

- fixation_dot (sketchpad)
- neutral_gaze (sketchpad)
- gaze_cue (sketchpad)
- target (sketchpad)
- keyboard_response (keyboard_response)
- incorrect_sound (sampler) Only after an icorrect response.
- logger (logger)

As before, don't add any content to the items. We'll do that later. Is that clear? Go!
```

I already mentioned that Sigmund sometimes makes mistakes. This would be a good moment to check whether Sigmund implemented the structure correctly!

For me, while writing this tutorial, Sigmund indeed made two mistakes while performing the task above. First, even though it confidently asserted that the *incorrect_sound* item was configured to play only after an incorrect response, he did not actually add the corresponding run-if expression to the trial sequence. Second, the logger wasn't added.

%--
figure:
 id: FigSigMistake
 source: sigmund-makes-mistake.png
 caption: "Oops! Sigmund forgot to add a logger and to define a run-if expression for incorrect_sound."
--%


Why did this happen? Mistakes are unpredictable, so in part this was simply bad luck. But Sigmund struggles with tasks that require a large number of actions. The task above, even though conceptually simple, required no fewer than nine consecutive actions: one for each of the seven newly created items, one to select the trial sequence, and one to add the run-if expression to the trial sequence. When asking Sigmund to perform multi-action tasks, be especially on guard for mistakes!

Now let's kindly remind Sigmund to finish the job. By providing very concrete instructions, we prevent more mistakes.

💬 Prompt (your prompt will be different, depending on whether and what kind of mistake Sigmund made):

```text
It seems that the logger is still missing. Coul you add it please? And once you're done with that, please select the trial sequence and add the run-if expression for the sampler. (Remember that a run-if expression for an item is not defined in the item itself, but rather in the sequence that contains the item.)
```

The *trial_sequence* now looks like %FigStep5.

%--
figure:
 id: FigStep5
 source: step5.png
 caption: "The *trial_sequence* at the end of Step 5."
--%


## Step 6: Draw the sketchpad items

We're now going to draw the SKETCHPAD items, starting with the fixation dot. Our stimuli are white, which means that we need to specify that the experiment uses a white background and a black foreground color.

💬 Prompt:

```text
Could you please change the experiment settings so that we use black stimuli on a white background? And then add a fixation dot to the fixation-dot item. And change the duration of the fixation dot to 745 ms.
```

Next, the display containing the neutral gaze. Sigmund is usually smart enough to infer that the neutral gaze is an image from the file pool (but check!).

💬 Prompt:

```text
Awesome! Now the neutral gaze please! The duration should again be 745 ms.
```

Next, the gaze cue. Again, Sigmund is usually smart enough to infer that the gaze cue is an image from the file pool, and that the `gaze_cue` variable (defined in the block loop) indicates which image should be shown (but check!).

💬 Prompt:

```text
Perfect! And now implement the actual gaze cue. It should be shown for 495 ms.
```

And finally the target.

💬 Prompt:

```text
Spot on! And now the target. The target display should also contain the gaze cue. In addition, the target letter should be shown either on the left or the right, depending on its defined position. On the other side, there should always be an 'X'.
```

Sigmund should have understood that the duration of the target should be 0, because the next item is a keyboard response. But mistakes happen easily, so double-check!


## Step 7: Configure the keyboard response item

Steps 7 through 12 are self-explanatory!

💬 Prompt:

```text
As for the resonse: I would like to have a response timeout of 2000 ms, and only valid keys should be accepted.
```


## Step 8: Configure the incorrect (sampler) item

💬 Prompt:

```text
Awesome. Can you now define the incorrect sound?
```


## Step 9: Draw the feedback item
 
💬 Prompt:

```text
Can you add participant feedback about the accuracy and average response time after each block of trials?
```


## Step 11: Set the length of the practice phase and experimental phase

💬 Prompt:

```text
I would like to have 2 practice blocks followed by 8 experimental blocks. Please define a `practice` variable (yes or no) so that later I can tell apart practice and experimental blocks later.
```


## Step 12: Write the instruction, end_of_practice and end_of_experiment forms

💬 Prompt:

```text
Awesome! Could you now add some clear and concise instructions as well as informative messages at the end of the practice phase and the end of the experiment? Use your good judgment as to the content of these messages!
```


## Step 13: Test and debug the experiment!

You're now ready to give the experiment a test run! For me, while writing this tutorial, I immediately got an error:


%--
figure:
 id: FigFStringError
 source: fstringerror.png
 caption: "Computer says no."
--%


This error results from the fact that end-of-practice item refers to the variable `acc`, which is not yet defined at the moment that this item is prepared. Sigmund is easily confused by the [distinction between the prepare phase and the run phase](%url:prepare-run%), but was able to correct the issue when I clicked 'Ask Sigmund to fix this error'. (In fact I had to ask twice: once for the end-of-practice item and once for the end-of-experiment item.)

✅ Done!

💬 Prompt:

```text
Thank you Sigmund!
```


## References

<div class='reference' markdown='1'>

Friesen, C. K., & Kingstone, A. (1998). The eyes have it! Reflexive orienting is triggered by nonpredictive gaze. *Psychonomic Bulletin & Review*, *5*, 490–495. doi:10.3758/BF03208827

Mathôt, S., Schreij, D., & Theeuwes, J. (2012). OpenSesame: An open-source, graphical experiment builder for the social sciences. *Behavior Research Methods*, *44*(2), 314-324. doi:10.3758/s13428-011-0168-7

Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509

</div>

[references]: #references