#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["cogsci-preprocess", "page_hierarchy"]
LOCALE = 'en_US'

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','headerid']

AUTHOR = u'Sebastiaan Math\xf4t'
SITENAME = u'Cogsci.nl'
STATIC_PATHS = ['pages']

PATH = 'content'
THEME=  'themes/cogsci'
TIMEZONE = 'Europe/Paris'
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
SLUGIFY_SOURCE = 'basename'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 250

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
