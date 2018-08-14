# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from passapp.models import UserProfileInfo

admin.site.register(UserProfileInfo)
