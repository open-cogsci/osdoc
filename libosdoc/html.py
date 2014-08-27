# -*- coding: utf-8 -*-

"""
This file is part of osdoc.

osdoc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

osdoc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with osdoc.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import re
import subprocess

def callOptimizeHTML(path):

	"""
	desc:
		Recursively compresses all HTML files in the path using
		htmlcompressor.jar

	arguments:
		path:	The folder path to optimize.
	"""

	for fname in os.listdir(path):
		fname = os.path.join(path, fname)
		if os.path.isdir(fname):
			callOptimizeHTML(fname)
		elif fname.lower().endswith(u'.html'):
			s1 = os.path.getsize(fname)
			cmd = [u'java', u'-jar', u'htmlcompressor.jar', u'--compress-js',
				fname, u'-o', fname]
			subprocess.call(cmd)
			s2 = os.path.getsize(fname)
			print u'Optimized:\t%s (%d kB -> %d kB, %d%%)' % (fname, s1, s2,
				(100.*s2/s1))

def adjustRootRelativeURLs(path, branch):

	"""
	desc:
		Recursively walks through a folder and replaces all root-relative URLs
		by a branched URL. Processes HTML and CSS files.

	arguments:
		path:		The path to walk through.
		branch:		The branch to add.
	"""

	print(u'Adjusting root-relative URLs (%s)' % path)
	for fname in os.listdir(path):
		fname = os.path.join(path, fname)
		if os.path.isdir(fname):
			adjustRootRelativeURLs(fname, branch)
			continue
		if fname.lower().endswith(u'.html'):
			html = open(fname).read().decode(u'utf-8')
			regex = u'(?P<_type>href|src)\\s*=\\s*["\'](?P<url>/.*?)["\']'
			for g in re.finditer(regex, html):
				url = g.group(u'url')
				if url.startswith(u'//'):
					print(u'Ignoring odd URL in %s: %s' % (fname, url))
					continue
				if url.startswith(u'/current'):
					print(u'Ignoring current URL in %s: %s' % (fname, url))
					continue
				old = g.group()
				new = u'%s="/%s%s"' % (g.group(u'_type'), branch, url)
				html = html.replace(old, new)
			open(fname, u'w').write(html.encode(u'utf-8'))
		elif fname.lower().endswith(u'.css'):
			css = open(fname).read().decode(u'utf-8')
			open(fname, u'w').write(css.encode(u'utf-8'))
			regex = u'url\(["\'](?P<url>.*?)["\']\)'
			for g in re.finditer(regex, css):
				url = g.group(u'url')
				if url.startswith(u'//'):
					print(u'Ignoring odd URL in %s: %s' % (fname, url))
					continue
				old = g.group()
				new = u'url(\'/%s%s\')' % (branch, url)
				css = css.replace(old, new)
			open(fname, u'w').write(css.encode(u'utf-8'))

