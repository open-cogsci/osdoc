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

import urllib2
import json
from libopensesame.experiment import experiment
from time import ctime

def generateExamples(targetPath=u'content/_includes/doc/examples'):

	"""
	desc:
		Generates a list of examples.

	keywords:
		targetPath:	The path of the file to write to.
	"""

	sys.stdout = open(targetPath, u'w')
	print '<p><small>This page was auto-generated on %s</small></p>' % ctime()
	url = "https://api.github.com/repos/smathot/OpenSesame/contents/examples"
	fd = urllib2.urlopen(url)
	js = json.loads(fd.read())
	for example in js:
		name = example['name']
		url = example['html_url']
		raw = url.replace('/blob/', '/raw/')
		if url.endswith('.opensesame'):
			fname = '/tmp/example.opensesame'
		else:
			fname = '/tmp/example.opensesame.tar.gz'
		fout = open(fname, 'wb').write(urllib2.urlopen(raw).read())
		try:
			exp = experiment('dummy', fname)
			title = exp.title
			description = exp.description
		except Exception as e:
			print e
			title = 'Failed to generate example'
			description = 'Failed to generate example'
		print '<p><b>%s</b><br />' % title
		print '%s<br />' % description
		print '<a href="%s">Download</a> - <a href="%s">View on GitHub</a></p>' \
			% (raw, url)
	sys.stdout = sys.__stdout__
