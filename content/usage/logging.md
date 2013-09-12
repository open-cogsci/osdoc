---
layout: osdoc
title: Logging and reading data files
group: Usage
permalink: /logging/
---

Always triple check whether your data has been correctly logged before running your experiment!
{: .page-notification}

:--
cmd: overview
--:
	
## Using the logger item

OpenSesame will not log your data automatically. Instead, you need to insert a *logger* item, typically at the end of your trial sequence.

:--
cmd: figure
src: logger.png
caption: The `logger` item.
--:

The logger has a number of options:

- **Include variables with missing values** indicates that all variables that OpenSesame knows of should be logged, even if they are not yet defined when the logger is called for the first time. If a variable is missing, it will simply be logged as 'NA'. If you disable this option, OpenSesame will only log those variables that have a value when the logger is called for the first time. This can wreak havoc, for example, when your experiment consists of two parts, so that some variables are only defined later on in the experiment. So it's typically safer to leave this option enabled!
- **Automatically detect and log all variables** means that OpenSesame will log all variables that it can detect. This is a safe choice, but it results in data files with a lot of variables that you do probably not want. You can disable this option, in which case you can manually select which variables you want to log.
- **Put quotes around values** means that OpenSesame will surround each value in the data file with double-quotes. If you do not have any specific reason to disable this option, it's best to leave it enabled.

In general, you should create only one logger item, and reuse that item at different locations in your experiment if necessary. If you create multiple logger items (rather than using a single logger multiple times), they will all write to the same log file, and the result will be a mess!

## Using Python inline script

You can write to the log file using the [`self.log()`][log-func], like so:

{% highlight python %}
self.log('This will be written to the log file!')
{% endhighlight %}

If you need more fine-grained control, you can use `exp.logfile`, which contains the name of the log file, and `exp._log`, which is a Python file object (`UTF-8` encoding through [`codecs.open()`][codecs]):

{% highlight python %}
print 'The location of the log file is %s' % exp.logfile
exp._log.write('This will be written to the log!')
{% endhighlight %}

Note that you will generally not want to write to the log file directly and use a logger item at the same time: This will result in very messy log files.

## Format of the data files

If you have used the standard logger item, data files are in plain text, comma-separated format, which can be opened in all popular spreadsheets. If you are looking for high quality, free spreadsheet software, take a look at [Libre Office][libreoffice], [OpenOffice.org][openoffice] or [Gnumeric][]. If you use Microsoft Excel, you may need to use the 'import' function to open the data files, because Excel may not properly separate the columns otherwise.

## Merging multiple data files into one large file

For some purposes, such as using pivot tables, it may be convenient to merge all data files into one large file. You can do this with the Datamerger program, written by Daniel Schreij.

:--
cmd: figure
src: datamerger.png
caption: The DataMerger program allows you to merge multiple files into one large file.
--:

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