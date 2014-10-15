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
import warnings

def generateVersionList(branch):

	"""
	desc:
		Creates content/_includes/version-select
	"""

	print(u'Generating version list')
	d = yaml.load(open(u'versions.yml').read())
	html = u''
	for version in d:
		if branch == version[u'branch']:
			html += u'<option value="%(branch)s" selected>%(desc)s</option>\n' \
				% version
		else:
			html += u'<option value="%(branch)s">%(desc)s</option>\n' \
				% version
	open(u'_content/_includes/version-select', u'w').write(html)

def branchStatus(branch):

	"""
	desc:
		Determines the status of a branch.

	returns:
		desc:	A status, which is 'old', dev', or 'current'.
		type:	unicode
	"""

	d = yaml.load(open(u'versions.yml').read())
	html = u''
	for version in d:
		if branch == version[u'branch']:
			status = version[u'status']
			assert(status in [u'old', u'dev', u'current'])
			return status
	warnings.warn(u'Your current branch is not defined in versions.yml')
	return 'dev'

