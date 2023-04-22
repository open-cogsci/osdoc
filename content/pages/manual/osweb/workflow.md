title: Running experiments online with OSWeb


[TOC]


## The workflow

For an introduction to the workflow, see also:

<notranslate>
Mathôt, S., & March, J. (2022). Conducting linguistic experiments online with OpenSesame and OSWeb. *Language Learning*. doi:10.1111/lang.12509
<br /><small>[Related preprint (not identical to published manuscript)](https://doi.org/10.31234/osf.io/wnryc)</small>
</notranslate>


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


## Tutorials

- %link:tutorials/intermediate-javascript%
- %link:wcst%
