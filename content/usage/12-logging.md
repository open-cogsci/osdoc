---
layout: osdoc
title: Logging and reading data files
group: Usage
permalink: /logging/
level: 1
sortkey: 004.012
---

##### Always triple check whether your data has been correctly logged before running your experiment!

Logging your data
-----------------

OpenSesame will not log your data automatically. Instead, you need to insert a *logger* item, typically at the end of your trial sequence.

![](/img/fig/fig4.12.1.png)

The logger has a number of options:

- **Include variables with missing values** indicates that all variables that OpenSesame knows of should be logged, even if they are not yet defined when the logger is called for the first time. If a variable is missing, it will simply be logged as 'NA'. If you disable this option, OpenSesame will only log those variables that have a value when the logger is called for the first time. This can wreak havoc, for example, when your experiment consists of two parts, so that some variables are only defined later on in the experiment. So it's typically safer to leave this option enabled!

- **Automatically detect and log all variables** means that OpenSesame will log all variables that it can detect. This is a safe choice, but it results in data files with a lot of variables that you do probably not want. You can disable this option, in which case you can manually select which variables you want to log.

- **Put quotes around values** means that OpenSesame will surround each value in the data file with double-quotes. If you do not have any specific reason to disable this option, it's best to leave it enabled.

Format of the data files
------------------------

If you have used the standard logger item, data files are in plain text, comma-separated format, which can be opened in all popular spreadsheets. If you are looking for high quality, free spreadsheet software, take a look at [Libre Office][libreoffice], [OpenOffice.org][openoffice] or [Gnumeric][]. If you use Microsoft Excel, you may need to use the 'import' function to open the data files, because Excel may not properly separate the columns otherwise.

If you prefer to have all data in one large spreadsheet, rather than in separate files per subject, you may be interested in the [on-line spreadsheet merger][merger]. This tool also provides functionality to convert the spreadsheet to Excel format and to select/ exclude columns.

[merger]: http://www.cogsci.nl/software/online-spreadsheet-merger
[libreoffice]: http://www.libreoffice.org/
[openoffice]: http://www.openoffice.org/
[gnumeric]: http://projects.gnome.org/gnumeric/