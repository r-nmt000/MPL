# -*- coding: utf-8 -*-

"""
アプリケーション設定(基本)

このファイルに関する詳細は下記参照
https://docs.djangoproject.com/en/1.9/topics/settings/

各設定及び設定値の詳細は下記参照
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from os.path import abspath, dirname, join, normpath


########## パス設定
# configディレクトリ
CONFIG_ROOT = dirname(dirname(abspath(__file__)))

# プロジェクトディレクトリ
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Djangoディレクトリ
DJANGO_ROOT = dirname(PROJECT_ROOT)


########## アプリケーション設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#installed-apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ()

PROJECT_APPS = (
    'core',
    'apps.accounts',
    'apps.mpl',
)

EXTENSION_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS


########## ミドルウェア設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


########## デバッグ設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = False


########## 秘密鍵設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#secret-key
SECRET_KEY = '$per=gqrn!jd6wa^_bb(xaedja5g&y(b0a(%wo@=v_h5(dgbij'


########## フィクスチャ設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#fixture-dirs
FIXTURE_DIRS = (
    normpath(join(PROJECT_ROOT, 'fixtures'))
)


########## パスワード検証設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


########## 国際化
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = 'Asia/Tokyo'

# https://docs.djangoproject.com/en/1.9/ref/settings/#language-code
LANGUAGE_CODE = 'ja'

# https://docs.djangoproject.com/en/1.9/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.9/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/1.9/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/1.9/ref/settings/#languages
from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('ja', _('Japanese'))
]

# https://docs.djangoproject.com/en/1.9/ref/settings/#locale-paths
LOCALE_PATHS = [
    normpath(join(PROJECT_ROOT, 'locale'))
]


########## テンプレート設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(PROJECT_ROOT, 'templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]


########## Media設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# https://docs.djangoproject.com/en/1.9/ref/settings/#media-url
MEDIA_URL = '/media/'


########## Staticファイル設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#static-root
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'public'))

# https://docs.djangoproject.com/en/1.9/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.9/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = (
    normpath(join(PROJECT_ROOT, 'static')),
)


########## URL設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'



# https://docs.djangoproject.com/en/1.9/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'



########## WSGI設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'


########## ユーザモデル設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'accounts.User'


########## ロギング設定
# https://docs.djangoproject.com/en/1.9/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)-8s %(name)-30s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_app': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': join(DJANGO_ROOT, 'logs/application.log'),
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
            'formatter': 'simple',
        },
        'file_sql': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': join(DJANGO_ROOT, 'logs/sql.log'),
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
            'formatter': 'simple',
        },
    },
}
