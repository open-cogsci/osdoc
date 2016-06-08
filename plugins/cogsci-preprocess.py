# encoding=utf-8

import os
import re
import sys
import yaml
from yamldoc._yaml import orderedLoad
from pelican import signals
from pelican.readers import MarkdownReader
from markdown import Markdown
from markdown.extensions.toc import TocExtension
from academicmarkdown import build, HTMLFilter
if 'publishconf.py' in sys.argv:
	from publishconf import *
else:
	from pelicanconf import *

ITEM_TYPES = [
	'SKETCHPAD', 'FEEDBACK', 'SEQUENCE', 'LOOP', 'SAMPLER', 'SYNTH', 'LOGGER',
	'INLINE_SCRIPT', 'RESET_FEEDBACK', 'COROUTINES', 'KEYBOARD_RESPONSE',
	'MOUSE_RESPONSE', 'JOYSTICK', 'SRBOX'
	]

root = os.path.dirname(os.path.dirname(__file__)) + '/content'

with open('constants.yaml') as f:
	const = yaml.load(f)

links = {}

class AcademicMarkdownReader(MarkdownReader):

	enabled = True

	def read(self, source_path):

		"""Parse content and metadata of markdown files"""

		self._source_path = source_path
		self._md = Markdown(
			extensions=self.extensions + [TocExtension(title='Overview')],
			extpeension_configs=self.extensions)
		img_path = os.path.dirname(source_path) + '/img/' \
			+ os.path.basename(source_path)[:-3]
		lst_path = os.path.dirname(source_path) + '/lst/' \
			+ os.path.basename(source_path)[:-3]
		tbl_path = os.path.dirname(source_path) + '/tbl/' \
			+ os.path.basename(source_path)[:-3]
		build.path = [img_path, lst_path, tbl_path] + build.path
		with open(source_path) as fd:
			text = fd.read().decode('utf-8')
			text = build.MD(text)
			# Process internal links
			for m in re.finditer('%link:(?P<link>[\w/-]+)%', text):
				full = m.group(0)
				link = m.group('link')
				print(link, full)
				if link not in links:
					raise Exception(u'%s not a key in %s' % (link, links))
				text = text.replace(full, '<%s/%s.html>' % (SITEURL, links[link]))
			text = text.replace(root, u'')
			text = HTMLFilter.DOI(text)
			content = self._md.convert(text)
			for var, val in const.items():
				content = content.replace(u'$%s$' % var, str(val))
			for item_type in ITEM_TYPES:
				content = content.replace(item_type,
					u'<span class="item-type">%s</span>' % item_type.lower())
		metadata = self._parse_metadata(self._md.Meta)
		build.path = build.path[3:]
		return content, metadata

def init_academicmarkdown(sender):

	build.postMarkdownFilters = []
	build.figureTemplate = 'jekyll'
	build.figureSourcePrefix = SITEURL
	build.path += u'include'
	build.extensions.remove('toc')
	build.extensions.insert(0, 'toc')
	with open('sitemap.yaml') as f:
		d = orderedLoad(f)
	process_links(d)

def isseparator(pagename):

	for ch in pagename:
		if ch != '_':
			return False
	return True

def process_links(d):

	for pagename, entry in d.items():
		if isseparator(pagename) or entry is None:
			continue
		if isinstance(entry, dict):
			process_links(entry)
			continue
		name = entry.split('/')[-1]
		if not name.strip():
			continue
		links[entry] = entry
		links[name] = entry

def add_reader(readers):

	readers.reader_classes['md'] = AcademicMarkdownReader


def register():

	signals.readers_init.connect(add_reader)
	signals.initialized.connect(init_academicmarkdown)
