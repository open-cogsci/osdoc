# coding=utf-8

from __future__ import unicode_literals
import sys, os
sys.path.append(os.path.dirname(__file__))
from baseconf import *

SITEURL = 'http://localhost:8000/' + BRANCH
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.debug']
}
TEMPLATE_DEBUG = True
