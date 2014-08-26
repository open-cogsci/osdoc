#!/usr/bin/env python
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

from optparse import OptionParser
from libosdoc import compileTools

if __name__ == u'__main__':

	# Parse command line options
	parser = OptionParser()
	parser.add_option(u'-n', u'--nojekyll', dest=u'jekyll',
		help=u'Do not generate site with Jekyll', action=u'store_false',
		default=True)
	parser.add_option(u'-c', u'--check-links', dest=u'checkLinks',
		help=u'Check for dead links (requires linkchecker)',
		action=u'store_true', default=False)
	parser.add_option(u'-o', u'--optimize-html', dest=u'optimizeHTML',
		help=u'Optimize HTML (requires htmlcompressor.jar)',
		action=u'store_true', default=False)
	parser.add_option(u'-t', u'--tarball', dest=u'tarball',
		help=u'Generate site tarball', action=u'store_true', default=False)
	parser.add_option(u'-g', u'--group', dest=u'group',
		help=u'Only parse a specific group', default=None)
	parser.add_option(u'--layout', dest=u'layout', help=u'Layout file',
		default=u'inpage')
	options, args = parser.parse_args()
	compileTools.compileSite(jekyll=options.jekyll,
		checkLinks=options.checkLinks, optimizeHTML=options.optimizeHTML,
		tarball=options.tarball, group=options.group,
		layout=options.layout)
