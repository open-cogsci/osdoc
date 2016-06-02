title: File format (.osexp)

[TOC]

## The .osexp format

OpenSesame experiments are saved in `.osexp` format. What a `.osexp` file is depends on whether there are files included with the experiment, that is, whether or not the file pool is empty.

## If the file pool is empty

If the file pool is empty, the experiment is saved as a plain-text file. This file is utf-8 encoded and uses Unix-style line endings. You can edit and view this file in most text editors.

The OpenSesame-script syntax is described here:

- %link:opensesame-script%

## If the file pool is not empty

If there are files in the file pool, the experiment is saved as a `.tar.gz` file, which is a `.zip`-like file format. Within this file, you will find the following:

- `script.opensesame` is the experimental script, in the same format as described above
- `pool/` is a folder that contains all the files in the file pool. Any non-ascii characters in the file names are replaced by `U+XXXX` strings.

## What happened to the .opensesame and .opensesame.tar.gz formats?

You can still open the `.opensesame` and `.opensesame.tar.gz` format, which was used for OpenSesame <= 2.9.X. However, you can no longer save experiments in this format.
