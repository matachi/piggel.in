#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Jonsson'
SITENAME = 'Piggel.in'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['static']
USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'pelican-piggelin'
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DIRECT_TEMPLATES = ['index', 'authors', 'archives']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
