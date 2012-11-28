---
layout: osdoc
title: Giving feedback to participants
group: Usage
permalink: /giving-feedback-to-participants/
level: 1
sortkey: 004.008
---

You will often want to provide participants with feedback, to let them know how well they are doing. As a courtesy towards the participants, because most people find it unpleasant to perform a task without getting feedback, and also to improve the participants' motivation. In OpenSesame there are lots of ways to provide feedback. Here I will give you a few pointers.

Outline
-------

- [The difference between feedback and sketchpad items](#difference)
- [Relevant variables](#relevant-variables)
- [Feedback after a block of trials](#after-block)
- [Feedback after a single trial](#after-trial)
- [Manipulating feedback variables in an inline_script](#inline-script)

The difference between feedback and sketchpad items <a id='difference'></a>
---------------------------------------------------

You may have noticed that feedback and sketchpad items are very similar. They both provide a drawable canvas that can be used as a stimulus display during the experiment. The crucial difference lies in the phase during which the canvas is constructed.

For a sketchpad item, the canvas is constructed during the prepare phase of the sequence of which it is part. This is done to reduce the possibility of timing glitches, because constructing a canvas can take a bit of time, especially when it contains many and/ or complex stimuli. Consequently, the contents of a sketchpad cannot depend on what happens during the sequence, after the sketchpad has been prepared. Therefore, sketchpads are not very well suited to provide feedback.

In contrast, for feedback items, the canvas is constructed when it is shown. Therefore, it may take some time for a feedback item to actually appear on the screen, it should not be used for presenting time critical stimuli. But, on the bright side, the contents of a feedback item can depend on what happened just before. Therefore, feedback items are well suited to provide feedback.

Relevant variables <a id='relevant-variables'></a>
------------------

For a description of all relevant variables, see the sections *Response variables* and *Feedback variables* in [this article][variables].

Feedback after a block of trials <a id='after-block'></a>
--------------------------------

It is common to provide feedback after every block of trials. This way you don't overwhelm the participant with feedback on every trial, which tends to disrupt the flow of the experiment (although it may be useful in some cases). To do this, construct a sequence that contains a single block of trials (typically a loop item), followed by a feedback item. It is also convenient to add a *reset_feedback* item just before the *block_loop*. This prevents carry-over effects, for example, from responses that have been collected during the instructions.

![](/img/fig/fig4.8.1.png)

In the feedback item, you can add some text. You can use the variables described above using the *[variable name]* notation.

![](/img/fig/fig4.8.2.png)

You can also use an *inline_script* item, inserted immediately before the *feedback item*, to provide custom types of feedback. For example, if you want to provide a warning when accuracy drops below 75% you could insert the following inline_script before the feedback item.

{% highlight python %}
if self.get('acc') > 90:
	exp.set('feedback_msg', 'Excellent, well done!')
elif self.get('acc') > 75:
	exp.set('feedback_msg', 'Pretty good')
else:
	exp.set('feedback_msg', 'Come on, you can do better!')
{% endhighlight %}
	
For more information about using inline_script items, see [this article][inline-script].

Feedback after a single trial <a id='after-trial'></a>
-----------------------------

Sometimes you may want to give the participant feedback after every trial. It's probably wise to use subtle feedback in this case, so you don't disrupt the flow of the experiment. What I often do is briefly (500 ms, say) present a green or red fixation dot, depending on whether the participant responded correctly. The easiest way to do this is to add both a red and a green fixation dot to the trial sequence, and execute one of them, depending on the value of the `correct` variable.

![](/img/fig/fig4.8.3.png)

In this case, you can use a sketchpad item, because you don't change the contents of the canvas depending on the participant's response. You only change which of the two sketchpads, both of which have been constructed in advance, will be shown: “green_fixation” or “red_fixation”.

You can also present full feedback after every trial, using a feedback item inserted after the response item (such as a keyboard_response), as shown in Figure 5.



Resetting and manipulating feedback variables <a id='inline-script'></a>
---------------------------------------------

Feedback variables, such as `average_response_time` and `accuracy` are reset when a feedback item is called in which the *Reset feedback variables* box is checked, and wherever you insert a reset_feedback plug-in. However, you can also manipulate the feedback variables using an inline_script.

For example, the following script resets the feedback variables:

{% highlight python %}
exp.set('total_responses', 0)
exp.set('total_correct', 0)
exp.set('total_response_time', 0)
exp.set('average_response_time', 'NA')
exp.set('avg_rt', 'NA')
exp.set('accuracy', 'NA')
exp.set('acc', 'NA')
{% endhighlight %}

And the following script updates the feedback variables based on a response:

{% highlight python %}
response_time = 1000 # Assume that the RT was 1000ms
correct = 1 # Assume that the response was correct

exp.set('total_responses', self.get('total_responses')+1)
exp.set('total_correct', self.get('total_correct')+correct)
exp.set('total_response_time', self.get('total_response_time')+response_time)

avg_rt = self.get('total_response_time')/self.get('total_responses')
acc = 100.*self.get('total_correct')/self.get('total_responses') 

exp.set('average_response_time', avg_rt)
exp.set('avg_rt', avg_rt)
exp.set('accuracy', acc)
exp.set('acc', acc)
{% endhighlight %}

[variables]: /usage/variables-and-conditional-qifq-statements/#built-in-variables