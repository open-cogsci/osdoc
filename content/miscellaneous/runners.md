---
layout: osdoc
title: Runners
group: Miscellaneous
permalink: /runners/
parser: academicmarkdown
---

Runners are available as of 2.8.0.
{: .page-notification}

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## About runners

There are several technically different ways in which you can execute your experiment. Each of these corresponds to a *runner*. You can select a runner from the Preferences section (%FigPreferences). If you experience stability issues, you can try whether selecting a different runner resolves the issues.

%--
figure:
 id: FigPreferences
 source: preferences.png
 caption: You can select a runner from the Preferences section.
--%

## Available runners

### multiprocess

The *multiprocess* runner executes your experiment in a different process of the same application. The benefit of this approach is that your experiment can crash without bringing the user interface down with it.

### inprocess

The *inprocess* runner executes the experiment in the same process as the user interface. The benefit of this approach is its simplicity. The downside is that the user interface may crash if the experiment crashes, and vice versa.

### external

The *external* runner executes the experiment by launching [opensesamerun] as a separate application. The benefit of this approach is that your experiment can crash without bringing the user interface down with it.

[opensesamerun]: /usage/opensesamerun