# -*- coding: utf-8 -*-

"""共通: URL設定"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.HomeListView.as_view(), name='home'),
]
