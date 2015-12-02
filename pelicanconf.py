#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from collections import OrderedDict

from baseconf import *

# Configurações Base
SITENAME = 'APyB'
AUTHOR = 'APyB'
THEME = 'themes/apyb'

# Referências à Github
GITHUB_REPO = 'https://github.com/pythonbrasil/apyb'
GITHUB_BRANCH = 'pelican'

# Referencia ao Google Groups
GOOGLE_GROUPS_MAIL_LIST_NAME = 'python-brasil'

# Imagens
ARTICLE_BANNERS_FOLDER = 'images/banners'

# Home settings
WELCOME_TITLE = 'Associação Python Brasil'
WELCOME_TEXT = 'A APyB tem como objetivo promover e apoiar iniciativas da comunidade Python no Brasil, empoderando a comunidade sem se apropriar da mesma.'
FOOTER_ABOUT = 'A Associação Python Brasil (APyB) é uma organização sem fins lucrativos com a meta de apoiar as comunidades relacionadas à linguagem Python e suas tecnologias derivadas.'

# Tema do Syntax Hightlight
PYGMENTS_STYLE = 'perldoc'

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        'title': 'Sobre',
        'href': 'sobre',
    },
    {
        'title': 'Associe-se',
        'href': 'associe-se',
    },
    {
        'title': 'Comunidade',
        'href': 'comunidade',
    },
    {
        'title': 'Eventos',
        'href': 'eventos',
    },
    {
        'title': 'Conferência Python Brasil',
        'href': 'python-brasil',
    },
    {
        'title': 'Patrocínio',
        'href': 'patrocinio',
    },
]

# Links sociais do rodapé
SOCIAL_LINKS = (
    {
        'href': 'https://github.com/pythonbrasil',
        'icon': 'fa-github',
        'text': 'GitHub',
    },
    {
        'href': 'https://twitter.com/pythonbrasil',
        'icon': 'fa-twitter',
        'text': 'Twitter',
    },
    {
        'href': 'https://www.facebook.com/groups/python.brasil',
        'icon': 'fa-facebook',
        'text': 'Facebook',
    },
    {
        'href': 'https://groups.google.com/forum/#!forum/python-brasil',
        'icon': 'fa-users',
        'text': 'Lista de emails',
    },
)