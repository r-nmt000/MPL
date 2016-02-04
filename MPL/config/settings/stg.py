# -*- coding: utf-8 -*-

"""
アプリケーション設定(ステージング環境)

このファイルに関する詳細は下記参照
https://docs.djangoproject.com/en/1.9/topics/settings/

各設定及び設定値の詳細は下記参照
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import, division, print_function, unicode_literals
import os
from config.settings.base import *  # noqa


########## ホスト設定
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


########## データベース設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': 5432,
        'ATOMIC_REQUESTS': True,
    }
}


########## 秘密鍵設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#secret-key
SECRET_KEY = os.environ['SECRET_KEY']


########## ロギング
# https://docs.djangoproject.com/en/1.9/ref/settings/#logging
LOGGING['loggers'] = {
    'django.request': {
        'handlers': ['file_app'],
        'level': 'ERROR',
        'propagate': False,
    },
    'core': {
        'handlers': ['file_app'],
        'level': 'INFO',
    },
    'apps': {
        'handlers': ['file_app'],
        'level': 'INFO',
    },
}
