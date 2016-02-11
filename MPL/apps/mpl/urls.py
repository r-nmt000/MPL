# -*- coding: utf-8 -*-

"""MPL: URL設定"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf.urls import url
from apps.mpl import views

urlpatterns = [
    url(r'$', views.MPLView.as_view(), name='main')
]

