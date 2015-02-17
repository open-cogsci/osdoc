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
import sys
import yaml
import re
import shutil
import subprocess
import csv
from md5 import md5
import re
from academicmarkdown import build, HTMLFilter
from libosdoc.versions import generateVersionList, branchStatus
from libosdoc.pdf import pdfWalk
from libosdoc.jekyll import runJekyll
from libosdoc.html import callOptimizeHTML, adjustRootRelativeURLs, \
	applyConstants
from libosdoc.gitinfo import setGitInfo, gitBranch

def getInfo(path):

	"""
	desc:
		Retrieves YAML info from a Markdown document.

	arguments:
		path:	The path to the document.

	returns:
		A dictionary with YAML info.
	"""

	s = open(path).read().decode(u'utf-8')
	l = s.split(u'---')
	if len(l) < 3:
		print u'getInfo(): Failed to parse %s' % path
		return None
	y = yaml.load(l[1])
	if u'lang' not in y:
		y[u'lang'] = u'en'
	return y

def setInfo(path, i):

	"""
	desc:
		Modifies the YAML info inside a Markdown document. The file is not
		modified directly, but returned as a string.

	arguments:
		path:	The path to the document.
		i:		A dictionary with the YAML info.

	returns:
		A string with the modified document.
	"""

	# Sortkey has to be string, otherwise it will not be parsed correctly by
	# yaml
	s = open(path).read().decode(u'utf-8')
	l = s.split(u'---')
	if len(l) < 3:
		return None
	yml = u''
	for key, value in i.iteritems():
		yml += u'%s: %s\n' % (key, value)
	l[1] = yml
	s = u'---\n' + u'---'.join(l[1:])
	return s

def listContent(dirname=u'content', l=[]):

	"""
	desc:
		Lists all content files in a given directory.

	keywords:
		dirname:	The content directory or None to use the last command line
					parameter.
		l:			A list to append the files to (for recursion purposes).

	returns:
		A list of all content Markdown files.
	"""

	print(u'\nListing content (%s) ...' % dirname)
	for basename in os.listdir(dirname):
		if basename.startswith(u'_'):
			continue
		path = os.path.join(dirname, basename)
		if os.path.isdir(path):
			l = listContent(dirname=path, l=l)
		elif basename.endswith(u'.md'):
			i = getInfo(path)
			if i != None:
				l.append((path, i))
				print(u'+ %s (%d)' % (path, len(l)))
	return l

def copyFile(fromPath, toPath):

	"""
	desc:
		Copies a file and creates the target folder structure if it doesn't
		exist.

	arguments:
		fromPath:	The source file.
		toPath:		The target file.
	"""

	if not os.path.exists(os.path.dirname(toPath)):
		os.makedirs(os.path.dirname(toPath))
	shutil.copyfile(fromPath, toPath)

def preprocessPage(path, info, s, status):

	"""
	desc:
		Pre-processes a page with academicmarkdown.

	arguments:
		path:	The path to the page.
		info:	A dictionary with the page's front matter.
		s:		A string with the page content.
		status:	The site status.

	returns:
		A string with the parsed page contents.
	"""

	print u'Parsing %s (%s) with academicmarkdown' % (info[u'title'], path)
	# Add all source paths to the build path, so that we can reference to
	# figures etc without considering paths
	build.path += [os.path.join(path, u'img', info['permalink'][1:]), \
		os.path.join(path, u'lst', info['permalink'][1:]), \
		os.path.join(path, u'tbl', info['permalink'][1:])]
	# Set the correct templates
	build.codeTemplate = u'jekyll'
	build.figureTemplate = u'jekyll'
	build.tableTemplate = u'kramdown'
	# Disable markdown filters
	build.preMarkdownFilters = []
	build.postMarkdownFilters = []
	# Enable clickable anchor headers
	build.TOCAnchorHeaders = True
	build.TOCAppendHeaderRefs = True
	# Original s
	_s = s
	# Convert script tags to jekyll style
	regex = r'^~~~\s+{*\.(?P<lang>\w+)}*(?P<script>.+?)^~~~'
	for g in re.finditer(regex, s, re.DOTALL | re.MULTILINE):
		old = g.group()
		new = u'{%% highlight %s %%}%s{%% endhighlight %%}' % (g.group('lang'),
			g.group('script'))
		s = s.replace(old, new)
	if status == u'current' or u'current-only' not in info or \
		not info[u'current-only']:
		s = build.MD(s)
	else:
		s = u'---\n%s\n---\n{%% include current-only %%}' % yaml.dump(info)
		print s
	s = HTMLFilter.DOI(s)
	# Remove the content/ part of figure paths, because it does not apply to
	# the generated site.
	s = s.replace(u'![content/', u'![/')
	s = s.replace(u'(content/', u'(/')
	# We need to find all images, and copy these to the _content folder
	for r in re.finditer(u'%--(.*?)--%', _s, re.M|re.S):
		try:
			d = yaml.load(r.groups()[0])
		except:
			print u'Invalid YAML block: %s' % r.groups()[0]
			continue
		if not u'figure' in d:
			continue
		src = os.path.join(path, u'img', info['permalink'][1:], \
			d[u'figure'][u'source'])
		if src.endswith(u'.svg'):
			src += u'.png'
		print u'Copying %s' % src
		copyFile(src, u'_'+src)
	# Remove the three newly added entries from the build path.
	build.path = build.path[:-3]
	return s

