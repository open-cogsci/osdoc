OSDOC README
============

Copyright 2010-2012
Sebastiaan Mathôt <s.mathot@cogsci.nl>

STYLE GUIDELINES
================
The style guidelines are according to the [Tango Desktop Project][tango].

PAGE MARKUP
===========

YAML FRONT MATTER
-----------------

Each file starts with a [YAML front-matter header][yaml_front].

	---
	layout: osdoc
	title: About OpenSesame
	group: General
	permalink: /about-opensesame/
	level: 0
	sortkey: 002.001
	---

- The `layout` is always 'osdoc'
- The `title` is the title as visible in the menu and the top of the page
- The `group` is used to cluster the menus. 'General' is the group for the pages that do not have any other pages.
- The `permalink` determines the location of the page. This should match the old http://osdoc.cogsci.nl. This link should also start and end with a slash (/)
- The `level` indicates the level in the menu. 0 is top-level, 1 is sub-menu.
- The `sortkey` indicates the order of the page in the menu. The typical notation is toplevel-order.category-order.

FOLDER STRUCTURE
----------------

Als files are stored in the contents folder in a way that matches the structure of the menu.

	index.md
	about-opensesame.md
	getting-started.md
	getting-started/getting-opensesame.md
	getting-started/running-from-source.md
	etc.

LAYOUT
------

The layout of the content can be in either [Markdown][] or HTML syntax. Markdown is prefrered for simple things, such as headers, links, etc. Links are preferably in reference-style, such that the URLS are provided at the bottom op the page.

CODE BLOCKS AND SYNTAX HIGHLIGHTING
-----------------------------------

Pygments is used to perform syntax highlighting for the Python scripts, as described [here][pygments]. The liquid syntax to indicate which parts should be highlighted is as follows:

{% highlight python %}

def my_example():

	pass

{% endhighlight %}

The stylesheet for pygments is generated with the following command.

	pygmentize -S tango -f html > stylesheets/pygments.css

[markdown]: http://daringfireball.net/projects/markdown/
[tango]: http://en.wikipedia.org/wiki/Tango_Desktop_Project
[yaml_front]: https://github.com/mojombo/jekyll/wiki/YAML-Front-Matter
[pygments]: https://github.com/mojombo/jekyll/wiki/Liquid-Extensions