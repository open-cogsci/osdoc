title: Running experiments online with OSWeb


%--
video:
 source: youtube
 id: OSWeb
 videoid: -DHAX_EyKlE
 width: 644
 height: 362
 caption: |
  A series of video tutorials that shows the workflow for running experiments online.
--%


[TOC]


## The workflow


### Developing your experiment

First, you develop your experiment as you ordinarily would, using the OpenSesame desktop application. Not all functionality is available in online experiments. Notably, you cannot use Python INLINE_SCRIPT items, but have to use JavaScript INLINE_JAVASCRIPT items instead. During the development of your experiment, it is therefore important to check that your experiment is compatible with OSWeb.

- %link:manual/osweb/osweb%
- %link:manual/javascript/about%
- %link:manual/osweb/questionnaires%


### Uploading your experiment to JATOS

Once you have developed your experiment, you export it from OpenSesame and upload it to JATOS. JATOS is a web server that manages experiments: it allows you to generate links that you can distribute participants, and it stores data that has been collected.

There is not a single JATOS server. Rather, many institutions maintain their own JATOS server. In addition, <https://mindprobe.eu> is a free JATOS server, sponsored by ESCoP and OpenSesame.

- %link:jatos%


### Collecting data

One you have uploaded your experiment to JATOS, you can start collecting data. You can do this by manually sending links to participants, for example through email. Or you can use a platform for participant recruitment, such as Prolific, Mechanical Turk, or Sona Systems.

- %link:prolific%
- %link:mturk%
- %link:sonasystems%


## Tutorial

Learn how to implement the Wisconsin Card Sorting Test with OSWeb:

- %link:wcst%
