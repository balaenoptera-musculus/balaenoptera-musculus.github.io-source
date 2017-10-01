#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'balaenoptera-musculs'
SITENAME = 'くじらメモ'
SITEURL = 'https://balaenoptera-musculus.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'Japanese'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
PLUGIN_PATHS = ['../pelican-plugins']
THEME = '../pelican-themes/pelican-bootstrap3'
PLUGINS = ['i18n_subsites', 'sitemap']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# I18N_TEMPLATES_LANG = 'ja'
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/balaenoptera_1'),
          ('Github', 'https://github.com/balaenoptera-musculus'),)

DEFAULT_PAGINATION = 10
GOOGLE_ANALYTICS = ""#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
