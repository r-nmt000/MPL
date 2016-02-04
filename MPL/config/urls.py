# -*- coding: utf-8 -*-

"""URL設定"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from apps.accounts import urls as accounts_urls
from core import urls as core_urls

urlpatterns = [
    # Core
    url(r'^', include(core_urls, namespace='core')),

    # Admin
    url(r'^admin/', admin.site.urls),

    # アプリケーション
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
]
