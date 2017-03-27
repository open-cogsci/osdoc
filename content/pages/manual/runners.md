title: Runners


[TOC]


## About runners

There are several technically different ways in which you can execute your experiment. Each of these corresponds to a *runner*. You can select a runner under Menu → Tools → Preferences → Runner.

Unless you have a reason not to, you should use the *multiprocess* runner. However, if OpenSesame sometimes crashes, you can try whether selecting a different runner resolves this.


## Available runners

### Multiprocess

The *multiprocess* runner executes your experiment in a different process. The benefit of this approach is that your experiment can crash without bringing the user interface down with it. Another advantage of the *multiprocess* runner is that it allows the variable inspector to show your experimental variables while the experiment is running.

### Inprocess

The *inprocess* runner executes the experiment in the same process as the user interface. The benefit of this approach is its simplicity. The downside is that the user interface may crash if the experiment crashes, and vice versa.

### External

The *external* runner executes the experiment by launching opensesamerun as a separate application. The benefit of this approach is that your experiment can crash without bringing the user interface down with it.
