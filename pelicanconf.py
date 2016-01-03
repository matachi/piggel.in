#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Jonsson'
SITENAME = 'Piggel.in'
SITEURL = 'http://localhost:8000'

PATH = 'content'
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

I18N_SUBSITES = {
    'sv': {
        'MENUITEMS': [
            ('Arkiv', '/sv/archives.html'),
        ]
    }
}
I18N_UNTRANSLATED_ARTICLES = 'remove'
I18N_UNTRANSLATED_PAGES = 'remove'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'pelican-piggelin/dist'
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DIRECT_TEMPLATES = ['index', 'authors', 'archives']

MENUITEMS = [
    ('Articles', '/archives.html'),
]

languages_lookup = {
    'en': 'English',
    'sv': 'Swedish',
}

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
