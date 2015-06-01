#-*- coding:utf-8 -*-

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

import re
import yamldoc
from academicmarkdown import build
import sys
sys.path.insert(0, '/home/sebastiaan/git/opensesame')
from libopensesame import plugins

def createDoc(cls, target, **kwdict):

	"""
	desc:
		Generates a single doc page.

	arguments:
		cls:		A class to document.
		target:		A target path to save to documentation to.
	"""

	df = yamldoc.DocFactory(cls, container=u'div', **kwdict)
	md = build.MD(unicode(df))
	regex = r'^~~~\s+{*\.(?P<lang>\w+)}*(?P<script>.+?)^~~~'
	for g in re.finditer(regex, md, re.DOTALL | re.MULTILINE):
		old = g.group()
		new = u'{%% highlight %s %%}%s{%% endhighlight %%}' % (g.group('lang'),
			g.group('script'))
		md = md.replace(old, new)
	open(target, 'w').write(md.encode('utf-8'))

def generateDocPages():

	"""
	desc:
		Generates all API doc pages.
	"""

	build.preMarkdownFilters = []
	build.postMarkdownFilters = []
	# Enable clickable anchor headers
	build.TOCAnchorHeaders = True
	build.TOCAppendHeaderRefs = True

	from libopensesame import python_workspace_api
	from libopensesame.file_pool_store import file_pool_store
	from libopensesame.var_store import var_store
	from libopensesame.item_store import item_store
	createDoc(python_workspace_api,
		u'content/_includes/doc/python_workspace_api', onlyContents=True)
	createDoc(var_store, u'content/_includes/doc/var_store', customName=u'var')
	createDoc(file_pool_store, u'content/_includes/doc/file_pool_store',
		customName=u'pool')
	createDoc(item_store, u'content/_includes/doc/item_store',
		customName=u'items')
	from libopensesame.experiment import experiment
	exp = experiment('Dummy', '')
	for backend in ['sampler', 'canvas', 'keyboard', 'mouse', 'clock', 'log']:
		cls = plugins.load_cls(u'../opensesame/openexp/_%s' % backend, backend,
			backend)
		try:
			if backend == 'sampler':
				cls(exp, None)
		except:
			pass
		createDoc(cls, u'content/_includes/doc/%s' % backend)
	#
	# cls = plugins.load_cls(u'../PyGaze/pygaze/_eyetracker',
	# 	u'BaseEyeTracker', u'baseeyetracker')
	# createDoc(cls, u'content/_includes/doc/pygaze')
	#
	# cls = plugins.load_cls(u'../opensesame/plugins/joystick/_libjoystick',
	# 	u'basejoystick', u'basejoystick')
	# createDoc(cls, u'content/_includes/doc/libjoystick')
	# cls = plugins.load_cls(u'../opensesame/plugins/srbox', u'libsrbox',
	# 	u'libsrbox')
	# createDoc(cls, u'content/_includes/doc/libsrbox')
	# cls = plugins.load_cls(u'../boks/opensesame/boks',
	# 	u'libboks', u'libboks')
	# createDoc(cls, u'content/_includes/doc/libboks')
	# for widget in ['button', 'checkbox', 'image', 'image_button', 'label',
	# 	'rating_scale', 'text_input', 'form']:
	# 	cls = plugins.load_cls(u'../opensesame/libopensesame/widgets',
	# 		widget, '_%s' % widget)
	# 	createDoc(cls, u'content/_includes/doc/%s' % widget)
	# createDoc(experiment, u'content/_includes/doc/experiment')
	# createDoc(inline_script, u'content/_includes/doc/inline_script')
