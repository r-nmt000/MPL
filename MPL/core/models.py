# -*- coding: utf-8 -*-

"""共通: モデル"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
