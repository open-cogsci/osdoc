#!/usr/bin/env python3
# coding=utf-8

from collections import OrderedDict
from yamldoc._yaml import orderedLoad
import yaml
import sys

if '--publish' in sys.argv:
	import publishconf as conf
else:
	import pelicanconf as conf

ROOT = conf.SITEURL
SUFFIX = '.html'

def isseparator(pagename):

	for ch in pagename:
		if ch != '_':
			return False
	return True


def build_menu(d):

	l = []
	for pagename, entry in d.items():
		if isseparator(pagename):
			l.append('<li><hr /></li>')
			continue
		if entry is None:
			l.append('<li class="cogsci-menuitem-header">%s</li>' % pagename)
			continue
		if isinstance(entry, dict):
			l.append(
				('<li><a href="#" class="dropdown-toggle" data-toggle="dropdown">'
				'%s<b class="caret"></b></a>') \
				% pagename)
			l.append('<ul class="dropdown-menu">')
			l.append(build_menu(entry))
			l.append('</ul></li>')
			continue
		if entry.startswith('http'):
			l.append('<li><a href="%s">%s</a></li>' % (entry, pagename))
		else:
			l.append('<li><a href="%s/%s%s">%s</a></li>' \
				% (ROOT, entry, SUFFIX, pagename))
	return '\n'.join(l)


def build_live_sitemap(d):

	sitemap = OrderedDict()
	for pagename, entry in d.items():
		if isseparator(pagename) or entry is None:
			continue
		if isinstance(entry, dict):
			sitemap[pagename] = build_live_sitemap(entry)
			continue
		if entry.startswith('http'):
			sitemap[pagename] = entry
		else:
			sitemap[pagename] = '/' + conf.BRANCH + '/' + entry + SUFFIX
	return sitemap


def main():

	with open('sitemap.yaml') as f:
		d = orderedLoad(f)
	with open('themes/cogsci/templates/menu-content.html', 'w') as f:
		f.write(build_menu(d))
	print('Generated menu content')
	sitemap = build_live_sitemap(d)
	with open(u'static/sitemap.yml', u'w') as fd:
		yaml.dump(sitemap, fd, default_flow_style=False)
	print('Generated live sitemap')

if __name__ == '__main__':
	main()
