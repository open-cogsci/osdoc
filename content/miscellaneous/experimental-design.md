---
layout: osdoc
title: Experimental design
group: miscellaneous
permalink: /experimental-design/
---

## Overview

%--
toc:
 mindepth: 2
 maxdepth: 2
 exclude: [Overview]
--%

## Experimental design

Going from an abstract research question to a concrete experimental design can be difficult. You can clarify the design for yourself by writing it down in formal notation. There are many such notations, but here we will use the one proposed by [Rouanet and Lepine (1977)][references]. This notation is simple, yet flexible enough to cover most experimental designs that you will encounter in real life.

In this notation, conditions (or factors) are denoted by a single letter, with a small number that indicates how many levels there are. For example, if you have three stimulus durations, you might indicate this as D<sub>3</sub>. A special condition is 'subject'. If you have *N* subjects, you indicate this as <u>S</u><sub>N</sub>. It might sound strange to refer to subject as a condition, but, in a sense, that's exactly what it is.

There are two operators:

- &lt; &gt; indicates 'boxing in', typically used for conditions that are varied between subjects
- × indicated 'crossing', typically used for conditions that are varied within subjects

There are often multiple ways to write an experimental design. For example, you can omit conditions that are not relevant to your research question, such as whether a stimulus appears on the left or right side of the display.

## Within-subject designs

In a within-subject design, all participants do all conditions. This the most powerful kind of design, because it doesn't suffer much from variability between participants: You can compare the performance of a participant in condition A with his or her performance in condition B.

Consider a Posner cuing paradigm [(Posner, 1980)][references], in which an arrow points to the left or right side of the display. The arrow is followed by a target, which also appears on the left or right side of the display. We thus have two conditions that are varied within participants:

- *cue side* with two levels (left, right), or C<sub>2</sub>
- *target side* with two levels (left, right), or T<sub>2</sub>

We can write this design as <u>S</u><sub>N</sub>×C<sub>2</sub>×T<sub>2</sub>

## Between-subject designs

In a between-subject design, different participants do different experimental conditions. This is less powerful than a within-subject design, because differences between participants are an important source of noise: If the performance of participant 1 in condition A is better than that of participant 2 in condition B, you don't know whether this due to a condition effect, or simply because participant 1 tends to perform better than participant 2. For this reason, between-subject designs require a large number of participants.

Consider [Bargh's (1996)][references] famous (and controversial) social-priming experiment in which some participants read words that are associated with old age (e.g. 'retired'), whereas other participants read age-neutral words (e.g. 'thirsty').

We thus have one condition that is varied between participants:

- *prime type* with two levels (old, neutral), or P<sub>2<sub>

We can write this design as <u>S</u><sub>N</sub> &lt; P<sub>2</sub> &gt;

Rouanet and Lepine call this *emboîtement*, or 'boxing in'. This simply means that both levels of P have their own group of N subjects. Therefore, the total number of subjects is 2*N.

## Complicated designs

Occasionally, you will encounter more complicated designs that are not easily classified as either within- or between-subject. Psycholinguistic experiments are good examples of this.

Let's consider a semantic priming experiment, in which a target word is preceded either by a semantically related prime (e.g. 'garden' -> 'flower' or 'cat' -> 'dog') or an unrelated prime (e.g. 'money' -> 'flower' or 'yes' -> 'dog'). To avoid that a participant sees one word multiple times, you can 'rotate' the conditions between words:

- Odd participants (1, 3, 5, etc.) do rotation A:
    - 'flower' is in the related condition
    - 'dog' is in the unrelated condition
- Even participants (2, 4, 6, etc.) do rotation B:
    - 'flower' is in the unrelated condition
    - 'dog' is in the related condition

We thus have two conditions:

- *prime type* with two levels (related, unrelated), or P<sub>2</sub>; this is varied within subjects
- *rotation* with two levels (A, B), or R<sub>2</sub>; this is varied between participants

Therefore, the design is <u>S</u><sub>n</sub> &lt; R<sub>2</sub> &gt; × P<sub>2</sub>

## Limitations

This notation has several limitations, including:

- You cannot indicate how often certain conditions occur. For example, in a Posner cuing task, valid trials (i.e. cue and target on the same side) generally occur more often than invalid trials (i.e. cue and target on opposite side). This cannot be written down in the notation described here.
- It is difficult to indicate the role of 'item' in a design. For example, in the design under [Complicated designs], the target word plays a role that is similar to that of participant. It is possible to write an item-centric design or a participant-centric design (as in the example), but I have not found a way to satisfactorily do both.

## References

Bargh, J. A., Chen, M., & Burrows, L. (1996). Automaticity of social behavior: Direct effects of trait construct and stereotype activation on action. *Journal of Personality and Social Psychology*, *71*(2), 230.
{: .reference}

Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, *32*(1), 3–25. doi:10.1080/00335558008248231
{: .reference}

Rouanet, H., & Lepine, D. (1977). Structures linéaires et analyse des comparaisons. *Mathématiques et Sciences Humaines*, *56*, 5–46. Retrieved from: <http://www.numdam.org/item?id=MSH_1977__56__5_0>
{: .reference}
