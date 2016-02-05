# -*- coding: utf-8 -*-

"""MPL: ビュー"""

from __future__ import absolute_import, division, print_function, unicode_literals
import logging
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import FormView
from apps.mpl.forms import MPLForm

logger = logging.getLogger(__name__)

REDIRECT_FIELD_NAME = 'next'


class MPLView(FormView):
    form_class = MPLForm
    template_name = 'index.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def get_success_url(self):
        redirect_to = self.request.POST.get(REDIRECT_FIELD_NAME,
                                            self.request.GET.get(REDIRECT_FIELD_NAME, ''))
        if not redirect_to:
            return self.success_url
        return redirect_to

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(MPLView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(MPLView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(MPLView, self).get_context_data(**kwargs)
        kwargs[REDIRECT_FIELD_NAME] = self.request.GET.get(REDIRECT_FIELD_NAME, '')
        return kwargs


