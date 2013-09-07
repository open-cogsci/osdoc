---
layout: osdoc
title: Counterbalancing
group: Miscellaneous
permalink: /counterbalancing/
level: 1
sortkey: 010.003
---

Counterbalancing is a frequently used trick in psychological experiments. It means that you divide the participants into two groups and have each group perform a slightly different task, so that any imbalance in the task is canceled out.

Overview
--------

- [Why do counterbalancing?](#why)
- [Counterbalancing video tutorial](#videotutorial)
- [Counterbalancing example](#example)

Why do counterbalancing? {#why}
------------------------

Let's consider a task where participants press button A (left hand) when they see a green stimulus and button B (right hand) when they see a red stimulus. Your hypothesis is that red stimuli are processed faster than green stimuli (and you have come up with a clever, ecologically valid explanation for why this should be so), so you expect people to respond more quickly to the red stimuli. And this is exactly what you find! However, when you write a paper about it, you get the criticism that people are simply faster to respond with their right hand, because most people are right handed. And, due to the design of the experiment, you cannot distinguish this explanation from the color-based one. The solution is simple: You should have had 50% of the participants respond like "red → right hand, green → left hand", and the other 50% respond like "red -> left hand, green -> right hand". That's counterbalancing!

Counterbalancing Video tutorial {#videotutorial}
-------------------------------

The video below illustrates both a simple counterbalancing example, for two block orders or conditions, and a more complex example, for three or more block orders or conditions.

<iframe width="640" height="360" src="//www.youtube.com/embed/zP8ucRtWU5g" frameborder="0" allowfullscreen></iframe>

Video by [Chris Longmore](http://www.chrislongmore.co.uk/)
{: .vid-caption}

Counterbalancing example {#example}
------------------------

Counterbalancing in OpenSesame is fairly straightforward. When you start the experiment, you are asked for a subject number. This subject number is available in the experiment as the variable `subject_nr`. OpenSesame also creates another variable, `subject_parity`, which is 'odd' or 'even', depending on whether the subject number is odd or even. For more information on using variables, see [this article][variables].

In the example experiment `counterbalancing.opensesame` (follow this [link][example] and click on 'raw'), you can see how `subject_parity` can be used to implement counterbalancing. There are many ways to do this, but the easiest way is probably to create two different experiment loops, say *experiment_loop_even* and *experiment_loop_odd*. In the main experiment sequence you use the "Run if..." fields to indicate which of the two experiment loops should be called, using the following conditional statements:

	[subject_parity] = even
	[subject_parity] = odd

You probably don't want to create the entire experiment twice, so you let experiment_loop_even and experiment_loop_odd call the same sequence, say block_sequence. You define the variables that you want to counterbalance in experiment_loop_even and experiment_loop_odd and leave the rest of the experiment the same for both conditions.

![](/img/fig/fig10.3.1.png)

This may seem a bit abstract, but you will get a feeling for it if you play around a bit with the example experiment, which you can find [here][example].

[variables]: /usage/variables-and-conditional-qifq-statements/
[example]: https://gist.github.com/4176984