# -*- coding: utf-8 -*-

"""共通: ミックスイン"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class LoginAndPermissionRequiredMixin(LoginRequiredMixin, PermissionRequiredMixin):
    pass