def compileLess():

	"""
	desc:
		Compiles the less stylesheets to css.
	"""

	print(u'\nCompiling .less to .css ...')
	cmd = ['lesscpy', '-X', 'content/stylesheets/main.less']
	subprocess.call(cmd, stdout=open(u'_content/stylesheet.css', u'w'))

def copyResources(layout):

	"""
	desc:
		Copies non-Markdown resources.
	"""

	print(u'\nCopying non-page resources ...')
	shutil.copytree(u'content/_includes', u'_content/_includes')
	shutil.copytree(u'content/_layouts', u'_content/_layouts')
	shutil.copytree(u'content/attachments', u'_content/attachments')
	shutil.copytree(u'content/img', u'_content/img')
	shutil.copy(u'content/favicon.ico', u'_content/favicon.ico')
	shutil.copy(u'content/_layouts/osdoc-%s.html' % (layout),
		u'_content/_layouts/osdoc.html')

def preprocessSite(content, group, branch, status):

	"""
	desc:
		Pre-processes the full site.

	arguments:
		content:	A content list, as generated by listContent().
		group:		A group to include or None to include all groups.
		status:		The site status.
	"""

	print(u'\nCompiling pages ...')
	sortkey = [0,0]
	_group = 'General'
	sitemap = open('sitemap.txt').read().decode(u'utf-8')
	YAMLSitemap = {}
	for title in sitemap.split(u'\n'):
		if title.startswith(u'#') or title.strip() == u'':
			continue
		if title.startswith(u'\t'):
			sortkey[1] += 1
			level = 1
		else:
			sortkey[0] += 1
			level = 0
		title = title.strip()
		if title.startswith(u':'):
			show = False
			title = title[1:]
		else:
			show = True
		i = 0
		for path, info in content:
			if info[u'title'].lower() == title.lower():
				# Strip of the 'content' bit from the path and prepend the
				# target path.
				targetPath = '_'+path
				if level > 0:
					print u'\t',
				else:
					_group = info[u'group']
				print '-> %s (%s)' % (title, path)
				info[u'show'] = show
				info[u'sortkey'] = u'%.3d.%.3d' % (sortkey[0], sortkey[1])
				info[u'level'] = level
				info[u'group'] = _group
				info[u'figures'] = 0
				info[u'videos'] = 0
				info[u'listings'] = 0
				info[u'tables'] = 0
				info[u'gitlink'] = \
					u'https://github.com/smathot/osdoc/blob/%s/%s' \
						% (branch, path)
				if group == None or group.lower() == \
					_group.lower() or title.lower() == u'home':
					s = setInfo(path, info)
					# Fix missing alt tags
					s = s.replace(u'![](', u'![No alt text specified](')
					s = preprocessPage(os.path.dirname(path), info, s, status)
					if not os.path.exists(os.path.dirname(targetPath)):
						os.mkdir(os.path.dirname(targetPath))
					open(targetPath.encode(sys.getfilesystemencoding()), \
						u'w').write(s.encode(u'utf-8'))
					# Generate the YAML sitemap, which is read automatically by
					# OpenSesame to browse the online documentation.
					if show and (u'menuclass' not in info or \
						info[u'menuclass'] != u'external'):
						title = title.capitalize().encode(u'utf-8')
						__group = _group.capitalize().encode(u'utf-8')
						path = u'/%s/%s/' % (branch, path[8:-3])
						path = path.encode(u'-utf-8')
						if __group == 'General':
							YAMLSitemap[title] = path
						else:
							if __group not in YAMLSitemap:
								YAMLSitemap[__group] = {}
							YAMLSitemap[__group][title] = path
				i += 1
		if i > 1:
			raise Exception(u'Multiple matches for "%s"' % title)
		if i == 0:
			raise Exception(u'Failed to find "%s"' % title)
	open(os.path.join(u'_content', u'sitemap.yml'), u'w').write(
		yaml.dump(YAMLSitemap, default_flow_style=False))

def createTarball(siteFolder):

	"""
	desc:
		Creates a tarball of the site.
	"""

	print(u'\nCreating tarball (osdoc.tar.gz)')
	cmd = [u'tar', u'-zcvf', u'osdoc.tar.gz', u'-C', siteFolder, u'.', \
		u'--exclude-from=dev-scripts/excludefromgz.txt']
	subprocess.call(cmd)
	shutil.move(u'osdoc.tar.gz', siteFolder)

