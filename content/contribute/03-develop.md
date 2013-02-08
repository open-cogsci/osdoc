---
layout: osdoc
title: Develop
group: contribute
permalink: /develop/
level: 1
sortkey: 0013.003
---

Getting the latest source code
------------------------------

The OpenSesame source code is hosted on GitHub:

- <https://github.com/smathot/OpenSesame>.

GitHub provides a straightforward way for collaborating on a project. If you're not familiar with GitHub, you may want to take a look at their help site: <http://help.github.com/>.

The best (and easiest) way to contribute code is as follows:

- Create a GitHub account.
- Create a fork of OpenSesame <https://github.com/smathot/OpenSesame>.
- Modify your fork.
- Send a 'pull request', asking for your changes to be merged back into the main repository.

The two main branches of OpenSesame are:

- `master` contains reasonably stable code.
- `playground` contains potentially unstable code.

Coding-style guidelines
-----------------------

The goal is to maintain a readable and consistent code base. Therefore, please consider the following style guidelines when contributing code:

### Indentation

Indentation should be tab based. *This is the most important style guideline of all*, because mixed indentation causes trouble and is time consuming to correct.

### Names, doc-strings, and line wrapping

- Names should be lower case, with words separated by underscorses. 
- Each function should be accompanied by an informative doc string, of the format shown below. If a doc-string is redundant, for example, because a function overrides another function that has a doc-string, please indicate where the full doc-string can be found.
- Please do not have lines of code extend beyond 79 characters (where a tab counts as 4 characters), with the exception of long strings that are awkward to break up.

{% highlight python %}
def a_function(argument, keyword=None):

	"""
	All arguments, keywords, and return values should be documented as shown
	below. 
	
	Arguments:
	argument	--	this is an argument
	
	Keyword arguments:
	keyword		--	this is a keyword (default=None)
	
	Returns:
	This function returns some values
	"""
	
	pass
	
def a_simple_function():

	"""This is a simple doc-string"
	
	pass
	
{% endhighlight %}

### Unicode and strings

Assure that all functionality is Unicode safe. For new code, use *only* Unicode strings internally.

{% highlight python %}
my_value = 'a string' # not preferred
my_value = u'a string' # preferred
{% endhighlight %}

### Other

With the exception of the guidelines shown above, please adhere to the following standard:

- <http://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds>