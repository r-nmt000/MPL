# -*- coding: utf-8 -*-

"""MPL: フォーム"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _


class MPLForm(forms.Form):
    editor = forms.CharField()
    message = _('morn here')