def checkDeadLinks(branch):

	"""
	desc:
		Checks the site for dead links.
	"""

	print(u'\nChecking for dead links')
	cmd = [u'linkchecker', u'--no-warnings', u'-o', u'csv', \
		u'http://localhost:8000/%s' % branch]
	subprocess.call(cmd, stdout=open(u'deadlinks.log', u'w'))
	nErr = 0
	for l in open(u'deadlinks.log').read().decode(u'utf-8').split(
		u'\n')[4:]:
		r = l.split(u';')
		if len(r) < 6 or r[0] == u'urlname':
			continue
		url = r[0]
		# Don't check index.pdf pages, as they are generated later on, and
		# don't check e-mail addresses.
		if url.endswith(u'index.pdf') or url.startswith(u'mailto:'):
			continue
		parent = r[1]
		warning = r[3]
		valid = r[5] == u'False'
		nErr += 1
		print '%s\n\tin %s' % (url, parent)
	print u'%d dead link(s) found' % nErr

def createHtaccess(siteFolder, branch):

	"""
	desc:
		Creates an .htaccess file in the parent folder.
	"""

	s = u"""RewriteEngine On
RewriteRule    ^$    %s/$1   [NC,L]
RewriteRule    ^current?$    %s/$1   [NC,L]
RewriteRule    ^notes/(.*)?$    %s/notes/$1/   [NC,L]
RewriteRule    ^([^0-9]+.*)/?$    %s/$1   [NC,L]
RewriteRule    ^([0-9]+).([0-9]+).([0-9])+/(.*)$    $1.$2/$4
""" % (branch, branch, branch, branch)
	path = os.path.join(os.path.dirname(siteFolder), u'.htaccess')
	open(path, u'w').write(s)
	print(u'Created %s' % path)

def compileSite(layout=u'inpage', group=None, jekyll=True, optimizeHTML=False,
	tarball=False,	checkLinks=False, gitInfo=False, htaccess=False,
	adjustURLs=True):

	"""
	desc:
		Compiles the site.

	keywords:
		layout:
			desc:	Indicates the layout to be used. Should be 'fullpage' or
					'inpage'.
			type:	[str, unicode]
		group:
			desc:	The name of a group (subsection) to speed up compilation for
					debugging purposes.
			type:	[str, unicode, NoneType]
		jekyll:
			desc:	Indicates whether Jekyll should be called to compile the
					site source to HTML.
			type:	bool
		optimizeHTML:
			desc:	Indicates whether HTML should be optimized/ minified.
			type:	bool
		tarball:
			desc:	Indicates whether a tarball of the site should be generated.
			type:	bool
		checkLinks:
			desc:	Indicates whether the site should be checked for dead links.
			type:	bool
		gitInfo:
			desc:	Indicates whether gitinfo should be updated.
			type:	bool
		htaccess:
			desc:	Indicates whether an .htaccess file should generated in the
					parent folder, to rewrite branchless URLS to the current
					branch.
			type:	bool
		adjustURLs:
			desc:	Indicates whether URLs should be adjusted so that the branch
					name is prefixed. This is only applicable for stable
					branches.
			type:	bool

	returns:
		desc:	The folder where the site has been generated.
		type:	unicode
	"""

	assert(layout in [u'fullpage', u'inpage'])
	branch = gitBranch()
	status = branchStatus(branch)
	print(u'Branch:\t%s\nStatus:\t%s\n' % (branch, status))
	if gitInfo:
		setGitInfo()
	print(u'\nRecreating _content ...')
	if os.path.exists('_content'):
		shutil.rmtree('_content')
	os.makedirs('_content')
	copyResources(layout)
	generateVersionList(branch)
	compileLess()
	content = listContent(l=[])
	preprocessSite(content=content, group=group, status=status, branch=branch)
	if jekyll:
		runJekyll(status, branch)
	if branch != '':
		if adjustURLs or status != u'current':
			skipHTML = False
		else:
			skipHTML = True
		adjustRootRelativeURLs('_tmp', branch, skipHTML=skipHTML)
		siteFolder = u'_site/%s' % branch
	else:
		siteFolder = u'_site'
	applyConstants('_tmp', branch)
	print(u'Moving site to %s' % siteFolder)
	if os.path.exists(siteFolder):
		shutil.rmtree(siteFolder)
	shutil.move(u'_tmp', siteFolder)
	if optimizeHTML:
		callOptimizeHTML(siteFolder)
	if tarball:
		createTarball(siteFolder)
	if checkLinks:
		checkDeadLinks(branch)
	if htaccess and status == u'current':
		createHtaccess(siteFolder, branch)
	return siteFolder
