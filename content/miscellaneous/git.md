---
layout: osdoc
title: Git and versioning
group: Miscellaneous
permalink: /git/
parser: academicmarkdown
---

This functionality requires OpenSesame 2.8.2, which is currently under development.
{: .page-notification}

Using a version-control system, such as [Git], is good practice when developing experiments.

## Overview

%--
toc:
 mindepth: 2
 excludes: [Overview]
--%

## Setting up a Git-friendly experiment

OpenSesame's default `.opensesame.tar.gz` file format is inconvenient for versioning, because Git is unable to look inside the archive to inspect changes. But with some clever tricks you can nevertheless set up a Git-friendly OpenSesame experiment.

### Save your experiment in .opensesame format

The `.opensesame` format is a plain-text format and is therefore suitable for version control.

### Use a static file-pool folder

The downside of using the `.opensesame` format is that it doesn't save the file pool along with the experimental script. To work around this, put all the files that you would normally put in the file pool in a subfolder called `__pool__`. OpenSesame will automatically treat this folder as part of the file pool.

### Create an export script that creates a .opensesame.tar.gz file

To share your experiment it is convenient to use the `.opensesame.tar.gz` format, because it bundles all experimental files into a single file. You can easily create a Python script that exports your Git-controlled experiment to a single `.opensesame.tar.gz` file. For an example, see `release.py` in the [Example project].

## Example project

An example project can be found here:

- <https://github.com/smathot/OpenSesame-Git-Demonstration>

[git]: http://git-scm.com/
