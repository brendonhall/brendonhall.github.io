#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brendon Hall'
SITENAME = u"Brendon Hall"
SITESUBTITLE = "Geology, Python & Machine Learning"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'#/index.html'


DEFAULT_PAGINATION = False

THEME = './theme/'

# Theme related config
THEME_COLOR = 'blue'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi quae hic dicta eius ad quam eligendi minima praesentium voluptatum? Quidem quaerat eaque libero velit impedit dicta, repudiandae sapiente. Deserunt, excepturi."

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
# PLUGINS = [
#     'summary',       # auto-summarizing articles
#     'feed_summary',  # use summaries for RSS, not full articles
#     'ipynb.liquid',  # for embedding notebooks
#     'liquid_tags.img',  # embedding images
#     'liquid_tags.video',  # embedding videos
#     'liquid_tags.include_code',  # including code blocks
#     'liquid_tags.literal'
# ]
PLUGINS = [
    'summary',
    'ipynb.liquid',  # for embedding notebooks
]
IGNORE_FILES = ['.ipynb_checkpoints', '.DS_Store']

# for liquid tags
NOTEBOOK_DIR = 'downloads/notebooks'  

ABOUT_PAGE = '/pages/about.html'

DEFAULT_HEADER_BG = '/images/bg-test.jpg'
TWITTER_USERNAME = 'brendonhall'
GITHUB_USERNAME = 'brendonhall'

ENABLE_MATHJAX = True
STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']  
SHOW_ARCHIVES = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
