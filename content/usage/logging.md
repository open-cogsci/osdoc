---
layout: osdoc
title: Logging and reading data files
group: Usage
permalink: /logging/
---

Always triple check whether your data has been correctly logged before running your experiment!
{: .page-notification}

%--
toc:
 mindepth: 2
--%

## Using the logger item

OpenSesame will not log your data automatically. Instead, you need to insert a *logger* item, typically at the end of your trial sequence.

%--
figure:
 id: FigLogger
 source: logger.png
 caption: |
  The `logger` item.
--%

The simplest way to use the `logger` is by leaving the 'Log all variables (recommended)' enabled. That way, all variables that OpenSesame knows about are written the log file.

If you find that some variables are missing, you can explicitly add the name of a custom variable, or drag a variable from the variable inspector into the `logger` table.

If you prefer to log only certain variables, you can disable the 'Log all variables' option, and indicate explicitly which variables you want to log.

In general, you should create only one logger item, and reuse that item at different locations in your experiment if necessary. If you create multiple logger items (rather than using a single logger multiple times), they will all write to the same log file, and the result will be a mess!

## Using Python inline script

You can write to the log file using the `log` object:

~~~ .python
log.write('This will be written to the log file!')
~~~

For more information, see:

- [/python/log/](/python/log/)

You should generally not write to the log file directly and use a `logger` item at the same time; doing so will result in messy log files.

## Format of the data files

If you have used the standard logger item, data files are in plain-text, comma-separated format, which can be opened in all popular spreadsheets. If you are looking for high quality, free spreadsheet software, take a look at [Libre Office][libreoffice], [OpenOffice.org][openoffice] or [Gnumeric][]. If you use Microsoft Excel, you may need to use the 'import' function to open the data files, because Excel may not properly separate the columns otherwise.

## Merging multiple data files into one large file

For some purposes, such as using pivot tables, it may be convenient to merge all data files into one large file. You can do this with the Datamerger program, written by Daniel Schreij.

%--
figure:
 id: FigDatamerger
 source: datamerger.png
 caption: |
  The DataMerger program allows you to merge multiple files into one large file.
--%

You can download Datamerger for Windows and Mac OS from here:

- <http://www.cogsci.nl/dschreij/datamerger/>

For Ubuntu, you can install the `datamerger` package from the [Cogsci.nl PPA][ppa]:

	sudo add-apt-repository ppa:smathot/cogscinl
	sudo apt-get update
	sudo apt-get install datamerger

The source code is available from here:

- <https://github.com/dschreij/Datamerger>

[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/
[log-func]: /python/inline-script/#inline_script.log
[codecs]: http://docs.python.org/2/library/codecs.html
[ppa]: https://launchpad.net/~smathot/+archive/cogscinl/
