# encoding=utf-8

import os
import yaml
from pelican import signals
from pelican.readers import MarkdownReader
from markdown import Markdown
from markdown.extensions.toc import TocExtension
from academicmarkdown import build, HTMLFilter

root = os.path.dirname(os.path.dirname(__file__)) + '/content'

with open('constants.yaml') as f:
	const = yaml.load(f)

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
		build.path += [img_path, lst_path, tbl_path]
		with open(source_path) as fd:
			text = fd.read().decode('utf-8')
			text = build.MD(text)
			text = text.replace(root, u'')
			text = HTMLFilter.DOI(text)
			content = self._md.convert(text)
			for var, val in const.items():
				content = content.replace(u'$%s$' % var, str(val))
		metadata = self._parse_metadata(self._md.Meta)
		build.path = build.path[:-2]
		return content, metadata

def init_academicmarkdown(sender):

	build.postMarkdownFilters = []
	build.figureTemplate = 'jekyll'
	build.path += u'include'
	build.extensions.remove('toc')
	build.extensions.insert(0, 'toc')

def add_reader(readers):

	readers.reader_classes['md'] = AcademicMarkdownReader

# This is how pelican works.
def register():

	signals.readers_init.connect(add_reader)
	signals.initialized.connect(init_academicmarkdown)
