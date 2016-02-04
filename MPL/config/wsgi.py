# -*- coding: utf-8 -*-

"""WSGI設定"""

from __future__ import absolute_import, division, print_function, unicode_literals
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
application = get_wsgi_application()
