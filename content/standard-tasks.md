---
layout: osdoc
title: Standard tasks
group: General
permalink: /standard-tasks/
parser: academicmarkdown
singleton: true
---

This page provides an overview of standard tasks with a high re-use potential that have been implemented in OpenSesame.

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Available tasks

### CombiTVA

This is an open implementation of the CombiTVA paradigm [(Vangkilde, Bundesen & Coull, 2011)](http://dx.doi.org/10.1007/s00213-011-2361-x) in OpenSesame.

- __Developer:__ Martin Papenberg
- __URL:__ <https://github.com/crsh/combitva>
- __License:__ [GPL-2]
- __Citation:__ Papenberg, M. & Aust, F. (2014). *An open implementation of the CombiTVA paradigm in OpenSesame*. Retrieved from <https://github.com/crsh/combitva>

### Conjunctive continuous performance task

Conjunctive Continuous Performance Task (CCPT) is a sustained attention test developed and validated by [Shalev et al (2011)](http://www.sciencedirect.com/science/article/pii/S002839321100251X). This is the visual variant of the CCPT implemented in OpenSesame. Available in English and German.

- __Developer:__ Krzysztof J. Gorgolewski
- __URL:__ <https://github.com/NeuroanatomyAndConnectivity/ConjunctiveContinuousPerformanceTask>
- __License:__ ?
- __Citation:__ Gorgolewski., K. J. (2014). *Conjunctive Continuous Performance Task (CCPT)*. Retrieved from <https://github.com/NeuroanatomyAndConnectivity/ConjunctiveContinuousPerformanceTask>

### Mini version of the New York Cognition Questionnaire

New York Cognition Questionnaire (NYC-Q) is a questionnaire probing the content and form of self generated thoughts (mindwandering). This is a minimal version of the NYC-Q suitable for using after behavioural tests or resting state fMRI scans. Available in English and German.

- __Developer:__ Krzysztof J. Gorgolewski
- __URL:__ <https://github.com/NeuroanatomyAndConnectivity/NYC-Q/blob/master/scripts/questionnaire/inscanner-NYCQ.opensesame>
- __License:__ ?
- __Citation:__ Gorgolewski., K. J. (2014). *Mini version of the New York Cognition Questionnaire (min-NYC-Q)*. Retrieved from <https://github.com/NeuroanatomyAndConnectivity/NYC-Q/blob/master/scripts/questionnaire/inscanner-NYCQ.opensesame>

### Mouse-tracking

[Spivey, Grosjean and Knoblich (2005)](http://www.pnas.org/content/102/29/10393) introduced the mouse-tracking paradigm, in which participants' mouse trajectories are recorded as they move the cursor from a starting point to click on one of two or more responses. The path of the mouse cursor can be analysed to infer instantaneous attraction towards competing responses over the course of a trial.

- __Developer:__ Eoin Travers
- __URL:__ <http://eointravers.github.io/blog/2014/03/os-mousetracking/>
- __License:__ ?
- __Citation:__ Travers, E. (2014) *OpenSesame mouse-tracking script*. Retrieved from <http://eointravers.github.io/blog/2014/03/os-mousetracking/>


## Adding your own task

If you have implemented a task that you feel has a high re-use potential, we want to know about it! You can have your task included in this list in two ways:

1. Edit this page on GitHub, add your experiment, and send a pull request. To do this, you need to have a GitHub account.
	- This page on GitHub: <https://github.com/smathot/osdoc/blob/master/content/standard-tasks.md>
	- Instructions on how to edit a page: [/contribute/documentation](/contribute/documentation)
2. Or drop a note on the forum to let us know about your experiment.
	- <http://www.cogsci.nl/forum/index.php?p=/discussion/823/>

Please provide the following information:

1. A description of your task.
2. A (list of) developer(s).
3. A URL where people can download the task.
4. Citation information.
5. A license, such as the [GPL-3].

For tips on how to develop a Git-friendly experiment, see:

- [/miscellaneous/git](/miscellaneous/git)

[gpl-2]: http://www.gnu.org/licenses/gpl-2.0.html
[gpl-3]: https://www.gnu.org/copyleft/gpl.html
