<div class="ClassDoc YAMLDoc" markdown="1">

# instance __log__

The `log` object provides data logging. A `log` object is created
automatically when the experiment starts.

__Example__

~~~ .python
# Write one line of text
log.write('My custom log message')
# Write all variables
log.write_vars()
~~~

[TOC]

## close()

Closes the current log.



__Example__

~~~ .python
log.close()
~~~



## open(path)

Opens the current log. If a log was already open, it is closed
automatically, and re-opened.


__Parameters__

- **path**: The path to the current logfile. In most cases (unless) a custom
log back-end is used, this will be a filename.

__Example__

~~~ .python
# Open a new log
log.open('/path/to/new/logfile.csv')
~~~



## write(msg, newline=True)

Write one message to the log.


__Parameters__

- **msg**: A text message. When using Python 2, this should be either
`unicode` or a utf-8-encoded `str`. When using Python 3, this
should be either `str` or a utf-8-encoded `bytes`.
- **newline**: Indicates whether a newline should be written after the message.

__Example__

~~~ .python
# Write a single string of text
log.write(f'time = {clock.time()}')
~~~



## write_vars(var_list=None)

Writes variables to the log.


__Parameters__

- **var_list**: A list of variable names to write, or None to write all variables
that exist in the experiment.

__Example__

~~~ .python
# Write all variables to the logfile
log.write_vars()
~~~



</div>

