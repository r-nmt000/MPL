# -*- coding: utf-8 -*-

"""アカウント: URL設定"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.conf.urls import url
from apps.accounts import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
]
