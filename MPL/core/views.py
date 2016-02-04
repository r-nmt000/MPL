# -*- coding: utf-8 -*-

"""共通: ビュー"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.views.generic import TemplateView


class HomeListView(TemplateView):
    template_name = 'core/home.html'
