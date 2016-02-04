# -*- coding: utf-8 -*-

"""アカウント: ビュー"""

from __future__ import absolute_import, division, print_function, unicode_literals
import logging
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView

logger = logging.getLogger(__name__)

REDIRECT_FIELD_NAME = 'next'


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
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
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(LoginView, self).get_context_data(**kwargs)
        kwargs[REDIRECT_FIELD_NAME] = self.request.GET.get(REDIRECT_FIELD_NAME, '')
        return kwargs


class LogoutView(RedirectView):
    permanent = False
    url = settings.LOGIN_REDIRECT_URL

    def dispatch(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).dispatch(*args, **kwargs)
