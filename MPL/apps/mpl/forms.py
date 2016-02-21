# -*- coding: utf-8 -*-

"""MPL: フォーム"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _


class MPLForm(forms.Form):
    editor = forms.CharField(widget=forms.Textarea(attrs={'id': 'input', 'class': 'form-control', 'placeholder': 'Moan here'}))
    message = _('morn here')
