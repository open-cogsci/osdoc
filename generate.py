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

import sys
sys.path = ['../opensesame'] + sys.path
from subprocess import call
from optparse import OptionParser
from libosdoc.pdf import pdfWalk, pdfRestore
from libosdoc.compileTools import compileSite, createTarball
from libosdoc.examples import generateExamples
from libosdoc.docPages import generateDocPages

if __name__ == u'__main__':

	# Parse command line options
	parser = OptionParser()
	parser.add_option(u'-g', u'--group', dest=u'group',
		help=u'Only parse a specific group', default=None)
	parser.add_option(u'-e', u'--examples', dest=u'examples',
		help=u'Generate examples', action=u'store_true', default=False)
	parser.add_option(u'-y', u'--yamldoc', dest=u'yamldoc',
		help=u'Generate YAMLDoc pages', action=u'store_true', default=False)
	options, args = parser.parse_args()
	if options.examples:
		generateExamples()
	if options.yamldoc:
		generateDocPages()
	# First compile the site with fullpage layout, so that we can generate PDFs
	siteFolder = compileSite(layout=u'fullpage', gitInfo=True,
		group=options.group)
	pdfWalk(siteFolder)
	# Now compile the site with inpage (=normal) layout, and move all PDFs
	# into the site.
	compileSite(optimizeHTML=True, group=options.group, htaccess=True,
		adjustURLs=False)
	pdfRestore(siteFolder)
	# Create a tarball for the site
	createTarball(siteFolder)
	# Finally compile the mobile site
	compileSite(layout=u'mobile', optimizeHTML=True, group=options.group,
		htaccess=True, adjustURLs=False)
