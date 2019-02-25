# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.db import models



class Bookmark(models.Model):
    title = models.CharField(max_length=100 , blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title

