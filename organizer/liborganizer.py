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
import os
import yaml
import shutil

def getInfo(path):
	
	"""
	Retrieves YAML info from a Markdown document.
	
	Arguments:
	path	--	The path to the document.
	
	Returns:
	A dictionary with YAML info.
	"""
	
	s = open(path).read().decode(u'utf-8')
	l = s.split(u'---')
	if len(l) < 3:
		print u'liborganizer:getInfo(): Failed to parse %s' % path
		return None
	y = yaml.load(l[1])	
	b, s = str(y[u'sortkey']).split(u'.')
	y['sortkey'] = b.rjust(3, '0') + u'.' + s.ljust(3, '0')
	return y

def setInfo(path, i):
	
	"""
	Modifies the YAML infor inside a Markdown document. The file is not modified
	directly, but returned as a string.
	
	Arguments:
	path	--	The patch to the document.
	i		--	A dictionary with the YAML info.
	
	Returns:
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

def match(i, key):
	
	"""
	Determines whether a YAML info dictionary matches a key.
	
	Arguments:
	i		--	A dictionary with YAML info.
	key		--	A key where 'X' indicates a wildcard. For example, '00X.001' or
				'002.00X', or '010.002'.
	
	Returns:
	True on a match, False otherwise.
	"""
	
	big, small = i[u'sortkey'].split('.')
	_big, _small = key.split('.')
	return (_big == u'00X' or big == _big) and (_small == u'00X' or small == \
		_small)

def changeKey(i, key, path=None):
	
	"""
	Changes the key in the YAML info of a markdown document.
	
	Argument:
	i		--	A dictionary with YAML info.
	key		--	A key where 'X' indicates a wildcard. For example, '00X.001' or
				'002.00X', or '010.002'.
	
	Keyword arguments:
	path	--	A path to a file that should be modified. (default=None)
	
	Returns:
	A dictionary with updated YAML info.
	"""
	
	print u'liborganizer.changeKey(): %s' % path
	big, small = i[u'sortkey'].split(u'.')
	_big, _small = key.split(u'.')
	
	if _big != u'00X':
		big = _big
	if _small != u'00X':
		small = _small
	i[u'sortkey'] = u'%s.%s' % (big, small)
	if path != None:		
		s = setInfo(path, i)
		if not '--dry' in sys.argv:
			f = open(path, 'w')
			f.write(s)
			f.close()
	return i

def listContent(dirname=None, l=[]):
	
	"""
	Lists all content files in a given directory.
	
	Keyword arguments:
	dirname		--	The content directory or None to use the last command line
					parameter. (default=None)
	l			--	A list to append the files to (for recursion purposes).
					(default=[])
	
	Returns:
	A list of all content Markdown files.
	"""
	
	if dirname == None:
		dirname = sys.argv[-1].decode(sys.getfilesystemencoding())

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
	return sorted(l, key=lambda i: i[1][u'sortkey'])

def printItem(path, i):
	
	"""
	Prints a description of an item to the standard output.
	
	Arguments:
	path	--	The path to the item.
	i		--	A dictionary with YAML info.
	"""
	
	print u'%6s' % i[u'sortkey'], u'\t', u'\t' * i[u'level'],
	print i[u'permalink'].ljust(50), path
	
def formatItem(path, i):
	
	"""
	Returns a description of an item.
	
	Arguments:
	path	--	The path to the item.
	i		--	A dictionary with YAML info.
	
	Returns:
	A unicode string with the item description.
	"""	
	
	return u'%6s' % i[u'sortkey'] + u'\t' + u'\t' * i[u'level'] + \
		i[u'permalink'].ljust(50) + path

def printContent():
	
	"""Prints a description of the full content to the standard output."""
	
	l = listContent()
	for path, i in l:
		printItem(path, i)

def changePath(path, i, toKey):
	
	"""
	Determines the new path based on a new key.
	
	Argument:
	path	--	The old path.
	i		--	A dictionary with YAML info.
	toKey	--	The new key.
	
	Returns:
	The new path.
	"""
	
	if i[u'level'] == 0:
		s = toKey.split(u'.')[0]
	else:
		s = toKey.split(u'.')[1]
	s = s[-2:]
	if u'X' not in s:
		dirname = os.path.dirname(path)
		basename = os.path.basename(path)	
		basename = s + basename[2:]
		path = os.path.join(dirname, basename)
	return path
		
def move(fromKey, toKey):
	
	"""
	Moves all files that match fromKey to pathnames that match toKey.
	
	Arguments:
	fromKey		--	The old key.
	toKey		--	The new key.
	"""
	
	l = listContent()
	for path, i in l:
		if match(i, fromKey):
			print u'Move',
			printItem(path, i)
			i = changeKey(i, toKey, path=path)
			_path = changePath(path, i, toKey)
			if _path != path:
				if not '--dry' in sys.argv:
					shutil.move(path, _path)
				path = _path
			print u'  ->',
			printItem(path, i)

