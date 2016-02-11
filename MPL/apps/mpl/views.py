# -*- coding: utf-8 -*-

"""MPL: ビュー"""

from __future__ import absolute_import, division, print_function, unicode_literals
import logging
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import FormView
from apps.mpl.forms import MPLForm

logger = logging.getLogger(__name__)

REDIRECT_FIELD_NAME = 'next'


class MPLView(FormView):
    form_class = MPLForm
    template_name = 'index.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(output='aaa'))
