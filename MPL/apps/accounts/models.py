# -*- coding: utf-8 -*-

"""アカウント: モデル"""

from __future__ import absolute_import, division, print_function, unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from core.models import TimeStampedModel


class UserManager(BaseUserManager):
    def create_user(self, name, password=None):
        if not name:
            raise ValueError('Users must have an name')
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.create_user(name, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampedModel):
    name = models.CharField(unique=True, max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'name'
