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

from subprocess import call
import os
import shutil

tmpList = {}

def pdfWalk(siteFolder):

	"""
	desc:
		Walks through the _site folder and converts all .html files to pdf. The
		PDFs are initially saved in a temporary location, and can be moved to
		the site by pdfRestore.
	"""

	global tmpList

	for fname in os.listdir(siteFolder):
		path = siteFolder + '/' + fname
		if os.path.isdir(path):
			print 'Entering folder %s' % path
			pdfWalk(path)
		if path.endswith('.html'):
			realTarget = os.path.dirname(path) + '/index.pdf'
			tmpTarget = '/tmp/%.5d.pdf' % len(tmpList)
			cmd = './wkhtmltopdf http://localhost:8000/%s %s' % (path[6:],
				tmpTarget)
			print cmd
			call(cmd.split())
			tmpList[tmpTarget] = realTarget

def pdfRestore(siteFolder):

	"""
	desc:
		Moves previously generated PDFs to the site.
	"""

	global tmpList

	for tmpPath, realPath in tmpList.items():
		print(u'%s -> %s' % (tmpPath, realPath))
		shutil.move(tmpPath, realPath)
