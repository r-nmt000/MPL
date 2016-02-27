# -*- coding: utf-8 -*-

"""URL設定"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf.urls import include, url
from apps.mpl import urls as mpl_urls

urlpatterns = [
    # アプリケーション
    url(r'^', include(mpl_urls, namespace='mpl')),
]
