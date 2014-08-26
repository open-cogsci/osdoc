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

import git
import time

def setGitInfo(targetPath=u'content/_includes/gitinfo'):

	"""
	desc:
		Writes current git info to an includes file.

	keywords:
		targetPath:	The path of the file to write to.
	"""

	repo = git.Repo(u'.')
	commit = repo.commit()
	s = u"Revision <a href='https://github.com/smathot/osdoc/commit/%s'>#%s</a> on %s" \
		% (commit.hexsha, commit.hexsha[:6],
		time.asctime(time.gmtime(commit.committed_date)))
	open(targetPath, u'w').write(s)

def gitBranch():

	"""
	returns:
		desc:	The name of the current git branch.
		type:	unicode
	"""

	return git.Repo(u'.').active_branch.name
