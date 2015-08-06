---
layout: osdoc
title: Develop
group: contribute
permalink: /develop/
parser: academicmarkdown
---

## Overview

%--
toc:
 mindepth: 2
 exclude: [Overview]
--%

## Getting the latest source code

The OpenSesame source code is hosted on GitHub:

- <https://github.com/smathot/OpenSesame>.

GitHub provides a straightforward way for collaborating on a project. If you're not familiar with GitHub, you may want to take a look at their help site: <http://help.github.com/>.

The best (and easiest) way to contribute code is as follows:

1. Create a GitHub account.
2. Create a fork of OpenSesame <https://github.com/smathot/OpenSesame>.
3. Modify your fork.
4. Send a 'pull request', asking for your changes to be merged back into the main repository.

The two main branches of OpenSesame are:

- `master` contains reasonably stable code.
- `playground` contains potentially unstable code.

## Developing a plug-in

For plug-in development, see:

- [/plug-ins/create-plug-in](/plug-ins/create-plug-in)

## Source-code architecture

For a description of the OpenSesame source-code architecture, see:

- [/contribute/architecture](/contribute/architecture)

## Coding-style guidelines

The goal is to maintain a readable and consistent code base. Therefore, please consider the following style guidelines when contributing code:

### Exception handling

Exceptions should be handled via the `libopensesame.exceptions.osexception` class. For example:

{% highlight python %}
from libopensesame.exceptions import osexception
raise osexception(u'An error occurred')
{% endhighlight %}

### Printing debug output

Debug output should be handled via `libopensesame.debug.msg()`, and is shown only when OpenSesame is started with the `--debug` command-line argument. For example:

{% highlight python %}
from libopensesame import debug
debug.msg(u'This will be shown only in debug mode')
{% endhighlight %}

### Indentation

Indentation should be tab based. *This is the most important style guideline of all*, because mixed indentation causes trouble and is time consuming to correct.

### Names, doc-strings, and line wrapping

- Names should be lower case, with words separated by underscorses.
- Each function should be accompanied by an informative doc string, of the format shown below. If a doc-string is redundant, for example, because a function overrides another function that has a doc-string, please indicate where the full doc-string can be found.
- Please do not have lines of code extend beyond 79 characters (where a tab counts as 4 characters), with the exception of long strings that are awkward to break up.

{% highlight python %}
def a_function(argument, keyword=None):

	"""
	desc:
		This is a YAMLDoc-style docstring, which allows for a full specification
		of arguments. See also <https://github.com/smathot/python-yamldoc>.

	arguments:
		argument:   This is an argument.

	keywords:
		keyword:    This is a keyword.

	returns:
		This function returns some values.
	"""

	pass

def a_simple_function():

	"""This is a simple doc-string"""

	pass

{% endhighlight %}

### Unicode and strings

Assure that all functionality is Unicode safe. For new code, use *only* Unicode strings internally.

{% highlight python %}
my_value = 'a string' # not preferred
my_value = u'a string' # preferred
{% endhighlight %}

For more information, see:

- <http://docs.python.org/2/howto/unicode.html>

### Other

With the exception of the guidelines shown above, please adhere to the following standard:

- <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>
