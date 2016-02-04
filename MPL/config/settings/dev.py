# -*- coding: utf-8 -*-

"""
アプリケーション設定(開発環境)

このファイルに関する詳細は下記参照
https://docs.djangoproject.com/en/1.9/topics/settings/

各設定及び設定値の詳細は下記参照
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from config.settings.base import *  # noqa


########## デバッグ設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = True


########## データベース設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DJANGO_ROOT, 'db.sqlite3'),
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': 5432,
    #     'ATOMIC_REQUESTS': True,
    # }
}


########## アプリケーション設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#installed-apps
INSTALLED_APPS += (
    'debug_toolbar',
)


########## ロギング設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#logging
LOGGING['loggers'] = {
    'django.request': {
        'handlers': ['file_app'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'django.db.backends': {
        'handlers': ['file_sql'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'django.template': {
        'handlers': ['file_app'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'core': {
        'handlers': ['console', 'file_app'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'apps': {
        'handlers': ['console', 'file_app'],
        'level': 'DEBUG',
        'propagate': False,
    },
}
