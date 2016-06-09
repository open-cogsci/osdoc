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

import yaml
import subprocess

def runJekyll(status, branch):

	"""
	desc:
		Compiles the site to HTML with Jekyll.

	arguments:
		status:		The site status, which is 'dev', 'current', or 'old'.
	"""

	print(u'\nCreating _config.yml')
	cfg = {
		'notifications' 	: True,
		'status'			: status,
		'pygments'			: True,
		'markdown'			: 'kramdown',
		'source'			: '_content',
		'destination'		: '_tmp',
		'branch'			: branch,
		'langs'				: ['fr', 'en', 'es'],
		}
	yaml.dump(cfg, open('_config.yml', 'w'))
	print u'\nLaunching jekyll'
	subprocess.call([u'jekyll'])
