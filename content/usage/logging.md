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

If you have used the standard logger item, data files are in the following format format (simply standard csv):

- plain-text
- comma-separated
- double-quoted (literal double-quotes are escaped with backward slashes)
- unix-style line endings
- UTF-8 encoded
- column names on the first row

## Reading and processing data files

### In Python with pandas

In Python, you can use (for example) [pandas](http://pandas.pydata.org/) to read csv files.

~~~ .python
import pandas
df = pandas.read_csv('subject-1.csv')
print(df)
~~~

### In R

In R, you can simply use the `read.csv()` function to read a single data file.

~~~ .R
df = read.csv('subject-1.csv', encoding = 'UTF-8')
head(df)
~~~

In addition, you can use the `read_opensesame()` function from the [readbulk](https://github.com/pascalkieslich/readbulk) package to easily read and merge multiple data files into one large data frame. The package is available on CRAN and can be installed via `install.packages('readbulk')`.

~~~ .R
# Read and merge all data files stored in the folder 'raw_data'
library(readbulk)
df = read_opensesame('raw_data')
~~~

### In JASP

[JASP](http://jasp-stats.org/), an open-source statistics package, opens csv files straight away.

### In LibreOffice Calc

If you open a csv file in LibreOffice Calc, you have to indicate the exact data format, as indicated in %FigLibreOffice. (The default settings are often correct.)

%--
figure:
 source: libreoffice.png
 id: FigLibreOffice
--%

### In Microsoft Excel

In Microsoft Excel, you need to use the Text Import Wizard.

### Merging multiple data files into one large file

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
